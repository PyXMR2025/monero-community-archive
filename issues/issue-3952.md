---
title: Daemon stuck at block height 2651490
source_url: https://github.com/monero-project/monero-gui/issues/3952
author: C0smicfrog
assignees: []
labels: []
created_at: '2022-06-23T11:00:59+00:00'
updated_at: '2022-06-24T21:53:33+00:00'
type: issue
status: closed
closed_at: '2022-06-24T21:53:33+00:00'
---

# Original Description
Hello, I have an issue, my node is stuck at block height 2651490 since 24h, so I can't transfer my XMR...

I have Windows 10, use Monero gui v0.17.3.2

I'm not very techical, the node/wallet worked well for several days, but stuck yesterday, I don't know why, and I can't re-sync it..

Try to stop/restrat several time, trying several flag that I saw on forum but.. nothing work..

Can you please help me with this issue ?

Cheers

![image](https://user-images.githubusercontent.com/106738707/175282765-3ebfdc83-95f2-4d9f-9026-19aa6fbfcbd8.png)

![image](https://user-images.githubusercontent.com/106738707/175283140-40bec28c-bb0e-492d-a1aa-30b59844186c.png)

![image](https://user-images.githubusercontent.com/106738707/175282915-eed3e07a-21f5-4be8-ba02-6a159ed53789.png)


# Discussion History
## selsta | 2022-06-23T19:59:41+00:00
Can you post the output of "status" and "sync_info" ?

## C0smicfrog | 2022-06-23T20:09:02+00:00
just now :

![image](https://user-images.githubusercontent.com/106738707/175388867-78bfff4a-d96a-46f1-8fe2-e3c0564bf218.png)


## selsta | 2022-06-23T20:11:03+00:00
You don't have any peers. Are you using a VPN? Some kind of firewall?

## C0smicfrog | 2022-06-23T20:12:27+00:00
No VPN, and no special Firewall.. just the Windows one and Norton 

## selsta | 2022-06-23T20:14:23+00:00
Can you try to add an exception to Norton? I assume that's the issue.

## C0smicfrog | 2022-06-23T20:18:09+00:00
Already did, and the node was synced during several days.. and yesterday it stuck at this block height..
I'm gonna check if the exception is always here..
What are the files/folders exactly do I have to put in the exceptions ?

## selsta | 2022-06-23T22:26:38+00:00
I'm not a Norton user myself so I can't help you here. Going by your screenshot no peers get blocked, that likely means that it's a network related issue, not a database one.

## C0smicfrog | 2022-06-24T21:47:04+00:00
It worked, I desabled the Norton Firewall for 15 min, and succeed to connect to new peers, and sync again.

But it's not secure, to open the Firewall, I receive strange attack (one that Norton blocked)
How to allow peers connection without put my PC at risk..?

## selsta | 2022-06-24T21:53:33+00:00
Anti viruses like to block everything monero related, so I'm confident that this "attack" was a false positive.

Add an exception for monero or add an exception for port 18080 (used for monero p2p traffic).

Closing this as this is an issue with your firewall setup and not anything monero related.

# Action History
- Created by: C0smicfrog | 2022-06-23T11:00:59+00:00
- Closed at: 2022-06-24T21:53:33+00:00
