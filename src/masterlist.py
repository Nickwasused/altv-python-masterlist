#!/usr/bin/env python3
from dataclasses import dataclass
from re import compile
import src.shared as shared
import requests
import logging
import sys

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)


# Masterlist API Docs: https://docs.altv.mp/articles/master_list_api.html


logging.debug(f'starting with base link: {shared.MasterlistUrls.base_link}')


# This is the server object
@dataclass
class Server:
    id: int
    active: bool = False
    maxPlayers: int = 0
    players: int = 0
    name: str = ""
    locked: bool = False
    host: str = ""
    port: int = 0
    gameMode: str = ""
    website: str = ""
    language: str = ""
    description: str = ""
    verified: bool = False
    promoted: bool = False
    useEarlyAuth: bool = False
    earlyAuthUrl: str = ""
    useCdn: bool = False
    cdnUrl: str = ""
    useVoiceChat: bool = False
    tags: list[str] = None
    bannerUrl: str = ""
    branch: str = ""
    build: str = ""
    version: float = 0.0
    lastUpdate: int = 0

    # initialize the object with all values that are available in the alt:V masterlist API
    def __init__(self, id):
        self.id = id
        temp_data = shared.request(shared.MasterlistUrls.server_link.format(self.id))
        if temp_data is None or temp_data == {} or not temp_data["active"]:
            # the api returned no data or the server is offline
            pass
        else:
            self.active = temp_data["active"]
            self.maxPlayers = temp_data["info"]["maxPlayers"]
            self.players = temp_data["info"]["players"]
            self.name = temp_data["info"]["name"]
            self.locked = temp_data["info"]["locked"]
            self.host = temp_data["info"]["host"]
            self.port = temp_data["info"]["port"]
            self.gameMode = temp_data["info"]["gameMode"]
            self.website = temp_data["info"]["website"]
            self.language = temp_data["info"]["language"]
            self.description = temp_data["info"]["description"]
            self.verified = temp_data["info"]["verified"]
            self.promoted = temp_data["info"]["promoted"]
            self.useEarlyAuth = temp_data["info"]["useEarlyAuth"]
            self.earlyAuthUrl = temp_data["info"]["earlyAuthUrl"]
            self.useCdn = temp_data["info"]["useCdn"]
            self.cdnUrl = temp_data["info"]["cdnUrl"]
            self.useVoiceChat = temp_data["info"]["useVoiceChat"]
            self.tags = temp_data["info"]["tags"]
            self.bannerUrl = temp_data["info"]["bannerUrl"]
            self.branch = temp_data["info"]["branch"]
            self.build = temp_data["info"]["build"]
            self.version = temp_data["info"]["version"]
            self.lastUpdate = temp_data["info"]["lastUpdate"]

    # fetch the server data and replace it
    def update(self):
        temp_server = get_server_by_id(self.id)

        # check if the server is returned
        if temp_server is None:
            # don`t update the server object because the API returned invalid, broken, or no data
            logging.warning(f"the alt:V API returned nothing.")
            return

        # check if the server is online
        if temp_server.active:
            # these values are only available when the server is online
            self.active = temp_server.active
            self.maxPlayers = temp_server.maxPlayers
            self.players = temp_server.players
            self.name = temp_server.name
            self.locked = temp_server.locked
            self.host = temp_server.host
            self.port = temp_server.port
            self.gameMode = temp_server.gameMode
            self.website = temp_server.website
            self.language = temp_server.language
            self.description = temp_server.description
            self.verified = temp_server.verified
            self.promoted = temp_server.promoted
            self.useEarlyAuth = temp_server.useEarlyAuth
            self.earlyAuthUrl = temp_server.earlyAuthUrl
            self.useCdn = temp_server.useCdn
            self.cdnUrl = temp_server.cdnUrl
            self.useVoiceChat = temp_server.useVoiceChat
            self.tags = temp_server.tags
            self.bannerUrl = temp_server.bannerUrl
            self.branch = temp_server.branch
            self.build = temp_server.build
            self.version = temp_server.version
            self.lastUpdate = temp_server.lastUpdate
        else:
            # set the server to be offline and the players to 0, because the server is offline
            self.active = False
            self.players = 0

    # use this function to fetch the server connect json
    # this file has every resource of the server with a hash and name
    def fetch_connect_json(self):
        return shared.get_connect_json(self.useCdn, self.locked, self.active, self.host, self.port, self.cdnUrl)

    def get_dtc_url(self, password=None):
        return shared.get_direct_connect_url(self.useCdn, self.cdnUrl, self.host, self.port, self.locked, password)

    # fetch the required and optional permissions of the server
    # available permissions:
    # Screen Capture: This allows a screenshot to be taken of the alt:V process (just GTA) and any webview
    # WebRTC: This allows peer-to-peer RTC inside JS
    # Clipboard Access: This allows to copy content to users clipboard
    def get_permissions(self):
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

        # fetch connect json
        data = self.fetch_connect_json()
        if data is None:
            return None
        optional = data["optional-permissions"]
        required = data["required-permissions"]

        if optional is not []:
            for permission in optional:
                permissions["optional"][permission] = True

        if required is not []:
            for permission in required:
                permissions["required"][permission] = True

        return permissions

    def get_resource_size(self, resource, decimal=2):
        if self.useCdn:
            resource_url = f"{self.cdnUrl}/{resource}.resource"
        else:
            resource_url = f"http://{self.host}:{self.port}/{resource}.resource"

        data = requests.head(resource_url, headers={"User-Agent": "AltPublicAgent"}, timeout=60)

        if data.ok:
            return round((int(data.headers["Content-Length"]) / 1048576), decimal)
        else:
            return None


# Fetch the stats of all servers that are currently online
# e.g. {"serversCount":121,"playersCount":1595}
def get_server_stats():
    data = shared.request(shared.MasterlistUrls.all_server_stats_link)
    if data is None:
        return None
    else:
        return data


# Get all Servers that are online as Server object
def get_servers():
    return_servers = []
    servers = shared.request(shared.MasterlistUrls.all_servers_link)
    if servers is None or servers == "{}":
        return None
    else:
        for server in servers:
            # Now change every JSON response to a server object that we can e.g. update it when we want
            temp_server = Server("unknown", server["id"], server["maxPlayers"], server["players"], server["name"],
                                 server["locked"], server["host"], server["port"], server["gameMode"],
                                 server["website"],
                                 server["language"], server["description"], server["verified"], server["promoted"],
                                 server["useEarlyAuth"], server["earlyAuthUrl"], server["useCdn"], server["cdnUrl"],
                                 server["useVoiceChat"], server["tags"], server["bannerUrl"], server["branch"],
                                 server["build"], server["version"], server["lastUpdate"])
            return_servers.append(temp_server)

        return return_servers


# get a single server by their server id
def get_server_by_id(server_id):
    return Server(server_id)


# get the average player count with a specified time range
# returns a JSON object e.g. [{"t":1652096100,"c":50},{"t":1652096400,"c":52},{"t":1652096700,"c":57}]
# time: 1d, 7d, 31d
def get_server_by_id_avg(server_id, time):
    avg_data = shared.request(shared.MasterlistUrls.server_average_link.format(server_id, time))
    if avg_data is None:
        return None
    else:
        return avg_data


# works like get_server_by_id_avg() but returns a integer/number
# time: 1d, 7d, 31d
def get_server_by_id_avg_result(server_id, time):
    avg_result_response = get_server_by_id_avg(server_id, time)
    if avg_result_response is None:
        return None
    else:
        players_all = 0
        for entry in avg_result_response:
            players_all = players_all + entry["c"]
        result = players_all / len(avg_result_response)
        return round(result)


# get the maximum player count with a specified time range
# returns a JSON object e.g. [{"t":1652096100,"c":50},{"t":1652096400,"c":52},{"t":1652096700,"c":57}]
# time: 1d, 7d, 31d
def get_server_by_id_max(server_id, time):
    max_data = shared.request(shared.MasterlistUrls.server_max_link.format(server_id, time))
    if max_data is None:
        return None
    else:
        return max_data


# validate a given alt:V server id
def validate_id(server_id):
    regex = compile(r"^[\da-zA-Z]{32}$")
    result = regex.match(server_id)
    if result is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    print("This is a Module!")
    sys.exit()
