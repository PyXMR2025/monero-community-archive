---
title: Monero Research Lab Meeting - Wed 11 September 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1070
author: Rucknium
assignees: []
labels: []
created_at: '2024-09-06T19:49:06+00:00'
updated_at: '2024-09-25T16:21:49+00:00'
type: issue
status: closed
closed_at: '2024-09-25T16:21:49+00:00'
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

5. 10 block lock discussion: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259 , [Monero output lock analysis](https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final)

6. Chainalysis capabilities video.

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1068 

# Discussion History
## Rucknium | 2024-09-11T20:12:42+00:00
Logs

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1070     

> __< j​effro256:monero.social >__ howdy     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< c​haser:monero.social >__ hello     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< b​oog900:monero.social >__ hi     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< k​ayabanerve:matrix.org >__ 👋     

> __< v​tnerd:monero.social >__ Got stuck with some LWS stuff, but back on hackerone stuff     

> __< j​effro256:monero.social >__ me: done getting first proposals back for Carrot audit quotes. DM me if you want to see the proposals and/or my comparison. Also just adding finishing touches and preparing for an implementation PR     

> __< r​ucknium:monero.social >__ me: Some double spend probability analysis for the N blocks lock discussion. Some analysis of issues in the Chainalysis video. Finishing up analysis of node tx relay logs for black marble source detection (preview: it was made very difficult after a code fix in 2019).     

> __< j​berman:monero.social >__ me: fcmp++, implemented trimming the tree on reorg/pop blocks, implemented multithreaded tree building, moving to the key image migration next     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod. https://github.com/monero-project/monero/issues/9348     

> __< r​ucknium:monero.social >__ AFAIK there are no new updates about stressnet     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. Reviews for Carrot. https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< k​ayabanerve:matrix.org >__ I'll raise the question of a consensus rule vs output index binding.     

> __< k​ayabanerve:matrix.org >__ jeffro256: did you form an opinion on which side you prefer?     

> __< 0​xfffc:monero.social >__ ( apologies for being late. Hi everyone )     

> __< j​effro256:monero.social >__ I think I prefer the consensus rule again since implementing output index binding causes an extra round for collaborative protocols anyways, *and* adds the round to normal wallet workflows.     

> __< k​ayabanerve:matrix.org >__ Sorry, how does output index binding add a round to the normal wallet workflow?     

> __< j​effro256:monero.social >__ As long as this rule is well documented, I don't see it being an issue. And anyways, it should be best practice for collaborative protocols to commit-and-reveal their transaction components anyways to prevent any accidental interdependence     

> __< k​ayabanerve:matrix.org >__ The amount commitment doesn't need to bind to the input context. If we share the amount commitment with the key images, there's no complexities to the flow there.     

> __< k​ayabanerve:matrix.org >__ Unless I'm missing something, sorry if I am.     

> __< j​effro256:monero.social >__ You have to do your amount commitment derivations for all enotes first, then sort them within the transaction and assign `output_index`, and then complete the enotes. Whereas without ouput index binding, all enotes are completely derived in parallel and only sorted at the end     

> __< rbrunner >__ Ah, you are talking about internal wallet "workflow"     

> __< k​ayabanerve:matrix.org >__ I'll drop it even though I truly hate the idea of using consensus rules to solve the burning bug.     

> __< j​effro256:monero.social >__ The amount commitment binding to the input context isn't the complication, it's the `output_index` being dependent on a component inside the enote that complicates things for wallet code     

> __< j​effro256:monero.social >__ I did the whole rewrite of Carrot for binding to `output_index` instead of relying on the consensus rule, and it was pretty hairy I gotta say     

> __< k​ayabanerve:matrix.org >__ Can I bully you by pointing out there's a random chance TXs will fail naturally if we use a consensus rule due to the minimized amount of entropy     

> __< k​ayabanerve:matrix.org >__ ... Hm. I wonder that the exact odds of that are. I'm unsure it's as high as 2**64 because there's a pool of n outputs. It may actually be something we as humans would naturally stumble onto...     

> __< j​effro256:monero.social >__ You can bully me lol but what do you mean about the minimized amount of entropy?     

> __< k​ayabanerve:matrix.org >__ We're only using 16 bytes for entropy during the derivations?     

> __< k​ayabanerve:matrix.org >__ If two outputs happen to have the same entropy, they'll trigger this consensus rule and cause a failure? You need to derive entropy and do a uniqueness check prior to doing the full derivations?     

> __< j​effro256:monero.social >__ Is 16 max outputs enough for that effect to be noticeable (assuming we sent all to the same address anyway)? I mean I guess it's technically lower than 128 bits so....     

> __< k​ayabanerve:matrix.org >__ Because I think at best this is a 1/2**64 chance, but the fact it's any 2 of the n outputs in a transaction may reduce that further to the point yes, we do actually need code for that.     

> __< k​ayabanerve:matrix.org >__ I assume the check the entropy is unique before deriving is simple enough to implement tbf.     

> __< j​effro256:monero.social >__ I don't think it's as low as 2**64 since the result space isn't 128 bits, its 256 bits     

> __< k​ayabanerve:matrix.org >__ ... except it only has 16 bytes of entropy?     

> __< k​ayabanerve:matrix.org >__ I'm looking to collide the preimage, not the hash.     

> __< k​ayabanerve:matrix.org >__ Can we move on to whatever other topics we have on the agenda today by at least acknowledging checking the entropy is unique is a viable solution if this is a problem? We can discuss statistics/implementation/how that complexity compares to other complexity later?     

> __< j​effro256:monero.social >__ Yes and 2**64 is the expected value assuming you get as many samples as you want, no? The real probability for a preimage collision in a 16-out tx (assuming your machine's entropy is good) is 1/(2**128-1) * 1/(2**128-2) * 1/(2**128-3) * ... * (1/2**128 - 15)     

> __< r​ucknium:monero.social >__ jeffro256: You wanted to talk about Carrot reviews, right?     

> __< j​effro256:monero.social >__ Oops formatting. Yeah, we can move on. I will look into it for sure     

> __< j​effro256:monero.social >__ https://github.com/jeffro256/carrot/blob/master/carrot.md     

> __< j​effro256:monero.social >__ So I solicited quotes from different auditing firms for the Carrot specification. For all of them, I requested that the general specification be reviewed to find any glaring vulnerabilities, but more concretely, to create security proofs for the security properties in Section 9 (except for Janus resistance). My first question: is this the best way to go about scoping the Carrot au<clipped messag     

> __< j​effro256:monero.social >__ dit in term of what the community needs?     

> __< k​ayabanerve:matrix.org >__ Oh gosh, you may be right this isn't what I was thinking yet is properly defined as a multi-target collision where each new entropy is checked against all existing entropy. That'd be 2**k / n (where n is the amount of already sampled entropy). Sorry if I did botch that.     

> __< k​ayabanerve:matrix.org >__ Your definition for auditing seems reasonable to me *though I haven't reviewed every line item in that section*.     

> __< rbrunner >__ Why the exception for Janus resistance?     

> __< rbrunner >__ If that can be explained in some simple terms :)     

> __< k​ayabanerve:matrix.org >__ I ask the same question but without the "if" 👀     

> __< j​effro256:monero.social >__ I got some feedback that Janus attack resistance might be slightly harder to prove, which might raise costs     

> __< j​effro256:monero.social >__ I asked for a less formal review of Janus resistance, but that can certainly be upgraded if desired     

> __< rbrunner >__ Well, lately donors were extremely generous. At least some of them, it seems. Maybe if do all that effort, spending some more might still be worth it     

> __< j​effro256:monero.social >__ It does take up a good chunk in the number of steps in the enote scan process, so it might be worth reviewing more formally just because of that complexity     

> __< j​effro256:monero.social >__ Okay I will inquire into that and report on it when that information becomes available     

> __< j​effro256:monero.social >__ Second note: The most expensive firm which responded had a quote 5x higher than the cheapest firm. On the one hand, they valued their man-hours at about 2.5x higehr rate than the cheapest firm, so they were likely going to be more expensive regardless. However, they also estimated the number of man-hours required to be 2x than the cheapest firm. One of these firms is probably misg<clipped messag     

> __< j​effro256:monero.social >__ uided on the effort required, or they understood the scope to be of different depths. At any rate, I need to sync with them on that to see where the man-hour discrepancies lie.     

> __< rbrunner >__ It's easy to ask other people's money shall get spent, but I would feel better if all components there get equal treatment     

> __< k​ayabanerve:matrix.org >__ Can we get two quotes? With/without?     

> __< j​effro256:monero.social >__ Yes, I will ask     

> __< j​effro256:monero.social >__ At what point does the marginal utility of a formal security proof get outweighed by its cost?     

> __< c​haser:monero.social >__ such a difference makes me want to know the firms. I know it's been decided to be withheld, but still.     

> __< k​ayabanerve:matrix.org >__ Depends on the cost :D get us numbers jeffro     

> __< r​ucknium:monero.social >__ Janus only affects privacy, right? Just so I understand right     

> __< k​ayabanerve:matrix.org >__ I'll personally pay at least an extra $10  for this so we can set a floor there     

> __< j​effro256:monero.social >__ lmao     

> __< r​ucknium:monero.social >__ AFAIK FCMP++ is spending a little below expected budget for the research side, so it's probably worth it.     

> __< k​ayabanerve:matrix.org >__ Janus is where someone has two public addresses and confirms they are held by the same entity     

> __< r​ucknium:monero.social >__ *puts 10 USD in my willingness-to-pay privacy calculator*     

> __< j​effro256:monero.social >__ Yeah Janus affects off-chain privacy: the ability to correlate two Monero addresses to the same user. The attack needs to be actively started by sending funds     

> __< r​ucknium:monero.social >__ It is not a theft risk nor a counterfeiting risk.     

> __< k​ayabanerve:matrix.org >__ The legitimate worst case is linking an anonymous profile to a doxxed one.     

> __< r​ucknium:monero.social >__ AFAIK Seraphis-Jamtis was supposed to eliminate the Janus attack. So it would be good if Carrot does too     

> __< k​ayabanerve:matrix.org >__ Nope     

> __< k​ayabanerve:matrix.org >__ Nor a DoS     

> __< r​ucknium:monero.social >__ I thought one of the variants eliminated it?     

> __< k​ayabanerve:matrix.org >__ This is the same technique as JAMTIS AFAIK.     

> __< r​ucknium:monero.social >__ Oh. You were responding to my previous message     

> __< k​ayabanerve:matrix.org >__ Nope was it to not being a theft risk, sorry for the confusion.     

> __< k​ayabanerve:matrix.org >__ Obviously, jeffro256 to confirm, yet an unproven Carrot presumably is as good at stopping Janus as an unproven Seraphis JAMTIS? Same guts on this matter?     

> __< j​effro256:monero.social >__ Yeah btw Carrot should have feature parity with Jamtis except for 1) subaddress lookahead tables are still required 2) no fancy probabilistic light wallet servers, and 3) the key exchange is *slightly* slower     

> __< j​effro256:monero.social >__ It doesn't use the same technique, but they both should have cryptographic strength at blocking Janus attacks AFAIK     

> __< k​ayabanerve:matrix.org >__ Oh. My bad, sorry.     

> __< j​effro256:monero.social >__ Jamtis does a third Diffie-Helman key exchange and binds to that in the amount commitment, while Carrot basically does an HMAC and stuffs it in the space where Jamtis address tags would be     

> __< r​ucknium:monero.social >__ I think MRL wants to get quotes for both with/without Janus.     

> __< j​effro256:monero.social >__ What should the upper limit of our budget be for Carrot in general? 40K, 50K, 60K USD? For transparency, the highest quote I received was for 100K USD, which I think is likely too high for this work in the depth that we need it     

> __< j​effro256:monero.social >__ This is with *less formal* Janus review, but it's still defined to be in-scope     

> __< c​haser:monero.social >__ 20K (the cheapest offer) definitely sounds too low, so 40K minimum?     

> __< rbrunner >__ How many offers did you receive so far?     

> __< k​ayabanerve:matrix.org >__ Are we including proof review, not including proof review, or not doing proof review?     

> __< k​ayabanerve:matrix.org >__ Can you DM me all the groups you reached out to thus far?     

> __< r​ucknium:monero.social >__ One entity needs to write the proofs and another has to review, right? This would only be for writing them, right?     

> __< j​effro256:monero.social >__ rbrunner: 4     

> __< rbrunner >__ Ok, might be enough to learn about "reasonable" regarding amounts by comparing them     

> __< j​effro256:monero.social >__ We could do a review of the written proofs. I wonder how much value that would bring given that Monero addressing schemes are already relatively well understood     

> __< j​effro256:monero.social >__ A review of the implementation code is definitely more important in my opinion     

> __< r​ucknium:monero.social >__ We have two more agenda items. jeffro256 , do you have everything you need until the next meeting?     

> __< j​effro256:monero.social >__ I think so yes. I told the firms that we would have a discussion where the representatives could pop into the meeting and discuss pros/cons of their proposal. Would next week be a good time for that?     

> __< r​ucknium:monero.social >__ That sounds great.     

> __< r​ucknium:monero.social >__ 5) 10 block lock discussion https://github.com/monero-project/research-lab/issues/102 https://github.com/AaronFeickert/pup-monero-lock/releases/tag/final     

> __< r​ucknium:monero.social >__ kayabanerve at last meetng suggested that the N block lock should be set so that the mining pool with the highest hashpower share (currently about 30%) should have a 1% or less probability of success of re-orging the chain N blocks deep through a double-spend attack.     

> __< r​ucknium:monero.social >__ If you thought users liked the 10 block lock, they're going to love     

> __< r​ucknium:monero.social >__ the 20 block lock     

> __< r​ucknium:monero.social >__ I used Theorem 1 of Grunspan & Perez-Marco (2018) "Double spend races" to produce this table: https://gist.github.com/Rucknium/da1e57b1864aca477dfa3b4e02e86e26     

> __< r​ucknium:monero.social >__ The formula assumes that the adversary keeps mining on the attacking chain for an infinitely long period of time if they don't succeed after N blocks. That's usually not economically rational.     

> __< r​ucknium:monero.social >__ Grunspan & Perez-Marco (2021) "On Profitability of Nakamoto Double Spend" considers scenarios when the attacker breaks off the attack after falling behind the honest chain. I plugged in a few numbers. The results don't change much with this economic rationality formula because of the parameters we're working with. The attacker already accepts a 99% probability of failure.     

> __< r​ucknium:monero.social >__ If a 20 block lock is considered too long, then you can change the assumptions. Lower the hashpower share of the attacker or increase the acceptable attack success probability.     

> __< r​ucknium:monero.social >__ Or just say that only benign re-orgs will be considered for the N block lock analysis     

> __< rbrunner >__ The cell with 0.86739 is the one, right, row 20, column 0.3     

> __< k​ayabanerve:matrix.org >__ Sorry, what are the cells?     

> __< r​ucknium:monero.social >__ Right     

> __< c​haser:monero.social >__ nice work Rucknium, I'll read it with more active attention after the meeting. I want to say that looking at current hash rates of pools is an insufficient metric IMHO. the economic feasibility of a related attack depends on the depth N. if N is lowered, more hash power may come online from the sideliness to carry out an attack, because they are no longer priced out.     

> __< rbrunner >__ The table in that gist     

> __< r​ucknium:monero.social >__ Probability of attack success     

> __< k​ayabanerve:matrix.org >__ I understand the row and column definition. I'm unclear what the cells are.     

> __< rbrunner >__ Percentages of success?     

> __< rbrunner >__ Yeah, Rucknium does not fail to surprise :)     

> __< c​haser:monero.social >__ essentially, a dark forest scenario.     

> __< rbrunner >__ But so far what this does *not* hint at IMHO is that 10 is already overlay cautious     

> __< r​ucknium:monero.social >__ chaser: I agree. However, 30% is already very high for a hidden adversary. Just 20% more and the attacker can execute a malicious re-org for any confirmation wait time.     

> __< k​ayabanerve:matrix.org >__ 10% of hash power over 5 years makes a 10-block reorg likely, if I'm interpreting this correctly?     

> __< k​ayabanerve:matrix.org >__ I'd consider that secure and not call for further raising the lock     

> __< r​ucknium:monero.social >__ Years? The sequential numbers down the rows are the number of blocks that an attacker could re-org in a single attack attempt     

> __< k​ayabanerve:matrix.org >__ 100/c, where c is the cell value, for the amount of attempts. Then I said 20 minutes per attempt as the goal is a 10-block reorg (which is 20 minutes of time).     

> __< k​ayabanerve:matrix.org >__ That value, for a 10% attacker, is roughly 5 years.     

> __< r​ucknium:monero.social >__ If you allow the attacker to attack over and over again, the necessary block lock to prevent all attacks would be huge     

> __< k​ayabanerve:matrix.org >__ *I'm perfectly aware that's not the proper formula, I just wanted an offhand estimate of how long an adversary with 10% would need before they stumble onto a successful reorg.     

> __< j​effro256:monero.social >__ Is that the probability of attack success that a single, given block at the top of the chain will get reorged by the largest malicious mining party in some finite timeframe?     

> __< c​haser:monero.social >__ Rucknium: that would be new-entrant hash power, so essentially +100% on top of what we have now. I 'm honestly not sure if that's low or high, but also consider that Monero is non-ASIC, so there is a lot of hardware out there that can be repurposed to support a reorg attack.     

> __< k​ayabanerve:matrix.org >__ I'm not asking about preventing all locks. I'm curious how long it takes before they stumble onto it. I can't reasonably argue an adversary would pay for 10% of the hash power for *years* just to perform a DoS here.     

> __< k​ayabanerve:matrix.org >__ But there may be value to an adversary in having a large amount of hash power for days, or weeks, to perform even just a DoS.     

> __< r​ucknium:monero.social >__ jeffro256: The first row is just probability of re-orging one block with a single attack. The model assume that the attacker gets a head start of one block. The attacker is basically constantly mining until they get that one-block head start     

> __< r​ucknium:monero.social >__ If people are wondering "How secure is PoW, really?", then you can read Budish, E. (2022). "The Economic Limits of Bitcoin and Anonymous, Decentralized Trust on the Blockchain."  https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=101     

> __< j​effro256:monero.social >__ What is a single attack "attempt"? How long does it take for this attacker to give up on a failed attack?     

> __< r​ucknium:monero.social >__ Budish recently released an updated draft a few months ago     

> __< rbrunner >__ Maybe after much back and forth with will find out, in a few weeks, that - surprise - 10 blocks are just *perfect*     

> __< r​ucknium:monero.social >__ jeffro256: In this model, the attack continues forever. If the attacker "loses" the race to the N blocks, he/she can still win later because of random block arrivals     

> __< r​ucknium:monero.social >__ In the second paper Grunspan & Perez-Marco (2021). "On Profitability of Nakamoto Double Spend."     

> __< r​ucknium:monero.social >__ they consider the attacker breaking off the attack if he/she loses the first part of the race     

> __< r​ucknium:monero.social >__ But anyway, I put some number in that Grunspan & Perez-Marco (2021) formula and didn't see much difference     

> __< k​ayabanerve:matrix.org >__ So if they 'start a new attempt' to reroll a 1% chance,  it's of no difference to continuing the existing attack?     

> __< k​ayabanerve:matrix.org >__ I'm not surprised by that statement, but the numbers in the table don't mentally click for me to be in line with that statement     

> __< r​ucknium:monero.social >__ "it's of no difference to continuing the existing attack"  What do you mean?     

> __< r​ucknium:monero.social >__ The traditional 6 block confirmation time for bitcoin comes from the slightly incoirrect original formula from Staoshi where the attacker has 10% hashpower share and less than 0.1% probability of success. See Table 1 of Grunspan & Perez-Marco (2018) https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=192     

> __< r​ucknium:monero.social >__ Satoshi*     

> __< rbrunner >__ Interesting     

> __< r​ucknium:monero.social >__ I want to get to the Chainalysis video. Maybe we can digest this info later, discuss the video now     

> __< k​ayabanerve:matrix.org >__ If I have 10% of the hash power and want to do a 10-block reorg, what period of time do I need to maintain 10% of the hash power before I successfully pull off such an unlikely event?     

> __< k​ayabanerve:matrix.org >__ That's the question I've been trying to get to, but sure, we can circle back lager     

> __< k​ayabanerve:matrix.org >__ *later     

> __< r​ucknium:monero.social >__ Ok I can try to answer for you later. It's not difficult to compute  because the attempts are independent     

> __< r​ucknium:monero.social >__ 6) Chainalysis capabilities video     

> __< r​ucknium:monero.social >__ Sometimes I read papers about attacks that seem a little contrived. I think "Is anyone listening? Does anyone care?" Now I know that Chainalysis is listening and caring.     

> __< r​ucknium:monero.social >__ In other words, this gives us a lower bound on the resources they have put into attacking the privacy on Monero users.     

> __< c​haser:monero.social >__ I watched it and I wasn't too surprised. the edge they have will be mostly curbed by FCMP++. on top of that the main assets for them are weaknesses in transfer-layer privacy, which they formed by running swarms of their own nodes.     

> __< r​ucknium:monero.social >__ Some interesting things: There are a few abbreviated variables attached to transactions that the presenter doesn't explain. Any ideas what those could be?     

> __< c​haser:monero.social >__ I felt that the recent further looking-into into  D++ is a worthy direction.     

> __< j​effro256:monero.social >__ A lot of government provided IP address information was used in the analysis. Makes https://github.com/monero-project/monero/pull/8996 a bit more important than I originally anticipated     

> __< j​effro256:monero.social >__ chaser: agreed     

> __< c​haser:monero.social >__ Rucknium I can't recall the abbreviations, could you give a time stamp?     

> __< r​ucknium:monero.social >__ They have the time difference between when one of their nodes observed the txs relayed for the first and second time. If they don't have network topology info, the first-spy estimator is best. I wonder if they are trying a topology-based estimator. It may be possible to take the time delay data they display, put it into a complex statistical model, and get an estimate for the numb<clipped message     

> __< r​ucknium:monero.social >__ er of malicious nodes they are running.     

> __< r​ucknium:monero.social >__ chaser: About 19:00     

> __< r​ucknium:monero.social >__ "Transaction features box"     

> __< k​ayabanerve:matrix.org >__ Wallet trees would mean a passively malicious node doesn't learn any additional info on the outputs spent.     

> __< c​haser:monero.social >__ 10/+ is probably decoy count?     

> __< r​ucknium:monero.social >__ IMHO, fee uniformity should be a near-term research priority. Fees were at the top of their tx indistinguishably list.     

> __< r​ucknium:monero.social >__ chaser: The `K,E` part     

> __< k​ayabanerve:matrix.org >__ The fundamental technique can be done with outputs today, it'd just use a lot more wallet storage.     

> __< c​haser:monero.social >__ I was just about to say this. discretized fees, here we go again!     

> __< rbrunner >__ Well, cough, with Seraphis we would get these, if I remember correctly ...     

> __< b​oog900:monero.social >__ I _think_ it's the details of the extra field     

> __< r​ucknium:monero.social >__ IMHO, at a minimum it makes sense to charge fees based on the number of inputs/outputs and any extra tx_extra info instead of the exact number of bytes.     

> __< b​oog900:monero.social >__ K being a public key, E being an encrypted payment ID and AK being additional public keys     

> __< j​effro256:monero.social >__ rbrunner: we can do discretized fees in RingCT if we just restrict the `txnFee` field to only so many values by validator rule     

> __< r​ucknium:monero.social >__ It's really hard right now to even confirm that a wallet has standard fees since txs have variable-length integers that make tx sizes slightly different.     

> __< c​haser:monero.social >__ boog900 I think so too     

> __< j​effro256:monero.social >__ boog900: yeah I remember them mentioning "key order" as a feature which, yeah, might be what this     

> __< k​ayabanerve:matrix.org >__ Yes buy that shouldn't be fingerprintable Rucknium     

> __< j​effro256:monero.social >__ IIRC a long time ago one could tell which transactions were cold signed because they had 2 tx pubkey fields in `tx_extra` instead of 1     

> __< k​ayabanerve:matrix.org >__ The Monero wallet deals with that in a way. As long as everyone doing custom fee code matches that way, it's not distinguishable     

> __< r​ucknium:monero.social >__ There are so many wallets that dont do that     

> __< k​ayabanerve:matrix.org >__ I just want to clarify AFAICT, this is to force alt wallets in line, not to resolve fundamental issues     

> __< k​ayabanerve:matrix.org >__ Extra field presence/ordering has been a topic for a while, someone has a data set     

> __< r​ucknium:monero.social >__ And I have no function that I can input a Monero tx in and get the standard wallet2 fee     

> __< k​ayabanerve:matrix.org >__ Heard. I do support this work TBC.     

> __< r​ucknium:monero.social >__ The "problem" with discretized fees is that it doesn't fix nonstandard fees that are very far from "standard", which is a lot of them     

> __< k​ayabanerve:matrix.org >__ Explicitly giving each output its own key in a structured position? Sounds great     

> __< r​ucknium:monero.social >__ A lot of wallets aren't even trying     

> __< r​ucknium:monero.social >__ Reference: https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees     

> __< r​ucknium:monero.social >__ So we need....price control! :P     

> __< k​ayabanerve:matrix.org >__ Bit shilly, yet getting exactly in line with wallet2 was a couple weeks of work for monero-serai. I fully understand how nontrivial it is     

> __< c​haser:monero.social >__ kayabanerve isn't "force alt wallets in line" the way to solve the fundamental issue?     

> __< k​ayabanerve:matrix.org >__ (shout out to jberman who actually did it)     

> __< r​ucknium:monero.social >__ The price controls issue is what makes this hard. And the interaction with the dynamic block size, miner fee penalties, etc     

> __< k​ayabanerve:matrix.org >__ Yes chaser. My comment was this isn't wallet2 that is fingerprinting users. It's alt wallets which are. Users can use wallet2 without worrying their personal running of the software will fingerprint them across TXs.     

> __< r​ucknium:monero.social >__ A nice thing about discretized fees is it  fixes an issue with an EAE attack that is even possible with FCMP++: If a user spends the whole balance, then the only difference that Eve sees is the tx fee, which are different for many txs.     

> __< k​ayabanerve:matrix.org >__ That isn't to downplay the issue. that's to not have people concerned about its a protocol failure (rather than a shortcoming of it to handle lazy wallet devs)     

> __< r​ucknium:monero.social >__ All wallet devs are lazy until proven otherwise :P     

> __< k​ayabanerve:matrix.org >__ I proved otherwise :(((     

> __< c​haser:monero.social >__ kayabanerve got it.     

> __< r​ucknium:monero.social >__ I mean, they take the shortest path to get something working, usually     

> __< sneurlax >__ kayabanerve, not til you publish monero-wallet to crates.io :^)     

> __< r​ucknium:monero.social >__ More topics on the video?     

> __< c​haser:monero.social >__ I'm very much on board with making as much of the fee function part of consensus as possible.     

> __< sneurlax >__ (kayaba: jk just releease me from needing to use serai as a submodule, señor)     

> __< c​haser:monero.social >__ well, I have one but may be out of scope for the meeting     

> __< sneurlax >__ rucknium: re the video, would it be helpful to scrape more information from the presentation?     

> __< sneurlax >__ the information from the spreadsheets shown, that is     

> __< k​ayabanerve:matrix.org >__ Sneurlax: Cargo.toml a git revision?     

> __< r​ucknium:monero.social >__ This nice post by Stnby and Siren  suggests that Chainanlysis may have taken advantage of old DNS configs to "hijack" "trusted" remote nodes: https://www.digilol.net/blog/chainanalysis-malicious-xmr.html     

> __< c​haser:monero.social >__ what would cryptography that conceals in/out numbers look like? in/out arity was another factor they used.     

> __< k​ayabanerve:matrix.org >__ Every TX would be n/n     

> __< rbrunner >__ With tons of fake stuff for simple txs?     

> __< r​ucknium:monero.social >__ sneurlax: Yes, especially the relay timing info in `ms`. Later I could try to do something with that to estimate their number of spy nodes. I have been reading so many gossip protocol papers lately :D     

> __< c​haser:monero.social >__ I hope something else we thought would be mathematically impossible will see the light of day     

> __< k​ayabanerve:matrix.org >__ Zero-value ins/outs for padding     

> __< r​ucknium:monero.social >__ chaser: You can bring it up     

> __< c​haser:monero.social >__ (Rucknium: this is it, arity)     

> __< c​haser:monero.social >__ tevador had an idea for discretized arity, I'll dig it up     

> __< r​ucknium:monero.social >__ Oh, I forgot I had make another two tables     

> __< r​ucknium:monero.social >__ Tabulation of Monero transaction inputs and outputs  https://gist.github.com/Rucknium/d2c02f51a2d9f103a28caa8f51be7dbf     

> __< j​effro256:monero.social >__ With dummy inputs, every single transaction could be a 2/2, and owners of funds can still split/consolidate funds to/from `N` TXOs in `O(log(N))` time     

> __< r​ucknium:monero.social >__ The most import info is how many txs have 3+ inputs. At that point, consolidation heuristics might help adversaries narrow down which ring member is the real spend.     

> __< k​ayabanerve:matrix.org >__ jeffro256: you're a horrible person for not at least giving us 4/4.     

> __< r​ucknium:monero.social >__ About 7 percent of txs have 3 or more inputs. So the Chainalysis method of collecting info about who owns which outputs, then analyzing many-input txs, would usually only be applicable to about 7% of txs as an upper bound.     

> __< r​ucknium:monero.social >__ Maybe you could try that consolidation analysis with txs with only 2 inputs. I don't know.     

> __< r​ucknium:monero.social >__ Actually the probability hasn't been formally analyzed     

> __< j​effro256:monero.social >__ lol every tx being 256/16 should cover most usecases, mempool handling code be damned     

> __< j​effro256:monero.social >__ Wouldn't it be applicable to all txs since those 7% could (maybe, big assumption) be eliminated as decoys?     

> __< r​ucknium:monero.social >__ For the false positive rate of analyzing tx uniformity defects in single-ring transactions, I developed an exact formula in https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf     

> __< c​haser:monero.social >__ Dummy transaction inputs (tevador): https://github.com/monero-project/research-lab/issues/96     

> __< c​haser:monero.social >__ increasing uniformity of number of inputs/outputs (my generalized take): https://github.com/monero-project/research-lab/issues/114     

> __< r​ucknium:monero.social >__ The formula is equation 12, a little complicated already     

> __< c​haser:monero.social >__ IMHO restricting ins to 2^n (n>0) and outs to constant 2 could go a long way     

> __< r​ucknium:monero.social >__ jeffro256: Do you mean with a chain-reaction analysis?     

> __< c​haser:monero.social >__ ^ my gut instinct exactly     

> __< k​ayabanerve:matrix.org >__ I can't endorse 2/2 compared to 4/4, personally.     

> __< k​ayabanerve:matrix.org >__ 2/2 will be hours of delay and requires perfect precision w.r.t. output usage planning. It also will hit wallet UX.     

> __< r​ucknium:monero.social >__ IMHO, there is not a developed theory about why diverse in/outs are inherently bad, except that allowing many inputs can help an adversary perform the consolidation analysis when ring size is finite. Nonstandard fees are inherently bad because the wallet produces them _every time_, so an adversary can link the txs easier. a wallet won't produce the same in/outs every time     

> __< k​ayabanerve:matrix.org >__ *hours of delay at scale. 256 outputs take 8 hops or 2.66h as of right now. It's 1.33h with 4 which is still a massive hit compared to as many inputs as fit.     

> __< c​haser:monero.social >__ Rucknium I agree that fee uniformity is a more pressing issue     

> __< r​ucknium:monero.social >__ What comes to mind is that a txs with many inputs or many outputs is more likely to belong to a service. A miner or merchant consolidating txs with many inputs. An exchange sending txs out to many users in a single batch would use many outputs.     

> __< c​haser:monero.social >__ well, these guys love giving visits to services     

> __< r​ucknium:monero.social >__ If Monero requires 2/2 for all txs, then no one will have to worry about the privacy of those services since they won't exist. (this is a joke)     

> __< j​effro256:monero.social >__ lol     

> __< c​haser:monero.social >__ this behavior could be eliminated by restricting just outs to 2, with dummy if needed. the practicality issues are heavier with restricting ins     

> __< r​ucknium:monero.social >__ We are at two hours. Marathon meeting. Thanks all for attending and working so hard to improve Monero. If you didn't see the video, Chainalysis praises Monero developers for their hard work lol     

> __< c​haser:monero.social >__ let services send individual tx's. a service can afford forethought in output planning     

> __< c​haser:monero.social >__ yeah, thank you all     

> __< r​ucknium:monero.social >__ The meeting can end here. Feel free to continue discussing issues.     

> __< j​effro256:monero.social >__ Thanks, everyone!     

> __< c​haser:monero.social >__ updated draft, clocking an impressive 71 pages:     

> __< c​haser:monero.social >__ Budish: Trust at Scale: The Economic Limits of Cryptocurrencies and Blockchains (July 2024)     

> __< c​haser:monero.social >__ https://ericbudish.org/wp-content/uploads/2024/07/Trust-at-Scale-The-Economic-Limits-of-Cryptocurrencies-July-2024.pdf     

> __< c​haser:monero.social >__ a lot of complementary material here: https://ericbudish.org/publication/the-economic-limits-of-bitcoin-and-the-blockchain/   


# Action History
- Created by: Rucknium | 2024-09-06T19:49:06+00:00
- Closed at: 2024-09-25T16:21:49+00:00
