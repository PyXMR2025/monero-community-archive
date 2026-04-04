---
title: transfer by wallet-rpc only working randomly rarely
source_url: https://github.com/monero-project/monero/issues/3233
author: DavidBruchmann
assignees: []
labels: []
created_at: '2018-02-04T18:02:38+00:00'
updated_at: '2018-02-28T04:56:52+00:00'
type: issue
status: closed
closed_at: '2018-02-28T04:56:51+00:00'
---

# Original Description
Having commands like this in a loop
```
curl -u "monero":"monero" --digest -s -S -X POST http://127.0.0.1:28083/json_rpc -d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"wallet-dir\":\"/home/monero-wallets/\",\"method\":\"transfer\",\"params\":{\"destinations\":[{\"amount\":\"01000000000000\",\"address\":\"9sMgrW7guKiYKpttTGwQeDc5re8dkNFUQQDDqHbQrTd64WXZNakGzzjAyMEqZjAyfiMYvqueKR8qsLE4bdMm6gYFKEuFbFJ\"}],\"get_tx_key\":"true"}}" -H 'Content-Type: application/json'
```
I got 2 or 3 transfers and could control it in the wallets, but this is failing in more than 90% of cases.
I get mostly the response:
```
ERROR: -4: transaction was rejected by daemon
```
Is there any reason for that response and anything I can do about it?

# Discussion History
## DavidBruchmann | 2018-02-04T21:01:03+00:00
Now I remarked that waiting some minutes between the commands I can send when entering the commands directly on commandline:
```
curl -u "monero":"monero" --digest -s -S -X POST http://127.0.0.1:28083/json_rpc -d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"wallet-dir\":\"/home/monero-wallets/\",\"method\":\"transfer\",\"params\":{\"destinations\":[{\"amount\":\"01000000000000\",\"address\":\"9sMgrW7guKiYKpttTGwQeDc5re8dkNFUQQDDqHbQrTd64WXZNakGzzjAyMEqZjAyfiMYvqueKR8qsLE4bdMm6gYFKEuFbFJ\"}],\"get_tx_key\":true}}" -H 'Content-Type: application/json'
{
  "error": {
    "code": -4,
    "message": "not enough unlocked money"
  },
  "id": "0",
  "jsonrpc": "2.0"
}
```
Waiting some time ...

```
curl -u "monero":"monero" --digest -s -S -X POST http://127.0.0.1:28083/json_rpc -d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"wallet-dir\":\"/home/monero-wallets/\",\"method\":\"tansfer\",\"params\":{\"destinations\":[{\"amount\":\"01000000000000\",\"address\":\"9sMgrW7guKiYKpttTGwQeDc5re8dkNFUQQDDqHbQrTd64WXZNakGzzjAyMEqZjAyfiMYvqueKR8qsLE4bdMm6gYFKEuFbFJ\"}],\"get_tx_key\":true}}" -H 'Content-Type: application/json'
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    "fee": 3816720000,
    "multisig_txset": "",
    "tx_blob": "",
    "tx_hash": "666cfd75a0aeac2d18a0cdbfd2f551a70c3eba724713db5535d30eae0fac1ead",
    "tx_key": "b7ef7c54c894f669da7d3ec8194ee8edde1a497d322bcef9fbd1b58ea23d6a0d",
    "tx_metadata": ""
  }
}
```
Also the reason for rejecting is on commandline different, it's "not enough unlocked money".
Question is why monero-wallet-rpc reacts so unreliable and cranky and how to deal with it?

## moneromooo-monero | 2018-02-04T21:11:38+00:00
Change is locked for 10 blocks.

You hint there are two different cases where it fails, is that right ? If so, please describe how they differ. In one of those you say you get "not enough unlocked money", and you imply in the other you don't.


## DavidBruchmann | 2018-02-04T21:31:40+00:00
In the first case (very top, first post) the command is send by a script, and the answer I got was `transaction was rejected by daemon`.
As I echoed the curl-command too I just copied that and used it in the second post directly on commandline. Both commands there are the same, just for the second one I waited some time and the answer differs then as the last one is executed without error.

## DavidBruchmann | 2018-02-04T21:35:22+00:00
Mhm, so the lock is at least directly independent from time, but related to blocks.
Any way to circumvent or shorten that somehow?
Or is it possible to use further blocks?
I know I can send several transactions at once, but it's a huge amount of transactions (~5000) so the problem exists in any case because I think I should limit it to max. 100 at once perhaps.

## moneromooo-monero | 2018-02-05T15:11:53+00:00
It's not about blocks, but outputs. It'll be blocks if you have just one or two outputs. Split your outputs if you want to send repeatedly. That is, run "set merge-destinations 0" in monero-wallet-cli, then send yourself eg, 10% of your balance 10 times in the same tx. Then set min-output-count 100 and set min-output-value 1 in monero-wallet-cli to avoid re-coalescing.


## DavidBruchmann | 2018-02-05T15:45:55+00:00
Ok, thank's will try to completely understand and realize it.

## moneromooo-monero | 2018-02-05T20:15:24+00:00
For a fiat analogy:

Alice and Bob both have $100, and they want to pay $10 to both Charlie and Donna.

Alice has 10 $10 bills. She gives one to Charlie, and one to Donna.

Bob has a single $100 bill. He gives it to Charlie, and waits while Charlie looks for change. Bob has nothing left during that time. Later on, once he got change back, he pays Donna.

## DavidBruchmann | 2018-02-06T15:15:00+00:00
What could be a reason that a command is declined by script but accepted by cli?  
I entered this one several times this day by script and got always the message:  
```
ERROR: -4: transaction was rejected by daemon  
```
now I entered it directly a few seconds afterwards by cli and get a confirmation with tx-details.

This is the command:
```
curl -u "monero":"monero" --digest -s -S -X POST http://127.0.0.1:28083/json_rpc -d "{\"jsonrpc\":\"2.0\",\"id\":\"0\",\"wallet-dir\":\"/home/monero-wallets/\",\"method\":\"transfer\",\"params\":{\"destinations\":[{\"amount\":\"00900000000000\",\"address\":\"9sJBGmoSHET4VFvxAD7T1ZV7fohZdXukcbM1s8nUfJ6G7Frr1VEoNnFbY88WAkc7eQ6SeWLRSqLgN4vf6A3CnRx8AyQ1V5D\"},{\"amount\":\"01000000000000\",\"address\":\"9sMgrW7guKiYKpttTGwQeDc5re8dkNFUQQDDqHbQrTd64WXZNakGzzjAyMEqZjAyfiMYvqueKR8qsLE4bdMm6gYFKEuFbFJ\"}],\"get_tx_key\":true}}" -H 'Content-Type: application/json'
```
The script-part I mentioned is just doing it by php, the $curlCommand is exactly the same:
```
		ob_start();
		$exec = passthru($curlCommand, $return_var);
		$content = json_decode(ob_get_contents());
		ob_end_clean();
```

## moneromooo-monero | 2018-02-07T13:13:39+00:00
set_log 1 in the daemon will tell you why your tx is rejected.

## DavidBruchmann | 2018-02-28T04:56:51+00:00
I got it working, "transaction was rejected by daemon" is raised if blocks are not yet confirmed and "not enough unlocked money" is raised if the own part of the balance is not yet written back to the own wallet. Background is that the remaining amount in the wallet is send to the own wallet as transfer too.

# Action History
- Created by: DavidBruchmann | 2018-02-04T18:02:38+00:00
- Closed at: 2018-02-28T04:56:51+00:00
