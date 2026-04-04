---
title: Sweep_single Trezor not working
source_url: https://github.com/monero-project/monero/issues/6635
author: ReadandSweepm
assignees: []
labels: []
created_at: '2020-06-08T16:16:48+00:00'
updated_at: '2020-08-25T18:28:05+00:00'
type: issue
status: closed
closed_at: '2020-08-16T19:46:39+00:00'
---

# Original Description
CLI 16.0 with Trezor then sweep_single not working

Try it (sweep_single unimportant <key image> <destination address>) and you'll get the CLI saying: 
  Error: transaction <txid> was rejected by daemon
  Error: Reason: invalid input
and the daemon saying:
  E Bad key image
  W [on_send_raw_tx]: tx verification failed: invalid input

Suspect trezor because sweep_single perfectly possible with just cli wallet.


# Discussion History
## selsta | 2020-06-08T16:17:59+00:00
Are you using the latest Trezor firmware?

## ReadandSweepm | 2020-06-08T21:03:48+00:00
Yes

## selsta | 2020-06-09T07:39:01+00:00
ping @ph4r05 

## ph4r05 | 2020-06-09T09:18:44+00:00
@selsta thanks for the notification. I will check what I can do. 
@ReadandSweepm are other transaction methods working well? 

## ReadandSweepm | 2020-06-09T12:04:16+00:00
> @ReadandSweepm are other transaction methods working well?

Yes

## ph4r05 | 2020-06-09T14:06:30+00:00
@ReadandSweepm  thanks for info. OK so it will be problem just in the `sweepp_single`, thats a good sign :)

I will look into in next week probably as this one is quit busy for me.

## ph4r05 | 2020-06-09T17:38:58+00:00
@ReadandSweepm just an idea, can you pls try running `hw_key_images_sync` to make sure the key images are computed correctly and then rerun `sweep_single` with the newly computed key image? It would help me diagnose the culprit.

How did you obtain the key image for the UTXO you want to transfer with `sweep_single`?


## ReadandSweepm | 2020-06-10T17:43:32+00:00
> try running `hw_key_images_sync`

Did not try that yet. the command returns: 
    "key images synchronized to height {height},  {amount} spent, {amount} unspent" 
and then shows some tx's (not same as incoming_transfers available)

> rerun `sweep_single`

Did it now after the key image sync but same problem. 

> How did you obtain the key image

incoming_transfers available verbose


## ReadandSweepm | 2020-06-19T11:58:03+00:00
This should be easy to reproduce. Are you able to?

## ph4r05 | 2020-06-19T12:16:42+00:00
@ReadandSweepm I was looking at it but haven't finished it at the moment. I will get to that soon. (it took quite some time to sync all the projects and setup the local testnet)

## ph4r05 | 2020-06-19T14:29:39+00:00
It seems the `sweep_single` does not even hit the Trezor, the generated transaction returns key image `0100000000000000000000000000000000000000000000000000000000000000` which is obviously wrong (probably due to zero spending key).

The fix should be quite easy. I will look into it later next week.

## ph4r05 | 2020-06-23T11:04:40+00:00
I consider this issue fixed as #6677 and #6681 are fixing it and @selsta tested it (thanks!)

## ReadandSweepm | 2020-08-25T18:28:05+00:00
Thanks for fixing this, confirmed it works. I noticed from the release note you fixed it thanks much

# Action History
- Created by: ReadandSweepm | 2020-06-08T16:16:48+00:00
- Closed at: 2020-08-16T19:46:39+00:00
