---
title: unsigned_monero_tx and submit_transfer using RPC
source_url: https://github.com/monero-project/monero/issues/3272
author: zkaf
assignees: []
labels: []
created_at: '2018-02-16T12:22:13+00:00'
updated_at: '2018-09-09T13:16:48+00:00'
type: issue
status: closed
closed_at: '2018-09-09T13:16:48+00:00'
---

# Original Description
I'm trying to generate unsigned_monero_tx in view-only wallet, sign it in full wallet, then go back to view-only one and submit the signed_monero_tx using RPC.
I'm wondering how to generate ```unsigned_monero_tx``` and ```signed_monero_tx```, and whether or not there is an equivalent of GUI's "_submit_transfer_" using RPC.
I don't find it in the guide https://getmonero.org/resources/developer-guides/wallet-rpc.html.
It is my understanding that it could be done using "_sendrawtransaction_", but in that case, how can I obtain the signed tx_hex to be sent?
(the original tx_hex is generated using "transfer" in view-only wallet with "do_not_relay" and "get_tx_metadata" set as true, which, however, is without a valid signature, thus cannot be sent. I can get the signature using "sign" in the full wallet, but not the signed tx_hex)

Thank you very much for your time and help.


# Discussion History
## johnconger | 2018-02-21T14:32:01+00:00
I have been trying to accomplish exactly what you are describing for the past few weeks and I have come to the conclusion that this is not possible via RPC.  You can only do this via the CLI.  I am in the process of writing a RPC wrapper around the CLI so that I can make programmatic RPC calls that issue the proper CLI commands.  A step-by-step guide around the CLI process can be found here: https://monero.stackexchange.com/questions/2160/how-do-i-use-cold-transaction-signing/ but you've probably seen this already.  I am using this as a guide for the RPC wrapper.

## zkaf | 2018-02-22T06:02:03+00:00
Thanks @johnconger for your answer and explanations. Yeah I have been trying all the ways I can think of, and searching online for solutions, only to find https://monero.stackexchange.com/questions/7239/is-there-a-way-to-make-unsigned-transaction-sign-and-submit-manually-using-wall unanswered.
(I see you also replied to that post which was not submitted by me)
CLI is pretty easy to understand and use, just RPC is not as friendly. I just don't get it if the command "sign" in RPC is not for unsigned_monero_tx, then how do we use it?

## zkaf | 2018-02-22T06:09:01+00:00
Just figured out another way is to forget about the RPC of the view-only wallet (on hot PC). Simply make a transaction and output it's tx_blob from the cold (full) wallet, then copy it to hot PC and use monerod's "sendrawtransaction". The problem of this is you have to copy sync-ed blockchain from hot PC to cold PC everytime you make a transaction. Otherwise it's possible that you would get error messages like "not enough money" cuz the DB on your cold PC is not sync-ed.
One solution is to use export/import key images but I got an error message "Failed" (RPC's error messages are basically useless). Maybe I was not doing it correctly.
Another is to add an option "-f" to skip certain errors like "not enough money" (currently not permitted) and force to generate a transaction offline (of course such a tx would fail to be broadcast). I know Factom's wallet has that implemented in its factom-cli.

## zhongqiuwood | 2018-05-26T23:53:39+00:00
@johnconger @zkaf 
According to wallet2::sign_tx method, the command [sign_transfer] only produces <signed_monero_tx> file that is encrypted by secret_view_key.
However the command [sign_transfer export] produces both <signed_monero_tx_raw> **that is NOT encrypted** and <signed_monero_tx> as well.

The RPC '/sendrawtransaction' seems asks for a **raw** transacation as the input, right?
So can you try RPC /sendrawtransaction + <signed_monero_tx_raw> to make it happen?


## stoffu | 2018-05-27T04:09:14+00:00
Yes, /sendrawtransaction accepts unencrypted tx blobs (which is why it’s called ‘raw’).

The support for cold signing with wallet RPC has been proposed a few weeks ago in #3780.

## zkaf | 2018-05-29T02:39:27+00:00
@zhongqiuwood 
Thanks for your reply. Just checked your solution; it seems to work. Didn't notice the `export` option of `sign_transfer` in v0.12.

## zhongqiuwood | 2018-05-31T13:17:24+00:00
@stoffu. Thank you for your clarification!

The command [sign_transfer export] really confuses people. 
Neither [-help] really helps. :(
I never know what the [sign_transfer export] does until read the code.
Can we enhance the usage and use [sign_transfer export_raw_tx] instead?

## stoffu | 2018-06-01T00:37:35+00:00
#3896

## moneromooo-monero | 2018-09-09T13:11:42+00:00
The missing parts seem to be merged now.

+resolved

# Action History
- Created by: zkaf | 2018-02-16T12:22:13+00:00
- Closed at: 2018-09-09T13:16:48+00:00
