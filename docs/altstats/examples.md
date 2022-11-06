# Examples

## Get a alt:V Server object

```python3
import altstats as altv
import sys

# get the server json
server = altv.get_server_by_id(86)

if server is None:
    print("Error while getting Server")
    sys.exit(1)
```

## Get a alt:V Server object and update it

```python3
from time import sleep
import altstats as altv
import sys

# get the server json
server = altv.get_server_by_id(86)

if server is None:
    print("Error while getting Server")
    sys.exit(1)

print(server.Players)

# wait 10 seconds
sleep(10)

server.update()
print(server.Players)
```

## Get a alt:V Server connect.json

```python3
import altstats as altv
import sys

# get the server json
server = altv.get_server_by_id(86)

if server is None:
    print("Error while getting Server")
    sys.exit(1)

connect_json = server.fetchconnectjson()
if connect_json:
    print(connect_json)
```

## Get a alt:V Server connect.json with a Proxy

```python3
import altstats as altv
import sys

# get the server json
server = altv.get_server_by_id(86)

if server is None:
    print("Error while getting Server")
    sys.exit(1)

connect_json = server.fetchconnectjson({
        "http": "http://user:password@host:port/",
        "https": "http://user:password@host:port/"
    })
if connect_json:
    print(connect_json)
```

## Get all alt:V Servers that are active

```python3
import altstats as altv

servers = altv.get_servers()

# update the first server
servers[0].update()

for server in servers:
    print(server.Players)
```

## Get the Direct Connect Url of a Server

```python3
import altstats as altv

# get the server dtc url with a password
server = altv.get_server_by_id(86)
print(server.get_dtc_url(password="test"))

# get the server dtc url without a password
server = altv.get_server_by_id(86)
print(server.get_dtc_url())
```

## Get the Permissions of a Server

```python3
import altstats as altv

server = altv.get_server_by_id(86)
permissions = server.get_permissions()
print(permissions)

if permissions["required"]["Screen Capture"]:
    print("The server requires the screen capture permission")
```

## Get the Permissions of a Server with a Proxy

```python3
import altstats as altv

server = altv.get_server_by_id(86)
permissions = server.get_permissions({
        "http": "http://user:password@host:port/",
        "https": "http://user:password@host:port/"
    })
print(permissions)

if permissions["required"]["Screen Capture"]:
    print("The server requires the screen capture permission")
```
