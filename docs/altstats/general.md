# General

By default, a function will return None when it is failing, so please account for that in your code.

Example:

```python3

from altvmasterlist import altstats as altv

# get the server json
response = altv.get_server_by_id(86).get_json()

if response:
    print(response["LastFetchOnline"])
```
