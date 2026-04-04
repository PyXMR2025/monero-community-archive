---
title: Error writing wallet from hardware device. Check application logs.
source_url: https://github.com/monero-project/monero-gui/issues/3279
author: efb4f5ff-1298-471a-8973-3d47447115dc
assignees: []
labels: []
created_at: '2020-12-22T09:44:44+00:00'
updated_at: '2020-12-22T11:41:00+00:00'
type: issue
status: closed
closed_at: '2020-12-22T11:41:00+00:00'
---

# Original Description
Hi i wanted to create a new wallet from my Trezor T, but i got this error. How do i fix this?
Im running the latest firmware version and im using the latest windows version of the GUI Wallet 

# Discussion History
## selsta | 2020-12-22T10:29:52+00:00
There should be a second error message. Can you post that too?

## efb4f5ff-1298-471a-8973-3d47447115dc | 2020-12-22T11:01:16+00:00
Thanks for the quick response @selsta, but the issue seems to resolved itself. The only thing i did is restart my PC.

## efb4f5ff-1298-471a-8973-3d47447115dc | 2020-12-22T11:26:48+00:00
Hi @selsta, i accidentally logged out of the wallet and tried to login, but i receive an error.
Could not open wallet: Could not connect to the device Trezor.
I dont understand why i get this because my Trezor is still connected to the PC.

## selsta | 2020-12-22T11:27:42+00:00
Do you use the Trezor web wallet simultaneously?

## efb4f5ff-1298-471a-8973-3d47447115dc | 2020-12-22T11:27:58+00:00
No i do not. I do have the Trezor Suite, but that program is not running.

## selsta | 2020-12-22T11:29:13+00:00
Try installing the latest version of Trezor bridge: https://wiki.trezor.io/Trezor_Bridge

## efb4f5ff-1298-471a-8973-3d47447115dc | 2020-12-22T11:35:10+00:00
This seems to have worked. Thanks!
Do i always have to start the bridge first in order for the application to work?

# Action History
- Created by: efb4f5ff-1298-471a-8973-3d47447115dc | 2020-12-22T09:44:44+00:00
- Closed at: 2020-12-22T11:41:00+00:00
