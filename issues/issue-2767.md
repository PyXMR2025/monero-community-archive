---
title: RPC status string "Failed" hard coded multiple times in core_rpc_server.cpp
source_url: https://github.com/monero-project/monero/issues/2767
author: cryptoshrimpi
assignees: []
labels:
- invalid
created_at: '2017-11-06T10:54:56+00:00'
updated_at: '2017-11-06T11:24:24+00:00'
type: issue
status: closed
closed_at: '2017-11-06T11:23:54+00:00'
---

# Original Description
[rpc/core_rpc_server.cpp](https://github.com/monero-project/monero/blob/master/src/rpc/core_rpc_server.cpp) makes often use of `CORE_RPC_STATUS_OK` to signal that the RPC call was processed with success. In cases of failure the string is hard coded as `"Failed"` and occurs multiple times. 

I think it would make sense to introduce `CORE_RPC_STATUS_FAILED` in [rpc/core_rpc_server_commands_defs.h](https://github.com/monero-project/monero/blob/960886aa04f0b50265884c0d4338031a93b1bc5d/src/rpc/core_rpc_server_commands_defs.h ) to replace lines like `res.status = "Failed";` with `res.status = CORE_RPC_STATUS_FAILED;`

# Discussion History
## moneromooo-monero | 2017-11-06T11:19:04+00:00
Anything other than OK is a failure, status can be set to explanatory strings if such a thing is appropriate for a particular RPC. "Failed" is not particularly meaningful here, and is just being used as a "no particular reason given" string.

+invalid


# Action History
- Created by: cryptoshrimpi | 2017-11-06T10:54:56+00:00
- Closed at: 2017-11-06T11:23:54+00:00
