---
title: Segfaut when request rpc cut before bitmonerod send response ?
source_url: https://github.com/monero-project/monero/issues/115
author: perl5577
assignees: []
labels: []
created_at: '2014-09-03T18:04:19+00:00'
updated_at: '2016-03-20T20:21:10+00:00'
type: issue
status: closed
closed_at: '2016-03-20T20:21:10+00:00'
---

# Original Description
One server
Aug 31 19:43:25 sd-52200 kernel: [3744359.110587] traps: bitmonerod[38545] general protection ip:558000 sp:7fffc205a0e0 error:0 in bitmonerod[400000+27a000]
Aug 31 22:56:44 sd-52200 kernel: [3755969.543315] bitmonerod[9622]: segfault at d4 ip 0000000000558000 sp 00007fff69c9ba60 error 4 in bitmonerod[400000+27a000]
Sep  2 12:52:20 sd-52200 kernel: [3892643.870889] bitmonerod[41405]: segfault at 2d ip 0000000000558000 sp 00007fffa5069de0 error 4 in bitmonerod[400000+27a000]
Sep  2 21:12:01 sd-52200 kernel: [3922655.656492] traps: bitmonerod[49690] general protection ip:558000 sp:7fff909b5020 error:0 in bitmonerod[400000+27a000]
Sep  2 23:48:08 sd-52200 kernel: [3932031.486473] traps: bitmonerod[59552] general protection ip:558000 sp:7ffff0dab060 error:0 in bitmonerod[400000+27a000]
Sep  2 23:51:19 sd-52200 kernel: [3932223.256345] bitmonerod[61345]: segfault at 29 ip 0000000000558000 sp 00007fff11cb4aa0 error 4 in bitmonerod[400000+27a000]

Other server
Aug 31 22:56:02 sd-61632 kernel: [3093513.417808] bitmonerod[61424]: segfault at 49edc80002e ip 0000000000538500 sp 00007fff3c8dba20 error 4 in bitmonerod[400000+27a000]
Sep  2 13:02:44 sd-61632 kernel: [3230652.364691] bitmonerod[29388]: segfault at 31 ip 0000000000538517 sp 00007fff153345e0 error 6 in bitmonerod[400000+27a000]

As not impact on my pool , I use multibitmonerod .
Seems to occur if an RPC request getblocktemplate cuts before bitmonerod send response.
After segfault bitmonerod is never OK 


# Discussion History
## sammy007 | 2014-09-03T18:21:21+00:00
> As not impact on my pool , I use multibitmonerod .

Not impact on my pool I use stock bitmonerod. Should't you submit this issue to multibitmonerod coin repo?


## perl5577 | 2014-09-03T22:28:26+00:00
I use also stock bitmonerod :)
My pool use just 4 bitmonerod for prevent at or other probleme. 


## fluffypony | 2016-01-25T17:50:38+00:00
Is this still happening?


## moneromooo-monero | 2016-03-20T12:49:33+00:00
What does "an RPC request getblocktemplate cuts before bitmonerod send response" mean ? The client closes connection after sending the request, but before a reply is received ?


## perl5577 | 2016-03-20T20:20:41+00:00
You can close


# Action History
- Created by: perl5577 | 2014-09-03T18:04:19+00:00
- Closed at: 2016-03-20T20:21:10+00:00
