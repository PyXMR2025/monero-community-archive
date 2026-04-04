---
title: Monero Research Lab Meeting - Wed 29 November 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/938
author: Rucknium
assignees: []
labels: []
created_at: '2023-11-29T15:17:19+00:00'
updated_at: '2023-12-17T17:15:02+00:00'
type: issue
status: closed
closed_at: '2023-12-17T17:15:02+00:00'
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

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#932 

# Discussion History
## plowsof | 2023-12-17T17:01:45+00:00
Logs 
> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours. We might discuss multisig again.     

> __< a​js_:matrix.org >__ would also like to plug CfP MoneroKon 2024     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/938     

> __< r​ucknium:monero.social >__ 1. Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ kayabanerve: Will you join the meeting today?     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2. Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Me: still on adding scanning tests to LWS. Found two bugs so far!     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< r​ucknium:monero.social >__ me: OSPEAD. Also, MAGIC Monero Fund fundraisers will likely appear in the next version of Feather wallet, using my API :)     

> __< h​into.janaiyo:matrix.org >__ working on an air-gapped machine guide https://malvarma.org     

> __< r​ucknium:monero.social >__ The (self-)nominations for two seats on the MAGIC Monero Fund committee members will open December 5.     

> __< r​ucknium:monero.social >__ 3. Discussion. Do we want to discuss multisig again?     

> __< r​ucknium:monero.social >__ The MAGIC Monero Fund has about 29,000 USD total in its general fund that it could deploy to improve multisig, as a bounty, request for proposals, or a grant. kayabanerve has a plan.     

> __< k​ayabanerve:matrix.org >__ The discussion present in the most recent MAGIC meeting was about the work necessary to make Monero's multisig proper regarding DKG alignment, signing protocol formalization, and P2P networking.     

> __< k​ayabanerve:matrix.org >__ The alternative reiterated was to drop multisig from the core repo, and in practice, advocate monero-serai.     

> __< k​ayabanerve:matrix.org >__ My personal suggestion was to replace PyBitmessage with either the Monero network itself OR Tor hidden services.     

> __< k​ayabanerve:matrix.org >__ With Arti, Tor now has a library interface. Tor hidden services use an existing P2P network, not requiring additional setup, ensure privacy, blend in, etc.     

> __< r​ucknium:monero.social >__ Is LibP2P not a good idea, after considering?     

> __< k​ayabanerve:matrix.org >__ With hidden services, we don't have to program a P2P stack. It's effectively coding a web server that receives multisig messages. We could likely even use IRC as the communication protocol for "how shimmed together can this be"     

> __< k​ayabanerve:matrix.org >__ *not a recommendation in the slightest, obviously.     

> __< k​ayabanerve:matrix.org >__ LibP2P, another candidate, was my recommendation for a new P2P network. that'd require basic infra and potentially have privacy issues (leakage of IPs of multisig participants, linkage of network bandwidth usage to recently published TXs)     

> __< v​tnerd:monero.social >__ Why would we go through the effort of creating another p2p infrastructure?     

> __< k​ayabanerve:matrix.org >__ I believe a solution based on Arti would still have minimal dependencies, be quite clean, and not require modifying monerod (potentially overloading it). It'd also work quite well with monero-serai which is also in Rust.     

> __< h​into.janaiyo:matrix.org >__ what is the status on `arti`'s onion support? from what I could tell a few weeks ago they were still in the process of stabilizing and testing against C tor     

> __< r​ucknium:monero.social >__ How good/bad would onion hidden service UX be for a noob user?     

> __< k​ayabanerve:matrix.org >__ vtnerd @vtnerd:monero.social: For multisig message delivery? Someone has to host a centralized relay server and port forward/manage UPnP, or we need some global P2P net, or to hook into an existing P2P net.     

> __< k​ayabanerve:matrix.org >__ Arti has burgeoning hidden service support and should happen in H1 24.     

> __< k​ayabanerve:matrix.org >__ Rucknium @rucknium:monero.social: The idea would be complete abstraction.     

> __< v​tnerd:monero.social >__ But we already have a p2p mechanism in monerod, why use another? And why arti instead of just leveraging standard tor daemon?     

> __< k​ayabanerve:matrix.org >__ So no user impact.     

> __< h​into.janaiyo:matrix.org >__ vtnerd: arti has a client library you can embed in applications, the user wouldn't need to run tor manually     

> __< k​ayabanerve:matrix.org >__ We'd have to modify Monero's P2P net to relay ephemeral messages.     

> __< k​ayabanerve:matrix.org >__ They'd need to go through Dandelion to not reveal IPs in a multisig.     

> __< k​ayabanerve:matrix.org >__ Ephemeral message bandwidth usage would reveal how many multisig TXs are actively in progress.     

> __< k​ayabanerve:matrix.org >__ This allows presuming some recently published TXs are from multisig wallets.     

> __< k​ayabanerve:matrix.org >__ It's additional burden on Monero itself with much worse privacy properties and nontrivial implementation complexity. Monero would need to become a private messaging network for it to be proper.     

> __< k​ayabanerve:matrix.org >__ As in, Monero itself would have to be an onion router for arbitrary messages as a piece of public infrastructure with multifaceted use cases.     

> __< v​tnerd:monero.social >__ Ok, I get the use case for tor, but not for libp2p. And I'm not sold on embedding arti instead of standard tor daemon     

> __< rbrunner >__ How would that Arti solution from the viewpoint of storing multisig messages, so they "wait for you"? It can be very bad UX wise if all signers have to be online at the some moment in time     

> __< k​ayabanerve:matrix.org >__ I'm not advocating LibP2P. That was an alternative.     

> __< k​ayabanerve:matrix.org >__ rbrunner: Everyone would have a message server. As long as one has liveness, all messages can be synced.     

> __< k​ayabanerve:matrix.org >__ This does presume authentication and humans handle consensus.     

> __< v​tnerd:monero.social >__ If the project/developers arti disappears, we are left maintaining this lib     

> __< k​ayabanerve:matrix.org >__ I'm not going to be for having usera download the Tor daemon and/or kludge it in vs including a purpose built library.     

> __< k​ayabanerve:matrix.org >__ Arti is under the Tor umbrella at this point afaik     

> __< v​tnerd:monero.social >__ What's wrong with having them install it via package manager? Only windows users are out of luck, and they are few now     

> __< k​ayabanerve:matrix.org >__ Hundreds of k in funding, wide interest and support, praise for cleaning tech debt and distinct intended use cases     

> __< rbrunner >__ Does that library just speak the Tor protocol for you, so to say?     

> __< k​ayabanerve:matrix.org >__ Yep     

> __< rbrunner >__ One can wonder then why it took so long to develop such a library, no?     

> __< k​ayabanerve:matrix.org >__ Instead of remote management of a Tor daemon for a hidden service, requiring an additional service, it's Tor as a lib     

> __< k​ayabanerve:matrix.org >__ Also, the proposal isn't necessarily to do this in monero     

> __< k​ayabanerve:matrix.org >__ I believe, due to lack of developer support, the inclination is to NOP monero multisig and focus on out-of-repo multisig     

> __< v​tnerd:monero.social >__ The repo claims it's not feature complete (arti) - does anybody know the status?     

> __< k​ayabanerve:matrix.org >__ Hidden services are a WIP with kinda support rn. A proper release is expected within the next few months.     

> __< rbrunner >__ Sounds to me like the best way to lose multisig support altogether, frankly     

> __< rbrunner >__ with "out-of-repo multisig"     

> __< rbrunner >__ "isn't necessarily to do this in monero" For example some standalone messaging daemon, with own repo and codebase?     

> __< k​ayabanerve:matrix.org >__ So we can integrate Monero's experimental multisig into some UX, using whatever people want for the P2P network, and try to find developers to maintain it.     

> __< k​ayabanerve:matrix.org >__ We can state there's a lack of developers to work on Monero multisig and encourage third-party solutions which do have developers.     

> __< k​ayabanerve:matrix.org >__ To be clear, last time this was discussed I said I believe multisig is critical and stated my belief Monero should maintain its multisig. I provided the path forward on that.     

> __< k​ayabanerve:matrix.org >__ Unless we have developers willing to maintain it, I cannot maintain my position.     

> __< k​ayabanerve:matrix.org >__ koe stated they wanted it out of repo.     

> __< k​ayabanerve:matrix.org >__ I also don't personally believe they want to further work on it, though we'd need to double check.     

> __< rbrunner >__ Not sure what exactly you mean with "maintain"     

> __< k​ayabanerve:matrix.org >__ rbrunner: Do all the work necessary to remove its experimental status.     

> __< v​tnerd:monero.social >__ I understood the multisig implementation well enough (especially compared to bp++), but have no idea how to stop the fake DKG attack or whatever it's called, without changing to a new algo     

> __< k​ayabanerve:matrix.org >__ Align the DKG with 0009     

> __< k​ayabanerve:matrix.org >__ Document the signing protocol     

> __< k​ayabanerve:matrix.org >__ Get everything audited     

> __< k​ayabanerve:matrix.org >__ The signing impl was audited. AFAIK, the dkg wasn't, and the signing protocol went unreviewed. We need an actual protocol and to confirm alignment.     

> __< k​ayabanerve:matrix.org >__ vtnerd @vtnerd:monero.social: The DKG in MRL-0009 has the same principle as ours and is proven.     

> __< k​ayabanerve:matrix.org >__ We just need to ensure alignment, that they're the same protocol, and audit.     

> __< rbrunner >__ Well, I always have that chicken-and-egg problem going around in my head. With no multisig that people dare to use, even with caution because experimental, nobody really cares about it     

> __< rbrunner >__ Or, in other words, we wait until it's perfect, we wait forever     

> __< k​ayabanerve:matrix.org >__ This leads to the fundamental fact:     

> __< k​ayabanerve:matrix.org >__ - Monero's multisig does not have developers volunteering     

> __< k​ayabanerve:matrix.org >__ - Third party impls do have developers     

> __< v​tnerd:monero.social >__ "same principle as ours" - you mean monero-serai or the musig2 implementation in monero     

> __< k​ayabanerve:matrix.org >__ I mean the ECDH-based DKG premised in MRL-0009 is the same building block as Monero's impl.     

> __< v​tnerd:monero.social >__ It does feel wrong exporting this outside of monero-project GitHub repo     

> __< k​ayabanerve:matrix.org >__ We just need to ensure the DKG implemented is MRL-0009 and not some handwaved protocol which also happens to be ECDH-based.     

> __< k​ayabanerve:matrix.org >__ And then audit it.     

> __< v​tnerd:monero.social >__ I guess we do that already with stuff in external     

> __< v​tnerd:monero.social >__ It would be nice if this were it's own repo, like I did with supercop, although that never got used outside monerod and lws really     

> __< k​ayabanerve:matrix.org >__ My preference is Monero's sovereignty via taking the steps needed on its multisig. Without developers to do that, my forced acknowledgement is to move to something with developers.     

> __< v​tnerd:monero.social >__ Does monero-serai implement mrl 009?     

> __< k​ayabanerve:matrix.org >__ If it's out of repo, and no longer in the monero core repo at all, we have greater flexibility, no technical blockers re: upgrades, and greater flexibility.     

> __< k​ayabanerve:matrix.org >__ No, it's the PedPoP DKG which has O(n**2) complexity, not O(n!)     

> __< rbrunner >__ This is all much too theoretical for me, I have to say. No way we will make it perfect first, then use it. But I think I have to carefully write an issue to argument     

> __< k​ayabanerve:matrix.org >__ As for signing, it's an extension over FROST hooking into an actual FROST lib. I think Monero's multisig can be argued as a Musig2 extension?     

> __< rbrunner >__ Can't do that here, ad-hoc     

> __< k​ayabanerve:matrix.org >__ Unless someone steps up to actively work on multisig, my recommendation is we stop endlessly discussing how that's what we want and expecting to eventually drop experimental.     

> __< k​ayabanerve:matrix.org >__ We Ack it's experimental indefinitely, and we focus our time and effort on solutions which have developers making them non-experimental.     

> __< v​tnerd:monero.social >__ Ok, so that's something to think about too. I could realistically attempt a mrl009 implementation, but it already has drawbacks, and I'm duplicating what could be leveraged by monero-serai. The downside is that critical crypto code is no longer controlled by monero-project     

> __< k​ayabanerve:matrix.org >__ Someone either has to step up or we have to drop the discussion. That's my take.     

> __< v​tnerd:monero.social >__ I'm saying I could step up, but I'm just duplicating work, no? Outside of the one nice to have of it being in monero proper     

> __< k​ayabanerve:matrix.org >__ (the discussion being dropping the experimental flag from Monero's impl. It's clear what the blocker is and talking ad infinitum doesn't remove it)     

> __< k​ayabanerve:matrix.org >__ I mean, MRL-0009, IMO, is definitively worse     

> __< k​ayabanerve:matrix.org >__ It's not just duplication but worse results     

> __< rbrunner >__ You know what, that may be a bit shocking, but that "experimental" does not really worry me. The whole thing, Monero is "experimental" if you apply the same strict measure     

> __< k​ayabanerve:matrix.org >__ Also, cc Rucknium @rucknium:monero.social: to jump back in after having me step up and then staying silent for the next 30m :p     

> __< rbrunner >__ If enough people "experiment" with Monero multisig because it's fun, support will materialize     

> __< k​ayabanerve:matrix.org >__ rbrunner: That I vehemently disagree with. I don't know any Monero developer who'd argue there's as likely a risk to lose coins with Bulletproofs as there is multisig.     

> __< k​ayabanerve:matrix.org >__ I may have to drop out in a few minutes due to battery issues, sorry.     

> __< v​tnerd:monero.social >__ kayabanerve: that's what I mean, I'm duplicating the functionality of this other lib when it has worse complexity in error case. It's mainly just whether we think it's worth having multisig controlled by monero-project.  rbrunner, thoughts on that?     

> __< rbrunner >__ Well, I think a "serious" coin must have multisig out of the box. And as I said, take it out of the core repo, it dies, to say it provocantly.     

> __< r​ucknium:monero.social >__ kayabanerve: This is cryptography + software engineering. I understand neither well. My opinion/concern is that the main proposal on the table to restart CCS is to escrow it with single-signer wallet managed by the same escrow agent as when the theft occured (luigi). We could have a better setup with multisig.     

> __< rbrunner >__ That's just the last excuse that people need to get rid of it :)     

> __< c​harutocafe:matrix.org >__ is removing from mainnet but keeping in stagenet/testnet an option even worth discussing?     

> __< rbrunner >__ For doing what with it then on these "play coin" nets?     

> __< v​tnerd:monero.social >__ Rucknium @Rucknium:libera.chat: that's another issue. This needs to be handled asap, the ccs is already backlogged with ideas that are now stalled     

> __< r​ucknium:monero.social >__ I don't really agree with rbrunner's reasoning. It is like https://en.wikipedia.org/wiki/Normalization_of_deviance . "Nothing catastrophic has happened yet, so it's safe enough."     

> __< rbrunner >__ That you don't agree doesn't surprise me :)     

> __< r​ucknium:monero.social >__ Yes, probably the CCS will be single-signer escrow again soon, but I hope that will not be permanent.     

> __< h​into.janaiyo:matrix.org >__ this seems like an "evolve or die" situation     

> __< rbrunner >__ I juggle with probabilities. What is, for example, the probability there is a gaping whole after koe rewrote much of the code and thought things through? It exists, but is small, IMHO     

> __< rbrunner >__ *gaping hole     

> __< h​into.janaiyo:matrix.org >__ wouldn't moving this functionality _outside_ of the core repo be desired? after all the core already is stuffed - makes maintenance and upgrades hard     

> __< v​tnerd:monero.social >__ The issue kayabanerve: mentions likely won't be too bad given the low number of signers for ccs     

> __< rbrunner >__ For me it's not the sheer size of the repo that makes things hard. It's complex code, that makes it hard. But, IMHO, not too much of it.     

> __< a​js_:matrix.org >__ Rucknium:  if there is w return to the status quo, it is unlikely there will be much motivation to look for better alternatives     

> __< r​ucknium:monero.social >__ AFAIK, koe wants to keep the "experimental" flag on the current multisig implementation. I guess koe thinks the probability of a gaping hole is high enough to keep the label.     

> __< rbrunner >__ I agree. No problem. I take the experimental multisig. Rino at least seems to think along the same lines.     

> __< r​ucknium:monero.social >__ RINO's threat model is different     

> __< rbrunner >__ Experimental multisig based web wallet better than no-multisig web wallet. Simple, no?     

> __< k​ayabanerve:matrix.org >__ vtnerd @vtnerd:monero.social: Not in error case. Always.     

> __< k​ayabanerve:matrix.org >__ I support Monero having multisig. I don't support it enough to do it myself. I'd love if you'd do it, vtnerd. I'd ask you if you find it worth it.     

> __< v​tnerd:monero.social >__ I don't understand, always what?     

> __< r​ucknium:monero.social >__ ajs_: A lot of community members are in favor of multisig for CCS. That's the motivation. And to not be complacent, lose XMR again, and damage reputation further.     

> __< k​ayabanerve:matrix.org >__ I found a vuln in the rewrite PR.     

> __< k​ayabanerve:matrix.org >__ Any TX leader could burn the multisig.     

> __< k​ayabanerve:matrix.org >__ Monero always has worse complexity, not just in the error case     

> __< rbrunner >__ I see that we approach things in quite fundamentally different ways. With all points of view having worth of course. I don't possess the truth.     

> __< r​ucknium:monero.social >__ Threat of burn in multisig could be analyzed as an ultimatum game in game theory I think: https://en.wikipedia.org/wiki/Ultimatum_game     

> __< rbrunner >__ Well, it's funny to worry about a bad first signer burning if the final signer that reaches the threshold can simply steal. Funny at least to me. A bit.     

> __< rbrunner >__ I guess that theoretically minded people versus, well, maybe call it pragmatist.     

> __< k​ayabanerve:matrix.org >__ rbrunner: It allows for millions in damages with just tens of thousands of dollars in losses in collaborative funding schemes.     

> __< v​tnerd:monero.social >__ kayabanerve: the bug you mentioned, this prevents one particular sign attempt, or permanently locks funds?     

> __< rbrunner >__ Yes. Not downplaying things. Attempting to put them into perspective.     

> __< rbrunner >__ Funding schemes dealing with millions can be robbed by the final signer. Just as bad.     

> __< rbrunner >__ At least if they need simple multisig     

> __< rbrunner >__ *if they use     

> __< h​into.janaiyo:matrix.org >__ on a more practical note - usage of multisig will definitely extend contributor payout delay even more :)     

> __< k​ayabanerve:matrix.org >__ The bug I found which survived the rewrite PR which enables burning the multisig.     

> __< v​tnerd:monero.social >__ This bug occurs in the setup phase then?     

> __< rbrunner >__ More like an exploit, seems to me. If nobody is malicious, I don't expect it happens, right?     

> __< k​ayabanerve:matrix.org >__ vtnerd @vtnerd:monero.social: It happened during signing. The TX leader could propose a TX which would.     

> __< k​ayabanerve:matrix.org >__ @rbrunner That's a bad threat model     

> __< k​ayabanerve:matrix.org >__ If you assume compromise=0, multisig offers recovery, not security     

> __< rbrunner >__ I was just arguing about calling this a "bug", not something more fundamental     

> __< v​tnerd:monero.social >__ Which would permanently lock funds?  This seems like something wrong with the implementation then     

> __< v​tnerd:monero.social >__ I could see how that would happen, one user goes into a spent state, even though the TX is dead     

> __< rbrunner >__ Our multisig transactions do not burn themselves just because full moon falls on a Monday, I mean     

> __< v​tnerd:monero.social >__ No, he is talking about a threat model. In the worse case someone gets hacked, and the hacker proposes a signature which locks funds     

> __< rbrunner >__ Agree with that, yeah. Would be nicer if that wasn't possible of course, no doubt.     

> __< k​ayabanerve:matrix.org >__ It's by the leader's prior ability to select the R used for the change address, which enabled triggering the burning bug.     

> __< rbrunner >__ But see: You are already hacked before that can happen. If you are hacked, tons of other bad things can happen instead if that burning is not possible.     

> __< k​ayabanerve:matrix.org >__ It was a comment on the rewrite PR having further findings still identified.     

> __< v​tnerd:monero.social >__ Yeah but we might as well do no multisig if that's that argument     

> __< rbrunner >__ Yes, that's why it's still experimental, and rightly so     

> __< rbrunner >__ There is some logic in that :)     

> __< t​obtoht:monero.social >__ I'm integrating multisig in Feather. It's mostly an exercise in designing practical ms UI/UX. I'm taking experimental multisig 'as-is', sticking a big not-for-production-use disclaimer on it, rewriting the MMS so it connects to a centralized self-hosted message relay (optionally over some user configurable SOCKS5-proxy). The thinking is: show users 'what could be possible' -> crea<clipped message>     

> __< t​obtoht:monero.social >__ te more demand for a better multisig implementation.     

> __< rbrunner >__ Couldn't have it said better, tobtoht.     

> __< rbrunner >__ Just don't program yourself into a burnout, do you ...     

> __< rbrunner >__ That's a lot of work     

> __< h​into.janaiyo:matrix.org >__ > centralized self-hosted message relay     

> __< h​into.janaiyo:matrix.org >__ what would this be exactly?     

> __< v​tnerd:monero.social >__ Why so confident that monero-serai has no such issues? I realize it follows a different standard, but it could have unknown bugs too.     

> __< r​ucknium:monero.social >__ kayabanerve: ^     

> __< t​obtoht:monero.social >__ A service that stores encrypted messages and allows participants to retrieve them. Thinking about using FastAPI + Redis for an MVP.     

> __< r​ucknium:monero.social >__ The meeting is over. Feel free to continue discussing multisig :)     


Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-11-29T15:17:19+00:00
- Closed at: 2023-12-17T17:15:02+00:00
