---
title: Monero Research Lab Meeting - Wed 13 September 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/894
author: Rucknium
assignees: []
labels: []
created_at: '2023-09-13T14:05:43+00:00'
updated_at: '2023-09-21T17:15:31+00:00'
type: issue
status: closed
closed_at: '2023-09-21T17:15:31+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

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

#890 

# Discussion History
## plowsof | 2023-09-20T18:50:09+00:00
Logs 
```
17:01:11 <Rucknium> Meeting time! https://github.com/monero-project/meta/issues/894

17:01:21 <Rucknium> 1) Greetings

17:02:09 <rbrunner> Hello

17:02:10 <vtnerd> hi

17:03:26 <msvb-web> Hello meeting?

17:03:35 <Lyza> haii, yes meeting

17:04:07 <Rucknium> 2) Updates. What is everyone working on?

17:05:40 <vtnerd> me: still ssl :/ having trouble getting the fingerprints storing across runs. also beginning
work on subaddresses+lws (dont see a reason to wait much longer)

17:05:58 <Rucknium> me: Working on an empirical analysis of nonstandard transaction fees. Working on a
theoretical analysis of a real spend classifier that uses nonstandard tx features (fungibility/uniformity
defects) to guess the real spend in a ring.

17:06:08 <vtnerd> might do lws-schema+seraphis first though

17:07:25 <rbrunner> vtnerd: Not sure what you mean with this

17:07:46 <vtnerd> The lws protocol will have to be updated for seraphis most likely

17:08:41 <rbrunner> Yeah, such servers could even look completely different, only scanning for viewtags and
apart from that not doing much

17:09:16 <vtnerd> LWS will probably support both modes, if possible

17:09:46 <rbrunner> Certainly a good idea to look into this early

17:09:55 <vtnerd> the problem is the unspent outputs will grow rather large with seraphis, so it still might
be work doing a full-scan for LWS

17:10:28 <rbrunner> But hey, they are still discussing whether 1 or 2 view tags, and how calculated, and so
an. Just check the Jamtis gist :)

17:10:32 <vtnerd> because its possible spends (of a much larger ring) of possible receives

17:11:18 <rbrunner> So Jamtis might not have its first "final" form yet

17:13:40 <Rucknium> 3) Discussion. What to discuss?

17:14:15 <Rucknium> (I have the nonstandard fees to discuss, but anything else someone wants to bring up?)

17:16:36 <Rucknium> When recent blocks are not congested, get_fee_estimate suggests possible standard fee
levels at 20, 80, 320, or 4000 nanoneros per byte. I consider anything outside of the set of 4 fee levels to
be "nonstandard".

17:16:55 <Rucknium> IMHO, there are at least three reasons to analyze nonstandard fees:

17:17:23 <Rucknium> 1) The current Seraphis proposal includes "fee discretization" that will reduce the
possible values of fees by consensus rules. We don't know what the best set of values could be. Current
behavior on the blockchain can guide our choices.

17:17:38 <Rucknium> 2) Wallets that use nonstandard fees may also construct transactions with other
nonstandard characteristics, such as the decoy selection algorithm or tx_extra contents.

17:17:53 <Rucknium> 3) In general it is a good idea to know what's happening on the blockchain and any privacy
issues that nonstandard fees are causing.

17:18:52 <Rucknium> The reason I started looking at nonstandard fees is (2). I want to identify nonstandard
decoy selection algorithms on the chain for OSPEAD. In the short term I won't do a "full" analysis of
nonstandard fees since I will return to OSPEAD. But I want to get certain analysis down on paper while it is
fresh.

17:19:13 <Rucknium> The more I look at the data, the more I think fee discretization is going to require some
deeper analysis. IMHO, nonstandard fees probably have at least three different causes:

17:19:28 <Rucknium> 1) Wallet developers trying to use standard fees, but the calculation is slightly
incorrect. 2) Wallet developers not trying to use standard fees at all. 3) Monero users deciding to select a
custom fee.

17:19:40 <Rucknium> AFAIK, (3) cannot be done by any users of wallet2 nor its derivatives. It would have to be
a different "nonstandard" wallet implementation, anyway.

17:20:00 <Rucknium> I think a simple fee discretization rule could reduce or eliminate (1) and (3). Trying to
reduce (2) would require more thought and analysis.

17:20:19 <Rucknium> My analysis so far has focused on (2). It's worse than I expected. About 10% of recent
transactions have a nonstandard fees that cannot be explained by a "rounding error".

17:21:46 <Rucknium> That's the empirical part. The theoretical part is a classifier that exploits any defects
in transaction uniformity/fungibility. I am almost finished with a formula that will calculate the probability
of true positives and false positives when the classifier guesses the real spend in a ring.

17:22:55 <rbrunner> That somehow sounds very surprising - what do you mean with "formula"?

17:23:06 <Rucknium> True/false positive probability is determined by the ring size, the proportion of
transactions on the blockchain that have the defect, and the probability that a user's real spend is a change
output (instead of an output that they received from someone else).

17:23:29 <Rucknium> A math formula with these ^ variables.

17:24:01 <Rucknium> If I use this classifier, what is the probability that I correctly guess the real spend in
a ring?

17:25:16 <Rucknium> The classifier is a simple classification rule. It is applied to rings in txs with the
defect. If the ring has no outputs that come from txs with the defect, then just guess randomly (probability
of success is 1/ring_size)

17:25:39 <Rucknium> If the ring has exactly one ring member with the defect, then guess that the output with
the defect is the real spend.

17:26:13 <Rucknium> If the ring has two outputs with the defect, then randomly guess between those two. Of
three, then randomly guess between the three, and so on.

17:26:52 <Rucknium> It's putting numbers to a problem that has been discussed for years.

17:26:59 <rbrunner> Interesting. Maybe dumb question: Is this approach new, as far as you know?

17:28:46 <Rucknium> AFAIK, yes, but it is simple. A few draft papers have been written at a "higher level"
than this. About how fungibility defects can help guess multiple hops. But none of them have a formula for the
actual potency of an analysis at the single "hop" level (and you need the single hop formula to start putting
numbers to multiple hops IMHO)

17:29:41 <Rucknium> Putting specific numbers can help make protocol decisions in two ways.

17:30:27 <Rucknium> 1) If there is a downside to requiring certain forms of tx uniformity, what do we gain
from requiring the uniformity? We can evaluate the tradeoffs then.

17:30:57 <Rucknium> 2) What is the actual drawback of changing the decoy selection algorithm at a time outside
of a hard fork?

17:32:06 <Rucknium> If we changed the DSA outside of a hard fork, then some users would be using the old DSA
and some would be using the new one simultaneously. How much advantage could an adversary gain from that
situation?

17:32:38 <rbrunner> This seems closely connected with the use of rings. I.e., no more rings, aka "full chain
membership proofs", less drastic consequences of such "defects"?

17:33:46 <Rucknium> Yes. We would still not want to have defects, but the privacy effects would be much less.

17:34:00 <rbrunner> Understood.

17:34:58 <rbrunner> You mean with two major DSAs on the network, one maybe could used in the sense of the
"defect" in your approach

17:35:18 <Rucknium> On "newness": Researchers have done something similar on bitcoin and other transparent
UTXO for a long time. For example: Moser & Narayanan (2022) "Resurrecting Address Clustering in Bitcoin"
https://arxiv.org/abs/2107.05749

17:36:52 <Rucknium> rbrunner: Right. It's more complicated with the DSA compared to fees for example since you
first need to do a statistical test of whether the actual ring distribution in a specific ring comes from one
of the two (or more) DSAs. If it is hard to draw conclusions from that test, then the privacy risk is lower.

17:37:51 <Rucknium> The bitcoin research doesn't have to consider rings, of course. That research tries to
detect which outputs are change so that transfer of bitcoin custody can be guessed.

17:38:53 <rbrunner> Can only say, eagerly awaiting results :)

17:39:19 <Rucknium> With bitcoin the real spend is always known. Whether an output is a change output is not
known. My proposed classifier just tries to guess the real spend.

17:39:55 <Rucknium> I think I will post it as a discussion note next week.

17:41:06 <Lyza> maybe slightly off topic, but in terms of protecting users, if 10% of transactions are using
very non-standard fee levels then some investigation could reveal if any larger public services are
responsible, and maybe they'd change if informed

17:41:08 <Rucknium> The main "thing" is that you must consider the probability of the decoy selection
algorithm including an output with the defect by chance. That chance is determined by a binomial distribution
(as usual).

17:42:56 <Rucknium> Lyza: I agree. Doing an exhaustive search would take weeks or months. If someone wants to
take it on, I could definitely get them started. Like I said, this is sort of a detour from my DSA improvement
work. I can come back to this later after OSPEAD is completed.

17:45:08 <Rucknium> If I saw something very obvious, then I would take action to fix it. Going down every
rabbit hole with possible dead ends is a distraction for me right now.

17:45:53 <Lyza> of course

17:45:56 <Lyza> I'm happy to at least check some services I use and maybe a few more popular ones, I guess
something like a table of observed fee levels etc would be useful to compare against if you wanna share

17:46:14 <Lyza> seems like something that wouldn't be too hard to crowdsource

17:47:54 <Rucknium> I could put up something like that. Maybe next week. I think there are 5 major "islands" I
see in the data. 3 very minor ones. A specific service or wallet implementation may be creating more than one
of those islands.

17:48:31 <rbrunner> Could even develop into something like a treasure hunt "find the Monero fee dissenters"
...

17:49:15 <Rucknium> I didn't try to look at fee levels that are very close but not exactly at the "standard"
levels because I don't know really how wallet2 might do rounding. I looked at the low hanging fruit.

17:51:05 <Rucknium> (This analysis was made possible by the Monero Research Computing server, partially funded
by the CCS. Thanks, donors!)

17:54:21 <Rucknium> Anything else to discuss?

17:58:12 <Rucknium> We can close the meeting. Thanks everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-09-13T14:05:43+00:00
- Closed at: 2023-09-21T17:15:31+00:00
