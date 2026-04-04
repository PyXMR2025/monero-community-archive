---
title: '[TREZOR] Integrated addresses are displayed as plain addresses on device'
source_url: https://github.com/monero-project/monero-gui/issues/3346
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2021-03-02T17:31:05+00:00'
updated_at: '2021-03-20T05:53:12+00:00'
type: issue
status: closed
closed_at: '2021-03-20T05:53:12+00:00'
---

# Original Description
Integrated addresses are displayed as plain addresses on device. This may cause user confusion, as it effectively results in a visual mismatch of addresses. A workaround is available to verify the address, but it is evidently not ideal. 

Relevant thread:

https://www.reddit.com/r/Monero/comments/lvxwvm/integrated_addresses_on_trezor/

# Discussion History
## ph4r05 | 2021-03-03T09:55:16+00:00
As mentioned in /r/:
> We already take care about different address types, Trezor currently handles both subaddresses and integrated addresses. For that we need Monero client to correctly send metadata about addresses to the Trezor (identifying which address is integrated).

I've just checked 
- Trezor Firmware 2.3.6+, 10edcb0d3adbd8ff524133c2671f34f9dc085e8c
- monero-wallet-cli master 964ad0e51a9b034311d9b341f0d8926cc5cc3ec7
- integrated address `ACRXji9tbufJtyQKfdh5KRYNe2WK4aDMBeMwPvkjrm45BQ8bVHurmLyadDx3EiM6AjNH7JJx5TMNrjC4JLZEhszc7usxdicz6qmKxaNy6F` is shown *correctly* (my local testnet setup, thus testnet address)

![t_s1](https://user-images.githubusercontent.com/1052761/109787533-9e2bf780-7c0e-11eb-9890-d68c98928a25.png)
![t_s2](https://user-images.githubusercontent.com/1052761/109787542-a08e5180-7c0e-11eb-8f69-72b18f6e15ef.png)

I did not test the GUI, would be nice if somebody with Trezor and prepared GUI wallet tested that :)

## ph4r05 | 2021-03-03T12:40:09+00:00
Interesting, I can confirm using integrated address in monero-gui shows normal address on Trezor + payment ID.

## ph4r05 | 2021-03-03T14:22:31+00:00
Fix in https://github.com/monero-project/monero/pull/7418 
(bump of the monero submodule is needed in monero-gui once it is merged)

# Action History
- Created by: dEBRUYNE-1 | 2021-03-02T17:31:05+00:00
- Closed at: 2021-03-20T05:53:12+00:00
