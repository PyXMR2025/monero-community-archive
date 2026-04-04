---
title: 'Seed nodes '
source_url: https://github.com/monero-project/monero/issues/6422
author: sumogr
assignees: []
labels: []
created_at: '2020-04-02T21:36:52+00:00'
updated_at: '2020-07-08T23:00:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This is not a bug description but i think its the proper place to put it.
I see there is an urge for adding more hardcoded seed nodes, I think monero should consider adding a   seed node on an HK server for mainland China access since i am willing to bet chinese users behind the great wall have a hard time reaching the current seed nodes which are placed either in european or us servers. (I would add one but the data rates are too damn expensive :D)

# Discussion History
## selsta | 2020-04-02T21:39:06+00:00
> adding more hardcoded seed nodes

We talked about this in the latest meeting and working on it. There are already 3 PRs with new seed nodes. A seed node in China sounds like a good idea.

## sumogr | 2020-04-02T21:40:33+00:00
A mainland China is kind of hard, expensive and risky but one in Hong Kong would do just fine

## binaryFate | 2020-04-08T15:47:57+00:00
Are you confident that HK IPs are always considered "inside" firewall restrictions?

I may get a VPS there from my own pockets to provide a stable (+ possibly seed) node, but only if it is certain to be useful.

## ghost | 2020-04-08T16:04:35+00:00
Chinese firewall does not block base on location of IPs, but on the type of services using those IPs. For example. no matter where you set up a Tor bridge, it will be blocked instantly, since the bridge list is public. If they want to block your IP, which is also public in the source code, they could. Just add a "monero scanning script" done.

Do not add a seed node in China, you are feeding the firewall. Add better support for socks5 and tor.

## moneromooo-monero | 2020-04-09T11:36:23+00:00
> Do not add a seed node in China, you are feeding the firewall.

Can you expand on that ?

## ghost | 2020-04-09T12:58:02+00:00
~~Instead of tear down a wall, of which the primary goal is to limit the freedom of speech. You will be working with it, setting up factories, productions, finance, generating taxes, that feed the very government that built it.~~

Sorry my account was hacked. Please come, I invite you. China is a free and loving country.

## fluffypony | 2020-04-09T14:45:19+00:00
> ~Instead of tear down a wall, of which the primary goal is to limit the freedom of speech. You will be working with it, setting up factories, productions, finance, generating taxes, that feed the very government that built it.~
> 
> Sorry my account was hacked. Please come, I invite you. China is a free and loving country.

That makes no sense whatsoever. The Chinese government could just run their own node and check the whitelist / graylist for Chinese IP addresses. They may already do so. Having or not having a seed node in China is irrelevant to that.

## Svaag | 2020-04-25T20:35:47+00:00
Have you considered adding IPv6 seed nodes?

## moneromooo-monero | 2020-07-08T23:00:13+00:00
Hong Kong is now inside the firewall...

# Action History
- Created by: sumogr | 2020-04-02T21:36:52+00:00
