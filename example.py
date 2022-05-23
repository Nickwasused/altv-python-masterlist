from altvmasterlist import masterlist as altv
import logging 
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# get the server json
print(altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f").get_json())

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get the connect.json
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.fetchconnectjson())

# get server with update
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.lastUpdate)
time.sleep(120)
server.update()
print(server.lastUpdate)