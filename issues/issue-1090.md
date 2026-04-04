---
title: Monero Research Lab Meeting - Wed 09 October 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1090
author: Rucknium
assignees: []
labels: []
created_at: '2024-10-09T14:59:12+00:00'
updated_at: '2024-10-17T15:55:04+00:00'
type: issue
status: closed
closed_at: '2024-10-17T15:55:04+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

5. Any other business

6. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1086 

# Discussion History
## Rucknium | 2024-10-11T15:18:25+00:00
Logs:

> __< r​ucknium:monero.social >__ MRL meeting in this channel in two hours.     

> __< j​effro256:monero.social >__ I'm attaching a document from Trail of Bit     

> __< j​effro256:monero.social >__ It's from their Statement of Work and describes who would work on the Carrot audit     

> __< j​effro256:monero.social >__ Those on IRC, if you want a copy, email me at jeffro256⊙tc     

> __< j​effro256:monero.social >__ https://matrix.monero.social/_matrix/media/v1/download/monero.social/wJNcQpFYWVQwITphJvOSQhEo     

> __< geonic >__ link works on irc too     

> __< j​effro256:monero.social >__ Ok, sweet. TIL     

> __< r​ottenwheel:kernal.eu >__ Nice jeffro256!     

> __< s​yntheticbird:monero.social >__ So, do we expect an Audit arena once again in this meeting? (Will all auditors from last meeting be present?)     

> __< j​effro256:monero.social >__ Nope     

> __< j​effro256:monero.social >__ Well, I guess I can't stop them from being present ;). But they weren't explicitly invited to this meeting     

> __< s​yntheticbird:monero.social >__ ack     

> __< r​euben:firo.org >__ Jim Miller worked on our earlier Lelantus audit     

> __< j​effro256:monero.social >__ How did that go?     

> __< r​euben:firo.org >__ While I think they did a good job, they did miss a fiat-shamir thing (which was exploited) which lead to his article :)     

> __< j​effro256:monero.social >__ Was it the Bulletproof Fiat-Shamir issue?     

> __< r​euben:firo.org >__ I got feedback from others to say it should have been caught     

> __< r​euben:firo.org >__ I think so I'm not technical so yeah but thought it was worth pointing out     

> __< k​ayabanerve:matrix.org >__ FCMP++s mirrors Orchard and kills it accordingly.     

> __< r​euben:firo.org >__ https://github.com/trailofbits/publications/blob/master/reviews/zcoin-lelantus-summary.pdf     

> __< k​ayabanerve:matrix.org >__ Proofs are an opaque byte buffer. Any item read is automatically transcripted. You can't have a proof element not transcripted accordingly.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1090     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ Reuben: Thanks for the info!     

> __< j​effro256:monero.social >__ Yes, thanks for the input, Reuben     

> __< o​ne-horse-wagon:monero.social >__ Hello.     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< v​tnerd:monero.social >__ Hi     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< v​tnerd:monero.social >__ Nearing completion on a separate span update patch in monerod, and testing the LWS to boost::beast conversion     

> __< k​ayabanerve:matrix.org >__ Discussed next step of divisors is moving forward. I'm still working on tidying FCMP++ for the next steps of integration.     

> __< r​ucknium:monero.social >__ me: Finished Dulmage-Mendelsohn decomposition analysis of the suspected black marble attack. The DM decomposition increased the number of rings with effective ring size zero from 0.57 percent to 0.82 percent (an increase of 44 percent). Also finished analysis of tx fluff phase log data. Will post the write-up after the meeting.     

> __< j​effro256:monero.social >__ me: Carrot balance recovery integration, still. I'm trying to tie it into jberman's async scanning framework as well     

> __< j​berman:monero.social >__ *waves*, continuing work on wallet syncing the tree for fcmp++ with minimal data stored, so full wallets can construct fcmp++ referencing updated owned output paths in the tree     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod. https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ The current streessnet is scheduled to be deprecated in two days (unless someone makes a compelling argument to not deprecate it). I think we will set up a new stressnet when FCMP++ is testnet-ready.     

> __< r​ucknium:monero.social >__ Deprecation = I'll stop sending spam and shut down a few of my nodes     

> __< j​effro256:monero.social >__ Rucknium rules the stressnet with an iron fist     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://www.getmonero.org/2024/04/27/fcmps.html https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< j​effro256:monero.social >__ It would be nice to make a decision today for Carrot auditing so we can set up the CCS / MAGIC, etc and get the ball rolling     

> __< j​effro256:monero.social >__ I have an opinion, but I'll save it until after others get their chance to chime in     

> __< r​ucknium:monero.social >__ Here is my rank (1 being most preferred). 1 Cypherstack. 2 Quarkslab. 3 Veridise. 4 Trail of Bits. 5 Zellic. I post this to be provocative so that others who are more knowledgeable tell me why I am wrong.     

> __< s​yntheticbird:monero.social >__ Yeah that was pretty obvious with Zellic being last.     

> __< r​ucknium:monero.social >__ I looked at the example reviews/audits that some of the firms provided. I looked for the level of cryptographic review and how similar the work was to what Carrot requires.     

> __< rbrunner >__ That's interesting. I found that Zellic company and their people quite interesting, and would find it interesting having them work for us. Why definitely last, for all things?     

> __< rbrunner >__ Working in very different areas?     

> __< r​ucknium:monero.social >__ Trail of Bits did a Stealth Address review, but the team that did that review is not the same as who would work on Carrot.     

> __< rbrunner >__ Beside finding Zellic, I only have an opinion about 1 other company: Cypherstack, because known quantity, track record and "closeness" to our ecosystem     

> __< rbrunner >__ *Beside finding Zellic interesting     

> __< r​ucknium:monero.social >__ The examples that Zellic gave analyzed code more than the cryptography and were basically smart contract audits AFAIK.     

> __< rbrunner >__ Alright, I did not look that closely.     

> __< rbrunner >__ Maybe code reviews would be more appropriate giving to them, later on?     

> __< r​ucknium:monero.social >__ I like that Quarkslab analyzed BP+ and found at least one issue in its mathematical proof. On Veridise, maybe it's unfair, but their divisor proof we commissioned them for was not tight enough, so that lowers their rating IMHO.     

> __< r​ucknium:monero.social >__ kayabanerve: Do you plan to give an opinion on Carrot reviews? I would like to hear from more cryptographers on this.     

> __< k​ayabanerve:matrix.org >__ I'd endorse CS personally. They're the best priced on a reasonable timeline and completely trusted.     

> __< s​yntheticbird:monero.social >__ Not a cryptographer, but I've heard of Zellic (and perfect blue team) reputation before even joining the Monero community. I think they may be the most inclined to *think out of the box*. But again, not a cryptographer and no data to back it.     

> __< r​ucknium:monero.social >__ jeffro256: Can you share your opinion?     

> __< k​ayabanerve:matrix.org >__ The only reason not to go with CS is a limited availability argument or we want to build relationships with other groups *at cost* IMO     

> __< j​effro256:monero.social >__ Not to be a copycat, but my ranking was very similar to Rucknium's: 1. Cypherstack 2. QuarksLabs 3. Veridise, and then a tie between Trail of Bits and Zellic. Cypherstack was the most affordable and would have Surae, a coauthor of CLSAG overseeing the audit. That means that they would be able to being over their knowledge of RingCT composition to apply in many ways to FCMP++ compo<clipped messag     

> __< j​effro256:monero.social >__ sition. QuarksLabs is also a great candidate because they are very familiar with Pederson commitment related cryptography and rerandomization, making their previous knowledge applicable to FCMP++ composition. As for Trail of Bits, they were on the higher end of price, but tend to produce decent results consistently. Zellic was somewhat of a wild card, as their main focus AFAICT ha<clipped messag     

> __< j​effro256:monero.social >__ s mainly been smart contract code, but they seem exceedingly capable at finding High and Critical level vulnerabilities, if their published track record is to be believed. They are also the only firm who hasn't worked with Monero yet, AFAIK. As was mentioned earlier, they might be a better candidate for the reviewing a concrete implementation.     

> __< j​effro256:monero.social >__ If Cypherstack can confirm that the turnaround time would be <= 6 weeks, then that would be on par with the rest, and I would recommend that we go with them     

> __< r​ucknium:monero.social >__ Diego Salazar: Question for you ^     

> __< d​iego:cypherstack.com >__ ye     

> __< d​iego:cypherstack.com >__ damn I really need to raise my prices     

> __< d​iego:cypherstack.com >__ yes turnaround time will be 6 weeks or less     

> __< r​ucknium:monero.social >__ I think we are close to loose consensus in favor of contracting Cypher Stack to perform the Carrot review.     

> __< rbrunner >__ Yeah, still waiting for a dissenting voice :)     

> __< k​ayabanerve:matrix.org >__ I also vote we no longer publicize prices so CS cannot learn how 'competitive' they are or are not /s     

> __< d​iego:cypherstack.com >__ As a bonus I can have one of my illustrators draw Monero Chan holding a carrot     

> __< r​ucknium:monero.social >__ Does anyone want to suggest another plan of action?     

> __< d​iego:cypherstack.com >__ I say this every time but never do for you guys at MRL. Just love you guys too much.     

> __< s​yntheticbird:monero.social >__ Diego. The community answered yes to your illustration proposal.     

> __< r​ottenwheel:kernal.eu >__ Please do not. 😅     

> __< r​ucknium:monero.social >__ I see loose consensus in favor of contracting Cypher Stack to perform the Carrot review. Thanks all for reviewing the reviewers and especially jeffro256  for writing the Carrot specification and working with firms to get quotes, etc.     

> __< r​ottenwheel:kernal.eu >__ 🤨👎     

> __< d​iego:cypherstack.com >__ ok, and to understand a separate CCS is being opened for this, yes?     

> __< s​yntheticbird:monero.social >__ Cypherstack theory and Zellic on code seems to be a balance plan of action.     

> __< d​iego:cypherstack.com >__ That's what I recall after the last meeting     

> __< r​ucknium:monero.social >__ Diego Salazar: Yes. AFAIK jeffro256 will handle bureaucracy from here.     

> __< d​iego:cypherstack.com >__ Sounds good.     

> __< j​effro256:monero.social >__ Yes. Carrot wasn't defined as part of the scope for kayabanerve FCMP++ CCS, so it shouldn't thrown in now IMO even though it is applicable     

> __< rbrunner >__ We had people asking on Reddit how they can donate, and I mentioned that probably soon a "Carrot" CCS will go up     

> __< r​ucknium:monero.social >__ Do we have more items to discuss on FCMP? Or any other agenda items?     

> __< o​ne-horse-wagon:monero.social >__ Rucknium:     

> __< k​ayabanerve:matrix.org >__ 1) It isn't in-scope     

> __< k​ayabanerve:matrix.org >__ 2) I wasn't involved with quote solicitation     

> __< k​ayabanerve:matrix.org >__ 3) Adding extraneous scopes risks budget exhaustion     

> __< k​ayabanerve:matrix.org >__ 4) carrot is great yet extraneous     

> __< k​ayabanerve:matrix.org >__ I have nothing beyond my already provided update.     

> __< r​ucknium:monero.social >__ I took the 10 block lock off of the agenda for now. I posted the cleaned-up version of my double-spend attack success tables on the relevant MRL issue: https://github.com/monero-project/research-lab/issues/102#issuecomment-2402750881     

> __< r​ucknium:monero.social >__ I think we can end the meeting here. Thanks everyone!     

> __< s​yntheticbird:monero.social >__ Delicious meeting. Thanks     

> __< j​effro256:monero.social >__ Thanks, everyone! Great input and feels great to make a decison finally     

> __< r​ucknium:monero.social >__ The Dulmage-Mendelsohn decomposition results and analysis of p2p tx relay logs is at https://github.com/Rucknium/misc-research/blob/main/Monero-Black-Marble-Flood/pdf/monero-black-marble-flood.pdf . The new additions are page 14, lines 183-203 and pages 19-25, lines 310-434, figures 14-16, tables 1-2.     

> __< r​ucknium:monero.social >__ The p2p tx logs analysis may be interesting to people who work with the p2p code (e.g. vtnerd and boog900 ). This was a case of making lemonade out of lemons since originally I wanted to use the logs submitted by community members (thank you!) to try to find the node origin of the spam. I changed the scope to producing a statistical profile of p2p transaction relay behavior under <clipped message     

> __< r​ucknium:monero.social >__ normal conditions.     

> __< r​ucknium:monero.social >__ Main findings: Total number of IP addresses in the p2p log data was about 13,600, which backs up the estimates of the number of nodes on the network from monero.fail/map . The average duration of a peer connection is 23 minutes, shorter than I would have expected. The probability that a node relays a transaction to two different peers at the same time is higher than what is expect<clipped message     

> __< r​ucknium:monero.social >__ ed with the theoretical distribution.     

> __< b​oog900:monero.social >__ Nice work!     

> __< b​oog900:monero.social >__ Yeah I was wrong about the amount of time between rebroadcasts here are some actual timings: https://github.com/monero-project/monero/pull/8326 which follows the data.      

> __< b​oog900:monero.social >__ I had a quick look at the code and I couldn't see anything obvious for why the time between when a txs is sent drops so low after the 7th time     

> __< b​oog900:monero.social >__ Do you know if there are still a lot of txs being sent every 2 to 4 minutes from the 2nd to 7th time, which aren't showing in the median?     

> __< b​oog900:monero.social >__ > The probability that a node relays a transaction to two different peers at the same time is higher than what is expected with the theoretical distribution     

> __< b​oog900:monero.social >__ If you have multiple Poisson-distributed independent random variables and took the smallest output out of all of them, the output would no longer be Poisson-distributed, right?     

> __< b​oog900:monero.social >__ If you had multiple connections all with a tx waiting for their Poisson-distributed timer to fire, then the distribution of the time to receive the tx would be skewed downwards due to taking the smallest value from all the timers.     

> __< b​oog900:monero.social >__ Just to be clear there I was talking about this from the last section of that paper:     

> __< b​oog900:monero.social >__ > If a node is following the protocol, we should observe two data patterns when we compute     

> __< b​oog900:monero.social >__ the difference between the arrival times of a transaction between two logging nodes. First, the differences     

> __< b​oog900:monero.social >__ should usually be in quarter second intervals. Second, the difference should follow a Skellam distribution,     

> __< b​oog900:monero.social >__ which is the distribution that describes the difference between two Poisson-distributed independent random     

> __< b​oog900:monero.social >__ variables     

> __< b​oog900:monero.social >__ If that did mean from the same origin node then ignore what I said.     

> __< r​ucknium:monero.social >__ IMHO, it's misbehaving nodes. I looked at some of the raw log data and some nodes were just re-broadcasting every 2-4 minutes. I will make some histograms to show the full distribution at each re-broadcast iteration for you.     

> __< r​ucknium:monero.social >__ Same origin node. Sorry that it wasn't clear. By chance, some of the listening nodes connected to the same node occasionally. So we could see what a node was doing on two of its connections.     

> __< r​ucknium:monero.social >__ Maybe I should make a little diagram to show clearly the situation I was talking about.     

> __< r​ucknium:monero.social >__ Do you know why connections last for about 23 minutes? Is there a timer in the code? 

> __< b​oog900:monero.social >__ ah my bad yeah that makes sense     

> __< b​oog900:monero.social >__ We do once synced, drop a single outbound peer when `on_idle` is called here: https://github.com/monero-project/monero/blob/9866a0e9021e2422d8055731a586083eb5e2be67/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L1787     

> __< b​oog900:monero.social >__ `on_idle` seems to be called every 1 to 2 minutes looking at my logs  


# Action History
- Created by: Rucknium | 2024-10-09T14:59:12+00:00
- Closed at: 2024-10-17T15:55:04+00:00
