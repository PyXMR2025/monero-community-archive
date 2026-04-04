---
title: Monero transaction stuck as sent in the GUI
source_url: https://github.com/monero-project/monero-gui/issues/4230
author: 1kitsch
assignees: []
labels: []
created_at: '2023-10-21T09:39:28+00:00'
updated_at: '2023-10-21T18:32:41+00:00'
type: issue
status: closed
closed_at: '2023-10-21T18:32:41+00:00'
---

# Original Description
I sent a transaction over a day ago using the GUI wallet.

My transaction has been stuck on sent.
I used a great [stackexchange post](https://monero.stackexchange.com/questions/6649/transaction-stuck-as-pending-in-the-gui) and fixed this problem once before months ago. Last time i had this issue i ran through the guide and eventually fixed this by adding the 'old' suffix to my wallet name to initiate a wallet refresh. This time this has not helped me.



>I have tried changing from simple mode to advanced & using a remote node to refresh the wallet and sync it up
>I have updated the gui wallet now and restored the wallet from its 25 words and no help.

I have tried to use the relay_tx command, i am receiving this error.

">>> relay_tx 1455b07a95fa7dbc2256aec056aaaf264d427abaa2aa671d0f1d8e9ff8ae5592
[21/10/2023 04:26] 2023-10-21 03:26:42.940 I Monero 'Fluorine Fermi' (v0.18.3.1-release)
Error: Unsuccessful -- json_rpc_request:"

_This is the only thing I tried last time i had this issue, and i believe it worked last time, this may have been what fixed my issue last time, so if anyone has any ideas how i can avoid that error, maybe it will fix the transaction?_

I have decoded the transaction on xmrchain.net and found the outputs to be a value of 0 Xmr which puts me at peace that i havent lost my money.


Any idea?
i am using the monero gui wallet on mac
version 0.18.2.2-release (Qt 5.12.8)





# Discussion History
## selsta | 2023-10-21T13:48:45+00:00
I'm a bit confused, does the transaction id show up when you search it on xmrchain.net?

Also can you go to Settings -> Info, and share what "Wallet mode" you have?

## 1kitsch | 2023-10-21T18:00:28+00:00
Yes, it shows up with 1200 confirmations and 2 outputs of 0 xmr. As for wallet mode, i have since switched from simple to advanced using a remote node, i have tried a few from monero.fail. This was one of the things that possibly solved my problem when i had this issue before, but it hasnt worked this time

Please let me know if you have any ideas :)

## selsta | 2023-10-21T18:03:44+00:00
A transaction can't be "stuck as sent", either you sent it or not. According to the 1200 confirmations it correctly sent the transaction. What is the exact issue you are having?

## 1kitsch | 2023-10-21T18:07:58+00:00
The transaction hasnt been received by the other wallet.

Thats what i meant by stuck as sent, as I understand maybe I didnt communicate that very well.
I believe the only ever time i had this issue, i followed a guide for tx stuck on pending, and managed to solve the problem by reinstalling the wallet. But none of the fixes in the stackexchange post i linked have helped this time.

I decoded the tx on xmrchain and the 2 outputs both show amounts of '?' rather than a decimal amount

i compared this with a previous successful transaction that showed an output matching the sent amount of xmr.

Thats what is leading me to believe the transaction is stuck, as it hasnt shown up in the other wallet either :)

## selsta | 2023-10-21T18:15:06+00:00
Stuck as pending means the transaction didn't propagate to the network, it would mean it doesn't show up on xmrchain.net. This did not happen here so the issue must be somewhere else, 1200 confirmations means it correctly sent. Did you double check with the person who is receiving that funds that the issue isn't on their side?

> i compared this with a previous successful transaction that showed an output matching the sent amount of xmr.

Did you do this with a transaction that you received or that you sent?

## 1kitsch | 2023-10-21T18:24:14+00:00
Yes, the xmr definitely didnt arrive. I had this issue with somebody once before, and the transaction did show on xmrchain. Very strange now that you say 

> Did you do this with a transaction that you received or that you sent?

I have double checked, and i was wrong, i must have compared this with a incoming transaction rather than one i sent. Apologies.

So it looks like the transfer has sent, but has not been received. Is there any other ways of getting in between this and trying to troubleshoot? It would be a huge weight lifted off my back. Im pretty much 100% certain the transaction was sent to the right address of course.

## selsta | 2023-10-21T18:26:23+00:00
Can the receiver do this decode output thing? 

If you sent it to the correct address then it's almost certainly an issue with the receiver wallet. Do you know what wallet software they use?

## 1kitsch | 2023-10-21T18:30:44+00:00
Thank you, i'll have them do it and report back. 

> Do you know what wallet software they use?

Not certain ill ask.

Thank you very much for now.

# Action History
- Created by: 1kitsch | 2023-10-21T09:39:28+00:00
- Closed at: 2023-10-21T18:32:41+00:00
