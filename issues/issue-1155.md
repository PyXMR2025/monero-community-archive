---
title: Monero Research Lab Meeting - Wed 12 February 2025, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1155
author: Rucknium
assignees: []
labels: []
created_at: '2025-02-11T21:29:17+00:00'
updated_at: '2025-02-21T17:08:31+00:00'
type: issue
status: closed
closed_at: '2025-02-21T17:08:31+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Prize contest to optimize some FCMP cryptography code](https://github.com/j-berman/fcmp-plus-plus-optimization-competition/tree/3da4c0f39b80afdc2ab46b1b143e333f63b82d1b/ec-divisors-contest).

6. Research on [subnet deduplication for peer selection](https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf) to reduce spy node risk.

7. Any other business

8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1152 

# Discussion History
## Rucknium | 2025-02-14T16:21:33+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1155     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ *waves*     

> __< rbrunner >__ Hello     

> __< a​rticmine:monero.social >__ Hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: I posted a draft of the "Subnet Deduplication for Monero Node Peer Selection" research note: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< j​berman:monero.social >__ I'm nearly done setting up tests for the FCMP++ optimization competition. Link: https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ There are some lingering questions I'm still working through:     

> __< j​berman:monero.social >__ - Benchmarking helioselene (how best to score it considering distinct ops have different expected execution times)     

> __< j​berman:monero.social >__ - wasm cycle counting for ec divisors (for an unknown reason I'm getting distinct wasm cycle counts across runs)     

> __< j​berman:monero.social >__       

> __< j​berman:monero.social >__  By next week, I'm aiming to have a finalized repo ready for review. Once reviewed, we can move forward with launching the contest     

> __< v​tnerd:monero.social >__ Code reviews, going to target those selsta has listed for 0.18 but need response     

> __< r​ucknium:monero.social >__ 3) Prize contest to optimize some FCMP cryptography code. https://github.com/j-berman/fcmp-plus-plus-optimization-competition     

> __< j​berman:monero.social >__ See above for an update on where it stands     

> __< j​berman:monero.social >__ Also, I recalled the initial meeting where discussed prize payouts. kayabanerve estimated 3 weeks of work for ec-divisors, and significantly less than that for helioselene optimizations. That was the original reasoning for the payouts chosen     

> __< j​berman:monero.social >__ That's worth taking into consideration when weighing the prize payouts that we didn't fully weigh when bumping the amounts     

> __< rbrunner >__ "significantly less than that". You mean somebody works e.g. only for a week and half, from start to finish and submission? Isn't that quite optimistic?     

> __< j​berman:monero.social >__ I don't know as well as kayabanerve so I would defer to their estimate. But my guess is it may just be a matter of implementing specific arithmetic that someone with prior expertise on curve arithmetic could churn out quickly     

> __< rbrunner >__ Ok     

> __< j​berman:monero.social >__ For reference, the originally proposed payouts were ec-divisors 1st: 150, 2nd: 75 and helioselene 1st: 50, 2nd: 25     

> __< j​berman:monero.social >__ The "bumped" proposed were ec-divisors 1st: 500, helioselene: 200     

> __< j​effro256:monero.social >__ Howdy, sorry I'm late     

> __< j​berman:monero.social >__ So, anyone have thoughts on 500 XMR for 3 weeks of work from a number of competitors -> 1st place ec-divisors, 200 XMR for less work than that for helioselene?     

> __< rbrunner >__ Maybe go for the middle between the old and the new prizes :)     

> __< rbrunner >__ Say if I am really a capacity in such stuff, and have to take into account that I work for naught because somebody else wins, I imagine I need some good offer before I lift a finger, so to say     

> __< j​berman:monero.social >__ So how bout 300 XMR for ec-divisors, 100 XMR for helioselene     

> __< rbrunner >__ That's what crossed my mind, as a compromise, yes     

> __< j​berman:monero.social >__ Ok, will pencil that as the latest proposed prize payouts     

> __< j​berman:monero.social >__ And will hopefully have a finalized draft by next week ready for review. Will try to have it ready 1-2 days before the meeting     

> __< j​effro256:monero.social >__ It's always easy to spend other's money, so I think we should aim low, and in the case that we need to drum up more support, we can raise it again later     

> __< r​ucknium:monero.social >__ I can offer this quick-searched economics research paper: https://www.chapman.edu/ESI/wp/Sheremeta-Winner-Take-All.pdf     

> __< r​ucknium:monero.social >__ > This study provides a unified theoretical and experimental framework in which to compare three canonical types of competition: winner-take-all contests won by the best performer, winner-take-all lotteries where probability of success is proportional to performance, and proportional-prize contests in which rewards are shared in proportion to performance. We introduce random noise<clipped message     

> __< r​ucknium:monero.social >__  to reflect imperfect information, and collect independent measures of risk aversion, other-regarding preferences, and the utility of winning a contest. The main finding is that efforts are consistently higher with winner-take-all contest.     

> __< rbrunner >__ There *always* is a good paper, lol     

> __< r​ucknium:monero.social >__ jberman: Could you enable GitHub issues on the repo so that minor issues could be raised and resolved that way? I see a few.     

> __< j​berman:monero.social >__ done     

> __< r​ucknium:monero.social >__ Thanks! IIRC, when repos on GitHub are forked, issues are disabled by default.     

> __< j​berman:monero.social >__ I haven't updated the root readme yet fwiw     

> __< j​berman:monero.social >__ jeffro256: so basically something like: we go with initial estimates, if after 1 month of the competition being open, we have < n submissions, we bump the prize payouts?     

> __< r​ucknium:monero.social >__ I'm not sure it's a good idea to do that     

> __< j​effro256:monero.social >__ It would have to be an in-the-moment decision I feel like. Because we may only have 3 submissions, but all of them are really really solid     

> __< j​effro256:monero.social >__ Or we may have 15 bad entries     

> __< r​ucknium:monero.social >__ If we have bad entries, the minimum "bid" should be designed to exclude them     

> __< r​ucknium:monero.social >__ of 20%     

> __< j​berman:monero.social >__ I'm still not convinced we should have a 2nd place prize. So totaling 150+75 = 225, rounded to 250 XMR for ec-divisors. And 50+25=75, rounded to 100 XMR for helioselene. Seems like a reasonable estimate to kick off, and we have the option to bump if needed     

> __< r​ucknium:monero.social >__ From just reading the abstract of that paper I found in five seconds, it appears that a single winner-take-all prize will generate more effort from the programmers, which is good for Monero.     

> __< j​berman:monero.social >__ Some more reasoning for not having a 2nd place was that since we're allowing anon submissions, the winner could potentially slyly modify their impl to get both 1st and 2nd     

> __< j​berman:monero.social >__ I'm ok to move to next topic unless there are more thoughts     

> __< r​ucknium:monero.social >__ 4) Research on subnet deduplication for peer selection to reduce spy node risk. https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/monero-peer-subnet-deduplication.pdf     

> __< r​ucknium:monero.social >__ I posted this draft research note ^     

> __< r​ucknium:monero.social >__ The new results compared to the discussion last meeting are treemap plots of spy nodes and honest nodes and their subnet groupings, on pages 5 and 6.     

> __< r​ucknium:monero.social >__ The paper has the mathematical explanation and basic game theory of why the choice of best peer selection algorithm depends on the price premium of subnet-distinct IP leasing vs. leasing whole subnets and the concentration of honest nodes in subnets.     

> __< r​ucknium:monero.social >__ The game theory isn't completely rigorous yet (it's missing a comparison of all cases).     

> __< r​ucknium:monero.social >__ The next steps on this may be to research what the actual price premium is, since we already have the honest node subnet concentration in the current Monero network.     

> __< r​ucknium:monero.social >__ And also modeling how some honest nodes may get more inbound connections, and some less, because of the proposed new peer selection rules. That depends on how many "unreachable" nodes with closed ports are operating on the network     

> __< r​ucknium:monero.social >__ And I think before this new algorithm would be deployed on mainnet (if deemed an improvement), Monero's white_list/address book processes could be reviewed for problems. BTC has had a number of vulnerabilities in its address book processes, including at least one that was exploited in the wild.     

> __< r​ucknium:monero.social >__ In that review, raising the default white_list and grey_list limits (1000 and 5000 now AFAIK) could be considered, too.     

> __< r​ucknium:monero.social >__ Right now my models do not take into account those limits. I don't know if they would have a big effect     

> __< r​ucknium:monero.social >__ This type of subnet deduplication logic could be applied to Autonomous Systems instead, but the code implementation of that is more complicated, with more potential for technical debt IMHO.     

> __< j​effro256:monero.social >__ All of the considerations we have to take into account to group and select outgoing connections is reminding me a lot of the dense decoy selection logic     

> __< s​yntheticbird:monero.social >__ PTSD     

> __< r​ucknium:monero.social >__ boog900: could you make a PR to add this: https://gist.github.com/Boog900/5e9fe91197fbbf5f5214df77de0c8cd8     

> __< r​ucknium:monero.social >__ in https://github.com/Rucknium/misc-research/tree/main/Monero-Peer-Subnet-Deduplication/code/Rust     

> __< r​ucknium:monero.social >__ and give it an open source license?     

> __< r​ucknium:monero.social >__ IMHO, the subnet deduplication is pretty simple. But that's easy for me to say I guess     

> __< r​ucknium:monero.social >__ AFAIK, there is already something like subnet deduplication in the code, but to eliminate multiple ports on the same IP address.     

> __< a​ntilt:we2.ee >__ do you see a way to offload this logic from monerod ? It is simple now....     

> __< r​ucknium:monero.social >__ If used against the current spy node adversary, subnet deduplication reduces privacy risk by an order of magnitude.     

> __< r​ucknium:monero.social >__ From 33 percent to 2.5 percent     

> __< b​oog900:monero.social >__ Sure     

> __< s​yntheticbird:monero.social >__ there are no reason not to try. Afaiu there is nothing indicating that under adversary coordination they could (with the same number of nodes) achieve higher coverage percentage     

> __< s​yntheticbird:monero.social >__ in other words: they can't use that improvements against us     

> __< r​ucknium:monero.social >__ boog900: Thanks!     

> __< r​ucknium:monero.social >__ In the research note I give the specific conditions that would give an adversary an advantage in the subnet deduplication peer selection algorithm, compared to the status quo. Probably, those conditions are not satisfied in real life since an adversary would have to lease thousands of IP addresses all in distinct /16 subnets at a cheap price.     

> __< j​effro256:monero.social >__ If the visualization is correct, the many number of very small block-border boxes is good news for this scheme     

> __< r​ucknium:monero.social >__ Specifically, the price per IP address would have to be less than 38 percent higher than what they get from bulk leasing /24 subnets from a few providers     

> __< r​ucknium:monero.social >__ jeffro256: Yes, exactly. I made the plots as a visual check on the simulations and mathematics logic.     

> __< r​ucknium:monero.social >__ I'm glad that the treemap made sense :D     

> __< j​effro256:monero.social >__ It's a great visualization NGL     

> __< j​effro256:monero.social >__ I don't think I've seen anyone else actually breakdown the decentralization of the Monero network layer over IPv4 before     

> __< j​effro256:monero.social >__ Really interesting     

> __< r​ucknium:monero.social >__ For people who don't want to open the PDF, the plot is here: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/images/treemap-status-quo.png     

> __< r​ucknium:monero.social >__ An here's what happens when honest nodes use a subnet deduplication peer selection algorithm: https://github.com/Rucknium/misc-research/blob/main/Monero-Peer-Subnet-Deduplication/pdf/images/treemap-16-subnet-deduplication.png     

> __< r​ucknium:monero.social >__ Note that these are nodes that accept inbound connections (i.e. have open ports). Nodes with closed ports are not represented in this data.     

> __< c​haser:monero.social >__ one reason to consider if it's really worth it (do market research on to see if the prices satisfy the 38% condition) is not to have to modify the logic again if they (LinkingLion) turn nimble and change their strategy     

> __< r​ucknium:monero.social >__ But these are the ndoes that matter for Dandelion++ privacy since the stem phase tx relay occurs on connections to these nodes     

> __< r​ucknium:monero.social >__ I hope my explanation of how IP addresses work in the Background section is correction. Inform me of any corrections.     

> __< r​ucknium:monero.social >__ Any other agenda items?     

> __< j​effro256:monero.social >__ All of it seemed correct to my knowledge     

> __< r​ucknium:monero.social >__ We can end the meeting here. Thanks everyone.     

> __< j​effro256:monero.social >__ Thanks Rucknium     

> __< a​rticmine:monero.social >__ Thank     

> __< a​rticmine:monero.social >__ I will post later on the IP address issue     

> __< a​rticmine:monero.social >__ I would start by applying the sub net  duplication to /24 or class C. So an attacker would need to lease an entire class C to get one usable spy node. That is a factor of 254.      

> __< a​rticmine:monero.social >__ /16 or class B is far more aggressive since that could catch small towns certain VPNs etc. in the net.     

> __< a​rticmine:monero.social >__ One thing to keep in mind here is that leasing Sub C IP address ranges is in the realm of. retail and far more expensive     

> __< j​effro256:monero.social >__ Perhaps if the node is suffering from a peer deficiency, it should not aggregate as much, but if it has an abundance of /16 subnets to choose from (more than its outgoing connection count), it should be deduplicating anyways, right? If I can choose 3 peers from A, B, C towns, or 3 peers from D town, I should go for A, B, and C, yeah?     

> __< j​effro256:monero.social >__ Unless we're talking about trying to maximize locality for transaction propagation speeds     


# Action History
- Created by: Rucknium | 2025-02-11T21:29:17+00:00
- Closed at: 2025-02-21T17:08:31+00:00
