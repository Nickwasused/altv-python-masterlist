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

## Functions

You can call the following functions on the server object:

| Function | Description
| - | -
| get_json() | which is going to return the complete data (active to lastUpdate) as a JSON object.
| update() | which is going to fetch the API data from alt:V and replace it in the Server object. 
| fetch_connect_json(proxy) | which is going to fetch the "connect.json" from the CDN of the specified server if it has a CDN otherwise we are trying to fetch it directly from the alt:V http server. You can define a proxy server here because this is connecting to the server directly.
| get_dtc_url(password) | Get the "Direct Connect Protocol" URL. You can supply a password. E.g. altv://connect/1.1.1.1:7788?password=test
| get_permissions(proxy) | Get the Permissions of the Server as JSON. E.g. ```{'required': {'Screen Capture': True, 'WebRTC': False, 'Clipboard Access': False}, 'optional':{'Screen Capture': False, 'WebRTC': False, 'Clipboard Access': False}}``` You can define a proxy server here because this is connecting to the server directly.
| get_resource_size(resource, decimal, proxy) | Get the size of a alt:V resource. 