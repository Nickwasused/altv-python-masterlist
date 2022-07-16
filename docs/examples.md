# Examples

## Get a alt:V Server object

```
import altvmasterlist as altv

# get the server json
server = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2")

if (server == None):
    print("Error while getting Server")
    sys.exit()
```

## Get a alt:V Server object and update it

```
import altvmasterlist as altv
from time import sleep

# get the server json
server = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2")

if (server == None):
    print("Error while getting Server")
    sys.exit()

print(server.players)

# wait 10 seconds
sleep(10)

server.update()
print(server.players)
```

## Get a alt:V Server connect.json

```
import altvmasterlist as altv

# get the server json
server = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2")

if (server == None):
    print("Error while getting Server")
    sys.exit()

connect_json = server.fetchconnectjson()
if (connect_json != Null):
    print(connect_json)
```

## Get all alt:V Servers that are active

```
import altvmasterlist as altv

servers = altv.get_servers()

# update the first server
servers[0].update()

for server in servers:
    print(server.players)
```