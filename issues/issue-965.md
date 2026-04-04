---
title: Monero Research Lab Meeting - Wed 07 February 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/965
author: Rucknium
assignees: []
labels: []
created_at: '2024-02-07T16:58:24+00:00'
updated_at: '2024-02-15T21:13:34+00:00'
type: issue
status: closed
closed_at: '2024-02-15T21:13:34+00:00'
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

#963 

# Discussion History
## Rucknium | 2024-02-15T21:13:34+00:00
Log

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/965     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< j​effro256:monero.social >__ Howdy     

> __< vtnerd >__ hi     

> __< rbrunner >__ Hello     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< vtnerd >__ I'm investigating whether ssl trust-on-first-use for wallet2/simplewallet can be added without destroying the codebase     

> __< vtnerd >__ the goal is to have a user interactive warning if a daemon ssl cert changes     

> __< j​effro256:monero.social >__ Getting back to seraphis development after writing the pool handling PR     

> __< r​ucknium:monero.social >__ me: Got the list of possible nonstandard txs from isthmus 🙏 , based on custom unlock time and possible cached ring members. I will combine that list with my own list based on nonstandard fees and Mordinal minting/transfers. There is another statistical step after these initial filters to identify the wallet2 rings by their distribution.     

> __< h​into.janaiyo:matrix.org >__ working on cuprate's db thread/actor system     

> __< r​ucknium:monero.social >__ 3. Discussion. What do we want to discuss?     

> __< j​effro256:monero.social >__ I wanted to revisit issue https://github.com/monero-project/research-lab/issues/78 and seriously  discuss removing the unlock time from future transactions     

> __< r​ucknium:monero.social >__ hinto: When you are finished with cuprate's database, do you think it would be possible to directly read its contents without monerod? OK if not.     

> __< r​ucknium:monero.social >__ I am in favor of prohibiting new txs with custom unlock time in the next network upgrade.     

> __< j​effro256:monero.social >__ Regarding the unlock time, I went ahead and wrote a PR which would ban nonzero unlock times in the mempool : https://github.com/monero-project/monero/pull/9151     

> __< h​into.janaiyo:matrix.org >__ do you mean without `cuprated`? Cuprate's db and `monerod`'s db won't be compatible, but i'm sure we could make a separate tool that can work with `cuprated`'s db     

> __< j​effro256:monero.social >__ What DB format will cuprate use ?     

> __< r​ucknium:monero.social >__ Yes, that's what I meant. Without `cuprated`.     

> __< r​ucknium:monero.social >__ Don't change your design plans at all if it would not be possible with your intended path. Just wondering.     

> __< h​into.janaiyo:matrix.org >__ in terms of format, it is just a regular `.mdb` file, it's just the schema/tables & byte encodings that will differ than `monerod`'s db     

> __< h​into.janaiyo:matrix.org >__ and the other database backend we have planned doesn't use LMDB at all, i guess it is its own format     

> __< j​effro256:monero.social >__ You have two different DB backends planned ?     

> __< h​into.janaiyo:matrix.org >__ yes, one is basically a shim around LMDB, the other is an original rust db     

> __< r​ucknium:monero.social >__ AFAIK, if I try to read monerod's database, I would get serialized C++ objects that only make sense to monerod. With cuprate would I get serialized Rust objects that only make sense to cuprated? It is ok if the answer is "yes".     

> __< j​effro256:monero.social >__ Its even more specific than that, it's objects that only make sense to monerod on systems with the same ABI     

> __< j​effro256:monero.social >__ but damn is it fast     

> __< hyc >__ there's nothing C++-specific about the objects     

> __< hyc >__ there are a bunch of 64bit and 256bit hashes     

> __< h​into.janaiyo:matrix.org >__ i'm not sure about the more complex objects/types, but a lot of the things stored are language agnostic bytes     

> __< 0​xfffc:matrix.org >__ I thought we are saving the hashes, not the objects too.     

> __< j​effro256:monero.social >__ Well you also know how your system packs the structs     

> __< j​effro256:monero.social >__ IIRC most structs use the default compiler packing and not something like pragma pack 1     

> __< rbrunner >__ Er ... I think the members get written one by one, each one after the other, never some struct as a whole     

> __< rbrunner >__ I.e. 1 call for every value     

> __< 0​xfffc:matrix.org >__ If we store serialized objects, I think there will be some C++/compiler specific stuff that will be saved. But my points was I thought we are only saving the members     

> __< h​into.janaiyo:matrix.org >__ yes rust structs are undefined, you can specify manual layout but i don't think any of our/monero-serai's type do that (yet)     

> __< r​ucknium:monero.social >__ I'm basing my (maybe incorrect) knowledge of the database's contents on this answer: https://monero.stackexchange.com/questions/10919/understanding-the-structure-of-moneros-lmdb-and-how-explore-its-contents-using     

> __< 0​xfffc:matrix.org >__ https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L2530      

> __< 0​xfffc:matrix.org >__ Lets look at the code to make sure.     

> __< rbrunner >__ I am quite sure that any compiler packing questions don't play any role because we simply don't write out structs     

> __< j​effro256:monero.social >__ rbrunner7: this isn't always the case. Some structs are sent in their entirety to the DB in their arbitrary layout: https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L835     

> __< 0​xfffc:matrix.org >__ https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L814     

> __< j​effro256:monero.social >__ Jinx     

> __< hyc >__ how is any of this detail important?     

> __< rbrunner >__ Ah, ok, that's one level deeper than I was thinking     

> __< r​ucknium:monero.social >__ Ok, maybe this detail isn't important. We can move on to discussing jeffro256 's topic on prohibiting new txs with custom unlock time     

> __< rbrunner >__ If I remember correctly unlock time is still with us and not long gone solely because we just could not get our act together and afterwards find somebody coding their end     

> __< rbrunner >__ "loose consensus" failed to materialize for once, and then the subject was dropped ...     

> __< j​effro256:monero.social >__ It's not super important but it does make it slightly easier to write debugging tools, especially in languages that aren't c++     

> __< r​ucknium:monero.social >__ rbrunner: Can you remember why loose consensus was not reached? Does anyone here support keeping it the way it is, even a little?     

> __< j​effro256:monero.social >__ Im very much of the opinion to move forwards and ban nonzero unlock times obviously which is why I alreafy wrote the code     

> __< rbrunner >__ Not sure, I don't remember it to that detail. Maybe also mixed in was sheer lack of enthusiasm, lack of somebody who took the lead     

> __< r​ucknium:monero.social >__ I don't really think it should be banned by tx relay rules before a network upgrade.     

> __< j​effro256:monero.social >__ It comes up frequently that we have to engineer really tricky edge handling logic when we take into account unlock times, most recently with working with the new seraphis enote store     

> __< rbrunner >__ If we have now somebody with jeffro256 we hopefully can get rid of that     

> __< j​effro256:monero.social >__ Why not banned by relay rule ?     

> __< hyc >__ jeffro256 the structs being written are just collections of 64bit and 256 bit values. no packing required, no padding present. https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/blockchain_db/lmdb/db_lmdb.cpp#L283     

> __< rbrunner >__ I am pretty sure there is a high number of people out there processing Monero transactions that would get cought with their pants down if you send them a locked tx     

> __< r​ucknium:monero.social >__ Maybe the biggest thing to work on is making sure users can have their say on banning new custom unlock time.     

> __< r​ucknium:monero.social >__ Ban by relay rule is best for when there is a widespread active problem     

> __< rbrunner >__ There were some long Reddit threads with some user opinions     

> __< r​ucknium:monero.social >__ Like Mordinals     

> __< r​ucknium:monero.social >__ Ban by relay rule might not be successful.     

> __< rbrunner >__ I think somebody could achieve a "widespread active problem" if they spammed Monero processing entities left and right with tiny amount locked txs.     

> __< rbrunner >__ Don't want to give anybody ideas, just saying maybe we just kill it, and get over it, and live happily ever after.     

> __< r​ucknium:monero.social >__ Ok. But make sure there is rough consensus in the userbase first.     

> __< rbrunner >__ I am with you here, but that's easier said than done :)     

> __< rbrunner >__ First problem is, if I remember Reddit discussions, to get "pure users" to understand the problem and the "feature" properly.     

> __< r​ucknium:monero.social >__ IMHO, it is acceptable to filter out opinions that are based on complete wrong understanding of the feature.     

> __< rbrunner >__ A quick search on Reddit gave me this: https://old.reddit.com/r/Monero/comments/mwrm6g/how_to_lock_send_future_monero_to_yourself_with/     

> __< rbrunner >__ Or this warning from MajesticBank: https://old.reddit.com/r/Monero/comments/z51c19/warning_incoming_payments_can_confirmed_but/     

> __< j​effro256:monero.social >__ Basically everything, including that first post, that uses unlock_time for something can be done with a time lock puzzle     

> __< r​ucknium:monero.social >__ AFAIK, not checking unlock time has been a security problem for multiple payment processors.     

> __< j​effro256:monero.social >__ ^^^     

> __< rbrunner >__ Yeah, but it's a fact of life that sometimes you get illogical if it's question to let go of something that you currency possess. Like this feature.     

> __< rbrunner >__ *currently possess     

> __< rbrunner >__ Yes, that's what I meant, I doubt that everybody is already "prepared". Not by a long shot.     

> __< rbrunner >__ I could try to write a post on Reddit and fish for fresh opinions, and also giving enough background info to make the whole story understandable for "non-techies".     

> __< h​into.janaiyo:matrix.org >__ does this mean users would have to compute the solution to their own transactions if done this way?     

> __< r​ucknium:monero.social >__ rbrunner: IMHO, that would be wonderful 👍️     

> __< rbrunner >__ Ok, maybe until Sunday.     

> __< j​effro256:monero.social >__ @hinto: yes     

> __< r​ucknium:monero.social >__ I will put it on next MRL agenda in the GitHub issue so there is "official" notice posted.     

> __< r​ucknium:monero.social >__ I have read of time lock puzzles. I didn't understand how CPU power would not affect time to unlock.     

> __< r​ucknium:monero.social >__ For example, I think some Monero payment channel ideas are based on time lock puzzles.     

> __< j​effro256:monero.social >__ CPU power does affect time to unlock     

> __< j​effro256:monero.social >__ I havent read those channel ideas, but would the network verify solutions to the timelock puzzles and give access to coins based on that?     

> __< r​ucknium:monero.social >__ I don't know. I don't like payment channels much, so I put them in moneroresearch.info and moved on.     

> __< r​ucknium:monero.social >__ Which apparently plowsof and I need to renew the SSL cert of     

> __< r​ucknium:monero.social >__ Two days late     

> __< rbrunner >__ Lol     

> __< rbrunner >__ Happens to the very best webmasters     

> __< h​into.janaiyo:matrix.org >__ Rucknium: https://certbot.eff.org     

> __< r​ucknium:monero.social >__ I couldn't get certbot to work with my domain provider     

> __< h​into.janaiyo:matrix.org >__ sounds like you need a new provider     

> __< r​ucknium:monero.social >__ I think the paper was this one: https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=123 Thyagarajan, S. A., Malavolta, G., Schmid, F., & Schröder, D. 2022, Verifiable timed linkable ring signatures for scalable payments for Monero.     

> __< plowsof >__ Oops     

> __< r​ucknium:monero.social >__ Sounds like plowsof needs to set up auto reminders :P     

> __< plowsof >__ Am i allowed to use the fluffy excuse of reminders going into my spam folder :(     

> __< r​ucknium:monero.social >__ Anything more to discuss?     

> __< j​effro256:monero.social >__ How's bp++ reviews coming along ?     

> __< r​ucknium:monero.social >__ Diego Salazar: Sorry to bother. Any comments on the state of BP++ review?     

> __< r​ucknium:monero.social >__ We can end the meeting here.     

> __< k​4r4b3y:karapara.net >__ Afaik caddyserver renews the certs for you automatically. Just throwing its name out there...     

> __< d​iego:cypherstack.com >__ 80 hours into the review     

> __< r​ucknium:monero.social >__ Diego Salazar: Thanks. IIRC, the CCS proposal did not have a specific number of hours. How many hours do the funds cover?     

> __< 1​23bob123:matrix.org >__ Most do if you have certbot     

> __< r​ucknium:monero.social >__ If the result after the funds are exhausted is "the soundness could not be verified or disproven", then that is a legitimate conclusion, too.     

> __< 1​23bob123:matrix.org >__ Nginx,apache,nginx manager     

> __< d​iego:cypherstack.com >__ We're roughly at the halfway point.     

> __< d​iego:cypherstack.com >__ And we'll complete it until it's done.     

> __< d​iego:cypherstack.com >__ Lol. Bad phrasing. We'll keep working until it's done.     

> __< plowsof >__ Phew     

> __< d​iego:cypherstack.com >__ If I can give a bit of a spoiler,  my personal opinion is not high of bp++     

> __< r​ucknium:monero.social >__ (I knew it)     

> __< r​ucknium:monero.social >__ I assume you will follow any vulnerability response procedures. I want to make sure anything MRL is involved in follows good vulnerability procedures. I don't know if Blockstream is using it on mainnet yet. Or anyone else.     

> __< r​ucknium:monero.social >__ any procedures _if needed_     

> __< c​haserene:matrix.org >__ it's not ideal, but it is the best temporary fix until a network upgrade enforces it on the consensus level, isn't it? anyone with the previous relay rules may relay it and even get it mined, but the chances of those happening will be reduced, which seems to be a net advantage.     

> __< d​iego:cypherstack.com >__ always     

# Action History
- Created by: Rucknium | 2024-02-07T16:58:24+00:00
- Closed at: 2024-02-15T21:13:34+00:00
