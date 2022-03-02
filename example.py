from altvmasterlist import masterlist as altv
import time

# get the server json
altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2").get_json()

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