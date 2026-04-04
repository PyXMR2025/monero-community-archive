---
title: Block 1288623 bug - clients performing IBD get stuck on dead chain
source_url: https://github.com/monero-project/monero/issues/2562
author: Gingeropolous
assignees: []
labels:
- duplicate
created_at: '2017-10-02T13:44:18+00:00'
updated_at: '2017-10-19T16:06:23+00:00'
type: issue
status: closed
closed_at: '2017-10-19T16:06:23+00:00'
---

# Original Description
There's no logs, its been reported multiple places and times. 

as @hyc mentioned elsewhere, indicated in

https://github.com/monero-project/monero/issues/2449

https://github.com/monero-project/monero/issues/2451

https://www.reddit.com/r/Monero/search?q=1288623&restrict_sr=on

and its 7 blocks after the 1288516 hardfork of RingCT introduction. 


# Discussion History
## moneromooo-monero | 2017-10-02T14:24:49+00:00
Any evidence it's not fixed by 2492 ?

## hyc | 2017-10-02T14:33:56+00:00
PR #2492 appears to be about fixing a crash. These reports don't seem to be about crashes, and most likely could be cleared up by deleting p2pstate.bin.

## moneromooo-monero | 2017-10-02T14:36:10+00:00
They're both about crashes (the ones on github anyway).

## hyc | 2017-10-02T14:50:42+00:00
Ah, right. Not sure how those people would have tested PR#2492, they're only using v0.11.0.0 official binaries.

## moneromooo-monero | 2017-10-02T14:51:56+00:00
One of those on reddit is not a crash though, but could plausibly be this as the size of the tx hash array is dynamic. The other is unknown, not enough data to tell.

## moneromooo-monero | 2017-10-02T14:53:10+00:00
Sure, I mean I won't investigate another thing unless I have some evidence there *is* another thing :)

## moneromooo-monero | 2017-10-02T16:08:19+00:00
If there is a report for this which does not go away after using 2492 (which is merged now), then please ask to restart with: --log-level 1,net.cn:DEBUG,\*p2p\*:DEBUG

## dEBRUYNE-1 | 2017-10-03T14:53:01+00:00
@hyc: Deleting `p2pstate.bin` doesn't seem to help here. In addition, I've noticed that often even popping blocks doesn't help. 

@moneromooo-monero: [Here's](https://paste.fedoraproject.org/paste/VDXcdXmFw7BBDT~9CRKItA
) a log from someone who used a `monerod` from #2492 (he used the buildbot binaries). Full thread can be read here:

https://www.reddit.com/r/Monero/comments/73fij0/wallet_keeps_disconnecting/

## Gingeropolous | 2017-10-09T03:30:44+00:00
yet another

https://www.reddit.com/r/Monero/comments/7562kx/wallet_gui_daemon_is_crashing/

## moneromooo-monero | 2017-10-15T13:28:44+00:00
All evidence is pointing to this being a duplicate. Can you find any pointing to it not being ?

## moneromooo-monero | 2017-10-19T16:02:26+00:00
I've been pointing a few people having that problem to a build with those fixes above, and it always worked. So this is indeed a dupe.

+duplicate


# Action History
- Created by: Gingeropolous | 2017-10-02T13:44:18+00:00
- Closed at: 2017-10-19T16:06:23+00:00
