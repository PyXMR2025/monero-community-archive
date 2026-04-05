---
title: '"Environment Variables for rig-id Not Applied on Windows (MSYS2)"'
source_url: https://github.com/xmrig/xmrig/issues/3639
author: BaugetteGenZ
assignees: []
labels:
- question
created_at: '2025-02-27T22:14:31+00:00'
updated_at: '2025-06-16T15:12:14+00:00'
type: issue
status: closed
closed_at: '2025-06-16T15:12:14+00:00'
---

# Original Description
### Describe the Bug: 

The environment variables are not being reflected as expected when compiled with MSYS2 for XMRig on Windows. Specifically, the rig-id variable in config.json does not take the expected value when using environment variables like %random% or ${random}, even with the -DWITH_ENV_VARS=ON flag.

**To Reproduce:**
1. Follow the official documentation to compile XMRig for Windows using MSYS2.
2. Ensure that -DWITH_ENV_VARS=ON is passed during the build process.
3. Add the following to your config.json file or config_platform.h:
4. "rig-id": "%random%"
5. "rig-id": "${random}"
6. Compile and run the XMRig binary.
7. Observe that the rig-id is not dynamically set as expected based on the environment variable.


When using the -DWITH_ENV_VARS=ON flag, the rig-id should reflect the environment variable values set in the configuration file, allowing dynamic and random generation of the rig-id during runtime.

For example:

The rig-id in config.json should be replaced with a random value at runtime if using %random% or ${random}.

**Full command used to compile the project:**
 
"c:\Program Files\CMake\bin\cmake.exe" .. -G "Unix Makefiles" -DXMRIG_DEPS=c:/xmrig-deps/gcc/x64 -DWITH_EMBEDDED_CONFIG=ON -DWITH_ENV_VARS=ON

# Discussion History
## SChernykh | 2025-02-28T09:18:00+00:00
%random% is not a real environment variable, it's a .bat preprocessor thing in Windows. You can see the list of environment variables by running `set` command in the Windows console..

# Action History
- Created by: BaugetteGenZ | 2025-02-27T22:14:31+00:00
- Closed at: 2025-06-16T15:12:14+00:00
