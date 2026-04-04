---
title: 'run monero-wallet-rpc failed with ''E No message store file found: test1.mms'''
source_url: https://github.com/monero-project/monero/issues/6207
author: past2017
assignees: []
labels: []
created_at: '2019-12-02T04:53:43+00:00'
updated_at: '2020-10-15T22:49:18+00:00'
type: issue
status: closed
closed_at: '2020-10-15T22:49:18+00:00'
---

# Original Description
version: v0.15.0.0-release/ubuntu 16.04
```
 ./monero-wallet-rpc --password password --wallet-file  test1 --rpc-bind-ip 0.0.0.0 --rpc-bind-port 19999  --rpc-login user:password           

This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Carbon Chamaeleon' (v0.15.0.0-release)
Logging to ./monero-wallet-rpc.log
WARNING: You may not have a high enough lockable memory limit, see ulimit -l
2019-12-02 04:21:00.648	W Loading wallet...
2019-12-02 04:21:00.649	I Generating SSL certificate
2019-12-02 04:21:01.170	I Generating SSL certificate
2019-12-02 04:21:01.888	W Loaded wallet keys file, with public address: 42AKevf1rcdH8MA6HJ9kgWNW9w4yKmPXPFYrToNaqSpw1PVbyuY8AZ1NQPeB5kaTAbZde6EVdDEksczUeNhSFoTh4f3AtbG
2019-12-02 04:21:01.942	E No message store file found: test1.mms
2019-12-02 04:21:02.200	E --rpc-bind-ip permits inbound unencrypted external connections. Consider SSH tunnel or SSL proxy instead. Override with --confirm-external-bind
2019-12-02 04:21:02.200	E Failed to initialize wallet RPC server

```

# Discussion History
## moneromooo-monero | 2019-12-02T12:31:04+00:00
Did you try --confirm-external-bind as suggested, if you're OK with the drawback that is being explained to you ?

## minereobot1 | 2020-01-03T15:53:15+00:00
--rpc-bind-ip only produce more problems 
2020-01-03 15:51:10.389	E No message store file found: wownero.mms
2020-01-03 15:51:10.643	E --rpc-bind-ip permits inbound unencrypted external connections. Consider SSH tunnel or SSL proxy instead. Override with --confirm-external-bind
2020-01-03 15:51:10.643	E Failed to initialize wallet RPC server


## minereobot1 | 2020-01-03T15:54:08+00:00
how i can generate this file ? monero.mms or wownero?


## moneromooo-monero | 2020-01-03T17:56:45+00:00
You don't care about this error. The second one is the one you care about.

## minereobot1 | 2020-01-05T01:41:59+00:00
second one ? what are you smoking ? what are you talking about ? second one
? i just asking about this error.. second one ? Come on buddy!

El vie., 3 ene. 2020 a las 14:56, moneromooo-monero (<
notifications@github.com>) escribió:

> You don't care about this error. The second one is the one you care about.
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6207?email_source=notifications&email_token=AJC2OYRGUXZW2QVUM33RA5LQ35355A5CNFSM4JTQGCZ2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOEIBWMFA#issuecomment-570648084>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AJC2OYRG2NOM3F75IZQW7GLQ35355ANCNFSM4JTQGCZQ>
> .
>


## niukouMan | 2020-04-27T14:09:33+00:00
I have the same problem. Have you solved your problem

## moneromooo-monero | 2020-05-16T16:13:15+00:00
By doing what the error tells you to:

> 2019-12-02 04:21:02.200	E --rpc-bind-ip permits inbound unencrypted external connections. Consider SSH tunnel or SSL proxy instead. Override with --confirm-external-bind


# Action History
- Created by: past2017 | 2019-12-02T04:53:43+00:00
- Closed at: 2020-10-15T22:49:18+00:00
