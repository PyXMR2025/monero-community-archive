---
title: Monero Research Lab Meeting - Wed 09 August 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/876
author: Rucknium
assignees: []
labels: []
created_at: '2023-08-08T18:32:58+00:00'
updated_at: '2023-08-25T19:07:29+00:00'
type: issue
status: closed
closed_at: '2023-08-22T22:33:13+00:00'
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

#873 

# Discussion History
## plowsof | 2023-08-25T19:07:29+00:00
Logs 
```
17:00:38 <Rucknium> Meeting time: https://github.com/monero-project/meta/issues/876

17:00:49 <Rucknium> 1) Greetings. Hi

17:01:03 <vtnerd> hi

17:01:05 <rbrunner> Hello

17:02:08 <m-relay> <r​ucknium:monero.social> (The Matrix bridge seems to be working)

17:02:43 <Rucknium> Thank you, DataHoarder, for setting up the bridge

17:03:09 <Rucknium> 2) Updates. What is everyone working on?

17:04:05 <vtnerd> last week more lws stuff (ci and "hardening" chain syncing), with a tiny bit of noise. Plan
to focus more on noise protocol (or transition to ssl)

17:04:38 <vtnerd> the annoying hold up is handling a mismatch between the expected encryption status an actual
(i.e. node disables encryption after previously enabling it, etc)

17:05:16 <Rucknium> Me: I am taking a wider view of the inaccuracy problem with the dependent ring members.
The dependent ring members creates some inaccuracy, but it is not the only inaccuracy. Fitting a parametric
distribution and taking into account the "moving target" over time also add inaccuracy. So I am trying to
measure total inaccuracy now.

17:05:17 <vtnerd> as far as ssl goes, I thought about it somre more and am still considering switching. I
think we are better off "stealing" the openvpn port instead of the ssl port htough

17:07:04 <Rucknium> vtnerd: Thanks. Are you getting feedback from others about the choice between SSL and
Noise? Sorry that you are not really getting feedback during MRL meetings.

17:10:34 <vtnerd> the annoying hold up is handling a mismatch between the expected encryption status an actual
(i.e. node disables encryption after previously enabling it, etc)

17:11:29 <vtnerd> rucknium: only feedback from jeffro

17:11:54 <vtnerd> I'll ping a few others privately to see what they think

17:12:26 <Rucknium> The Curve Trees paper will be presented at the USENIX Security Symposium. Tomorrow 3:15pm
(Local time I think): https://www.usenix.org/conference/usenixsecurity23/technical-sessions

17:12:39 <Rucknium> kayabaNerve's Full Chain Membership Proofs (FCMP) uses Curve Trees.

17:12:39 <vtnerd> how do you ping people behind the m-relay? that stinks

17:13:22 <Rucknium> For private messages? I think you cannot use this bridge for PMs.

17:14:02 <m-relay> <r​ucknium:monero.social> DataHoarder: Do you know if the bridge can be used for PMs
between IRC and Matrix users?

17:14:09 <DataHoarder> currently not sadly

17:14:39 <DataHoarder> you can ping people by mentioning their full matrix user, matrix clients will pick it
up that way

17:14:55 <DataHoarder> for example @rucknium:monero.social

17:15:49 <DataHoarder> I can look over the weekend for privileged setups that offer 1:1 users, for now the
bridge is simple and I will let you keep your meeting going :) (ping me elsewhere about this/later)

17:17:02 <Rucknium> Matrix Element gives a red ping for just my username: rucknium. Matrix users need to do
@Rucknium:libera.chat to properly ping IRC users in a chat room I believe.

17:18:00 <Rucknium> I don't think the USENIX conference is being streamed or recorded. If anyone happens to be
there, let us know how the Curve Trees presentation is!

17:19:08 <Rucknium> 3) Discussion. Anything to discuss?

17:22:10 <Rucknium> There are three dev/research CCS proposals on the Merge Requests list. Boog900's proposal
to work on Cuprate, a Rust implementation of monerod. selsta's part-time development. kayabaNerve's Full Chain
Membership Proofs.

17:22:47 <Rucknium> Comments can be left here: https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests

17:24:16 <Rucknium> Looks like we can end the meeting here. Thanks everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-08-08T18:32:58+00:00
- Closed at: 2023-08-22T22:33:13+00:00
