---
title: How mine with local node and GUI Wallet ?
source_url: https://github.com/monero-project/monero-gui/issues/4542
author: DirtyGadget
assignees: []
labels:
- question
created_at: '2025-12-10T11:22:27+00:00'
updated_at: '2025-12-17T17:44:21+00:00'
type: issue
status: closed
closed_at: '2025-12-17T17:42:55+00:00'
---

# Original Description
Hi,

I have `monerod` up and running on the **testnet** network.

I would like to start mining, so I tried with the `Monero GUI Wallet` that is successfully connect to my local node ( 127.0.0.1 ) 

![Image](https://github.com/user-attachments/assets/299a809f-a7a4-4c82-ac5e-b3f0f321e278)


But I get

![Image](https://github.com/user-attachments/assets/e4125a81-78b3-4993-88a9-f55292b5c815)



Should I run something else ? `Monero CLI Wallet` ?

# Discussion History
## selsta | 2025-12-10T11:24:25+00:00
If you set your monero-gui to Testnet, then go to Settings -> Node and select local node it will automatically start a testnet node, then you should also be able to mine.

## DirtyGadget | 2025-12-12T08:21:30+00:00
Thanks @selsta , but that the thing, I have already a **testnet** running, I don't want that the GUI wallet create a second one...
or will it realize/check that a `monerod` is already running ?

## DirtyGadget | 2025-12-13T06:42:50+00:00
update proposal , if an user set 127.0.0.1 then it should be considered as **local node**

For my part, you can close this topic.

## selsta | 2025-12-17T17:44:21+00:00
@DirtyGadget When "local node" is selected it is assumed the node runs on the same machine without any restrictions. If "remote node" is selected, it is assumed the other node is restricted and monero-gui does not allow you to interact with it. There would be ways to change this but it would make things more complicated for an edge case.

# Action History
- Created by: DirtyGadget | 2025-12-10T11:22:27+00:00
- Closed at: 2025-12-17T17:42:55+00:00
