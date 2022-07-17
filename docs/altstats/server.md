# Server
## Object
This is the server object:

```Case Sensitive!```

| Paramete          | Type
|-------------------| -----
| Id                | int
| FoundAt           | string
| LastActivity      | string
| Visible           | boolean
| ServerId          | string
| Players           | int
| Name              | string
| Locked            | boolean
| Ip                | string
| Port              | int
| MaxPlayers        | int
| Ping              | int
| Website           | string
| Language          | string
| Description       | string
| LastUpdate        | int
| IsOfficial        | boolean
| PlayerRecord      | int
| PlayerRecordDate  | string
| LastFetchOnline   | boolean
| LanguageShort     | string
| GameMode          | string
| Branch            | string
| Build             | int
| CdnUrl            | string
| EarlyAuthUrl      | string
| Verified          | boolean
| UseCdn            | boolean
| UseEarlyAuth      | boolean
| BannerUrl         | string
| Promoted          | boolean
| Tags              | array
| UseVoiceChat      | boolean
| Level             | int
| Version           | string

## Functions

You can call the following functions on the server object:

| Function | Description
| -------- | -------
| get_json() | which is going to return the complete data (Id to Version) as a JSON object.
| update() | which is going to fetch the API data from alt:V and replace it in the Server object. 
| fetch_connect_json() | which is going to fetch the "connect.json" from the CDN of the specified server if it has a CDN otherwise we are trying to fetch it directly from the alt:V http server
| get_dtc_url(password) | Get the "Direct Connect Protocol" URL. You can supply a password. E.g. altv://connect/1.1.1.1:7788?password=test
| get_permissions() | Get the Permissions of the Server as JSON. E.g. ```{'required': {'Screen Capture': True, 'WebRTC': False, 'Clipboard Access': False}, 'optional':{'Screen Capture': False, 'WebRTC': False, 'Clipboard Access': False}}```