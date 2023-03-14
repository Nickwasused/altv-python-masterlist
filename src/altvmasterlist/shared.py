from dataclasses import dataclass
from json import dumps, loads
from io import StringIO
import requests
import logging
import secrets

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)


@dataclass
class MasterlistUrls:
    base_link: str = "https://api.altv.mp"
    all_server_stats_link: str = f"{base_link}/servers"
    all_servers_link: str = f"{base_link}/servers/list"
    server_link: str = f"{base_link}/server" + "/{}"
    server_average_link: str = f"{base_link}/avg" + "/{}/{}"
    server_max_link: str = f"{base_link}/max" + "/{}/{}"


@dataclass
class AltstatsUrls:
    base_link: str = "https://api.altstats.net/api/v1/"
    all_server_stats_link: str = f"{base_link}/master"
    all_servers_link: str = f"{base_link}/server"
    server_link: str = f"{base_link}/server/" + "{}"


@dataclass
class RequestHeaders:
    """Common headers"""
    host: str = "",
    user_agent: str = 'AltPublicAgent',
    accept: str = '*/*',
    alt_debug: str = 'false',
    alt_password: str = '17241709254077376921',
    alt_branch: str = "",
    alt_version: str = "",
    alt_player_name: str = secrets.token_urlsafe(10),
    alt_social_id: str = secrets.token_hex(9),
    alt_hardware_id2: str = secrets.token_hex(19),
    alt_hardware_id: str = secrets.token_hex(19)

    def __init__(self, version, debug="false", branch="release"):
        self.alt_branch = branch
        self.alt_version = version
        self.alt_debug = debug

    def __repr__(self):
        return dumps({
            'host': self.host,
            'user-agent': self.user_agent,
            "accept": self.accept,
            'alt-debug': self.alt_debug,
            'alt-password': self.alt_password,
            'alt-branch': self.alt_branch,
            'alt-version': self.alt_version,
            'alt-player-name': self.alt_player_name,
            'alt-social-id': self.alt_social_id,
            'alt-hardware-id2': self.alt_hardware_id2,
            'alt-hardware-id': self.alt_hardware_id
        })


# custom request function
def request(url, cdn=False, server=None):
    # Use the User-Agent: AltPublicAgent, because some servers protect their CDN with
    # a simple User-Agent check e.g. https://luckyv.de does that
    if "http://" in url and cdn:
        req_headers = RequestHeaders(server.version, server.branch)
    else:
        req_headers = {
            'User-Agent': 'AltPublicAgent',
            'content-type': 'application/json; charset=utf-8'
        }

    try:
        api_data = requests.get(url, headers=req_headers, timeout=60)

        if api_data.status_code != 200:
            logging.warning(f"the request returned nothing.")
            return None
        else:
            return loads(api_data.content.decode("utf-8", errors='ignore'))
    except Exception as e:
        logging.error(e)
        return None


# get the "Direct Connect Protocol" url
# e.g. altv://connect/127.0.0.1:7788?password=xyz
# https://docs.altv.mp/articles/connectprotocol.html
# cdn off: altv://connect/${IP_ADDRESS}:${PORT}?password=${PASSWORD}
# cdn on: altv://connect/{CDN_URL}?password=${PASSWORD}
def get_dtc_url(useCdn, cdnUrl, host, port, locked, password=None):
    dtc_url = StringIO()
    if useCdn:
        if not "http" in cdnUrl:
            dtc_url.write(f"altv://connect/http://{cdnUrl}")
        else:
            dtc_url.write(f"altv://connect/{cdnUrl}")
    else:
        dtc_url.write(f"altv://connect/{host}:{port}")

    if locked and password is None:
        logging.warning(
            "Your server is password protected but you did not supply a password for the Direct Connect Url.")

    if password is not None:
        dtc_url.write(f"?password={password}")

    return dtc_url.getvalue()


# use this function to fetch the server connect json
# this file has every resource of the server with a hash and name
def fetch_connect_json(useCdn: bool, locked: bool, active: bool, host: str, port: int, cdnUrl: str):
    if not useCdn and not locked and active:
        # This Server is not using a CDN.
        cdn_request = request(f"http://{host}:{port}/connect.json", True)
        if cdn_request is None:
            # possible server error or blocked by alt:V
            return None
        else:
            return cdn_request
    else:
        # let`s try to get the connect.json
        cdn_request = request(f"{cdnUrl}/connect.json")
        if cdn_request is None:
            # maybe the CDN is offline
            return None
        else:
            return cdn_request


# fetch the required and optional permissions of the server
# available permissions:
# Screen Capture: This allows a screenshot to be taken of the alt:V process (just GTA) and any webview
# WebRTC: This allows peer-to-peer RTC inside JS
# Clipboard Access: This allows to copy content to users clipboard
def get_permissions(connect_json):
    permissions = {
        "required": {
            "Screen Capture": False,
            "WebRTC": False,
            "Clipboard Access": False
        },
        "optional": {
            "Screen Capture": False,
            "WebRTC": False,
            "Clipboard Access": False
        }
    }

    if connect_json is None:
        return None
    optional = connect_json["optional-permissions"]
    required = connect_json["required-permissions"]

    if optional is not []:
        for permission in optional:
            permissions["optional"][permission] = True

    if required is not []:
        for permission in required:
            permissions["required"][permission] = True

    return permissions


def get_resource_size(useCdn, cdnUrl, resource, host, port, decimal):
    if useCdn:
        resource_url = f"{cdnUrl}/{resource}.resource"
    else:
        resource_url = f"http://{host}:{port}/{resource}.resource"

    data = requests.head(resource_url, headers={"User-Agent": "AltPublicAgent"}, timeout=60)

    if data.ok:
        return round((int(data.headers["Content-Length"]) / 1048576), decimal)
    else:
        return None