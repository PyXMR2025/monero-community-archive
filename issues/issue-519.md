---
title: MRLmeeting logs, 2020/10/21
source_url: https://github.com/monero-project/meta/issues/519
author: moneromooo-monero
assignees: []
labels: []
created_at: '2020-10-21T19:46:36+00:00'
updated_at: '2022-06-23T07:31:34+00:00'
type: issue
status: closed
closed_at: '2022-06-23T07:31:34+00:00'
---

# Original Description
< TheCharlatan> Seems like we have some more people here for today's meeting :)
< TheCharlatan> Hi all
< UkoeHB_> hi
< Isthmus> heyo
< moneromooo> Oh. Forgot again -_- Hi.
-!- infinicrypt [~infinicry@217.138.199.76] has quit [Ping timeout: 256 seconds]
< TheCharlatan> We don't have any items posted, right?
< UkoeHB_> has anyone been working on any research-like projects they would like to mention
< UkoeHB_> ?
< TheCharlatan> I'll go first then. With the last fork we also changed the way Unix time based unlock_times are treated.
< Isthmus> :- )
-!- maybefbi [~maybefbi@112.199.218.101] has quit [Remote host closed the connection]
< TheCharlatan> The formula for that was created by UkoeHB_
< UkoeHB_> yep
< TheCharlatan> I published a full writeup on why it was changed on my blog: https://thecharlatan.ch/Monero-Unlock-Time-Vulns/
< UkoeHB_> oh nice
< TheCharlatan> There should be a disclosure on hackerone as well, but someone from the core team has to hit a button for it to be visible or something.
< ArticMine> Hi
< TheCharlatan> Anyway, that article treated a specific weakness in the protcol that is now patched.
< moneromooo> I can do that. I think we just do it for actual exploits, not all the stuff we get.
< TheCharlatan> I also wrote another article on timelocks that gives a summary of why I think the field is problematic.
-!- TheoStorm [~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl] has quit [Quit: Leaving]
< TheCharlatan> It builds on work that Isthmus has discussed here in January and that we discussed here in May with sarang https://thecharlatan.ch/Monero-Unlock-Time-Privacy/
< TheCharlatan> To re-iterate: about 98% of current unlock_time usage does not really make semantic sense.
< TheCharlatan> These are unlock_time values that are far below a current block height.
< TheCharlatan> The 2% of legitiamte values seem reasonably distributed, safe for some small weird clusters.
 * Isthmus gets an idea for a plot
< Isthmus> (brb)
< TheCharlatan> However, current ring selection does not take the unlock_time into account.
< ArticMine> One question that I have with time locks is allowing for basic payment channels in Monero
< moneromooo> Hmm. We could consensus forbid unlock time below currnet height. It'd double as "this tx is only valid for N blocks". That sounds like it could be useful.
-!- rj_ [~x@modemcable106.252-37-24.static.videotron.ca] has joined #monero-research-lab
< TheCharlatan> So two transactions mined in the same block, but with different values and mature since different times are treated the same.
< TheCharlatan> Yes, so in the article I argue that we should get rid of it altogether.
< TheCharlatan> But I think that might be a hard selll.
< TheCharlatan> So instead, I propose to 1) limit the field to a more compact size, 2) only use block-based unlock_time, 3) move it to per-output and 4) take the maturity of a transaction, not its mined height into account.
< TheCharlatan> And then 5) what you said moneromooo
< Isthmus> `(unlock time) - (height of youngest ring member) >= 10`
< moneromooo> 3 sounds you could usually deduce which is the change (the one without an unlock time).
< moneromooo> What is 4 ?
< TheCharlatan> moneromooo Copied from the post:
< Isthmus> Hmm yea, per-output is good for functionality, will make info leaks leakier if kept plaintext. However, per-output encrypted lock time would give best of both worlds (full functionality & information-theoretic privacy)
< TheCharlatan> Assume the current block height is 400'000. By the current rules, an output with unlock_time 350'000 mined at block height 200'000 is treated the same as an output at 200'000, even though the unlock_time encumbered output has only been available for spending for 50'000 blocks, while the other output has been for 200'000.
< moneromooo> You mean the code selects ring members which are still locked ? Are you sure about this ? IIRC it at least tries not to, but it might be buggy if that's what you saw...
< TheCharlatan> No
< TheCharlatan> That's not what I mean :)
< TheCharlatan> That code works correctly in that respect.
< moneromooo> Define "treated the same" then please.
< TheCharlatan> The ring member selection should not select by current_height - tx_mined_height, but rather by current_height - unlock_time (if the timelock is not 0)
< Isthmus> BTW here's the visual representation of comment by TheCharlatan "To re-iterate: about 98% of current unlock_time usage does not really make semantic sense."
< Isthmus> https://usercontent.irccloud-cdn.com/file/h4V6caVQ/image.png
< Isthmus> The data set started at height 10^6 (red line)
< Isthmus> So every single unlock time below that value is meaningless (would never be locked)
< moneromooo> I see. 
< moneromooo> That makes sense.
< moneromooo> So you're saying an output with a very lock time would never the a period of high likelihood of selection as fake out, so will likely onle be used  as the real spend. Right ?
< moneromooo> very *long* lock time
< TheCharlatan> To repair this unlock_time ring member selection, we should collect some data from bitcoin's use of CHECKLOCKIMEVERIFY and CHECKSEQUENCEVERIFY first though. Just to make sure we mimic actual unlock_time usage.
< TheCharlatan> yes moneromooo
< UkoeHB_> I think that treating a locked tx age as 'time spendable' instead of 'time on-chain' for purposes of ring-member selection is a good idea
< Isthmus> Haha wait it's even better as a PDF than CDF... The few txns in the blue circle are the only ones that used block unlock times in a meaningful way
< Isthmus> https://usercontent.irccloud-cdn.com/file/qa6YyXhu/image.png
< TheCharlatan> But, as stated in the article, it's not really a problem right now, because it amounts to about 200 such transactions. Of course usage may change in the future though.
< TheCharlatan> On the topic of transparent per-output timelocks, I might be weighing the risks wrong here. After all, we could not find a single transaction that locked XMR for a fatal amount of time.
< Isthmus> besides mine :- P
< UkoeHB_> ArticMine: I wondered that too, but have a hard time imaging who would use them or for what purpose
< TheCharlatan> Besides yours :P
< ArticMine> Multiple tx to one vendor
< ArticMine> For example a coffer shop or transit authority
< ArticMine> One opens a payment channel with the vendor. Then spends n the channel for each cup of coffee or bus / tram ride etc
< ArticMine> There are very significant privacy advantages for this
< TheCharlatan> Anyway, next step for me will be to probe bitcoin's usage of timelocks.
< TheCharlatan> Then I think I should open a MRL issue with points 1), 2), 3) and 5). The discussion can be continued after that with something more fleshed out.
< moneromooo> With encrypted lock times, does the lock time prevent verification if any input in the ring is locked, or if only the real input is locked ?
< Isthmus> Has to be real input, because we wouldn't be able to know/decrypt lock time of decoys
< moneromooo> Then this would fix the problem TheCharlatan pointed out.
< TheCharlatan> yes, it's just the real input. It's analogous to the amounts.
< Isthmus> BTW b10c has written some really great articles about bitcoin lock time.
< Isthmus> https://b10c.me/mempool-observations/1-locktime-stairs/
< Isthmus> https://b10c.me/mempool-observations/2-bitmex-broadcast-13-utc/
< moneromooo> (since locked outs would be selected in rings without failing verification, and yes, thinking some more I could have worked it out)
< TheCharlatan> ^ I might have inspired some of those articles :P
< TheCharlatan> So I guess I'll still ask, how the room feels about removing them entirely?
< UkoeHB_> I don't have strong feelings either way
< Isthmus> I think the only viable options are removing or encrypting
< moneromooo> I would not be against it, unless they're needed for payment channel style stuff.
< moneromooo> (replacement would still be OK if so)
< UkoeHB_> the lack of current use implies it wouldn't be missed
< ArticMine> I am not in favor of removing
< ArticMine> because of the future payment channel application
< ArticMine> LN is a horrible mess, but vendor payment channels is that baby that should not be thrown out with the bathwater
-!- rj_ [~x@modemcable106.252-37-24.static.videotron.ca] has quit [Ping timeout: 240 seconds]
< ArticMine> So I would go for encrypting
< UkoeHB_> would you mind sketching out how such a payment channel would be constructed?
< moneromooo> The lock time scheme we end up needing for that future payment channel system might not be the one we have now, so that doesn't prevent removing.
< UkoeHB_> or could be*
< TheCharlatan> ^ I agree with moneromooo
< moneromooo> And either reading later, or, more likely, adding a differentl one later better adapted to payment channels.
< moneromooo> Umless you think we won't be able to change anything at some point I guess.
< ArticMine> Then we can remove the current one
-!- rj_ [~x@modemcable106.252-37-24.static.videotron.ca] has joined #monero-research-lab
< ArticMine> Unless there is another clear use case
< Isthmus> I think that the IRC crowd does not know of other known current uses. (based on this and recent conversations)
< Isthmus> If we open a github issue about removal and crosspost to Reddit, that should give ample opportunity for anybody in the community with a compelling use case time to speak up
< ArticMine> That sounds like a good idea
< TheCharlatan> Isthmus I'm all for that :)
< moneromooo> Uses I heard about are: "prevent my future self from selling in fear", "gift some money to my kids for when they're 18" and "prevent stealing", though that last one's miguided.
 * Isthmus clarifies: payment channels are a very compelling use case, and I'm fine with discussing re-implementation if/when payment channels are on the table
 * Isthmus ponders cases mentioned by mooo
< moneromooo> I could also imagine keeping money as security (ie, a flat deposit).
< moneromooo> Though that's probably better done with multisig.
< ArticMine> US DOJ "burn Monero" application with lock time >> age of the universe
< Isthmus> Ah yea
< Isthmus> That's not the only way to provably burn, right?
< Isthmus> e.g. send to generator, send to pubkey 00000000000000000, etc
< moneromooo> No :)
< moneromooo> I mean, maybe not :)
 * Isthmus wants to compile a list of all the ways to provably destroy monero, but doesn't want to derail unlock time convo
< moneromooo> Just setting the pubkey in extra to 0000 doesn't mena it's burnt. 
< Isthmus> Oh true, there *could* exist a private key...
< sech1> boating accidents have always been the only way to burn monero
 * sech1 runs
< TheCharlatan> Meeting is nearly over, does someone else have something to discuss?
< Isthmus> Oh btw all data credit for unlock time stuff goes to @n3ptune and their magical DB
< TheCharlatan> yupyup, thanks n3ptune!
< n3ptune> thanks!
< n3ptune> #noncesense-research-lab is always open for your data needs
< Isthmus> :- D
< Isthmus> I got a giant (many GB) data set from n3ptune this weekend to do the per-field stats tests for info leaks, but I'm still working on data ingestion, no results yet https://github.com/Mitchellpkt/crypto_field_stats_tests
< TheCharlatan> nice :)
-!- thrmo is now known as SaifedeanAmmousC
-!- SaifedeanAmmousC is now known as SaifedeanAmmous
< TheCharlatan> see y'all next week then
< UkoeHB_> Thanks for the meeting


# Discussion History
# Action History
- Created by: moneromooo-monero | 2020-10-21T19:46:36+00:00
- Closed at: 2022-06-23T07:31:34+00:00
