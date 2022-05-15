# Functions

| Function  | Description | Example Output | Extra
| ------- | ------------------ | ------------------ | ------------------ 
| get_server_stats() | Get the Stats of all alt:V Servers | {'serversCount': 111, 'playersCount': 665} | 
| get_servers() | Get an Array of all alt:V Servers on the Masterlist | [ServerObject1, ServerObject2, ServerObject3] | Array with Server Object
| get_server_by_id(id, always_create) | Get a specific Server using the id | ServerObject | Returned as Server Object if there is data returned. This can be overwritten with always_create. E.g. if there is no data returned then a empty Server object is returned.
| get_server_by_id_avg(id, time) | Get the average Player Numbers of a specific alt:V Server | [{'t': 1638140400, 'c': 521}, {'t': 1638226800, 'c': 527}] |
| get_server_by_id_avg_result(id, time) | Get the average Player Count over a defined time span. | 300 |
| get_server_by_id_max(id, time) | Get the max Player Numbers of a specific alt:V Server | [{'t': 1638140400, 'c': 521}, {'t': 1638226800, 'c': 527}] |
| validate_id(id) | Validate a alt:V Server id | True or False | Example id: ceaac3d1cc22761223beac38386f5ab2
