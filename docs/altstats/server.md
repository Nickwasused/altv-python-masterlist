# Server
## Object
This is the server object:

```Case Sensitive!```

| Paramete          | Type
|-------------------| -----
| Id                | int
| FoundAt           | string
| LastActivity      | boolean
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
| connect_json      | json
| permissions       | json

You can create a Server object like this: Server(server_id)

## Functions

You can call the following functions on the server object:

| Function                  | Description
|---------------------------| -------
| update()                  | which is going to fetch the API data from alt:V and replace it in the Server object. 
| get_resource_size(resource, decimal, proxy) | Get the size of a alt:V resource.
| get_dtc_url(password=None) | Get the server direct connect Url
  
You can print the server object directly to get the JSON Object as a string.