---
title: Signature mismatch, connection will be closed
source_url: https://github.com/monero-project/monero/issues/3106
author: SpliffyMap
assignees: []
labels: []
created_at: '2018-01-11T20:38:21+00:00'
updated_at: '2018-01-15T17:56:36+00:00'
type: issue
status: closed
closed_at: '2018-01-15T17:51:27+00:00'
---

# Original Description
Hello. I working on Monero app for android for couple a weeks. So first I need to understand how Monero source code works. I compiled it and it works, great! And suddenly I understand that current blockchain is 27 GB. Little too large for testing on my testing seed nodes, testnet not good too.

So what I did. I changed Network ID and it's not downloading current chain anymore. Great!
![selection_032](https://user-images.githubusercontent.com/35120072/34845901-258a02ee-f71f-11e7-9a4d-0630d07bb574.png)

I have only two testing nodes so looks like I need to change min nodes. Also IP addresses.
![selection_034](https://user-images.githubusercontent.com/35120072/34845913-2f0aead6-f71f-11e7-9936-1017608f1f99.png)

Just in case removed DNS node lists.
![selection_033](https://user-images.githubusercontent.com/35120072/34845955-5b725f6e-f71f-11e7-9fd5-8b27e985413f.png)

So it started new chain. Good start for testing! But no, android library doesn't working. I was thinking, maybe I do something wrong. Just in case tested monero-ui. Compiled, connected to node ip and got this error.
![selection_042](https://user-images.githubusercontent.com/35120072/34846110-cb83af24-f71f-11e7-990a-cb0e0f9ac7be.png)

So my question, how Network ID change made this signature mismatch problem and how to deal with it and fix it? Thank you, I'm very new guy here!

# Discussion History
## dEBRUYNE-1 | 2018-01-12T14:11:24+00:00
As a sidenote, it's more trivial to set up a private testnet. Guide here (needs some tweaking though, as it's fairly outdated):

https://moneroexamples.github.io/private-testnet/

## SpliffyMap | 2018-01-12T14:14:42+00:00
But if I choose my way, how to make signature match?

## jtgrassie | 2018-01-15T12:48:42+00:00
This smells like coin-fork questions.

## dEBRUYNE-1 | 2018-01-15T16:50:11+00:00
@SpliffyMap Is this for a fork of Monero or?

## jtgrassie | 2018-01-15T16:59:08+00:00
Why else would someone need to change the network ID? And be asking about genesis block creation on another Monero fork (https://github.com/sumoprojects/sumokoin/issues/56)? IMO this issue needs closing as invalid.

## SpliffyMap | 2018-01-15T17:56:36+00:00
No matter, just downloaded 54 GB of data :+1: All good :+1: 

# Action History
- Created by: SpliffyMap | 2018-01-11T20:38:21+00:00
- Closed at: 2018-01-15T17:51:27+00:00
