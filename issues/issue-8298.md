---
title: commission 19.73 xmr SOS
source_url: https://github.com/monero-project/monero/issues/8298
author: xmrmfjj2
assignees: []
labels: []
created_at: '2022-04-27T12:13:41+00:00'
updated_at: '2023-08-09T00:04:00+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:04:00+00:00'
---

# Original Description
391d2a8c6d34267d673f06e631e631ea213180f4df7193a37091d540be92a605 transaction posted 2.5 xmr commission 19.73xmr why such a commission? how to return 19.73 help I use Monero GUI Wallet

# Discussion History
## selsta | 2022-04-27T15:18:04+00:00
Did you use simple mode? The problem is that simple mode uses a random remote node and it's possible that malicious remote nodes can increase the fee required.

If you still have the GUI open, can you go to Settings -> Log and enter "status" and post the output?

The GUI will display the fee but it's possible that you overlooked it. The fee goes to the miner of the block.

## selsta | 2022-04-27T15:44:34+00:00
I have opened this now for the GUI: https://github.com/monero-project/monero-gui/pull/3897

This should mean in the future users are warned more visibly when the remote node sets a high fee.

<img width="800" alt="Screnshot" src="https://user-images.githubusercontent.com/7697454/165557782-af28867d-a759-43b9-8a31-d2dea0fa157c.png">

Now not sure yet what we are going to do with your case.

## SChernykh | 2022-04-28T10:02:40+00:00
This transaction was mined in block [2610570](https://xmrchain.net/block/2610570) which was mined by https://xmr.solopool.org/blocks
Try to contact admin of that mining pool.

## stefanomarty | 2022-04-28T10:30:03+00:00
What about a more evident warning like a pop up when fee is > some average high value, asking the user to double confirm. Something like:
Warning!
Transaction fee asked by node is higher than average.
Are you sure you want to confirm this transaction?

## poiuty | 2022-04-28T10:47:15+00:00
xmrmfjj2 lost 19.73 XMR.
It is important not only to fix the bug. But also to help return the funds.
Possible via funding required https://ccs.getmonero.org

## proudmuslim-dev | 2022-04-28T12:19:37+00:00
I agree with @poiuty 

## Mspy1 | 2022-04-28T15:40:52+00:00
> xmrmfjj2 lost 19.73 XMR. It is important not only to fix the bug. But also to help return the funds. Possible via funding required https://ccs.getmonero.org

That block was mined by XMR solo pool "https://xmr.solopool.org/blocks", it might be possible for them to return it. But highly unlikely, cuz it's must've been paid already.

## xmrmfjj2 | 2022-04-29T08:30:52+00:00
thanks wrote to pool waiting for a reply

## xmrmfjj2 | 2022-04-29T09:02:39+00:00
Hello!

This is an incredible case, but unfortunately we can't help you. The miner has already received a payout for this block.

reply received

kapets now not as my 5000$ will not be returned? we have a war in Ukraine I'm in a polish ass

## xmrmfjj2 | 2022-05-22T16:55:45+00:00
help how to return the money

## HardenedSteel | 2022-07-22T17:32:07+00:00
@xmrmfjj2 sorry you can't recover your coins. Please check transaction fees before sending.

# Action History
- Created by: xmrmfjj2 | 2022-04-27T12:13:41+00:00
- Closed at: 2023-08-09T00:04:00+00:00
