---
title: Wallet v0.16 refresh command throwing errors before completed.
source_url: https://github.com/monero-project/monero/issues/6605
author: downystreet
assignees: []
labels: []
created_at: '2020-05-31T12:08:11+00:00'
updated_at: '2020-06-05T11:26:26+00:00'
type: issue
status: closed
closed_at: '2020-06-05T11:26:26+00:00'
---

# Original Description
When running the refresh command in the CLI wallet v0.16 it will scan a chunk of blocks and then exit with Error: refresh failed: payment required.. Blocks recieved: 29230. When I run the refresh command again it resumes from where it ended with the error but then throws the error again after scanning another chunk of blocks. When I start the wallet it gives error right away:
Error: refresh failed: payment required.. Blocks received 0 
Background refresh thread started 

OS: Centos 8
Kernel: 4.18.0-147.8.1

# Discussion History
## downystreet | 2020-05-31T12:18:30+00:00
 Does using the refresh command interfere with this?

## moneromooo-monero | 2020-05-31T12:39:24+00:00
Did you have enough credits for that node to begin with ? It's possible your balance depleted, then you found a good enough hash, which allowed you to get some more blocks.

## downystreet | 2020-05-31T12:41:25+00:00
You have to have credits for your wallet to sync to the blockchain?

## moneromooo-monero | 2020-05-31T12:48:40+00:00
If you're connected to a daemon that requires it, yes. Are you connected to a daemon that requires it ? You can see with "rpc_payment_info".

## downystreet | 2020-05-31T12:55:03+00:00
I'm using my daemon. I have the full blockchain downloaded. rpc_payment_info gives this output:
Using daemon: http://localhost:18081
Payments required for node use, current credits: 250
Credits target: 50000
Credits spent this session:5500
Credit discrepancy this session: 0 (0%)
Difficulty: 1000, 250 credits per hash found, 0.25 credits/hash
Mining for payment at 45.9H/s
Estimated time till 50000 credits target mined: 1 hours

## moneromooo-monero | 2020-05-31T12:58:12+00:00
Odd. The default is to not require payment. And you mentioned you did not know it was possible so you clearly did not set it up. In any case, that daemon appears to be set up to require payment, and your wallet is mining for it, so that explains the refresh stopping and restarting once it's got more credits.
What is your monerod command line ?

## downystreet | 2020-05-31T13:01:58+00:00
I set the daemon to require payment. running --restricted-rpc --rpc-payment-address 49....  --rpc-payment-credits 250 --rpc-payment-difficulty 1000. 
So you're saying if I just let it sit and do it's thing it will eventually sync?

## moneromooo-monero | 2020-05-31T13:05:49+00:00
Yes.

## downystreet | 2020-05-31T13:13:07+00:00
Alright I just restarted the daemon and ran it regularly and it syncs fine now. Thanks for the help.

## moneromooo-monero | 2020-06-05T11:26:26+00:00
No bug here, closing.

# Action History
- Created by: downystreet | 2020-05-31T12:08:11+00:00
- Closed at: 2020-06-05T11:26:26+00:00
