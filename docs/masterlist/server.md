# Server

## Object
This is the server object:

| Parameter | Type
| ------- | ------------------ 
| active | boolean
| id | string
| maxPlayers | int
| players | int
| name | string
| locked | boolean
| host | string
| port | int
| gameMode | string
| website | string
| language | string
| description | string
| verified | boolean
| promoted | boolean
| useEarlyAuth | boolean
| earlyAuthUrl | string
| useCdn | boolean
| cdnUrl | string
| useVoiceChat | boolean
| tags | array
| bannerUrl | string
| branch | string
| build | int
| version | string
| lastUpdate | int

You can create a Server object like this: Server(server_id)

## Functions

You can call the following functions on the server object:

| Function | Description
| - | -
| update() | Update the server object by calling __init__
| get_max(time) | Get the maximum player data of the server
| get_avg(time, return_result=False) | Get the average player data of the server
| fetch_connect_json() | Fetch the connect.json of the server
| get_dtc_url(password=None) | Get the "Direct Connect Protocol" URL. You can supply a password. E.g. altv://connect/1.1.1.1:7788?password=test
| get_permissions() | Get the permissions of the Server in JSON
| get_resource_size(resource) | Get the size of an alt:V resource in MB
