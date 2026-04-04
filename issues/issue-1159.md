---
title: Monero Research Lab Meeting - Wed 19 February 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1159
author: Rucknium
assignees: []
labels: []
created_at: '2025-02-18T22:40:24+00:00'
updated_at: '2025-02-27T17:48:10+00:00'
type: issue
status: closed
closed_at: '2025-02-27T17:48:09+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition).

4. [FCMP research progress status](https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/).

5. Fluffy blocks efficiency improvements.

6. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1155 

# Discussion History
## Rucknium | 2025-02-21T17:08:07+00:00
Logs

> __< j​berman:monero.social >__ FCMP++ competition details are ready for review: https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ I recommend first reading the README at the root, then README's in the 2 directories. I still have some more minor TODO's (the biggest being I want to update the helioselene benchmark tests to calculate the final score)     

> __< r​ucknium:monero.social >__ MRL meeting in this room in two hours.     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1159     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< s​yntheticbird:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< s​agewilder:unredacted.org >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ Howdy     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Some more analysis of subnet deduplication peer selection against spy nodes, preparing all OSPEAD-related documents and code for public release (expected tomorrow), and learning Rust.     

> __< j​berman:monero.social >__ Got FCMP++ txs validating at consensus, the FCMP++ optimization competition details are ready for preliminary review, started re-reviewing 9135     

> __< j​berman:monero.social >__ FCMP++ dev source (I intend to merge this code with jeffro256  's latest): https://github.com/j-berman/monero/tree/73f0e9202ab6397f43babd4c5c129852d68f8f30     

> __< j​berman:monero.social >__ FCMP++ competition: https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< s​yntheticbird:monero.social >__ Me: Uncovered the reason of the levin protocol header signature. It's a reference to an episode of Futurama series     

> __< j​effro256:monero.social >__ Me: Working on debugging release issues and review     

> __< rbrunner >__ Bender's Nightmare, mentioned in a comment somewhere     

> __< r​ucknium:monero.social >__ By the way, as a reminder, anyone can suggest MRL agenda items. Just ping me here or in #monero-research-lounge:monero.social , or leave a comment on one of the MRL agenda GitHub issues. I have been composing the agenda based on my own judgement recently.     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ So main things I did since last week were: 1) settled on a method of scoring helioselene, weighting specific arithmetic operations as a % of the final score, 2) fixed an issue in the wasm-cycles counter used to check for constant time, 3) updated the README's     

> __< j​berman:monero.social >__ On 1) I got flamegraphs for prove/verify/hash_grow (weighting much more heavily on the latter 2, because prove's flamegraph is heavily dominated by ec-divisors) to help determine how much to weigh each op     

> __< j​berman:monero.social >__ That approach / tje weights could use another set of eyes for sure     

> __< j​berman:monero.social >__ Link to the weights: https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/b84d9ecf922f9e1a90ab4dae3206a685622e2c69/helioselene-contest#how-your-helioselene-score-is-calculated     

> __< rbrunner >__ Just curious: How hard, according to experience, will it be to achieve constant time execution for the submitted code?     

> __< rbrunner >__ And I wondered whether people may overlook that requirement and then stumble over it     

> __< j​berman:monero.social >__ That is an important requirement that I should highlight more significantly     

> __< rbrunner >__ Non-negotiable even? Let's say somebody is twice as fast, but not contant time ...     

> __< r​ucknium:monero.social >__ Why is constant-time so important in this application? Just curious.     

> __< j​berman:monero.social >__ I don't know how to answer "how hard" but you can see how the current reference code uses ops like ct_eq and conditional_select to achieve constant time     

> __< s​yntheticbird:monero.social >__ afaik ocnstant-time is only useful for construction. Nodes that only proceed to verification don't need constant timeness     

> __< rbrunner >__ Sounds logical     

> __< j​berman:monero.social >__ kayabanerve: mentioned at one point how it would be relatively trivial to speed up the code by like 300% if non-constant time code was allowed fwiw     

> __< j​effro256:monero.social >__ Do the point adds include doubling ? There might be different techniques for specifically doubling , I don't know if you want to change the weight based on that     

> __< rbrunner >__ If those 300% are true, that will be quite some temptation     

> __< r​ucknium:monero.social >__ I am tempted likewise rbrunner :D     

> __< s​yntheticbird:monero.social >__ same     

> __< s​yntheticbird:monero.social >__ jberman please shatter our dream or we are gonna advocate two implementations :P     

> __< s​yntheticbird:monero.social >__ one for proving, one for verifying     

> __< j​berman:monero.social >__ Constant time is meant to prevent side channel/timing attacks by measuring how long specific functions run, which is a vector to recover the private key material     

> __< s​yntheticbird:monero.social >__ one for proving that is constant-time, and one for verifying that is variable time     

> __< rbrunner >__ Maybe even submit two different algorithms, with one big "if (construction) else if (verifying)" around it     

> __< rbrunner >__ Yeah, that side channel/timing attack story sure is important, but alas, when veryfing transactions probably not important, right?     

> __< j​berman:monero.social >__ point muls do. current point add is composed of field mul/add/sub     

> __< j​berman:monero.social >__ https://github.com/j-berman/fcmp-plus-plus-optimization-competition/blob/b84d9ecf922f9e1a90ab4dae3206a685622e2c69/helioselene-contest/helioselene-contest-src/src/point.rs#L82-L139     

> __< j​berman:monero.social >__ it's dominated mostly by field mul     

> __< j​berman:monero.social >__ like 70% IIRC     

> __< j​berman:monero.social >__ it's true, constant time isn't necessary for verifying. That 300% figure was for ec-divisors prove fwiw     

> __< rbrunner >__ Too bad     

> __< rbrunner >__ But well, maybe somebody comes up with an ingenious approach to making constant-time execution code     

> __< rbrunner >__ With much less penalty     

> __< j​berman:monero.social >__ kayabanerve has explicitly expressed a lack of interest in maintaining/reviewing multiple implementations. Makes most sense to start with constant time anyway     

> __< r​ucknium:monero.social >__ Speaking of kayabaNerve, last week he said "FYI I will explicitly and publicly opt-out of being a judge, as I already have, yet with the additional comment I may enter (publicly or anonymously) as a contestant in the above proposed contest." https://libera.monerologs.net/monero-research-lab/20250213#c495472     

> __< rbrunner >__ Oh     

> __< s​yntheticbird:monero.social >__ \> create a contest     

> __< s​yntheticbird:monero.social >__ \> abandon the contest     

> __< s​yntheticbird:monero.social >__ \> contest is picked up by someone else     

> __< s​yntheticbird:monero.social >__ \> "i will participate to the contest"     

> __< j​berman:monero.social >__ Thinking by next week's meeting we can get sign-offs on the competition details, then move forward with timeline etc.     

> __< s​yntheticbird:monero.social >__ jk. obviously not claiming this was what he planned, i'm still happy by this turn of event, im sure kayabanerve will cook up something nice     

> __< rbrunner >__ You forget the line with "Profit!!!"     

> __< rbrunner >__ Yeah, bad joke, I don't want to insinuate anything of this was planned     

> __< j​berman:monero.social >__ I mean would be great if kayaba wants to jump in too     

> __< rbrunner >__ Hmmm. Maybe that makes other potential contestants think twice, worst case?     

> __< rbrunner >__ We will see.     

> __< c​haser:monero.social >__ rbrunner: it's a risk.     

> __< j​berman:monero.social >__ I don't see a significantly better option on the table than this competition to achieve the goal of faster code     

> __< rbrunner >__ Sure. Is this, by the way, the first contest ever for Monero? Might be, no?     

> __< rbrunner >__ The logo contest at the very start does not count :)     

> __< r​ucknium:monero.social >__ IMHO, there are some ethics issues here. Important enough to bar kayaba from participating? I don't know.     

> __< j​berman:monero.social >__ I think so, I don't recall any past similar contests     

> __< s​yntheticbird:monero.social >__ May I recommend some delay between the announcement of the contest and opening the contest?     

> __< s​yntheticbird:monero.social >__ I'm sure the "cryptography" environment isn't as "excited" as average monero fan, and needs some time to get to the hear of everyone     

> __< r​ucknium:monero.social >__ Ready to move onto the next agenda item, or more to discuss on this?     

> __< c​haser:monero.social >__ what do you have in mind?     

> __< j​berman:monero.social >__ +1 to announcement first, delay, then contest opens     

> __< r​ucknium:monero.social >__ chaser: Self-dealing is the possible ethics issue     

> __< r​ucknium:monero.social >__ Of course, the potential pool of programmers who could/would participate is probably small, so hard to avoid a "self" in there.     

> __< s​yntheticbird:monero.social >__ Oh also, I completely forgot. There should be a chinese translation of the contest. China have a much higher pool than the rest of the world.     

> __< s​yntheticbird:monero.social >__ No i'm not shilling Xin jin ping, our overlord     

> __< c​haser:monero.social >__ Rucknium you mean Kayaba raising the funds, writing the code, and then entering the contest to improve the code and winning part the funds he raised?     

> __< r​ucknium:monero.social >__ More, setting the contest rules     

> __< r​ucknium:monero.social >__ Which writing the code in the first place is part of     

> __< j​berman:monero.social >__ Perhaps kayaba can provide more color/insight into a decision to participate. I would give a few days for a chance to respond     

> __< c​haser:monero.social >__ I don't know. for now I'm not entertaining this possibility.     

> __< r​ucknium:monero.social >__ 4) FCMP research progress status. https://cryptpad.fr/sheet/#/2/sheet/view/yPVIUywwA9-deE9VF6GYm9bXbPdCerdST3UDEEfBxcM/embed/     

> __< rbrunner >__ Sounds a bit far-fetched alright. I think we will have other, much more surprising problems with the contest     

> __< r​ucknium:monero.social >__ I wanted to bring this up since we haven't talked about it in about a month and a half. Anything we can be doing now to prepare for the next steps of protocol proving and code auditing?     

> __< r​ucknium:monero.social >__ And is the sheet I linked up-to-date?     

> __< j​berman:monero.social >__ Sheet is up to date AFAIK. Last I heard, Veridise is making solid progress on their leg of EC divisors R1CS. I haven't heard anything on CS progress. I will get an update     

> __< r​ucknium:monero.social >__ Thanks, jberman     

> __< j​berman:monero.social >__ Perhaps we could bring in a new 3rd party to start on some impl audits. There is also the torsion check review that is isolated and can be reviewed by anyone unfamiliar with the rest of FCMP++ components     

> __< j​berman:monero.social >__ The latter wasn't explicitly part of the funds raised for the CCS     

> __*__ m-relay <s​yntheticbird:monero.social> whispers "zellic... zellic... zellic..."     

> __< c​haser:monero.social >__ does "CS started (?) // Veridise started (?)" mean we don't know whether they started or not?     

> __< j​berman:monero.social >__ I know 100% Veridise started, I'm not 100% sure on CS. I'll double check     

> __< c​haser:monero.social >__ thank you!     

> __< r​ucknium:monero.social >__ Would the torsion check review be a review of mathematics or a code audit?     

> __< c​haser:monero.social >__ as for "Gadgets formal verification", has Veridise been sent a request?     

> __< j​berman:monero.social >__ I'll check up on starting impl audits too. Seems reasonable to start those     

> __< j​berman:monero.social >__ Mathematics. The code is pretty small     

> __< c​haser:monero.social >__ sorry if it's too many questions, I'm just trying to understand the spreadsheet     

> __< j​berman:monero.social >__ AFAIK no. Seems sensible to wait on them to complete their current work     

> __< c​haser:monero.social >__ ah, alright. I suppose they're a small team and they're now fully occupied with the R1CS proofs     

> __< j​berman:monero.social >__ Maybe they do have others available, that's a good point. Will follow up on that as well     

> __< c​haser:monero.social >__ presuming this work is parallelizable with the EC divisors part     

> __*__ sech1 sighs. That competitions being Rust-only cuts a lot of devs, including me     

> __< c​haser:monero.social >__ jberman and given that there is no other viable candidate     

> __< r​ucknium:monero.social >__ I knew it. kayaba eliminating the competition hahahaha     

> __< r​ucknium:monero.social >__ (This is a joke)     

> __< s​yntheticbird:monero.social >__ sech1: never too late to learn Rust (i can understand the disappointment for a C/C++ dev)     

> __< j​berman:monero.social >__ sech1: rust is really not that hard to learn 😏     

> __< rbrunner >__ But hey, getting so good at it in weeks as to win a contest, I don't know :)     

> __< sech1 >__ I'm sure it's easy to learn... but hard to master (to be competitive), as all things     

> __< sech1 >__ Too late for me to enter this competition     

> __< s​yntheticbird:monero.social >__ you can always try to team up with a Crab master and he will translate your improvements     

> __< j​berman:monero.social >__ I think the core of this competition will be implementing faster algorithms, not necessarily niche micro-optimizations that are language specific     

> __< s​yntheticbird:monero.social >__ algorithmic optimization, not code optimization     

> __< r​ucknium:monero.social >__ 5) Fluffy blocks efficiency improvements.     

> __< r​ucknium:monero.social >__ jeffro256 was looking into this ^     

> __< sech1 >__ "Crandall prime with fast reduction algorithms available accordingly.", and "This would enable implementing ECFFT, reducing the computational complexity of ec-divisors." sounds like a plan already, and then what's left will be micro-optimizations that will require extensive knowledge of Rust     

> __< j​berman:monero.social >__ I'll be surprised I guess if it's someone's knowledge of rust that puts them over the edge of another submission as opposed to better algos     

> __< c​haser:monero.social >__ is there a link to get a better meta on the fluffy blocks improvements topic?     

> __< r​ucknium:monero.social >__ chaser: AFAIK, it is very early stages     

> __< j​effro256:monero.social >__ Yes. I think we're probably going to merge #9135 with relaying empty blocks at first , but it would be nice to know if the scheme of relaying transactions you didn't know about doesn't leak information     

> __< j​effro256:monero.social >__ Because its almost guaranteed to be faster in an average case     

> __< r​ucknium:monero.social >__ Oh, it's part of that PR? Ok.     

> __< j​effro256:monero.social >__ https://github.com/monero-project/monero/pull/9135#discussion_r1957451272     

> __< j​effro256:monero.social >__ This is the discussion     

> __< j​effro256:monero.social >__ It should be noted that we can always change the scheme later     

> __< j​effro256:monero.social >__ It's all compatible with one another     

> __< j​berman:monero.social >__ fwiw relaying empty blocks seemed ok to me, I also wanted to re-review that full flow of requesting missing / responding     

> __< j​berman:monero.social >__ want to re-review*     

> __< r​ucknium:monero.social >__ At first glance, I think there could be a small info leak because relaying a block and relaying a fluff-phase tx aren't completely equivalent because fluff-phase txs are relayed with a random delay, but blocks are immediate AFAIK. But on the other hand, at current network conditions, few txs would be in this situation.     

> __< r​ucknium:monero.social >__ I could check it empirically in the node logs from last year since the log level recorded fluffy blocks and when txs were "missed" by the nodes. But anyway, centralized mining pools still do not update their block templates instantly when the get new txs. IIRC, they are on about 20-30 second cycles. And txs propagate throughout the network during the fluff phase in two seconds or less.     

> __< k​ayabanerve:monero.social >__ rbrunner Rucknium Non-constant-time means leaked private keys and no privacy under side-channel attacks.     

> __< k​ayabanerve:monero.social >__ That 300% comment wasn't for node operations. It was for proving. The part that *needs* to be constant-time.     

> __< k​ayabanerve:monero.social >__ Oh, jberman did clarify the context of the 300% comment 👍     

> __< j​effro256:monero.social >__ It would give miners a competitive advantage to puts txs into the block as soon as they see them though?     

> __< r​ucknium:monero.social >__ Yes, but they still don't do that.     

> __< j​effro256:monero.social >__ If that 20-30 second cycle thing really is true then that should be changed IMO     

> __< j​effro256:monero.social >__ that's bad for confirmation turnaround time     

> __< k​ayabanerve:monero.social >__ syntheticbird:monero.social: I didn't propose a contest with an annual extrapolated pay of >1m to the winner :p I can lose interest as a volunteer and reacquire interest upon sufficient payment.     

> __< k​ayabanerve:monero.social >__ If there are sufficient ethical concerns, I'll drop out though. I'll note jberman has been working on the scoring framework without my commentary other than what little I've said here. I also haven't advocated for larger prizes and didn't write the rules with intent to participate.     

> __< r​ucknium:monero.social >__ I already fought this battle, and this is the compromise that mining pools arrived at     

> __< r​ucknium:monero.social >__ kayabanerve: I don't think that the discussion here in this meeting raised to the level of "sufficient ethical concerns" for you to drop out.     

> __< j​berman:monero.social >__ fwiw the total proposed payout right now is 350 XMR (250+100) after taking into consideration the estimate for expected time to complete. Original proposed was 300 XMR (150+75 + 50+25)     

> __< r​ucknium:monero.social >__ In other words, right now it looks like loose consensus to allow you to participate.     

> __< r​ucknium:monero.social >__ e.g. HashVault's refresh is 20 seconds after I published my research: https://old.reddit.com/r/Monero/comments/10gapp9/centralized_mining_pools_are_delaying_monero/j52n5uc/     

> __< k​ayabanerve:monero.social >__ jberman: Math and impl. I'm not convinced the impl matches the paper and think it's a further derivative. Then, even if the theory is sound, if your code doesn't match, it risks questions about inflation.     

> __< j​berman:monero.social >__ Ya, fair. I think all of impl could use auditing fwiw     

> __< k​ayabanerve:monero.social >__ sech1: I don't believe Rust, at this level of programming, should be a blocker. The end-goal of the Helioselene arithmetic is just operations over arrays which Rust doesn't really do with novelty UNLESS you explicitly expect the C preprocessor.     

> __< k​ayabanerve:monero.social >__ The FFT code is also mathematical theory. The divisors preprocessing is just bit operations. The question is there a more intelligent series than the 3 O(n**2) steps currently present.     

> __< j​berman:monero.social >__ TBC, it seems like we'd want paper math reviewed, then the code math which deviates formalized and reviewed, then the code impl reviewed     

> __< k​ayabanerve:monero.social >__ Sorry. I didn't realize the meeting was still ongoing. Apologies for talking past the current discussion. I'm caught up now.     

> __< s​yntheticbird:monero.social >__ don't apologies people were waiting on your inputs     

> __< k​ayabanerve:monero.social >__ Or to use it for wallets only where it's only a liveness issue if it breaks.     

> __< s​yntheticbird:monero.social >__ now you may proceed to apologies for apologizing     

> __< j​berman:monero.social >__ (or combine first two together as one mathematics review)     

> __< j​berman:monero.social >__ I think we should still use it for wallets only and is probably worth a focused review anyway     

> __< k​ayabanerve:monero.social >__ I will also accept 1m/y to operate the contest, and not participate accordingly, for the time I spend working on the contest :p     

> __< k​ayabanerve:monero.social >__ I'm not trying to be rude, I'm just being explicitly clear my interest in this contest isn't due to my free time or personal love for the subject. I believe the current code is fine. It just got bumped up to a very large $ figure after I dropped it.     

> __< s​yntheticbird:monero.social >__ i dont find it rude     

> __< s​yntheticbird:monero.social >__ i love money so it make sense to me     

> __< k​ayabanerve:monero.social >__ Eh, it's at least a bit cutthroat/ruthless/merc     

> __< j​berman:monero.social >__ It got bumped in discussions where we weren't accurately taking into consideration expected time to complete the work. It was brought down again after taking your prior estimate into consideration     

> __< k​ayabanerve:monero.social >__ And like magic, I've lost interest and will go find other places to pay my bills     

> __< k​ayabanerve:monero.social >__ :p     

> __< j​berman:monero.social >__ lol     

> __< r​ucknium:monero.social >__ We can end the meeting here. Feel free to continue discussing things.     

> __< c​haser:monero.social >__ I don't think anyone  can "allow" someone to participate, since the contest allows pseudonymous submissions. if it's assumed that Kayaba is self-dealing, they could just enter under a different name. and, if not, then please participate, by all means necessary.     

> __< sech1 >__ kayabanerve I will take a look of course at the competition tasks, from the algorithmic perspective. But my progress will be slowed down by almost 0 knowledge of Rust, so there's that. I'm sure I will be able to get through this, but my implementation can suffer from some stupid performance mistake that I don't know about in Rust     

> __< s​yntheticbird:monero.social >__ sech1 really you should team up with someone else     

> __< k​ayabanerve:monero.social >__ I'll be honest about if I may participate. It's only if I was dishonest that I could compete without approval (or at least without backlash).     

> __< sech1 >__ I would "team up" with an AI to check my code, but it's not allowed in the competition     

> __< j​berman:monero.social >__ we can request kayaba not participate as a show of good faith and knowing kayaba, I imagine would honor it. I think the ethics concern is understandable to some degree, and was first voiced by a potential contestant who doesn't want to participate anymore     

> __< sech1 >__ but wait, is it allowed to just check the code for possible performance issues?     

> __< s​yntheticbird:monero.social >__ sech1 "LLM generated code is prohibited", as long as our overlord DeepSeek don't write a fix it's ok on paper     

> __< sech1 >__ I would write code myself, with AI guidance about Rust-specific details     

> __< k​ayabanerve:monero.social >__ jberman: BTW, Rust 1.84 added wasm32v1-none which is without platform-specific architectural extensions. The contest should likely compile with it (not wasm32-unknown-unknown) to prevent concerns re: autovectorization.     

> __< k​ayabanerve:monero.social >__ sech1: Evaluation box is public. I think the scoring framework was publicized by jberman.     

> __< j​berman:monero.social >__ well, that makes things easier. sgtm     

> __< sech1 >__ what is the time frame for the competition? How long will it last?     

> __< j​berman:monero.social >__ I'm going to take out the AI/LLM thing. if the code works the code works. I guess concern was over licensing issues?     

> __< sech1 >__ 50% of the time, AI code works all the time :D     

> __< j​berman:monero.social >__ I was thinking 2 months from contest open to close     

> __< s​yntheticbird:monero.social >__ my concern is about human dignity and being able to look at yourself in the mirror ngl. But the "The end justify the means" outreach human condition.     

> __< j​berman:monero.social >__ maybe 3?     

> __< sech1 >__ I wouldn't rely on AI and just copy-paste their (its?) code     

> __< sech1 >__ For me, AI is a tool, not a "make it work" button     

> __< k​ayabanerve:monero.social >__ jberman: I'm not merging LLM-generated code or code with a reasonable suspicion it may have been LLM-generated into my personal tree.     

> __< k​ayabanerve:monero.social >__ I don't consider it ethical not safe.     

> __< k​ayabanerve:monero.social >__ LLM-assisted developers have higher confidence in their code despite lower quality.     

> __< sech1 >__ How would you know it's LLM-generated? Where is the line? Is autocomplete is IDEs an AI?     

> __< sech1 >__ *in IDEs     

> __< k​ayabanerve:monero.social >__ Monero doesn't need greater confidence in worse code. It needs proper confidence in solid code.     

> __< s​yntheticbird:monero.social >__ sech1: I don't particularly target you with my statement, i believe you are good enough to expect a tool to act as a tool.     

> __< s​yntheticbird:monero.social >__ I was more talking about people fully generating their code and whom their work is "prompt engineering"     

> __< sech1 >__ If I enter the competition I will be LLM-assisted only by necessity. I wouldn't need it for C/C++     

> __< k​ayabanerve:monero.social >__ LLM-generated code has a vibe to it. I also had it in their rules so only a dishonest participant would use an LLM. I believe that rule, plus reasonable evaluation, would be sufficient.     

> __< k​ayabanerve:monero.social >__ Also, auto complete generally doesn't use ML so it obviously wouldn't qualify.     

> __< j​berman:monero.social >__ Ok if LLM-generated code wins the competition I'll rewrite the code     

> __< sech1 >__ Apart from licensing isssues, a good test suite will filter out any bad code     

> __< s​yntheticbird:monero.social >__ Zed editor would like to have a word     

> __< s​yntheticbird:monero.social >__ (Yes autocomplete can now be LLM powered)     

> __< k​ayabanerve:monero.social >__ sech1: I don't care how you waste your time. I just care no spam enters into the code I have to deal with, if I have to deal with it.     

> __< sech1 >__ I said already I won't be copy-pasting     

> __< sech1 >__ I like to know my code from top to bottom     

> __< sech1 >__ otherwise I wouldn't understand what to do with it     

> __< k​ayabanerve:monero.social >__ jberman: You're either throwing out the winner or laundering. Either way, you're not doing something proper.     

> __< k​ayabanerve:monero.social >__ That's why it's an explicit disqualification currently.     

> __< j​berman:monero.social >__ I don't really understand your argument here     

> __< sech1 >__ I'm just being open about my LLM usage     

> __< k​ayabanerve:monero.social >__ sech1: Heard. Please see "I don't care how you waste your time". I have no issues between us right now.     

> __< sech1 >__ If you think that I will waste my time befcause someone else will have a better implementation, maybe I shouldn't try then     

> __< s​yntheticbird:monero.social >__ sech1 he was talking to jberman not you     

> __< k​ayabanerve:monero.social >__ jberman: If the winner is LLM generated, and you rewrite it:     

> __< k​ayabanerve:monero.social >__ Are you writing a distinct solution or are you just making it so the teacher doesn't notice you copied someone else's homework?     

> __< k​ayabanerve:monero.social >__ If the latter, there's all of the same issues. You just laundered the LLM output.     

> __< s​yntheticbird:monero.social >__ replying to jberman proposing to rewrite manually an AI generated winner     

> __< sech1 >__ Plus I don't think an LLM will be able to write a meaningful working code for this competition     

> __< sech1 >__ It will need to be tightly guided, step by step and with small pieces of code     

> __< k​ayabanerve:monero.social >__ sech1: No. I'm saying I think you using a LLM is a waste of your time. I don't think competing is a waste of your time. I tried to encourage you to do so.     

> __< j​berman:monero.social >__ Where is the "wrong" thing? LLM's generating code and then them not attributing properly and so downstream user of teh code not attributing properly?     

> __< sech1 >__ Why waste of my time? If I get some Rust compiler error (which I know nothing about), it will be faster to ask an LLM wtf is wrong than google the answer     

> __< j​berman:monero.social >__ "copying someone else's homework" it's FOSS..     

> __< k​ayabanerve:monero.social >__ I think you can pick up sufficient Rust trivially or find the necessary educational resources without going to a bottom-barrel plagiarist who consistently hallucinates, even if hallucinations are less discussed now.     

> __< k​ayabanerve:monero.social >__ jberman:      

> __< k​ayabanerve:monero.social >__ > LLM-assisted developers have higher confidence in their code despite lower quality.     

> __< k​ayabanerve:monero.social >__ That and the ethical issues.     

> __< k​ayabanerve:monero.social >__ That's not what FOSS means.     

> __< sech1 >__ I tested LLMs and I have 0 confidence about their ability to write code longer than 10-20 lines at a time :D     

> __< k​ayabanerve:monero.social >__ FOSS doesn't mean you're allowed to copy without care.     

> __< sech1 >__ Even 10 lines C++ programs I tested had issues and needed to be guided to fix them     

> __< j​berman:monero.social >__ As judges we're going to review the code quality     

> __< k​ayabanerve:monero.social >__ sech1: That's why I think LLMs are a waste of time.     

> __< sech1 >__ Not a waste of time to explain some Rust syntax of compiler errors, that's my plan     

> __< k​ayabanerve:monero.social >__ You're welcome to disagree though, I don't have to care here and don't mean to scare you off.     

> __< sech1 >__ *or compiler errors     

> __< k​ayabanerve:monero.social >__ I still disagree :p But that's fine, we can.     

> __< sech1 >__ Honestly I would prefer C for this competition. It's "unsafe" only in incapable hands.     

> __< b​oog900:monero.social >__ Lol     

> __< s​yntheticbird:monero.social >__ you just paint yourself a target for all rustacean in the chat     

> __< j​berman:monero.social >__ yes so your ethics concern is with LLM not attributing properly and then downstream using the code, and also therefore not attributing properly by default sounds like     

> __< sech1 >__ Rust being "safe" doesn't automatically make it _safe_     

> __< sech1 >__ Sure, it eliminates whole classes of errors (that juniors and mids do in C/C++), but not all of them     

> __< s​yntheticbird:monero.social >__ not saying you are wrong (i think it's wrong) but clearly all rustacean have been indoctrinated in counter-argumenting this specific "skill issue" argument     

> __< k​ayabanerve:monero.social >__ There's an ethics concern and a safety concern. Reviewers shouldn't be further burdened.     

> __< sech1 >__ A dangerous delusion about Rust I feel in the programming community     

> __< k​ayabanerve:monero.social >__ sech1: It achieves a specific definition of memory safety, which is a very large class of bugs.     

> __< k​ayabanerve:monero.social >__ *barring compiler bugs     

> __< sech1 >__ Except memory leaks. Memory leaks are fine :D     

> __< k​ayabanerve:monero.social >__ Then the std lib, libraries in general, practice solid design patterns to build code with.     

> __< s​yntheticbird:monero.social >__ sech1: Don't mind the community, they are delusional as all programming communities. Even if you disagree, profit from their tech, it'll make your life easier.     

> __< s​yntheticbird:monero.social >__ Rust is a great programming langauge     

> __< s​yntheticbird:monero.social >__ Rust is a great programming language     

> __< k​ayabanerve:monero.social >__ Memory leaks aren't unsafe. They don't risk out of bound read/writes.     

> __< sech1 >__ I don't argue about Rust being great at what it does.     

> __< sech1 >__ But C/C++, with enough skill, is not worse     

> __< k​ayabanerve:monero.social >__ Nor segfaults, nor unaligned operations, nor...     

> __< sech1 >__ Out of bound read/writes are not a thing in C++ if you you std containters only and know how to do it     

> __< k​ayabanerve:monero.social >__ It just places a much higher burden on the developer as there's no longer the automated system ensuring it.     

> __< sech1 >__ anyway, the discussion went off rails     

> __< s​yntheticbird:monero.social >__ I like trains     

> __< s​yntheticbird:monero.social >__ 👍     

> __< k​ayabanerve:monero.social >__ Uhhh I think Vector indexing allows out-of-bounds reads.     

> __< sech1 >__ range-for loops and std::for_each would like to have a word     

> __< k​ayabanerve:monero.social >__ So I really contest 'std containers only and know how to do it' when they blatantly provide unsafe methods     

> __< sech1 >__ modern C++ is safe     

> __< j​berman:monero.social >__ anyone else here think LLM's are unethical?     

> __< k​ayabanerve:monero.social >__ No, but like, x[1] where x is a Vector is unsafe.     

> __< s​yntheticbird:monero.social >__ There is a bounds checking compiled so you will immediately crash. no undefined behavior     

> __< k​ayabanerve:monero.social >__ SyntheticBird: Vector     

> __< s​yntheticbird:monero.social >__ unlike C++     

> __< k​ayabanerve:monero.social >__ C++     

> __< k​ayabanerve:monero.social >__ Not Vec     

> __< s​yntheticbird:monero.social >__ Ah my bad     

> __< k​ayabanerve:monero.social >__ If the immediate way to index one of the most popular C++ std containers is unsafe, I contest modern C++/the std is safe.     

> __< sech1 >__ C++ just doesn't give this guarantee on the language level. But you can write a C++ program without a single index operator and still have loops and vectors and so on     

> __< k​ayabanerve:monero.social >__ Yeah, sure. You can carefully define a subset and manually ensure you're within it.     

> __< k​ayabanerve:monero.social >__ Or you can use an explicitly formally verified subset, as exist, to remove that developer burden.     

> __< sech1 >__ not a burden for a skilled developer, merely a matter of habit     

> __< k​ayabanerve:monero.social >__ Or you can use Rust which isn't a C subset but has a full language and ecosystem.     

> __< sech1 >__ and be performance limited by range checks at every [] operator, right?     

> __< k​ayabanerve:monero.social >__ Yeah, it's a habit for me to use get instead of [], I still occasionally use [] by accident.     

> __< k​ayabanerve:monero.social >__ (One implicitly panics)     

> __< s​yntheticbird:monero.social >__ sech1: it's not that bad as it sounds, compiler do a pretty good job at bound checking analysis     

> __< sech1 >__ tldr Rust is "safe", but not formally, mathematically "safe". Code review, audits etc are still required     

> __< k​ayabanerve:monero.social >__ Isn't Rust just 3-7% slower in a variety of case studies?     

> __< s​yntheticbird:monero.social >__ I heard the same numbers     

> __< sech1 >__ So C++ and Rust are just a different shades of "safe"     

> __< s​yntheticbird:monero.social >__ 3% if you disable overflow check     

> __< s​yntheticbird:monero.social >__ sech1: There is a subset of Rust (i forgot the name but shared it to jberman) that is formally verified for cryptographic purposes     

> __< sech1 >__ great     

> __< c​haser:monero.social >__ I don't see an ethical issue if it helps us find a faster algorithm. the burden on the reviewers due to the fact that LLMs mostly write slop is an angle I haven't considered and may have merit     

> __< sech1 >__ now there is a subset of Rust :D     

> __< s​yntheticbird:monero.social >__ https://hacspec.org/     

> __< sech1 >__ But the current implementation doesn't use it, right?     

> __< b​oog900:monero.social >__ I don't think LLM's should be allowed, although if you can't tell an LLM was used then the submission can't be disqualified ;)     

> __< s​yntheticbird:monero.social >__ ;)     

> __< s​yntheticbird:monero.social >__ # ;)     

> __< sech1 >__ Very true. If the code compiles and passes all tests, was there an LLM? Who knows?     

> __< b​oog900:monero.social >__ often you can smell it, but if you use it very sparingly like what you wanted sech1 then I see no issue.     

> __< s​yntheticbird:monero.social >__ Can we add a rule to prohibit flutter bridged AI generated rust bindings. I don't want Kewbit to announce a 90% completed heliosene implementation     

> __< j​berman:monero.social >__ LLM slop isn't going to win this competition, and if by some miracle chance it does and the code reveals a sound approach, which I would be utterly shocked by also, it should honestly be trivial to rewrite. the challenge is going to be in finding the sound approach     

> __< b​oog900:monero.social >__ then we should reward the LLM!     

> __< b​oog900:monero.social >__ not the person that submitted it     

> __< k​ayabanerve:monero.social >__ Ethics ^     

> __< k​ayabanerve:monero.social >__ Where's a stonks meme but just "efiks"     

> __< sech1 >__ LLM is not a legal entity (yet), so you can't reward it.     

> __< s​yntheticbird:monero.social >__ AI rights     

> __< s​yntheticbird:monero.social >__ soonTM     

> __< sech1 >__ Even my dog has more rights than LLMs     

> __< s​yntheticbird:monero.social >__ krita don't stop crashing in my VM (I blame ZCash) sorry, can't do that on the fly     

> __< c​haser:monero.social >__ an LLM is not only not a legal entity, it's not an entity at all. people like to hallucinate it is because of their yearnings.     

> __< sech1 >__ yes, LLMs miss a crucial part of being "alive" which is memory/experience. They forget everything once you relaunch them, they don't learn on your queries - they're a static blob of 0s and 1s. Heck, even if you don't relaunch them, they forget the beginning of the conversation once it doesn't fit in the context window.     

> __< k​ayabanerve:monero.social >__ PoI had a really interesting scene about this. Great show, one of my favorites.     

> __< k​ayabanerve:monero.social >__ I won't detail it as it's a minor spoiler but iykyk     

> __< k​ayabanerve:monero.social >__ https://github.com/kayabaNerve/fcmp-plus-plus/blob/78754718faa21f0a5751fbd30c9495d7f7f5c2b1/crypto/divisors/src/lib.rs#L289-L414 sech1     

> __< k​ayabanerve:monero.social >__ This is the amount of Rust you need to massively improve ec-divisora     

> __< k​ayabanerve:monero.social >__ *ec-divisors     

> __< k​ayabanerve:monero.social >__ That code is a couple hundred thousand iterations per divisor.     

> __< sech1 >__ "(-F::ONE).to_le_bits().into_iter().take(num_bits_usize).enumerate()" Does Rust force this style of programming?     

> __< sech1 >__ Functional-like?     

> __< sech1 >__ Plus it must be a constant in the end, so does the compiler make it "constexpr" (for a lack of better term)?     

> __< sech1 >__ yeah, I see a lot of micro-optimizations in this code, assuming that compiler is not that smart     

> __< k​ayabanerve:monero.social >__ That's just a vibe. You can manually say     

> __< k​ayabanerve:monero.social >__ let neg_one_bits = (-F::ONE).to_le_bits();     

> __< k​ayabanerve:monero.social >__ for i in 0 .. num_bits_usize {     

> __< k​ayabanerve:monero.social >__ let b = neg_one_bits[i];     

> __< k​ayabanerve:monero.social >__ }     

> __< k​ayabanerve:monero.social >__ It must be constant-time.     

> __< sech1 >__ this whole "for (i, bit) in (-F::ONE).to_le_bits().into_iter().take(num_bits_usize).enumerate() " can be done at compile time. Or by programmer, if compiler is not capable.     

> __< k​ayabanerve:monero.social >__ -F::ONE is a constant, sure, but that transform should be cheap and is *not* available via `const fn`     

> __< sech1 >__ I mean the whole for loop     

> __< sech1 >__ decomposition_of_modulus can be initialized with a constant instead of a loop     

> __< k​ayabanerve:monero.social >__ (const fn are functions running at compile-time and eligible to calculate constants)     

> __< k​ayabanerve:monero.social >__ Probably if the APIs exist. F::ONE is a constant. None of the math ops on it are. Traits (bounds on generics) don't have const fns available :/     

> __< k​ayabanerve:monero.social >__ You'd have to define an extension trait exposing the constant and now we get into more complex Rust     

> __< sech1 >__ It's always like this. Once you start hunting for performance, all language complexity has to be used.     

> __< sech1 >__ But this is micro-optimizations, then can be done at the last step (when the algorithms are implemented)     

> __< k​ayabanerve:monero.social >__ That transform really should be some bit masking and shifts, making it micro, yep.     

> __< sech1 >__ my C/C++ brain says it must be a memset in the end :D (to initialize decomposition_of_modulus)     

> __< sech1 >__ NUM_BITS is typically 256 or close to it?     

> __< k​ayabanerve:monero.social >__ Yep     

> __< sech1 >__ yeah, for loops over single bits are expensive then     

> __< sech1 >__ That code asks for a full rewrite     

> __< j​berman:monero.social >__ Still holding to this: https://libera.monerologs.net/monero-research-lab/20250219#c499558     

> __< j​berman:monero.social >__ you're looking at the part that's not going to speed up the function by >20%     

> __< sech1 >__ "can be done at the last step (when the algorithms are implemented)"     

> __< sech1 >__ Also 256-bit is only 4 64-bit words, so I'm not sure FFT will be faster on such small numbers     

> __< sech1 >__ FFT is good when multiplying really big numbers     

> __< sech1 >__ it can be even slower for small numbers     

> __< sech1 >__ maybe maybe it will be better for 32-bit targets     

> __< k​ayabanerve:matrix.org >__ sech1: That's a misunderstanding.     

> __< k​ayabanerve:matrix.org >__ We do polynomial multiplications where the polynomials have 256 256-bit coefficients.     

> __< sech1 >__ ah, then it's a different story :D     

> __< sech1 >__ this is FFT territory     

> __< sech1 >__ I speak in rhymes now :D     

> __< k​ayabanerve:matrix.org >__ That bit code there is also just nontrivial running time and benefits from a more intelligent design.     

> __< j​berman:monero.social >__ am I missing something with linking this? this snippet isn't the slow part of prove (unless you're saying that part should be constructed differently so that scalar_mul_divisor is faster?)     

> __< k​ayabanerve:matrix.org >__ ... that part is a couple seconds IIRC.     

> __< j​berman:monero.social >__ NO     

> __< j​berman:monero.social >__ sorry lol     

> __< j​berman:monero.social >__ no*     

> __< k​ayabanerve:matrix.org >__ It's 200k iterations per divisor constructed.     

> __< k​ayabanerve:matrix.org >__ I remember adding an additional loop to avoid branch prediction and runtime going up by seconds.     

> __< k​ayabanerve:matrix.org >__ I also remember boog900 replaced an O(n**3) step with an O(n**2) step so it may no longer be so egregious?     

> __< k​ayabanerve:matrix.org >__ Anyways, feel free to bench it by itself if you don't believe it notable. I believe  it's a notable percentage of divisor construction (when defined as scalar, generator -> full divisor).     

> __< k​ayabanerve:matrix.org >__ That preprocess is an isolate step as it's reusable across generators and we do reuse an instance across generators.     

> __< k​ayabanerve:matrix.org >__ It was slow enough it was worth reusing.     

> __< k​ayabanerve:matrix.org >__ I'm not saying it's >50%. Just that it's notable.     

> __< j​berman:monero.social >__ that part is taking my machine less than 1ms, and scalar_mul_divisor is taking 2s     

> __< k​ayabanerve:matrix.org >__ Oh, then I may be completely misremembering/remembering the O(n**3) part exclusively.     

> __< k​ayabanerve:matrix.org >__ (which boog900 removed)     

> __< k​ayabanerve:matrix.org >__ Apologies if so, glory to the flamegraph     

> __< k​ayabanerve:matrix.org >__ https://github.com/kayabaNerve/fcmp-plus-plus/blob/develop/crypto/divisors/src/poly.rs     

> __< k​ayabanerve:matrix.org >__ In that case, this file     

> __< j​berman:monero.social >__ div_rem is the really slow one. I'll upload a flamegraph for prove in a bit     

> __< k​ayabanerve:matrix.org >__ Urgh. I recommended wasm32v1-unknown. That means build, tests pass with 1.69 but bench with 1.84. That's wonky.     

> __< k​ayabanerve:matrix.org >__ (We support platforms which complain with more modern Rusts due to choice of linker. Instead of spending the time correcting cross-compilation, I just bound Rust support to the mutually agreeable 1.69. People *should* build with a modern Rust, not just for the hell of it, but perf improved by 20% for whatever codegen reasons).     

> __< k​ayabanerve:matrix.org >__ (wasm32v1-unknown ensures a lack of variables in the binary, as desired for these benchmarks, but is only available on modern Rust)     

> __< j​berman:monero.social >__ This was the main reason for 1.69 in the first place right? https://github.com/j-berman/monero/blob/23b1b35ba7c7a8e758e1729546b71a9a97291dde/.github/workflows/depends.yml#L98-L100     



# Action History
- Created by: Rucknium | 2025-02-18T22:40:24+00:00
- Closed at: 2025-02-27T17:48:09+00:00
