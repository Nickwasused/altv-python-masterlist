#!/usr/bin/env python3
from json import dumps
from re import compile
import src.shared as shared
import requests
import logging
import sys

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)


# Masterlist API Docs: https://docs.altv.mp/articles/master_list_api.html

logging.debug(f'starting with base link: {shared.AltstatsUrls.base_link}')


# This is the server object
class Server:
    # initialize the object with all values that are available in the alt:V masterlist API
    def __init__(self, Id, FoundAt, LastActivity, Visible, ServerId, Players, Name, Locked, Ip, Port, MaxPlayers, Ping,
                 Website, Language, Description, LastUpdate, IsOfficial, PlayerRecord, PlayerRecordDate,
                 LastFetchOnline, LanguageShort, GameMode, Branch, Build, CdnUrl, EarlyAuthUrl, Verified, UseCdn,
                 UseEarlyAuth, BannerUrl, Promoted, Tags, UseVoiceChat, Level, Version):
        self.Id = Id
        self.FoundAt = FoundAt
        self.LastActivity = LastActivity
        self.Visible = Visible
        self.ServerId = ServerId
        self.Players = Players
        self.Name = Name
        self.Locked = Locked
        self.Ip = Ip
        self.Port = Port
        self.MaxPlayers = MaxPlayers
        self.Ping = Ping
        self.Website = Website
        self.Language = Language
        self.Description = Description
        self.LastUpdate = LastUpdate
        self.IsOfficial = IsOfficial
        self.PlayerRecord = PlayerRecord
        self.PlayerRecordDate = PlayerRecordDate
        self.LastFetchOnline = LastFetchOnline
        self.LanguageShort = LanguageShort
        self.GameMode = GameMode
        self.Branch = Branch
        self.Build = Build
        self.CdnUrl = CdnUrl
        self.EarlyAuthUrl = EarlyAuthUrl
        self.Verified = Verified
        self.UseCdn = UseCdn
        self.UseEarlyAuth = UseEarlyAuth
        self.BannerUrl = BannerUrl
        self.Promoted = Promoted
        self.Tags = Tags
        self.UseVoiceChat = UseVoiceChat
        self.Level = Level
        self.Version = Version

    # return the current server data as JSON object
    def get_json(self):
        return {
            "Id": self.Id,
            "FoundAt": self.FoundAt,
            "LastActivity": self.LastActivity,
            "Visible": self.Visible,
            "ServerId": self.ServerId,
            "Players": self.Players,
            "Name": self.Name,
            "Locked": self.Locked,
            "Ip": self.Ip,
            "Port": self.Port,
            "MaxPlayers": self.MaxPlayers,
            "Ping": self.Ping,
            "Website": self.Website,
            "Language": self.Language,
            "Description": self.Description,
            "LastUpdate": self.LastUpdate,
            "IsOfficial": self.IsOfficial,
            "PlayerRecord": self.PlayerRecord,
            "PlayerRecordDate": self.PlayerRecordDate,
            "LastFetchOnline": self.LastFetchOnline,
            "LanguageShort": self.LanguageShort,
            "GameMode": self.GameMode,
            "Branch": self.Branch,
            "Build": self.Build,
            "CdnUrl": self.CdnUrl,
            "EarlyAuthUrl": self.EarlyAuthUrl,
            "Verified": self.Verified,
            "UseCdn": self.UseCdn,
            "UseEarlyAuth": self.UseEarlyAuth,
            "BannerUrl": self.BannerUrl,
            "Promoted": self.Promoted,
            "Tags": self.Tags,
            "UseVoiceChat": self.UseVoiceChat,
            "Level": self.Level,
            "Version": self.Version
        }

    def __repr__(self):
        return self.get_json()

    def __str__(self):
        return dumps(self.__repr__())

    # fetch the server data and replace it
    def update(self):
        temp_server = Server(self.Id)

        # check if the server is returned
        if temp_server is None:
            # don`t update the server object because the API returned invalid, broken, or no data
            logging.warning(f"the alt:V API returned nothing.")
            return

        self.Id = temp_server.Id
        self.FoundAt = temp_server.FoundAt
        self.LastActivity = temp_server.LastActivity
        self.Visible = temp_server.Visible
        self.ServerId = temp_server.ServerId
        self.Players = temp_server.Players
        self.Name = temp_server.Name
        self.Locked = temp_server.Locked
        self.Ip = temp_server.Ip
        self.Port = temp_server.Port
        self.MaxPlayers = temp_server.MaxPlayers
        self.Ping = temp_server.Ping
        self.Website = temp_server.Website
        self.Language = temp_server.Language
        self.Description = temp_server.Description
        self.LastUpdate = temp_server.LastUpdate
        self.IsOfficial = temp_server.IsOfficial
        self.PlayerRecord = temp_server.PlayerRecord
        self.PlayerRecordDate = temp_server.PlayerRecordDate
        self.LastFetchOnline = temp_server.LastFetchOnline
        self.LanguageShort = temp_server.LanguageShort
        self.GameMode = temp_server.GameMode
        self.Branch = temp_server.Branch
        self.Build = temp_server.Build
        self.CdnUrl = temp_server.CdnUrl
        self.EarlyAuthUrl = temp_server.EarlyAuthUrl
        self.Verified = temp_server.Verified
        self.UseCdn = temp_server.UseCdn
        self.UseEarlyAuth = temp_server.UseEarlyAuth
        self.BannerUrl = temp_server.BannerUrl
        self.Promoted = temp_server.Promoted
        self.Tags = temp_server.Tags
        self.UseVoiceChat = temp_server.UseVoiceChat
        self.Level = temp_server.Level
        self.Version = temp_server.Version

    def fetch_connect_json(self):
        return shared.fetch_connect_json(self.UseCdn, self.Locked, True, self.Ip, self.Port, self.CdnUrl)

    def get_dtc_url(self, password=None):
        return shared.get_dtc_url(self.UseCdn, self.CdnUrl, self.Ip, self.Port, self.Locked, password)

    def get_permissions(self):
        return shared.get_permissions(self.fetch_connect_json())

    def get_resource_size(self, resource, decimal=2):
        return shared.get_resource_size(self.UseCdn, self.CdnUrl, resource, self.Ip, self.Port, decimal)


# Fetch the stats of all servers that are currently online
# e.g. [
#   {
#     "ServerCount": 72,
#     "PlayerCount": 958,
#     "TimeStamp": "2021-01-01T12:15:00.464Z"
#   },
#   {
#     "ServerCount": 73,
#     "PlayerCount": 945,
#     "TimeStamp": "2021-01-01T12:10:00.465Z"
#   },
#   {
#     "others": "..."
#   }
# ]
def get_server_stats():
    data = shared.request(shared.AltstatsUrls.all_server_stats_link)
    if data is None:
        return None
    else:
        return data


# Get all Servers that are online as Server object
def get_servers():
    return_servers = []
    servers = shared.request(shared.AltstatsUrls.all_servers_link)
    if servers is None or servers == "{}":
        return None
    else:
        for server in servers:
            # Now change every JSON response to a server object that we can e.g. update it when we want
            temp_server = Server(server["id"], None, None, None,
                                 None, server["playerCount"], server["name"],
                                 bool(server["locked"]), None, None,
                                 server["slots"], None,
                                 None, server["language"]["full"],
                                 None, None,
                                 bool(server["official"]), None, None,
                                 None, server["language"]["short"], server["gameMode"],
                                 None, None, None, None,
                                 bool(server["verified"]), None, None, None,
                                 bool(server["promoted"]), server["tags"], None, None,
                                 None)
            return_servers.append(temp_server)

        return return_servers


# get all servers and calculate the average values
def get_servers_average():
    data = get_server_stats()
    if data is None:
        return None
    start_date = data[-1]["TimeStamp"]
    end_date = data[0]["TimeStamp"]

    server_count_total = 0
    player_count_total = 0

    for entry in data:
        server_count_total += entry["ServerCount"]
        player_count_total += entry["PlayerCount"]

    server_count_avg = round(server_count_total / len(data), 0)
    player_count_avg = round(player_count_total / len(data), 0)

    return start_date, end_date, server_count_avg, player_count_avg


# validate a given alt:V server id
def validate_id(server_id):
    server_id = str(server_id)
    regex = compile(r"^[0-9]{1,}$")
    result = regex.match(server_id)
    if result is not None:
        return True
    else:
        return False


if __name__ == "__main__":
    print("This is a Module!")
    sys.exit()
