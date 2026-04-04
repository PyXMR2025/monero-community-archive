---
title: Monero Research Lab Meeting - Wed 11 June 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1220
author: Rucknium
assignees: []
labels: []
created_at: '2025-06-10T22:01:30+00:00'
updated_at: '2025-06-19T18:10:53+00:00'
type: issue
status: closed
closed_at: '2025-06-19T18:10:53+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Divisors for FCMP. [zkSecurity quote for review of Elliptic Curve Divisors for FCMP](https://hackmd.io/@rotn/HyyFGZcfxl).  [Cypher Stack review](https://github.com/cypherstack/divisor_deep_dive).

4.  CCS proposal: [Monero Network Simulation Tool](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589).

5. Subnet deduplication in peer selection algorithm to avoid spy nodes. [Draft research bulletin](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf), [implementation PR](https://github.com/monero-project/monero/pull/9939).

6. Web-of-Trust for node peer selection.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1217 

# Discussion History
## Rucknium | 2025-06-12T23:18:21+00:00
Logs

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours     

> __< j​berman:monero.social >__ I unfortunately won't be able to make today's meeting. Repeating my update from NWLB:     

> __< j​berman:monero.social >__ All expected tests now pass in fcmp++-stage (we have green CI), shared a TODO list for launch issue tracker ( https://github.com/seraphis-migration/monero/issues/53 ), made serious headway on destroying FFI types correctly thanks to jeffro256 ( https://github.com/seraphis-migration/monero/pull/39 )     

> __< j​berman:monero.social >__ Working on finishing that last task, and allowing txs with >8 inputs next. And fixing up current PR's / reviewing jeffro's     

> __< j​effro256:monero.social >__ Sorry, I also won't be able to make it to the meeting today. Yeah, mainly spent this week on cleanups / fixes / reviewing j-berman's work     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1220     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ mac      hi     

> __< 0​xfffc:monero.social >__ Hi everyone     

> __< a​rticmine:monero.social >__ Hola     

> __< s​gp_:monero.social >__ Hello     

> __< rbrunner >__ Hello     

> __< a​ntilt:we2.ee >__ seas     

> __< d​iego:cypherstack.com >__ hi     

> __< d​iego:cypherstack.com >__ us first please, I have to go soon. On vacation.     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ Diego Salazar: Yes, you will be first     

> __< r​ucknium:monero.social >__ jberman and jeffro256 gave their updates just before the meeting ^     

> __< b​randon:cypherstack.com >__ finishing up teh report on divisors     

> __< b​randon:cypherstack.com >__ have a pre-pre-print for yall which is actionable     

> __< b​randon:cypherstack.com >__ still has some edits remaining and we need to spend a few days copyediting it before we throw it up on iacr and make it more public, but we can hand off what we have today so MRL can move on it     

> __< r​ucknium:monero.social >__ me: Working on finishing review of Clover, an alternative to Dandelion++. Also, I modified boog900 's Rust network scanner to get an estimate of the number of reachable nodes that are using the spy nodes ban list: https://github.com/Rucknium/misc-research/pull/5     

> __< 0​xfffc:monero.social >__ ( Last W til yesterday I was off. So I have not an important update right now. I am running late but I will address all the 9933 PR comment before end of this week with new code )     

> __< r​ucknium:monero.social >__ 3) Divisors for FCMP. [zkSecurity quote for review of Elliptic Curve Divisors for FCMP](https://hackmd.io/@rotn/HyyFGZcfxl).  [Cypher Stack review](https://github.com/cypherstack/divisor_deep_dive).     

> __< v​tnerd:monero.social >__ me: more work on subaddress/fees in lws     

> __< d​iego:cypherstack.com >__ we have something!     

> __< s​gp_:monero.social >__ Before the zksecurity quote, it would be good to hear from CS about what they worked on last week     

> __< s​gp_:monero.social >__ Since the outcome of that will determine what we need zksecurity for     

> __< b​randon:cypherstack.com >__ making a github repo with the doc as we speak     

> __< b​randon:cypherstack.com >__ merging final conflicts, yada yada     

> __< r​ucknium:monero.social >__ ....LaTeX refuses to build 😳     

> __< r​ucknium:monero.social >__ ;)     

> __< b​randon:cypherstack.com >__ we aren't fully done but the report is actionable enough to send off to yall. we present a protocol as we understand how it SHOULD work, and we show how to use it for schnorr signature verification and bulletproof verification     

> __< d​iego:cypherstack.com >__ if I may, Brandon, I will quote you from earlier today     

> __< b​randon:cypherstack.com >__ so if i were to recommend how to use zksecurity to move forward, they should vet our work and check it for correctness and look for mistakes in our proofs     

> __< b​randon:cypherstack.com >__ sure     

> __< d​iego:cypherstack.com >__ "We think we have things proven to our satisfaction, we just haven't finished fully computing all the probabilities and computational costs, nor have we fully finished providing examples. However, the vast vast vast majority of the argumentation is done, and i think good."     

> __< d​iego:cypherstack.com >__ "The final touches will be a bit longer, but at this point we don't have much reason to think the technique is incorrect or unsound fundamentally."     

> __< r​ucknium:monero.social >__ "Computational costs". Does that mean that the verification time would be much different from what we think it is now?     

> __< d​iego:cypherstack.com >__ late nights and weekends to get it to this point by this meeting     

> __< r​ucknium:monero.social >__ Or maybe the proving time?     

> __< s​gp_:monero.social >__ I assume the proof modifications are documented in the forthcoming tentative report, but can you briefly summarize them and how major you think those changes might be for Monero to adjust to (it's ok if you don't fully know the answer there)     

> __< r​ucknium:monero.social >__ Thank you Cypher Stack for putting in all this incredible work     

> __< b​randon:cypherstack.com >__ freeman wrote up a little sage piece of code which will be helpful for assessing these costs     

> __< b​randon:cypherstack.com >__ So, the short answer is this     

> __< b​randon:cypherstack.com >__ firstly, the proof modifications required don't seem to impact our asymptotic results, but influence specific constants.     

> __< b​randon:cypherstack.com >__ we compute a soundness error lower than Bassa's, and I don't fully trust it. But, if Bassa's soundness error is an acceptable upper bound already, then this actually isn't much of a problem.     

> __< b​randon:cypherstack.com >__ we beat Bassa's completeness error.     

> __< b​randon:cypherstack.com >__ eagen derived his verification equations by looking at everything as a function of slope and intercept, but by doing so accidentally assumed that everything could be written as rational functions in these parameters. they cannot be, except in edge cases. reparameterizing (begun by Bassa at veridise but not completed) resolves the problem, but due to this mistake, the "chain rule" <clipped messag     

> __< b​randon:cypherstack.com >__ from calculus was not correctly computed, so verification equations are all much more complicated     

> __< b​randon:cypherstack.com >__ i'm not sure if that answers your question to your satisfaction sgp_     

> __< b​randon:cypherstack.com >__ so, at this point, everything seems fine, and we have 40 pages of argumentation and background and proofs to back up the word "seems"     

> __< b​randon:cypherstack.com >__ moreover, kayaba's divisor witness computation works fine also.     

> __< b​randon:cypherstack.com >__ so if any further modifications to code are required it is all on the verification side, to make sure that the verification equations being checked actually support the proving system in question     

> __< b​randon:cypherstack.com >__ we began working out an example of kayaba's "discrete log gadget" which is really a "correct scalar multiplication proving" gadget, but we haven't fully finished that example due to time constraints; future updates to this paper will include it     

> __< s​gp_:monero.social >__ I don't really have a specific follow up question, but I will schedule some time with kayaba to go through your paper and see where any changes could impact their code, and if so, what that looks like     

> __< r​ucknium:monero.social >__ Verification equations being much more complicated = CPU verification time would be much longer? Do we know?     

> __< r​ucknium:monero.social >__ So Eagen neglected the reals, huh?     

> __< b​randon:cypherstack.com >__ freeman's sage code will help answer that question, but we did not finish our efficiency analysis yet either. all the added costs are "just" computations over the base field, and all muls and adds, no divisions. so we are asymptotically still getting the same advantage as the old verification equations     

> __< f​reeman:cypherstack.com >__ I'll throw in that adapting Eagen's divisors code to benchmark shouldn't take very long     

> __< b​randon:cypherstack.com >__ we've been scrambling on the proofs and all the rest was lower priority     

> __< f​reeman:cypherstack.com >__ For anyone curious https://gist.github.com/Liam-Eagen/666d0771f4968adccd6087465b8c5bd4     

> __< r​ucknium:monero.social >__ As I understand it, it is the role of the FCMP Research co-chairs to guide decisions on what to do next. And they are absent this meeting ( kayabanerve  and jberman ).     

> __< s​gp_:monero.social >__ Assuming kayaba can adapt it as expected, your efforts have helped save Monero a _lot_ of time, and saved Monero from choosing a significantly less performant approach     

> __< r​ucknium:monero.social >__ Or, more importantly, deploying a fatally flawed protocol on mainnet, which could destroy Monero.     

> __< f​reeman:cypherstack.com >__ For anyone curious, this is Eagen's code that can be adapted for timing https://gist.github.com/Liam-Eagen/666d0771f4968adccd6087465b8c5bd4     

> __< d​iego:cypherstack.com >__ yeah yeah, no need to thank us citizens. Just doing our superhero jobs.     

> __< b​randon:cypherstack.com >__ more review is better     

> __< d​iego:cypherstack.com >__ Now I'm going to tell Brandon to skedaddle. He was literally up most of the night finishing this up.     

> __< b​randon:cypherstack.com >__ i would love it if zksecurity scrutinized us     

> __< b​randon:cypherstack.com >__ i need to finish making the CS github for this though first, diego     

> __< d​iego:cypherstack.com >__ yes, please use zksecurity to look over our stuff     

> __< s​gp_:monero.social >__ Yeah, I think that is the best path forward (after kayaba/beman look at it)     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< s​gp_:monero.social >__ speak of the devil :)     

> __< r​ucknium:monero.social >__ I agree that this work by Cypher Stack needs review. zkSecurity can be considered. Would be a good candidate     

> __< k​ayabanerve:matrix.org >__ If everyone here agrees on zkSecurity performing review being a good idea, then I can be sent the draft for my professional opinion on if we should move forward (so MRL approval now, moving forward later).     

> __< k​ayabanerve:matrix.org >__ But I haven't seen the draft and can't comment this meeting.     

> __< k​ayabanerve:matrix.org >__ Alternatively, we just continue having SGP play diplomat and ask to keep the time boxed off and we'll sync again next meeting.     

> __< b​randon:cypherstack.com >__ it'll be available in the next hour or so     

> __< k​ayabanerve:matrix.org >__ I won't read it till tomorrow regardless so no worries there     

> __< r​ucknium:monero.social >__ The timeline on zkSecurity's original quote was:     

> __< r​ucknium:monero.social >__ > The team will primarily carry out the work during the week of the 23rd of June till 27th of June. We commit to providing the report by the 18th of July; with the additional time allowed to account for protocol / proof updates as necessary and to compile the final report.     

> __< s​gp_:monero.social >__ I want to get back to zksec this week with an (ideally) final plan for their review time. That should be doable     

> __< r​ucknium:monero.social >__ https://hackmd.io/@rotn/HyyFGZcfxl     

> __< r​ucknium:monero.social >__ So, theoretically, they have the week of June 23 open     

> __< k​ayabanerve:matrix.org >__ It's just a question on if we want to confirm with committed funding this weekend or next meeting. I'm indifferent. Up to y'all.     

> __< r​ucknium:monero.social >__ It sounds like the plan is for kayabaNerve to review the next Cypher Stack document, then kayabaNerve, jberman, and sgp can discuss  and decide on a plan to approach zkSecurity again     

> __< s​gp_:monero.social >__ I'll negotiate a different rate since they no longer need to do fixed rate     

> __< s​gp_:monero.social >__ I'd like to be able to move forward with their approval outside of a meeting, if possible     

> __< r​ucknium:monero.social >__ I want to say that an approved funds limit should be decided now, but then that gives away MRL's negotiating position 😅     

> __< s​gp_:monero.social >__ ha     

> __< r​ucknium:monero.social >__ I could easily see the admin work taking enough time that approval next Wednesday would not add much delay at all. zkSecurity has to read 40 dense pages, then produce a new SoW and quote     

> __< s​gp_:monero.social >__ it's a matter of keeping the slot at this point     

> __< s​gp_:monero.social >__ I can try to offer a refundable retainer, idk     

> __< r​ucknium:monero.social >__ I think it would be OK to go ahead with "approving" the funds before next meeting if the time slot is in danger of disappearing.     

> __< r​ucknium:monero.social >__ Again, giving away the negotiating position publicly :D     

> __< r​ucknium:monero.social >__ Or zkSecurity may decide that the direction that Cypher Stack took things is outside of their areas of expertise.     

> __< s​gp_:monero.social >__ I'll share it publicly when I have the scope updated so people can give their 👍 or 👎 publicly     

> __< s​gp_:monero.social >__ I just prefer not to wait another week if everyone on that committee gives it their 👍     

> __< r​ucknium:monero.social >__ Anyone else want to chime in on this decision?     

> __< s​gp_:monero.social >__ if the proposal sucks we can just skip it     

> __< s​gp_:monero.social >__ and find someone else     

> __< rbrunner >__ The difficulty of the job dropped considerably now, right?     

> __< s​gp_:monero.social >__ in theory     

> __< rbrunner >__ Well, if the new approach does not work out, it's back to square 1, but otherwise it's "only" a verification     

> __< b​randon:cypherstack.com >__ considerably, imo, yes     

> __< rbrunner >__ Still nice to get those people to do it, IMHO     

> __< rbrunner >__ For a bit less, hopefully :)     

> __< b​randon:cypherstack.com >__ i'm happy to hand off my latex code to them also if it turns out they would rather help fix our document than write their own new one     

> __< r​ucknium:monero.social >__ I am ok with going forward with a reasonable expenditure for a reasonable scope of work from zkSecurity, before next Wednesday's meeting.     

> __< rbrunner >__ Same     

> __< r​ucknium:monero.social >__ More discussion on this topic?     

> __< s​gp_:monero.social >__ I definitely expect to provide them with the CS doc. No more discussion from me     

> __< r​ucknium:monero.social >__ 4. CCS proposal: Monero Network Simulation Tool. https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/589     

> __< r​ucknium:monero.social >__ This is a proposal from gingeropolous     

> __< r​ucknium:monero.social >__ It would make Monero usable in the Shadow network simulator. Shadow has been developed for over ten years. Its primary purpose has been to research the Tor network.     

> __< r​ucknium:monero.social >__ Shadow could be used to test new Monero network code in a realistic setting without trying it on mainnet     

> __< a​ntilt:we2.ee >__ rucknium i read your R code; are you familiar with Shadow ?     

> __< r​ucknium:monero.social >__ Not to undermine gingeropolous , but in the interests of the Monero Project, it could be good to get an alternative "quote" from the developer of EthShadow, which made Ethereum nodes compatible with Shadow.     

> __< r​ucknium:monero.social >__ Which R code did you read? 👀     

> __< r​ucknium:monero.social >__ I have read a few papers recently that used Shadow to analyze the Tor network.     

> __< plowsof >__ if all goes well then yes, it would make Monero usable in the shadow network simulator but ginger  if "hesitant to list specific milestones. Instead, I request that this CCS be a time-spent based CCS"     

> __< r​ucknium:monero.social >__ January 29 MRL meeting has my summary of some of those papers     

> __< plowsof >__ there is also a hardware upgrade element for the MRL machine. a new UPS     

> __< a​ntilt:we2.ee >__ rucknium peer nodes list draft code     

> __< a​ntilt:we2.ee >__ i am a bit sceptical; would use R and C++ and test under real world conditions. but I dont know how smart Shadow is...     

> __< r​ucknium:monero.social >__ Shadow is supposed to give realistic results. You plug actual program binaries into it. That's how I understand it. The advantage is that you can "slow down" the network if the whole network is too burdensome for the CPU to process all at once. And it offer realistic latency on a global scale     

> __< rbrunner >__ I don't have an opinion, because I don't have any idea how something like "Shadow" really works, and what it brings to the table     

> __< r​ucknium:monero.social >__ I am not sure one way or the other about the need for more storage space in the Monero Computing Cluster. I don't know if I would try to use Shadow to fill up a lot of blockchain space. It could be hard for the I/O to process that many blockchains. On the other hand, the Shadow developers said that the simulation is "paused" during storage read/writes. I mean, it doesn't count the<clipped message     

> __< r​ucknium:monero.social >__  time spent on those operations.     

> __< r​ucknium:monero.social >__ Here's a discussion about the pros and cons of Shadow compared to running on "bare metal": https://github.com/shadow/shadow/discussions/3503     

> __< a​ntilt:we2.ee >__ IMHO this overhead is not needed for what we are doing with de-doubling     

> __< r​ucknium:monero.social >__ The discussion was initiated by the EthShadow developer: https://github.com/shadow/shadow/discussions/3425     

> __< a​ntilt:we2.ee >__ will read it tomorrow     

> __< r​ucknium:monero.social >__ Right. I don't think the deduplication would need analysis with Shadow. It is more about major protocol changes. For example, the more efficient tx propagation protocol.     

> __< r​ucknium:monero.social >__ Or catching potential netsplit behavior like the under-reviewed tx_extra limits     

> __< s​yntheticbird:monero.social >__ rbrunner, shadow is intercepting network requests of an application so that it can reroute it within its simulated network. You can apply many rules to simulate different situations. This is almost instantaneous and permit you to recreate internet like topologies.     

> __< rbrunner >__ So real Monero daemons, but simulated network?     

> __< s​yntheticbird:monero.social >__ exactly     

> __< rbrunner >__ I see. Sounds interesting.     

> __< a​ntilt:we2.ee >__ >Once the basic simulation is functional, I will design scenarios to test specific aspects      

> __< a​ntilt:we2.ee >__ this is too vague     

> __< r​ucknium:monero.social >__ Here was my summary of one of the Tor papers that used Shadow: https://libera.monerologs.net/monero-research-lab/20250129#c491556-c491559     

> __< r​ucknium:monero.social >__ Jansen & Goldberg (2021) "Once is Never Enough: Foundations for Sound Statistical Inference in Tor Network Experimentation"     

> __< g​ingeropolous:monero.social >__ im happy to mod the CCS request     

> __< r​ucknium:monero.social >__ gingeropolous: Thanks for joining. Do you want to respond to some of the comments here?     

> __< 0​xfffc:monero.social >__ I would like to comparison to ns3. and why shadow, instead of ns3     

> __< r​ucknium:monero.social >__ To get an idea of scale, let's see, the biggest machine has 1TB of RAM. Keeping all node processes in RAM and assuming usual mainnet RAM consumption (I think it's lower for small-blockchain nets like testnet), that would be about 500 nodes on the Shadow network.     

> __< 0​xfffc:monero.social >__ I had this idea of simulating monero under realworld network simulator for long time under ns3. But never had a time to implement it.  I use this to run 100s of nodes locally and do simple benchmarks though: https://github.com/0xFFFC0000/benchmark-project which was very successful.     

> __< g​ingeropolous:monero.social >__ yeah sorry im late. tryin to see things need responding... i could go either way on additional storage, i just didn't want it to block progress.     

> __< 0​xfffc:monero.social >__ I run 128 node here: https://github.com/0xFFFC0000/benchmark-project     

> __< r​ucknium:monero.social >__ However, the EthShadow developer reported https://github.com/shadow/shadow/discussions/2622     

> __< r​ucknium:monero.social >__ > "I tried using `--use-memory-manager=false` already. It works for me. I can run 5,000 gossipsub nodes with an 8GB machine with 96GB of swap space used. Thank you.     

> __< g​ingeropolous:monero.social >__ nice.     

> __< a​ntilt:we2.ee >__ 0xfffc did you test-run #9933 - what are your first impressions ?     

> __< g​ingeropolous:monero.social >__ re: scenarios, i can get more specific.     

> __< 0​xfffc:monero.social >__ Yes, I ran test for 9933. I can get into deeper information about this, before that need to fix something upstream. The numbers and information will be disclosed.     

> __< 0​xfffc:monero.social >__ Next week, You have my promise I will have more info about that :)     

> __< g​ingeropolous:monero.social >__ re: ns3, i'll be honest I hadn't come across it. But my backwards rationale would be that there already exists a cryptocurrency network impl of shadow, so we know it works. but that also holds true for ns3 now b/c of your work. so....     

> __< 0​xfffc:monero.social >__ I like how shadow operates. I think this can be very helpful CCS. For next step maybe we tried ns3. who knows. ns3 I believe would provide much tighter control over anything. but the cost would be it is much harder to get something like that running.     

> __< a​ntilt:we2.ee >__ 0xfffc i am interested in comparing white + gray_lists... how would spy nodes respond ?     

> __< 0​xfffc:monero.social >__ on 9933? or on ns3 simulation?     

> __< r​ucknium:monero.social >__ This recent paper (March 2025) uses Shadow instead of ns-3 and gives reasons: https://arxiv.org/abs/2503.04810     

> __< a​ntilt:we2.ee >__ #9933     

> __< r​ucknium:monero.social >__ On page 8 to 10     

> __< r​ucknium:monero.social >__ 9 to 10     

> __< r​ucknium:monero.social >__ I mean     

> __< 0​xfffc:monero.social >__ Interesting paper. I am reading it right now     

> __< 0​xfffc:monero.social >__ They have low level requirement which they cannot implement in ns-3 runtime env. This does not apply to monero AFAICT . I am not saying we should definitely use ns-3. But we should be aware of the options.     

> __< 0​xfffc:monero.social >__ I will have more info about this in next meeting. 🤝     

> __< 0​xfffc:monero.social >__ ( my apologies for delay )     

> __< a​ntilt:we2.ee >__ Shadow needs to be "trained" in how spy nodes would likely react... just to make a point that real world is hard to predict. We would need to compile spy nodes to create such a game-like scenario     

> __< r​ucknium:monero.social >__ Seems like there is opportunity for more discussion of the Shadow CCS, especially after more people have time to review materials and think about requirements.     

> __< g​ingeropolous:monero.social >__ oh yeah. there is a lot of ancillary work for the simulations. like, rate of transaction creation... where do we get realist numbers. probably statistics from node data seeing txs come in, with some math stats regarding how many nodes the txs likely came from. etc     

> __< 0​xfffc:monero.social >__ The idea is a positive move forward IMHO.     

> __< g​ingeropolous:monero.social >__ node types: exchanges nodes. pool nodes. user types. Ultimately I'd love there to be a web-gui (or some other means) such that anyone in MRC (or extended) could submit a simulation     

> __< 0​xfffc:monero.social >__ Yes, you are basically simulating a real world. So everything goes here     

> __< r​ucknium:monero.social >__ 5. Subnet deduplication in peer selection algorithm to avoid spy nodes. [Draft research bulletin](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf), [implementation PR](https://github.com/monero-project/monero/pull/9939).     

> __< r​ucknium:monero.social >__ Like I said in my update, I modified boog900 's Rust network scanner to collect the peer lists that nodes share when you do the initial Levin protocol handshake: https://github.com/Rucknium/misc-research/pull/5     

> __< r​ucknium:monero.social >__ And I have results: I estimate that 6 percent of reachable nodes (i.e. nodes with open ports) are running with the spy node ban list.     

> __< r​ucknium:monero.social >__ Not bad. Not great. Within my expectations.     

> __< rbrunner >__ Hmm. I would have estimated higher.     

> __< rbrunner >__ But very good to have hard numbers.     

> __< r​ucknium:monero.social >__ Nodes share 250 random IP addresses from their white_lists. So, if zero IP addresses from the spy node ban list are shared, with high probability the node is using the ban list.     

> __< r​ucknium:monero.social >__ To estimate the number of unreachable nodes using the ban list would be more difficult and take longer, since you have to passively wait for them to connect t you.     

> __< a​ntilt:we2.ee >__ hopefully jeffro256 will review #9939 soon :)     

> __< r​ucknium:monero.social >__ I spot-checked the results for nodes that are known (or claim) to be using the spy node ban list, e.g. Cake Wallet's nodes.     

> __< r​ucknium:monero.social >__ And the spot checks looked correct     

> __< plowsof >__ in my peer list there are approx 60-100 nodes who still relay mordinals at any given time     

> __< rbrunner >__ Lol. How would you even know that :)     

> __< r​ucknium:monero.social >__ plowsof: You mean, would accept a too-large tx_extra tx?     

> __< plowsof >__ correct, rbrunner i ask them "did you update yet lol?" (invalid transaction hex iirc) and their json error response contains the "new" key for being too large true/false      

> __< r​ucknium:monero.social >__ plowsof helped me with a problem I was having with this 6 percent estimate, by the way. Helpful in the shadows as always.     

> __< rbrunner >__ Ok     

> __< plowsof >__ if seed node operators all added this ban list would that help? or do clients then query the other peers in the provided list?     

> __< a​ntilt:we2.ee >__ would help most definitely     

> __< rbrunner >__ I don't think it would help much, at least not in the short term. The IP numbers of the spy nodes are stored all over the place.     

> __< r​ucknium:monero.social >__ plowsof: I think it would help temporarily, but eventually older nodes would just cycle through their peer lists. I think.     

> __< a​ntilt:we2.ee >__ gray_list spamming is too easy right now     

> __< plowsof >__ i see, thank you      

> __< r​ucknium:monero.social >__ IIRC, newborn nodes syncing the blockchain from scratch query the seed nodes. Old nodes only query them as a last resort when they cannot connect to anyone.     

> __< rbrunner >__ I remember the same, yes.     

> __< rbrunner >__ Testnet sometime ran without any working seed nodes for quite some stretches of time     

> __< a​ntilt:we2.ee >__ there is also a fall back mechanism iirc - what Gao et. al would use for a potential eclipse attack     

> __< r​ucknium:monero.social >__ 6. Web-of-Trust for node peer selection.     

> __< a​ntilt:we2.ee >__ Ruckrunium could we plz rename item: "Web-of-Trust for node peer selection" -> "Peer Scoring Metrics" ?      

> __< a​ntilt:we2.ee >__ would be more descriptive of what we are trying to do right now.      

> __< a​ntilt:we2.ee >__ #9933 and #9939 are on the way. Thats perfect already IMHO     

> __< r​ucknium:monero.social >__ Sure. I can do that     

> __< r​ucknium:monero.social >__ Anything more on this topic for now?     

> __< a​ntilt:we2.ee >__ I'd like to get an overview on the "anchor node" code as implemented right now. I can do that if no one has done it before     

> __< r​ucknium:monero.social >__ I would also like to know what the anchor peer behavior is     

> __< r​ucknium:monero.social >__ For now we shall be kept in suspense.     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< a​rticmine:monero.social >__ Thanks     

> __< s​yntheticbird:monero.social >__ chat is this real: https://x.com/MoneroResearchL     

> __< c​haser:monero.social >__ official logo, most officially looking handle possible, but it's unofficial. yeah.     

> __< 3​21bob321:monero.social >__ Wonder who created the account     

> __< s​yntheticbird:monero.social >__ thx anon     

> __< 3​21bob321:monero.social >__ Hope it's not the same person for @ monero    

# Action History
- Created by: Rucknium | 2025-06-10T22:01:30+00:00
- Closed at: 2025-06-19T18:10:53+00:00
