---
title: Monero Daemon not sync and not showing my balance will pay $2 for fixing help
source_url: https://github.com/monero-project/monero-gui/issues/4311
author: AMbns01
assignees: []
labels: []
created_at: '2024-05-01T12:48:21+00:00'
updated_at: '2024-05-03T13:07:57+00:00'
type: issue
status: closed
closed_at: '2024-05-03T13:07:56+00:00'
---

# Original Description
I downloaded and created monero wallet fron get monero and bought monero from changnow but now my balance is not showing as my daemon not sync. Please help
![XMR](https://github.com/monero-project/monero-gui/assets/168646452/bfc4ba5e-4eb8-4194-ae20-c30b571b08af)


# Discussion History
## selsta | 2024-05-01T12:50:34+00:00
Your balance won't show up until you have a fully synchronized daemon and wallet.

Can you go to Settings -> Info and share

- Version
- Wallet mode
- Wallet restore height

## AMbns01 | 2024-05-01T12:55:07+00:00
Version: 0.18.3.3-unknown (Qt 5.15.13)
Mode: Advanced mode (Local node)
Restore Height: 3119668


## selsta | 2024-05-01T12:57:06+00:00
You selected local mode, this means you first have to fully sync up with the network. This can take around a day. Once both bars are at 100% your balance should show up.

## AMbns01 | 2024-05-01T12:59:09+00:00
they just complete for a while but again starts from start and no update


## AMbns01 | 2024-05-01T12:59:19+00:00
how to make it fast

## selsta | 2024-05-01T13:09:01+00:00
You can go to Settings -> Node -> Remote node and then add a remote node from this list: https://monero.fail

Or you can simply wait for your local node to sync up.

## AMbns01 | 2024-05-01T15:26:02+00:00
![sync](https://github.com/monero-project/monero-gui/assets/168646452/bb5bbeaa-c1fa-44ed-a72b-1bf1da5d99c3)
It shows complete when i am offline is this ok can it show balance while its offline as it never show my balance since i deposited due to no commplete sync

## selsta | 2024-05-01T15:27:49+00:00
You need an internet connection and wait for it to fully sync up. If you don't have an internet connection it won't show you the correct progress.

## AMbns01 | 2024-05-01T15:28:38+00:00
can i make the process fast


## selsta | 2024-05-01T15:29:13+00:00
If you want your own node, no. If you want to use a remote node then follow the steps I explained in this comment: https://github.com/monero-project/monero-gui/issues/4311#issuecomment-2088439738

## AMbns01 | 2024-05-01T15:31:05+00:00
is there any risk using remote node

## AMbns01 | 2024-05-01T15:36:36+00:00
Please help me brother and also how can i give you the $2 as gift


## selsta | 2024-05-01T15:38:12+00:00
Using a remote node is slightly worse for privacy, but it is faster, since you don't have to wait for your node to sync up.

## AMbns01 | 2024-05-01T15:45:52+00:00
How much risky is it and also let me know about thank you gift

## selsta | 2024-05-01T16:05:09+00:00
See the explanation here: https://monero.stackexchange.com/a/10701

> thank you gift

This is not necessary but thank you!

## AMbns01 | 2024-05-01T17:23:14+00:00
sorry i didnt understand the explanation can you please describe what if i use remote node also will it permanent or temporary and i can change it later

## selsta | 2024-05-01T17:24:26+00:00
Yes, you can change between local and remote node whenever you want.

## AMbns01 | 2024-05-01T17:26:54+00:00
and what is the risk if i use remote node


## AMbns01 | 2024-05-01T17:32:38+00:00
can you please describe

## selsta | 2024-05-01T17:35:06+00:00
A malicious remote node can for example collect your IP address, make it so that your balance doesn't show up, make it so that you can't send transactions, etc.

The risk is quite low but still a possibility.

## AMbns01 | 2024-05-01T17:37:44+00:00
what is remote node i have rdp can i use it for that


## AMbns01 | 2024-05-01T17:43:41+00:00
once the wallet sync fully completed will it require the sync again and if yes then when

## selsta | 2024-05-01T18:01:21+00:00
> once the wallet sync fully completed will it require the sync again and if yes then when

Only new blocks, per day around 720 blocks get added so each day these 720 blocks have to be synced.

## AMbns01 | 2024-05-01T18:10:25+00:00
is there any tips to speed up the process


## AMbns01 | 2024-05-03T10:14:52+00:00
Hello brother i need some help my daemon started sync there are 443000 blocks remaining but there is a problem i got my storage full can i change the drive for this and if i change the location will the sync will start from beginning? 

## selsta | 2024-05-03T13:07:56+00:00
#4312 

# Action History
- Created by: AMbns01 | 2024-05-01T12:48:21+00:00
- Closed at: 2024-05-03T13:07:56+00:00
