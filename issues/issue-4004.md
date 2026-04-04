---
title: 'Can''t create transaction: ring size / bulletproof rangesig'
source_url: https://github.com/monero-project/monero-gui/issues/4004
author: pluja
assignees: []
labels: []
created_at: '2022-08-14T07:46:08+00:00'
updated_at: '2022-08-31T21:25:33+00:00'
type: issue
status: closed
closed_at: '2022-08-14T11:58:33+00:00'
---

# Original Description
I'm getting an error when trying to create a transaction from Monero GUI. I'm on the latest version v18.1.0, also made sure Trezor device is on latest firmware and the node I am connected to is updated to latest monero network upgrade.

The error:

> Can't create transaction: internal error. An output in this transaction was previously spent on another chain with ring size 16, it cannot be spent now with ring size 11 as it is smaller: use a higher ring size.

The Trezor gets stuck at "Processing outputs 2/2".

After testing to perform the transaction a second time I got the following error:

> E Can't create transaction:  unexpected error: Cannot deserialize bulletproof rangesig

# Discussion History
## pluja | 2022-08-14T11:58:33+00:00
Nevermind, it's because Trezor firmware update is not available yet until August 17.

Sorry and thank you all for the hard work. Awesome progress!

## michaelraasch | 2022-08-15T19:06:14+00:00
> Nevermind, it's because Trezor firmware update is not available yet until August 17.
> 
> Sorry and thank you all for the hard work. Awesome progress!

The new firmware 2.5.1 is already out.
I still have the issue as mentioned above with Trezor Suite v22.7.3 and Monero GUI 0.18.1.0-release (Qt 5.12.8)

## selsta | 2022-08-15T19:07:18+00:00
Please see the release notes: https://github.com/monero-project/monero-gui/releases/tag/v0.18.1.0

Firmware v2.5.2 is required, v2.5.1 has been out since May.

## liemgo | 2022-08-15T20:36:47+00:00
Hello, I think I have the same problem. The last three days I have updated trezor t to its lates firmware. Also updated my  monero gui wallet and let it sync for three days until it showed 
<img width="622" alt="屏幕快照 2022-08-15 下午12 24 47" src="https://user-images.githubusercontent.com/111313963/184713957-c003b98d-7b18-4ca9-928b-07a3b4bb6b9c.png">
 my funds. But when I want to send some xmr I get an error message that says:

Error
Can't create transaction: unexpected error: Cannot deserialize bulletproof rangesig

I have turned off and on my computer but no effect. can anyone advise? thanks in advance

## selsta | 2022-08-15T20:41:22+00:00
@liemgo You have to wait for Trezor to release firmware v.2.5.2, it should be out in 2 days.

## liemgo | 2022-08-15T21:04:19+00:00
Thank you @selsta then I will wait.

## M1nistry | 2022-08-20T06:23:58+00:00
Running v2.5.2 I still receive
Error
Can't create transaction: unexpected error: Cannot deserialize bulletproof rangesig
Have reinstalled fw once and issue persists. Was just receiving 'failure' on 2.5.1

## AlesRFK | 2022-08-20T20:28:06+00:00
XMR: 0.18.1.0-unknown (Qt 5.15.5)
T: v2.5.2
After sync and some errors I've reconnected device and node and sended multisig tx.

## selsta | 2022-08-20T20:33:52+00:00
@M1nistry Can you go to Settings -> Info and post which wallet mode and version you are using?

@AlennGK Can you rephrase your issue? Were you able to send successfully?

## AlesRFK | 2022-08-20T20:38:10+00:00
@M1nistry I'm using simple mode and yes I was able to successfully send XMR to my other adress and exchange.

## selsta | 2022-08-20T20:40:25+00:00
@AlennGK If you have issues again please set a manual remote node https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

Simple mode connects to a random remote node which means it can connect to a node that didn't update for v0.18. This will be improved in the next release.

## michaelraasch | 2022-08-20T20:47:53+00:00
> XMR: 0.18.1.0-unknown (Qt 5.15.5) T: v2.5.2 After sync and some errors I've reconnected device and node and sended multisig tx.

Where did you get 2.5.2 from? I can'r see it it in the changelog https://github.com/trezor/trezor-firmware/blob/master/core/CHANGELOG.md 
And my Trezor Suite also claims that 2.5.1 is the latest.

## selsta | 2022-08-20T20:50:59+00:00
@michaelraasch Trezor is doing a staged rollout.

- https://blog.trezor.io/trezor-suite-and-firmware-updates-august-2022-bitcoin-only-firmware-in-trezor-suite-a4e3d76214c1
- https://github.com/trezor/trezor-firmware/blob/core/v2.5.2/core/CHANGELOG.md

## michaelraasch | 2022-08-22T20:25:04+00:00
> @michaelraasch Trezor is doing a staged rollout.
> 
> * https://blog.trezor.io/trezor-suite-and-firmware-updates-august-2022-bitcoin-only-firmware-in-trezor-suite-a4e3d76214c1
> * https://github.com/trezor/trezor-firmware/blob/core/v2.5.2/core/CHANGELOG.md

@selsta I can confirm it works now. Thanks for your help.

## AlesRFK | 2022-08-31T21:25:33+00:00
@michaelraasch manual download and custom install because the rollout.

# Action History
- Created by: pluja | 2022-08-14T07:46:08+00:00
- Closed at: 2022-08-14T11:58:33+00:00
