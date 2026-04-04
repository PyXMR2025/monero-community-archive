---
title: Monero Research Lab Meeting - Wed 18 December 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1127
author: Rucknium
assignees: []
labels: []
created_at: '2024-12-17T21:21:30+00:00'
updated_at: '2025-01-07T20:40:19+00:00'
type: issue
status: closed
closed_at: '2025-01-07T20:40:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Discussion: preventing P2P proxy nodes](https://github.com/monero-project/research-lab/issues/126).

4. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131)

5. Any other business

6. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1123 

# Discussion History
## Rucknium | 2024-12-20T20:49:56+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting yime! https://github.com/monero-project/meta/issues/1127     

> __< r​ucknium:monero.social >__ time*     

> __< s​yntheticbird:monero.social >__ yreeting     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< a​rticmine:monero.social >__ Hello     

> __< rbrunner >__ Hello     

> __< c​haser:monero.social >__ hello     

> __< j​effro256:monero.social >__ Howdy     

> __< j​berman:monero.social >__ *waves*     

> __< r​ucknium:monero.social >__ Like I said last meeting, I won't make a meta GitHub issue nor chair a meeting on December 25. People are free to meet then, of course. Next meeting I will make an agenda for will be January 1, 2025     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Discovered and report a critical privacy vulnerability in Wownero's decoy selection algorithm: https://codeberg.org/wownero/wownero/issues/488 . One lesson: Don't disable the wallet2 decoy sanity checks. Also working on OSPEAD.     

> __< j​berman:monero.social >__ me: implementing this optimized torsion check for faster FCMP++ curve tree building: https://github.com/kayabaNerve/fcmp-plus-plus/blob/torsion-check/crypto/divisors/src/tests/torsion_check.rs     

> __< j​effro256:monero.social >__ Are you going to FFI it or remake it in the crypto ops code ?     

> __< j​berman:monero.social >__ the latter, I'm implementing in C++     

> __< j​berman:monero.social >__ / C     

> __< v​tnerd:monero.social >__ hi     

> __< v​tnerd:monero.social >__ been doing Boost 1.87 related things     

> __< j​effro256:monero.social >__ Me: brainstorming with kayaba on carrot switch commitments, I think we've settled on an optimal scheme considering we use a 256 bit curve     

> __< j​effro256:monero.social >__ Also drafting changes to the carrot doc     

> __< j​effro256:monero.social >__ Also found the issue in the code with Wownero's DSA     

> __< tobtoht_ >__ I'm mostly done with the build system work for rust FFI (#9440). What remains is some doc improvements and finding a potential fix for aarch64 non-determinism.     

> __< rbrunner >__ Is there a bounty on that Wownero stuff? :)     

> __< r​ucknium:monero.social >__ I was paid a WOW bounty     

> __< rbrunner >__ Nice     

> __< j​effro256:monero.social >__ A wownty, if you will     

> __< r​ucknium:monero.social >__ All operators of Wownero nodes, public and private, should update their nodes to the latest version: https://wownero-node-checker.redteam.cash/     

> __< r​ucknium:monero.social >__ 3) Discussion: preventing P2P proxy nodes. https://github.com/monero-project/research-lab/issues/126     

> __< r​ucknium:monero.social >__ The spy node ban list has been enabled on Cake Wallet's nodes. I think Stack Wallet's, too. PiNodeXMR implemented a feature to add ban lists. The MoneroNodo hardware node will enable it.     

> __< r​ucknium:monero.social >__ Here is the issue that announces the ban list recommendation, and the ecosystem projects that are enabling it: https://github.com/monero-project/meta/issues/1124     

> __< r​ucknium:monero.social >__ The `monero` Twitter/X account hasn't tweeted about it yet. That was a goal of the announcement campaign.     

> __< s​yntheticbird:monero.social >__ I don't know if anything really evolved since last time but Bucket ASMap seems like the next step     

> __< r​ucknium:monero.social >__ So anyone who has the capability to tweet from `monero` about it, please do so. Use the meta GitHub link: https://github.com/monero-project/meta/issues/1124     

> __< s​yntheticbird:monero.social >__ and in mid-term/long-term PPoS     

> __< r​ucknium:monero.social >__ Yes, I'll start researching ASmap soon.     

> __< j​effro256:monero.social >__ Thanks     

> __< r​ucknium:monero.social >__ Anything else on this?     

> __< r​ucknium:monero.social >__ 4) Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography. https://github.com/monero-project/research-lab/issues/131     

> __< s​yntheticbird:monero.social >__ Will be honest, I don't get conceptually whats a turnstile     

> __< r​ucknium:monero.social >__ For ZCash, it's that the total amount of coins in any of its shielded pools cannot go negative     

> __< j​effro256:monero.social >__ For Carrot, we are skipping the el gamal commitment and binding the blinding factor straight to the amount and the address spend pubkey. Simplifies the design over a traditional switch commitment but keeps the security     

> __< r​ucknium:monero.social >__ It the coin value in a shielded pool were to go negative, that would indicate that counterfeiting within the pool has occurred. For Monero, it's more complicated since everything is in the "shielded" pool. So you would have amounts cross a transparent barrier and count them up.     

> __< s​yntheticbird:monero.social >__ Ok I see, so the danger of a turnstile is that if there has been counterfeiting, the first one would pass but the last one would not be able to pass their coins.     

> __< j​effro256:monero.social >__ BTW, This would entail an LMDB migration where we keep track of total emission with a 128 bit integer instead of our truncated 64 bit integer     

> __< r​ucknium:monero.social >__ jeffro256: "This" meaning the turnstile?     

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ Don't know what to think about that graphic there: https://github.com/monero-project/research-lab/issues/131#issuecomment-2547789303     

> __< rbrunner >__ Will this need heaps of complex code to implement?     

> __< rbrunner >__ With a lot of effort?     

> __< r​ucknium:monero.social >__ There could also be a time-limited turnstile where users have to move to the post-quantum cryptography before a certain date. So users who don't move their coins for a long time would lose them permanently.     

> __< j​effro256:monero.social >__ rbrunner: Carrot is already almost that complicated right now. I just added a couple edges and shuffled things around to get that proposed graph     

> __< rbrunner >__ Ah, ok. Can't make my mind up right know whether I find that comforting or not :)     

> __< c​haser:monero.social >__ you could also have a turnstile that allows coins to pass beyond the legitimate supply, and is used only as an indicator/proof that counterfeiting occurred     

> __< s​yntheticbird:monero.social >__ with the amount being counterfeited or only a boolean at the end ?     

> __< j​effro256:monero.social >__ If we're detecting it already, why would we allow it to go over ? Ostensibly , once it hits the limit exactly, we already can guess that conterfeiting has alresdy occurred since no one ever spends 100% of coins in any system     

> __< c​haser:monero.social >__ IMHO that would be really bad. it's essentially burning people's XMR.     

> __< s​yntheticbird:monero.social >__ Wouldn't that pose a risk, if someone counterfeited lets say 50% over the actual total supply and passed it through the turnstile it would block 50% of the legitimate volume     

> __< r​ucknium:monero.social >__ If quantum computers become a reality, with a turnstile you are already burning their XMR, and giving it to the quantum adversary     

> __< rbrunner >__ As a strategic decision, we could say living with the counterfeited coins is less bad than burning the XMR of a lot of people?     

> __< a​rticmine:monero.social >__ It is more like: If you don't leave the sinking ship, you would sink     

> __< s​yntheticbird:monero.social >__ I don't understand     

> __< c​haser:monero.social >__ so that honest users have the opportunity to recoup some value (a value most probably diminished, but I'm not sure we can predict that)     

> __< r​ucknium:monero.social >__ jeffro256: Is it true that with the switch commitment design, if people use a Carrot address after the FCMP++ hard fork, they most likely would be able to get into post-turnstile heaven?     

> __< a​rticmine:monero.social >__ This presumes there is  no time limit on the turnstile, only an amount limit     

> __< a​rticmine:monero.social >__ ... but if we can detect counterfeiting during the transition this avoids the whole issue     

> __< r​ucknium:monero.social >__ SyntheticBird: A quantum counterfeiter would get through an amount-only turnstile before the laggard honest users get through. Then, they cannot spend their XMR after the turnstile hits its limit.     

> __< c​haser:monero.social >__ is it certain that a QA can steal existing enotes?     

> __< s​yntheticbird:monero.social >__ Oh so there is definitely a need for a time limit then     

> __< j​effro256:monero.social >__ Lmao yes. The output pubkeys for carrot address can be constructed in such a way that it allows for PoKs that are hard for QCs. This isn't the case for existing addresses     

> __< j​effro256:monero.social >__ Post-turnstile heaven , I like that term     

> __< r​ucknium:monero.social >__ Probably you need an amount limit _or_ an (amount and time) limit.     

> __< r​ucknium:monero.social >__ Saint Peter at the turnstile gate.     

> __< j​effro256:monero.social >__ In general, we can't detect counterfeiting for specific spends of single outputs, just if it has happened overall because the amount of XMR sent over the turnstile is too great     

> __< j​effro256:monero.social >__ Just like we can't determine on-chain if someone spent XMR honestly , or "stole" someone else's seed phrase     

> __< j​effro256:monero.social >__ If you can extract knowledge of the discrete log of output pubkeys, you "own" those coins     

> __< rbrunner >__ So after the FCMP++ hardfork everybody is free to send their coins to themselves to bring it into the "new world"     

> __< a​rticmine:monero.social >__ https://github.com/monero-project/research-lab/issues/131#issuecomment-2537588673     

> __< a​rticmine:monero.social >__ Is this a solution?     

> __< j​effro256:monero.social >__ If we have an amount limit, and we enforce post-QC secure composition , then the only purpose of a time limit would be if we value restricting counterfeiters over allowing potentially honest old wallets to come online     

> __< r​ucknium:monero.social >__ jeffro256: I agree.     

> __< j​effro256:monero.social >__ We definitely need to incorporate something like kayaba's sketch in that comment in order to keep the integrity of key images     

> __< r​ucknium:monero.social >__ Well, kayabanerve 's potential Proof-of-Stake discussion comes in here, too. If an adversary has a large or majority share of coins by QC cracking.     

> __< j​effro256:monero.social >__ But that doesn't inherently prevent QCs from stealing pre-Carrot coins     

> __< r​ucknium:monero.social >__ Or, I think in a PoS design, the adversary only needs a majority or 2/3rds of the _staked_ coins to re-org the blockchain, etc., so does not need so much of the total supply.     

> __< r​ucknium:monero.social >__ So that's a potential blockchain security reason to have an amount _and_ time limit on a PQ turnstile     

> __< j​effro256:monero.social >__ Actually we can't let any non-coinbase RingCT coins be spent without Carrot since they aren't statistically binding     

> __< j​effro256:monero.social >__ Okay so maybe I need to layout the spending requirements somewhere     

> __< a​rticmine:monero.social >__ So effectively only post Carrot or coinbase coins cannot be forged by a QC     

> __< j​effro256:monero.social >__ We can allow spending pre-RingCT coins as well as coinbase RingCT, because the amount is in cleartext. However, the owners of these would be in a race to spend their coins before a QC cracks their privkey. We can also spend coins made with the Carrot wallet protocol but with legacy addresses, but they're in the same boat where they're racing QCs. The only ones who get to relax are<clipped messag     

> __< j​effro256:monero.social >__  those with coins addressed to Carrot-migrated addresses, since their address composition gives them some degree of security against being opened by a QC     

> __< j​effro256:monero.social >__ Coins in confidential amount RingCT txs NOW, before being spent when the turnstile is activated are lost forever     

> __< j​effro256:monero.social >__ Coinbase coins now can be stolen since a QC can crack the privkey. However,  we can still allow spending of them at a protocol level since it wouldn't cause inflation     

> __< s​yntheticbird:monero.social >__ I'm not sure if this is ethical to let that happen...     

> __< j​effro256:monero.social >__ At a practical level, depending on the speed of initial QCs, The honest holder might be able to construct a proof of ownership before a QC can. That's why we would allow it     

> __< j​effro256:monero.social >__ But yea there's also the ethical consideration of monetizing theft of old coins     

> __< j​effro256:monero.social >__ I think allowing a pathway for old owners to migrate, even if means potentially rewarding key breakers, is the lesser of two evils     

> __< j​effro256:monero.social >__ Though that might wreak financial havoc on everyone else     

> __< j​effro256:monero.social >__ I'll leave that analysis to a macroeconomicist     

> __< r​ucknium:monero.social >__ Is it easier for a QC to counterfeit XMR amounts or break an output's privkey? What would be the first target?     

> __< j​effro256:monero.social >__ Outputs privkey     

> __< j​effro256:monero.social >__ If we are making a turnstile, I think we should ban all spending of RingCT outputs which don't have statistically binding amount commitments     

> __< r​ucknium:monero.social >__ By how much? IIRC, at least one paper about this has said that Monero's outputs are safer than transparent coins' outputs since an attacker doesn't know where the big XMR is. They could be breaking outputs with dust amounts     

> __< r​ucknium:monero.social >__ Unless they have some off-chain info     

> __< j​effro256:monero.social >__ Well that's assuming we aren't doing switch commitments. If I had a working quantum computer at this exact moment, I would first go for finding the discrete log between the G and H generators. That would let me mint infinite XMR in perpetuity without ever needing the QC again     

> __< j​effro256:monero.social >__ But if we ARE doing switch commitments and activate before a QC is working, then they can't attack amounts anymore     

> __< r​ucknium:monero.social >__ The adversary's intentions would determine the effect on XMR purchasing power. If they don't spend or exchange it, then there may be little effect. Except, there may be an expectation effect because the huge XMR amount could be visible in the turnstile counter.     

> __< j​effro256:monero.social >__ And have to go for privkeys     

> __< j​effro256:monero.social >__ Specifically of pre-Carrot addresses     

> __< s​yntheticbird:monero.social >__ I didn't made the link, but the turnstile will actually make individual outputs' amounts transparent?     

> __< j​effro256:monero.social >__ Yes     

> __< s​yntheticbird:monero.social >__ That's bad for privacy but somehow very exciting     

> __< a​rticmine:monero.social >__ Then there is the quotation of knowledge of the public key     

> __< a​rticmine:monero.social >__ Question     

> __< r​ucknium:monero.social >__ It will make the transparent for the turnstile crossover transaction unless some kind of zK proof of turnstile amounts is developed I guess. The blockchain protocol has to count up the amounts somehow     

> __< r​ucknium:monero.social >__ jeffro256: Does MRL have to come to a "decision" about the switch commitments today, or is it still in development?     

> __< j​effro256:monero.social >__ It's mostly sorted out how to move forward with Carrot, but there's decisions about how to structure the rules of the turnstile that can be decides later     

> __< j​effro256:monero.social >__ *decided     

> __< j​effro256:monero.social >__ So in short, we don't need to make any decisions today AFAICT     

> __< r​ucknium:monero.social >__ Here's that paper that compares QC risk for a few blockchains: Kearney, & Perez-Delgado (2021). "Vulnerability of blockchain technologies to quantum attacks." https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=80     

> __< s​yntheticbird:monero.social >__ I've a question     

> __< s​yntheticbird:monero.social >__ Kayabanerve linked NIST latest recommendations regarding hash security parameters, recommending 384 bit. Kayabanerve is actually against switching to a 384 bit elliptic curve despite a potential risk on 256 bit hash functions ?     

> __< s​yntheticbird:monero.social >__ May I missed something     

> __< s​yntheticbird:monero.social >__ Is it something to worry about or not is my question     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< s​yntheticbird:monero.social >__ thanks     

> __< j​effro256:monero.social >__ Thanks everyone !     

> __< a​rticmine:monero.social >__ Thanks     

> __< c​haser:monero.social >__ thank you all     

> __< k​ayabanerve:matrix.org >__ chaser chaser:monero.social: Yes, a QC can burn existing outputs. They can't burn FCMP++ outputs.     

> __< k​ayabanerve:matrix.org >__ Rucknium: jeffro256: rbrunner There's two migrations: When we have PQ and no one has a QC, when we have PQ and someone has a QC. The former lets anyone migrate. The latter requires a strongly bound wallet, not just the usage of Carrot.     

> __< k​ayabanerve:matrix.org >__ Outputs made today (including coinbase) cannot be migrated once a QC is live. Outputs made under CARROT cannot be migrated.     

> __< k​ayabanerve:matrix.org >__ jeffro256: Coinbase outputs can't be migrated as you can make 1G+1Y keys today. They'd spend with key image 1H(1G+1Y) after FCMP++ activates but if you assume they're xG, a QC can double spend.     

> __< k​ayabanerve:matrix.org >__ *1T, not 1Y     

> __< k​ayabanerve:matrix.org >__ You at least need a cut-off date where you assume T was unknown and couldn't already be used which isn't worth it IMO.     

> __< k​ayabanerve:matrix.org >__ The goal should be to give users five years to make and move to a new wallet, which is internally binding, and allows them to migrate indefinitely. Old outputs, RCT or not, I'd not bother with at all when we disable the legacy crypto except for the defined long-term migration process. I definitely wouldn't support enabling theft.     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: We could redo the Seraphis migration discussions so we can embed 384-bit hashes into our EC's scalar field. Considering 256-bit hashes shouldn't actually be broken, I don't see it worth the effort when it'll only be done for a few years.     

> __< k​ayabanerve:matrix.org >__ But if hashes do ever resolve with a cbrt attack, yeah, it'd require turning off on long-term migration scheme at some point as it'd only have 84 bits of security.     

> __< j​effro256:monero.social >__ Couldn't we do the following for migrating coinbase inputs before FCMP++: 1) do trivial membership where we index the coinbase output directly 2) Calculate Hp(O) 3) Make the signer do a Schnorr-esque signature with proof of equal discrete log between G->O and O->Hp(O) ?     

> __< j​effro256:monero.social >__ This would burn people's funds if they preemptively formed their coinbase outputs or pre-RingCT outputs by scaling by T before FCMP++, but idk of anyone doing that, it's probably a minority     

> __< j​effro256:monero.social >__ Sorry, it should be proof of equal discrete log between G->O and Hp(O)-> x*Hp(O), the linking tag     

> __< k​ayabanerve:matrix.org >__ jeffro256: What?     

> __< k​ayabanerve:matrix.org >__ Sorry, I don't follow     

> __< k​ayabanerve:matrix.org >__ Are you proposing a dedicated coinbase TX type for all future coinbases, without privacy today, so that all future coinbases can be migrated?     

> __< k​ayabanerve:matrix.org >__ *not alleging you endorse it, solely asking if that is the idea     

> __< j​effro256:monero.social >__ No this would be the input proof for already-existing coinbase and pre-RingCT outputs posted inside a migration tx. The amount obv isn't a problem since it's already in cleartext. Then to prove unspentness, all we need to do is make the signer make an equality-of-disrcrete-log proof between G->O and Hp(O)->L, where G is the generator, O is the output pubkey, and L is the key image<clipped messag     

> __< j​effro256:monero.social >__ . Let's say that we can write O = x G. The key image L for output O must be in the form L = x Hp(O). Anyone can calculate Hp(O) from public data. The signer needs to provide L, and then make an equality of discrete log proof that proves that for the same x', O = x' G and L = x' Hp(O). I don't know if there is already a proof for this, but theoretically, it should be possible becau<clipped messag     

> __< j​effro256:monero.social >__ se for a given O, there is *exactly* one `x` and one `L` such that O = x G and L = x Hp(O). A trivial proof would reveal x in plaintext, but that obviously leaks the private key     

> __< j​effro256:monero.social >__ That would let us spend all coinbase and pre-RingCT, but still prove unspentness in a post-quantum manner     

> __< j​effro256:monero.social >__ We can't take this approach for FCMP++ outputs because the honest holder won't know the discrete log x such that O = x G     

> __< j​effro256:monero.social >__ And the reason we have to do weird hash stacking inside the addresses is because there's `l` openings `(x', y')` for every single `O`, which makes unspentness a bit trickier     

> __< j​effro256:monero.social >__ Whereas with pre-FCMP++ outputs, there's exactly *one* opening of the output, which makes unspentness determinisitic     

> __< k​ayabanerve:matrix.org >__ You can't do this at time of the migration TX jeffro256:     

> __< k​ayabanerve:matrix.org >__ No, it wouldn't, unless we don't migrate those into FCMP++ and restore the hard migration     

> __< k​ayabanerve:matrix.org >__ No, there isn't, that only holds true for honestly formed outputs     

> __< k​ayabanerve:matrix.org >__ I can make an output, today, which is 1G+1T and unspendable.     

> __< k​ayabanerve:matrix.org >__ The moment FCMP++ goes live, it'll be spendable with a key image of 1 H(1G+1T)     

> __< k​ayabanerve:matrix.org >__ The moment we enable migrations, under your proposal, it'd be given a key image of dlog_G(1G + 1T) H(1G + 1T).     

> __< k​ayabanerve:matrix.org >__ We'd need to not migrate all current outputs with public amounts into the FCMP++ tree to enable their PQ migration.     

> __< k​ayabanerve:matrix.org >__ Or you add an assumption that no one made such malicious outputs before a certain date in time, or you add PoKs over G to coinbase outputs now, or you just have anyone with historical outputs move to a new, properly bound, wallet anytime over the next ~five years and don't bother with any of these bad ideas     

> __< s​yntheticbird:monero.social >__ PoKs?     

> __< k​ayabanerve:matrix.org >__ That would make coinbase outputs not to an address but to an already-derived non-reusable key and strip their forward secrecy.     

> __< k​ayabanerve:matrix.org >__ *the PoKs over G for coinbase outputs idea would...     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: Proofs of knowledge     

> __< k​ayabanerve:matrix.org >__ There was a similar bug noted during the work on the integration of FCMP++. The originally sketched flow calculated the HtP inserted into the tree after torsion clearing. That'd give a torsioned output a distinct key image generator now/after FCMP++, allowing double spending across protocol versions.     

> __< j​effro256:monero.social >__ I'm proposing that we do the equality-of-discrete-log input proof EXCLUSIVELY for pre-FCMP++ outputs, and do the properly-bound-wallet-address input proof EXCLUSIVELY for post-FCMP++ outputs. Under this proposal, the people who would get screwed are those who added a non-zero `T` component to their output pubkey *before* the FCMP++ fork AND didn't spent it between the time of FCMP<clipped messag     

> __< j​effro256:monero.social >__ ++ activation and the PQ migration. This way, the FCMP++ fork is still migrationless, since we can soak everything up into the same pool assuming the hardness of the discrete log. But when it comes time for the PQ migration, spending them requires separated input proofs     

> __< j​effro256:monero.social >__ All pre-FCMP++ coinbase outputs and all pre-RingCT outputs already have no forward secrecy     

> __< j​effro256:monero.social >__ Except for that subsection of pre-FCMP++ outputs which preemptively include a `T` component, being okay with not being able to spend, and praying that nothing changes about FCMP++ between then and the time of activation     

> __< j​effro256:monero.social >__ I don't think we should cater the PQ migration to that small niche IMHO     

> __< j​effro256:monero.social >__ Especially considering that we know ~9% of the supply is still tied up in unspent pre-RingCT outputs     

> __< k​ayabanerve:matrix.org >__ No? Because an adversary with a QC can spend during FCMP++ and migrate jeffro256:     

> __< k​ayabanerve:matrix.org >__ This lets a QC double-spend     

> __< k​ayabanerve:matrix.org >__ Unless you limit the migration to only when a QC can't break ECC but then they can do a standard EC inputs (full privacy), PQ outputs     

> __< k​ayabanerve:matrix.org >__ It's only once a QC exists we need to discuss all of this mess, and once a QC exists, a QC can migrate spent outputs under your proposal as you assume historical outputs are xG when that isn't guaranteed     

> __< j​effro256:monero.social >__ We must assume that we trigger the PQ migration and stop creating any FCMP++ outputs *before* the first feasible quantum computer can break a single discrete log, otherwise all this discussion is useless anyways     

> __< j​effro256:monero.social >__ Because if there is ever a single discrete log broken while we are still doing partial amount verification (BP+s), then that one output could contain any amount of XMR < 2^64, and a turnstile is largely pointless if it all gets gobbled up by one guy     

> __< j​effro256:monero.social >__ We can assume some breakage after the PQ migration is activated but we're more or less hosed if we assume any breakage while FCMP++ verification is still in place     

> __< k​ayabanerve:matrix.org >__ jeffro256: Sorry, we're still talking past each other.     

> __< k​ayabanerve:matrix.org >__ I'll reach out elsewhere     

> __< j​effro256:monero.social >__ ^^^^ Ok yes we can't do my fun idea b/c kayaba ruined it with math or whatever     

> __< j​effro256:monero.social >__ But by the time we have a PQ migration, and aren't assuming hardness of DLP, then there's a good chance that if we let people race to spend pre-RingCT (AKA pre-2018) outputs, it would just end with QC key breakers acquiring and then dumping 9% of the XMR supply     

> __< j​effro256:monero.social >__ So yeah it might end up being better to just forget about them     

> __< k​ayabanerve:matrix.org >__ I support only supporting PQ-safe methods after a QC is a sufficient threat to exist, banning spending old outputs entirely. We're discussing roughly five years to be able to migrate to a wallet which has a PQ-safe migration method.     

> __< j​effro256:monero.social >__ By *old outputs* here, you mean pre-FCMP++?     

> __< k​ayabanerve:matrix.org >__ No, any EC outputs which don't have the necessary binding to be migratable.     

> __< k​ayabanerve:matrix.org >__ So it's old by age of wallet, not by time of presence on-chain.     

> __< j​effro256:monero.social >__ Okay, then yes I agree   


# Action History
- Created by: Rucknium | 2024-12-17T21:21:30+00:00
- Closed at: 2025-01-07T20:40:19+00:00
