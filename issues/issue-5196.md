---
title: stagenet forked before mainnet
source_url: https://github.com/monero-project/monero/issues/5196
author: Gingeropolous
assignees: []
labels:
- invalid
created_at: '2019-02-25T03:59:50+00:00'
updated_at: '2019-03-19T14:25:49+00:00'
type: issue
status: closed
closed_at: '2019-03-19T14:25:49+00:00'
---

# Original Description
In blockchain.cpp for v0.14.0.0, the stagenet fork is
```
  { 10, 269000, 0, 1550153694 },
  { 11, 269720, 0, 1550225678 },
```

which means it already happened as far as I can tell. I thought the point of stagenet was always to be a mirror of mainnet?

# Discussion History
## moneromooo-monero | 2019-02-25T09:21:41+00:00
The point of stagenet is to allow people to test without using testnet, which tends to reorg with short notice. If stagenet did not fork before mainnet, people could not test whether their code will break before it's too late.

## moneroexamples | 2019-02-26T00:24:44+00:00
Wasn't the point of stagenet to be run using the same version of monero software as current mainnet?

## moneromooo-monero | 2019-02-26T01:18:27+00:00
Yes. It is, just a couple weeks early so people have a chance to test before the fork.

## moneroexamples | 2019-02-26T01:39:06+00:00
testnet is also on v11 now which can be used for testing forks before they happen. 

## stoffu | 2019-02-26T03:38:47+00:00
I think it's arguable that stagenet should be forked exactly at the same time as mainnet so as to avoid confusions for people wanting to test merchant services on stagenet.

As @moneromooo-monero stated, testnet is for experimenting new consensus rules and thus is expected to get reorged arbitrarily frequently.

Currently, there's no consensus rules being tested, so testnet and stagenet are effectively functioning identically.


## moneroexamples | 2019-02-26T23:39:06+00:00
@stoffu 

I understand that. But if both testnet and stagenet fork before mainnet, then there is a period of time when there is no network to keep testing and developing using current monero software. 

Also its fragments the network, because now there are two stagenets, v9 and v11. And its very confusing. For example, Monerjo wallet support stagenet. But witch one? v9 and v11? Kasisto is also on stagenet (https://amiuhle.github.io/kasisto/#/). But which one? What about xmr.to stagenet facet (https://community.xmr.to/faucet/stagenet/) or this faucet (http://stagenet.xmr-tw.org:38085/)? 

All this is again confusing. If I move openmonero stagenet version to v11 (http://139.162.60.17:81/) it may be out of sync with other stagenet services. If I leave it on v9, same can happen. 

Basally entire stagenet ecosystem that people rely on for development and testing their monero-based services and testing got fragmented. This situation happen last year with testnet, where there were 3 networks. So I was always under impression that stagenet was created to avoid it.  




## moneromooo-monero | 2019-02-26T23:41:57+00:00
There are two because people did not update. If stagenet was forking on the 9th, there would still be two because people do not update. Less likely maybe, because the more you wait, the more likely everyone will have updated, but the point is that it's a matter of people not updating.

But give people moan if we do one way and people moan if we do the other, I'll just ignore stagenet next time, and people who actually use it can choose when it forks.


## moneroexamples | 2019-02-26T23:52:28+00:00
@moneromooo-monero 

Also understand that. There is no golden solution for everything. 


## ndorf | 2019-02-28T16:14:40+00:00
There is an assumption that having two stagenets is a bug, but could it actually be viewed as a feature?

You can use the v9 stagenet to test things that you want to deploy to the mainnet before the fork, and the new stagenet to test things that you want to ensure will work afterwards.



## binaryFate | 2019-03-05T19:09:01+00:00
One thing is to give services and integrators the opportunity to test the fork in advance and in realistic enough conditions thanks to stagenet. I also believe because they have a different use than most users (relying much more on RPC, having different scalability needs, etc), they provide a valuable testing of the Monero fork itself.
A second thing is to make sure that a 1:1 copy of mainnet is always available, _even in the couple of weeks before the fork._

I don't think that these two goals are compatible (unless we add yet another network type), and for me the former is worth giving up on the later.

There was some issue this time between v9 and v11 simply because enough of us on stagenet did not update in time . Let's coordinate better next time!

## moneroexamples | 2019-03-05T23:44:04+00:00
Initially I didn't see the benefit of forking stagenet before mainnet, but now I see. The stagenet v11 has become vital in the last week or so for testing, development and upgrading of projects that I work on for the v11. 

If there was no stagenet at v11, I would have to use testnet which may or may not have features that will end up in mainnet. So having stagenet v11 before mainnet v11 is the closed one can get in terms of testing grounds for the mainnet v11.

## moneromooo-monero | 2019-03-19T14:14:48+00:00
So it's as it's supposed to be.

+invalid

# Action History
- Created by: Gingeropolous | 2019-02-25T03:59:50+00:00
- Closed at: 2019-03-19T14:25:49+00:00
