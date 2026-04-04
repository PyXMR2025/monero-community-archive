---
title: Bug v0.17.3.2 Generate payment proof button
source_url: https://github.com/monero-project/monero-gui/issues/3909
author: tczee36
assignees: []
labels: []
created_at: '2022-05-05T07:59:42+00:00'
updated_at: '2022-06-09T18:57:20+00:00'
type: issue
status: closed
closed_at: '2022-06-09T18:57:20+00:00'
---

# Original Description
Hello found a bug,

Environment

    Windows 11 x64 Virtual Machine in VMware workstation
    Remote node: xmr.support
    Ran monero-gui as admin
    No password key file

How i found the bug:

   - Created a temp wallet in monero-gui v0.17.3.1
   - temp wallet sent a transaction, generated payment proof, works no problem
   - Same temp wallet loaded in v0.17.3.2, tried to generate payment proof, no response.

Not sure why this is happening, already whitelisted v0.17.3.2 in windows defender.

thanks

# Discussion History
## selsta | 2022-05-05T08:01:48+00:00
@reemuru could you take a look? :)

## reemuru | 2022-05-05T11:00:16+00:00
@selsta sure, let me attempt to replicate.

@westz36 is this the payment proof button from the transaction list or the one on the Advanced menu?

## reemuru | 2022-05-05T14:29:18+00:00
hmm, strange. I just tried to generate a tx proof on v0.17.3.1 from the advanced menu and I'm not getting any response.
it works fine from the tx list menu with the payment proof button.

@selsta could you confirm?

@westz36 are you able to provide video of tx proof from the Advanced menu?

## reemuru | 2022-05-05T14:46:27+00:00
confirmed that payment proof button is no longer working from tx list on v0.17.3.2 with the error message below and no response.

```bash
2022-05-05 14:44:21.622 W qrc:/pages/History.qml:1723: Error: Insufficient arguments
```
Edit: also checked, but now tx proof is working on v0.17.3.2 from the Advanced menu when putting tx id and recipient address

## selsta | 2022-05-05T14:56:35+00:00
> @selsta could you confirm?

I honestly have no idea, I never use the proof features.

## reemuru | 2022-05-05T14:59:34+00:00
@selsta ah it is ok. I see what happened. When adding Reserve Proof support the additional argument was added for amount but not added to history.qml for that payment proof button. Luckily it works from Advanced menu now. My bad for not testing that thoroughly. I'm currently rebuilding my machine so I don't have the gui docker cache right now. I'm pretty sure that `null` just needs to be passed from `getProofClicked` on the history.qml for this payment proof button.

https://github.com/monero-project/monero-gui/blob/master/pages/History.qml#L1723

https://github.com/monero-project/monero-gui/blob/master/MiddlePanel.qml#L69

## selsta | 2022-05-05T15:01:50+00:00
So basically until we fix this users can use the advanced menu now to get the same proof?

## reemuru | 2022-05-05T15:13:05+00:00
@selsta correct I was able to generate `SpendProof` and `OutProof` (tx proof) from the advanced menu v0.17.3.2.
@westz36 could you try putting tx id and recipient address on the advanced tab for tx proof? 

## tczee36 | 2022-05-05T17:35:33+00:00
@selsta @reemuru 
i'll make a quick video of this in a few hours, thanks for the quick reply!
the "generate payment proof" button that didn't work for me is under the 'transactions' tab of the monero-gui

## reemuru | 2022-05-05T17:41:29+00:00
> @selsta @reemuru i'll make a quick video of this in a few hours, thanks for the quick reply! the "generate payment proof" button that didn't work for me is under the 'transactions' tab of the monero-gui

it is ok @westz36 i was able to replicate this. You don't have to upload a video. I'm testing fix now. Could you just let me know if you are able to generate tx proof from the Advanced menu (Prove / Check) ?



## tczee36 | 2022-05-06T03:17:40+00:00
@reemuru hihi,

yes, v0.17.3.2 'check transaction' and 'prove transaction' both works for me.

## reemuru | 2022-05-06T10:03:33+00:00
> @reemuru hihi,
> 
> yes, v0.17.3.2 'check transaction' and 'prove transaction' both works for me.

@tczee36 cool, thanks for checking. Apologies for the inconvenience. I tested a patch that will restore the payment proof button on the transaction list. Next version that button should be working again.

# Action History
- Created by: tczee36 | 2022-05-05T07:59:42+00:00
- Closed at: 2022-06-09T18:57:20+00:00
