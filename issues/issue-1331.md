---
title: 'Monero Tech Meeting #155 - Monday, 2026-01-26, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1331
author: rbrunner7
assignees: []
labels: []
created_at: '2026-01-23T16:22:59+00:00'
updated_at: '2026-01-26T19:07:51+00:00'
type: issue
status: closed
closed_at: '2026-01-26T19:07:50+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1325).


# Discussion History
## rbrunner7 | 2026-01-26T19:07:50+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1331
<s​needlewoods> Hey
<j​berman> *waves*
<r​brunner7> We won't have jeffro with us in the meeting today, but available for comments and questions during the rest of the day.
<r​brunner7> (for people reading along and being interested in the "OVK controversy" that bloomed on Reddit for the last 3 days.)
<r​brunner7> Alright, what is there to report from last week?
<j​berman> me: followed up on jeffro's unbiased hash to point review (about to push implementing his latest round of comments), and continuing now with boog's comment on my tx relay v2 changes PR
<r​brunner7> I started to look into Polyseed, but did not yet get very far
<s​needlewoods> worked on review comments from rbunner here: https://github.com/monero-project/monero/pull/10233
<s​needlewoods> continued with the wallet-rpc, you can open a wallet now
<s​needlewoods> and apart from my CCS, just out of curiosity, I based #10233 onto `fcmp++-alpha-stressnet`, there weren't too many conflicts and even though I just band-aided them without investigating, the whole thing built successfully, but I haven't tested that `monero-wallet-cli` yet, because my stagenet node is still ~25500 blocks behind.
<r​brunner7> How is progress with the wallet-rpc? I suppose quite good, if you can already open wallets?
<s​needlewoods> It's still quite early, but I expect it go faster than the wallet-cli once I get momentum
<j​berman> I spent a solid amount of time on this presentation to try and help with that fwiw: https://www.youtube.com/watch?v=dw6GKFhKKBE
<sneedlewoods> +1
<spirobel> +1
<r​brunner7> I see. Almost a classic now, no? :)
<r​brunner7> Anyway, Matrix does not show me more new people joining this Matrix room than usual, which I almost expected
<s​pirobel> there is outgoing viewkeys already in monero-oxide
<s​pirobel> just wild what people post on twitter
<r​brunner7> Ah, it spilled over there?
<r​brunner7> Have a link?
<s​pirobel> i thought it came from there
<s​pirobel> no i just saw it glancing at the time line
<s​pirobel> dont go there often because its all nonsense lol
<r​brunner7> Avoid the brain rot and contamination
<spirobel> +1
<r​brunner7> Ok, will do.
<r​brunner7> I confess I don't know much yet about that "tx relay v2". When and how is that scheduled to get the necessary rigorous testing? And can tx relay v2 and  tx relay v1 coexist, will daemons "speak" both?
<j​berman> ofrn has been running it on some nodes for quite a bit of time. I'd like to see it on stressnet (definitely on beta at least)
<s​needlewoods> iirc datahoarder shared this response from fluffypony https://xcancel.com/fluffypony/status/2015684629479510514
<d​atahoarder> it's a lost channel tbh :)
<DataHoarder> I shared it privately via DM, but yes. fluffypony also has received DMs and also helped combat this
<j​berman> it's still in code finalization stages I'd say though, very close to the finish line on that front
<r​brunner7> You mean "lost" as in "truly and utterly irrelevant" :)
<j​berman> "And can tx relay v2 and  tx relay v1 coexist, will daemons "speak" both?" -> yes, though I'd argue it could make sense to deprecate v1 after the hard fork
<DataHoarder> there's also another one - where FCMP++ context (no output tracking, no rings) also helps get the point across
<r​brunner7> Somehow nice to see that Fluffypony still watches things Monero
<DataHoarder> also has received DMs -> also has received similar questions (in public)
<r​brunner7> Mostly for nostalgia however, on my side
<DataHoarder> well they get directly messaged about it
<r​brunner7> Like that meme where you get prodded with a stick "Do something"
<j​berman> (granted, this presentation was given with the context of Seraphis 128-input rings front of mind, although it does address the hypothetical of fcmp's as well)
<r​brunner7> I see
<r​brunner7> So the fact that daemons will support both relay protocols will of course make testing much easier.
<r​brunner7> Alright, more reports, or more comments about OVKs?
<s​pirobel> sounds a bit similar to fluffly blocks vs initial block sync path ... good to only have one code path
<r​brunner7> In the mid-term, certainly. A hardfork is a good chance there.
<j​berman> yep, it's being implemented in a very similar way too for initial rollout: compiled in support flags so updated daemons speak v2  with each other, but can speak v1 with daemons not yet running v2
<r​brunner7> One more thing that the Cuprate people need to implement ...
<j​berman> I should say, has been implemented* that way by 0xfffc
<0xfffc> +1
<sneedlewoods> +1
<j​berman> boog900 has been very active in helping shape design from the start, so they're well aware
<spirobel> +1
<sneedlewoods> +1
<0xfffc> +1
<s​pirobel> what is the thought on potential for netsplits, blocks getting accepted on one, but not on the other
<j​berman> I agree that it's better to deprecate sooner rather than later to avoid that potential
<j​berman> but obviously, you can't deprecate on initial rollout because that would cause a netsplit
<j​berman> hence, deprecating after the fork I think is a solid goal
<r​brunner7> "blocks getting accepted on one, but not on the other" That could only happen if some daemons come to miss some transactions altogether?
<r​brunner7> Ah, no, not even then, because the blocks **are** the way transactions get known of course
<r​brunner7> The pool can be seen as a nice add-on, but not strictly necessary I guess
<s​pirobel> if there are multiple code paths that do serialization / processing logic slightly different you can craft a block / transaction in a block that make one set of nodes accept the block, while the others dont.
<r​brunner7> jberman: Just to be sure, with "deprecate" you mean "stop to support", not "marked for stopping support soon, be warned"?
<s​pirobel> can someone link to the tx relay pr?
<s​needlewoods> https://github.com/seraphis-migration/monero/pull/184
<spirobel> +1
<j​berman> I think there is a case for stopping supporting tx relay v1 after the fork
<j​berman> and there is a followup PR to that one here: https://github.com/0xFFFC0000/monero/pull/63
<spirobel> +1
<r​brunner7> Hmm. Couldn't people running on pre-fork daemons build their own network without knowing it, so to say?
<j​berman> and then eventually that will all get rolled up into the tx relay v2 PR to the main monero repo here: https://github.com/monero-project/monero/pull/9933
<j​berman> can you expand the scenario you're stating here?
<r​brunner7> Maybe it does not make sense. Old daemons will still be able to exchange blocks with each other, and sync blocks from each other, right? They just won't see any transactions anymore. So they won't be cut off and will only find old daemons to peer with.
<r​brunner7> *pool transactions
<r​brunner7> I mean, I can sync with an old daemon up to the hardfork block.
<r​brunner7> New tx relay protocol or not.
<j​berman> Before the fork: old daemons will still receive new pool txs using the v1 protocol from both old and new daemons
<r​brunner7> Yes, and after the fork, with v1 protocol off for almost all active daemons, the old ones are still not cut from the network, but just cut from the tx pool
<r​brunner7> Alright. Anything else to discuss today?
<j​berman> The goal is to release tx relay v2 either with the hard fork v19 daemon, or in an earlier release version than that so that it's definitely included no matter what in first v19 daemon release. The v19 daemon therefore would by default communcate tx relay v2 with other v19 daemons. After the fork, once v1 tx relay is deprecated, all the older nodes should already be cut off from th<clipped messag
<j​berman> e network anyway beacuse they don't know the new v19 consensus protocol
<p​lowsof> just for visibility: koe says he aims to be back mid Jan early Feb https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/384#note_33802
<jberman> +1
<sneedlewoods> +1
<xmrack> +1
<jberman> +1
<r​brunner7> I think I can describe a more concrete scenario: After the hardfork, you find some old pre-hardfor daemon version for download and start to use that. Nothing really bad will happen, except that syncing stops at the hardfork block. What won't happen is that such daemons accidentally form their own, private Monero network without noticing it.
<s​pirobel> slightly related: https://github.com/seraphis-migration/monero/pull/159/changes  how would this change improve block propagation speed? saw it mentioned here: https://github.com/seraphis-migration/monero/issues/139
<r​brunner7> Thanks for the reminder, plowsof. Might get interesting!
<plowsof> +1
<j​berman> the latter will happen regardless of the tx relay protocol
<j​berman> missed that, I'll respond there
<spirobel> +1
<s​pirobel> this intersects in the sense that adding of the blocks / deciding to reorg happens based on fluffy blocks vs the initial block sync path. maybe the old nodes would just fall back to the initial block sync
<r​brunner7> "the latter will happen regardless of the tx relay protocol" Not sure I understand, but it's probably not important, and my brain will click in due course anyway :)
<r​brunner7> Ok, let me close the meeting proper. Room is open of course. Thanks everybody for attending, read you again next week!
<s​pirobel> the hardfork introduces other changes too so if they dont update the tx relay is the least of their problems
<s​needlewoods> Thanks everyone, cu
<s​pirobel> thanks
<j​berman> after the v19 fork block has passed, v18 nodes that haven't updated will likely form their own network communicating with other v18 nodes, regardless of tx relay protocol
````


# Action History
- Created by: rbrunner7 | 2026-01-23T16:22:59+00:00
- Closed at: 2026-01-26T19:07:50+00:00
