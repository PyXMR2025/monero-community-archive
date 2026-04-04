---
title: decoy distribution algo
source_url: https://github.com/monero-project/monero/issues/6327
author: anonproject
assignees: []
labels: []
created_at: '2020-02-09T15:59:32+00:00'
updated_at: '2021-08-15T04:00:48+00:00'
type: issue
status: closed
closed_at: '2021-08-15T04:00:48+00:00'
---

# Original Description
I have read that there was a vulnerability in monero (well, actually a serious bug) on decoy distribution so that the latest output was almost always the real one.  Then the fix has been made so now it should pickup more decoys from the recent time.
I have a question on the nature of this new distribution algo.  For example if I am doing some churning to "distance" one txid from another what is the proper way to do it?  How long should I wait between the transactions?  Or should I monitor the blockchain to see if someone used one of my txid as a decoy and only after that make my tx?  What is the right strategy over here?

**UPD**:

The purpose of churning in my case is to receive the XMR from Alice and send it to Bob in such a way so Bob would have no idea it came from Alice, PROVIDED Bob knows the txid of all Alices's transactions.  Monero doesn't seem to provide such anonymity because the privacy set is only 11.  The matters are even worse if I received not one, but 100 transactions from Alice.  So if I would make one coinjoin transaction, each input containg Alice's txid Bob would know for sure the XMR came from Alice (the ring signatures would not provide any help here).
Correct?
So the only solution then is to do churning.
Correct?
If so, how to do it right?

**UPD2:**
The info provided in the following link is accurate?
https://monero.stackexchange.com/a/8489

**UPD3:**
I briefly looked into the code and it is pretty hard to understand what exactly is going on and WHY.  It is harder still to derive any recommendations on churning.
I do understand that the question of mine probably doesn't belong here, but it is pretty important question because plausible deniability provided by rings signatures is not enough if the attacker knows txids on input and output of the blockchain.  I believe one have to use Monero blockchain as a mixer via churning.  The question is how to do it correctly.

# Discussion History
## moneromooo-monero | 2020-02-13T20:10:12+00:00
It's not clear yet. MRL is working on a model for this to inform best practices.

## SamsungGalaxyPlayer | 2020-02-13T20:57:41+00:00
The method described in that StackExchange post is dated. I recommend that this issue is closed since it's a better topic for MRL or elsewhere.

# Action History
- Created by: anonproject | 2020-02-09T15:59:32+00:00
- Closed at: 2021-08-15T04:00:48+00:00
