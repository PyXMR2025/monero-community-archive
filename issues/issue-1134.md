---
title: Monero Research Lab Meeting - Wed 01 January 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1134
author: Rucknium
assignees: []
labels: []
created_at: '2024-12-31T20:11:10+00:00'
updated_at: '2025-01-15T15:12:08+00:00'
type: issue
status: closed
closed_at: '2025-01-15T15:12:08+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography](https://github.com/monero-project/research-lab/issues/131)

4. Any other business

5. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1127 

# Discussion History
## Rucknium | 2025-01-05T14:55:48+00:00
Log

> __< c​haser:monero.social >__ with the switch to Carrot, for new wallets, can we do away with the prefix difference between main and subaddresses (4... vs 8...)?     

> __< c​haser:monero.social >__ also, am I correct assuming that...     

> __< c​haser:monero.social >__ * ...for hardware wallets and wallets derived from 25-words mnemonics, the user will need to know the version of their wallet and choose it during the import flow?     

> __< c​haser:monero.social >__ * ...for future Polyseeds (generated after the FCMP++ fork), this hell *could* be avoided if Polyseed and its implementations are updated in time to use one of the free feature bits to bump the wallet version?     

> __< dukenukem >__ Reminder for enthusiasts! MoneroKon 5 conference still seeks your ground-breaking ideas on security, privacy, and decentralization. Share your insights and be part of the dialogue. Submit your talk proposal today! Apply: http://cfp.twed.org/mk5/cfp     

> __< dukenukem >__ If not interested in applying at the moment, share with friends and privacy-adjacent communities!     

> __< c​haser:monero.social >__ (cont.) assuming the latter point is correct, it would work reliably only for the bumped Polyseeds, since a user may not update the wallet they use for mnemonic generation by the fork date     

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1134     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ Hello     

> __< rbrunner >__ Hello     

> __< r​ucknium:monero.social >__ Happy New Year     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Likewise!     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. Probably will be submitting milestone 2 next week.     

> __< r​ucknium:monero.social >__ MoneroKon 2025 has posted its call for presentations. The submission deadline in March 25: https://cfp.twed.org/mk5/cfp     

> __< dukenukem >__ OSPEAD!? Nice!     

> __< dukenukem >__ Milestone 2 - Deliver initial probability density function to scientific review panel     

> __< dukenukem >__ https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html     

> __< r​ucknium:monero.social >__ These plots are beautiful, I tell you     

> __< dukenukem >__ Looking forward. About time. :-P     

> __< dukenukem >__ Almost in sync with FCMP++!     

> __< r​ucknium:monero.social >__ 3) Discussion: Post-quantum security and ethical considerations over elliptic curve cryptography https://github.com/monero-project/research-lab/issues/131     

> __< r​ucknium:monero.social >__ In the last two meetings we discussed resistance to quantum counterfeiting attacks. Maybe we can discuss PQ privacy.     

> __< s​yntheticbird:monero.social >__ I would like to ask a pretty dumb question. Under FCMP++, the breaking of a wallet with its public address by a QC, do not give adversary info on other public addresses used for its transactions?     

> __< j​berman:monero.social >__ My update: testing my reimplementation of kayabanerve's faster torsion check impl in order to speed up building the merkle tree for FCMP++. Moving back over to FCMP++ tx construction next     

> __< s​yntheticbird:monero.social >__ s/FCMP++/Carrot/Jamtis     

> __< s​yntheticbird:monero.social >__ my bad     

> __< r​ucknium:monero.social >__ SyntheticBird: I have had the same question in my mind     

> __< s​yntheticbird:monero.social >__ cool. The perfect forward secrecy make me think it isn't the case, otherwise one public address compromise all the underlying tx graph, but i have a doubt.     

> __< c​haser:monero.social >__ SyntheticBird: TBH I'm not sure I understand your question and would value a rephrasing     

> __< s​yntheticbird:monero.social >__ Afaik, on chain data are immune to quantum computer, as in no quantum adversary could break the transaction graph solely based on on-chain data. One limitation that has been shared however is that if a quantum adversary obtain a wallet public address, it can break the public key up to the wallet primary private key, compromising its privacy. The question is, does breaking a wallet<clipped me     

> __< s​yntheticbird:monero.social >__  private key and therefore history, give access to this quantum adversary to other public addresses of wallet which has been transacted to.     

> __< s​yntheticbird:monero.social >__ first paragraph, assuming FCMP++     

> __< r​ucknium:monero.social >__ With respect to PQ privacy, there are some PQ RingCT proposals, but the tx sizes would be huge. And that would require going back to rings instead of having a FCMP-like privacy. IIRC kayabaNerve suggested that there may be more size-efficient PQ FCMP-like proposals.     

> __< rbrunner >__ Is this equivalent to the question whether having the private key allows the QC to break the stealth addresses in the transactions out of that wallet as well?     

> __< a​rticmine:monero.social >__ The ballpark figure of  ~50000 bytes is huge but doable     

> __< s​yntheticbird:monero.social >__ rbrunner yeah thats equivalent, assuming of course in the context Carrot/Jamtis/FCMP++     

> __< a​rticmine:monero.social >__ Sorry 500000 bytes     

> __< a​rticmine:monero.social >__ For a TX     

> __< c​haser:monero.social >__ SyntheticBird: got it. I'm not sure, and would like to know as well     

> __< rbrunner >__ Lacking details, I just assumed that they do continue to use something worth the name "stealth address" ...     

> __< j​berman:monero.social >__ Pinging jeffro256. I may be wrong on this, but IIRC a break would compromise the wallet's seed, which an adversary could use to derive the wallet's other addresses     

> __< rbrunner >__ Isn't that a different question altogether?     

> __< s​yntheticbird:monero.social >__ ah. that wasn't the point.     

> __< s​yntheticbird:monero.social >__ its not about the wallet A's other addresses, but the addresses of other wallet B, C that wallet A transacted to     

> __< j​berman:monero.social >__ Ah, I'm not sure     

> __< s​yntheticbird:monero.social >__ mhm ig its time to panic     

> __< c​haser:monero.social >__ FWIW, I know this wasn't the question, but a QC can't "connect" addresses of a Carrot wallet, it would imply being able to break the Blake2b hashing algo: https://github.com/jeffro256/carrot/blob/master/carrot.md#613-subaddress-keys-new-hierarchy     

> __< s​yntheticbird:monero.social >__ ig my question is over if we want to focus on economic stability of monero in the PQ era     

> __< r​ucknium:monero.social >__ Here's one of the PQ RingCT papers by the way: Esgin, Steinfeld, and Zhao (2022). "MatRiCT+: More Efficient Post-Quantum Private Blockchain Payments" https://ieeexplore.ieee.org/document/9833655     

> __< r​ucknium:monero.social >__ The use the "+" convention, too :D     

> __< r​ucknium:monero.social >__ Double plus good.     

> __< c​haser:monero.social >__ sorry jberman, just realized I restated the same thing you said     

> __< c​haser:monero.social >__ but, to get back on topic, is it just me, or does a PQ migration with the current primitives and implementations mean putting up with very big, potentially impractical, addresses and tx sizes?     

> __< s​yntheticbird:monero.social >__ chaser afaik yes, the current PQ primitives (Module lattices, Fourier transform based, Hash-based signature, NTRU) are all requiring much much bigger key or signature sizes     

> __< s​yntheticbird:monero.social >__ maybe there is a way to cheat this from a UX perspective     

> __< s​yntheticbird:monero.social >__ I don't think this represent a scalability challenge tho     

> __< a​rticmine:monero.social >__ When Nielsen's Law of Bandwidth is factored in this is not that different from RingCT in 2017     

> __< s​yntheticbird:monero.social >__ I'll note tho. tevador seraphis-pq draft didn't tested S-NTRU.     

> __< c​haser:monero.social >__ I hope so. one thing that's hard to cheat on is address length. I've had doubts even about 244 characters in Jamtis-RCT     

> __< r​ucknium:monero.social >__ Animated address QR codes will be embedded in a little movie so at least users are entertained while their device reads them.     

> __< s​yntheticbird:monero.social >__ NTRU sizes for reference: https://ntruprime.cr.yp.to/security.html     

> __< s​yntheticbird:monero.social >__ Ok now that i see that I might understand why it wasn't shared. It's KEM not DSA     

> __< s​yntheticbird:monero.social >__ my bad     

> __< c​haser:monero.social >__ this, or encoding over the UTF-8 character space. I'm personally undecided     

> __< r​ucknium:monero.social >__ IIRC Brandon Goodell (surae) was working on PQ lattice cryptography before joining Cypher Stack.     

> __< f​ede:xmr.mx >__ Maybe sharing a 32-byte hash of the actual address, which must be registered in a sort-of DHT.     

> __< s​yntheticbird:monero.social >__ yeah i think we heard of that idea before.     

> __< c​haser:monero.social >__ it would be good to have him on board for this topic.     

> __< rbrunner >__ Before I worry too much about those lengths I will have a look what the quantum proofing research will bring in the next few years. Won't hardly stand still, I think.     

> __< c​haser:monero.social >__ I really don't like those approaches, but if something really has to give, on-chain registration is an option too.     

> __< c​haser:monero.social >__ Kayaba's Monerokon 2024 "unorthodox crypto for scaling" presentation may be adjacent related     

> __< c​haser:monero.social >__ rbrunner: very much indeed. I expect many novelties and optimizations. I don't know though how much we can afford waiting for those to become realized.     

> __< rbrunner >__ Agree     

> __< rbrunner >__ At least Monero "knows how to hardfork" if something decidedly better comes around ...     

> __< j​effro256:monero.social >__ Knowing address A does not reveal the sender of transactions that address A received XMR in. It also doesn't reveal which *other* addresses receive XMR to funded by those enotes. But if the QC knows of *any* public address of wallet A as well as wallet B, if can see that A sent B funds if there wasn't a churn in between to the "internal" view-balance secret     

> __< j​effro256:monero.social >__ Sorry for being so darn late     

> __< f​ede:xmr.mx >__ On-chain registration has UX issues: you must either pay a transaction fee for registering an address, which means it's impossible for newcomers to register it, or solve a PoW puzzle, which can frustrate users with long wait time. I'd rather use a non-permanent off-chain DHT which is less subject to scalability issues.     

> __< s​yntheticbird:monero.social >__ Thanks, that confirm that we can use disposable wallets for receiving funds and then send them an internal wallet and have QC protection     

> __< j​effro256:monero.social >__ But if wallet A receives some XMR, then churns it back to itself using the new Carrot key hierarchy, *then* sends it to wallet B, even though a QC could know the private view-incoming key for both wallet A and B, it can't say for certain that the funds moved from A->B. It could perform probabilistic timing and amount analysis, but there isn't a deterministic link     

> __< c​haser:monero.social >__ fede: that's true.     

> __< j​effro256:monero.social >__ Yeah at that point the privacy becomes similar to a cleartext amount BTC mixer under a quantum adversary. If a QC can see that wallet A received 398737693740037 pXMR, and then wallet B shortly thereafter received 398737693740037 - fee pXMR, then they can say with high probability that the funds were likely transferred A->B     

> __< j​effro256:monero.social >__ So *transferred* amount quantization as well as fee quantization is something we would likely want to look at in the future for posterity's sake     

> __< r​ucknium:monero.social >__ Having really high XMR precision must have seemed so clever at the time ;)     

> __< r​ucknium:monero.social >__ at the time it was decided, I mean. I guess that was Bytecoin that decided that     

> __< j​effro256:monero.social >__ Also you don't need a disposable wallet the way that Carrot key hierarchy is written, there is a symmetric secret used solely in hash functions that shouldn't *ever* leak due to ECC arithmetic. All change enotes are sent to this secret, which automatically makes change/selfsend forward secret *unconditionally*     

> __< j​effro256:monero.social >__ Existing wallets don't get this feature, and must migrate, but once migrated, this feature is completely opaque to the user     

> __< a​rticmine:monero.social >__ A caution here is that probabilistic guessing  can still be used to falsely accuse the innocent     

> __< j​effro256:monero.social >__ Yes, of course, but we can give them ammo to try if we're not careful     

> __< a​rticmine:monero.social >__ I agree we must eliminate the illusion of surveillance     

> __< s​yntheticbird:monero.social >__ jeffro256 would you happen to know a bit more about PQ primitives? we were talking size and practicality, do you know if there are ways to avoid this in the future     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< s​yntheticbird:monero.social >__ thanks     

> __< a​rticmine:monero.social >__ Thanks     

> __< j​effro256:monero.social >__ Thanks !     

> __< j​effro256:monero.social >__ Well basically the one thorn in the side of FCMP++ forward secrecy at the moment is the Diffie-Helman key exchange against the public addresses. All Carrot/Jamtis/legacy addresses easily reveal the private view key to a quantum computer, so getting rid of discrete log based key exchanges would more or less solve all on-chain privacy issues. There's multiple different ways to get r<clipped messag     

> __< j​effro256:monero.social >__ id of discrete log based key exchanges, but they mostly fall under two categories: 1) use a PQ key exchange, or 2) don't do an on-chain key exchange at all     

> __< s​yntheticbird:monero.social >__ Oh the second option was tevador proposal iirc     

> __< j​effro256:monero.social >__ I recommend reading the discussion in https://github.com/monero-project/research-lab/issues/106 for discussion of the latter     

> __< j​effro256:monero.social >__ That's something that is doable in the very near future without a lot of cryptography research needed     

> __< j​effro256:monero.social >__ It changes UX for sure though, don't get me wrong     

> __< j​effro256:monero.social >__ I think that people should start looking at and getting familiar with off-chain key exchanges, since it's an option much more accessible to developers who aren't familiar with PQ cryptography     

> __< j​effro256:monero.social >__ And it doesn't involve any changes to the transaction format, and as such, doesn't require widespread consensus     

> __< j​effro256:monero.social >__ So good for experimentation and getting PQ privacy sooner rather than later     

> __< c​haser:monero.social >__ since a SPHINCS+ pub key that targets 128-bit security is 32 bytes long (https://sphincs.org/data/sphincs+-r3.1-specification.pdf#page=58, Table 8), isn't that conducive to a PQ addressing scheme with the same base58 address lengths as we have today?     

> __< s​yntheticbird:monero.social >__ Yes but SPHINCS+ signature are HUGE     

> __< s​yntheticbird:monero.social >__ Last time i tested asurar0 PQ tool, the signature was like 40kB or smth     

> __< j​effro256:monero.social >__ You wouldn't need signatures for a key exchange AFAIK     

> __< s​yntheticbird:monero.social >__ jeffro256 KEM based KEX ?     

> __< s​yntheticbird:monero.social >__ S-NTRU might return into play if its the case     

> __< c​haser:monero.social >__ SyntheticBird: yeah, for now I'm just brainstrorming and handwaving every other problem away by e.g. hoping Nielsen's Law will hold. compute/bandwidth/storage/power can get cheaper over time, human attention and human willingness is much less likely to do so.     

> __< s​yntheticbird:monero.social >__ SNIPPERRR!!!     

> __< s​yntheticbird:monero.social >__ everyone take cover    


# Action History
- Created by: Rucknium | 2024-12-31T20:11:10+00:00
- Closed at: 2025-01-15T15:12:08+00:00
