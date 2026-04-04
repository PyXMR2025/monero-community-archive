---
title: Monero Research Lab Meeting - Wed 23 October 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1098
author: Rucknium
assignees: []
labels: []
created_at: '2024-10-22T19:26:41+00:00'
updated_at: '2024-10-31T16:04:37+00:00'
type: issue
status: closed
closed_at: '2024-10-31T16:04:37+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Monero Research Computing Server hardware needs.

4. Reviving the [MRL research bulletin/technical note paper series](https://www.getmonero.org/resources/research-lab/).

5. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html). Reviews for [Carrot](https://github.com/jeffro256/carrot/blob/master/carrot.md).

6. [Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`](https://github.com/monero-project/research-lab/issues/125)

7. CCS proposal: [Audit monero-serai and monero-wallet](https://gist.github.com/kayabaNerve/3723d0a3f2b62ef8ef00c0c4a574fb8e)

8. Any other business

9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1092 

# Discussion History
## Rucknium | 2024-10-24T16:41:26+00:00
Logs


> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1098     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< rbrunner >__ Hello     

> __< b​oog900:monero.social >__ Hi     

> __< j​effro256:monero.social >__ Howdy     

> __< j​berman:monero.social >__ *waves*     

> __< v​tnerd:monero.social >__ Hi     

> __< s​yntheticbird:monero.social >__ Hello     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: Reviewing Cypher Stack's draft paper on churning. And OSPEAD.     

> __< j​berman:monero.social >__ me: continuing fcmp++ wallet sync building the curve tree locally     

> __< k​ayabanerve:matrix.org >__ FCMP++, solved the data-flow for multi-input proofs, started on evaluating if it's constant time for prior proposed optimization contest. Will propose 8/4 max_in/max_out without strongly holding that opinion.     

> __< k​ayabanerve:matrix.org >__ Also fixing bugs in multi-input proving  and aligning the verifier for the multi-input case.     

> __< v​tnerd:monero.social >__ me: completed LWS /get_random_outs async conversion, and cleaning up LWS http client async conversion     

> __< r​ucknium:monero.social >__ kayabanerve: "Will propose 8/4 max_in/max_out without strongly holding that opinion." Can this go on next meeting's agenda?     

> __< k​ayabanerve:matrix.org >__ Rucknium: It can be left as the heads up I just made, briefly discussed under the FCMP++ topic, or kicked. I'd prefer to establish the premise today (without in-depth discussion) to leave people to consider it for next meeting but leave time considerations to you.     

> __< k​ayabanerve:matrix.org >__ I'll also write a note on GH and we can use that for async discussion.     

> __< r​ucknium:monero.social >__ Ok. Make your pitch for it today during the FCMP++ item and it can be discussed next meeting     

> __< r​ucknium:monero.social >__ 3) Monero Research Computing Server hardware needs.     

> __< r​ucknium:monero.social >__ gingeropolous, who manages the Monero Research Computing Cluster/Server, says this: "There are some nice 2x epycs on ebay that come without ram for $4k, and im debating grabbing one and opening a CCS to get a massive amount of ram on it. I think i could get 2TB for around $5k."     

> __< r​ucknium:monero.social >__ Right now MRCC has a machine with 256GB of RAM. Routinely I alone am using about 200GB of RAM on that machine to analyze ring data. We have lots of swap to prevent out-of-memory problems, but swap is much less performant than RAM. If Monero were staying with rings much longer and/or raising ring size to 40 for black marble defense or even 128+ with Seraphis, then the 2TB of RAM wo<clipped message     

> __< r​ucknium:monero.social >__ uld make a lot of sense.     

> __< r​ucknium:monero.social >__ With current expectations, maybe 2TB is not an efficient choice, but 1TB for 2500 USD may make sense. In addition to usual analysis of the blockchain data, in the near future we also may want to do large-scale P2P network simulations that could take up a lot of RAM.     

> __< k​ayabanerve:matrix.org >__ Sounds perfect, thank you.     

> __< r​ucknium:monero.social >__ Thoughts on this idea?     

> __< s​yntheticbird:monero.social >__ 3000$ for 2TB is an insane deal.     

> __< s​yntheticbird:monero.social >__ insane in the good sense     

> __< r​ucknium:monero.social >__ It's 5000 USD for 2TB     

> __< s​yntheticbird:monero.social >__ 5000$ 1 Epyc + 2TB     

> __< rbrunner >__ I think such a CCS would fill in no time because it makes sense     

> __< s​yntheticbird:monero.social >__ or 5000$ the 2 TB     

> __< k​ayabanerve:matrix.org >__ I don't want to trash the idea of having a very powerful computer around, yet what other tasks are running on it currently/presumably in the future?     

> __< r​ucknium:monero.social >__ gingeropolous would cover the cost of the Epyc. Then CCS would cover the cost of the RAM     

> __< s​yntheticbird:monero.social >__ ok even 5000$ for 2TB is good. a CCS should definitely be opened     

> __< r​ucknium:monero.social >__ One can use transparent blockchains' transation graphs to help learn about Monero's, which I have done. For the trasnaction graph analysis itself, the best way I know of is to analyze it with `igraph`, which requires holding the data in RAM     

> __< j​effro256:monero.social >__ At the risk of sounding pretentious and without knowing too much about the computations being performed, it sounds the code needs a data structures person to look at it. How can the ring data be 200GB when the blockchain itself, including all tx proofs, output caches, etc is 200GB?     

> __< r​ucknium:monero.social >__ I don't really disagree, but the cost of labor and capital can be weighed against each other     

> __< r​ucknium:monero.social >__ Cost of data structures person's time vs cost of hardware     

> __< k​ayabanerve:matrix.org >__ jeffro256: obviously it needs to be rewritten in zig to optimize cache locality /sss     

> __< j​effro256:monero.social >__ lol     

> __< r​ucknium:monero.social >__ I know I'm storing it inefficiently, but it's very fast to output the analysis at a moment's notice. No relational tables     

> __< s​yntheticbird:monero.social >__ mamma mia     

> __< j​effro256:monero.social >__ Do you anticipate the hardware requirements to keep going up in the short to medium term with the increase in blockchain size ?     

> __< r​ucknium:monero.social >__ And when you analyze data, often it has to be copied     

> __< k​ayabanerve:matrix.org >__ I don't mind the expense. I still am curious the non-ring tasks being done on this computer. Rucknium themselves has said we stop gaining new data the moment FCMP++s go live. With wallet trees, I wouldn't be surprised if OSPEAD is our final DSA/this research become solely to better understand our historical privacy.     

> __< s​yntheticbird:monero.social >__ May the MRCC be used as the main platform or benchmarking cryptographic implementations ?     

> __< r​ucknium:monero.social >__ SyntheticBird (Fermat is too good to be true): AFAIK, you don't need to hold a lot of data in RAM for that     

> __< j​effro256:monero.social >__ Benchmarking using an AMD EYPC with 1000 GB of RAM might not be useful for most people's use cases     

> __< r​ucknium:monero.social >__ Maybe some other MRCC users could comment, who aren't here right now. e.g. xmrack xmrack  and isthmus     

> __< s​yntheticbird:monero.social >__ Rucknium: ah yes certainly. I thought kayabanerve was saying that even the actual computer would have no usefulness     

> __< s​yntheticbird:monero.social >__ for non-ring tasks     

> __< rbrunner >__ So maybe aim a bit higher with CPU power and stay within reasonable bounds for memory, i.e. only 1 TB? For approx the same budget     

> __< a​ck-j:matrix.org >__ Hi     

> __< j​effro256:monero.social >__ If they're actually hitting swap frequently, the RAM upgrade will be 100x more cost efficient than upgrading the CPU     

> __< r​ucknium:monero.social >__ xmrack: Sorry to summon you in the middle of a meeting. We are discussing ^     

> __< r​ucknium:monero.social >__ xmrack: And I thought you could help with this question ^     

> __< k​ayabanerve:matrix.org >__ I have a use for a large amount of CPU FYI.     

> __< r​ucknium:monero.social >__ gingeropolous is changing some of the setup now, but there are about five powerful machines if you need access     

> __< k​ayabanerve:matrix.org >__ I have some lengthy CIs. I also am about to comment on how proper constant time testing is slow AF.     

> __< k​ayabanerve:matrix.org >__ I'm not saying there aren't other uses. Solely acting what other uses exist now.     

> __< r​ucknium:monero.social >__ Let's move on for now since the agenda is long. I don't think we have consensus for or against yet, so this item may appear next meeting.     

> __< r​ucknium:monero.social >__ xmrack: you can still give your input as we move on :)     

> __< r​ucknium:monero.social >__ 4) Reviving the MRL research bulletin/technical note paper series. https://www.getmonero.org/resources/research-lab/     

> __< r​ucknium:monero.social >__ I think we should start releasing real papers again instead of stashing them in GitHub repos     

> __< k​ayabanerve:matrix.org >__ FWIW, I lean to for on the server.     

> __< r​ucknium:monero.social >__ Possible papers: The FCMP++ paper, when completed. My black marble flood paper, when completed. My note on classifying real spends using tx uniformity defects.     

> __< a​ck-j:matrix.org >__ I’ve been planning a project on MRCC to use AFL to fuzz for memory corruption bugs but have not had the time to finish writing the harnesses. The epyc cpu would be nice for those  computations. Back when I did my research project I maxxed out the ram on the “Junior” server multiple times while creating my datasets. I dont have any plans for ram intensive tasks at the moment <clipped message>     

> __< a​ck-j:matrix.org >__ but I could see it useful for future research     

> __< r​ucknium:monero.social >__ Junior = the 256GB RAM machine     

> __< k​ayabanerve:matrix.org >__ An open consideration with Veridise is to publish the divisor work in a paper. It has industry-wide implications *and* will earn us free review as others work with it. that's not to mention the PR effects.     

> __< r​ucknium:monero.social >__ Thanks for your input, xmrack     

> __< j​effro256:monero.social >__ So were you finally able to compile fuzz on your machine? What did you change?     

> __< k​ayabanerve:matrix.org >__ The issue is papers cost money.     

> __< r​ucknium:monero.social >__ I think that's great. Get papers out as MRL research bulletins or IACR preprints or in peer-reviewed journals or all three     

> __< k​ayabanerve:matrix.org >__ I don't mind if the FCMP++ paper is hosted by Monero. Publication, even on ePrint (not a conference)? I'd be ashamed.     

> __< k​ayabanerve:matrix.org >__ Here     

> __< r​ucknium:monero.social >__ You'd be ashamed of?     

> __< k​ayabanerve:matrix.org >__ I'm proposing security proofs for FROSTy CLSAG     

> __< k​ayabanerve:matrix.org >__ The original estimate?     

> __< k​ayabanerve:matrix.org >__ 9 months     

> __< r​ucknium:monero.social >__ Oh. Well, yes the peer review process takes lots of time. But you can just post it as a preprint in the meantime and the FCMP research CCS can be considered done     

> __< k​ayabanerve:matrix.org >__ It's only after I clarified I don't want a full paper able for conferences, and solely want security proofs for the signature scheme (not any privacy aspects even), we reached an affordable estimate.     

> __< r​ucknium:monero.social >__ I don't like that we have papers in places that are inaccessible to researchers. koe complained that Halo2/Orchard had sparse docs. I don't want the same to be true with FCMP++     

> __< r​ucknium:monero.social >__ Just put the security proofs in the appendix of the big FCMP++ paper     

> __< k​ayabanerve:matrix.org >__ If someone takes my work and publishes it on eprint, even if legal due to permissive licensing and initially accepted, I'll request it taken down.     

> __< k​ayabanerve:matrix.org >__ It isn't that simple though.     

> __< k​ayabanerve:matrix.org >__ The FCMP++ paper I wrote is a technical manual on implementing the HF for Monero.     

> __< k​ayabanerve:matrix.org >__ It does establish statements for certain aspects, and we have proofs for certain aspects, but it isn't written as an extension of the academically-defined RingCT scheme.     

> __< k​ayabanerve:matrix.org >__ I'd legitimately rewrite it.     

> __< k​ayabanerve:matrix.org >__ I'd take the RingCT paper and note why this work was done. Not only backwards compatibility, yet simplicity and performance, noting the parts eligible for independent interest.     

> __< r​ucknium:monero.social >__ If you look at the MRL research bulletins, especially the early ones, they are not very rigorous and the tone is conversational.     

> __< k​ayabanerve:matrix.org >__ Every single portion would need clear academic definition, and the matching academic commentary. While we have security proofs, they can't simply be copy/pasted. a quality paper needs to marry them.     

> __< r​ucknium:monero.social >__ But anyway kayabanerve  can proceed as he wants with the FCMP written materials. Anyone have any thoughts pro/against myself forming some papers into MRL research bulletins? Or anyone else doing so?     

> __< k​ayabanerve:matrix.org >__ And again, this paper is a how-to for the literal Monero. It isn't an academic work establishing it in a pure sense with independent arguments.     

> __< k​ayabanerve:matrix.org >__ Feel free to publish it on the MRL page of the site.     

> __< r​ucknium:monero.social >__ As a research bulletin?     

> __< rbrunner >__ I think publishing something in this format is a good idea - if the source material lends itself to doing so, without the need to sink massive work into it     

> __< k​ayabanerve:matrix.org >__ If we're solely discussing a paper repository/mailing list, I'm for it and am fine with my works being submitted. Proper papers, ones we'd want to post to eprint/theoretically shop to conferences, would be a massive undertaking.     

> __< rbrunner >__ It also gives credibility to the Monero project as a whole.     

> __< k​ayabanerve:matrix.org >__ Rucknium: "research bulletin" sounds fine to me. ePrint doesn't. While there are specific papers I'd love to see posted there (GBPs, divisors, FROSTy CLSAG), they'd be massive amounts of effort. The only ones I see worth it are GBPs/divisors, with divisors being more feasible.     

> __< rbrunner >__ " ones we'd want to post to eprint/theoretically shop to conferences" The original MRL bulletins weren't thus, right?     

> __< r​ucknium:monero.social >__ Ok great.     

> __< k​ayabanerve:matrix.org >__ I'd be happy to make the proposal for that when the time comes, I just need to be clear it isn't trivial.     

> __< r​ucknium:monero.social >__ There was at least one MRL bulletin that was also an eprint     

> __< k​ayabanerve:matrix.org >__ rbrunner: Correct, but there are MRL papers on ePriint. they're completely distinct in form and tone.     

> __< rbrunner >__ I see     

> __< r​ucknium:monero.social >__ Moving on     

> __< r​ucknium:monero.social >__ 5) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot.  https://github.com/jeffro256/carrot/blob/master/carrot.md https://www.getmonero.org/2024/04/27/fcmps.html     

> __< k​ayabanerve:matrix.org >__ So I support a bulletin, I just want to be clear the line in the sand. I also have a candidate I can propose crossing the line in the sand. It just needs to be noted as such.     

> __< j​effro256:monero.social >__ The CCS for the Carrot Spec Review was fully funded, now just waiting for payout: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/511#note_26837. I have nothing to add otherwise unless Diego Salazar has any updates.     

> __< k​ayabanerve:matrix.org >__ A max outputs of 16 is because a Bulletproof for 17 outputs wastes 15*64 gates (960). A FCMP++ uses 256+128 gates. That means if we have 5 inputs (in a single BP), we use 1280+640 gates, wasting 768+384 (1152).     

> __< d​iego:cypherstack.com >__ Working on it. Should have something to show in a week or two, if not sooner.     

> __< k​ayabanerve:matrix.org >__ This implies per the existing MAX_OUTPUTS, we should limit MAX_INPUTS to 4. I don't support MAX_INPUTS < MAX_OUTPUTS at this time due to the creation rate exceeding accumulation rate (though you can achieve a logarithmic time bound). I also don't support MAX_OUTPUTS < 4. MAX_OUTPUTS = 2 requires perfect planning to make a tree of payments with only a logarithmic delay, and may be <clipped message     

> __< k​ayabanerve:matrix.org >__ incompatible with Carrot as you wouldn't have change outputs in your own TXs.     

> __< j​effro256:monero.social >__ Thanks Diego!     

> __< r​ucknium:monero.social >__ Noob question: How does FCMP change the outputs if FCMP inputs can spend pre-FCMP outputs?     

> __< k​ayabanerve:matrix.org >__ Accordingly, I support MAX_INPUTS = MAX_OUTPUTS = 4, which leads nicely into padding input/output count for privacy reasons. To minimize the disruption of so limiting in/outs at this time, my proposal is 8/4. I'd accept 8/8 as well but I believe the end goal should be 4/4 (or 2/2 if we're extremely aggressive).     

> __< j​effro256:monero.social >__ >  don't support MAX_INPUTS < MAX_OUTPUTS at this time due to the creation rate exceeding accumulation rate (though you can achieve a logarithmic time bound). I also don't support MAX_OUTPUTS < 4.      

> __< j​effro256:monero.social >__ I think this point is moot as long as 1 input is allowed and multiple outputs are allowed. One can always force creation rate to go up exponentially if 1/2 txs are allowed     

> __< k​ayabanerve:matrix.org >__ The output formats are backwards compatible. the only change is the output key of xG is now xG+yT. Historical outputs simply have y=0.     

> __< j​effro256:monero.social >__ Which means we get to start with an anon set of >100M. Yippee!     

> __< k​ayabanerve:matrix.org >__ If you send me 2 ins per TX, I can accumulate 2 ins per TX jeffro256.     

> __< r​ucknium:monero.social >__ Ok so a FCMP tx "needs" to have this additional `yT` because the input was a FCMP proof     

> __< r​ucknium:monero.social >__ We will discuss more next time     

> __< r​ucknium:monero.social >__ 6) Proposal for FCMP++ HF Activation Rule to Retroactively Ignore Future `unlock_time`. https://github.com/monero-project/research-lab/issues/125     

> __< k​ayabanerve:matrix.org >__ No. The FCMP composition defines a yT component. It's needed for certain features (forward secrecy, outgoing view keys). Old outputs simply have it as 0.     

> __< k​ayabanerve:matrix.org >__ I also had a note on constant-time evaluations but if we're keeping this to the hour I guess that's kicked to next meeting?     

> __< j​effro256:monero.social >__ Oh I think see. Someone who's really determined to send you money multiple times can flood you with inputs faster than you con consolidate, assuming you make the same numbers of txs per timeframe?     

> __< k​ayabanerve:matrix.org >__ Are we dissolving the overarching FCMP++ topic for individual line items Rucknium?     

> __< s​yntheticbird:monero.social >__ re: 6) People had enough time to update and avoid using unlock_time. Almost no one uses it. It's really ok to retroactively ignore it.     

> __< k​ayabanerve:matrix.org >__ jeffro256 Yes, but further discussions on the GH write-up I'll make please.     

> __< r​ucknium:monero.social >__ We still have the unlock time item and the Audit monero-serai and monero-wallet item     

> __< k​ayabanerve:matrix.org >__ I left a comment on that issue which speaks my opinion.     

> __< j​effro256:monero.social >__ I wish I had that problem....     

> __< j​effro256:monero.social >__ ;)     

> __< r​ucknium:monero.social >__ Which do you prefer?     

> __< r​ucknium:monero.social >__ Make then individual or keep the overall topic header?     

> __< r​ucknium:monero.social >__ I wanted the unlock time to be individual since I wanted community members to know that unlock time was on the agenda     

> __< k​ayabanerve:matrix.org >__ It's probably better, if we're now keeping meetings tight, to do explicit line items because then we can better evaluate the timing of it.     

> __< r​ucknium:monero.social >__ The unlock time thing will probably only be an issue if a malicious party tries to spam them. But because the malicious party knows that they can be retroactively deprecated at a certain height, the best move of the adversary is probably to not bother with the effort.     

> __< k​ayabanerve:matrix.org >__ It also would prevent a Carrot update at the same time as a MAX_IN/OUT discussion at the same time on my notes on constant-time testing methodology and keep the current topic clearer.     

> __< r​ucknium:monero.social >__ Ok sure. Then please give me specific wording for agenda items you want before the meeting. That goes for anyone     

> __< rbrunner >__ That's an interesting stand-off then. Probably nobody will bother to spam locked txs because they know we will "retaliate" with retro-active cancels     

> __< k​ayabanerve:matrix.org >__ So yes, I'll advocate explicit line items. I'll ask carrot be split into its own topic now and consider what I want for next week myself.     

> __< j​effro256:monero.social >__ A max number of outputs of 2 would be fine I think, as long as you decide to either split/consolidate OR transfer, but not both in the same tx. LIke you mentioned, you would also have to plan perfectly in advance     

> __< rbrunner >__ But at least we have to make clear that we would act if somebody started to spam, to make a credible "threat", IMHO     

> __< rbrunner >__ If we have consensus of course     

> __< r​ucknium:monero.social >__ Thanks, jeffro256 , for writing up the proposal in a clear and detailed manner     

> __< k​ayabanerve:matrix.org >__ jeffro256: "further discussions on the GH write-up I'll make please"     

> __< r​ucknium:monero.social >__ The proposal sounds good to me. But it's unavoidably incomplete since the time to decide the future deprecation date is...some time next year I guess     

> __< k​ayabanerve:matrix.org >__ We can say new year's.     

> __< r​ucknium:monero.social >__ I guess it would be decided when the FCMP hard fork date is decided     

> __< k​ayabanerve:matrix.org >__ Clean, simple, easy to remember.     

> __< j​effro256:monero.social >__ We could decide now, sooner is better than later     

> __< j​effro256:monero.social >__ TBC, the decision date being sooner is better, the value of the decided height doesn't have to be *sooner*     

> __< j​berman:monero.social >__ +1 thank you for the writeup jeffro256     

> __< rbrunner >__ Well, announcing any measure, with any weight, has a possible price, IMHO: It gives other people opportunity to badmouth us. Doing nothing unless somebody acts first with spamming does not have that cost     

> __< rbrunner >__ *with any height     

> __< rbrunner >__ The "not centralized" trope.     

> __< rbrunner >__ Which can make us *appear* bad in the eye of many people.     

> __< j​effro256:monero.social >__ I propose the ignore data be targeted for Easter 2025 April 20th, about six months from the current date in the spirit of past hard fork turnaround times     

> __< k​ayabanerve:matrix.org >__ I'm explicitly against that.     

> __< k​ayabanerve:matrix.org >__ Can we adjust to May 1st?     

> __< k​ayabanerve:matrix.org >__ The date should be clean and without reasons to nit it. When asked why that date, I think the 6 month reasoning is fine, yet Christianity is a poor option to enshrine.     

> __< r​ucknium:monero.social >__ May 1st sounds fine to me. Someone can comment that on the issue, but make it extremely clear that it is _not_ the actual hard fork date, wince people can get confused with rumors. Then in the near future that date can be finalized     

> __< j​effro256:monero.social >__ rbrunner: I'd rather people be aware ahead of time that `unlock_time` is planning to be deprecated, even if doesn't really take effect unless they merge FCMP++ code into their node     

> __< j​effro256:monero.social >__ The alternative is letting this detail of the FCMP++ fork be a surprise     

> __< rbrunner >__ FCMP++ does not support locks, right? As a totally not-surprise?     

> __< r​ucknium:monero.social >__ In case anyone did not read my comment on the issue: nonzero unlock_time txs are definitely being confirmed on the blockchain despite the tx relay rules. But only one actually had any locking effect, and it was only locked for 24 hours. Probably some fingerprintable wallet implementation is making non-binding unlock_times     

> __< j​berman:monero.social >__ Another alternative is not setting an explicit date, but announcing that the action to deprecate timelocks is proposeed as part of the FCMP++ fork with an unsettled date     

> __< k​ayabanerve:matrix.org >__ It will require unlock_time 0 rbrunner.     

> __< rbrunner >__ Yes, and we tell that frankly? I don't get the "surprise" part of jeffro256's argument.     

> __< s​yntheticbird:monero.social >__ I agree with jeffro256 users needs to be informed     

> __< r​ucknium:monero.social >__ There have been comments on GitHub that the relay rules were a surprise     

> __< j​berman:monero.social >__ I have a related comment: I just benchmarked wallet-side tree building on a 16-thread snappy cpu. Sync from genesis took 6 hours versus ~45 mins without tree building     

> __< r​ucknium:monero.social >__ Some GitHub commentators like unlock_time (even if they apparently use it very little according to the blockchain data)     

> __< rbrunner >__ We would tell "At FCMP++ hardfork height new locks are no more. If somebody starts to spam, we will make them invalid retroactively at FCMP++ hardfork time"     

> __< j​berman:monero.social >__ There's a lot of room for optimizing tree building (optimize arithmetic on helios/selene, get CPU utilization up from 10-30% closer to 100%)     

> __< k​ayabanerve:matrix.org >__ Bah. I also meant to cite my existing commentary on Curve Forests during the FCMP++ topic to cause awareness D:     

> __< j​effro256:monero.social >__ Eh 1st of the month defined in a Gregorian calendar is just as arbitrary, if not more so, but I'm fine with May 1st if its more politically correct     

> __< rbrunner >__ Oh, gives time to spam between release of the fork-ready software and the actual hardfork ...     

> __< k​ayabanerve:matrix.org >__ Rucknium: They like the idea of it.     

> __< j​berman:monero.social >__ However at this point I wouldn't fully discount the possibility that it might end up faster in most circumstances to just download the tree instead of rebuild it     

> __< k​ayabanerve:matrix.org >__ rbrunner: that still allows spam from date of HF binary release cut to date of fork.     

> __< rbrunner >__ Yes :)     

> __< r​ucknium:monero.social >__ "A Plea to Restore a Crucial Feature in XMR"  https://github.com/monero-project/monero/pull/9151#issuecomment-2365480992     

> __< k​ayabanerve:matrix.org >__ jberman: If you're not CPU bottlenecked, how will faster helioselene code help?     

> __< rbrunner >__ Unfortunate.     

> __< r​ucknium:monero.social >__ AFAIK, the proposed alternative to unlock_time is "off-chain" time-locked puzzles, which current devs and researchers don't have time to research/implement     

> __< rbrunner >__ rucknium: Right, but a pretty lone voice, as far as I remember and saw on the subreddit.     

> __< j​berman:monero.social >__ It is CPU bottlenecked currently, it may not be with optimal implementation     

> __< k​ayabanerve:matrix.org >__ jeffro256: It isn't just as arbitrary. One date was a religious holiday proposed because it's a religious holiday. One is an effectively universal start of a new period of time to 99% of the world.     

> __< k​ayabanerve:matrix.org >__ jberman: That reopens discussions of putting the tree root in the header.     

> __< k​ayabanerve:matrix.org >__ There is existing research.     

> __< j​effro256:monero.social >__ rbrunner: Sorry maybe I misunderstood your original comment. I thought you proposing doing the ignore height, but just not announcing which one it would be until we finalize the FCMP++ code     

> __< k​ayabanerve:matrix.org >__ No one implements them because they suck and no one actually wants to use them.     

> __< r​ucknium:monero.social >__ May 1st is also a holiday. But I don't think that's a reason not to do May 1     

> __< k​ayabanerve:matrix.org >__ How is it CPU bottlenecked if you aren't maxing out a CPU core? 🤔     

> __< rbrunner >__ The Monero subreddit has over 300,000 readers the way Reddit counts them, and yet nobody shows up and wants locks back, with very very rare exceptions     

> __< k​ayabanerve:matrix.org >__ But ACK, it is CPU bottlenecked.     

> __< j​berman:monero.social >__ If the CPU was faster, it would go faster     

> __< k​ayabanerve:matrix.org >__ Rucknium: That's not the reason I proposed it. I was unaware. What's it happen to be in what locality?     

> __< k​ayabanerve:matrix.org >__ Is it... Veteran's Day in the US?     

> __< k​ayabanerve:matrix.org >__ Or labor day?     

> __< rbrunner >__ Yes, Labor day.     

> __< c​haser:monero.social >__ international abor day     

> __< k​ayabanerve:matrix.org >__ Oh, it's international worker's day also known as labor's day.     

> __< k​ayabanerve:matrix.org >__ *labor day     

> __< j​berman:monero.social >__ The reason I bring it up now is because if tree building is sub-optimal compared to downloading, then the reasoning to support unlock time on account of wallet side tree building may end up moot     

> __< rbrunner >__ Alright, May 1 sounds good to me. But we could still agree on a "threat" to go even earlier if somebody starts to spam tomorrow. Or not?     

> __< r​ucknium:monero.social >__ Is tobtoht  here?     

> __< k​ayabanerve:matrix.org >__ Cool. I kinda wish that was the reason I proposed it now.     

> __< tobtoht_ >__ Hi     

> __< k​ayabanerve:matrix.org >__ Agreed not to set in stone in case of spam.     

> __< r​ucknium:monero.social >__ I agree on threat idea.     

> __< r​ucknium:monero.social >__ Dear adversary, I hope you heard that     

> __< rbrunner >__ Lol     

> __< rbrunner >__ Maybe make that plural     

> __< r​ucknium:monero.social >__ 7) CCS proposal: Audit monero-serai and monero-wallet https://gist.github.com/kayabaNerve/3723d0a3f2b62ef8ef00c0c4a574fb8e     

> __< j​berman:monero.social >__ I generally agree with rbrunner too     

> __< k​ayabanerve:matrix.org >__ I did post a link to the documentation and wrote out the wallet2 + monero-wallet multisig idea. I'll leave tobtoht to speak on the latter.     

> __< k​ayabanerve:matrix.org >__ For rbrunner's questions of what this lib is, I'd hope the linked documentation has let them explore the functionality of it.     

> __< tobtoht_ >__ Kaya followed up last week's discussion with a plausible path towards wallet2 integration (https://gist.github.com/kayabaNerve/3b2c648c623bc4ce4ca288725428ea76), which would make it useful to a wider range of projects. I wasn't able to dive into this yet, but I think it's worth exploring.     

> __< k​ayabanerve:matrix.org >__ I'll also note my prior estimate was 750 XMR - 1000 XMR (I'm still waiting on the final quote :( ) but that estimate holds. MRL is being asked their opinion on if auditing monero-wallet is sufficiently worthwhile to be posted as a CCS. It is not being proposed as wallet3/a sole option for Monero multisig.     

> __< k​ayabanerve:matrix.org >__ *that estimate of mine is still one I personally believe accurate/likely.     

> __< r​ucknium:monero.social >__ IIRC, tobtoht  wanted to open a discussion of software supply chain security with Rust     

> __< rbrunner >__ I thought about it, and I don't see any plausible reason to oppose a CCS. I think it's fine to let donors decide whether they see it worth their donation.     

> __< j​berman:monero.social >__ I'll explicitly correct myself from last week as well: integrating monero-wallet / monero-clsag with wallet2 actually does not seem as involved as I originally thought, since it appears plausible to reuse the view-only wallet2 wallet to manage wallet state (with some explict UI changes for multisig) / the cold signing flow (replacing cold signing in wallet2 with using monero-wallet)     

> __< r​ucknium:monero.social >__ I think I support this, but it would be much easier to support if it wasn't so expensive. But I know it cannot be done cheaper     

> __< k​ayabanerve:matrix.org >__ I can note how I did work to minimize dependencies in monero-serai/monero-wallet. They're also piecemeal. You can use monero-clsag for CLSAG multisig without ever touching monero-wallet (and any additional dependencies that brings). This isn't a topic I'm flippant on and do consider.     

> __< r​ucknium:monero.social >__ And the case for the multisig part alone is much stronger than for the whole proposal. But the case for the whole proposal still may be strong     

> __< rbrunner >__ Might need some good explanation what the CCS is about, as much more often CCS proposals are about building something. Here it's built already, possible misunderstanding.     

> __< k​ayabanerve:matrix.org >__ Rucknium: I can ask for the quote for the nine months of work proposal I cut down from if you'd like to feel you're saving money :D     

> __< c​haser:monero.social >__ it isn't cheap, but given the fact that we will finally get usable multisig in Monero after 10-11 years, it's not expensive either.     

> __< rbrunner >__ Ah, the 9 months were the time to review the libraries? 9 months of more or less fulltime work? Maybe I misunderstand.     

> __< k​ayabanerve:matrix.org >__ Usable, _proven secure_ multisig :D     

> __< k​ayabanerve:matrix.org >__ No, when I originally asked for proving FROSTy CLSAG, a full paper on it for conference submission was estimated to be nine months of work.     

> __< k​ayabanerve:matrix.org >__ I brought this up during Rucknium's research bulletin topic.     

> __< rbrunner >__ We only get that multisig if it's in wallet2, seems to me, and with a really usable UI/UX - which is still much work     

> __< rbrunner >__ Ah, ok, so misunderstanding     

> __< k​ayabanerve:matrix.org >__ I cut it down to just the necessary security proofs (eligible for a research bulletin, not eligible for conference submission). This scope of work is much smaller and will not take nine months.     

> __< rbrunner >__ But of course it all starts with the libraries as the biggest part     

> __< k​ayabanerve:matrix.org >__ I can ask for the quote for hiring Cypher Stack for several months however so this quote seems small in comparison though :p     

> __< r​ucknium:monero.social >__ This is about two days of tail emission :D     

> __< k​ayabanerve:matrix.org >__ I'm joking about it, but I do understand this is a very large ask. I wrote a paragraph attempting to justify it by the fact I never charged for my labor on building these libs in the first place (and I'm fine committing to no retroactive CCSs for monero-serai), the Cuprate CCS, and the benefit present.     

> __< k​ayabanerve:matrix.org >__ I'll note the Cuprate CCS have raised more than my estimate.     

> __< j​berman:monero.social >__ Disclosure again: I sometimes get paid to work on monero-wallet. I also +1 the porposal for similar reasons: this is imo the strongest path forward for a secure Monero multisig     

> __< rbrunner >__ Heck, more or less the only one on the table     

> __< rbrunner >__ The work that the "old" solution would need is donwright scary; I think koe detailed it once in a meeting.     

> __< rbrunner >__ I am just afraid we are yet again kicking the can down the road and wait *again* for working multisig ...     

> __< k​ayabanerve:matrix.org >__ That isn't to say the Cuprate CCS are overcharging. It's to put in perspective the Cuprate CCS which have been deemed acceptable over time are more significant than the request here. This just appears grand due to it happening to be at once. While the CCS ability to evaluate over-time (and before the work is done) does grant them influence and privilege, which I've arguably taken <clipped message     

> __< k​ayabanerve:matrix.org >__ away, I still believe I can argue the value is there and concern about the price can be largely argued as shock.     

> __< k​ayabanerve:matrix.org >__ rbrunner: my FCMP++ Development includes multisig AFAIK.     

> __< k​ayabanerve:matrix.org >__ So that won't have a dedicated CCS after the hard fork and we won't have to do this song and dance again ;)     

> __< tobtoht_ >__ rucknium: "IIRC, tobtoht  wanted to open a discussion of software supply chain security with Rust" <- I'm working on a write-up that I will post under #9436. (Again, the intent is to make sure we have the tools / awareness to deal with it, not to NACK.)     

> __< j​effro256:monero.social >__ As it is written, can the`modular-frost` crate be used to do multisig signing on FCMP++ outputs (AKA. opening against 2 independent generators)?     

> __< tobtoht_ >__ Fwiw, I'm in support of getting this audited.     

> __< j​berman:monero.social >__ I don't think this is kicking the can. I think the work to get to secure multisig is significant, and this is that work. This is the opposite of kicking the can imo, it's starting to drink the can     

> __< k​ayabanerve:matrix.org >__ It'll be built on the same libs used here however, so CS doing this audit for their experience and to shore it up remains solid.     

> __< k​ayabanerve:matrix.org >__ jeffro256: It'd only use a single secret. It wouldn't privately open the entire Pedersen Commitment.     

> __< k​ayabanerve:matrix.org >__ Either x is public and y is private, or y is zero and x is private.     

> __< j​effro256:monero.social >__ Okay, makes sense thanks     

> __< k​ayabanerve:matrix.org >__ I prior wrote generic code for GSPs with modular-frost which can be used for either use case. The larger concern would be the BP+ we composed the GSP with. That has x as a secret IIRC...     

> __< k​ayabanerve:matrix.org >__ Ugh. Backwards-compatible multisig may be a thing. I'll review it when I get to it and see how that affects our research needs.     

> __< k​ayabanerve:matrix.org >__ Also, tobtoht, sending you a message on Matrix re: rust versions.     

> __< j​effro256:monero.social >__ And I'm assuming the `modular-frost` would fall under this review, since `monero-wallet` uses it as a dependency for multisig?     

> __< j​effro256:monero.social >__ Oh you mention that it's already audited     

> __< k​ayabanerve:matrix.org >__ Correct, a while ago. I don't believe it's had such notable changes it necessitates a re-audit at this time.     

> __< r​ucknium:monero.social >__ Any more comments on this audit proposal?     

> __< s​yntheticbird:monero.social >__ Do it.     

> __< r​ucknium:monero.social >__ plowsof sent this draft CCS proposal to MRL from #monero-community:monero.social . I see loose consensus at this meeting in favor of https://gist.github.com/kayabaNerve/3723d0a3f2b62ef8ef00c0c4a574fb8e     

> __< r​ucknium:monero.social >__ Of course the final budget is not available. If it changes a lot from the estimate, then maybe it will need more commenting     

> __< k​ayabanerve:matrix.org >__ Great, thank you :) I'll bring it up at the next community meeting, get the final quote, make the CCS, and once it's had a sufficient comment period on GitLab (already having been through the meetings), hope it gets merged :)     

> __< r​ucknium:monero.social >__ Meeting ends here. Thanks everyone!     

> __< s​yntheticbird:monero.social >__ thanks     

> __< j​effro256:monero.social >__ Can `modular-frost` be used in the future to do the wacky `O = (a * s) G + b T` opening for Carrot deferred subaddresses? I'm in favor of the audit, but the price is hard to stomach IMHO. I think the multisig portions of the codebase are of the most value to the community, and are directly applicable and not duplicated efforts for the C++ codebase     

> __< j​effro256:monero.social >__ Would it be possible to split the audits into multisig-related parts of `monero-wallet` and everything else (e.g. tx scanning, tx construction, decoy selection, etc)?     

> __< 0​xfffc:monero.social >__ Thanks everyone     

> __< s​yntheticbird:monero.social >__ ig multisig is the bulk of the work     

> __< j​effro256:monero.social >__ Thanks everyone!     

> __< j​effro256:monero.social >__ Thanks Rucknium again for organizing     

> __< k​ayabanerve:matrix.org >__ We'd open y against T. If you're scaling x, against G, it isn't a concern.     

> __< k​ayabanerve:matrix.org >__ There's some caveat as I have to look into backwards compatible multisig but in general, that is irrelevant.     

> __< k​ayabanerve:matrix.org >__ Public scalar factors can be done. It's just annoying. I have an issue to support them.     

> __< k​ayabanerve:matrix.org >__ Private multiplicative scalars can't be done. You've reinvented Triptych.     

> __< j​effro256:monero.social >__ Oh oops you're right I switched them around     

> __< k​ayabanerve:matrix.org >__ As long as there's only one private scalar, it should be fine. If you introduce two *without a simple additive relationship*, it's an issue.     

> __< k​ayabanerve:matrix.org >__ jeffro256: Technically no, practically no.     

> __< k​ayabanerve:matrix.org >__ We can delineate FROSTy CLSAG proofs, monero-clsag, monero-serai/monero-wallet.     

> __< k​ayabanerve:matrix.org >__ That's bad. monero-wallet has multisig transaction construction code. You can't use the normal transaction construction code.     

> __< k​ayabanerve:matrix.org >__ See the issue I noted in Monero's multisig. One person selected the ephemeral keys, which let them cause reuse of a change one-time key (burning the change output).     

> __< k​ayabanerve:matrix.org >__ We can just audit CLSAG multisig, but we can't just multisig as we do need consideration towards if the TX construction code is secure in a multisig context or not.     

> __< k​ayabanerve:matrix.org >__ Then even if we wanted to split out FROSTy CLSAG formally with monero-clsag, I'd argue that just causes user confusion regarding what they're funding and causes me to ask CS for yet another quote as it now needs to be delineated.     

> __< k​ayabanerve:matrix.org >__ It also wouldn't service Cuprate nor the people building on monero-wallet currently.     

> __< k​ayabanerve:matrix.org >__ And then yes, the CLSAG multisig alone would still be the vast majority so...     

> __< j​effro256:monero.social >__ Thanks for spelling that all out !     

> __< k​ayabanerve:matrix.org >__ https://github.com/monero-project/research-lab/issues/100#issuecomment-2433524326     

> __< k​ayabanerve:matrix.org >__ cc jeffro256 jberman tevador     

> __< r​ucknium:monero.social >__ https://github.com/monero-project/research-lab/issues/100#issuecomment-2433531171     

> __< r​ucknium:monero.social >__ See, with all this RAM, I can do lightning-fast computations ;)     

> __< r​ucknium:monero.social >__ (These tables were produced after an earlier request: https://gist.github.com/Rucknium/d2c02f51a2d9f103a28caa8f51be7dbf  )     

> __< k​ayabanerve:matrix.org >__ can we not just download more ram     

> __< h​ardenedsteel:monero.social >__ does lab at getmonero email still works?     

> __< r​ucknium:monero.social >__ I am not aware of anyone having access to that email account.   



# Action History
- Created by: Rucknium | 2024-10-22T19:26:41+00:00
- Closed at: 2024-10-31T16:04:37+00:00
