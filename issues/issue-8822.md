---
title: closed
source_url: https://github.com/monero-project/monero/issues/8822
author: hugohugo130
assignees: []
labels: []
created_at: '2023-04-13T13:08:01+00:00'
updated_at: '2023-04-14T04:08:51+00:00'
type: issue
status: closed
closed_at: '2023-04-13T13:31:08+00:00'
---

# Original Description
I can't mine with the Monero client
Neither "p2pool" nor another option ("alone") option works
p2pool is stuck
Another option ("Solo") cannot start mining
(Translated by Google. there may be deviations, another option of p2pool should be Solo)

# Discussion History
## selsta | 2023-04-13T13:09:52+00:00
Please go to Settings -> Info and post what is says under

- Version
- Wallet mode

Also what computer hardware and operating system do you have?

## hugohugo130 | 2023-04-13T13:16:59+00:00
Oh, I forgot to mention, I use Windows system, the version is 0.18.2.2, it was release before, but now it becomes "unknown".
CPU: 12th Gen Inter(R) Core(TM) i7-1255U
RAM: 8GBx2 DDR4 SODIMM speed 3200MHz(Hynix)
DISK: 490GB SSD(system) + 2TB HDD
GPU: Intel(R) Iris(R) Xe Graphics
Internet: Ethernet
I use bootstrap node
ip: node.moneroworld.com
port: 18089


## selsta | 2023-04-13T13:19:36+00:00
You need a fully synced local node to mine. You can't use any bootstrap node or remote node.

## hugohugo130 | 2023-04-13T13:24:04+00:00
I am currently not using the boot node and syncing at 53% (it will be very slow after 45%)

## selsta | 2023-04-13T13:24:44+00:00
You can't mine before you are synced up to 100%.

## selsta | 2023-04-13T13:31:08+00:00
I'll close this for now, if you continue to have issues after your node is fully synced up please comment and I can reopen it.

## hugohugo130 | 2023-04-13T13:31:51+00:00
I know, but the bootstrap node shows me 100% synced when in fact it's only 50% synced

## selsta | 2023-04-13T13:32:28+00:00
Remove the bootstrap node from Settings -> Node.

## hugohugo130 | 2023-04-13T13:33:05+00:00
I know, so I removed

## hugohugo130 | 2023-04-13T13:33:52+00:00
I'm now trying to wait for him to sync to 100%. Hope the problem doesn't recur.

## hugohugo130 | 2023-04-13T14:27:22+00:00
there are many
   [195.13.207.253:53616 INC] Sync data returned a new top block candidate: 1524484 -> 2863425 [Your node is 1338941 blocks (5.1 years) behind]
SYNCHRONIZATION started
After that, the block will be synchronized very slowly
Is it normal?

## selsta | 2023-04-13T14:35:01+00:00
Did you set your blockchain location to your HDD to SSD? And yes, this message is normal.

## hugohugo130 | 2023-04-13T14:38:14+00:00
Because I want to be faster and have more space, I put it on SSD before sync progress 45%, and put it on HDD after sync progress 45%

## selsta | 2023-04-13T14:51:07+00:00
It is slow after 45% because you put it on HDD.

## hugohugo130 | 2023-04-13T14:57:30+00:00
The reason Monero is slow to sync is usually validating blocks, and I want a fast and stable sync method.

## selsta | 2023-04-13T15:29:30+00:00
If you want fast sync then put it in your SSD. HDD is slow for sync.

## hugohugo130 | 2023-04-14T00:32:49+00:00
Sync was slow after 45%, so I put it on HDD
I put it on the SSD, and there will be no space after about 45% of the progress
Now I have 4 options
1: Free up SSD space to put down the entire monero blockchain
2: Buy an SSD
3: Maybe it is possible to resize the blockchain to be synced?
4: Continue to put the entire monero blockchain on HDD


## selsta | 2023-04-14T00:44:05+00:00
Did you make sure to prune the blockchain? It will reduce the size to about 60GB.

## hugohugo130 | 2023-04-14T00:53:31+00:00
Yes, because I only want to sync to mine on the monero client, not on other mining software like Xmrig. I have not traded XMR

## hugohugo130 | 2023-04-14T01:02:33+00:00
But how to prune the blockchain?

## nahuhh | 2023-04-14T01:07:06+00:00
1. 'settings > node 
2. startup flag `--prune-blockchain`
3. stop node
4. start node 

you only need to do step 2 once

## hugohugo130 | 2023-04-14T01:07:29+00:00
thx

## plowsof | 2023-04-14T01:12:41+00:00
@hugohugo130 about 500 people receive an email every time we comment here. If you want real time feedback better join IRC. or the Monero Support room on Matrix #monero-support:monero.social

## hugohugo130 | 2023-04-14T02:15:55+00:00
I'm using Hexchat, which channel can I ask on?

# Action History
- Created by: hugohugo130 | 2023-04-13T13:08:01+00:00
- Closed at: 2023-04-13T13:31:08+00:00
