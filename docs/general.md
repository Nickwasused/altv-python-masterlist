# General

By default, a function will return None when it is failing, so please account for that in your code.

Example:
```
import altvmasterlist as altv

# get the server json
response = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2").get_json()

if (response != None):
    print(response["active"])
```

## Proxy

If you want to use a proxy then create a file called `.env` with the following content:
```commandline
HTTP_PROXY="http://192.168.1.1:8080"
HTTPS_PROXY="socks5://192.168.1.1:9050"
```