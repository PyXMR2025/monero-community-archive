---
title: Monero Research Lab Meeting - Wed 02 August 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/873
author: Rucknium
assignees: []
labels: []
created_at: '2023-08-01T20:58:39+00:00'
updated_at: '2023-08-08T18:33:13+00:00'
type: issue
status: closed
closed_at: '2023-08-08T18:33:13+00:00'
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

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#870 

# Discussion History
## plowsof | 2023-08-02T19:18:00+00:00
Logs 
```
17:01:05 <Rucknium[m]> Meeting time: https://github.com/monero-project/meta/issues/873

17:01:27 <Rucknium[m]> 1) Greetings

17:01:32 <Rucknium[m]> Hi

17:01:42 <rbrunner> Hello

17:04:08 <rbrunner> On Monday, for the wallet meeting, we were only 3 as well ...

17:04:34 <Rucknium[m]> compdec's messages aren't getting through to IRC. I may have to informally relay. I
heard that the Libera<>Matrix bridge is having trouble. Maybe mine get through OK since my Matrix server is
monero.social

17:04:53 <Rucknium[m]> compdec says hello

17:05:04 <rbrunner> Ah, ok :) Can you read me?

17:05:23 <Rucknium[m]> 2) Updates, what is everyone working on?

17:06:03 <Rucknium[m]> me: Working on a fix to the ring member dependence issue. I have an update or two on
that.

17:07:01 <Rucknium[m]> rbrunner: Yes, but maybe 30-60 second delay

17:07:09 <rbrunner> Pfff...

17:09:20 <Rucknium> I can chat from IRC. Potential agenda: compdec's initial work/findings, hard fork
readiness/justification criteria, ring member dependence issues.

17:10:06 <Rucknium> compdec: "I've got a number of progresses that I'll have a written report on next week.  I
can discuss anything in particular.  There will be a few code updates before that as well."

17:10:49 <rbrunner> I tried to join on Matrix, didn't work, "There was an error joining". Splendid.

17:12:43 <Rucknium[m]> compdec: To start, which research questions were you able to come to some conclusions
on?

17:13:11 <rbrunner> I can at least *read* Matrix. If we don't have somebody else right now on the IRC side, no
need to manually relay

17:13:21 <vtnerd> hi (sorry late)

17:13:51 <moneromoooo> Is it logged if not relayed ?

17:14:51 <Rucknium[m]> moneromooo: AFAIK, if it's not relayed to IRC, then it is not logged at
libera.monerologs.net

17:15:08 <rbrunner> Strangely, monerologs.net seems to be complete - at least right now

17:15:34 <Rucknium> rbrunner: I don't see anything from compdec there

17:15:51 <Rucknium> compdec: "The one thing I can say for sure, is things seem a lot more mixed now than when
I did my investigations a few years ago.  I think conclusions is still too strong a word at this stage, I'm
working on some tests today, but soon as I'm convinced things are doing what I think they are doing they'll be
in the MRC [Monero Research Computing Server] for anyone to play with."

17:15:53 <vtnerd> me: working on noise protocol and doing drole CI stuff for lws

17:16:02 <rbrunner> Ah, right

17:16:40 <Rucknium> vtnerd: Thanks. If there a document or something that we can read about which threat
models the noise protocol is designed to defend against?

17:17:29 <rbrunner7[m]> Sorry to spam, test, test

17:17:37 <vtnerd> I posted a PR that talked about this a while ago:https://github.com/monero-
project/monero/pull/8028

17:18:03 <Rucknium[m]> compdec: I think there is a breakdown of the bridge that connects Libera IRC to Matrix
servers. Sorry this happened during your first meeting :(

17:18:06 <vtnerd> in that PR, but basically the only threat it potentially prevents against (above SSL) is DPI
fingerprinting

17:18:24 <Rucknium[m]> There are desktop and mobile apps for Matrix element. I don't know if you would be more
successful with that with the bridge having trouble.

17:18:29 <vtnerd> although with the consistent port numbers, its probably pointless (without promoting random
port numbers)

17:18:57 <jeffro256[m]> Howdy, sorry I'm late

17:19:12 <Rucknium> vtnerd: Thank you!

17:19:36 <vtnerd> the other trouble with SSL or noise, are the strategies during the "upgrade", where some of
your peers support encryption but your local table hasnt been updated yet

17:20:00 <Rucknium[m]> jeffro is on the monero.social home server and it's being relayed to IRC. May be a home
server problem with matrix.org

17:20:01 <vtnerd> SSL vs noise have different strategies for this

17:20:29 <vtnerd> lastly, I choise noise simply because two community members recommended that over SSL, and
there wasn't much movement against in an GH issue that is still posted

17:20:39 <jeffro256[m]> vtnerd: One advantage using SSL over noise is that we can "hijack" the 443 port to
hide Monero network traffic among normal web traffic, even on the same server (using reverse proxies)

17:21:39 <Rucknium[m]> xmrack: But your messages aren't being sent to IRC

17:22:28 <Rucknium> compdec: "One interesting thing I'm finding is that some analogy or the EAE problem is
already present at the level of ring correlations."

17:23:11 <jeffro256[m]> I recently started thinking about that advantage of SSL when I tried to resync my
daemon in an airport. A lot of WIFI hotspots try to limit traffic to certain protocols. If we use SSL, we
stand a higher chance of blending in with web traffic and skirting less advanced network controls

17:24:05 <vtnerd> jeffro256[m]: possibly, but low port numbers often require special permission

17:25:03 <vtnerd> we could combine it with a patch that "steps down" permissions

17:26:07 <vtnerd> I'll think about this the next few days, one of the difficult points is detecting when the
peer supports encryption and how to upgrade it

17:26:34 <vtnerd> with noise I can control 100% of the data flow, but with SSL Im not writing my own
implementation so we have to work-around an API

17:27:51 <Rucknium> vtnerd: Could a hard fork boundary be used to make sure all peers support encryption? What
do you think about that?

17:33:03 <Rucknium[m]> selsta's new CCS proposal ( https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/404 ) says "Continue the planning of a network upgrade with RandomX changes
(https://github.com/monero-project/monero/issues/8827) and Bulletproofs++"

17:33:55 <Rucknium[m]> I think OSPEAD should be added to that list. Where do the RandomX changes and BP++ need
to be to be considered ready for a possible hard fork?

17:34:39 <Rucknium[m]> Liam Eagan say that the BP++ paper was submitted to this conference. Apparently it
wasn't accepted: https://sp2023.ieee-security.org/program-papers.html

17:35:15 <Rucknium[m]> That doesn't mean that the paper isn't good. Just maybe not a good fit for the topics
in the conference. This means that the paper has no peer review still.

17:36:20 <vtnerd> rucknium[m]: I discussed this at monerotopia22, the seth pointed out that we may not want to
make encryption mandatory, so that theres a fallback

17:36:41 <Rucknium[m]> For BP+ (one plus) there were two audits. Maybe at least one would be considered a
review of the math. Do we want to do that again for BP++?

17:36:43 <vtnerd> the difficult part is that the p2p connections persist "through" a hardfork, but it could
sort-of be done for making new connections

17:37:27 <Rucknium> vtnerd: I see. Thanks.

17:39:41 <jeffro256[m]> vtnerd: Assuming that 1) everyone is using the core project's daemon and 2) we know
all nodes have integrated the p2p encryption code since the code was merged before the most recent hardfork,
why would want to allow unencrypted connections?

17:45:22 <Rucknium[m]> I'll give my update on OSPEAD: I tried a quick fix to the ring member dependence issues
and...

17:45:28 <Rucknium[m]> it was a complete failure. lol

17:45:46 <Rucknium[m]> Maybe a different quick fix would not be a failure, but that one was.

17:47:05 <jeffro256[m]> Rucknium[m]: What did you try?

17:47:09 <Rucknium[m]> I am still evaluating the "long fix". Getting a little more pessimistic about that one,
too. So maybe we would accept some inaccuracy. Close doesn't count, except for horse shoes, hand
grenades....and statistics :)

17:47:33 <Rucknium> compec: "perhaps I should ask in the dev channel when finished here, but I have some
questions on the state of the decoy selection"

17:47:55 <Rucknium[m]> Maybe jeffro256  can answer some questions about the state of decoy selection

17:48:10 <jeffro256[m]> I'd be happy to ;)

17:48:53 <Rucknium[m]> jeffro256: I tried something that eliminated the correlation between ring members, but
that had unintended consequences that destroyed the final estimate.

17:49:03 <vtnerd> jeffro256[m]: that was my initial thought, seth convinced me otherwise at the conference but
I dont remember his argument :/

17:49:06 <vtnerd> it should be on video

17:50:07 <Rucknium[m]> That is, taking a dataset that has some correlation and transforming it to have no
correlation. (Instead of starting with an uncorrelated dataset to begin with, which the current OSPEAD
estimator happens to handle extremely well.)

17:50:37 <Rucknium> compdec: "I'll put it here then.  It seems that there is a window for recent transactions
and after that, things are called from a log(beta) distribution.  Is there an empirical distribution that is
being measured and drawn from for the recent transactions?"

17:52:29 <Rucknium> compdec: "Basically I'm trying to look at a ring, choose subsets of that ring, and test
the likelihood that configuration could have come from the decoy selection"

17:57:29 <jeffro256[m]> <compdec[m]> "I'll put it here then.  It seems..." <- The current decoy selection
algorithm takes a gamma (log) distribution, more or less uses that as a timestamp to index outputs. The gamma
distribution is distorted based on the output volume per block, but there is no empirical distribution to
speak of in Monero since the distribution of true spends is obfuscated by nature

17:59:05 <jeffro256[m]> IIRC, Rucknium uses the Litecoin spend distribution as an empirical "ground truth" and
compares spending in Monero to that distribution

17:59:13 <jeffro256[m]> (In OSPEAD)

18:00:06 <Rucknium[m]> I am using LTC as a test for the Monte Carlo. I know the LTC real spend, so I can tell
if the estimator recovers the correct real spend distribution. OSPEAD will be used on Monero's data for the
final estimate.

18:00:40 <Rucknium[m]> We don't know the ground truth for Monero. The estimator's output is supposed to be the
best guess.

18:01:04 <Rucknium[m]> We don't know the ground truth for most things in statistics, which is why we use
statistics in the first place :)

18:02:56 <jeffro256[m]> Rucknium[m]: Yes, sorry I worded that badly but that's what I'm getting at (which is
what makes Rucknium's work so hard); there's no way to tell what the actual distribution of true spends in
Monero is *by design*.

18:02:59 <jeffro256[m]> The decoy selection has gone from an even distribution, to a triangular distribution,
to a gamma distribution

18:03:07 <Rucknium> compdec: "I see.  I thought it was a beta distribution, which had support from 0 to 1."

18:03:42 <Rucknium> compdec: "How does the distortion by volume happen?  It seems that there is some
stationary component as well as some non-stationary component"

18:04:10 <Rucknium[m]> ("even" = uniform distribution)

18:05:07 <jeffro256[m]> The RPC endpoint /get_output_distribution lists the number of outputs for a given
amount at each block. This data is used in the DSA to more heavily weigh times of high transaction output

18:05:51 <Rucknium[m]> Mobilecoin and Zano are still using a uniform distribution AFAIK

18:05:55 <Rucknium[m]> (DSA = Decoy Selection Algorithm)

18:07:28 <Rucknium[m]> We can officially end the meeting here. Conversation about what exactly the Monero DSA
is doing can continue of course :)


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-08-01T20:58:39+00:00
- Closed at: 2023-08-08T18:33:13+00:00
