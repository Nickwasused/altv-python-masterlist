from altvmasterlist import masterlist as altv
import logging 
import time

logging.basicConfig(level=logging.DEBUG)
logging.getLogger().setLevel(logging.DEBUG)

# Valid id
print(altv.validate_id("bb7228a0d366fc575a5682a99359424f"))

# Invalid id
print(altv.validate_id("abcdefghijklmnop123"))

# get the server json
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.get_json())

print(server.fetch_connect_json())

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get the connect.json
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.fetch_connect_json())

# get server with update
server = altv.get_server_by_id("bb7228a0d366fc575a5682a99359424f")
print(server.lastUpdate)
time.sleep(120)
server.update()
print(server.lastUpdate)