---
title: 'warning: "PROTOBUF_MIN_PROTOC_VERSION" is not defined, evaluates to 0 '
source_url: https://github.com/monero-project/monero/issues/5713
author: moneroexamples
assignees: []
labels: []
created_at: '2019-07-01T10:51:16+00:00'
updated_at: '2020-05-18T01:00:57+00:00'
type: issue
status: closed
closed_at: '2020-05-18T01:00:57+00:00'
---

# Original Description
Getting plenty of warnings on gcc 9.1, e.g: 

```
/home/mwo2/monero/src/device_trezor/trezor/messages/messages.pb.h:16:15: warning: "PROTOBUF_MIN_PROTOC_VERSION" is not defined, evaluates to 0 [-Wundef]
   16 | #if 3007000 < PROTOBUF_MIN_PROTOC_VERSION
      |               ^~~~~~~~~~~~~~~~~~~~~~~~~~~
In file included from /home/mwo2/monero/src/device_trezor/trezor/transport.hpp:52,
                 from /home/mwo2/monero/src/device_trezor/trezor.hpp:36,
                 from /home/mwo2/monero/src/device_trezor/device_trezor.hpp:33,
                 from /home/mwo2/monero/src/device_trezor/device_trezor.cpp:30:
```

# Discussion History
## moneromooo-monero | 2020-05-17T14:45:30+00:00
The source does not match what I have, and this appears to be a generated file. Does it still happens ? If yes, it might be a protoc version issue.
I have:
#if 3006001 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION


## moneroexamples | 2020-05-18T01:00:57+00:00
Thanks. Its an old issue and its not not relevant anymore. Haven't observed such warnings for a while. 

# Action History
- Created by: moneroexamples | 2019-07-01T10:51:16+00:00
- Closed at: 2020-05-18T01:00:57+00:00
