---
title: Dockerfile does not work
source_url: https://github.com/monero-project/monero/issues/1107
author: sjug
assignees: []
labels: []
created_at: '2016-09-20T15:05:57+00:00'
updated_at: '2016-09-20T17:56:56+00:00'
type: issue
status: closed
closed_at: '2016-09-20T15:08:59+00:00'
---

# Original Description
$ docker run -it -v /monero/chain:/root/.bitmonero -v /monero/wallet:/wallet -p 18080:18080 monero

```
Creating the logger system
2016-Sep-20 15:00:53.067324 Initializing cryptonote protocol...
2016-Sep-20 15:00:53.067358 Cryptonote protocol initialized OK
2016-Sep-20 15:00:53.067704 Initializing p2p server...
2016-Sep-20 15:00:53.943386 Set limit-up to 2048 kB/s
2016-Sep-20 15:00:53.943499 Set limit-down to 8192 kB/s
2016-Sep-20 15:00:53.943550 Set limit-up to 2048 kB/s
2016-Sep-20 15:00:53.943594 Set limit-down to 8192 kB/s
2016-Sep-20 15:00:53.943700 Binding on 0.0.0.0:18080
2016-Sep-20 15:00:53.944004 Net service bound to 0.0.0.0:18080
2016-Sep-20 15:00:53.944025 Attempting to add IGD port mapping.
2016-Sep-20 15:00:57.948939 No IGD was found.
2016-Sep-20 15:00:57.948984 P2p server initialized OK
2016-Sep-20 15:00:57.949081 Initializing core rpc server...
2016-Sep-20 15:00:57.949139 Binding on 127.0.0.1:18081
2016-Sep-20 15:00:57.949507 Core rpc server initialized OK on port: 18081
2016-Sep-20 15:00:57.949548 Initializing core...
2016-Sep-20 15:00:57.950152 Error trying to lock /root/.bitmonero/.daemon_lock: No such file or directory
2016-Sep-20 15:00:57.950195 ERROR /src/src/cryptonote_core/cryptonote_core.cpp:271 Failed to lock "/root/.bitmonero"
2016-Sep-20 15:00:57.950215 Deinitializing rpc server...
2016-Sep-20 15:00:57.950306 Deinitializing p2p...
2016-Sep-20 15:00:57.950381 Failed to save config to file /root/.bitmonero/p2pstate.bin
2016-Sep-20 15:00:57.950481 Deinitializing core...
2016-Sep-20 15:00:57.950512 Closing IO Service.
2016-Sep-20 15:00:57.950565 Failed to deinitialize core...
2016-Sep-20 15:00:57.950590 Deinitializing cryptonote_protocol...
```


# Discussion History
## sjug | 2016-09-20T15:08:10+00:00
SElinux policy issue, closing.


## sjug | 2016-09-20T17:56:56+00:00
Just to help others that may run into the same thing, this helped me fix the issue:
http://www.projectatomic.io/blog/2016/03/dwalsh_selinux_containers/


# Action History
- Created by: sjug | 2016-09-20T15:05:57+00:00
- Closed at: 2016-09-20T15:08:59+00:00
