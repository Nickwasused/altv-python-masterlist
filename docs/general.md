# General

By default, a function will return None when it is failing, so please account for that in your code.

Example:
```
from altvmasterlist import masterlist as altv

# get the server json
response = altv.get_server_by_id("ceaac3d1cc22761223beac38386f5ab2").get_json()

if (response != None):
    print(response["active"])
```