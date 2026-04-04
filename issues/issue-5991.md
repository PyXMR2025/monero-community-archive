---
title: Linker error with zmq
source_url: https://github.com/monero-project/monero/issues/5991
author: tmoravec
assignees: []
labels: []
created_at: '2019-10-16T10:12:18+00:00'
updated_at: '2019-10-28T16:57:46+00:00'
type: issue
status: closed
closed_at: '2019-10-28T16:57:46+00:00'
---

# Original Description
On Ubuntu 18.04, in current master:

```
[ 86%] Linking CXX executable ../../bin/monero-wallet-rpc
../net/libnet.so: undefined reference to `zmq_term'
../net/libnet.so: undefined reference to `zmq_send'
../net/libnet.so: undefined reference to `zmq_msg_init'
../net/libnet.so: undefined reference to `zmq_msg_size'
../net/libnet.so: undefined reference to `zmq_strerror'
../net/libnet.so: undefined reference to `zmq_msg_data'
../net/libnet.so: undefined reference to `zmq_msg_close'
../net/libnet.so: undefined reference to `zmq_msg_recv'
../net/libnet.so: undefined reference to `zmq_msg_more'
../net/libnet.so: undefined reference to `zmq_errno'
collect2: error: ld returned 1 exit status
```

`libzmq3-dev` version `4.2.5-1ubuntu0.2`

# Discussion History
## moneromooo-monero | 2019-10-16T10:39:36+00:00
Are you sure it built everything and did not keep some old objects ?

## tmoravec | 2019-10-16T10:45:24+00:00
> Are you sure it built everything and did not keep some old objects ?

Yes, it happens even with a freshly cloned repo.

## tmoravec | 2019-10-16T10:46:11+00:00
FWIW, v0.14.1.2 builds fine on the same system.

## moneromooo-monero | 2019-10-16T11:23:48+00:00
Someone added the zmq libs to the cmake machinery for net, so it's not been merged yet then.

## moneromooo-monero | 2019-10-16T18:33:04+00:00
https://github.com/monero-project/monero/pull/5938

It wasn't merged because it broke on Mac apparently. Do you have a Mac by any chance ? :)

## tmoravec | 2019-10-16T18:36:49+00:00
This was on Ubuntu 18.04.

## moneromooo-monero | 2019-10-16T18:39:09+00:00
I'll take that as a no. Then we'll wait till someone with a Mac wants to debug.

## kayabaNerve | 2019-10-25T11:15:11+00:00
Happening to me to on Ubuntu 18.04, libpgm-dev and libnorm-dev installed, on the release-0.15 branch.

## moneromooo-monero | 2019-10-25T11:24:14+00:00
Does this fix it ?

```
diff --git a/src/net/CMakeLists.txt b/src/net/CMakeLists.txt
index 339587ffa..1ce7118ad 100644
--- a/src/net/CMakeLists.txt
+++ b/src/net/CMakeLists.txt
@@ -32,5 +32,5 @@ set(net_headers dandelionpp.h error.h i2p_address.h parse.h socks.h socks_connec
     tor_address.h zmq.h)
 
 monero_add_library(net ${net_sources} ${net_headers})
-target_link_libraries(net common epee ${Boost_ASIO_LIBRARY})
+target_link_libraries(net common epee ${ZMQ_LIB} ${Boost_ASIO_LIBRARY})
 
```

## kayabaNerve | 2019-10-25T12:05:59+00:00
Yes, thank you.

## moneromooo-monero | 2019-10-25T12:10:49+00:00
PRed as https://github.com/monero-project/monero/pull/6023

## moneromooo-monero | 2019-10-28T16:53:32+00:00
+resolved

# Action History
- Created by: tmoravec | 2019-10-16T10:12:18+00:00
- Closed at: 2019-10-28T16:57:46+00:00
