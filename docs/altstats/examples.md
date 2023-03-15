# Examples

## Get a alt:V Server object

```python3

from altvmasterlist import altstats as altv

# get the server
server = altv.Server(86)
```

## Get a alt:V Server object and update it

```python3
from time import sleep
from altvmasterlist import altstats as altv

# get the server json
server = altv.Server(86)

print(server.Players)

# wait 10 seconds
sleep(10)

server.update()
print(server.Players)
```

## Get a alt:V Server connect.json

```python3
from altvmasterlist import altstats as altv

# get the server json
server = altv.Server(86)

connect_json = server.connect_json
if connect_json:
    print(connect_json)
```

## Get all alt:V Servers that are active

```python3
from altvmasterlist import altstats as altv

servers = altv.get_servers()

# update the first server
servers[0].update()

for server in servers:
    print(server.Players)
```

## Get the Direct Connect Url of a Server

```python3
from altvmasterlist import altstats as altv


server = altv.Server(86)

# get the server dtc url with a password
print(server.get_dtc_url(password="test"))

# get the server dtc url without a password
print(server.get_dtc_url())
```

## Get the Permissions of a Server

```python3
from altvmasterlist import altstats as altv

server = altv.Server(86)
permissions = server.permissions
print(permissions)

if permissions["required"]["Screen Capture"]:
    print("The server requires the screen capture permission")
```
