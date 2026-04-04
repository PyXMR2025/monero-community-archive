---
title: '[Trezor] - Entering wallet when T2 and T1 is connected'
source_url: https://github.com/monero-project/monero-gui/issues/2112
author: vir-satoshi
assignees: []
labels:
- invalid
created_at: '2019-04-24T12:21:09+00:00'
updated_at: '2019-04-24T13:37:33+00:00'
type: issue
status: closed
closed_at: '2019-04-24T12:36:42+00:00'
---

# Original Description
If you have 2 Trezor devices connected (T1 and T2) it is impossible to enter the wallet. 

![image](https://user-images.githubusercontent.com/37402655/56658686-8c38af80-669b-11e9-8c9e-8402bb202401.png)

The Monero wallet does not accept the wallet password. 

I have heard you guys does not have both Trezor devices, so this might be difficult for you to reproduce. We would really like to help you with this, so we can send you the T1 device of course. If @ph4r05 is reading, we will give you a T1 next time you stop by.

# Discussion History
## selsta | 2019-04-24T12:23:56+00:00
T1 is the older model that doesn’t support Monero?

## vir-satoshi | 2019-04-24T12:25:11+00:00
Yes, it has nothing to do with Monero, but still...

## selsta | 2019-04-24T12:27:50+00:00
Ok, thanks for reporting :) This seems to be resolved here: https://github.com/monero-project/monero/pull/5476

+invalid

## ph4r05 | 2019-04-24T13:37:33+00:00
Yep the PR you mention should fix this. T1 is not allowed anymore (was a bug).

CLI has a parameter enabling to pick particular Trezor to use, but GUI has no device selection, unfortunately. It just picks the first available T2 device. After discussion with @prusnak we decided to leave this as it is now. However, expert users can select the device by setting TREZOR_PATH env var (works after the PR is merged).

# Action History
- Created by: vir-satoshi | 2019-04-24T12:21:09+00:00
- Closed at: 2019-04-24T12:36:42+00:00
