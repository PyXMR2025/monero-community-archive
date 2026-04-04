---
title: monero-wallet-rpc erroneously claims to lose connection to daemon if tx-notify
  script crashes
source_url: https://github.com/monero-project/monero/issues/8864
author: snex
assignees: []
labels:
- bug
- reproduction needed
created_at: '2023-05-19T19:30:10+00:00'
updated_at: '2025-01-04T21:38:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Monero 'Fluorine Fermi' (v0.18.1.2-release), downloaded via apk package manager on Alpine Linux.

If the script passed to --tx-notify crashes, monero-wallet-rpc crashes and also deletes the wallet file it was opened with. The exit code of the crashed script was 127, if that matters. Specifically, I used a script with /bin/bash in the shebang on a system without bash installed. The following should show the problem:

```
#!/bin/bash

echo "hi"
```

# Discussion History
## plowsof | 2023-05-20T18:53:54+00:00
i tried to reproduce with simply :
```
#!/bin/bash
exit 127
```
i could not reproduce hm

## snex | 2023-05-20T18:56:42+00:00
The wallet has to actually receive a transaction, and it was on stagenet. Forgot to mention that. I will see if I can create a docker image that reproduces the problem. It came up during dev work and once I figured out the cause I fixed my script and moved forward.

## snex | 2023-05-20T19:34:06+00:00
Ok I think that the wallet deletion may have been something I did, however the rpc client does lose connection to the daemon permanently and never seems to get it back.

create the wallet

```
monero-wallet-cli --stagenet --daemon-host=stagenet.community.rino.io
```

connect to the wallet with rpc client
```
monero-wallet-rpc --wallet-file=[THEWALLET] --stagenet --daemon-host=stagenet.community.rino.io --rpc-bind-port=12345 --password=[THEPASSWORD] --tx-notify="process_tx.sh 1 %s"
```

send a transaction to the wallet's address

```
This is the RPC monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Fluorine Fermi' (v0.18.1.2-release)
Logging to monero-wallet-rpc.log
2023-05-20 19:29:24.494	W Loading wallet...
2023-05-20 19:29:36.839	W Loaded wallet keys file, with public address: 54nnwUGEjCccNBdTxFX7vRg1JyeVRK2UV4VHaauUaRD5NDYXLetQJNVc1iyi1Vd52wXpwMNe9r7h6DKgCyKR3befNpaNEX6
2023-05-20 19:29:38.519	W RPC username/password is stored in file monero-wallet-rpc.12345.login
2023-05-20 19:29:38.519	I Binding on 127.0.0.1 (IPv4):12345
2023-05-20 19:29:41.335	W Starting wallet RPC server
2023-05-20 19:30:03.920	E Failed to execve: Bad file descriptor
2023-05-20 19:30:23.921	E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2023-05-20 19:30:23.931	E Exception at while refreshing, what=no connection to daemon
```

contents of process_tx.sh:

```
#!/bin/bash

POST_DATA="{\"transaction\":{\"wallet_id\":$1,\"monero_tx_id\":\"$2\"}}"
/usr/bin/curl -s -X POST -H 'Content-Type: application/json' -d "$POST_DATA" http://127.0.0.1:3000/api/v1/process_transaction
```

Since bash is not installed on the system, the script immediately crashes and we get stuck into this no-connection state forever.

## snex | 2023-05-21T05:11:15+00:00
I thought maybe issuing RPC commands to the wallet might trigger the issue, but after some extensive testing of that, it all seems to work. I also tried sending multiple transactions and the wallet still seems to pick them up despite claiming it is not connected to the daemon. Seems like the only problem here is the inaccurate error messages about not being connected.

## plowsof | 2023-05-21T09:51:15+00:00
i think the next step would be to force the "Failed to execve: Bad file descriptor" error to appear (im not sure how... maybe if the notify script is opened..) and see what happens (the script exiting with code 127 after tx is received does not cause the issue) 

## snex | 2023-05-21T14:47:50+00:00
> i think the next step would be to force the "Failed to execve: Bad file descriptor" error to appear (im not sure how... maybe if the notify script is opened..) and see what happens (the script exiting with code 127 after tx is received does not cause the issue)

If you grab snex00/xpg from dockerhub and run the commands I posted, you should see the issue.

## tankf33der | 2025-01-04T20:54:24+00:00
@snex, your Alpine is v3.21, right? :)

## snex | 2025-01-04T20:59:54+00:00
> @snex, your Alpine is v3.21, right? :)

ruby:3.2.2-alpine

## tankf33der | 2025-01-04T21:02:14+00:00
i meant Alpine Linux distro. Show me  output: `cat /etc/os-release`

## snex | 2025-01-04T21:05:10+00:00
```
/app # cat /etc/os-release 
NAME="Alpine Linux"
ID=alpine
VERSION_ID=3.19.0
PRETTY_NAME="Alpine Linux v3.19"
HOME_URL="https://alpinelinux.org/"
BUG_REPORT_URL="https://gitlab.alpinelinux.org/alpine/aports/-/issues"
```

## tankf33der | 2025-01-04T21:09:13+00:00
See, 3.19. Latest Alpine Linux is 3.21. 

i will try to repeat.

## tankf33der | 2025-01-04T21:24:59+00:00
@snex 

or I don't understand how to repeat the error correctly or I'm doing something wrong, but there is no error. Let's have you write again step by step how to repeat this. Thank you very much.


## snex | 2025-01-04T21:28:27+00:00
Everything in https://github.com/monero-project/monero/issues/8864#issuecomment-1555978360 should be all you need.

## tankf33der | 2025-01-04T21:38:34+00:00
> Everything in [#8864 (comment)](https://github.com/monero-project/monero/issues/8864#issuecomment-1555978360) should be all you need.

@0xFFFC0000, @snex  
Then, I claim that I cannot repeat this on latest stable Alpine Linux on master and 0.18.3.3.

# Action History
- Created by: snex | 2023-05-19T19:30:10+00:00
