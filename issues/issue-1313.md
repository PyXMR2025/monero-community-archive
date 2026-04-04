---
title: Monero Research Lab Meeting - Wed 17 December 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1313
author: Rucknium
assignees: []
labels: []
created_at: '2025-12-16T23:43:33+00:00'
updated_at: '2026-01-06T21:24:43+00:00'
type: issue
status: closed
closed_at: '2026-01-06T21:24:43+00:00'
---

# Original Description

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits.](https://moneroresearch.info/293)

4. [Spy nodes](https://github.com/monero-project/meta/issues/1124).

5. Post-FCMP scaling concepts.

6. [Transaction volume scaling parameters after FCMP hard fork](https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). [Revisit FCMP++ transaction weight function](https://github.com/seraphis-migration/monero/issues/44).

7. [Proposal: Limit blocks to 32 MB, regardless of context](https://github.com/monero-project/research-lab/issues/154).

8. [FCMP alpha stressnet](https://monero.town/post/6763165).

9. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1310 

# Discussion History
## Rucknium | 2025-12-23T21:12:21+00:00
Log

> __< suhyeon:matrix.org >__ Hi, I’m one of the authors (Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits. ) — thanks for discussing our work. We computed Qubic’s hashshare using both mainchain and orphan blocks, so that description of the paper is mistakenly incorrect. I’d be happy to discuss the other points further.     

> __< rucknium >__ suhyeon:matrix.org: Hello! Do you want to stay for the meeting? It will start in about two hours (17:00 UTC).     

> __< suhyeon:matrix.org >__ Especially we're interested in missing orphan blocks you pointed out.     

> __< suhyeon:matrix.org >__ oh can you share the information about the meeting? I have no clue      

> __< rucknium >__ https://github.com/monero-project/meta/issues/1313     

> __< rucknium >__ I can add you to the beginning of the meeting agenda if you want.     

> __< suhyeon:matrix.org >__ okay that will be great then !     

> __< rucknium >__ Fantastic. Good to meet you!     

> __< suhyeon:matrix.org >__ Good to meet you too      

> __< sgp_ >__ > <suhyeon:matrix.org> Hi, I’m one of the authors (Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits. ) — thanks for discussing our work. We computed Qubic’s hashshare using both mainchain and orphan blocks, so that description of the paper is mistakenly incorrect. I’d be happy to discuss the other points further.     

> __< sgp_ >__ Welcome! Thanks for joining     

> __< datahoarder >__ > <suhyeon:matrix.org> Especially we're interested in missing orphan blocks you pointed out.     

> __< datahoarder >__ as a heads up, here's also a CSV with all identified "mined" Qubic blocks including orphans up to last week https://irc.gammaspectra.live/05eb9beefdebb016/blocks-proof.csv, in case of them being orphan the full block header is included, which contain a miner transaction that can be verified with their viewkeys. Most of the dat [... too long, see https://mrelay.p2pool.observer/e/mem1s9MKSFFLTE4y ]     

> __< suhyeon:matrix.org >__ We found the reason. At first we attributed Qubic blocks without relying on view keys and used coinbase pattern. Later, we found viewkeys are shared in Qubic's discord channel, we confirmed the identified Qubic blocks but didn't check other blocks not attributed with the pattern. Thanks for sharing the dataset. With yours, our hashshare estimate should be corrected as the below plot (red to blue).     

> __< suhyeon:matrix.org >__ https://mrelay.p2pool.observer/m/matrix.org/psnGtaHExKEFXgRjmKpmlFtt.png (image.png)     

> __< rucknium >__ Meeting time! https://github.com/monero-project/meta/issues/1313     

> __< rucknium >__ 1. Greetings     

> __< articmine >__ Hi     

> __< jberman >__ waves     

> __< vtnerd >__ Hi     

> __< datahoarder >__ Hello     

> __< ArticMine >__ hi hivia hi via IRC     

> __< suhyeon:matrix.org >__ Is this meeting happening here in chat?     

> __< ArticMine >__ yes     

> __< suhyeon:matrix.org >__ okay good     

> __< boog900 >__ hi     

> __< rucknium >__ suhyeon:matrix.org: Yes. MRL meetings are text chat only.     

> __< rucknium >__ 2. Updates. What is everyone working on?     

> __< rucknium >__ me: Using Markov Decision Process (MDP) to analyze selfish mining countermeasures. Accidentally eating all the RAM on the MRL research computing cluster.     

> __< articmine >__ I updated and uploaded the latest scaling parameters      

> __< articmine >__ Capping MS to 8 ML     

> __< suhyeon:matrix.org >__ me: testing randomzied attention test to solve verifier's dilemma in optimistic rollups     

> __< jeffro256 >__ Howdy     

> __< jberman >__ Implemented changes to tree building using the unbiased hash to point (unbiased hash to point is on the TODO list for beta), addressed all comments on outstanding PR's, we're close to releasing v1.5 for the alpha stressnet. Continuing today with tx relay v2, then may investigate a reported segfault     

> __< jeffro256 >__ Me: working on knowledge proofs integration, reviewing PRs for v1.5 release, and still coordinating with potential auditors for carrot_core      

> __< vtnerd >__ Me: speced out fcmp++ spending in lws clients.  Nothing built, just convos with berman and jeffro confirming plan. Also attempting to rebase the lws carrot patch after jeffros changes to some functions. The tests fail and I havent dug into why yet. A user reported 0conf was broken in carrot but I haven't verified. And otherwis [... too long, see https://mrelay.p2pool.observer/e/_7yettMKODRFVXpk ]     

> __< datahoarder >__ Cleaned up all recent additions due to FCMP/Carrot on my codebase to try to make it usable for any potential library users/p2pool. All carrot changes now converge as well. Working on finally making a full event log of Qubic mining events with the archived points of view of their network.     

> __< rucknium >__ 3. Lee, S., & Kim, H. (2025). Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits. (https://moneroresearch.info/293)     

> __< rucknium >__ Welcome, suhyeon:matrix.org  (Suhyeon Lee), co-author of the paper!     

> __< rucknium >__ How did you find out about this Matrix room by the way?     

> __< suhyeon:matrix.org >__ Hello Thanks for inviting me and also for discussion      

> __< suhyeon:matrix.org >__ Oh I found your discussion in X (twitter) and tried to reach out for discussion     

> __< suhyeon:matrix.org >__ I wanted to mention the description of the hashshare calculation is wrong, not the hashrate calculation itself     

> __< suhyeon:matrix.org >__ Also, wanted to know missing Qubic blocks from our dataset     

> __< suhyeon:matrix.org >__ Actually, this work was not systemized, one of side project with me and one undergraduate student (my mentee)      

> __< suhyeon:matrix.org >__ So dataset was collected after most of selfish mining     

> __< rucknium >__ suhyeon:matrix.org: I think datahoarder:monero.social  , true to name, has even more data than that.     

> __< datahoarder >__ indeed.     

> __< suhyeon:matrix.org >__ So there was some mistake and thanks to you we can improve the paper     

> __< suhyeon:matrix.org >__ Also, for that, I want to mention, at least, appreciation to you guys in paper later. If possible, cowork on the paper will be nice. :)     

> __< datahoarder >__ Hi suhyeon:matrix.org. A few notes. I mostly noted that you lacked granular data on Qubic, and mostly ran on on-chain plus tasks from dispatcher (what you call job_notify)     

> __< rucknium >__ suhyeon:matrix.org: Do you plan to publish the analysis code and make it open source?     

> __< suhyeon:matrix.org >__ datahoarder: Yes we collected such data during only very limited time.      

> __< rucknium >__ suhyeon:matrix.org: I would be open to collaboration on the paper :)     

> __< suhyeon:matrix.org >__ rucknium: Yes      

> __< datahoarder >__ I have an archive on all historical tasks from their network, with full block template. Additionally, we also have a record of all solutions of 640M or higher (a block is a high difficulty solution, usually at several G)     

> __< suhyeon:matrix.org >__ Currently, I'm very busy with my main job. After some hassle, of course, we should publish all the codes.      

> __< datahoarder >__ That gives us around 6-20 solutions for every task which allows calculating hashrate of Qubic directly from source.     

> __< suhyeon:matrix.org >__ The reason why we didn't publish the codes is now it's too much with mess     

> __< suhyeon:matrix.org >__ datahoarder: Great. How did you collect all the data?      

> __< datahoarder >__ If you go back to when your paper was posted in this room historically I posted some charts comparing what we saw hashrate wise from them, but that's captured from the live database.     

> __< datahoarder >__ We connect to their consensus network directly and gather raw packets. These are verified against public keys     

> __< datahoarder >__ Then we gather tasks from dispatcher, and solutions for each task, provided by computors and signed by them.     

> __< datahoarder >__ Each solution includes nonce values and PoW hash (for verification)     

> __< suhyeon:matrix.org >__ okay I'll check this later > <datahoarder> If you go back to when your paper was posted in this room historically I posted some charts comparing what we saw hashrate wise from them, but that's captured from the live database.     

> __< rucknium >__ Discussion starts here ^ . suhyeon:matrix.org , can you try to click on the message? > <datahoarder> > view–key–based verification can be applied only to blocks that are already definitively included in the main chain; it cannot be used for blocks that are still within an ongoing epoch or for blocks that have already become orphaned.     

> __< suhyeon:matrix.org >__ What was the major difference in conclusions of your analysis other than hashrate?      

> __< datahoarder >__ However, this dataset has not been publicly gathered/released at this moment. Nonetheless the hashrate values are mostly similar to the ones reported by Qubic     

> __< suhyeon:matrix.org >__ rucknium: Thanks it works     

> __< suhyeon:matrix.org >__ What I wondered was their selifsh mining strategy in the research     

> __< datahoarder >__ We also saw similar lack of efficiency on their selfish mining. Initially estimated to -20% losses, later they optimized to -10-8% losses     

> __< datahoarder >__ The state machine you built is generally very close to what we observed, though they changed it over time.     

> __< rucknium >__ IMHO, their aim was propaganda. To publicize their cryptocurrency.     

> __< suhyeon:matrix.org >__ I came across Qubic guys in TOKEN 2049 Singapore      

> __< suhyeon:matrix.org >__ I asked what they're doing in Qubic     

> __< suhyeon:matrix.org >__ rucknium: I agree     

> __< suhyeon:matrix.org >__ Becuase of that I know Qubic now X)     

> __< suhyeon:matrix.org >__ They said they're doing optimized selfish mining     

> __< suhyeon:matrix.org >__ So I wondered they use theoretically optimized selifsh mining based on the Markov chain analysis     

> __< datahoarder >__ Additionally, there is bias on blocks published by Qubic. Not all of them were intended to be published, some of the bias was caused by sech1 / me :)     

> __< suhyeon:matrix.org >__ So I checked if they did 'catch up' which means they're behind and try to catch the main chain height. But we didn't find any intended or systemic trials on it.      

> __< datahoarder >__ in many cases this bias just made them more profitable (it prevented their selfish mining) and your analysis covers later stages, which were not biased this way.     

> __< suhyeon:matrix.org >__ Rather, we found they made selfish mining less efficient that is analyzed in the paper     

> __< datahoarder >__ suhyeon:matrix.org: They do not. The most they do is if they are at "par" after releasing their chain they will stick to it until next block.     

> __< rucknium >__ suhyeon:matrix.org: My guess is that they released blocks manually. It was a human judgement decision usually.     

> __< datahoarder >__ It was automated in later stages. Some of the first long trials were manually released, yes     

> __< suhyeon:matrix.org >__ Can you explain it more, I didn't understand clearly > <datahoarder> Additionally, there is bias on blocks published by Qubic. Not all of them were intended to be published, some of the bias was caused by sech1 / me :)     

> __< datahoarder >__ Basically. We read their nonces and built blocks to send them to the Monero network.     

> __< suhyeon:matrix.org >__ rucknium: if it's human decision, wow. Then, how did you guess so?     

> __< datahoarder >__ This makes them look like they weren't selfish mining for a given period, but they were. This was later prevented by including undisclosed transactions in their blocks.     

> __< rucknium >__ datahoarder: datahoarder:monero.social and sech1 prevented their long private alt-chains from forming by forcing them to be public.     

> __< datahoarder >__ Initially we pushed all instantly, later kept their chains short     

> __< rucknium >__ It was some intense spy-vs-spy, cloak-and-dagger maneuvering.     

> __< suhyeon:matrix.org >__ datahoarder: That's smart. Then, they changed a strategy for that?     

> __< suhyeon:matrix.org >__ rucknium: Sounds like game theory     

> __< datahoarder >__ They added encryption. They added new encryption. They added new new encryption. They blamed pools, disabled task dispatchers, and so on.     

> __< rucknium >__ A heroic battle in the shadows 😎     

> __< datahoarder >__ Nothing worked until they added the undisclosed transactions, after it was discussed in an MRL issue :)     

> __< suhyeon:matrix.org >__ You are cool, guys     

> __< datahoarder >__ All they did was centralize their network more, anyhow. Their infrastructure back then and now is effectively just a centralized pool with central dispatcher authority that decides what to mine     

> __< datahoarder >__ The encryption algorithms they use were kept private as well. So anyone verifying solutions is unable to do so anymore.     

> __< suhyeon:matrix.org >__ I think I can't stay much longer cause it was not a plan today for me. How can we communicate later? Especially datahoarder:monero.social     

> __< datahoarder >__ The encryption is kept secret, only to be revealed via discord DMs     

> __< datahoarder >__ I'm around here and #monero-research-lounge:monero.social     

> __< suhyeon:matrix.org >__ Okay I'll talk to there later then     

> __< datahoarder >__ As of last note, besides a specific oddity during a night, the reported hashrates on their API were mostly correct to what the internal stratum was.     

> __< datahoarder >__ Any other discussion on the paper/Qubic for now if suhyeon:matrix.org has to leave?     

> __< rucknium >__ suhyeon:matrix.org: Thank you very much! It's always great to see more people researching Monero.     

> __< rucknium >__ suhyeon:matrix.org: Here is something I wrote about Qubic's disruption: https://rucknium.me/posts/monero-18-block-reorg/     

> __< suhyeon:matrix.org >__ Oh thank you so much. I'll check this too.     

> __< suhyeon:matrix.org >__ Thanks for invitation and also thanks for your information.     

> __< suhyeon:matrix.org >__ Have a good day guys     

> __< rucknium >__ 4. Spy nodes (https://github.com/monero-project/meta/issues/1124).     

> __< datahoarder >__ (if you need input in other topics from me I'll be AFK, ping if needed, doesn't seem like from agenda)     

> __< rucknium >__ It seems that the new spy nodes have been consistently connected to the network for a week: https://moneronet.info/     

> __< rucknium >__ Last meeting I suggested that we wait until this meeting to confirm the switch to the new IP address ranges and adopt/publicize the new MRL ban list     

> __< rucknium >__ The new proposed list is https://github.com/Boog900/monero-ban-list/blob/update/ban_list.txt     

> __< ravfx:xmr.mx >__ I confirm it too, when I look at one of my node firewall log, the only thing I can see are the thousands lines that start with "SPIES" on the new range!     

> __< ravfx:xmr.mx >__ I did keep the old range blocked in case     

> __< rucknium >__ How can versioning be handled? IIRC, you can add comments to specific lines in the ban list file. IIRC, jeffro256:monero.social  added that feature. Can comments be added on their own line?     

> __< jeffro256 >__ Yes      

> __< jeffro256 >__ Everything on a line on or after a pound character is ignored, then whitespace is stipped, and empty lines ignores      

> __< jeffro256 >__ *ignored      

> __< rucknium >__ And there is the DNS ban list. One could take a big step and completely replace the DNS ban list with the new MRL ban list (or as many IP addresses on the MRL ban list that fit). It seems that all the nodes on the DNS ban list have disappeared from the network.     

> __< rucknium >__ Or you could keep most of the DNS ban list unchanged and add the big /24 subnets from the new MRL ban list.     

> __< rucknium >__ jeffro256: So maybe a comment could be added to the top of the MRL list: Version 2 or something. And put in-line comments on the old and new /24 ranges, describing what happened.     

> __< rucknium >__ I just remembered that I wanted to say something at the beginning of the meeting:     

> __< rucknium >__ Next Wednesday is December 24. Personally, I won't put up an MRL agenda in the meta repo and I won't chair a meeting then. If anyone else wants to, they should feel free.     

> __< boog900 >__ We could, do we care the ban list won't then work on older daemons though?      

> __< rucknium >__ Good question. Maybe just the comment on the top. That's supported on old nodes, right?     

> __< jeffro256 >__ i dont think so     

> __< rucknium >__ Here is your PR: https://github.com/monero-project/monero/pull/9558     

> __< rucknium >__ I thought from the decision that non-inline comments were allowed before, but maybe not.     

> __< rucknium >__ the description*     

> __< rucknium >__ Is there another way to properly version the list? Or just live without proper versioning?     

> __< jeffro256 >__ Nope, they weren't a thing at all. The old parsing code reads a line in, then immediately tries to parse it as an net address     

> __< jeffro256 >__ IIRC the net address parsing code skips whitespace, but definitely no comments      

> __< rucknium >__ Any comments from anyone else about this topic? Anyone opposed to updating the MRL ban list and publicizing it?     

> __< rucknium >__ Is preland:monero.social  here?     

> __< preland >__ I'm taking a final in 6 minutes (sry)     

> __< jberman >__ I think it's ok that the ban list doesn't work on older daemons     

> __< rucknium >__ preland:monero.social: Good luck!     

> __< jeffro256 >__ Me too. If they're not updating their daemon code, they're probably not keep up-to-date with the ban list      

> __< jberman >__ The recent updates have been important, more people updating is good     

> __< rucknium >__ Do we know what happens if a ban list with comments is ingested by an old-version node? I can try it if we don't know yet.     

> __< rucknium >__ The next agenda item (Post-FCMP scaling concepts) was suggested by preland, but they are busy now. Going to next item.     

> __< rucknium >__ 6. Transaction volume scaling parameters after FCMP hard fork (https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-01.pdf). Revisit FCMP++ transaction weight function (https://github.com/seraphis-migration/monero/issues/44).     

> __< ArticMine >__ https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-03.pdf     

> __< jberman >__ Last week boog900:monero.social , tevador , and I raised explicit support for max growth of 1.2x the LTM, in addition to the sanity cap     

> __< jberman >__ boog900:monero.social mentioned this would allow for 40-47x growth within 1 year, and 2.5x every year after that     

> __< jberman >__ 40-47x year 1 growth also fits within ofrnxmr:monero.social's expected growth also shared last week: https://libera.monerologs.net/monero-research-lab/20251210#c625246     

> __< jberman >__ I do not think the sanity cap justifies a higher LTM growth rate, because as boog900:monero.social has argued, the sanity cap eventually will not matter due to its exponential growth     

> __< jberman >__ Personally I would prefer boog900:monero.social's proposed params over all proposals, and rank my order of preference:     

> __< jberman >__ 1. boog900:monero.social's proposed params, 2) sanity cap, 3) hard cap     

> __< jberman >__ I am in favor of all 3, but personally mention I'd be ok with excluding the hard cap     

> __< articmine >__ I have updated this to to cap the MS growth to 8 ML     

> __< jeffro256 >__ Rucknium: a comment line in the ban list should get printed on stdout and skipped      

> __< articmine >__ I have given my reasons for keeping the growth of ML at 2 under the sanity cap      

> __< rucknium >__ jeffro256:monero.social: Would the rest of the ban list lines be interpreted normally and successfully?     

> __< jeffro256 >__ I think so, but I haven't tested      

> __< jberman >__ rucknium:monero.social jeffro256:monero.social ofrnxmr:monero.social curious if you have thoughts on 2x LTM versus 1.2x LTM     

> __< articmine >__ We must keep in mind the sanity cap applies      

> __< articmine >__ So it is the lower of the two     

> __< jberman >__ > I do not think the sanity cap justifies a higher LTM growth rate, because as boog900:monero.social  has argued, the sanity cap eventually will not matter due to its exponential growth     

> __< jeffro256 >__ jberman: I think that max long-term growth YoY of 2.5x is enoug, personally      

> __< jeffro256 >__ growth in block size     

> __< jeffro256 >__ Which corresponds to the 1.2x LTM value, right?     

> __< jberman >__ right     

> __< jeffro256 >__ Then I am also in favor of boog's proposal      

> __< articmine >__ Yet  but this ignores the suppression of Monero for at least the last 5 years      

> __< jberman >__ non sequitor     

> __< articmine >__ I know about the lobbying behind the scenes here      

> __< articmine >__ It is not a non sequitor     

> __< jberman >__ It is, and your constant witch hunting is hostile to the Monero project     

> __< rucknium >__ IMHO 1.2x growth on the 100,000-block long-term median (LTM), which allows 2.5x growth annually after exhausting the short-term growth ceiling, would sound good to me. Stressnet is having difficulties processing the (rough) amount of txs that the short-term growth would allow.     

> __< articmine >__ rucknium: But you are ignoring the sanity cap     

> __< jberman >__ > I do not think the sanity cap justifies a higher LTM growth rate, because as  has argued, the sanity cap eventually will not matter due to its exponential growthboog900bo     

> __< jberman >__ 3rd time I've posted this message and you've consitently ignored it every time     

> __< articmine >__ boog's was without a sanity cap      

> __< jberman >__ That is not a coherent response to the message     

> __< articmine >__ What is your rationale      

> __< rucknium >__ I don't really like exponential growth in the long term, but changing the functional form would require re-analysis of the whole blocksize-fee interaction system.     

> __< rucknium >__ IMHO, fee analysis of blockchains is nontrivial.     

> __< jberman >__ Expontential growth in the long term means that it will eventually grow so large that it won't have any impact in limiting growth     

> __< articmine >__ It is the lower of the two     

> __< jeffro256 >__ IMO I think that there should be a sanity cap just to be safe on either of the proposals, which doesn't necessarily have to be exponential indefinitely      

> __< articmine >__ I agree with the sanity cap      

> __< rucknium >__ Asking for rice grains on chessboard squares.     

> __< articmine >__ What I don't understand is why lock in the harm that has by done     

> __< jberman >__ It isn't locking in harm that has been done that is a madeup argument that has no basis in reality. It's implementing rational limits that ensure the network remains healthy     

> __< jeffro256 >__ I think that the harm is a sunk cost, we can't unharm reputation / adoption / suppression by allowing big blocks. The harm is at root done at the human level. Yes, perhaps Bitcoin's p-to-p use case is bottlenecked at a technical level, but we're not there: our use case is bottlenecked at the political / adoption level      

> __< ArticMine >__ https://bitinfocharts.com/comparison/monero-transactions.html#log&alltime     

> __< articmine >__ I can't ignore the suppression and how much longer it can go on     

> __< jberman >__ Good thing 1.2x LTM allows 40-47x growth within 1 year and 2.5x per year every year after that     

> __< articmine >__ Just look at the historical transaction data for Monero      

> __< articmine >__ jberman: It does not if the suppression continues     

> __< jberman >__ Yes, it does     

> __< articmine >__ The is no chance to recover      

> __< articmine >__ Do the math for another decade of suppression      

> __< boog900 >__ You cant predict the future usage of monero      

> __< jberman >__ By your argument, a 10,000x LTM also would not allow for growth if suppression continues     

> __< articmine >__ boog900: Neither can tou     

> __< articmine >__ You     

> __< boog900 >__ I know my numbers are arbitrary just like yours      

> __< articmine >__ jberman: We can go to the ridiculous     

> __< boog900 >__ I feel they allow enough growth while being much safer than what our current algo is and what you propose      

> __< articmine >__ I have to disagree if the suppression continues      

> __< articmine >__ For like a decade      

> __< articmine >__ This is the situation where there is a real difference      

> __< jberman >__ No algo works if suppression continues indefinitely. When suppression stops, 40-47x within 1 year and 2.5x every year after that is strong allowed growth     

> __< articmine >__ Which may not be enough      

> __< articmine >__ Monero climbed 1000x in under 2 months      

> __< articmine >__ That is in the data I posted      

> __< articmine >__ Which is being ignored      

> __< jeffro256 >__ If suppression continues for another decade, the limiting factor would be the circular economy infrastructure, not block size. There's a lot of moving parts in an economy that need slow growth and can't be migrated overnight      

> __< boog900 >__ And yet scaling has pretty much never been activated      

> __< articmine >__ boog900: Which proves my point     

> __< rucknium >__ I note that on current stressnet when blocks get around 20MB, there are a lot of orphans and alt chains. Mining pools, if they are alert, may try to limit their own block sizes voluntarily, below the consensus limits, to prevent their blocks from being orphaned.     

> __< boog900 >__ It proves we would have been fine up until now with my scaling algo      

> __< articmine >__ That the market is dealing with all of these Doomsday scenarios      

> __< rucknium >__ Alt chains on stressnet, by datahoarder:monero.social  : https://stressnet.p2pool.observer/     

> __< gingeropolous >__ rucknium: the mining pools would just peer with each other or create their own rails, like bitcoin has     

> __< articmine >__ boog900: ... and with the original algo     

> __< datahoarder >__ rucknium: Not visible at the moment even on https://stressnet.p2pool.observer/fullplot.svg but I could put a fixed height if we want to have an example     

> __< jeffro256 >__ That's not a fair comparison and you know that. A new currency going from 1 user to 1000 users is not the same as going from 1000 users to 1000000 users > <articmine> Monero climbed 1000x in under 2 months      

> __< rucknium >__ And then p2pool and solo miners would have a bad time     

> __< boog900 >__ articmine: Anyone agree with article today?     

> __< boog900 >__ Artic*      

> __< datahoarder >__ p2pool also has an effective limit in how many txs can be included on the template, but it might go up in the future     

> __< articmine >__ jeffro256: It is actually the sharpest that I have seen when compared to Bitcoin etc     

> __< ofrnxmr >__ rucknium: And to more effectively orphan other blocks     

> __< ofrnxmr >__ But these are efficiency gains, not impossible issues     

> __< vtnerd >__ articmine: That many users is way more complicated for the infrastructure     

> __< vtnerd >__ Like the difficulty in engineering ramps up considerably. Every other project just punts and requires tons of ram     

> __< articmine >__ I am not suggesting 1000x in two months      

> __< jberman >__ The orphaning issue would be a good one to write up in the stressnet repo. Theoretically I'd assume orphan rates would go up with larger blocks, but I'm sure there are fixes to work through there to mitigate the observed issues     

> __< ofrnxmr >__ ofrnxmr: It shouldnt take longer to produce a big block alt chain than a small block one, if the nodes already have the txs. It currently does. I assume its reverifying txs in alt chains or smthn     

> __< articmine >__ ...  but it will take over 6 years to get to 100 MB     

> __< boog900 >__ Your ability to not listen is impressive       

> __< articmine >__ So is yours      

> __< jberman >__ ofrnxmr:monero.social gingeropolous:monero.social do either of you guys have thoughts on 1.2x LTM vs 2x LTM? Do you follow the argument over that param specifically?     

> __< jberman >__ and datahoarder:monero.social     

> __< ofrnxmr >__ W/ sanity cap. 50x stm and 1.2ltm = 31mb and 78 max in yr. Year one limited to 10mb due yo sanity cap?     

> __< ofrnxmr >__ w/o sanity cap. 16x stm and 2.0?     

> __< ofrnxmr >__ Are these whats on the table?     

> __< articmine >__ jberman: You are asking people to consider a parameter in isolation out of context     

> __< datahoarder >__ I have not followed the precise parameters as they have progressed across the past weeks, but note that attacks can be done context-less on scaling methods that just depend on height (and not actual chain state) for abusing RPC or sync     

> __< articmine >__ Look for example at the 5 months scenario      

> __< ofrnxmr >__ I think 1.2ltm w/ a 50stm + sanity cap works     

> __< ofrnxmr >__ But 16stm and 1.2 is a bit low     

> __< gingeropolous >__ you gotta count me out of this. I don't have the terms / acronyms engrained in my head like I should for this conversation for me to be effective. over the next 3 weeks im gonna try and get myself re-acquainted with this stuff.      

> __< datahoarder >__ However if we are scaling to those block sizes - the current system is not workable for miners (they will soft cap) unless transactions can pass around easier in the future.     

> __< ofrnxmr >__ ofrnxmr: (This is using a 625kb penalty free)     

> __< articmine >__ ofrnxmr: I also can agree with that. But not with a 8 stm     

> __< articmine >__ ofrnxmr: They want 8 stm and 1.2ltm     

> __< boog900 >__ ofrnxmr: That is quite aggressive IMO, allowing 100x on the current long term median in the short term     

> __< boog900 >__ My proposal is 8 stm      

> __< articmine >__ On top of an agreed to less than 1.4 x yearly cap     

> __< ofrnxmr >__ boog900: in the short term the max is 10mb .. then 15mb.. then like 20mb..     

> __< articmine >__ boog900: Your original proposal did not have a sanity cat     

> __< articmine >__ cap     

> __< boog900 >__ articmine: I have stated so much its an optional add on     

> __< boog900 >__ Its still not in my proposal as a must     

> __< articmine >__ It was way more aggressive than Bitcoin Cash      

> __< ofrnxmr >__ W/o a sanity cap, id use more restrictive values     

> __< articmine >__ My point is that with a sanity cap we can use 8stm 2ltm     

> __< boog900 >__ > Optionally we can add the moving sanity cap, however I do not think it is necessary, with an algorithm that moves at an appropriate rate.     

> __< boog900 >__ Literally in my proposal from the start      

> __< boog900 >__ Politician level of honesty      

> __< jberman >__ One thing to clarify about STM. Common to all proposals on the table, there is a separate 2x on top of the STM. I believe that's why boog says 50stm allows 100x on the current LTM in the short term     

> __< ofrnxmr >__ boog900: yeah, i disagree with this, because this just caps scaling with the assumption that the network wont improve until it has to, where with sanity cap improving it should be a first class citizen     

> __< jberman >__ that's accurate, right boog900:monero.social ?     

> __< articmine >__ boog900: ... and I am not forgettting  the next item on the agenda the Bitcoin style hard caps that my proposal make redundant     

> __< boog900 >__ ofrnxmr: The sanity cap assumes exponential growth of our capacity, let's not pretend that will perfectly track our actual capacity growth     

> __< boog900 >__ jberman: Yes     

> __< boog900 >__ articmine: Politician levels of point dodging     

> __< ofrnxmr >__ boog900: so 50stm w 625kb penaltyfree = 62mb max?     

> __< articmine >__ A 32 MB hard cap is on the agenda      

> __< boog900 >__ ofrnxmr: Yes     

> __< ofrnxmr >__ boog900: ok so 25stm     

> __< articmine >__ We are talking at this point 8 stm and 2 ltm     

> __< articmine >__ With a sanity cap      

> __< boog900 >__ ofrnxmr: IMO even 8 is too high. With an adjusted long term median of 5 MB, 50x would allow 250 MB blocks in the short term.     

> __< ofrnxmr >__ 25stm + 1.2ltm + sanity cap     

> __< ofrnxmr >__ W/o sanity cap id be on the side of restricting further, but i dont think im in that camp     

> __< articmine >__ But this is not enough for the small blockers     

> __< boog900 >__ I just don't think the sanity cap should come into discussion for the underlying algo     

> __< boog900 >__ Like it should just be an add on for both      

> __< boog900 >__  Shouldn't be relying on it for security     

> __< jberman >__ I generally agree with boog there     

> __< articmine >__ boog900: It is critical for the discussion     

> __< ofrnxmr >__ I don't want to have this argument every 3-4 years. we can use semi-fast growth scaling and adjust the sanity cap at thr next hard fork if we fuck up and havent made progress     

> __< articmine >__ Who thinks the sanity cap is not relevant here?     

> __< boog900 >__ articmine: Yes because otherwise your proposal is stupid.     

> __< boog900 >__ It depends on it for its security     

> __< articmine >__ boog900: By the same argument so is yours     

> __< jberman >__ I re-raise the point that I'm in favor of boog's proposed params without a sanity cap     

> __< boog900 >__ ofrnxmr: That's exactly what I am trying to prevent by not having an ever moving sanity cap.     

> __< ofrnxmr >__ I wouldnt be in favor of 10mb blocks being the max 5 years from now, just because 4 years from now volume was low     

> __< articmine >__ ofrnxmr: That is my t     

> __< articmine >__ point      

> __< boog900 >__ ofrnxmr: It wouldn't be the max, blocks can grow. Yes there could be some congestion, but that's the case with anything but infinite block size.     

> __< ofrnxmr >__ With fcmp, it doesnt take very many txs to fill a 10mb block     

> __< boog900 >__ Its about safe growth, nodes need time to prepare      

> __< boog900 >__ Both software and hardware     

> __< jberman >__ 8x STM, 1.2x LTM allows for 40-47x growth short term. Even with the sanity cap (which I wanted to avoid rasing here), 4 years from now it will have grown 10mb * 1.4^n (n is years from when sanity cap is in place)     

> __< jberman >__ so there's no proposal on the table that would have a cap on block size at 10mb in 4 years     

> __< rucknium >__ 7. Proposal: Limit blocks to 32 MB, regardless of context (https://github.com/monero-project/research-lab/issues/154).     

> __< articmine >__ Just a note. I am traveling back to Canada on Dec 31st so I will not be able to attend a meeting on December 31st     

> __< jberman >__ did I misunderstand something? ofrnxmr:monero.social why did you say you're against 10mb blocks in 4 years just becaues volume now is low?     

> __< jberman >__ what proposal makes you think there would be max 10mb blocks in 4 years?     

> __< ofrnxmr >__ jberman: i must not understand the math here     

> __< rucknium >__ vtnerd:monero.social has stepped forward to save the kingdom: https://github.com/monero-project/research-lab/issues/154#issuecomment-3651723232     

> __< rucknium >__ i.e. to engineer a solution to the 100MB packet limit.     

> __< jberman >__ ofrnxmr: which math were you misunderstanding?     

> __< jberman >__ or assuming     

> __< ofrnxmr >__ jberman: i understand it as     

> __< ofrnxmr >__ penalty free = 625kb, 8x = 5000kb, *2 = 10000kb     

> __< vtnerd >__ rucknium:monero.social: oh no! Yeah itll be an interesting engineering feat     

> __< jberman >__ Got it, the proposal's short term limit, that the LTM still allows to be raised with consistent high usage     

> __< articmine >__ Yes this is not necessary with the sanity median      

> __< articmine >__ So NO     

> __< articmine >__ To the 32 MB or 90 MB Bitcoin style limit      

> __< ofrnxmr >__ jberman: So were talking about 25mb in first year w/o prior volume?     

> __< articmine >__ For clarity my ABSTAIN is no longer the case      

> __< articmine >__ Sanity cap      

> __< articmine >__ Makes these hard limits un necessary      

> __< jberman >__ ofrnxmr: yes     

> __< ofrnxmr >__ Last hard for q4 2022. So about 3.5yrs since last hard fork.     

> __< ofrnxmr >__ I assume the next hard fork (after fcmp) will be less than 4yrs after. With sanity cap, we wont hit 90mb before we hard fork again     

> __< articmine >__ Not with my proposal      

> __< ofrnxmr >__ And i assume we'll have to hard fork to fix relay /p2p     

> __< articmine >__ ofrnxmr: Yes     

> __< rucknium >__ Weren't fluffy blocks introduced between hard forks?     

> __< jberman >__ boog900:monero.social thoughts on raising the STM, and potentially reducing the LTM a bit further? that would accomodate the "holiday shopping" influx     

> __< ofrnxmr >__ jberman: Yeah.. i'd probably go with artics 16x + 1.2 + sanity     

> __< ofrnxmr >__ rucknium: As optional iirc, not sure how that worked     

> __< rucknium >__ IIRC, there is a Levin flag for Fluffy blocks support. That wouldn't be needed if fluffy blocks were introduced at a hard fork.     

> __< boog900 >__ ofrnxmr: That's literally my proposal fwiw.     

> __< ofrnxmr >__ rucknium: But the issue here isnt adding new feature, thats easy, its that old nodes would break if they dont adopt it and blocks go over 90mb     

> __< boog900 >__ jberman: Ehh the stm is the thing I think is too high, I wouldn't mind raising it a little     

> __< ofrnxmr >__ So the fixes could be deployed w/o hard fork, but wouldnt prevent neteork fracture unless mandatory update     

> __< articmine >__ boog900: To clarify 16 x on MS , 1.2x on ML plus sanity ?     

> __< jberman >__ boog900: ofrnxmr:monero.social by artic's 16x, you're saying you'd be ok with allowing 32x in short term?     

> __< boog900 >__ Just because an update it technically a HF it doesn't mean we have to actually officially HF      

> __< rucknium >__ And I guess if you have a lot of old nodes on the network, it would consume resources of the new nodes since they would relay txs the old way.     

> __< ofrnxmr >__ jberman: Yeah     

> __< ofrnxmr >__ rucknium: This is also an issue with tzrelayv2, since it still have to deal with old nodes using old relay     

> __< boog900 >__ Artics original 16x was with a modified algorithm that only allowed 16x max growth      

> __< articmine >__ Who If we cap MS then the blocksize  is allowed to go to 2x MS     

> __< boog900 >__ His new one is 8 x for stm which allows 16x max growth     

> __< articmine >__ Unless of t sanity caps the blocksize      

> __< boog900 >__ So I thought for either one my one is pretty much that. I didn't realize you wanted 32 x max growth      

> __< boog900 >__ I don't see the need ngl      

> __< boog900 >__ Bitcoin cash has much less aggressive algo and they showed it could handle the combined usage of btc ETH ltc and bch iirc      

> __< ofrnxmr >__ boog900: Their txs are also 20x lower in size, so isnt their tx throughput much greater     

> __< ofrnxmr >__ smaller*     

> __< boog900 >__ Its still multiplies based on previous size though, but yes.     

> __< kayabanerve:matrix.org >__ I still support a 90 MB hard cap until the P2P, RPC protocols are upgraded.     

> __< articmine >__ That is correct. 16x on both MS and block weight > <boog900> Artics original 16x was with a modified algorithm that only allowed 16x max growth      

> __< rucknium >__ I propose that scaling discussion be skipped at the December 31 MRL meeting.     

> __< boog900 >__ I think we can declare consensus, with the people supporting my proposal last meeting and this meeting.     

> __< articmine >__ rucknium: I will not be able to attend that meeting since I am flying back to Canada from Europe that day     

> __< ofrnxmr >__ So in conclusion: what is artics proposal and boogs proposal.     

> __< boog900 >__ articmine: Yes so max size with both is than same as my proposal     

> __< articmine >__ ofrnxmr: My latest is 8x on MS 16x on the block weight 2 x on ML plus sanity cap     

> __< boog900 >__ https://github.com/seraphis-migration/monero/issues/44#issuecomment-3617687600     

> __< boog900 >__ The last bit of that comment is my proposal     

> __< articmine >__ Just plug give us the critical numbers      

> __< ArticMine >__ https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025-12-03.pdf     

> __< boog900 >__ articmine: 8 MS, 1.2 ML, optional sanity     

> __< articmine >__ What about the block weight!     

> __< articmine >__ 8 Or 16?     

> __< boog900 >__ I didn't change the algorithm to try and get faster growth.      

> __< boog900 >__ So 16x      

> __< articmine >__ So we are both in agreement on MS and the block weight      

> __< boog900 >__ Yes, the part of my proposal that had the most contention today, we agree on.      

> __< articmine >__ This come then down to 2x on ML with mandatory sanity vs 1.2x on ML with optional sanity?     

> __< jberman >__ I'm in favor of boog900:monero.social's proposal regardless of the sanity cap     

> __< articmine >__ Let us be clear on what is on the table      

> __< boog900 >__ 1.2 has had overwhelming support      

> __< jberman >__ I would reluctantly be ok with 2x'ing the MS (to allow for 32x growth) and keeping 1.2 ML     

> __< jberman >__ And I am in favor of the sanity cap regardless     

> __< ofrnxmr >__ Alright so sounds like we're close     

> __< articmine >__ I have to oppose 1.2 on ML with sanity      

> __< boog900 >__ You would be OK without sanity?      

> __< articmine >__ No because the proposed hard caps at 90 MB and 32  MB     

> __< articmine >__ I have to insist on sanity      

> __< jberman >__ I would be ok with boog's proposed without a sanity cap and without a hard cap     

> __< jberman >__ 2-3 years of consistently maxxed out usage to trip the 100mb limit     

> __< articmine >__ jberman: I can support that     

> __< boog900 >__ Sounds good to me.      

> __< jberman >__ 2-3 years seems manageable, albeit it is a marginally uncomfortable position to be in for something to need to potentially be "managed"     

> __< boog900 >__ better than the current situation at least      

> __< jberman >__ boog900: yep     

> __< articmine >__ So there we have it      

> __< articmine >__ 8x on MS 16x on block weight 1.2 on ML no sanity no hard caps     

> __< articmine >__ Do we have consensus?     

> __< jberman >__ +1     

> __< boog900 >__ I agree to that.      

> __< ofrnxmr >__ deal     

> __< rucknium >__ +1     

> __< rucknium >__ More people want to chime in?     

> __< ofrnxmr >__ rucknium: twitter's never going to let us live this down     

> __< jeffro256 >__ +     

> __< ofrnxmr >__ This will incidentally fix (hide) the xmrig issue for large templates (since there wont be any blocks with 2800txs in them)     

> __< rucknium >__ Twitter is a constant reminder that the medium is the message.     

> __< spackle >__ +1     

> __< ofrnxmr >__ (for a while anyway)     

> __< rucknium >__ It looks like there is consensus at this meeting for "8x on MS 16x on block weight 1.2 on ML no sanity no hard caps"     

> __< articmine >__ I will proceed to update the document accordingly      

> __< rucknium >__ articmine:monero.social: Thank you     

> __< rucknium >__ 8.  FCMP alpha stressnet (https://monero.town/post/6763165).     

> __< jeffro256 >__ v1.5 is coming out soon, be on the lookout for that      

> __< ofrnxmr >__ Not many fcmp issues being encountered. Mostly monerod issues     

> __< jberman >__ anything new? AFAIK, main items now are the "not relayed" state, segfault, and higher orphan rates?     

> __< rucknium >__ We can end the meeting here. Thanks everyone.     

> __< ofrnxmr >__ Cheers     

> __< jeffro256 >__ Thanks everyone     

> __< ofrnxmr >__ jberman: Not relayed = absent on current spam so maybe can ignore that for now     

> __< ofrnxmr >__ Higher orphan rates also seem to be related to very slow notifications of new blocks when blocks are big. When i mine a block on node A (add-priority-node=nodeb) nodeb doesnt see that theres a new block for sometimes 5-10 seconds     

> __< jberman >__ I'm guessing node B probably doesn't have all the block's txs and has to do rounds to get them all     

> __< jberman >__ but maybe there are some lingering connection issues to still deal with / correct     

> __< jberman >__ in any case ya it shouldn't take 5-10s to do all those rounds. logs will help explain that one     

> __< rucknium >__ Maybe could have something to do with the 600MB default txpool size. "Actual" txpool is size is 1GB. Next stressnet, default txpool size should probably be raised.     

> __< jberman >__ yes, if missing txs, it'll still verify any new ones which can take ~5s b/c of 128-in's. and then it does a round to get its missing ones which can take another ~5s to verify again     

> __< ofrnxmr >__ Both of the pools are pretty similar, i assume they have most of the same txs, especially for the first block mined     

> __< ofrnxmr >__ I add like 100mb to the pool of high fee txs before mining, so the first block should have the oldest of those in it     

> __< ofrnxmr >__ And there are (afaik) no 128in txs     

> __< ofrnxmr >__ Not from me, anyway     

> __< ofrnxmr >__ All of mine are 1 or 2 in, and 2 or 16 out     

> __< rucknium >__ When the txpool hits the limit, does it refuse new txs or kick out old ones?     

> __< jberman >__ if a tx pays a fee higher than any alreayd in the pool, it'll replace the lowest paying tx(s)     

> __< jberman >__ otherwise it won't accept the new ones     

> __< rucknium >__ That could cause problems here because my spammer is paying low fees and ofrnxmr:monero.social  is paying high fees.     

> __< jberman >__ jberman: fwiw there is a TODO to address this here: https://github.com/monero-project/monero/blob/48ad374b0d6d6e045128729534dc2508e6999afe/src/cryptonote_core/blockchain.cpp#L4236-L4240     

> __< jberman >__ rucknium: v1.5 will also include improvements to the node's behavior when this is happening     

> __< jberman >__ and v1.4 is actually broken when that's happening     

> __< jberman >__ https://github.com/seraphis-migration/monero/issues/244#issuecomment-3609352393     

> __< articmine >__ Thanks      

> __< articmine >__ I have added the updated scaling documents as discussed      

> __< articmine >__ https://github.com/ArticMine/Monero-Documents/blob/master/MoneroScaling2025Final.pdf     

> __< boog900 >__ articmine: why change the definition of Ms?     

> __< articmine >__ The bound to ML was performed on MN before     

> __< articmine >__ On the next step      

> __< articmine >__ So technically MS was not bound to ML . It was the actual penalty median MN     

> __< articmine >__ It is simpler and in line with what was discussed but functionally equivalent      

> __< articmine >__ I believe that this was changed at the last fork, but I may be wrong      

> __< articmine >__ Yes it was defined in two steps before. So yes we should have been arguing over MN rather than MB      

> __< articmine >__ MS*     

> __< articmine >__ Since we argued over MS then changing the definition of MS to follow everyone's understanding of what MS means makes sense      

> __< boog900 >__ in the code we get the median of the last 100 blocks weight for Ms, but for Mn we then do min(max(Ml, Ms), 50 * Ml). From the doc it would seem Ms should be a median of max(Mb, Ml) for the Ml at block Mb.     

> __< articmine >__ So the simplest way then is to change 50 to 8 in the code and then change the definitions of both MS and MN to reflect the code?     

> __< articmine >__ That actually makes more sense to me.      

> __< boog900 >__ yeah I agree      

> __< articmine >__ Then I will make the changes in document to avoid any confusion      

> __< articmine >__ The other median should be straight forward. Just change 1.7 to 1.2     

> __< articmine >__ ML     


# Action History
- Created by: Rucknium | 2025-12-16T23:43:33+00:00
- Closed at: 2026-01-06T21:24:43+00:00
