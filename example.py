from altvmasterlist import masterlist as altv
import time

# get the server json
print(altv.get_server_by_id("6715009029d9a5e5a3383af676d3e601").get_json())

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get the connect.json
server = altv.get_server_by_id("6715009029d9a5e5a3383af676d3e601")
print(server.fetchconnectjson())

# get server with update
server = altv.get_server_by_id("6715009029d9a5e5a3383af676d3e601")
print(server.lastUpdate)
time.sleep(120)
server.update()
print(server.lastUpdate)