import altvmasterlist as altv

# get the server json
altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2").get_json()

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()