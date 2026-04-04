---
title: Host 127.0.0.1:18081:ZMQ:18083 seems to be stuck
source_url: https://github.com/monero-project/monero/issues/9236
author: wxysystem32
assignees: []
labels:
- more info needed
created_at: '2024-03-11T03:43:17+00:00'
updated_at: '2024-03-11T05:01:31+00:00'
type: issue
status: closed
closed_at: '2024-03-11T05:01:31+00:00'
---

# Original Description
,how to fix this issue?
Host 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:59865[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m
mmonitor thread ready[0m
;31mHost 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:65258[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m
mmonitor thread ready[0m
;31mHost 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:58662[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m
mmonitor thread ready[0m
;31mHost 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:56627[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m
mmonitor thread ready[0m
;31mHost 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:49353[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m
mmonitor thread ready[0m
;31mHost 127.0.0.1:18081:ZMQ:18083 seems to be stuck, reconnecting[0m
mstopping[0m
mmonitor thread stopped[0m
mworker thread stopped[0m
mstopped[0m
mconnected to tcp://127.0.0.1:62910[0m
mconnected to tcp://127.0.0.1:18083[0m
mworker thread ready[0m

# Discussion History
## selsta | 2024-03-11T03:45:04+00:00
Can you share more information? What are you doing to trigger this? Which version are you using?

## wxysystem32 | 2024-03-11T03:59:02+00:00
> Can you share more information? What are you doing to trigger this? Which version are you using?

I use this command: monerod.exe --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist --data-dir "T:\bitmonero1"
these versions I've used have had this problem: windows 64 , 0.18.3.2,, 0.18.3.1

## wxysystem32 | 2024-03-11T04:59:13+00:00
> > Can you share more information? What are you doing to trigger this? Which version are you using?
> 
> I use this command: monerod.exe --zmq-pub tcp://127.0.0.1:18083 --disable-dns-checkpoints --enable-dns-blocklist --data-dir "T:\bitmonero1" these versions I've used have had this problem: windows 64 , 0.18.3.2,, 0.18.3.1

sorry,you can close it,the issue from p2pool.exe

# Action History
- Created by: wxysystem32 | 2024-03-11T03:43:17+00:00
- Closed at: 2024-03-11T05:01:31+00:00
