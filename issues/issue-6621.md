---
title: Daemon with RPC Pay Stops Communicating and on Reboot Earned Credits are Lost
source_url: https://github.com/monero-project/monero/issues/6621
author: Cactii1
assignees: []
labels: []
created_at: '2020-06-02T16:13:26+00:00'
updated_at: '2024-08-22T13:25:30+00:00'
type: issue
status: closed
closed_at: '2020-07-08T22:57:29+00:00'
---

# Original Description
I'm running a Monero daemon with RPC Pay enabled  for some experimental purposes. My wallet seems to start off fine with the daemon and it starts mining and submitting hashes to earn credits. They build up what seems to be normally and then after awhile the wallet stops mining. When I try the rpc_payment_info command it can't communicate with the daemon.

So I restart the daemon and set set the wallet to use it again (seems to know the daemon went offline) and am able to start mining to it again.

When I check the daemon with the rpc_payments command the previously earned credits are not available.

I checked the RPC Client ID and the Secret Key to confirm they are the same before and after reboot of the daemon and they are.

I'm doing this on Windows 8.1 and the Monero version is 0.16.0.0-release. Both the daemon and wallet are on the same machine but it's pointing to the machines external IP address which is behind a VPN.

# Discussion History
## Cactii1 | 2020-06-02T16:17:31+00:00
*** UPDATE ***
I ran the "save" command on the daemon and then rebooted it and no credits were saved. This is without the daemon having lost or stopped communicating - just a normal shutdown and restart.

## moneromooo-monero | 2020-06-02T23:01:43+00:00
If you run with:

> --log-level 0,daemon.rpc.payment:DEBUG

do you see anything interesting, like errors saving/loading?

## Cactii1 | 2020-06-03T18:17:54+00:00
I tried running like this and there is nothing obvious going wrong. When stopping the daemon it give the message that it's storing rpc payments data .

2020-06-03 18:08:40.324 D storing rpc payments data to C:\ProgramData\bitmonero

When I go to the directory where the files are stored they are present and the .old file is also present. It also updates the last modified time and date to when I shut down the node.

Starting it back up and it says it's loading the rpc payments info.

2020-06-03 18:11:34.074 I loading rpc payments data from /rpcpayments.bin

I can confirm that the file is there but the credits my client has are not reflected when I do an rpc_payments command.

My client expects it to be there too and says the following:

Error: Error mining to daemon: Found nonce, but daemon errored out with: 'RPC payment did not increase balance', continuing

Then it continues accruing credits again starting from zero balance.

## Cactii1 | 2020-06-03T19:09:46+00:00
Without shutting down the daemon - I'm able to shut down the wallet and restart it whilst telling it to use the previous secret key and the credit balance shows and is available.

## moneromooo-monero | 2020-06-05T11:22:23+00:00
https://github.com/monero-project/monero/pull/6627

## moneromooo-monero | 2020-07-08T22:57:29+00:00
Merged

## kongkeed | 2024-08-22T00:20:44+00:00
restart my local nodes from clip example but after back to restart  the nodes  shows no xmr in there  why  now i install blockchain again hope it correct  can you help me 

## selsta | 2024-08-22T13:25:29+00:00
@kongkeed please open a new issue and add more details of what your issue is, it's not apparent from your description

# Action History
- Created by: Cactii1 | 2020-06-02T16:13:26+00:00
- Closed at: 2020-07-08T22:57:29+00:00
