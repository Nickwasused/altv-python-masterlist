# alt:V Masterlist for Python

You can use this Package to interface with the alt:V master list API.

# Install 

```pip install altvmasterlist``` or ```pip3 install altvmasterlist```

# Examples

```
import altvmasterlist as altv

# get the server json
altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2").get_json()

# get all servers as server object
altv.get_servers()

# get all server stats
altv.get_server_stats()

# get a server and read stuff
server = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2")
print(server.players) 
This should output something like 200
```