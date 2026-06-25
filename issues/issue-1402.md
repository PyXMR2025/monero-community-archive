---
title: Monero Research Lab Meeting - Wed 10 Jun 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1402
author: Rucknium
assignees: []
labels: []
created_at: '2026-06-10T15:40:27+00:00'
updated_at: '2026-06-24T14:16:13+00:00'
type: issue
status: closed
closed_at: '2026-06-24T14:16:13+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Helios/Selene review.

4. [Post-quantum encryption](https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). [Jamtis](https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).

5. [Monero-PSK](https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).

6. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

7. View-all/view-some key.

8. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

9. Any other business

10. Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs: #1399 

# Discussion History
## Rucknium | 2026-06-17T14:56:45+00:00
Logs

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1402     

> __< rucknium >__ 1. Greetings     

> __< tevador >__ Hi     

> __< jberman >__ waves     

> __< sgp_ >__ hello     

> __< boog900 >__ hi     

> __< rbrunner >__ Hello     

> __< jpk68:matrix.org >__ Hello     

> __< vtnerd >__ hi     

> __< jeffro256 >__ Howdy     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< UkoeHB >__ hi     

> __< articmine >__ Hi     

> __< tevador >__ me: Jamtis specs     

> __< UkoeHB >__ me: reviewed jberman's curve tree builder, probably start reviewing carrot_impl/etc.     

> __< syntheticbird >__ Hi     

> __< rucknium >__ me: I wrote a preliminary review of the monerosim network simulator public beta: https://github.com/Fountain5405/monerosim/issues/3 . I may have uncovered some connection stability issues that gingeropolous:monero.social  is working through. Also I'm keeping stressnet stressed.     

> __< jeffro256 >__ Me: updating some crypto code according to Cypherstack's FCMP++ audit, stressing the stressnet, working on header-only sync and wallet-side fee calculation logic locally      

> __< jberman >__ Continued remediation from phase 1 of the FCMP++ integration audit (Cypher Stack's audit was of comparable quality to the Trail of Bits audit they caught mostly the same informational issues [well done Cypher Stack], working with Trail of Bits to complete the final task from Phase 1B ensuring all expected legacy enotes remai [... too long, see https://mrelay.p2pool.observer/e/oqH734sLem1Zc1RN ]     

> __< vtnerd >__ me: primarily ssl related fixes to tests, and beginnings of the wallet metadata encryption lib I proposed in my ccs     

> __< vtnerd >__ also Im somewhat stalled on the block size limit issue, as I’ve exhausted ways to alleviate the limits of de-serialization unless we switch to a DOMless parser that knows what values its unpacking     

> __< gingeropolous >__ me: monerosim , responding to review     

> __< vtnerd >__ I thought I could sneak something in the existing code, but it doesn’t work with pruned txes being sent via p2p     

> __< jpk68:matrix.org >__ vtnerd: Boost.JSON is DOMless, right? That might also allow us to remove a dependency     

> __< rucknium >__ vtnerd:monero.social: Is this the 100MB limit?     

> __< rucknium >__ 3. Helios/Selene review.     

> __< rucknium >__ sgp_:monero.social ^     

> __< sgp_ >__ MAGIC Grants has received 7 quotes ranging from $15,000 to $100,000     

> __< sgp_ >__ The $15,000 one would be an honest review, but I recommend a review for $35,000 since the auditors appear to have more experience. It seems like the best compromise between cost and skill     

> __< sgp_ >__ Jeffo, Luke, and Berman can also add their comments if they like     

> __< vtnerd >__ jpk68:matrix.org: afaik, it is not domless     

> __< sgp_ >__ I would like to get approval during this meeting to go forward with the $35,000 one as the selected option     

> __< vtnerd >__ rucknium:monero.socialthis is the vague limit set by the epee decoder. I recally ofrnxmr:monero.socialclaiming it was actually limited around ~33MiB due to hitting the hard limits on strings     

> __< sgp_ >__ unless people strongly feel that it's best to select the cheapest one, or have other opinions     

> __< jberman >__ I second that opinion, $35k quote appears the best value     

> __< tevador >__ +1 for the 35K quote     

> __< rucknium >__ Did we get 24 hours notice on the H/S reviewer options?     

> __< vtnerd >__ and jpk68 the issue is not related to json, its that the epee format only has parsing to dom, unless we switch to my custom domless epee parser     

> __< rucknium >__ I don't want to delay, but I am wondering why we have this informal rule that is being broken more often than followed. Or did I miss a prior message?     

> __< sgp_ >__ I thought I posted it here earlier but I guess it was only this morning. Long day     

> __< rucknium >__ op irc_articmine:monero.social 10     

> __< rucknium >__ Oops     

> __< rucknium >__ Have jeffro256:monero.social , kayabanerve:matrix.org  , and jberman:monero.social  seen more details about the review quotes? > <sgp_> Jeffo, Luke, and Berman can also add their comments if they like     

> __< sgp_ >__ I'll let them answer but if someone else wants to review as well, please ask     

> __< jberman >__ We have 2 layers of beaureaucracy now for managing audits, and multiple audit tasks in flight. I don't fault sgp on this. We have been discussing the candidates internally as well > <rucknium> I don't want to delay, but I am wondering why we have this informal rule that is being broken more often than followed. Or did I miss a prior message?     

> __< jberman >__ rucknium: Yes     

> __< sgp_ >__ I do fault sgp on this :p     

> __< tevador >__ Any info about the lead time on the audit?     

> __< jberman >__ 35k candidate was also my number 1 prior to this meeting     

> __< jeffro256 >__ SGP sent info last week, but I just haven't gotten around to analyzing it deeply, sorry      

> __< sgp_ >__ tevador: Give me one sec to double check     

> __< sgp_ >__ In the quote they put June 8th as the suggested start date, but we are past that. So we will need to confirm new dates while finalizing     

> __< tevador >__ OK, it means they will probably start without a delay     

> __< sgp_ >__ Hopefully so. Before finalizing acceptance with them, I will get clarity on the new start date and ensure it's acceptable to berman, jeffro, luke     

> __< tevador >__ Does anyone object to going with the 35K quote?     

> __< sgp_ >__ fwiw, MAGIC Grants hired the same auditor for the June 8th slot because that other project moved a bit faster. Let me check when that ends; that end date might be the most likely new start date     

> __< sgp_ >__ that project is June 9 to 29. So if they can't do concurrent with different team members, then possibly a June 29th/30th start     

> __< rbrunner >__ I am not sure about accepting ... we have now only statements from sgp and jberman, if I followed correctly. Would be assuring to have at least 1 more IMHO     

> __< sgp_ >__ fwiw, I don't think this review is blocking anything, at least strictly speaking. It's something that needs to get done, but there's no expected work that is waiting on this afaik     

> __< jberman >__ End of June start date would be acceptable to me     

> __< sgp_ >__ jeffro256:monero.social: do you have time to review it now?     

> __< tevador >__ So we have time to postpone the decision until the next meeting     

> __< sgp_ >__ We can, I just won't move to finalize anything until the funds are in order     

> __< tevador >__ There would be 2 reasons to postpone: 1) the 24h notice and 2) giving jeffro256 time to review it     

> __< jeffro256 >__ The firm for 35K is one that I have never worked with directly, but I have heard goof things about them      

> __< jeffro256 >__ *good     

> __< syntheticbird >__ MINOR SPELLING MISTAKES     

> __< rucknium >__ rbrunner: How do you feel about accepting now?     

> __< rucknium >__ Not to pressure you or anything.     

> __< rbrunner >__ Let's say I don't oppose :)     

> __< sgp_ >__ let's just wait then. Ideally luigi could be ready to go after the meeting     

> __< rucknium >__ Sounds good. Thank you for arranging things.     

> __< jeffro256 >__ Yes, thanks sgp_:monero.social     

> __< rbrunner >__ +1     

> __< rucknium >__ 4. Post-quantum encryption (https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686). Jamtis (https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#appendix-c-instant-sync-protocol).     

> __< tevador >__ I have published the interactive payment protocol (IPP) and the instant sync protocol (ISP) in the Jamtis draft appendix. I'd like to discuss these today.     

> __< jberman >__ My opinion on the ISP is that I don't like the UX and am pretty eh on its inclusion in the spec as its a tacit encouragement for wallets to implement it     

> __< jberman >__ But it's a cool idea and I respect that it's 0 added cost on addresses / chain space     

> __< jeffro256 >__ Re: UX, I would assume that wallets can implement this exchange automatically. Bob and Alice wouldn't actually be copying and pasting messages 4 times      

> __< jeffro256 >__ I mean, you could if you wanted it to be airgapped ig     

> __< rbrunner >__ Hmm, isn't this the same problem as with multisig data exchanges earlier: wallets can't directly see each other?     

> __< tevador >__ Note that jberman is speaking about Appendix C, while jeffro256 is speaking about Appendix B     

> __< jberman >__ ^     

> __< jbabb:cypherstack.com >__ Jamtis-ISP > Monero-PSK     

> __< jeffro256 >__ Oh oops, sorry, yeah I was talking about IPP      

> __< tevador >__ Yes, Appendix C was added in response to the Monero-PSK proposal     

> __< tevador >__ It's the closest thing we can do with Jamtis     

> __< jberman >__ One thing to be clear about for IPP: is there a way to restore an IPP wallet from blockchain data? I was under the impression that wasn't the case, but the spec isn't perfectly clear on that     

> __< rbrunner >__ Exchanging data directly between wallets is a problem that I thought long and hard and found no easy and straightforward way     

> __< jeffro256 >__ rbrunner: Are you taking about IPP or ISP? For IPP, you wouldn't need a transport layer with long-term storage like Bitbucket since messages can fail at any point and you end up okay. Whereas the same can't necessarily be said about multisig. Also you only need 2-way comms, not N-way comms     

> __< tevador >__ jberman: the interactive payment is restorable from blockchain data (as an internal payment)     

> __< spirobel:kernal.eu >__ yes and there is another way to do it in one round. so wallets can be shared publicly and users can directly send the tx without having to wait for the other party to be online  > <jeffro256> Re: UX, I would assume that wallets can implement this exchange automatically. Bob and Alice wouldn't actually be copying and pasting messages 4 times      

> __< jeffro256 >__ *bitmessage      

> __< rbrunner >__ jeffro256: Data exchange between wallets quite in general. If if only "both online" and "only 2 way", how would they find each other?     

> __< rbrunner >__ *Even if only ...     

> __< spirobel:kernal.eu >__ i am not a fan of jamtis. and pushing it down everyones throat. but i dont want to stand in your guys way if you want to implement it     

> __< spirobel:kernal.eu >__ i personally dont want to use it because i think this pq crypto is too new and unproven     

> __< spirobel:kernal.eu >__ people can just use signal or other messaging apps and treat the addresses as secret key material     

> __< jberman >__ Aka public key sharing infrastructure? > <spirobel:kernal.eu> yes and there is another way to do it in one round. so wallets can be shared publicly and users can directly send the tx without having to wait for the other party to be online      

> __< rbrunner >__ Well, standing up to a task, actually producing something, and then proposing it, is not "pushing it down my throat" in my book     

> __< jeffro256 >__ Lots of ways. For example, if a merchant has a website that you interact with anyways, you could use a HTTP API (hopefully somewhat standardized)     

> __< tevador >__ "PQ crypto new and unproven" - that's why we have hybrid encryption, IMO that's not a real reason against Jamtis.     

> __< rbrunner >__ Exactly, let's standardize something :)     

> __< spirobel:kernal.eu >__ jeffro256: yes i am currently working on exactly this. i have a few endpoints already specified and working.      

> __< jberman >__ jeffro256: Specifically for the case of friend wants to pay a friend e.g. not a merchant payment     

> __< jberman >__ Or merchant hasn't set up a server     

> __< tevador >__ "people can just use signal" - good luck doing that with a static donation address     

> __< jpk68:matrix.org >__ I think having to use public key-sharing infrastructure is way more of a UX hurdle than, say long addresses with Jamtis     

> __< jpk68:matrix.org >__ Look at how unusable PGP is for the average person     

> __< rbrunner >__ Getting something accepted as new standard in our, well, quite chaotic ecosystem, is a bit of a challenge, me things ...     

> __< rbrunner >__ *me thinks     

> __< jberman >__ tevador: And with the scheme, as soon as you share a static address from your wallet, your wallet then has to scan the chain into perpetuity to identify receives     

> __< rucknium >__ Is anyone very familiar with BitPay? I think they have wallet-specific interaction protocols for BTC and other coins.     

> __< spirobel:kernal.eu >__ jberman: i want to add messaging functionality anyway. so there is the possibility to do it automated and standardized but the user is not forced to. they can also send the receiver a snippet / link over any other (encrypted) chat app / email      

> __< spirobel:kernal.eu >__ jpk68:matrix.org: yes its not good. so we have to do better      

> __< jberman >__ Automated = via a messaging server in the middle     

> __< jeffro256 >__ If neither of you run a server of your own (e.g. you're both on mobile), and you're okay with bouncing messages off another server, Websockets is a good option  > <jberman> Specifically for the case of friend wants to pay a friend e.g. not a merchant payment     

> __< tevador >__ jberman: my response was directed to spirobel, who thinks we don't need to support static addresses at all (see Monero-PSK)     

> __< spirobel:kernal.eu >__ no use to private payments if people communicate non encrypted or over centralized services all the time      

> __< rucknium >__ BitPay as a whole model isn't very good because they require a lot of controls. I think they did KYC of consumers for merchant txs in some jurisdictions.     

> __< jberman >__ Lol     

> __< spirobel:kernal.eu >__ rucknium: no idea never heard of them      

> __< jberman >__ spirobel argue your case why Monero should get rid of static addresses     

> __< tevador >__ Jamtis ISP is a way to get instant sync while still supporting static addresses (with the caveat that you lose instant sync if you use a static address)     

> __< rucknium >__ BitPay is big. So get familiar maybe     

> __< spirobel:kernal.eu >__ jberman: i never made this case. i am saying that there should be the option for people to have addresses that dont require syncing. and there should be the option to have static addresses where the sender notifies the receiver out of band, and the receiver then notes down the channel opening so he can recover from seed      

> __< jeffro256 >__ If you are in-person, RFC payments  > <jberman> Specifically for the case of friend wants to pay a friend e.g. not a merchant payment     

> __< spirobel:kernal.eu >__ and my case is: there is no contradiction to jamtis there you guys can do your pq stuff with 400 bytes addresses and i do my stuff     

> __< spirobel:kernal.eu >__ no need for this discussion      

> __< rucknium >__ bitjson, who does a lot of Bitcoin Cash protocol work, used to work at BitPay: https://github.com/bitjson  https://blog.bitjson.com/     

> __< tevador >__ Everyone can do their stuff, but the official software cannot support everyone's stuff.     

> __< jberman >__ spirobel:kernal.eu: So receiver has to have info saves from the channel opening in order to recover from seed = receiver can't recover instant sync from seed alone     

> __< jberman >__ Saved*     

> __< spirobel:kernal.eu >__ jberman: yes the receiver can recover from seed. both can recover from seed      

> __< jberman >__ How can the receiver recover from seed alone in that case?     

> __< tevador >__ If someone needs to post a static address somewhere, Jamtis offers better long term privacy than a legacy address.     

> __< spirobel:kernal.eu >__ by finding the channel opening the receiver noted down as i mentioned      

> __< jberman >__ How do they find it from seed alone?     

> __< rbrunner >__ So that's "from seed", but not "from seed alone"?     

> __< tevador >__ jberman: We've been asking spirobel for a draft proposal for a long time. All I've seen are hand waving arguments.     

> __< spirobel:kernal.eu >__ by noting it down in a tx. in both cases a secret that is derived from seed is embedded in a tx so it can be found later     

> __< jberman >__ I've also seen insults and poor logic     

> __< spirobel:kernal.eu >__ doesnt matter who writes it      

> __< spirobel:kernal.eu >__ i dont know what your point is just move on     

> __< spirobel:kernal.eu >__ the logic is very simple     

> __< tevador >__ The proposal needs to be written by someone who knows the solution, which only seems to be you.     

> __< jberman >__ This is an interesting idea. A scheme expanding on this and explaining how it works would be interesting to read > <spirobel:kernal.eu> by noting it down in a tx. in both cases a secret that is derived from seed is embedded in a tx so it can be found later     

> __< rbrunner >__ What speaks against a draft proposal? Things still in flux? Lack of time right now?     

> __< spirobel:kernal.eu >__ yes i will write it down and build a poc once I have more time      

> __< rucknium >__ Next agenda item is supposed to be Monero-PSK. It's being discussed now, so:     

> __< rucknium >__ 5. Monero-PSK (https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).     

> __< rucknium >__ Should we return to it when spirobel has a draft proposal?     

> __< tevador >__ If spirobel's wallet also supports static addresses, I don't think it can be done without scanning. And after restoring from a seed, you can't be sure no static address was ever used. So in the end, you end up with something very similar to Jamtis ISP.     

> __< spirobel:kernal.eu >__ yes. good idea. I am still busy with other work atm.      

> __< spirobel:kernal.eu >__  I also want to state that this is not an either or discussion vs jamtis. So there is no need to debate this like a life and death situation :D      

> __< jpk68:matrix.org >__ Unfortunately, I don't think Q-Day is going to wait with you     

> __< rucknium >__ 6. FCMP beta stressnet (https://github.com/seraphis-migration/monero/releases/).     

> __< spirobel:kernal.eu >__ jpk68:matrix.org: trust me. it will be done before the quantum puter arrives and tells us the answer is 42 :)      

> __< rucknium >__ I pushed up the stress to 6MB blocks, which is the short-term median. But in the last 24 hours the main spamming server has had an outage.     

> __< spirobel:kernal.eu >__ and it will be possible to use it in a PQ secure way      

> __< rucknium >__ I hope I didn't accidentally cause the outage, but it's too early to tell now.     

> __< jberman >__ spirobel:kernal.eu: It's ideal for the entire Monero ecosystem to have a standardized protocol for transacting. It's also beneficial to have a complete picture of protocol options before settling on an address protocol     

> __< tevador >__ There is no way to do a static PQ secure address without a PQ key exchange. Prove me wrong.     

> __< jeffro256 >__ rucknium: Thank you for doing that      

> __< spirobel:kernal.eu >__ jberman: then lets agree to disagree here. no urgency to this. and no way to force this 400 bytes addressing protocol on everyone      

> __< jpk68:matrix.org >__ It can fit in an IRC message and that     

> __< jeffro256 >__ Besides the spamming server going out, the daemons seems to be pretty stable AFAICT      

> __< tevador >__ spirobel: 400 characters*     

> __< jpk68:matrix.org >__ *that's, like, the only noticeable difference     

> __< rucknium >__ I saw some peer banning when hashpower tripled.     

> __< tevador >__ Good luck designing a shorter PQ secure address (with static address support).     

> __< jberman >__ jeffro256: Yep, this does seem to be the case to me. I'm looking into higher frequency bans, and jeffro's latest optimizing pool fetching (should help both daemons and wallets when the pool is large)     

> __< jberman >__ And vtnerd's p2p SSL is in the wings right now, we can aim to have that in next beta release     

> __< rucknium >__ 7. View-all/view-some key.     

> __< rucknium >__ This was brought up last meeting. Do we want to discuss this issue?     

> __< spirobel:kernal.eu >__ tevador: the issue with being unable to tell if an address hasnt been used doesnt exist with public / static addresses. it is not like jamtis isp as it requires only one round and the two parties dont have to be online at the same time. thats it     

> __< jbabb:cypherstack.com >__ I don't see our relevant "fraus bug"/view-all evasion CS researchers online and I think the conclusion from the last discussion, that it shouldn't be re-added to the agenda without a writeup and/or proof of concept, fair.  I agree that it requires not adhering to the CARROT spec and it isn't a CARROT-specific issue, it affects [... too long, see https://mrelay.p2pool.observer/e/sfaM4osLZVIySTVQ ]     

> __< jbabb:cypherstack.com >__ it is a way to hide things from view keys by not doing things in the way you're supposed to and think it's safe to move on until we/CS share more code     

> __< jbabb:cypherstack.com >__ the conclusion to stress was that we should not and can not claim that we have "view-all" keys that make monero safe for eg. KYC/AML compliance purposes     

> __< jeffro256 >__ I think that it's a good informational issue to be documented somewhere. I also planned for the view-all tier to be opt-in, but I can see how that would be confusing / concercing to a third-party who expects the view-all properties to hold unconditional on the viewed entity's behavior.      

> __< rucknium >__ Oh sorry I struck out the wrong agenda items that didn't have write-ups, either.     

> __< jeffro256 >__ *I always planned     

> __< jbabb:cypherstack.com >__ the new carrot view keys do not guarantee exchanges can see safely view all customer activity     

> __< rucknium >__ Lots of things last meeting didn't have write-ups     

> __< jeffro256 >__ I mentioned this to BG, but it would make a good footnote in the CARROT spec, yeah? Exactly how to break it, how to make sure the view-all properties can stays intact with further info, etc ...     

> __< jbabb:cypherstack.com >__ ... any more than the legacy view keys*.  however of course the new carrot view keys enable great UX eg for hardware wallets, so I'm excited for it, especially now that the doomerism that "all exchanges will require these new keys" is a technical non-issue (we can lie to the view key)     

> __< jbabb:cypherstack.com >__ (also you could always just hop one wallet away--much simpler)     

> __< jbabb:cypherstack.com >__ Sorry, that's all on the topic.     

> __< rucknium >__ 8.  CCS proposal: ProbeLab P2P Network Metrics Proposal (https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).     

> __< rucknium >__ I think discussion on this has concluded, but just put it here just in case.     

> __< rucknium >__ yiannisbot:matrix.org     

> __< yiannisbot:matrix.org >__ Hi everyone! 👋     

> __< rucknium >__ Just some paperwork things: You should remove the strike-through formatting and get it ready to go here: https://ccs.getmonero.org/funding-required/     

> __< rucknium >__ We know what edits were made because it's a git repo.     

> __< rucknium >__ And maybe ofrnxmr:monero.social  and plowsof:matrix.org  want to reevaluate their thumb votes on the proposal since they spoke approvingly of it most recently.     

> __< rucknium >__ rucknium: I mean you need to get the body ready to be public-facing. Potential donors see the proposal body and evaluate it.     

> __< yiannisbot:matrix.org >__ Agreed. Wanted to make it easier to spot changes, before we proceed. Will do final edits by tomorrow.     

> __< rucknium >__ Thank you.     

> __< tevador >__ spirobel: you confused Jamtis IPP and Jamtis ISP. Jamtis ISP works offline after an initial 1 round setup.     

> __< rucknium >__ yiannisbot:matrix.org: AFAIK, you can finalize the process with ofrnxmr:monero.social  and/or plowsof:matrix.org     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< jeffro256 >__ Thanks everyone      

> __< jpk68:matrix.org >__ Sorry if this sounds rude, but once something like Jamtis is no longer in use, is it possible to remove the user-facing code for it from the codebase? I guess this would apply to Carrot as well. It seems like needless attack surface if it's not in use anymore     

> __< jpk68:matrix.org >__ For example, in the wallet implementations     

> __< tevador >__ spirobel: of course the problem exists with static addresses. Addresses that have once been published may not stay published forever and you can't know who's still keeping them.     

> __< UkoeHB >__ jeffro256: the view-all tier accompanied by a thorough (well-implemented) audit is unconditional (would have to think hard on if you can make such an audit with just the view-all key, which would make that key functionally unconditional). Unviewable enotes would be isolated from viewable, making them essentially in a separate wallet.     

> __< tevador >__ "view-all" is really "view-all-within-specs"     

> __< UkoeHB >__ jpk68: in the case of moving completely to PQ? Sends to Jamtis addrs would no longer work, whether or not there is user-facing code.     

> __< jpk68:matrix.org >__ ukoehb: Yes, I understand that. I just mean that, for example, it seems there would be not much point in having carrot_core/carrot_impl if Carrot isn't being used anymore (and is somewhat unrelated to consensus rules). I might be misunderstanding something     

> __< UkoeHB >__ jpk68: everything needs to remain at least minimally supported for existing users     

> __< jpk68:matrix.org >__ So once there are no users (i.e. when we switch to full PQ), then it's unneeded?     

> __< tevador >__ It's needed to restore legacy wallets, at the very least.     

> __< jpk68:matrix.org >__ Ah, I forgot about that. Thanks.     

> __< jeffro256 >__ sech1: should we discuss including the number of txs in the block header hasing blob in v17 in next week;s meeting?     

> __< tevador >__ Do you mean excluding? AFAIK it's already included.     

> __< jeffro256 >__ Yes. Whether or not to keep including      

> __< jeffro256 >__ Not the scanning code at least if we plan to alloe people to recover their funds indefinitely  > <jpk68:matrix.org> Sorry if this sounds rude, but once something like Jamtis is no longer in use, is it possible to remove the user-facing code for it from the codebase? I guess this would apply to Carrot as well. It seems like needless attack surface if it's not in use anymore     

> __< jeffro256 >__ But we could remove code to create CARROT-FCMP++ txs, and verify tx proofs for them, which is most of the code in carrot_impl     

> __< jeffro256 >__ tevador: do you mean an opinion either way on keeping the tx count inside the block header hashing blob? I'm on the side of removal since it isn't an accurate metric     

> __< boog900 >__ jeffro256: why is it not accurate?     

> __< jeffro256 >__ With only header hashing info, it is trivially faked. It can also be "faked" (in the sense that it doesn't represent mempool processing) during consensus validation by keeping txs local to the miner private until block propgation.      

> __< jeffro256 >__ In all scenarios where you can verify that that number means anything, you do it without checking that number     

> __< jeffro256 >__ As such, when people use it as metric for monitoring block template health, they are giving themselves a false sense of security      

> __< tevador >__ I think I'm feeling neutral about that. What would be the reason for removing it? Does it cause trouble for P2Pool?     

> __< jeffro256 >__ Because it has no real use case and it takes up space in the block header hashing blob. I don't know about p2pool, but apparently it is displayed in xmrig      

> __< boog900 >__ I know this doesn't really change anything now but having the number of txs hashed makes correcting block 202612 nicer. You don't need to compare the block blob.     



# Action History
- Created by: Rucknium | 2026-06-10T15:40:27+00:00
- Closed at: 2026-06-24T14:16:13+00:00
