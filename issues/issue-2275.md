---
title: 'ver 0.14.1.0 Wallet shows "Monero sent succesfully: 0 transaction(s)" after
  sending a transaction'
source_url: https://github.com/monero-project/monero-gui/issues/2275
author: pankrats
assignees: []
labels:
- bug
created_at: '2019-07-08T07:10:34+00:00'
updated_at: '2019-07-15T23:41:40+00:00'
type: issue
status: closed
closed_at: '2019-07-15T23:41:40+00:00'
---

# Original Description
Tried to send a tx with Monero-gui using Trezor. 
The process went normally and the transaction was actually sent, but the wallet showed the following:
<img width="981" alt="Screenshot 2019-07-08 at 09 07 48" src="https://user-images.githubusercontent.com/31442634/60789782-359e2600-a160-11e9-8a13-11cf3e1d4cdb.png">




# Discussion History
## dEBRUYNE-1 | 2019-07-08T11:20:24+00:00
+bug

## dEBRUYNE-1 | 2019-07-08T11:20:32+00:00
Paging @ph4r05 as well :-P 

## ph4r05 | 2019-07-08T12:37:29+00:00
@pankrats what is pls your Trezor firmware version?

## ph4r05 | 2019-07-08T12:58:04+00:00
@pankrats and which OS do you use?

## pankrats | 2019-07-08T13:40:39+00:00
I use MacOS Mojave (ver 10.14.5) and Trezor T (fw version 2.1.1).
 
 

## ph4r05 | 2019-07-08T14:13:34+00:00
The problem seems be global, not just Trezor related. 
The PR #2276 fixed it for me.

## rating89us | 2019-07-12T00:12:04+00:00
I have the same issue with macOS and Trezor.

# Action History
- Created by: pankrats | 2019-07-08T07:10:34+00:00
- Closed at: 2019-07-15T23:41:40+00:00
