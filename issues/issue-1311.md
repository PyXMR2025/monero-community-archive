---
title: 'Monero Tech Meeting #150 - Monday, 2025-12-15, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1311
author: rbrunner7
assignees: []
labels: []
created_at: '2025-12-12T15:58:55+00:00'
updated_at: '2025-12-15T18:50:58+00:00'
type: issue
status: closed
closed_at: '2025-12-15T18:50:58+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1308).


# Discussion History
## rbrunner7 | 2025-12-15T18:50:58+00:00
````
<rbrunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1311
<sneedlewoods> hey
<rbrunner7> Hmm ... people busy Christmas shopping maybe :)
<jberman> waves
<jberman> sorry
<rbrunner7> Alright, what are the reports about last week?
<sneedlewoods> while updating https://github.com/monero-project/monero-gui/pull/4437 I also fixed some issues I didn't notice before
<sneedlewoods> began to look back into the problem with setting restore height on wallet creation with the GUI
<sneedlewoods> also wrote a CCS proposal, but haven't made a merge request yet. Maybe someone wants to have a look first and give feedback https://repo.getmonero.org/SNeedlewoods/ccs-proposals/-/blob/SNeedlewoods-03_part-time_dev_work-Q1-26/SNeedlewoods-03_part-time_dev_work-Q1-26
<rbrunner7> Do you have something reviewable already for the Wallet API and the use of that in the CLI wallet?
<rbrunner7> Will have a look at your CCS proposal
<sneedlewoods> Not sure I understand, but this is "reviewable" I guess https://github.com/monero-project/monero/pull/10233
<rbrunner7> I mean you don't plan to immediately change it again significantly, what could make an on-going review invalid so to say
<jberman> Solved some lingering issues with the daemon/wallet2 noticed during stressnet (sporadic repeated double spend errors in the wallet, some connection drop issues), <jberman> investigated/identified a cause of what looked like a regression in sync perf (depends builds are slow, GUIX builds fast), implemented jeffro's review comments on <jberman> multithreaded verify. Continuing this week with tx relay v2, getting all outstanding PR's shaped up, and may dig into a segfault reported by ofrn
<sneedlewoods> the only thing I'm planning to fix is "outgoing pending txs not showing up in show_transfers", else it should be pretty much done
<sneedlewoods> I assume some things will change because of review though
<rbrunner7> "tx relay v2" is a pretty big change, right?
<rbrunner7> Or maybe I confuse it with something else
<jberman> it is, it's mostly implemented by 00xfffc already, but I have some changes in mind pointed out in review that I want to implement
<jberman> and plan to work with 0xff on that
<jberman> the current PR for reference: https://github.com/seraphis-migration/monero/pull/184
<rbrunner7> That could be quite a big step forward
<rbrunner7> Especially in times of many transactions
<jberman> yep, we also apparently have some relay issues in the daemon, so I want to see this in the daemon first and then tackle the relay issues
<jeffro256> Howdy sorry I'm late 
<rbrunner7> Not sure what you mean with "relay issues"
<jberman> https://github.com/seraphis-migration/monero/issues/163
<jberman> likely due to frequent disconnects, eventually the node ended up with many txs that are in a "not relayed" state. These were there for over 12hrs, and (strangely) causing double spend errors via rpc
<rbrunner7> Ah, ok. Might be present for quite a while already, but only surfacing now
<jberman> seems to be the case
<jberman> SSNeedlewoods (@sneedlewoods): you don't have to lower your paid hours for those reasons. you can include the time you expect to spend
<jberman> working in your proposal fine, no one should have an issue with that
<rbrunner7> jeffro256: What kept you busy during last week?
<j​effro256> Working on tx knowledge proofs integration (decode, spend, reserve, etc)
<r​brunner7> Anything that is significantly more complex now among those because of Carrot?
<j​effro256> Hoping to get that done this week
<j​effro256> Uh not significantly in term of concepts, but now there's a bit more business logic because of different transactions types, and the difference b/t internal and external enotes. It's also probably going to require some RPC changes to the daemon
<r​brunner7> Ok, if that's the worst that happens, quite alright :)
<r​brunner7> Alright, anything to discuss beyond reports today?
<o​frnxmr> stressnet didnt die with sustained 20+mb blocks
<s​needlewoods> thanks for your feedback, but I don't think I would feel well asking for more, I would like to give more than I take if possible
<o​frnxmr> Main issue is probably that when templates are >2800txs, xmrig has problems connecting, and mining a block with it will crash the node
<j​berman> your call!
<j​effro256> My old desktop server sounding like a jet engine tho
<r​brunner7> Lol
<o​frnxmr> Mining large blocks were often reorged by empty blocks, so thats potentially an issue - that people can produce artificially small blocks to win the block race
<r​brunner7> Finally working like it should have all the time already
<s​needlewoods> laptop fans been spinning non-stop for days
<r​brunner7> Is mining large blocks indeed somehow significantly slower? Where does that slowing happen, is that known?
<o​frnxmr> Cpu usage spikes hard when getting alt chains
<j​berman> very rough idea that probably has problems: maybe difficulty should also factor in n txs
<o​frnxmr> Probably can improve that logic to now download alt blocks unless the alt chain is longer than yours.. currently it seems to always download them (and probabky re-verifying the txs in them)
<o​frnxmr> to not* download
<o​frnxmr> Essentially, your node gets hammered with alt blocks (which could be bullshit attempts at selfish mining) even if your chain is longer
<r​brunner7> But those alt blocks need to be correct regarding RandomX?
<j​berman> alt block handling does need a pass
<r​brunner7> Another entry on a long list of such things maybe ...
<o​frnxmr> yea, theyre valid blocks, just not an equal or longer chain
<r​brunner7> That severly limits the potential to use them as some sort of DoS attack I guess, as long as our code does not handle them with good performance
<o​frnxmr> Yeah, not fcmp problem, but ive seen my nodes becomes slightly unresponsive when adding alt blocks that have no chance of overtaking. And if my chain is longer, then my chain should be pushed to the peer. Currently (master) it works fine because the small blocks are sent to them fast enough to force them to reorg, but on stressnet the peer keep mining blocks on their shorter chain before syncing the blocks from the longer chain
<o​frnxmr> Reorg doesnt happen until theyve actually synced the final block that surpasses their chain height
<o​frnxmr> So you can essentially game this by setting your download speed to something low, so you dont receive blocks fast
<o​frnxmr> anyway, not an fcmp issue. Just a big block issue
<r​brunner7> Aka "the bug" ... as it was brutally simplified in some Reddit discussions ...
<r​brunner7> Correct the "bug", and no more block size limit needed, presto :)
<r​brunner7> Well, not everybody can be a dev and know how awfully interconnected things can be
<r​brunner7> Alright, looks like we may be through with immediately important things for now. Thanks everybody for attending, read you again next week!
<s​needlewoods_xmr:matrix.org> thanks, see ya
<o​frnxmr> I H8 the txpool
<o​frnxmr> So many issues stemmed from the pool :)
<j​berman> it's significantly improving with the latest ya?? seems like just the not relayed issue is the last remaining main thing
<j​berman> and I guess that segfault but I don't think that's a txpool issue
````


# Action History
- Created by: rbrunner7 | 2025-12-12T15:58:55+00:00
- Closed at: 2025-12-15T18:50:58+00:00
