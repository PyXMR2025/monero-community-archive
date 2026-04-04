---
title: 'Monero Tech Meeting #129 - Monday, 2025-07-21, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1241
author: rbrunner7
assignees: []
labels: []
created_at: '2025-07-18T08:01:01+00:00'
updated_at: '2025-07-21T19:53:29+00:00'
type: issue
status: closed
closed_at: '2025-07-21T19:53:29+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1236).


# Discussion History
## rbrunner7 | 2025-07-21T19:53:29+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1241
<s​needlewoods> hi
<j​berman> *waves*
<s​yntheticbird> hi
<r​brunner7> On to the reports from last week already!
<s​needlewoods> mainly testing and bug fixes related to `[en/de]crypt_keys()`
<s​needlewoods> In the Wallet API we default wallet2s `m_unattended = true` (src: [last argument here]](https://github.com/monero-project/monero/blob/fbc242d52d89d9c8021194cd4faae657c94d5a31/src/wallet/api/wallet.cpp#L438), [wallet2 constructor](https://github.com/monero-project/monero/blob/fbc242d52d89d9c8021194cd4faae657c94d5a31/src/wallet/wallet2.cpp#L1188)), so for the CLI I added `bool unattended = true` as optional argument to `WalletImpl()`.
<r​brunner7> From reading the backlog I see that kaya had fun with optimizations
<s​needlewoods> and "m_wallet" 288 times left
<r​brunner7> You have to ask Ruck for a nice plot, and an estimate when you will hit zero :)
<rucknium> +1
<s​needlewoods> lol, probably will have some tail emission because of bugs
<j​berman> me: opened PR's from the contest to the fcmp-plus-plus repo, leder's helioselene is merged in and kayaba has been improving on top of it. fabrizio's divisors currently has an internal test failure fabrizio is continuing to help out with (it won't impact their contest payout). Handled compiler warnings for fcmp++/carrot with some help from jeffro too, set up core tests testing constructing a FCMP++/Carrot tx spending from a pre-rct tx., tests went smooth. I also continued on PoWER (proof-of-work enabled relay) setting up a design doc
<sneedlewoods> +1
<rucknium> +1
<j​berman> Still working on the latter design doc, but mostly just drafting what we discussed in a past MRL meeting
<r​brunner7> Did you come up with *PoWER* as an acronym?
<j​berman> that was actually @SyntheticBird
<r​brunner7> Ah, ok
<j​berman> good name
<r​brunner7> Yeah, has the potential to go even beyond Monero, I would say
<j​berman> Yep agreed
<r​brunner7> If we are through with the reports, I have a question that I think you will be able to answer
<r​brunner7> On Reddit there was a mention about "offline transactions" for Monero, as a hypothetical possibility
<r​brunner7> Taken literally, I would that means that a wallet builds a Monero transaction all on its own, without connection to any daemon
<r​brunner7> I am pretty sure that's not viable to do properly with our current protocols
<r​brunner7> Sure, you could grab some transactions as decoys and store them somewhere for later tx building, but the distribution would of course be off
<r​brunner7> So now my question: How will that look with FCMP++?
<j​berman> Before: the ring signature *signs* the decoys selected in the transaction, i.e. you need a spend key, your prior outputs you want to spend in the next tx, and decoys to construct a signed tx ready for submission to the network. Decoys require a connection to a daemon to select. You *could* select decoys at an early point in time and then sit on them, although yes this causes your tx to stick out because your decoys would be "old"
<j​berman> After FCMP++/Carrot: we "sign" the components necessary to authorize a set of outputs you want to spend (spend key and prior outputs are necessary for this), and separately, construct  the membership proof (which only needs the output path in the tree). You can "sign" with spend key at a point in time A, and then at a later point in time B, construct the membership proof and tack it onto the tx without the spend key. The "output path in the tree" requires a connection to the daemon to determine its latest state
<r​ucknium> Some txs have actually done this "cached ring members" behavior. Nonstandard and very bad for privacy, of course.
<j​berman> I have  a TODO on our TODO list to more clearly document the design decisions necessary to achieve this
<s​pirobel> maybe there should be a way to expire transactions
<r​brunner7> > The "output path in the tree" requires a connection to the daemon to determine its latest state
<r​brunner7> I can't do that with an old state of the trees that I downloaded from a daemon while still connected earlier?
<j​berman> Spending is one way to expire txs, although ya, a way to prevent a future tx from being able to be spent after a certain point without requiring an on-hcain tx is interesting (and I believe is part of the idea behind LN's HTLC's IIRC)
<j​berman> You can, but if you use an old path, your tx would stick out as referencing an older state of the tree (tx's include a "referenceBlock" which is the block idx used to construct the path and refers to the state of the tree when that block is tip)
<j​berman> Most txs would include the current chain tip when they enter the pool
<r​brunner7> And well, won't there be "gaps in the proof", so to say, for the time between the cached tree state and the tree state at time of tx submission? What if somebody manages to spend one of the enotes just in this time intervall?
<j​berman> Ya it's possible that some txs will honestly reference an older block than chain tip by the time they hit the chain tip
<s​pirobel> on solana you have to fetch a recent blockhash and sign the transaction against it. so by default it will expire in a minute or so. to sign transactions offline there is a method they call durable nounces. (it comes with caveats and UX pitfalls, that can lead to transactions looking like they were invalid, but still going through later on)
<j​berman> by the time they hit the chain*
<r​brunner7> Maybe I mix now membership proofs and double-spend protection
<j​berman> Interesting
<r​brunner7> The legit case of pointing to an older tree tip, or however you call this, is probably multisig transactions?
<spirobel> +1
<s​pirobel> yes and dealing with hardware wallets
<j​berman> Neither  multisig nor hw wallets are expected  to be different from normal txs. For multisig, you have multisig participants do the signing, and then once the tx is signed and ready, just have one participant (the submitter) construct and tack on the membership proof right before submitting
<spirobel> +1
<s​pirobel> would it be an option to make it the default to reject transaction that reference an older one at the pool / node level?
<j​berman> For hw wallets, hw wallet signs, then online wallet with view/ful lbalance  key constructs the membership proof right before submitting the tx
<s​pirobel> would it be an option to make it the default to reject transactions that reference an older one at the pool / node level?
<j​berman> Yes, theoretically could do that sort of thing for ring sigs too. Might have downstream unintended negative consequences / UX pains that some might not expect (even though they're doing an anti-pattern)
<r​brunner7> Say again, what exactly do you need for building the membership proof? Any secrets?
<r​brunner7> Ah, you mention the view/full balance key there
<j​effro256> Howdy sorry I'm late
<s​pirobel> howdy
<j​berman> You need the output path in the tree (and technically you need matching blinds to SAL signature too). Sorry, we'll have clearer docs on it
<r​brunner7> Alright :)
<j​effro256> You don't need the full balance key , but you do reveal which inputs you're spending to the prover
<j​berman> Main point is you don't need the spend key
<j​berman> For the memberhsp proof
<r​brunner7> Ah, that would be the compromise if anybody had the idea to "outsource" proof construction to some third-party, to be able to work offline for tx construction itself
<j​effro256> BTW, the hot/cold wallet code I'm working on at the moment will support exactly this scheme of "sign now, compete later"
<s​pirobel> btw is there work on accumulating this similar to the scaling work by ebfull ? ... maybe you saw the effort posts in the community workgroup recently .,..
<j​berman> personally not familiar with ebfull's effort there, got a link?
<s​pirobel> https://seanbowe.com/blog/tachyaction-at-a-distance/
<s​yntheticbird> that was actually not me
<s​yntheticbird> at least i don't remember
<j​berman> whoops, I thought  "POWER" was you in the MRL meeting that day
<j​berman> Ah, I'm familiar with tachyon but I guess I'm not sure what you mean regarding its relationship to the above
<r​brunner7> Oh, that "Tachyon" thing that may develop into the new "Zcash is better than Monero because X" argument
<spirobel> +1
<j​berman> I see what you're getting at a bit, reading this now
<r​brunner7> At first glance, it looks interesting, even for a crypto noob like me. Maybe it really is interesting and novel.
<j​berman> (@spirobel)
<j​effro256> Zcash actually will still have one theoretical privacy benefit over Monero after FCMP++: the transaction input/output counts are hidden
<r​brunner7> Well, there is always something, right
<r​ucknium> They are hidden?
<j​effro256> Yes they are now AFAIK , regardless of Tachyon
<r​ucknium> https://forum.zcashcommunity.com/t/are-numbers-of-shielded-inputs-and-outputs-hidden-in-pre-sapling-versions-of-zcash/43758
<r​ucknium> > Orchard merged spend and output proofs back together for performance reasons, which means each Action corresponds to 1-in 1-out. It is therefore more similar to Sprout again, in that if you create a 1-in 5-out Orchard transaction, the network can’t distinguish it from a 5-in 1-out Orchard transaction.
<r​ucknium> Maybe semi-hidden
<j​berman> Regarding accumulating proofs into one single proof for many proofs, @kayabanerve wrote this up a while back and can probably speak to further effort/focus on this front as it relates to FCMP++: https://github.com/monero-project/research-lab/issues/110
<j​effro256> If we had dummy inputs w/ FCMP++, then we more or less can achieve parity , especially if >= 2 input count is enforced by consensus
<r​brunner7> That issue is mentioning Seraphis quite a lot ...
<r​brunner7> But maybe it transfers to current FCMP++
<k​ayabanerve> One of my immediate comments on Tachyon is the comparison to tevador's proposal for off-chain communication of output recipience.
<k​ayabanerve> jeffro256: No, they aren't. They reveal how many 'actions' are in an Orchard bundle, each action representing one input and one output, both either potentially unused.
<k​ayabanerve> So you learn the max(inputs.len(), outputs.len()) due to the lack of explicit padding.
<r​brunner7> Still a bit less than with the explicite numbers of FCMP++?
<k​ayabanerve> Correct, their methodology isn't amenable to our current modular design and we should distinctly employ dummy inputs and then add a consensus rule for the amount of ins/outs.
<j​effro256> Yes, thank you for clarifying . You learn a possible number combinations , but its not guaranteed in all cases (except perhaps in 1-in, 1-out? Unless they ban that case)
<j​effro256> But with FCMP++ as-is, if you only own one enote, you can only ever create a 1-in tx
<j​effro256> I support this as long as dummies can be done semi-performantly
<r​brunner7> We will see how people will think about dummies and the still-larger tx sizes they would bring after the network digested the considerable jump in tx size for FCMP++ as planned now
<k​ayabanerve> tevador proposed a trivial solution: each input tuple is extended with a key. We ad-hoc extend the tree with that key and do the FCMP proof off the extended tree.
<jeffro256> +1
<k​ayabanerve> We don't have to communicate an amount commitment (we can just use `1G + 0H`) and the key image generator would still be `H(O)`. This also prevents burning another user's outputs (as the key image generator binds to the private spend key as well).
<k​ayabanerve> So it's trivially cheap. The issue is ad-hoc extending trees _including arbitrary historical trees_.
<k​ayabanerve> We'd have to be able to efficiently pull up the entire edge for any historical height, and perform a tree grow with every TX verification. While it's only adding a single leaf, it's still ~8 scalar multiplications _outside of the multiexp_.
<k​ayabanerve> Ugh. Depends on if we save the intermediates and can solely delta hash or not.
<k​ayabanerve> I do support that upgrade. i'm just noting jberman will be annoyed.
<k​ayabanerve> As jberman is not me, and as we love privacy, I fully support it.
<k​ayabanerve> :p
<j​effro256> Ah I see. This also has the "downside" that you can't create more dummies than enotes you own, yeah? Which doing so is of questionable utility , but...
<k​ayabanerve> No?
<k​ayabanerve> Even someone with no inputs on-chain would be able to produce fully valid FCMPs for no amount. If we accepted 0-fee TXs, people without any Monero could get full TXs on-chain.
<r​brunner7> That sounds funny
<j​berman> @SyntheticBird good news!!! https://libera.monerologs.net/monero-research-lab/20250430#c522744
<sneedlewoods> +1
<syntheticbird> +1
<j​effro256> Oh you're saying add a key at time of input alongside the rerandomized input ? Not provide it when adding outputs to the tree ?
<k​ayabanerve> rbrunner7: Inability to distinguish a real input from a dummy input implies inability to distinguish if a TX has any real inputs or is entirely dummies
<s​yntheticbird> Let's go. Thanks for reminding
<k​ayabanerve> jeffro256: Correct. "each input tuple is extended"
<r​brunner7> Yeah, makes sense, only dummies would be trivially possible.
<k​ayabanerve> Well, they wouldn't be able to pay a fee :) So it would require no-fee TXs be allowed. I assume they technically are right now? But I would have to check.
<r​brunner7> Maybe no relay, but tx would be valid, so you have to find somebody who mines it?
<plowsof> correct, sech1 could confirm 
<k​ayabanerve> Presumably but boog900 would know better than me, and I don't care to find the relevant rules myself right now
<j​effro256> Yeah if Helios-Selene is fast, then doing an extra right-hand-side hash grow might not be so bad. Do you know off the top of your head about how many scalar-point multiplications are done for FCMP verification for a 1-in, 7-layer right now?
<k​ayabanerve> 510 in a multiexp for the FCMP alone?
<j​effro256> Okay so ~2% slower ?
<j​berman> an extra 8 sounds fine to me
<k​ayabanerve> "in a multiexp" is the key-word. They're probably only as expensive as 300 individual point multiplications. Tree growing would be 8 scalar muls + 8 point compressions (in effect), where one point compression is several times more expensive than a traditional multiplication. It'd also probably re-instate performant random reads as a requirement to run a Monero node.
<j​berman> Thanks I hate it
<k​ayabanerve> How much worse are point compressions again?
<j​effro256> You could remove the random read requirement by caching the right edge , which I think we already do in the current DB impl
<k​ayabanerve> We just ran extensive benchmarks on this
<k​ayabanerve> jeffro256: We support arbitrary historical trees, so no, we can't.
<j​effro256> Lol
<k​ayabanerve> We can just optimize for the popular case.
<k​ayabanerve> So probably 3% slower before we discuss the impact caused by point compressions.
<j​effro256> No I mean we cache the right edge for all historical FCMP trees to handle rollbacks
<j​berman> We do do this^
<k​ayabanerve> ... but we'd still randomly read them.
<j​berman> Random reads per tx sounds a lot better than random reads per ring member to be fair
<k​ayabanerve> There's no practical distinction between randomly reading the RingCT out DB and the historical tree edge DB other than quantity.
<k​ayabanerve> That argument can even be made for historical tree root hashes, those are just soooo smalllllll
<k​ayabanerve> Anyways, I support it as a post-FCMP++ hardfork, y'all can figure out the implementation details.
<j​effro256> Oh yeah well I mean its just as many random reads as pulling just the FCMP root, but yeah its more data, which may have a concrete effect
<k​ayabanerve> The bigger topic is if we plan to do that, we should keep in mind now how we _plan_ to enforce an IO count under consensus, which means we should start a migration path now.
<jeffro256> +1
<j​effro256> There is a difference for rings in that the number of jumps around in memory space is higher for rings
<r​brunner7> Sorry, have to leave now, but I will come back later and pack the whole rest of the discussion into the log. Thanks for attending everybody, read you again next week!
<k​ayabanerve> One way we can start migrating now: Limit all TXs to 8 inputs and force people who weren't ready for that (people who were unprepared for life and how it occurs) to handle it.
<k​ayabanerve> I'll take my leave now before I start getting hate mail again :p
<j​effro256> Lol
<s​needlewoods> thanks everyone, very interesting meeting
<s​pirobel> if state is accumulated later similar to tachy action it shouldnt be a big deal in any case
<j​effro256> Thanks everybody !
<r​brunner7> Learned a lot today, really interesting meeting
````


# Action History
- Created by: rbrunner7 | 2025-07-18T08:01:01+00:00
- Closed at: 2025-07-21T19:53:29+00:00
