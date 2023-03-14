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
def get_direct_connect_url(useCdn, cdnUrl, host, port, locked, password=None):
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
