---
title: Daemon should mark the alternative chain (after a hard fork) as invalid and
  should automatically reorganize the blockchain such that it syncs to the correct
  chain
source_url: https://github.com/monero-project/monero/issues/3661
author: dEBRUYNE-1
assignees: []
labels: []
created_at: '2018-04-18T14:28:53+00:00'
updated_at: '2018-06-05T11:41:02+00:00'
type: issue
status: closed
closed_at: '2018-06-05T11:41:02+00:00'
---

# Original Description
The current behavior is as follows. If a user forgets to upgrade he'll sync to the alternative chain. However, after the user upgrades, they remain on the alternative chain. Thus, the user has to manually pop blocks in order to end up on the correct chain. Frankly, the current behavior has resulted in a bit of a support nightmare for the whole Monero ecosystem and is absolutely unsustainable going forward, especially if Monero grows further. Thus, desired behavior would be that the daemon marks the alternative chain (after a hard fork) as invalid and automatically reorganizes the blockchain such that it / the user syncs to the correct chain.

# Discussion History
## khelle | 2018-04-18T14:33:18+00:00
If the hard forks are scheduled ahead of the time to the specific block height, then the easiest way to prevent people from getting stuck in altchain would be to mimic Waves / Ethereum behaviour in which node just stops synchronizing at hard fork height and requires node update.

## dnaleor | 2018-04-18T14:37:55+00:00
I think as well that stopping the sync at a certain block height is the easiest fix :)

## fluffypony | 2018-04-18T14:48:46+00:00
There's an easier way, and that's to mimic Bitcoin. When Bitcoin starts up it re-validates the last N blocks, and if the first one is invalid then it steps back another N till it's one a valid chain. So imagine validating the last 100 blocks at daemon startup; if the first one is invalid then step back by 100 blocks from that point and then revalidate.

So, practically, let's say I was running 0.11 and I ended up on the v6 chain, but now I'm way past the v7 fork height. When I upgrade to 0.12 and start up for the first time it re-validates the past 100 blocks using v7 rules (since we're past the fork height), but the first block fails validation. So it steps back and steps back until it finds a valid block, which is a pre-fork-height v6 block, and then syncs from there.

The advantage of this is that it works even when we don't know the fork height in advance.

## el00ruobuob | 2018-04-18T18:08:58+00:00
Stepping back is more elegant (and also fluffier) way.

## italocoin-project | 2018-04-20T06:22:20+00:00
Any commit for fluffy's idea?

## mps01k | 2018-04-21T06:16:23+00:00
would love to see this also. For people that did not upgrade all over at correct time they need to manually pop blocks to before fork to be able and resync

## One-horse-wagon | 2018-04-21T14:36:40+00:00
Fluffy pony's idea is terrific and would solve this issue beautifully.  

A number of people getting into crypto are not computer literate.  When they can't find their coins because they are on an old chain, they panic wildly.  Their experience gives them a bad taste for Monero and they wonder how else are they going to lose their coins?  

## tioann | 2018-04-27T22:56:16+00:00
If I understand fluffy's idea correctly, the point is that the blocks built in the v6 blockchain after the fork are invalid because of the consensus changes introduced by v7, such as the higher ring size and the slow hash change. If no such big changes take place in one of the next forks, the previous version block may be valid under the new rules and the fluffy search will not backtrack. Am I missing something?

## One-horse-wagon | 2018-04-28T14:57:12+00:00
If you read his idea carefully, a new fork version will have different validating rules starting with hard fork block number so and so.  If you continued running the old version after the hard fork, you created invalid blocks.  

So when you upgrade to the new version, those blocks won't validate.  The program will then automatically go back in steps until it finds blocks that will validate.  If need be, it will go all the way back to the hard fork block number and then start there.

It's an elegant solution.

## jonathancross | 2018-05-03T15:51:03+00:00
I believe @tioann was asking about how we can be sure that blocks created by older clients will **_always_** be invalid according to new clients.

This is the best I have come up with: each block contains a block **_version number_** which is incremented between forks. Blocks on the "wrong" chain will be marked invalid by upgraded clients and will therefore trigger the step-back behavior (_regardless of block contents_).  Eg: version `6` blocks should be invalid after block height `1546000`. (please correct me if I am wrong :)

## r3lik | 2018-05-24T18:23:40+00:00
I'm trying to deal with this right now...what is the solution? I'm running monerod and I don't see a pop-blocks option

## italocoin-project | 2018-05-24T18:29:51+00:00
This was merged download latest commit

## moneromooo-monero | 2018-06-05T11:04:40+00:00
+resolved

# Action History
- Created by: dEBRUYNE-1 | 2018-04-18T14:28:53+00:00
- Closed at: 2018-06-05T11:41:02+00:00
