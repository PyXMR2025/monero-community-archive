---
title: Monero Research Lab Meeting - Wed 15 November 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/928
author: Rucknium
assignees: []
labels: []
created_at: '2023-11-14T17:15:57+00:00'
updated_at: '2023-12-17T17:14:44+00:00'
type: issue
status: closed
closed_at: '2023-12-17T17:14:44+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them? Info:
- [Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf)
- [Monero multi-signature patch review by Inference](https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf)
- [Rust alternative implementation](https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs) by @kayabaNerve

3. Any other business


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#925 

# Discussion History
## plowsof | 2023-12-17T16:58:35+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting here in one hour.     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ Meeting time: https://github.com/monero-project/meta/issues/928     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​effro256:monero.social >__ Howdy     

> __< rbrunner >__ Hello     

> __< k​ayabanerve:matrix.org >__ Hello again     

> __< a​js_:matrix.org >__ hi     

> __< weechat2 >__ hi     

> __< h​into.janaiyo:matrix.org >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< j​berman:matrix.org >__ hello     

> __< j​effro256:monero.social >__ Rucknium: the link on that Github issue for kayaba's alternate multisig implementation is the wrong link I believe     

> __< t​obtoht:monero.social >__ hi     

> __< r​ucknium:monero.social >__ me: Improved decoy selection with OSPEAD.     

> __< r​ucknium:monero.social >__ Oh you are right, jeffro256     

> __< r​ucknium:monero.social >__ Should be https://github.com/serai-dex/serai/blob/develop/coins/monero/src/wallet/send/multisig.rs     

> __< r​ucknium:monero.social >__ Thanks. Fixed     

> __< j​berman:matrix.org >__ me: finalizing background sync, GUI implementation is nearly done     

> __< a​js_:matrix.org >__ starting to plan for monerokon: https://kanban.monerokon.org     

> __< r​ucknium:monero.social >__ 3) Discuss: How to confirm security of Monero's multisignature protocol? Do we need mathematical security proofs, and can we get them?     

> __< r​ucknium:monero.social >__ Outcomes could be: 1) Try to get a security proof for current C++ Monero multisig. 2) Get security proof for kayabanerve 's Rust implementation. 3) Do nothing and wait for Seraphis multisig implementation and security proofs. 4) Something else?     

> __< weechat2 >__ me: more serialization stuff; working on my convulted gpg setup; figuring out how to p2p-ssl tests (if at all)     

> __< j​effro256:monero.social >__ I wrote some code which would allow `wallet2` to import/export part of its multisig info per onetime-address instead of everything all at once, which would help improve the scalability of syncing multisig info on multisig messaging systems     

> __< weechat2 >__ someone posted a security review by inference, did you see that rucknium?     

> __< r​ucknium:monero.social >__ Is weechat2 vtnerd?     

> __< weechat2 >__ ah crap, sorry     

> __< r​ucknium:monero.social >__ Security proof is different from security review of the code. My knowledge of this area is shallow, so maybe someone else can explain more.     

> __< vtnerd >__ it looked like a review of the code based on the report I saw (so they did both)     

> __< k​ayabanerve:matrix.org >__ I believe the focus should be on ensuring Monero's security independent of my own work. Even if my work is proven secure, Monero still should ship a non-experimental multisig as a piece of core infra. Unless Monero is willing to ship monero-serai than...     

> __< k​ayabanerve:matrix.org >__ vtnerd: Mind clarifying with a link, please?     

> __< k​ayabanerve:matrix.org >__ *ship monero-serai, then...     

> __< vtnerd >__ https://community.rino.io/rino-multisig-pr8194-audit-20220627.pdf     

> __< vtnerd >__ rino paid for it, since it was part of their core business     

> __< k​ayabanerve:matrix.org >__ Oh, the RINO audit     

> __< vtnerd >__ was that not good enough? They definitely looked at the code based on what I saw, but maybe this is untrusted for some reason?     

> __< vtnerd >__ rino paid for it, inference did the review     

> __< vtnerd >__ *or I assume rino paid     

> __< k​ayabanerve:matrix.org >__ IIRC, that work explicitly says it's incomplete as it doesn't have a formal reference to verify against     

> __< r​ucknium:monero.social >__ I think we don't know if the math is right. Code can perfectly execute math, but if the math isn't right then the code is vulnerable.     

> __< vtnerd >__ kayabanerve : I don't remember seeing that listed in the report (that its incomplete)     

> __< r​ucknium:monero.social >__ Lack of math security proofs is blocking a lot of Monero development work.     

> __< j​berman:matrix.org >__ For current C++ Monero multisig: I believe we would need security proofs (or at least formalized mathematical documentation of the protocol). Then probably a security review to verify the code matches up with that spec     

> __< k​ayabanerve:matrix.org >__ The burning bug patch also wasn't included in the RINO audit.     

> __< rbrunner >__ It was UkoeHB who rewrote and improved large parts of the multisig code. I think to remember that he was *for* the experimental label quite strongly.     

> __< k​ayabanerve:matrix.org >__ I don't see such a warning present, yet I have to note at no point in this audit does it comment on the protocol's security. It solely comments security against specific attacks. The warning I'm thinking of may have been human commentary associated with it not in the literal report...     

> __< k​ayabanerve:matrix.org >__ (not that any audit should say the protocol is guaranteed to be secure, to say the audit isn't inclusive of the protocol)     

> __< k​ayabanerve:matrix.org >__ > The client requested a review of this patch to the multisig system, in pull request #8149. The code was     

> __< k​ayabanerve:matrix.org >__ reviewed at commit f5e33479d656bc95001d2f135651e9fe9194681a.     

> __< k​ayabanerve:matrix.org >__ > We also assessed the three vulnerabilities the patch sought to address, looking at their security impact,     

> __< k​ayabanerve:matrix.org >__ and the extent to which they have been adequately addressed by the changes in the patch     

> __< k​ayabanerve:matrix.org >__ This is an extremely distinct scope from the multisig protocol and its implementation.     

> __< vtnerd >__ do you remember the name of the paper this was the musig code was based on?     

> __< k​ayabanerve:matrix.org >__ MRL-0009 has the ECDH-based DKG and a three-round sign. Monero implemented the ECDH-based DKG to... some degree, which I can't comment, and a two-round sign. The current sign implementation is closest to Musig2.     

> __< k​ayabanerve:matrix.org >__ I know Monero's DKG is the same premise. I'm not familiar enough to confirm it's the same protocol (or even that it attempts to be the same protocol).     

> __< r​ucknium:monero.social >__ https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf Brandon Goodell and Sarang Noether (2018) "Thring Signatures and their Applications to Spender-Ambiguous Digital Currencies"     

> __< j​berman:matrix.org >__ kayabanerve since you implemented FROST (which already has security proofs) in monero-serai, would your impl need anything further spec'd for the Monero-specific parts?     

> __< k​ayabanerve:matrix.org >__ Not to be a dick, but to be a dick, it would be immensely easier to prove the security of monero-serai AFAIK. Unfortunately, proving the security of monero-serai's multisig impl doesn't equal security for Monero's shipped multisig impl.     

> __< rbrunner >__ Why is that? Is it much simpler?     

> __< j​effro256:monero.social >__ It's based on FROST, yeah?     

> __< j​effro256:monero.social >__ oops already asked     

> __< r​ucknium:monero.social >__ Ok. So why not change Monero's shipped multisig implementation to a C++ version of your Rust implementation?     

> __< rbrunner >__ Ah, ok, "FROST (which already has security proofs)"     

> __< k​ayabanerve:matrix.org >__ jberman: We don't have a custom DKG. We use PedPoP from the FROST paper. Accordingly, we don't need any security proofs reviewed. AFAIK, the ECDH-based DKG has proofs yet not reviewed proofs. Whether or not that needs its proofs reviewed, and whether or not Monero tries to impl that ECDH-based DKG protocol (or its own ECDH-based DKG protocol we handwave as close enough), I can't c<clipped message     

> __< k​ayabanerve:matrix.org >__ omment. Please note RINO didn't audit that the DKG currently in Monero is equivalent to the one in MRL-0009.     

> __< k​ayabanerve:matrix.org >__ As for the signing code, FROST itself is proven, with layers of review, and modular-frost is Serai's audited FROST implementation. Not only is it audited as a library (with, IMO, what I'd call praise from sarang), it's also compliant with the IETF draft. The IETF draft takes took the academic paper (which can be implemented in several ways) and created a literal spec to match.     

> __< rbrunner >__ That would make any already built multisig wallets invalid, right?     

> __< r​ucknium:monero.social >__ The Rust implementation has N^2 message passing complexity. Monero's C++ implementation has N! complexity (N factorial). That's another reason to switch to the Rust impl.     

> __< r​ucknium:monero.social >__ rbrunner: well, you could have both implementations in there, one legacy and one new.     

> __< k​ayabanerve:matrix.org >__ There are many Monero-specific components in several ways. modular-frost then had a CLSAG algorithm written for it. While modular-frost ensures the integrity of the nonces, and the private key, and modular-frost was audited (meaning it does most of the heavy lifting), that doesn't change we have our own CLSAG algorithm floating around.     

> __< k​ayabanerve:matrix.org >__ And then beyond the raw CLSAG algorithm, there's the entire TX construction code (though solely the CLSAG code could be integrated into Monero proper).     

> __< vtnerd >__ I remember reading the musig2 paper now, the code definitely was based on that (which has a security proof that needs reviewing?)     

> __< k​ayabanerve:matrix.org >__ rbrunner: Technically, you could run a conversion protocol, but you shouldn't.     

> __< j​effro256:monero.social >__ Technically, and correct me if I'm wrong, but I think you also only need O(N^2) messages, just that the size of the messages is N!     

> __< r​ucknium:monero.social >__ The original multisig implementation was flawed. That makes me wonder about the MRL-0009 paper. I haven't read the paper. It had a security proof against at least one type of attack, but I'm not sure if against all types of attacks.     

> __< k​ayabanerve:matrix.org >__ vtnerd: The parts of Monero signing which needs proving/review/whatever is the CLSAG integration (as it requires one nonce BUT across two generators) *and* the key... interpolation?     

> __< vtnerd >__ rucknium, I recall the implementation being based on musig2 and not mrl009     

> __< k​ayabanerve:matrix.org >__ Actually, there is no interpolation in the ECDH-based DKG. Accordingly, for Monero signing, the sole part up for discussion is the CLSAG-specifics and the DKG.     

> __< vtnerd >__ or maybe mrl009 is the same? Id have to look     

> __< k​ayabanerve:matrix.org >__ I'll also note monero-serai implements *identifiable aborts*, and checks the data it's handed for propriety at each step. AFAIK, the Monero codebase doesn't have identifiable aborts and simply errors if the final signature fails. This creates vastly different DoS properties and may affect security analysis (as one may give you more leeway than the other). I'd ask koe to comment mo<clipped message     

> __< k​ayabanerve:matrix.org >__ re before I make any final comments though.     

> __< rbrunner >__ Seems to be that before we can decide how to best move forward some research is needed: What is really implemented now in C++?     

> __< k​ayabanerve:matrix.org >__ We also have a dedicated crate for building fiat-shamir transcripts, which was audite,d and does a lot of work with domain-separation, and minimize data sent around (minimizing opportunities to insert malicious data), etc, etc     

> __< rbrunner >__ Not to forget that we need a way to carry all this forward to Seraphis. I think multisig there is already implemented.     

> __< k​ayabanerve:matrix.org >__ MRL-0009 is an ECDH-based DKG (and Monero also uses a ECDH-based DKG, I can't comment if they're intended to be the same) and a proven, Musig-DN-esque signing protocol. Monero's current is Musig2 inspired.     

> __< k​ayabanerve:matrix.org >__ The audit did not confirm Monero's DKG is as specified in MRL-0009's, so even if they're intended to be equivalent, RINO's audit didn't cover that.     

> __< k​ayabanerve:matrix.org >__ (and i keep going on about intent as we got into this issue with Drijver's in the first place because Monero didn't impl MRL-0009's Musig-DN-esque protocol yet a Musig-esque protocol)     

> __< k​ayabanerve:matrix.org >__ What'd likely be easiest, in a pure-C++ way, is to explicitly intended Monero's DKG to match MRL-0009 (if not already) and have it audited to line up. Then, a Musig2-esque CLSAG should be formalized (likely a modification of MRL-0009's Musig-DN-esque CLSAG?) and Monero should explicitly intended to match it. The fact it lines up should be audited.     

> __< k​ayabanerve:matrix.org >__ After that, we can claim we have a proven protocol implemented with the implementation audited. I believe that'd warrant removing the experimental label.     

> __< rbrunner >__ Can we for a change speculate a bit, if that's ok. What problems could there be in the current protocol, what bad things could happen?     

> __< rbrunner >__ I think people call this "failure modes"     

> __< rbrunner >__ It obviously works correctly, per se, as long as nobody starts an attack     

> __< k​ayabanerve:matrix.org >__ I also personally believe extending FROST (which uses the same binomial nonces as Musig2) to CLSAG was natural and security of it should be considered trivially following. I have no practical doubts in its security. The one note is you have to publish your nonces across generators G *and* hash_to_point(K). I checked those nonces were correctly formed. Monero... may not have? And t<clipped message     

> __< k​ayabanerve:matrix.org >__ hat part I don't like. if Monero does perform that check, I'd say the theory behind Monero's multisig signing being sane likely follows.     

> __< k​ayabanerve:matrix.org >__ Since there's no identifiable aborts, a single malicious participant can potentially hold the protocol up ad infinitum as signers brute force all possible combinations of t over n until they find a multisig without the malicious signer(s).     

> __< rbrunner >__ The building of keys, or also the signing of transactions?     

> __< k​ayabanerve:matrix.org >__ Signing.     

> __< k​ayabanerve:matrix.org >__ If you have a 7-10 multisig, any 7 should be able to sign. If 3 are malicious, only a single combination will be valid. If you can't identify that combination, you have to brute force it.     

> __< h​into.janaiyo:matrix.org >__ kayabanerve: has there been any attempts at FFI for`multisig.rs` or monero-serai yet? i'm assuming cxx would be used?     

> __< k​ayabanerve:matrix.org >__ 7-10 combinations gets up there in possibility count...     

> __< k​ayabanerve:matrix.org >__ It's still feasible. With multisig's at the size of Serai though, no, length of the universe esque bs. That's why we guarantee if there's a fault, one faulty participant will be kicked out, reverting it to being linear to the amount of malicious actors (not what I believe to be some factorial)     

> __< k​ayabanerve:matrix.org >__ hinto: No     

> __< rbrunner >__ I don't understand. Isn't that trivial? I mean, if enough people are not in the mood to sign, everything comes to halt, no?     

> __< k​ayabanerve:matrix.org >__ If there's 3 malicious, there are 7 who want to sign.     

> __< j​effro256:monero.social >__ Well one participant could pretend they want to sign and submit bad data, and currently there's no way to figure out who dud     

> __< k​ayabanerve:matrix.org >__ That's the threshold. The system shouldn't halt.     

> __< rbrunner >__ Those people would claim to cooperate, but do otherwise?     

> __< k​ayabanerve:matrix.org >__ Right.     

> __< rbrunner >__ Any easy way to improve on that within the current C++ implementation?     

> __< k​ayabanerve:matrix.org >__ Forcing it to a brute force of possible signing sets unless you have a identification protocol. AFAIK, Monero's protocol enables one and the Monero code simply doesn't calculate/report it. I'm also unsure how useful the blame would be in a round robin settings. If all that can happen is a single node files out an accusation, with no evidence, it's not useful.     

> __< k​ayabanerve:matrix.org >__ So we'd need not only to have proper reporting, yet to be able to export a proof of blame.     

> __< k​ayabanerve:matrix.org >__ In a FROST setting, there's no linear round robin. You simply send everyone every message while signing, and you don't need to tell people someone faulted. You just all detect if someone did.     

> __< k​ayabanerve:matrix.org >__ Or we don't support identification, forcing the multisig to small-scale use cases which at worse become a game of Secret Hitler     

> __< j​berman:matrix.org >__ hinto: here's a start at using cxx for integrating kayaba's full chain membership proofs into the monero repo: https://github.com/j-berman/monero/commit/722f266edd75e3ad521b01a9b6b92dae72c1ffa9     

> __< rbrunner >__ And how about any risks that somebody could steal funds that shouldn't be able to?     

> __< rbrunner >__ Suddenly somebody is able to sign alone, through some loophole     

> __< rbrunner >__ Not very probable, right?     

> __< k​ayabanerve:matrix.org >__ In the signing protocol? That'd be via challenge manipulation or secret key leakage.     

> __< t​obtoht:monero.social >__ jberman: How will you do gitian builds? That's _a lot_ of transitive dependencies.     

> __< k​ayabanerve:matrix.org >__ Challenge manipulation should be stopped via binomial nonces + higher level code.     

> __< k​ayabanerve:matrix.org >__ (don't sign a raw hash you're handed, sign an intended tx you hash yourself)     

> __< k​ayabanerve:matrix.org >__ tobtoht: Serai has in its repo reproducible builds of a wasm blob.     

> __< k​ayabanerve:matrix.org >__ A wasm blob != monero-serai for x86. I'm just commenting we have a Docker setup to repro build Rust.     

> __< k​ayabanerve:matrix.org >__ So there's a basis of work there....     

> __< rbrunner >__ Whatever nice things can be said about that Serai multisig implementation, I somehow doubt that's the way to go. But well, not much more than a gut feeling     

> __< rbrunner >__ And this classic here, in a way: https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/     

> __< k​ayabanerve:matrix.org >__ I'll accept free audits as I'm not an idiot but I don't believe Monero should adopt monero-serai's impl.     

> __< UkoeHB >__ Recently I have begun to think it is a mistake having multisig integrated in the core monero repo. I spent a ton of time working on multisig to get it perfect, and the end result is a lot of advanced code that realistically cannot be reviewed and maintained without a lot of resources. The core monero wallet should be designed to support custom wallet extensions, and multisig should go in a separate repo that can be      

> __< UkoeHB >__ maintained (both dev work and security review/proofing) by those who depend on multisig. If we don't do that, multisig will end up an albatross blocking seraphis migration.     

> __< k​ayabanerve:matrix.org >__ + identifiable aborts? Except those may be quite annoying in the round robin setting...     

> __< k​ayabanerve:matrix.org >__ Actually, I don't believe we can have identifiable aborts *by key share* in the round robin setting because two people hold each key. We'd have to have add message authentication over every single message in the round robin protocol to obtain a single origin of a message (I don't assume that's already present?).     

> __< k​ayabanerve:matrix.org >__ *in the ECDH setting     

> __< k​ayabanerve:matrix.org >__ I do believe it's important for Monero to offer a canonical multisig, whether or not it's in a separate repository.     

> __< j​berman:matrix.org >__ tobtoht: AFAICT zcash implements gitian reproducible builds using cxx + rust code integrated on their end as well. It doesn't look too bad on first glance     

> __< rbrunner >__ Yeah, to depend on those people "who need it" is maybe a tad optimistic     

> __< j​effro256:monero.social >__ Are you saying that the current multisig implementation in the core repo needs round robin? AFAIK, there's no specific order nor signals to "pass" on the tx or submit disproval required for signin     

> __< rbrunner >__ No, the tx goes from one signer to the next     

> __< rbrunner >__ At least I don't know any other way to do it     

> __< t​obtoht:monero.social >__ jberman: Interesting, I'll have a look.     

> __< k​ayabanerve:matrix.org >__ I'm saying because every key share is held by two people under the ECDH protocol, if a key share's contribution isn't valid, you can't identify a human at fault *because* two human had the key share.     

> __< k​ayabanerve:matrix.org >__ I'm unsure the signing protocol's message format and if you can associate a human with specific contributions     

> __< rbrunner >__ Well, on the other hand I doubt that anybody seriously needs and seriously considers something like 7/10     

> __< k​ayabanerve:matrix.org >__ ... i'm looking to support 101/150 :(     

> __< k​ayabanerve:matrix.org >__ i'm right here rbrunner :( right here :(     

> __< rbrunner >__ and the combinatorial horror that ensues with people that try to sabotage     

> __< k​ayabanerve:matrix.org >__ :P There are large-scale use cases is my point.     

> __< rbrunner >__ I guess you have a terrribly special use case for that?     

> __< k​ayabanerve:matrix.org >__ Whether or not Monero wants to support them is a distinct issue, but I'd argue the current limit (16) likely needs to be significantly reduced.     

> __< k​ayabanerve:matrix.org >__ I think, already, 16 isn't feasible for humans to bother with *and* it likely has to many combinations to not break under a few malicious actors.     

> __< rbrunner >__ If you think of the use case "Not a single person has all the XMR, but a handful of carefully selected people" you probably land at 2/4, or maybe 3/5     

> __< k​ayabanerve:matrix.org >__ If Monero only wants to support up to 5 signers, I wouldn't object, as that lines up with most human use cases.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Decentralized network which receive coins on Monero. If we were only given 10 key shares, we could only have 10 validators. Not really too decentralized...     

> __< k​ayabanerve:matrix.org >__ It's definitely special, yet it's not unique. THORChain currently claims their integration is blocked on technical reasons (including multisig being experimental).     

> __< rbrunner >__ Oh well, those people :)     

> __< k​ayabanerve:matrix.org >__ Though I'm not asking Monero to support this use case. monero-serai exists for a reason.     

> __< j​effro256:monero.social >__ What's the reason for not wanting Monero to adapt moner-serai?     

> __< k​ayabanerve:matrix.org >__ This, and reducing the amount of supported signers to 5 or so, is my current advocacy.     

> __< rbrunner >__ To manage the CCS in the future, in particular?     

> __< k​ayabanerve:matrix.org >__ jeffro256: I don't believe there's enough reason present in it to justify the Rust toolchain and dependency set.     

> __< k​ayabanerve:matrix.org >__ rbrunner: 5 signers just sounds enough to manage most boards/CEX cold wallets/safety deposit backups/families.     

> __< j​effro256:monero.social >__ Ah okay. And Ukoe is of the opinion to not have it in the core repo at all     

> __< j​effro256:monero.social >__ have multisig     

> __< k​ayabanerve:matrix.org >__ Monero already has an experimental multisig. Having it cross the line is feasible IMO, re: scope of remaining work.     

> __< k​ayabanerve:matrix.org >__ Not sure re: developers willing to work on it.     

> __< r​ucknium:monero.social >__ Let's continue the meeting for at least 15 more minutes unless the main participants need to leave.     

> __< r​ucknium:monero.social >__ "What'd likely be easiest, in a pure-C++ way, is to explicitly intended Monero's DKG to match MRL-0009 (if not already) and have it audited to line up. Then, a Musig2-esque CLSAG should be formalized (likely a modification of MRL-0009's Musig-DN-esque CLSAG?) and Monero should explicitly intended to match it. The fact it lines up should be audited."     

> __< j​effro256:monero.social >__ Do we know if identifiable aborts are possible to be added to future signing sessions while keeping key data backwards compatible?     

> __< r​ucknium:monero.social >__ ^ Do we think there are enough "internal + external resources to do this? Is it worth it?     

> __< r​ucknium:monero.social >__ Has MRL-0009 been peer reviewed?     

> __< k​ayabanerve:matrix.org >__ jeffro256: If there's not a key actively associated with humans in the current protocol, then no, which I'd have to check. Regardless, my advocacy is reduced size multisigs, not identifiable aborts at this time (purely as a cost cutting measure)     

> __< k​ayabanerve:matrix.org >__ Not AFAIK, though that's not on my list of requirements.     

> __< t​obtoht:monero.social >__ jberman: Only for x86_64 linux. https://github.com/zcash/gitian.sigs/tree/master     

> __< k​ayabanerve:matrix.org >__ From my understanding, reproducible builds from x86_64 for other platforms aren't problematic. Reproducible builds from other platforms for a specific platform are.     

> __< k​ayabanerve:matrix.org >__ I have a friend who ships a binary which must be reproducible and it can't be reproduced from ARM due to *host* platform effecting the target binary.     

> __< t​obtoht:monero.social >__ The difficulty is in setting up cross-compile toolchains.     

> __< k​ayabanerve:matrix.org >__ I don't personally mind the comment "run docker in a x86-64 emulator to build for ARM" though.     

> __< k​ayabanerve:matrix.org >__ Rust has *great* support for cross-compilation.     

> __< k​ayabanerve:matrix.org >__ https://github.com/serai-dex/serai/blob/develop/orchestration/runtime/Dockerfile     

> __< k​ayabanerve:matrix.org >__ Here's how we handle reproducible builds     

> __< k​ayabanerve:matrix.org >__ We grab a specific Docker image, move to a Debian package snapshot, install deps, cross-compilation enabled via `rustup target add`, and then it's a very traditional build command.     

> __< k​ayabanerve:matrix.org >__ ```     

> __< k​ayabanerve:matrix.org >__ rustup target add riscv32imac-unknown-none-elf     

> __< k​ayabanerve:matrix.org >__ sudo apt update && sudo apt install -y gcc-riscv64-unknown-elf gcc-multilib     

> __< k​ayabanerve:matrix.org >__ cd tests/no-std && CFLAGS=-I/usr/include cargo build --target riscv32imac-unknown-none-elf     

> __< k​ayabanerve:matrix.org >__ ```     

> __< k​ayabanerve:matrix.org >__ And here's Serai code for RISC-V builds (not checking reproducibility)     

> __< k​ayabanerve:matrix.org >__ Also, sorry, to clarify. Here's how *Serai* handles.     

> __< r​ucknium:monero.social >__ If anyone really wants to work on multisig, especially in the direction of kayabanerve 's proposal, please speak up. IMHO, this was a productive conversation, but I don't expect any action to be taken unless more labor it put toward the problem. Thanks everyone.     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-11-14T17:15:57+00:00
- Closed at: 2023-12-17T17:14:44+00:00
