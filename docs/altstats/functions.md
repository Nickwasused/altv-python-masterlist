# Functions

| Function                            | Description | Example Output                                                                                     | Extra
|-------------------------------------| ------------------ |----------------------------------------------------------------------------------------------------| ------------------ 
| get_server_stats()                  | Get the Stats of all alt:V Servers | [{...}, { "ServerCount": 72, "PlayerCount": 958, "TimeStamp": "2021-01-01T12:15:00.464Z" }, {...}] | 
| get_servers_average() | Get the average values of the stats. | ('2022-07-16T10:35:00.379Z', '2022-07-17T10:30:00.305Z', 116.0, 1891.0) | Start Date, End Date, Average Server Count, Average Player Count
| get_servers()                       | Get an Array of all alt:V Servers on the Masterlist | [ServerObject1, ServerObject2, ServerObject3]                                                      | Array with Server Object
| get_server_by_id(id)   | Get a specific Server using the id | ServerObject                                                                                       | Returned as Server Object
| validate_id(id)                     | Validate a alt:V Server id | True or False                                                                                      | Example id: 86
