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
| fetch_connect_json() | which is going to fetch the "connect.json" from the CDN of the specified server it it has a CDN