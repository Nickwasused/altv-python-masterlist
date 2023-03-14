# Examples

## Get a alt:V Server object

```python3
import masterlist as altv

# create Server object
server = altv.Server("ceaac3d1cc22761223beac38386f5ab2")

print(server)
```

## Get a alt:V Server object and update it

```python3
from time import sleep
import masterlist as altv

# get the server json
server = altv.Server("ceaac3d1cc22761223beac38386f5ab2")

print(server.players)

# wait 10 seconds
sleep(10)

server.update()
print(server.players)
```

## Get a alt:V Server connect.json

```python3
import masterlist as altv

# get the server json
server = altv.Server("ceaac3d1cc22761223beac38386f5ab2")

connect_json = server.fetch_connect_json()
if connect_json:
    print(connect_json)
```

## Get all alt:V Servers that are active

```python3
import masterlist as altv

servers = altv.get_servers()

# update the first server
servers[0].update()

for server in servers:
    print(server.players)
```

## Get the Direct Connect Url of a Server

```python3
import masterlist as altv

# get the server dtc url with a password
server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server.get_dtc_url(password="test"))

# get the server dtc url without a password
server = altv.Server("bb7228a0d366fc575a5682a99359424f")
print(server.get_dtc_url())
```

## Get the Permissions of a Server

```python3
import masterlist as altv

server = altv.Server("0330ffff0c5e97e277d038a707701024")
permissions = server.get_permissions()
print(permissions)

if permissions["required"]["Screen Capture"]:
    print("The server requires the screen capture permission")
```
