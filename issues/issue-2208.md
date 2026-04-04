---
title: Run monerod first time. Gets stuck after about 4 hrs. 0.10.3.1 gui beta 2 for
  linux 32bit
source_url: https://github.com/monero-project/monero/issues/2208
author: cavapoo2
assignees: []
labels: []
created_at: '2017-07-26T13:04:35+00:00'
updated_at: '2017-08-07T15:48:39+00:00'
type: issue
status: closed
closed_at: '2017-07-27T14:06:12+00:00'
---

# Original Description
log file attached.
i can see a few exceptions in there
[log.zip](https://github.com/monero-project/monero/files/1176613/log.zip)


# Discussion History
## cavapoo2 | 2017-07-26T13:34:58+00:00
ok here is txt file
[bitmonero.log.txt](https://github.com/monero-project/monero/files/1176700/bitmonero.log.txt)


## cavapoo2 | 2017-07-26T13:42:11+00:00
https://paste.fedoraproject.org/paste/txqft2i9JF~2G02hutDX7w/deactivate/qIStHRHPqloTTKxClSnKE4C0eIoXmt0F3Yh0M9NdsekAzitekZp9coixUEd5uS06

## moneromooo-monero | 2017-07-27T10:37:49+00:00
I'll need a log with --log-level 1,net.p2p.msg:INFO,net:CN:DEBUG,*verify*:INFO

## cavapoo2 | 2017-07-27T12:29:01+00:00
maybe you can close this. After stopping, i then rebooted and resumed monerod. No lock up so far, only issue now is lots of red console message ( command_timed_sync, handshake invoke failed). 

## moneromooo-monero | 2017-07-27T12:42:25+00:00
I can't close it, but you can, as the originator.

# Action History
- Created by: cavapoo2 | 2017-07-26T13:04:35+00:00
- Closed at: 2017-07-27T14:06:12+00:00
