---
title: 'Monero Tech Meeting #111 - Monday, 2025-03-10, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1168
author: rbrunner7
assignees: []
labels: []
created_at: '2025-03-07T13:21:29+00:00'
updated_at: '2025-03-10T19:30:05+00:00'
type: issue
status: closed
closed_at: '2025-03-10T19:30:04+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1165).

# Discussion History
## rbrunner7 | 2025-03-10T19:30:04+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1168
<s​needlewoods> hi
<o​frnxmr> Hi
<r​brunner7> Let me ping jberman and jeffro256
<j​berman> *waves*
<j​effro256> Howdy
<s​pirobel:kernal.eu> 你好
<r​brunner7> Alright, what is there to report from last week? kayabanerve is already busy writing :)
<v​tnerd> Hi
<j​berman> me: completed successful FCMP++ transfers in the CLI, merged with jeffro256 's latest in fcmp++-stage (https://github.com/seraphis-migration/monero/pull/18), implemented kayabanerve  's suggestions for the FCMP++ optimization competition
<jeffro256> +1
<rbrunner7> +1
<sneedlewoods> +1
<rucknium> +1
<rottenwheel> +1
<r​brunner7> Successful week, as it seems!
<o​frnxmr> Is there a _goal_ date for 1. fcmp testnet hf 2. Fcmp mainnet hf / offset. Example. 1. July testnet 2. January 26 binaries, july 26 hf
<s​needlewoods> did some clean up, rebased fixed issues and I'm about to push, but having technical dificulties
<j​effro256> Still working on `wallet2` tx construction in regards to cold signing and delegated FCMPs. I think I will be done by the end of the week though
<r​brunner7> ofrnxmr: At least in this forum nothing in this direction was discussed yet.
<r​brunner7> People just seem to work forward as fast as they can ...
<s​pirobel:kernal.eu> is there a carrot implementation planned in monero-oxide?
<j​berman> Planning to work on the following this week: FCMP++ batch verification integration, scan_tx for FCMP++ txs (will include an RPC route to fetch paths via the daemon)
<r​brunner7> SNeedlewoods: Anything anybody can help regarding these difficulties?
<s​needlewoods> no should be fixed in a minute, trying to reboot now lol
<k​ayabanerve> May I send a long post?
<ofrnxmr> +1
<sneedlewoods> +1
<jeffro256> +1
<jberman> +1
<rotthenwheel> +1
<spirobel> +1
<o​frnxmr> Yeah. Not rushing. And not asking the "wen" question, just wondering if we had targets set. (previously feb testnet was a short term target). Of  course we still have issue with current releases where our rings are quite poor
<k​ayabanerve> Do we have another topic in the way first?
<r​brunner7> Not that I know, kayabanerve
<k​ayabanerve> The current output tuple, denoted `OIC`, is accumulated into the tree by its `x`-coordinates. This allows proving that either `O` or `-O` is in-tree. We accepted this as the key image of +-`O`, +-`I`, for any combination, shares an `x`-coordinate with all other possibilities. By migrating key images from points to `x`-coordinates, which can be done even for legacy key images, this scheme is without issue in practice, barring the loss of a single bit.
<k​ayabanerve> The issue is the academia. The composition, and signature, was prior reviewed considering all of these elements as points. To modify now to `x`-coordinates alone would be non-trivial as its a very awkward scheme to discuss.
<k​ayabanerve> We can move the membership proof to be over points. The naive way to do this is to bind `x`- and `y`-coordinates into the tree.  This doubles the size of the multiscalar-multiplication done for the leaf layer, effectively doubling the time the tree's hashes take (as the leaves dominate due to the fan-in degree). It doesn't increase the time of the torsion checking/clearing however, and minimally increases the time of the Weierstrass conversion.
<k​ayabanerve> Alternatively, we can re-introduce permissibility. This can't be applied to `I`, so we'd now hash in `O.x, I.x, I.y, C.x`, representing just a 25% increase in the leaf layer's MSM. The issue is this is a DoS, so avoiding the DoS means having wallet2 (CARROT, really) only generate permissible output keys/commitments. This is annoying but possible.
<k​ayabanerve> My advocacy is to hash the `y`-coordinates. It solves the FCMP++ composition's bounds. The performance penalty is ideally offset by the optimization competition.
<j​effro256> Yeah, I'm probably going to be the one implementing it ;)
<spirobel> +1
<rottenwheel> +1
<ofrnxmr> +1
<k​ayabanerve> I did start speculating on ways we can further improve performance. My best idea is to replace `I = hash_to_point(O)` with `I = hash_to_point("key_image_generator")`. This would allow us to calculate the hash of `I` and cache it, so calculating the hash of this 6-element tuple is only performing the work of a 4-element tuple. That requires we be able to fix the key image generator however, which historically opened related key attacks.
<k​ayabanerve> Take a public spend key S, and public view key V. To send to such an address, assuming it's not a subaddress, we have `O = S + Hs(8rV || i)G`. We summarize this as `O = S + dG`. For someone who sends to an address twice, they have `d` and `d'`. They can look for key images on-chain such that `I + (d' - d)H == I'` to identify the outputs' spends. Accordingly, this derivation scheme does not allow a static key image generator.
<k​ayabanerve> If the derivation was rewritten as `O = S + dV`, we avoid this issue. The discrete logarithm is `s + dv`. While the sender may have `d, d'`, and can calculate `(d' - d)H`, they can't calculate `(d' - d)vH`. `vH` would become the outgoing view key. The issue is the outgoing view key is derivable from the incoming view key. Setting `O = dS + V` solves this issue, with `sH` being the outgoing view key (`s` the private spend key).
<k​ayabanerve> The question is if we can perform a similar transform with CARROT. If so, we can maintain the FCMP++ composition (without having incomplete academia/pain there), and instead of doubling the leaf tuples' length (the current proposal), only increase them by 33%. This exact proposal also allows existing wallets to create outgoing view keys and prevents fragmentation of wallets who have `x` as their private spend key and wallets who have `y` as their private spend key (the current proposal for legacy/new wallets, with a multisignature protocol for each). It does shift the burden to CARROT however, which I kick to jeffro256.
<k​ayabanerve> I am available for questions.
<r​brunner7> kayabanerve: What happened here, on a high conceptual level, with the first issue you described? Something got overlooked in some audit? Misunderstandings between us and the auditors because of unclear documentation?
<k​ayabanerve> We have the `OIC` points. We noted ~a year ago ago just the `x`-coordinates was fine. That wasn't reflected in my definition of the composition. Aaron did their review/work on the SAL proof (the new signature) presuming points. To now move to `x`-coordinates is just non-trivial work, of what is fundamentally a messy thing to model.
<r​brunner7> Sounds a bit unfortunate to this layman's ears ...
<k​ayabanerve> Not 'presuming'. They did their work off the definition I provided. The fact they didn't comment it should be `x`-coordinates, per discussions we had on a gist, isn't something reasonably expected of them. That wasn't their job.
<k​ayabanerve> Moving to the expanded leaf tuples makes our academia simpler and prevents some malleability issues. It's also dead-simple. The issue is the performance cost. It'd wipe out our gains from the contest.
<j​berman> I would advocate for the most conservative academic approach i.e. chart a path on a foundation that is simpler to model.
<j​berman> I've become somewhat less concerned by tree build time over time because I think the option for wallets to download layer tree elements is ok, and as CPU's improve / client architecture improves, we can implement client-side tree building (such architectural improvements are also in the pipeline with the async scanner).
<k​ayabanerve> Hence why we can accept the expanded tuple, but the discussion for further optimizations exist. I came up with an optimization that restores most of the benefit while also reducing upcoming wallet fragmentation (and future academia on that point) IF CARROT can be adjusted and its academia is amenable.
<r​brunner7> Those possible changes you mention, as a reaction to these things being points instead of coordinates, do they invalidate some audits?
<k​ayabanerve> It also, again, enables existing wallets to produce OVKs.
<k​ayabanerve> It'd require I modify the definition of the composition and we have someone sign off on the wonkiness of it. I'm unsure exactly what it'd invalidate regarding existing work as it's extremely weird to model.
<r​brunner7> So I get it the ideas for further optimizations that you wrote are under the assumption that we go along with points, as per audit, right?
<k​ayabanerve> As per sanity and path of least resistance.
<k​ayabanerve> We can make this optimization at any hard fork in the future, solely making the tree-format decision now. It's re: the address derivation protocol.
<k​ayabanerve> Also, caveat, OVKs for existing wallets would only be for freshly received outputs.
<r​brunner7> "as it's extremely weird to model" Isn't that something that maybe you don't want to hear in a discussion about correctness and safety of a protocol ...
<k​ayabanerve> Exactly
<k​ayabanerve> So I can simplify this. The academia is a mess with the proposal to only work with `x`-coordinates. Also including the `y`-coordinates resolves this. It's simple to implement in the C++ code yet does increase how long tree-building takes, which has side-effects for nodes/wallets (see jberman's comment). This is unfortunate yet still seems optimal to me.
<k​ayabanerve> Because tree-building is slow, I'm happy to announce I have a proposed optimization to save 33% of our tree-building time*!
<k​ayabanerve> *after accepting this change
<k​ayabanerve> We can make the key image generator static if the address derivation protocol is amenable. This can be done at any HF willing to modify the address derivation scheme.
<r​brunner7> Make something slower to take credit afterwards of making it faster again, yeah right :)
<k​ayabanerve> The net cost across these two changes is it's 33% slower. 3 -> 6 -> 4
<r​brunner7> Just joking, barerly hanging along
<k​ayabanerve> The 3 -> 6 is more or less how it is. The 6 -> 4, when we have the bandwidth and CARROT-willing, is just a good idea.
<j​effro256> I will look into this and see if it is possible
<r​brunner7> Well, my gut feeling: It is like it is. If our assumptions about speed were too optimistic, well a bit unfortunate, but that's life.
<k​ayabanerve> There's also another architectural improvement I can propose, yet the complexity of it makes me want to refrain until after the optimization contest so we can see where we're at then.
<k​ayabanerve> I try to come with some solutions to the problems I introduce.
<rbrunner7> +1
<s​yntheticbird> don't be shy, spoil it already
<r​brunner7> This shapes up to be some quite exceptional meeting!
<k​ayabanerve> We just ship a small quantum computer as an ASIC with every Monero node /s
<ofrnxmr> +1
<jeffro256> +1
<syntheticbird> +1
<s​yntheticbird> Now that's what I call innovation!
<r​brunner7> "Complexity" is already sky-high in Monero tech. Just saying.
<r​brunner7> Complexity is right now what bugs me personally most about Monero.
<k​ayabanerve> And again. Right now, we have two multisignature protocols for FCMP++: one for `x` as the private spend key and one for `y` as the private spend key. Under `I + hash_to_point(O)`, `x` is the outgoing view key meaning existing wallets don't get an OVK, and we have these two types of wallets. With a constant key image generator, we can solely have `x` as the private spend key as `x` is no longer the OVK yet `xI` would be (now constant, not per-output).
<r​brunner7> OVK = outgoing view key
<k​ayabanerve> This not only increases functionality of existing wallets but also reduces future implementation work *and* current academia (two multisig protocols -> one).
<k​ayabanerve> rbrunner7, hanging along ;)
<r​brunner7> I trust jeffro256 understands what this is all about and can work out something for Carrot. Don't dare to tell me we have to switch to something else, I am writing a series of posts about that.
<k​ayabanerve> Ideally, it's as simple as replacing the letter `G` in one or two lines.
<j​effro256> NO
<s​pirobel:kernal.eu> how does the multisig situation change under FCMP? Does this affect the FROST based multisignature scheme as well or are we talking about the old one?
<k​ayabanerve> FCMP++ comes with two multisignature schemes, one for each case. A constant key image generator would allow collapsing to just one.
<k​ayabanerve> Both are FROSTy.
<r​brunner7> jeffro256: Can you elaborate on your "NO" a bit already?
<s​yntheticbird> yeah bro yelled that NO from the bottom of his soul
<j​effro256> Sorry I was just being facetious, it's never as as simple as that
<syntheticbird> +1
<r​brunner7> Ok. I guess our cryptographically savvy people leave this meeting with quite some pondering and homework to do. I am always surprised how it seems it's possibly to "play" with these schemes, treat them almost like clay. Take away something here, dent it some more there.
<r​brunner7> *possible
<r​brunner7> One can only marvel
<s​yntheticbird> yeah sounds cool, i didn't understand anything but I trust jeffro256 and jberman
<k​ayabanerve> I'm not trusted? :(
<s​yntheticbird> and kayabanerve
<s​yntheticbird> my bad
<s​yntheticbird> ofc I trust you
<k​ayabanerve> The whole point here is in how the FCMP++ composition doesn't have any commentary on how `I` is generated, and how we can define `I` in a way which gives us nice properties elsewhere. Hence why it's like clay ;)
<syntheticbird> +1
<r​brunner7> I guess the ball is in the implementers' court now, at least in part
<r​brunner7> Alright. Is there something left for this very meeting?
<s​needlewoods_xmr> managed to push https://github.com/monero-project/monero/compare/release-v0.18...SNeedlewoods:seraphis_wallet:x_remove_cached_password and https://github.com/monero-project/monero-gui/compare/master...SNeedlewoods:monero-gui:x_replace_cached_password_with_verifyPassword 
<s​needlewoods_xmr> first one is large because it is based on #9464
<s​pirobel:kernal.eu> do you have a rough timeline?
<s​yntheticbird> i was there. when people said "fcmp testnet in february"
<o​frnxmr> I'd like to bring up something only partially related to fcmp++
<o​frnxmr> My suggestion is an interim hard fork with goals of:
<o​frnxmr> 1. Randomx v2
<o​frnxmr> 2. jeffro256 coinbase dsa pr https://github.com/monero-project/monero/pull/8815
<o​frnxmr> 3. Cutting off technical debt by moving to v0.19 based on master
<o​frnxmr> the idea is that
<o​frnxmr> 1. the fcmp++ hard fork will have (much) less extra baggage
<o​frnxmr> 2. master will be thoroughly tested on its own
<o​frnxmr> 3. Rings will be improved in the meantime
<spirobel> +1
<s​pirobel:kernal.eu> is the max blocks param on getblocks.bin part of that? if not please add it.
<k​ayabanerve> NACK to any intermediary HFs. It'd take months to organize and two HFs in short succession sounds negative.
<r​brunner7> Yeah, I saw your proposal after the last MRL meeting. IMHO the sentiment in that meeting was against some intermediate hardfork. Maybe because of this the MRL meeting in 2 days would be a better forum to discuss.
<s​pirobel:kernal.eu> even more common releases of monerod would be good
<k​ayabanerve> extremely negative
<syntheticbird> +1
<o​frnxmr> The second hard fork isnt on testnet yet
<k​ayabanerve> Also, increasing ring sizes too much breaks HWW support. I know that wasn't a goal stated here but I want to note it can't carelessly be pitched as a reason to HF.
<o​frnxmr> We could do the first hard fork by july
<o​frnxmr> And the second is still like a year out
<o​frnxmr> I'm against increasing ring size
<j​berman> I would prefer not to focus on an intermediary HF personally. Just need to get all those async scanner PR's into the release branch spirobel, should be fairly straightforward
<spirobel> +1
<o​frnxmr> Whats there to focus on aside from releasing it?
<r​brunner7> ofrnxmr: Maybe people misunderstand your point 3), "Rings will be improved in the meantime"?
<o​frnxmr> Randomxv2 = sech1, jeffro coinbase pr = complete
<s​yntheticbird> Is there really nothing we can do to accelerate FCMP++ HF date?
<s​pirobel:kernal.eu> yes hf has potential to cause more trouble than it is worth. but at least release monerod more often
<s​pirobel:kernal.eu> could already include some fcmp testing code
<k​ayabanerve> We can immediately accept the 6-elem tuple over the 3-elem tuple and acknowledge further discussions on optimizations are completely distinct.
<o​frnxmr> The coinvase segregation pr ffor mrl 108/109 has been complete for like 1-2 yrs
<j​berman> reviewing code. I said for me personally (e.g. 8815)
<k​ayabanerve> (I think we already have, I just want to be utterly unambiguous)
<r​brunner7> As I am also against any additional hardfork before going to FCMP++ and Carrot, seems to me we still wait for somebody beside ofrnxmr advocating, to be blunt
<j​berman> (fwiw I just pushed code that has an FCMP++ testnet working with the CLI)
<spirobel> +1
<syntheticbird> +1
<r​brunner7> I can follow ofrnxmr 's reasoning, and it has something, but for me going straight to FCMP++ is the lesser evil
<spirobel> +1
<s​yntheticbird> how much months would that make us gain? afair you advocated that current implementation was fine for production use (DoS-wise)
<t​obtoht> I support branching from master well before the FCMP++ fork date to give us ample time to iron out unrelated bugs, but I don't think we can reasonably squeeze a hard-fork in between without delaying FCMP++.
<syntheticbird> +1
<jberman> +1
<o​frnxmr> our effective ring size is 4 atm, and fcmp doesnt have a timeline. Shouldnt uodate dsa without a hf. Releasinf fcmp++ at the same time as master is potentially dumping a lot of large melt untested code to be released at the same tome
<r​ucknium> It doesn't make sense to me to say that a hard fork should have the coinbase-exclusion DSA, but not the OSPEAD-derived DSA. The OSPEAD-derived DSA provides a larger privacy boost than the coinbase-exclusion one, plus it requires fewer code changes. I'm not saying that I think an intermediate hard fork is a good idea (or that it isn't a  good idea). Just saying that OSPEAD should be included if it happens.
<o​frnxmr> i think master has long since diverged from release and on its own could be an issue to release, and (like tob said) should be branched before fcmp
<s​yntheticbird> I think everyone can agree on the branching
<r​brunner7> "our effective ring size is 4 atm" Fair enough. I just fail to get to worried about that "ringsize 4" given how long we have that already. We should be able to endure that a bit longer.
<o​frnxmr> Coinbase exclusion is an immediate 2-5 decoy boost. Not saying we shouldnt include ospead, but coinbase exclusion should be a no-brainer
<r​brunner7> Sadly not this late in the game, IMHO ...
<o​frnxmr> A bit longer means rushing fcmp or potentially waiting for well over 1yr
<s​yntheticbird> How about launching an intermediate HF in 2 months only?
<ofrnxmr> +1
<s​yntheticbird> is that practically possible?
<o​frnxmr> With minimal changes? I dont see why not
<s​yntheticbird> I'm mostly worried about ecosystem
<k​ayabanerve> 2 months only???
<r​brunner7> Sigh. Now it gets weird, if you ask me.
<r​ucknium> According to my quick recent calculations, coinbase outputs are about 6% of outputs. On average, that's just 1 decoy per ring (0.06 * 15). Of course, there are rings that get more of them by unlucky draws.
<ofrnxmr> +1
<o​frnxmr> Yes. We the changes on master shouldnt be breaking changing.
<k​ayabanerve> Then don't ship them in a HF.
<s​yntheticbird> ok yeah the 3 "?" answer my question
<o​frnxmr> Dsa changes shouldnt be shipped w/o a hf
<r​brunner7> Usually we want HF ready software in the hands of people 3 months before hardfork, for heaven's sake
<syntheticbird> +1
<k​ayabanerve> Then don't ship the DSA changes.
<r​ucknium> AFAIK, sech1 wants a 6 month lead time on monerod binaries with RandomX version 2 because miners would need to update. So a RandomX version 2 would probably not go in this proposed intermediate HF.
<syntheticbird> +1
<jeffro256> +1
<k​ayabanerve> Ship all of the other code which is being clamored about.
<k​ayabanerve> ^ and don't ship RandomX v2
<k​ayabanerve> TBF we should have miners update before the HF is cut in that case Rucknium
<s​pirobel:kernal.eu> 6 months lead time sounds too long
<s​pirobel:kernal.eu> they should be more aware and accustomed to updates
<ofrnxmr> +1
<o​frnxmr> I'd personally run the new dsa's even with anonymity puddles
<o​frnxmr> I'm 100% sure that all recommended wallets and well known public nodes would update
<r​brunner7> Current RandomX is stable for years and years, why should they be "more accustomed to updates"?
<s​yntheticbird> I will just remember that if the main concern about DSA change requires everyone to change in a short-time, and we can't an hard fork, we can maybe profit from the next release 18.4.0 to ship it since it comes with a vulnerability fix. Not a wallet one but still should be loud enough for everyone to remember to update
<r​ucknium> I am looking into spackle_xmr 's suggestion of gradual rollout of a new DSA, to reduce anon puddles issues.
<syntheticbird> +1
<r​brunner7> Ok, we are well over the hour for the meeting. By all means continue to discuss, but allow me to close the meeting proper. Thanks everybody for attending this very interesting meeting. Read you again in 1 week!
<s​yntheticbird> Thx everyone
<s​needlewoods_xmr> Thanks everyone, very active today
<o​frnxmr> If were not hard forking (randomx) then id still want to see the rest of those changes
<s​pirobel:kernal.eu> thc
<s​pirobel:kernal.eu> thx
<o​frnxmr> Rucknium:  tobtoht:
<o​frnxmr> Thats master branching and dsa rollout
````

# Action History
- Created by: rbrunner7 | 2025-03-07T13:21:29+00:00
- Closed at: 2025-03-10T19:30:04+00:00
