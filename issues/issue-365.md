---
title: NOT AN ISSUE ! how to automatically assign the ip address as worker name..?
  Is it possible?
source_url: https://github.com/xmrig/xmrig/issues/365
author: Gill1000
assignees: []
labels:
- question
created_at: '2018-01-27T10:33:28+00:00'
updated_at: '2018-03-14T22:48:33+00:00'
type: issue
status: closed
closed_at: '2018-03-14T22:48:33+00:00'
---

# Original Description
I was wondering ,can the worker name automatically assign to the ip address as it worker name.. @xmrig .....?

# Discussion History
## xmrig | 2018-01-31T08:51:13+00:00
You can use bat/cmd file instead of config file and use some solution from here https://stackoverflow.com/questions/5898763/how-do-i-get-the-ip-address-into-a-batch-file-variable

Also how set worker name, depends of pool, not all support this feature and not all allow use dot in worker name.
Thank you.

## sv0 | 2018-02-04T10:35:05+00:00
You can try following approach if you use Linux/FreeBSD:
 
    IP=`dig +short myip.opendns.com @resolver1.opendns.com`
    xmrig -o stratum+tcp://pool.host.com:port  -u MoneroWallet -p $IP 

## djdomi | 2018-02-06T14:02:19+00:00
@sv0 
I think he mentoid how to get the Local IP from the LAN-Worker

# Action History
- Created by: Gill1000 | 2018-01-27T10:33:28+00:00
- Closed at: 2018-03-14T22:48:33+00:00
