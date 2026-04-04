---
title: release v0.13.0.4 have double spending issue
source_url: https://github.com/monero-project/monero/issues/4745
author: Vaidas737
assignees: []
labels: []
created_at: '2018-10-27T20:45:51+00:00'
updated_at: '2018-10-28T07:04:02+00:00'
type: issue
status: closed
closed_at: '2018-10-27T23:46:26+00:00'
---

# Original Description
I tested the new release with monero-wallet-rpc and transfer_split method. As the result the wallet send the same amount twice.

monero-linux-x64-v0.13.0.4

# Discussion History
## moneromooo-monero | 2018-10-27T22:07:52+00:00
Can you give more info about what you are doing ? I just tried a transfer_split here, and the correct amounts were sent and received.

## moneromooo-monero | 2018-10-27T22:17:55+00:00
Including anwers to:
- twice as many outputs,  twice as many txes, or  outputs with amount twice as large ? Or other ?
- do you have the JSON that was sent ?
- do you have the JSON that was returned ?


## Vaidas737 | 2018-10-27T22:28:17+00:00
here the txids if it can help
4f4c224b1547634e34773b96ae239facb506739ae129ab3d6b4fb78a400de62b
6156cf32837ab97d9d2361f94c8bc07f79453a7fa8e8b747a5dc27527c12d20a

JSON sent
{
  "jsonrpc": "2.0", 
  "id": "0", 
  "method": "transfer_split",
  "params": {
    "destinations": [
      { "amount": 400000000, "address": "*****" }
    ],
    "mixin": 3,
    "get_tx_key": true,
    "new_algorithm": true
  }
}

JSON returned
{"amount_list":[400000000],"fee_list":[46120000],"multisig_txset":"","tx_hash_list":["4f4c224b1547634e34773b96ae239facb506739ae129ab3d6b4fb78a400de62b"],"unsigned_txset":""} 



## moneromooo-monero | 2018-10-27T22:46:56+00:00
Do you have the log from monero-wallet-rpc ?


## moneromooo-monero | 2018-10-27T22:58:27+00:00
I sent that same JSON (replacing the address), and it behaves as expected, one single tx.
The code that relays the tx to the daemon adds the txid to the list at the same time, so it the JSON reply has only one txid, it implies only one tx got sent. Could be a bug though, we'd likely see that in the monero-wallet-rpc log.
Is it possible two JSON requests were made in short order ?

## Vaidas737 | 2018-10-27T23:03:26+00:00
I can send the logs, it's too long to post it here.

## moneromooo-monero | 2018-10-27T23:05:10+00:00
You can post to fpaste.org or paste.debian.net and paste the URL here.
But really only the part near the timestamp of the tx are of interest.

## Vaidas737 | 2018-10-27T23:20:33+00:00
https://paste.fedoraproject.org/paste/gwNEDl7S2pINR1~9hsRf2A

## moneromooo-monero | 2018-10-27T23:30:27+00:00
Lucky this log has a lot of information.

If you run:
<pre>
grep -E handle_accept\|sent\ to\ daemon\|transfer_split log | less -SR
</pre>
Then you see two different calls to transfer_split, one at 20:21:54.088, the other at 20:22:07.064.
It looks like whatever sends the JSON sent it twice.

The handle_accept is when a new connection is received by the HTTP server.


## Vaidas737 | 2018-10-27T23:40:35+00:00
I see, thanks for clarification

## moneromooo-monero | 2018-10-27T23:46:44+00:00
No problem.
Your situation makes me think we could have a "unique id" in the transfer RPC, so that monero-wallet-rpc would ignore any duplicate. That would save you the dupe call, assuming the caller would send it twice exactly the same.

## Vaidas737 | 2018-10-28T07:04:02+00:00
That will be great, I like the idea.

# Action History
- Created by: Vaidas737 | 2018-10-27T20:45:51+00:00
- Closed at: 2018-10-27T23:46:26+00:00
