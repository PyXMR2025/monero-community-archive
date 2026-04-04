---
title: Monero Research Lab Meeting - Wed 04 September 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1068
author: Rucknium
assignees: []
labels: []
created_at: '2024-09-03T20:43:58+00:00'
updated_at: '2024-09-17T21:24:51+00:00'
type: issue
status: closed
closed_at: '2024-09-17T21:24:51+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

5. [Change how transactions are broadcasted to significantly reduce P2P bandwidth usage](https://github.com/monero-project/monero/issues/9334).

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1063 

# Discussion History
## Rucknium | 2024-09-06T19:42:44+00:00
Logs

> __< m-relay_ >__ <r​ucknium:monero.social> Meeting time! https://github.com/monero-project/meta/issues/1068     

> __< m-relay_ >__ <r​ucknium:monero.social> 1) Greetings     

> __< m-relay_ >__ <v​tnerd:monero.social> Hi     

> __< m-relay_ >__ <o​ne-horse-wagon:monero.social> Hello.     

> __< m-relay_ >__ <b​oog900:monero.social> Hi     

> __< m-relay_ >__ <j​berman:monero.social> *waves*     

> __< rbrunner >__ Hello     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> 👋     

> __< m-relay_ >__ <r​ucknium:monero.social> 2) Updates. What is everyone working on?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> Nothing of note on my end.     

> __< m-relay_ >__ <v​tnerd:monero.social> Hackerone issues     

> __< m-relay_ >__ <j​effro256:monero.social> Hpwdy     

> __< m-relay_ >__ <r​ucknium:monero.social> me: I updated https://moneroresearch.info to use the latest version of WIKINDX. The Quick Search is improved. Instead of "OR" it now uses "AND" between words. So you get much more relevant results with multiple keyword searches. I will be on MoneroTalk at 22:30 UTC today: https://xcancel.com/MoneroTalk/status/1830994649730699491 , using a hired voice. I have been working on final <clipped mes     

> __< m-relay_ >__ <r​ucknium:monero.social> results for combining black marble attacks with the Dulmage-Mendelsohn decomposition.     

> __< m-relay_ >__ <j​effro256:monero.social> me: collecting Carrot audit proposals, hopefully should be done by next MLR meeting     

> __< m-relay_ >__ <j​berman:monero.social> continuing fcmp++, working on trimming the tree on reorg/pop blocks     

> __< m-relay_ >__ <r​ucknium:monero.social> 3) Stress testing monerod. https://github.com/monero-project/monero/issues/9348     

> __< m-relay_ >__ <r​ucknium:monero.social> I have merged 0xfffc 's PR for dynamic block size sync: https://github.com/spackle-xmr/monero/pull/30     

> __< m-relay_ >__ <r​ucknium:monero.social> I have started to spam stressnet again.     

> __< m-relay_ >__ <j​effro256:monero.social> How's it going so far?     

> __< m-relay_ >__ <r​ucknium:monero.social> plowsof wrote a bounty to enable fast sync for testnet (this would enable it on stressnet since stressnet is a testnet fork): https://bounties.monero.social/posts/149/0-450m-add-fast-blockchain-sync-to-testnet     

> __< m-relay_ >__ <r​ucknium:monero.social> Currently the bounty is at 0.45 XMR     

> __< m-relay_ >__ <0​xfffc:monero.social> Hi everyone. Apologies for being absent. Right now, I am working on an issue on stressnet side. But I will keep an eye on this chat too.      

> __< m-relay_ >__ <0​xfffc:monero.social> My work past week was mostly on finishing dynamic bss and dynamic span. (L     

> __< m-relay_ >__ <r​ucknium:monero.social> jeffro256: Initial testing of dynamic block size sync has been good. But we haven't subjected it to big blocks yet.     

> __< m-relay_ >__ <r​ucknium:monero.social> Reminder that this stressnet will stop being "supported" in about a month. So it is a good time to test your code that fixes bottlenecks.     

> __< m-relay_ >__ <r​ucknium:monero.social> 4) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< m-relay_ >__ <r​ucknium:monero.social> kayabanerve: Do you have an update on the potential Veridise followup work?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I believe we're planning to get on a call to organize within the next week or so.     

> __< m-relay_ >__ <r​ucknium:monero.social> Anything more on FCMP++?     

> __< m-relay_ >__ <j​berman:monero.social> not exactly mrl, but tobtoht proposed considering dropping windows 32-bit support since windows 11 requires 64-bit (only >18 year old CPU's running windows 10 would be affected), and the 32-bit windows build will be a bit of a pain to get working. Seems reasonable to me but worth bringing up to a wider group     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> the devs yearn for monero-dev meetings     

> __< rbrunner >__ shrug :)     

> __< m-relay_ >__ <r​ucknium:monero.social> kayabanerve: Yeah lol     

> __< m-relay_ >__ <r​ucknium:monero.social> 5) Change how transactions are broadcasted to significantly reduce P2P bandwidth usage. https://github.com/monero-project/monero/issues/9334     

> __< m-relay_ >__ <r​ucknium:monero.social> vtnerd: Do you have an opinion about changing the fluff-phase tx queue timer to exponential distribution instead of Poisson?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I see we're moving on but I'll note I support monero-dev meetings (distinct from NWLB) and have no objections to dropping first-party support from problematic archaic targets.     

> __< m-relay_ >__ <v​tnerd:monero.social> It needs to be exponential, I don't have any other comments than that really     

> __< m-relay_ >__ <j​effro256:monero.social> I'd also tentatively say I support dropping official support for 32-bit windows unless it gets brought to our attention  that more than a handful of people are actually using it     

> __< m-relay_ >__ <r​ucknium:monero.social> Maybe we are moving toward loose consensus to change it from Poisson to exponential. It could be a PR and discussed further in the PR     

> __< m-relay_ >__ <j​effro256:monero.social> I'd say we should converge on whatever the reviewed literature says , which is exponential , no?     

> __< m-relay_ >__ <v​tnerd:monero.social> There is a pr     

> __< m-relay_ >__ <r​ucknium:monero.social> The Dandelion++ paper seemed to assume that the fluff phase has exponential timers.     

> __< m-relay_ >__ <r​ucknium:monero.social> I thought the PR only affected the embargo timeout?     

> __< m-relay_ >__ <v​tnerd:monero.social> https://github.com/monero-project/monero/pull/9295     

> __< m-relay_ >__ <v​tnerd:monero.social> Oh right, I thought I changed both in that pr     

> __< m-relay_ >__ <r​ucknium:monero.social> Here's what I said about the D++ paper: https://github.com/monero-project/monero/pull/9295#issuecomment-2260998091     

> __< m-relay_ >__ <v​tnerd:monero.social> I'll just update that pr then     

> __< m-relay_ >__ <r​ucknium:monero.social> > I have been looking at whether the fluff-phase timer should also be changed from Poisson to exponential. The Dandelion++ paper doesn't explicitly say that the fluff timers should be exponential, but it strongly hints that way IMHO. Algorithm 5 "Dandelion++ Spreading at node v" in Fanti et al. (2018) ends with Diffusion(X ,v, H). The paper says "Bitcoin Core, the most popular Bit<clipped mes     

> __< m-relay_ >__ <r​ucknium:monero.social> coin implementation, adopted a protocol called diffusion, where each node spreads transactions with independent, exponential delays to its neighbors on the P2P graph." Fanti & Viswanath have an earlier paper about the privacy properties of bitcoin's transaction broadcast system. It describes diffusion: "In diffusion spreading, each source or relay node transmits the message to eac<clipped mes     

> __< m-relay_ >__ <r​ucknium:monero.social> h of its uninfected neighbors with an independent, exponential delay of rate λ. We assume a continuous-time system, in which a node starts the exponential clocks as soon as it receives (or creates) a message."     

> __< m-relay_ >__ <o​ne-horse-wagon:monero.social> It is estimated that as of 2024, only 4.3% of Windows users are running a 32 bit version and that number is shrinking every year.     

> __< m-relay_ >__ <r​ucknium:monero.social> IIRC in PR #9295, the function named "exponential" takes the floor of the drawn values, which actually creates a geometric distribution. Probably there should be a true exponential distribution and the exp-turned-geometric distribution can be named something special for use when a discrete number is needed.     

> __< m-relay_ >__ <r​ucknium:monero.social> Do we want to discuss the ten block lock now? Put it on next agenda's meeting? Neither?     

> __< m-relay_ >__ <r​ucknium:monero.social> Always a fun one     

> __< m-relay_ >__ <r​ucknium:monero.social> Aaron Feickert and isthmus wrote a report on it: https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final     

> __< m-relay_ >__ <r​ucknium:monero.social> AFAIK the new contributions are in Section 4 with the FCMP++ discussion     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I've prior stated my disagreement with the premise, and I believe there was a general agreement we needed a proper quantitative analysis of the odds of various reorg depths/natural likelihood/etc.     

> __< m-relay_ >__ <r​ucknium:monero.social> A quantitative analysis is on my CCS research agenda.     

> __< m-relay_ >__ <r​ucknium:monero.social> Do we think that block propagation will change significantly when FCMP++ is activated on mainnet?     

> __< m-relay_ >__ <b​oog900:monero.social> We use fluffy blocks, so probably not     

> __< m-relay_ >__ <r​ucknium:monero.social> Does it make sense to investigate changing it with the FCMP++ hard fork, or should we wait until we see the network behavior, then possibly change it in a future hard fork?     

> __< rbrunner >__ Did stressnet unearth any block propagation problems as blocks became bigger? I don't think so, but I am not sure     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I've called for the FCMP++ hardfork being monolithic its set of changes.     

> __< m-relay_ >__ <o​ne-horse-wagon:monero.social> There's going to be a huge change with FCMP++ and I would suggest waiting until everything is settled in before piling on more changes.     

> __< m-relay_ >__ <r​ucknium:monero.social> We figured out that some nodes rejected valid blocks since they didn't have the txs.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I want to deprecate/prune RPCs, ship Carrot, etc, because if we're already forcing users to update for XYZ, adding A isn't much more (but forcing them to change twice, six months apart, is).     

> __< m-relay_ >__ <r​ucknium:monero.social> Then the nodes marked the blocks as permanently invalid. jeffro256 made a PR to stop the permanent invalidity of the blocks     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> So if we're changing the n-block lock, I'd call for it at the hard fork.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I'll also reiterate the n-block lock should be the depth reorganizations are infeasible, not unlikely, but I've rung that bell more than enough.     

> __< m-relay_ >__ <j​effro256:monero.social> I agree with one-horse-wagon: we should discuss after smoothing out details of the FCMP upgrade. Unlike kayaba, I think it can be reduced now with FCMPs without such a permanate loss to privacy under certain circumstances which made the 10 block lock privacy impact much more relevant, but we definitely shouldnt try from the get go     

> __< rbrunner >__ The pessimist in me whispers that we will need a second hardfork to micro-adjust some things anyway that we did not yet get fully right with the original FCMP++ introduction ...     

> __< m-relay_ >__ <r​ucknium:monero.social> kayabanerve: The only way to do that is a rolling checkpoint like BCH has     

> __< m-relay_ >__ <r​ucknium:monero.social> If you do that, you add a liveness assumption to the network     

> __< m-relay_ >__ <r​ucknium:monero.social> Or to nodes I mean     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> jeffro256: The private option is the depth reorgs are infeasible. To suggest we can reduce it is to disagree with my premise or to say reorgs aren't feasibly by an adversary at 9 blocks.     

> __< m-relay_ >__ <r​ucknium:monero.social> Since a node that has been shut down for a while can wake up to two blockchains because it never saw the Nth checkpoint block     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> It's not about if a reorg actually happens. It's about the tree root selection being a fingerprint.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> Rucknium: If we assume you're not eclipsed, and no adversary has 51%, then the probability of a n-block reorg goes down with each additional block.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> An adversary with just 49% can only pull off any reorg with random chance.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I'm calling for the n-block lock to have n be the soft finality depth, where we define soft finality as an adversary having infeasible likelihood of performing a reorg. This is generally done in practice with the hash power percentage of the top mining pool(s).     

> __< m-relay_ >__ <r​ucknium:monero.social> Allowing nodes to leave and re-enter the network was part of the bitcoin design in the white paper     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I'm not claiming it's hard finality, even though that can be a discussion for another day. I'm saying PoW coins for years have evaluated reorg risks for minority adversaries and recommended amounts of confirmations accordingly.     

> __< m-relay_ >__ <r​ucknium:monero.social> What's your infeasibility probability?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> (and also higher confirmations for situations of higher criticality, I'm not blind to that)     

> __< m-relay_ >__ <r​ucknium:monero.social> Those have usually been heuristics. Satoshi had the wrong minority attack formula in the white paper anyway     

> __< m-relay_ >__ <r​ucknium:monero.social> Recommendations are just risk management. Everyone has a different risk preference     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> If you want to say they're heuristics and have me call them such, I'm fine doing so.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I'd call for at least 1% odds by the largest mining pool.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> Specifically for the n-block lock.     

> __< m-relay_ >__ <r​ucknium:monero.social> Over what period of time? A year? And what is the resource of the adversary? Can it keep trying every block?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I guess we'd have to define how long until we expect users to realize they've been so repurposed. I am scared to ask what the confirmation count needs to be if we say over a day though.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> I said > largest mining pool     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> And if they have a finite amount of hash power for attempts, can't they only start an attempt occasionally? Having attempts in parallel would mean they have more hash power than assumed.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> Or we simplify to a singular attempt. I don't have all the answers here and I'm not trying to claim I do. I'm solely saying that even if a non-trivial adversary attempts a reorg, it should be agreed sufficiently unlikely at some confirmation depth. I believe that depth should be lock depth.     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> (not just unlikely naturally, yet unlikely by an active attacker so infeasible)     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> If we want to reduce the lock depth, I'd call to reduce the depth at which we consider reorgs infeasible. I wouldn't call to alternatively define the lock depth.     

> __< m-relay_ >__ <r​ucknium:monero.social> I have a question about this sentence in the paper: "[In Zcash] There are few network consensus rules governing the age of this anchor; it must be at least one and at most 100 blocks old."     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> If I can pay 10k over a year to invalidate TXs once a month, some wallets will default to more stable tree roots and we will end up with fingerprints though.     

> __< m-relay_ >__ <r​ucknium:monero.social> Would FCMP++ have a maximum age of an anchor? If it doesn't any tx that stays in the txpool longer than the max anchor depth would be permanently invalid, right?     

> __< m-relay_ >__ <k​ayabanerve:matrix.org> No, doing so would invalidate TXs as you say.     

> __< m-relay_ >__ <r​ucknium:monero.social> Unless there are objections I will put the 10 block lock on the agenda for next meeting. It has been about a year since it was on the agenda. Right on time for its annual appearance.     

> __< m-relay_ >__ <r​ucknium:monero.social> We can end the meeting here.     

> __< isthmus >__ I don't think Zcash has _any_ consensus rules regarding the anchor depth.     

> __< isthmus >__ The 100 blocks thing is just a limit on what parameters the wallet uses     

> __< isthmus >__ It defaults to 3 but allows the user to specify 1 to 100     

> __< isthmus >__ And of course it would be trivial to fork the wallet and change that range to 200 or 1000 or whatever     

> __< m-relay_ >__ <r​ucknium:monero.social> Thanks, isthmus     

> __< dEBRUYNE >__ Having had experience in the past with network upgrades, the ecosystem will not be able to cope with successive network upgrqdes in a short time-spqn     

> __< dEBRUYNE >__ Even when Monero was much smaller it was already difficult to get everyone to upgrade properly and on time    

# Action History
- Created by: Rucknium | 2024-09-03T20:43:58+00:00
- Closed at: 2024-09-17T21:24:51+00:00
