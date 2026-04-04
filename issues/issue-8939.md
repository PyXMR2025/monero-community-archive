---
title: Upgrading from v0.18.1.1 to v0.18.2.2 gives "thread_resource_error"
source_url: https://github.com/monero-project/monero/issues/8939
author: astupidmoose
assignees: []
labels: []
created_at: '2023-07-07T19:29:31+00:00'
updated_at: '2023-11-03T16:46:38+00:00'
type: issue
status: closed
closed_at: '2023-11-03T16:43:58+00:00'
---

# Original Description
Hello All, 

I'm running Monerod on BTCPay server through the docker implementation. 

Version 18.1.1 works well, but upgrading to 18.2.2 gives the following errors:

Monerod gives:

> 2023-07-07 18:54:50.004 I Monero 'Fluorine Fermi' (v0.18.2.2-release)
> 2023-07-07 18:54:50.004 I Initializing cryptonote protocol...
> 2023-07-07 18:54:50.004 I Cryptonote protocol initialized OK
> 2023-07-07 18:54:50.005 I Initializing core...
> 2023-07-07 18:54:50.005 I Loading blockchain from folder /home/monero/.bitmonero/lmdb ...
> 2023-07-07 18:54:50.044 I Stopping cryptonote protocol...
> 2023-07-07 18:54:50.044 I Cryptonote protocol stopped successfully
> 2023-07-07 18:54:50.045 E Exception in main! boost::thread_resource_error: Resource temporarily unavailable
> 

Monero Wallet:

> 2023-07-07 18:50:21.741 W Loading wallet...
> 2023-07-07 18:50:21.935 E dbr. THROW EXCEPTION: tools::error::wallet_internal_error
> 2023-07-07 18:50:21.935 E Failed to initialize ringdb: Failed to open rings database file '/home/monero': Permission denied
> 2023-07-07 18:50:23.969 W Loaded wallet keys file, with public address: 4AsYt5GTLHNFEWd6h1ZMnAFRfvBha1i7iGdcsFCCnZ6f2t3VZ9oTjhZ6SqR9gD9vQ3PPaVNc1M941Pu3YBYn5scYALETVsc
> 2023-07-07 18:50:24.333 E Initial refresh failed: boost::thread_resource_error: Resource temporarily unavailable
> 2023-07-07 18:50:24.335 E Failed to query mining status: No connection to daemon
> 2023-07-07 18:50:24.335 I Binding on 0.0.0.0 (IPv4):18082
> 2023-07-07 18:50:24.759 W Starting wallet RPC server
> 2023-07-07 18:50:24.759 W Stopped wallet RPC server
> 2023-07-07 18:50:24.759 W Saving wallet...
> 2023-07-07 18:50:25.093 W Successfully saved
> 

wondering if anyone has any insights on what could be causing these issues? 
I'm assuming this:

> 2023-07-07 18:54:50.045 E Exception in main! boost::thread_resource_error: Resource temporarily unavailable

but I really have no idea where to look to start with this. 

# Discussion History
## jeffro256 | 2023-07-11T04:23:25+00:00
https://stackoverflow.com/a/22570554

What's the thread limit per process in this docker container?

## michnovka | 2023-10-04T09:13:47+00:00
@jeffro256 on my installation with the same issue its like this:

```
monero@93b1565d858a:/$ root@btcpay277840:~# cat /proc/sys/kernel/threads-max
63276
```

## michnovka | 2023-10-04T09:14:23+00:00
It was suggested by @kukks that this might be permission error

## michnovka | 2023-10-10T08:58:09+00:00
[tested on fresh install](https://chat.btcpayserver.org/btcpayserver/pl/nnsmkamqjjg19mxzf1u9mg9w6r), the issue is the same. BTCPay devs dont want to fix this, does anybody have an idea what might be causing this?

## jeffro256 | 2023-10-26T00:10:17+00:00
Can you run `monerod` with `--log-level 4`?

## jeffro256 | 2023-10-26T00:12:13+00:00
Does this fix the problem? https://unix.stackexchange.com/a/255603

## astupidmoose | 2023-11-03T16:43:58+00:00
Closing this as upgrading to 0.18.3.1 fixed my issues. 

## selsta | 2023-11-03T16:46:37+00:00
I don't think anything was changed on our end so it might show up again in the future.

# Action History
- Created by: astupidmoose | 2023-07-07T19:29:31+00:00
- Closed at: 2023-11-03T16:43:58+00:00
