---
title: Wallet password prompt can be brute forced
source_url: https://github.com/monero-project/monero-gui/issues/2608
author: rating89us
assignees: []
labels:
- invalid
created_at: '2019-12-15T23:39:04+00:00'
updated_at: '2025-04-05T17:43:35+00:00'
type: issue
status: closed
closed_at: '2020-02-13T01:18:46+00:00'
---

# Original Description
There should be increasing waiting delays after wrong passwords are entered.
![image](https://user-images.githubusercontent.com/45968869/70871146-d51adc80-1f7a-11ea-977f-8b812a9c3516.png)

# Discussion History
## tobtoht | 2019-12-15T23:47:16+00:00
Anyone attempting to bruteforce a wallet wouldn't be typing passwords manually into the GUI.

## selsta | 2019-12-16T00:03:20+00:00
Yep, any visual delays can easily be bypassed with a custom wallet/software. Don’t think there is anything we can do here.

## selsta | 2020-02-13T01:12:42+00:00
Closing this as there is nothing we can do about this. Use safe passwords.

+invalid

## LimerBoy | 2023-09-28T12:26:47+00:00
good way it's implement custom iterations count for password derivation methods.

## selsta | 2023-09-28T12:28:31+00:00
@LimerBoy monero supports this by setting KDF rounds

## Manus84 | 2025-03-24T21:20:37+00:00
> [@LimerBoy](https://github.com/LimerBoy) monero supports this by setting KDF rounds

But what is the best number of "KDF rounds" to set when creating a new wallet in order to have a wallet that can resist brute force attacks?

## selsta | 2025-04-05T17:43:34+00:00
@Manus84 the higher you set it, the longer it will take to open your wallet. but it will also be more difficult to brute-force. In general it is enough to set a strong password without changing the KDF parameter.

# Action History
- Created by: rating89us | 2019-12-15T23:39:04+00:00
- Closed at: 2020-02-13T01:18:46+00:00
