---
title: 'Monero Tech Meeting #119 - Monday, 2025-05-05, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1198
author: rbrunner7
assignees: []
labels: []
created_at: '2025-05-02T16:53:02+00:00'
updated_at: '2025-05-05T19:11:45+00:00'
type: issue
status: closed
closed_at: '2025-05-05T19:11:44+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1194).

# Discussion History
## rbrunner7 | 2025-05-05T19:11:44+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1198
<s​yntheticbird> hello
<s​needlewoods> hey
<r​ucknium> Hi
<plowsof> *waves*
<r​brunner7> Ok, let's start already with the first reports
<r​brunner7> After studying code for quite a while and an extensive discussion with Rucknium  I am ready to start coding modifications of the peer selection mechanism
<sneedlewoods> +1
<jeffro256> +1
<jberman> +1
<j​effro256> Howdu
<s​needlewoods> I tried to catch up a little with the fcmp++ development and looked into the fcmp++stage branch and cli/rpc wallet integration
<j​berman> *waves*
<j​berman> me: shared tx weight analysis, fixed a bug in the wallet tree cache, worked on moving forward outstanding PR's, pushed a draft PR demonstrating memory safe FFI usage (https://github.com/seraphis-migration/monero/pull/39), this week working on removing the FCMP++ input limit for the alpha stressnet May 21st (we seemed to have solid support in favor of PoW-enabled relay for larger input txs >8 so that nodes don't expose a vector to hog CPU verifying invalid FCMP++'s)
<jeffro256> +1
<sneedlewoods> +1
<r​ucknium> Same update as rbrunner7 , but from the other side of the table. There are a few open questions, but they will probably be resolved without much trouble.
<r​brunner7> "we seemed to have solid support in favor of PoW-enabled relay for larger input txs >8 " interesting development
<j​effro256> me: fixed a few bugs with Carrot/FCMP CLI/RPC integration and am working on GUI integration
<j​berman> (solid support *in last MRL meeting* in favor of PoW-enabled relay)
<r​brunner7> Was that in the MRL meeting itself? Maybe I checked out too early ...
<j​berman> Ah it might have been in the convo right after, spillover from the meeting
<r​brunner7> Do we have a candidate for the PoW algorithm already? That stuff that tevador did for Tor?
<j​berman> perhaps the low memory RandomX variant makes sense for this use case: https://libera.monerologs.net/monero-research-lab/20250430#c522764-c522767
<r​brunner7> Ah, yeah, one new dependency less if that fits the bill
<r​brunner7> That may mean that some smartphone wallets won't bother and not offer txs with more than 8 inputs ...
<r​brunner7> But I guess can't have it all
<j​berman> Likely the only reason they might not bother is if they don't want the RandomX dependency. Preliminary discussions on expected CPU-time for the PoW will be fairly light relative to tx construction in the first place
<r​brunner7> Maybe that's a bit of a heresy, but maybe a quick look over to what Nano did? Feeless, network stability and spam protection entirely based on PoW, as far as I remember.
<j​effro256> Or they may not want it if they are very RAM size constrained i.e. less than 256MB
<r​ucknium> IIRC, their PoW-only solution was successfully attacked. Then they added tx prioritization by amount and age, which Monero hides.
<j​effro256> Tobtoht didn't want RandomX simply b/c Windows Defender is stupid and flags everything with RandomX in it as malware
<j​berman> would be pretty surprised if there's a wallet out there that implements scanning the chain with less than 256mb
<r​brunner7> They have a point ...
<s​yntheticbird> I think it is safe to assume people willing to execute transactions with phones or low-memory devices are unlikely to use more than 8 inputs
<j​effro256> Really? Doesn't wallet only queue 10 blocks at a time?
<j​effro256> *wallet2
<j​effro256> Oh wait I'm thinking of the async scanner, and it's requests, not blovks
<r​brunner7> SyntheticBird: I guess it may happen "just like that", depending on the enotes that are present, and their values
<syntheticbird> +1
<r​ucknium> IIRC, people have done pool mining to hardware wallets and then wondered why their triple-digit-input txs couldn't be signed
<r​brunner7> Cool
<j​effro256> Lol
<s​yntheticbird> lmao fair
<j​berman> the daemon currently has a max cap of 100mb OR 20k txs OR 1000 blocks, whichever comes first. Then wallet2 is doing some copying, sooo.. it's feasible to sync with less than 256mb of ram, but would be pretty surprised if anyone's actually doing it
<j​effro256> good point
<r​brunner7> jeffro256: Did you already schedule what comes after GUI wallet? I guess not much big stuff is left now.
<r​ucknium> https://support.ledger.com/article/360018969814-zd
<r​ucknium> > Sending a large number of transactions to a Ledger hardware wallet is troublesome. If you receive a lot of small transactions from mining please read this article carefully.
<r​brunner7> "since the chip may overheat" Mmmm, ok
<j​berman> did tobtoht actually say this somewhere? he gave that whole engineering explanation of why equix over randomx that made sense
<j​effro256> I thought Equix was someone else , but I could be wrong
<r​brunner7> I think I heard this argument many years ago already
<j​berman> https://github.com/tevador/equix/blob/master/devlog.md
<j​effro256> After GUI, I'm going to work on the Rust carrot library, and then probably HW devices and multisig
<syntheticbird> +1
<jberman> +1
<s​yntheticbird> In tevador we trust
<j​berman> oh lol I actually just mixed up tobtoht and tevador (sorry tobtoht and tevador), my bad
<j​berman> I blame monday
<r​brunner7> Who seems to be missing, unfortunately. I saw somewhere with a German translation for Polyseed which is now probably in limbo
<r​brunner7> *somebody
<s​yntheticbird> I think tevador is koe's alt
<s​yntheticbird> this was supposed to be a joke but I don't manage to find good way to put it
<s​yntheticbird> forget it
<j​effro256> That'd be crazy lore
<syntheticbird> +1
<r​brunner7> That Rust Carrot library, that's something that will be first used for Serai, I guess?
<r​ucknium> https://matrix.to/#/!mehPttlWNbDtNeDbvu/$skmafkmWjQq9ow9HVN9HrTdH6hLROs99uK9OKbJzpE8?via=matrix.org&via=monero.social&via=hackliberty.org
<r​ucknium> I hope that link works. Not a completely clear statement
<j​berman> it works
<s​yntheticbird> and Cuprate I think
<r​brunner7> Ah, yes of course
<r​ucknium> tobtoht said:
<r​ucknium> > All it took to bypass Monero detections for most AV vendors was to change a few strings. We're down to 2 detections now on Windows binaries, from completely irrelevant AV vendors.
<r​ucknium> > Well, that, and strip out RandomX.
<j​effro256> If Cuprate is node-only code, then it doesn't need almost any carrot code whatsoever
<syntheticbird> +1
<r​ucknium> "We" I think means Feather wallet.
<s​yntheticbird> alright thx for clarifying
<r​brunner7> I dimly remember similar statements, like already mentioned years ago already
<j​effro256> For consensus, Cuprate needs to define the new output type variant, and that's about it. It doesn't need to know anything about it besides how to serialize/deserialize
<r​brunner7> Those false positive flaggings of our software on Windows are a big PITA
<r​brunner7> But probably not important enough to go down some sub-optimal route for that new PoW use
<r​brunner7> Sadly
<r​brunner7> Alright, beside these reports, do we have anything more to discuss today?
<s​yntheticbird> I remember when Avast integrated a crypto miner into its free software. This is probably the incarnation of hypocrisy within antivirus
<r​brunner7> Right, *that* crazy story
<r​ucknium> Isn't EquiX supposed to be must faster to verify than RandomX?
<r​ucknium> much*
<s​yntheticbird> Yes
<jeffro256> +1
<s​yntheticbird> It's like 50µs on a Ryzen 1700
<j​berman> if we're allowing 8 input txs without PoW, that gives an allowed window of (rough estimate) 200ms for PoW verification, whereas RandomX with light memory verification "takes around 15 ms" (from that linked rationale above)
<r​brunner7> I don't understand. How do we "allow" something? Don't we want everything as fast as possible?
<j​effro256> FCMP++ verification of a 8-input tx will inherently take about 200ms is what jberman is saying
<j​berman> ^
<r​brunner7> Yes, and thus you want to add to add as few cycles as possible if you go to more inputs yet, no?
<j​effro256> So RandomX time-to-hash is almost always going to be faster than FCMP++ verification
<b​oog900> we need to create miner templates
<j​berman> ideally optimizations will bring that FCMP++ verification time down a significant amount, but regardless, I don't expect we'll get 8-input FCMP++ txs verifying in less than 15 ms
<j​effro256> True... I forgot about that
<b​oog900> don't know how much carrot that will be, probably a nibble
<r​brunner7> Maybe I confuse which party is doing which work right now
<s​yntheticbird> whispers variable time performance gains are worth the maintenance burden
<j​effro256> The way that I envision it is that PoW is required on the p2p layer for someone to *send* a mempool transaction. So whoever originates the transaction must create PoW. If you are relaying the transaction, you can also relay the PoW proof without doing more PoW. Now, either A) the daemon which receives the transaction over RPC can do the PoW for that transaction or B) the wallet which signs the transaction can do the PoW
<j​berman> ok for rbrunner7 : backing up, the core issue for large input FCMP++ txs is that it takes a long time for a node to verify a single tx (e.g. a 100+ input tx could take seconds to verify). and so we brought up PoW-enabled relay as a "solution" to this in that if you want to send a tx to a node and get that node to verify it so it can add it to its pool, then you have to attach a PoW to that tx demonstrating ~seconds of CPU-time, to make it more costly for a malicious actor to get a node to do verification of bad txs
<j​berman> in the meeting we discussed only requiring PoW verification on FCMP++ txs with more than 8 inputs, since it may be relatively acceptable for nodes to take up to 200ms to verify 8-input FCMP++ txs
<j​effro256> This will be most of the stuff in the `enote_utils.h` file in the `carrot_core` module in the C++ repo. This doesn't cover scanning, address generation, or advanced transaction creation
<boog900> +1
<j​berman> now since we're saying it's acceptable for nodes to take up to 200ms to verify an 8-input FCMP++ tx, then we have a 200ms acceptable verification window for the PoW on relayed FCMP++ txs, and so we don't necessarily have to use equix for the reasons tevador chose it for tor
<jeffro256> +1
<j​berman> and can reasonably stick with randomx
<r​brunner7> So the argument goes that if you already spend more than 200 ms to just verify the transaction, with no way around that of course, 15 ms or so to verify whether the PoW is correct does not matter too much, in comparison? Not much won to bring that down to, say, 1 ms, with EquiX?
<jeffro256> +1
<j​berman> right
<r​brunner7> I see
<r​brunner7> That makes sense
<s​yntheticbird> Main appeal of EquiX over RandomX was originally its memory constraints. 1.8MB vs 256MB.
<r​brunner7> Ok, funny how such a quite new element pop ups so late on the way to FCMP++ :)
<r​brunner7> Quite a surprise, at least how I see it
<j​effro256> Our PoW discussed here wouldn't be applicable to txs already in mined blocks, just relaying mempool txs, since txs in blocks obviously already PoW done for them
<j​effro256> IMO this has no effect for our use case since nodes already have their RandomX cache loaded up and ready to go
<s​yntheticbird> oh maybe i missed something I assumed wallets were doing the PoW. It's confirmed that broadcasting nodes are doing it?
<j​effro256> It's definitely not totally decided, but the 8/8 limit came up as a big point of contention, so if it's feasible to use PoW to get rid of the 8/8 limit, I think it's worth looking into
<r​brunner7> Looks like a "political" decision, not only a technical one? (Who does the PoW)
<r​brunner7> Absolutely, I don't think anybody is really happy with that 8/8 limit
<j​effro256> Okay yes if the wallets do it, then *maybe* it's a constraining factor. That is, if scanning memory usage already is lower memory than RandomX lite mode, which jberman argues it's not
<j​berman> personally I think it would be simplest to have wallets do it
<j​berman> btw I also brought up a potential fingerprinting issue and then didn't expand on the point, but here it is: if some wallets don't implement >8 input txs because of the new PoW rule, then wallets that send >8 input txs stick out
<r​brunner7> Oh yes, maybe having the daemon doing it may reduce the number of people offering public nodes considerably
<j​berman> as in, you receive a >8 input FCMP++ tx, you know that it must have come from a wallet implementing the feature, and not another wallet
<r​brunner7> I don't think doing PoW for dozens of connected wallets sounds attractive :)
<r​brunner7> That would be the exact other way round than that micropayment scheme, how was it called already?
<r​brunner7> Pay for RPC or something
<r​brunner7> Alright, we are nearing the full hour. Let me close the meeting proper, while discussions can go on of course. Thanks for attending everybody, read you again next week!
<j​effro256:monero.social> Probably, although I would like to see the option for daemons to do it after receiving a raw tx, so that wallet vendors at least have the option of not including the RandomX dependency
<s​needlewoods> thanks, very interesting
<j​effro256> Thanks rbrunner7 and everyone else!
<j​berman> ya I guess the latter would need to be a requirement for windows wallets
````


# Action History
- Created by: rbrunner7 | 2025-05-02T16:53:02+00:00
- Closed at: 2025-05-05T19:11:44+00:00
