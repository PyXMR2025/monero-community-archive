---
title: wallet-rpc transfer waiting feedback so long
source_url: https://github.com/monero-project/monero/issues/5546
author: randy86
assignees: []
labels: []
created_at: '2019-05-16T13:30:00+00:00'
updated_at: '2019-06-29T12:06:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
i try for getbalance and other function is work perfectly but when i try to transfer with curl the feedback so long until 120s , i used the ssd with 4 core 8gb memory. how to make the curl transfer or rpc transfer feedback faster ?

Thank you

# Discussion History
## moneromooo-monero | 2019-05-16T15:03:25+00:00
The delay is caused by the daemon getting the history of output ages. I assume you're using 0.13.0.4 ? This is much improved in master.


## randy86 | 2019-05-16T16:00:31+00:00
im using latest monero version :

monerod version
Monero 'Boron Butterfly' (v0.14.0.2-release)


## moneromooo-monero | 2019-05-16T16:04:40+00:00
Oh yes, that's the one I meant :) Thanks.

## randy86 | 2019-05-16T16:07:13+00:00
so how to fixed it the feedback so long ?

## moneromooo-monero | 2019-05-16T17:58:22+00:00
Assuming you meant "how can I fix the delay being so long", then use master.

## stupidoes-day | 2019-05-20T04:45:14+00:00
> Assuming you meant "how can I fix the delay being so long", then use master.

hi , i have some problem ,so  i build from master branch as you suggest, the build process is success, and  i tried to run this command :

`monerod --data-dir=/mydir/.bitmonero` --detach

it does the synchronization , i tried to check the status by this command
 `monerod status`

i got this message ,

> 2019-05-20 04:38:30.890 I Monero 'Boron Butterfly' (v0.14.1.0-e8487fa)
2019-05-20 04:38:30.891 I Generating SSL certificate
Error: Couldn't connect to daemon: 127.0.0.1:18081

can you tell me which part i do wrong

## moneromooo-monero | 2019-05-20T09:46:59+00:00
Use --rpc-ssl disabled for now.

## moneromooo-monero | 2019-06-15T10:35:38+00:00
Can you try with 0.14.1.0 ?

## moneromooo-monero | 2019-06-29T12:06:42+00:00
ping

# Action History
- Created by: randy86 | 2019-05-16T13:30:00+00:00
