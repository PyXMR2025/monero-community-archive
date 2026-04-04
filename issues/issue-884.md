---
title: Monero Research Lab Meeting - Wed 23 August 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/884
author: Rucknium
assignees: []
labels: []
created_at: '2023-08-22T22:32:54+00:00'
updated_at: '2023-08-29T22:06:47+00:00'
type: issue
status: closed
closed_at: '2023-08-29T22:06:47+00:00'
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

#880 

# Discussion History
## plowsof | 2023-08-25T19:13:58+00:00
Logs 
```
17:00:54 <Rucknium> Meeting time: https://github.com/monero-project/meta/issues/884

17:01:02 <Rucknium> 1) Greetings

17:01:04 <Rucknium> Hi

17:01:07 <m-relay_> <j​effro256:monero.social> Howdy

17:01:12 <rbrunner> Hello

17:03:01 <vtnerd> hi

17:03:56 <Rucknium> 2) Updates. What is everyone working on?

17:04:53 <m-relay_> <j​effro256:monero.social> Implementing my Jamtis F-R privacy changes

17:05:26 <m-relay_> <j​effro256:monero.social> https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d1702
4?permalink_comment_id=4665372#gistcomment-4665372

17:06:04 <Rucknium> Me: Did some more simulations about the ring member dependence issue. I think I have a
conclusion on it. Calculating numbers for risks with different N for the N block lock on spending outputs.
Reviewing preliminary results from compdec on EAE attacks and similar.

17:06:46 <m-relay_> <j​effro256:monero.social> How do risks change with different block lock levels?

17:07:05 <Rucknium> That's what I was calculating

17:07:17 <m-relay_> <j​effro256:monero.social> Oh okay ;)

17:07:19 <Rucknium> The answer may surprise you :P

17:07:43 <Rucknium> I want to get to that in the discussion part of the meeting

17:08:36 <vtnerd> I pivoted from p2p-noise to p2p-ssl, hopefully will have something working by next week. The
first version should allow fingerprint "pinning" (server authentication)

17:09:07 <vtnerd> its looking to be much easier than noise to get in the existing tcp/server code (since it
already supports ssl)

17:09:28 <m-relay_> <j​effro256:monero.social> Awesome

17:09:41 <rbrunner> "Easier" sounds great, yeah

17:09:41 <vtnerd> I made the decision after talking to few other people privately, there wasnt much push for
noise and the benefits are small given that I scaled things back from the original plan anyway

17:10:29 <vtnerd> yeah the noise code had to buffer messages before the noise handshake completed, or be
implemented in the tcp server directly like ssl is

17:11:39 <Rucknium> Thanks, vtnerd

17:11:44 <Rucknium> 3) Discussion

17:11:57 <m-relay_> <c​ompdec:matrix.org> I'm a bit late, but here now.  I shared a rough draft of some EAE
results, and I'll be adding a couple more sections for friday

17:13:09 <m-relay_> <j​effro256:monero.social> Honestly yeah SSL E2E encryption is probably better anyways for
uniformity with other networks... I'm glad that's being worked on

17:13:47 <Rucknium> compdeec: Thanks. I am about halfway through it. Stopped to run some of my own simulations
about some issues you raised :)

17:15:04 <rbrunner> I wonder a bit that jeffro256 is already implementing his Jamtis changes

17:15:10 <rbrunner> Isn't it a bit early for that?

17:15:23 <m-relay_> <c​ompdec:matrix.org> Cool.  It's going to take a while to parse, there are a lot of ideas
in a lot of different directions

17:15:27 <Rucknium> jeffro256: Do you want to discuss your Seraphis Find-Receive privacy proposal?

17:16:07 <rbrunner> Or is this more in the sense of "rapid prototyping" to see where it really leads?

17:20:22 <m-relay_> <j​effro256:monero.social> Yeah so the basic idea behind the Jamtis changes is that ex
extra pubkey is added to the address, so that senders can do 2 different DH operations to a given address. The
keys for each DH op are used to recompute view tags and nothing else. Only when you combine access to both
private keys can you calculate the main sender-receiver secret, decrypt address tags, and recompute
one-t<clipped mes

17:20:23 <m-relay_> <j​effro256:monero.social> ime addresses. The pros of this scheme are threefold: 1) light
wallet servers can't strongly identify incoming enotes to known public addresses, 2) can't strongly identify
incoming enotes sent to the same address twice and 3) can generate receive addresses for you AND calculate
view tags without learning any additional balance recovery information. The cons are that the address
si<clipped mes

17:20:23 <m-relay_> <j​effro256:monero.social> ze increase from 196 to 244 characters and light wallet
scanning on the client side is slightly slower

17:20:56 <m-relay_> <j​effro256:monero.social> Yeah so the basic idea behind the Jamtis changes is that an
extra pubkey is added to the address, so that senders can do 2 different DH operations to a given address. The
keys for each DH op are used to recompute view tags and nothing else. Only when you combine access to both
private keys can you calculate the main sender-receiver secret, decrypt address tags, and recompute
one-t<clipped mes

17:20:56 <m-relay_> <j​effro256:monero.social> ime addresses. The pros of this scheme are three-fold: 1) light
wallet servers can't strongly identify incoming enotes to known public addresses, 2) can't strongly identify
incoming enotes sent to the same address twice and 3) can generate receive addresses for you AND calculate
view tags without learning any additional balance recovery information. The cons are that the address
s<clipped mes

17:20:57 <m-relay_> <j​effro256:monero.social> ize increase from 196 to 244 characters and light wallet
scanning on the client side is slightly slower

17:22:42 <rbrunner> So if you already implement, maybe you will soon be able to quantify that "slightly
slower"?

17:22:48 <m-relay_> <j​effro256:monero.social> I started implementing it now just to get the ball rolling
since it requires a non-trivial amount of effort. I'm received almost all positive responses thus far, but if
it's decided to not do it, then I'll just drop the code

17:23:22 <m-relay_> <j​effro256:monero.social> Yes, I def interested too see what the IRL performance
difference is

17:23:37 <Rucknium> In the status quo Seraphis proposal, if the light wallet server doesn't know the address
that the receiver gave to the sender, then the server doesn't have the "strongly identify" capability in the
first place?

17:23:42 <vtnerd> are we assuming full chain membership proofs with this proposal? the light-wallet server can
frequently compute the real spend because the client has to ask for dummies in a ring signature

17:24:12 <m-relay_> <j​effro256:monero.social> My hypothesis is that I/O dominates the processing time
anyways, so my changes won't really affect much, but I could be wrong

17:25:38 <m-relay_> <j​effro256:monero.social> If can make an extremely accurate guess about incoming enotes
to the same public address without actually knowing the address

17:25:42 <m-relay_> <j​effro256:monero.social> *it

17:26:24 <Rucknium> That's multiple tx sent to the same address, right? What if just one?

17:27:04 <m-relay_> <j​effro256:monero.social> If you successfully recompute view tags, then decrypt an enote
get the exact same address tag as another enote, both are almost guarantee to be owned by the user, barring
intentional sender shenenigans

17:27:57 <m-relay_> <j​effro256:monero.social> If there's just 1 enote sent to a public address, and that
address is not known, then the light wallet server gets no extra information

17:28:48 <m-relay_> <j​effro256:monero.social> That's a good question. This proposal doesn't touch on sender
privacy at all, just receiver

17:30:59 <m-relay_> <j​effro256:monero.social> But that dummy-request ring problem can be fixed by changing
your telegraphy yeah?

17:31:29 <Rucknium> What is telegraphy?

17:32:23 <m-relay_> <j​effro256:monero.social> Which information you send/reciver to/from server

17:32:39 <m-relay_> <j​effro256:monero.social> And which servers

17:33:35 <Rucknium> If the remote node model is used for light wallet servers to request candidate decoys, it
should be fine, right? Just get the output age distribution.

17:36:30 <vtnerd> no, it will typically leak the real spend

17:36:57 <vtnerd> or not wait, it won't nevermind, sorry for the noise

17:37:21 <vtnerd> the problem is that the light-wallet-server spec currently does the ring selection for the
wallet

17:37:33 <Rucknium> Depends on how much the server knows about which outputs the user owns, right?

17:37:46 <vtnerd> so currently the light-wallet-server can compute the real spend (since it generated the
dummy ring)

17:38:05 <vtnerd> no, the spec needs to be updated because currently it does the dummy selection for the
client

17:38:16 <rbrunner> That will probably change, seems to me, with the typical Seraphis/Jamits light server
knowing much less

17:39:15 <vtnerd> most likely this will change. the downside is that these clients will receive a large blob
of integers to handle

17:39:30 <vtnerd> I recall that being one of the reasons why the server does it, the server typically has more
ram and processing

17:39:39 <rbrunner> Maybe even "light server" or "light wallet server" will have to step back for more apt
terms, like "view tag selector" (just brainstorming)

17:39:52 <rbrunner> or "view tag checker"

17:40:07 <rbrunner> because there is not much more left, for the minimal such server, right?

17:42:51 <m-relay_> <j​effro256:monero.social> Luke and I have both talked about, but haven’t gotten around
to, caching the RCT enote distribution on the wallet side . It only ever extends, save for reorgs, isn’t that
much to store persistently, but it’s a lot to transmit all at once. It’s the perfect candidate for a
persistent cache. I think that’s within scope for a light wallet client to do (until FCMPs) w/o hurti<clipped
mes

17:42:51 <m-relay_> <j​effro256:monero.social> ng performance too much

17:43:30 <m-relay_> <j​effro256:monero.social> Would also be used by full wallets

17:43:50 <vtnerd> yeah, it doesnt really change so caching would work

17:44:19 <Rucknium> About how much data is it?

17:44:58 <rbrunner> I hope nobody seriously plans to put substantial new work into wallet2, e.g. to implement
such a cache alread today ...

17:45:17 <m-relay_> <j​effro256:monero.social> Yes, this will definitely affect sender privacy but thankfully,
can be done sort of efficiently by the client side and doesn’t rely on any Jamtis/Seraphis details AFAIK

17:45:27 <m-relay_> <j​effro256:monero.social> Uhhh I think like 3 MB?? I used to know off the top of my head

17:45:46 <vtnerd> I recall it being 6mb or so, moo would remember

17:46:22 <m-relay_> <j​effro256:monero.social> Well the exact same technique could be applied to wallet3 so
that effort wouldn’t be lost unless we significantly changed the decoy selection algorithm

17:46:39 <Rucknium> And it just scales up with number of blocks, not total tx volume, right?

17:46:53 <m-relay_> <j​effro256:monero.social> Yes

17:48:45 <rbrunner> You still lose some time with reviews, merge conflicts, etc., if you put something into
wallet2 first. That horse should be dead by now, in effect, if you ask me :)

17:50:40 <rbrunner> With me as the CEO of Monero we would probably have a hard feature freeze now on wallet2,
to move full steam ahead towards Seraphis/Jamtis. (Old boomer grumbling)

17:53:12 <Rucknium> I'll save N block lock for next meeting. By then I think I will have a writeup (unless I
find additional surprising things that I have to convince myself of.)

17:53:19 <Rucknium> Any other discussion?

17:55:27 <m-relay_> <j​effro256:monero.social> Guess I’ll just wait then ;)

17:56:28 <m-relay_> <j​effro256:monero.social> All hail Monero CEO

17:56:34 <rbrunner> :)

17:56:46 <rbrunner> Would be much more boring with me as that CEO

17:57:07 <rbrunner> Good it won't happen

17:57:53 <Rucknium> jeffro256: If you want the main part of the analysis, look at Table 1, Page 10 of
Rosenfeld (2014) "Analysis of hashrate-based double spending."
https://moneroresearch.info/index.php?action=resource_RESOURCEVIEW_CORE&id=191

17:58:40 <Rucknium> I wondered why some of those attack success probabilities in the table were so high.

17:58:59 <m-relay_> <j​effro256:monero.social> Thank you I’ll take a look at that for sure

18:00:58 <Rucknium> Do we agree that if the lock on spending outputs is N (i.e. N is 10 now), then an attacker
has to re-org N + 1 blocks, since that would include the spent output and the tx with that output in its ring,
which has 1 confirmation?

18:01:54 <Rucknium> Let's end the meeting here. Thanks everyone.


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

# Action History
- Created by: Rucknium | 2023-08-22T22:32:54+00:00
- Closed at: 2023-08-29T22:06:47+00:00
