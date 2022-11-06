# Functions

| Function                            | Description                                                                | Example Output | Extra
|-------------------------------------|----------------------------------------------------------------------------| ------------------ | ------------------ 
| get_version_info(branch: Branch, file: Files, platform: Platform)                  | Get the Version info of a certain file with a certain branch and platform. | {"latestBuildNumber":-1,"version":"11.0","hashList":{"modules/libjs-bytecode-module.so":"c5800adc86dbb0606bc14ea1c959e69140a31384"},"sizeList":{"modules/libjs-bytecode-module.so":31062136}} |

# Enums

The following Enums are avalible. See the [Examples](./examples.md) on how to use them.

## Platform

| Enum    | Value
|---------|-----------
| Windows | x64_win32 
| Linux   | x64_linux 

## Branch

| Enum    | Value   
|---------|---------
| Dev     | dev     
| RC      | rc      
| Release | release 

## Files

| Enum        | Value              
|-------------|--------------------
| Csharp      | coreclr-module     
| JavaScript  | js-module          
| JSByte      | js-bytecode-module 
| VoiceServer | voice-server       
| GameServer  | server             
| GameClient  | client             