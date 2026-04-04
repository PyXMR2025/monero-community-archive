---
title: 'Monero Community Workgroup Meeting: Saturday 14th January 2023 @ 16:00 UTC'
source_url: https://github.com/monero-project/meta/issues/779
author: plowsof
assignees: []
labels: []
created_at: '2023-01-11T08:32:11+00:00'
updated_at: '2023-01-15T09:45:54+00:00'
type: issue
status: closed
closed_at: '2023-01-15T09:45:00+00:00'
---

# Original Description
Location: [Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

[Instructions for joining the monero.social Matrix server.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time
16:00 UTC [Check your timezone](https://www.timeanddate.com/worldclock/converter.html)

Moderator: plowsof

Please reach out in advance of the meeting if you would like to propose an agenda item.

Proposed Meeting Items:

1. Introduction
2. Greetings
3. Community highlights    
- [p2pool hardforking to reduce chain bloat] (https://www.reddit.com/r/MoneroMining/comments/1095730/psa_p2pool_network_upgrade_aka_hardfork_on_march/) Credit goes duggavo who posted [this issue](https://github.com/SChernykh/p2pool/issues/221) on Github. Testing shall begin next week according to xmrig/p2pool dev sech1 ([who provides instructions here](https://github.com/SChernykh/p2pool/issues/153))
- jeffro256 found something that [isn't an issue](https://libera.monerologs.net/monero-dev/20230114#c188411) but could have been - kayaba/sech are on it, more eyes on the code the better! thanks jeff!

News: [Monero Observer](https://www.monero.observer/) - [Revuo Monero](https://revuo-xmr.com/) - [The Monero Standard](https://localmonero.co/the-monero-standard)
5. [CCS updates](https://ccs.getmonero.org/)    
  b. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/357)    
  d. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/366) 

Sentiment in the [previous](https://github.com/monero-project/meta/issues/775) meeting
Merge:
f. [koe seraphis library work 2](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/369)     

Close:
a. [xmr-btc-swap development and improvement](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/355) 
e. [Empower Lebanon(and similar hyperinflated countries) to use Monero instead of fiat(educational and bartering platform/guerilla marketing/workshops)](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/367)   
 
6. Workgroup reports    
  a. Dev workgroup
  b. Localization workgroup
  c. Outreach workgroup
  d. Events workgroup - [MoneroKon 2023](https://github.com/MoneroKon/)
  e. Website workgroup
  f. Policy workgroup
  g. Research workgroup
  h. [Seraphis Migration workgroup](https://github.com/seraphis-migration)
7. Open ideas time    
8. Confirm next meeting date/time    

[Previous meeting including logs](https://github.com/monero-project/meta/issues/775)    

Meeting logs will be posted here afterwards.    


# Discussion History
## plowsof | 2023-01-15T09:44:59+00:00
Logs 
```
16:00:31 <plowsof11> Meeting time https://github.com/monero-project/meta/issues/779

16:00:35 <plowsof11> Greetings

16:00:36 <plowsof11> hello

16:00:58 <ofrnxmr[m]> Greetings

16:00:59 <Lovera[m]> Hi

16:01:26 <Rucknium[m]> Hi

16:01:28 <hinto[m]> hi i'm here

16:02:19 <plowsof11> Community highlights - what happened this week?

16:02:39 <Siren[m]> Hello, quick update about The Monero ATM Project ❗️Our main parts have arrived and we
already started to program libraries starting with the bill acceptor (ccTalk).

16:02:39 <Siren[m]> All the progress/ideas/technical information/videos 📹️ can be found on our Matrix room
linked on the website. 🏧 https://atm.monero.is
http://xmratmkz4ehs3ejl2x23fuski4tkw4sjkqlted445bkwx3dmhtbu5sid.onion

16:03:40 <plowsof11> very promising, wishing the atm a safe journey to MoneroKon!

16:04:13 <plowsof11> [p2pool hardforking to reduce chain bloat]
(https://www.reddit.com/r/MoneroMining/comments/1095730/psa_p2pool_network_upgrade_aka_hardfork_on_march/)
Credit goes duggavo who posted [this issue](https://github.com/SChernykh/p2pool/issues/221) on Github. Testing
shall begin next week according to xmrig/p2pool dev sech1 ([who provides instructions
here](https://github.com/SChernykh/p2pool/issues/153))

16:04:54 <plowsof11> the transactions on testnet are ready for the p2poolers
https://community.rino.io/explorer/testnet/

16:05:09 <ofrnxmr[m]> Not sure how this prevents a had actor from deploying the old p2pool, but havent thought
about it either

16:05:44 <plowsof11> anyone can help test the p2pool HF next week btw,, only need a tiny amount of hashes

16:06:01 <plowsof11> - jeffro256 found something that [isn't an issue](https://libera.monerologs.net/monero-
dev/20230114#c188411) but could have been - kayaba/sech are on it, more eyes on the code the better! thanks
jeff!

16:06:16 <plowsof11> this is on going and i don't know much about it but looks like its being handled ^

16:06:53 <sech1> we found a solution already

16:07:07 <sech1> check #monero-dev logs

16:07:17 <MSvB[m]> Hello.

16:07:33 <plowsof11> hello MSvB!

16:08:06 <Rucknium[m]> AFAIK, continuing the old P2Pool chain is possible. It's a question off if there would
be enough hashpower on the old chain for anyone to want to mine on it.

16:08:23 <plowsof11> great work sech1, thanks!

16:09:11 <plowsof11> GUPAX will be ready for the p2pool hardfork hinto ? 😁

16:09:26 <hinto[m]> is the chain bloat mostly from consolidation? i remember being surprised at how small the
p2pool payout outputs were

16:09:36 <sech1> gupax and monero-gui just need to pull the latest binaries and they'll be ready

16:09:41 <hinto[m]> i think it turned out to be less than a megabyte a day?

16:09:45 <sech1> bloat is from consolidation

16:09:57 <MSvB[m]> Hi plowsof @plowsof:matrix.org

16:10:45 <plowsof11> there will be an events meeting in #monero-events:monero.social at 18:00UTC for those
wondering

16:10:53 <Rucknium[m]> Next week I will release my findings about centralized mining pools (accidentally)
delaying transaction confirmations. Any commentary on it? Has anyone noticed this with your own transactions?

16:11:45 <hinto[m]> i've mined a smaller coin where a majority of the nodes were also operated by the biggest
pool

16:12:00 <hinto[m]> and it seemed like they rejected any hashes from solo miners (including me)

16:12:38 <Rucknium[m]> hinto: IMHO, the big issue is the privacy problems with normal users' effective ring
sizes being 1-3 units lower than intended, due to them including p2pool outputs

16:13:07 <plowsof11> oh almost forgot - ofrnxmr found that marking a node as trusted reduces initial network
traffic - for redeeming a giftcard this means instead of 20 seconds - its now 6 seconds , thanks ofrnxmr

16:13:33 <ofrnxmr[m]> We shall see

16:13:34 <Rucknium[m]> See https://github.com/monero-project/research-lab/issues/109

16:14:57 <hinto[m]> agreed, you hate to see multiple coinbase transactions in the ring

16:15:54 <plowsof11> anything else on anyones mind before we discuss the ccs proposals?

16:17:24 <plowsof11> if we could quickly look at the 'sentiments from the last meeting' here
https://github.com/monero-project/meta/issues/779

16:17:25 <ofrnxmr[m]> Stack wallet and cake both support trusted nodes now btw

16:17:37 <plowsof11> is there anyone who disagrees with the merge / close list ?

16:17:56 <plowsof11> koe to funding, close commit / lebanon

16:21:33 <plowsof11>   b. [CypherPunk Radio](https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/357)

16:21:57 <plowsof11> i had direct messagedNotMtth after last meeting

16:22:35 <plowsof11> meant to be giving them a chance to act on the feedback

16:23:07 <plowsof11> no updates / nothing new though

16:23:09 <ofrnxmr[m]> I agree

16:23:18 <ofrnxmr[m]> With merge close list

16:23:36 <plowsof11> thanks

16:23:36 <monerobull[m]1> <plowsof11> "koe to funding, close commit..." <- Agreed

16:23:55 <plowsof11> we have nothing to discuss for cypherpunk radio tbh

16:24:32 <monerobull[m]1> Close

16:25:20 <plowsof11> ajs gave some statistics for their radio project - lack luster. the only saving grace for
radio is the small amount , but even sitll not much interest in terms of votes / sentiment

16:25:39 <Rucknium[m]> On Cypherpunk Radio, if a proposer doesn't have the motivation or capability to follow
through with the steps and feedback of a proposal, they likely won't follow through on implementation after
funding.

16:26:17 <plowsof11> i agree

16:26:47 <monerobull[m]1> If you plan on being a community-funded community radio you could at least attend
community meetings

16:27:01 <ofrnxmr[m]> Id be ok with closing just because it seems to be a resource hog without much to gain
from it

16:27:37 <plowsof11> moving on

16:27:46 <plowsof11>   d. [Create Educational Content in Spanish](https://repo.getmonero.org/monero-
project/ccs-proposals/-/merge_requests/366)

16:28:14 <ofrnxmr[m]> Any news on the sponships

16:28:23 <plowsof11> thanks Lovera for the update here https://repo.getmonero.org/monero-project/ccs-
proposals/-/merge_requests/366#note_20324

16:28:32 <Rucknium[m]> Some people probably cannot attend community meetings due to time conflicts. That
shouldn't be a requirement. But they can leave comments on the CCS proposal or post comments here before/after
meetings

16:28:43 <Lovera[m]> Hello everyone!  Sorry for not being able to attend the previous meeting.

16:28:51 <Rucknium[m]> Or message plowsof

16:28:53 <plowsof11> yes can definitely post on the ccs if unable to attend (as others have done)

16:29:07 <ofrnxmr[m]> Rucknium:  he does usually attend, to be fair

16:29:17 <ofrnxmr[m]> The quote could be aimed at everyone

16:30:05 <ofrnxmr[m]> Regarding lovera update,

16:30:08 <ofrnxmr[m]> Close er

16:30:25 <Lovera[m]> Regarding cakewallet, as I have commented in the ccs, "Unfortunately I am unable to
disclose that information. However, I don't think this will influence in any way as there is no rule in this
regard. The work submitted and the money required for it, is something completely different from the
cakewallet sponsor."

16:31:03 <ofrnxmr[m]> For all I know you make more in sponsorships than you are hoping to milk us for.

16:31:03 <ofrnxmr[m]> Could ve that you get peanuts

16:31:03 <ofrnxmr[m]> Business =/= speculation

16:31:03 <ofrnxmr[m]> So I must say, no

16:31:06 <plowsof11> technically not breaking any rules (from what i can see) - its just peoples opinions now
if that 'ok'

16:31:24 <ofrnxmr[m]> You dont have to break a rule

16:31:30 <ofrnxmr[m]> You're not entitled to funding just because you didnt break rules

16:31:53 <Lovera[m]> > <@ofrnxmr:monero.social> For all I know you make more in sponsorships than you are
hoping to milk us for.... (full message at
<https://libera.ems.host/_matrix/media/v3/download/libera.chat/db471420c98705fe293f1f3718bf3f53528501ed>)

16:32:40 <plowsof11> not so much a rule but - ' if you want thier upvote / support '

16:33:15 <nioc> ofrnxmr[m]: is Lovera[m] getting funding elsewhere for what they are proposing?

16:33:16 <ofrnxmr[m]> If I get 100k a year from cake to advertise them on NY twitter

16:33:17 <Rucknium[m]> With these new CCS videos, do you intend to omit mention of Cake sponsorship in all of
them?

16:33:29 <ofrnxmr[m]> And then I ask community for 10k to run that same twitter account

16:33:32 <ofrnxmr[m]> You dont see the issue?

16:33:36 <Lovera[m]> This is monero, the mere fact of having to share financial information should already be
a problem. I have had no problem showing you my YT income, you might be surprised by cake's income but I am
not allowed to disclose this information.

16:33:45 <ofrnxmr[m]> nioc:  yes

16:34:04 <nioc> mentioning cake sponsorship in the videos sounds like free advertising of cake  :D

16:34:48 <Lovera[m]> plowsof11: Support from only ofrnxmr?   There are other proposals that were in the same
situation as mine and have passed to funding. A proposer could submit a proposal and also work part-time. What
is the problem?

16:35:01 <ofrnxmr[m]> Paid advertising* cake sponsors them

16:35:16 <ofrnxmr[m]> You mean observed

16:35:22 <ofrnxmr[m]> You forgot about moon

16:35:32 <ofrnxmr[m]> Observer*

16:35:49 <Lovera[m]> nioc: This is completely different work than 5 cakewallet videos

16:35:52 <ofrnxmr[m]> And dont get me wrong, I will be asking observer

16:36:09 <nioc> ofrnxmr[m]: are you saying that cake already paid lovera for the content that they are
proposing in this CCS?

16:36:09 <plowsof11> for the people who ' not disclosing cake sponsorship '  (is not an issue) then it would
be good to make clear that - " this is a community sponsored video "  (and include no other advertisers in it

16:36:31 <plowsof11> cake are sponsoring 5 videos per month

16:37:12 <ofrnxmr[m]> Not sure. They cant say what they were paid or what for

16:37:17 <ofrnxmr[m]> Only that that the project in question already generates income

16:37:24 <plowsof11> the ccs would be sponsoring extra content - on loveras main channel iirc

16:37:26 <Lovera[m]> Of course, I mean, have you read the proposal? xD

16:37:26 <Lovera[m]>  this is completely different work!! this include even more videos in my other channel
YT. W/o cakewallet sponsor .. How can I apply for financing and at the same time place cakewallet ads?

16:38:25 <ofrnxmr[m]> Lots of wordgames being played here

16:38:35 <ajs_[m]> Yes, xmr.radio had strong start, but died down after a few months

16:39:08 <Lovera[m]> Cakewalelt promotes 5 videos per month. This is something totally separate. Can't I work
part time and at the same time launch a proposal? It sounds really strange, actually.... There is NO rule for
this.

16:39:08 <Lovera[m]> This job is completely dedicated to the Monero community. I would even make videos
without youtube ad (no monetization).

16:39:08 <ajs_[m]> I didn't renew radio license subscription and switched over creative commons music to cut
costs

16:39:08 <Lovera[m]> More than marketing is a help to the whole spanish community.

16:39:14 <ofrnxmr[m]> You have multiple channels

16:39:14 <ofrnxmr[m]> one of those is a large channel

16:39:14 <ofrnxmr[m]> One is smaller and dedicated to monero

16:39:21 <ofrnxmr[m]> Which channel do you refer to

16:39:31 <Lovera[m]> Take a look at the videos related to the mining or Nodes of monero... Many visualizations
that help people.

16:39:32 <ajs_[m]> And run the stream at least until the domain expires July 2023

16:39:33 <nioc> people come for funding of content that few people are going to see.  Here we have a proposal
for a channel that actually gets views.

16:39:46 <plowsof11> thank you for this information ajs_ (xmr.radio is still a great project)

16:39:47 <Lovera[m]> ofrnxmr[m]: Both... I will post in both channels

16:40:10 <Rucknium[m]> It's still not clear to me whether Cake sponsorship will appear in these proposed CCS
videos.

16:40:56 <plowsof11> so for the people who do not care about the disclosing of cakes sponsorship - then take
Ruckniums suggestion and state clearly in the proposal - that the community sponsored videos will not be
monetised / advertise anything else

16:41:16 <ofrnxmr[m]> Lovera[m]: Which one does cake sponsor

16:42:10 <Lovera[m]> Rucknium[m]: Guys, I repeat again. The work proposed in the CCS is solely and exclusively
for the community. No cakewalelt ads, no youtube ads (although sometimes youtube adds them without
permission). it is a work completely apart from cakewallet's sponsorship.

16:42:29 <plowsof11> nice, just write that in the proposal to be clear

16:42:44 <Rucknium[m]> Lovera: Thanks for clarifying

16:42:55 <ofrnxmr[m]> There's nothing wrong with having multiple sponsors..

16:43:54 <Lovera[m]> plowsof11: I will update the CCS to make it even clearer.

16:44:48 <plowsof11> and then people must vote on the gitlab if they support

16:45:12 <monerobull[m]1> Next item please

16:45:16 <ofrnxmr[m]> Im a she, not a person

16:45:31 <ofrnxmr[m]> Not a people**

16:45:44 <monerobull[m]1> ofrnxmr[m]: You're a ringsig

16:45:59 <plowsof11> there are no other items

16:46:21 <monerobull[m]1> Cool

16:46:26 <plowsof11> AOB?

16:46:54 <ofrnxmr[m]> Next week

16:46:55 <ofrnxmr[m]> Monero meet

16:46:58 <monerobull[m]1> Nice

16:47:30 <Rucknium[m]> I'm going to use txstreet.com to explain the tx confirmation delay issue. So thanks to
CCS donors for supporting txstreet in 2021.

16:47:36 <monerobull[m]1> What time?

16:47:52 <ofrnxmr[m]> Txstreet is awesome

16:47:52 <ofrnxmr[m]> The 24th, not sure the time

16:47:52 <ofrnxmr[m]> sgp:

16:47:56 <plowsof11> when they get kicked off the bus?

16:48:11 <ofrnxmr[m]> Ive seen that

16:48:24 <ofrnxmr[m]> Yesterday actually.

16:48:35 <ofrnxmr[m]> Bus wasnt full but 5 or so people got booted

16:48:48 <Rucknium[m]> That's what's happening. Of course, I collect the data directly from nodes rather than
txstreet.

16:48:51 <plowsof11> theres a tx here thats been waiting for nearly 7 hours .. could definitely use a seat
https://community.rino.io/explorer/testnet/txpool

16:49:01 <ofrnxmr[m]> Rucknium:  amateue

16:49:08 <Rucknium[m]> My motto is "Keep the Isabellas on the bus"

16:49:31 <ofrnxmr[m]> I have a feeling those long lineups are coming

16:49:58 <plowsof11> new transactions with the same fee get to sit on the bus - not fair

16:50:23 <monerobull[m]1> ofrnxmr[m]: Then the bus just gets larger silly

16:51:40 <ofrnxmr[m]> Monero unconfirmed racist

16:52:00 <ofrnxmr[m]> monerobull @monerobull:matrix.org:  🐒 does it tho 🥳

16:52:40 <plowsof11> looking forward to the demonstration Rucknium , hopefully its recorded or planned so we
can see?

16:53:18 <ofrnxmr[m]> Screenrecording ftw

16:53:19 <Rucknium[m]> I just take screenshots. It's in blog/Reddit form

16:53:26 <plowsof11> ok good

16:54:31 <plowsof11> with great sadness, it seems its time to end the meeting

16:54:54 <hinto[m]> wrap up by listing ccs proposals that have consensus?

16:55:25 <Rucknium[m]> Litecoin is beating Monero in speed to first transaction confirmation. Did you know
that? Now you do

16:55:34 <Rucknium[m]> Litecoin block time is 2 minutes 30 seconds. Monero's is 2 minutes flat (on average)

16:55:53 <plowsof11> radio seems to have consensus of "meh" and "close"

16:56:47 <plowsof11> lovera's is ready for your opinions / votes after showing their hand / clarifying things

16:57:16 <ofrnxmr[m]> Poke it with a stick, see if it does something

16:57:54 <plowsof11> the others are listed in the issue (koe to funding, close lebanon/commit)

17:00:02 <plowsof11> thank you all for attending x

17:00:29 <monerobull[m]1> Thanks for hosting

17:01:06 <plowsof11> events meeting in 1 hour 🤝

17:01:34 <MSvB[m]> Thanks everyone for good meeting and great moderation plowsof @plowsof:matrix.org.

17:01:55 <hinto[m]> ty plowsof

17:02:06 <hinto[m]> speaking of, shouldn't you be getting payed?

17:02:21 <ofrnxmr[m]> A long time sgo

17:02:26 <ofrnxmr[m]> But luigi paid mj instead

17:02:36 <ofrnxmr[m]> 🙊

17:02:41 <monerobull[m]1> Kek

17:03:32 <ofrnxmr[m]> He's like 4+ months UB lol

17:03:43 <ofrnxmr[m]> Has been going since the proposal was proposed

17:04:12 <plowsof11> i am a masochist and have requested and received 1 payout : and am imposing more delays
until i have surpassed the workload of the 1st period

17:04:56 <ofrnxmr[m]> 1/4, not bad

17:05:44 <ofrnxmr[m]> I mean, working for 25% of the stated rate is awesome. Thanks for being so generous

17:06:02 <plowsof11> im unsure of what my path should be - focus on the (perhaps irrelevant) work in progress
list : e.g. xmrsale's abandoned proposal  ~ what to do with the remaining funds or should i focus on (perhaps
important) things such as getting people to look at the 10block lock again? 'no library left behind'?

17:06:40 <ofrnxmr[m]> Should be collect you pay and keep doing what your doing

17:07:01 <monerobull[m]1> Can I get paid for something too pls

17:07:09 <plowsof11> i have focussed more on the gui / testing recently and taken more a backseat in terms of
ccs proposals

17:07:31 <blankpage[m]> Clearly I have missed the meeting but I'd just like to say I broadly agree with the
apparent consensus on each CCS proposal. I think a radio stream requires passion more than funding to get the
word out and it should be able to stand on it's own two feet. We could pay 1000s for the slickest stream ever
but there is no guarantee of an audience.

17:08:55 <plowsof11> "helping" ccs proposers 'behind the scenes' can be misinterpreted as favouritism and
such. it seems best to keep it in the open

17:09:24 <ofrnxmr[m]> monerobull[m]1: No

17:09:30 <ofrnxmr[m]> I wont use your referral

17:09:35 <blankpage[m]> I think Lovera is a better investment as they have established audience, although I'd
suggest to them to have a single channel rather than 2 and to try and get their backlog onto other platforms

17:09:38 <ofrnxmr[m]> I might waste your time though..

17:10:15 <ofrnxmr[m]> ... what a guy 😅🤣

17:10:20 <plowsof11> thanks for input blankpage

17:10:25 <monerobull[m]1> Sirs why hasn't the money been taken out of my account yet

17:12:16 <ofrnxmr[m]> Helping them find instructions on creating it etc is all good and fine

17:12:39 <ofrnxmr[m]> But coaching them just leads to people saying "plowsof is my friends so let me in"

17:12:39 <plowsof11> a user called tom asked for help (in 10 monero channels) and ofrnxmr / monerobull
provided support - but every time tom kept insisting on returning to step one and posting screenshots with
arrows

17:13:16 <monerobull[m]1> The numbers didn't even make any sense

17:14:28 <blankpage[m]> plowsof @plowsof:matrix.org:  I think clearing out the junk in the CCS WIP category is
very important work. Any funds which are returned to the general fund can be put to good use

17:14:33 <ofrnxmr[m]> 0.1234

17:15:08 <monerobull[m]1> And then he just states "thank you very much I've done it thanks to you"

17:15:12 <nioc> yes WIP and completed is not.....complete

17:15:16 <monerobull[m]1> And didn't use my referral code

17:15:20 <ofrnxmr[m]> Nit exactly blankpage:

17:15:24 <ofrnxmr[m]> Id prefer those funds not go to GF

17:15:24 <nioc> I would like to make a CCS proposal for NGU

17:16:11 <blankpage[m]> Why would it be better for funds for abandoned projects not to return to general fund?

17:16:26 <ofrnxmr[m]> No overisight

17:16:58 <nioc> isn't that the stated rule?

17:16:59 <ofrnxmr[m]> Who's to say that the money is put to good use?

17:16:59 <ofrnxmr[m]> Id prefer it be earmarked for future ccs or something

17:17:08 <ofrnxmr[m]> It is

17:17:12 <plowsof11> for xmrsale - there are 30xmr - the project is a fork - that has fell behind the master
branch and is abandonned and not used - monero wordpress remains king

17:17:24 <monerobull[m]1> Monerotopia is live rn

17:17:24 <monerobull[m]1> Join on stage: https://streamyard.com/bdyrcgcs7a

17:17:24 <monerobull[m]1> Watch: https://www.youtube.com/watch?v=VhM39knZcU8

17:17:35 <nioc> but having CCS stay in CCS has some sort of simple logic

17:17:51 <nioc> but how is it determined where it goes?

17:18:12 <plowsof11> currently the "lowest hanging fruit" is "xmrsale" imo

17:18:29 <blankpage[m]> I assumed the purpose of general fund was to pay for worthy CCS and some hosting costs

17:18:51 <nioc> yes the GF does contribute to some CCSs

17:19:05 <nioc> so it does go back, and more

17:19:22 <plowsof11> yes the general fund is paying for things each month : but it is currently heaviy
subsidised by donators https://www.getmonero.org/community/sponsorships/

17:19:35 <plowsof11> s/heaviy/heavily

17:20:42 <plowsof11> ok then, lets pick xmrsale and ruin the developers life / stop them from returning when
xmr moons

17:20:49 <plowsof11> to claim remaining funds

17:21:46 <blankpage[m]> For previous abandoned WIP CCSs which you have resolved, were the funds mostly
returned to the general fund?

17:22:54 <plowsof11> i've resolved nothing

17:23:00 <nioc> lol

17:23:01 <monerobull[m]1> Failure

17:23:24 <plowsof11> other than tryptych - which resolved itself - confirmed failure

17:23:25 <ofrnxmr[m]> <nioc> "but how is it determined where..." <- Is say by percentage

17:26:19 <blankpage[m]> I see. This list is long and many things seem abandoned

17:26:19 <blankpage[m]> https://ccs.getmonero.org/work-in-progress/

17:26:19 <blankpage[m]> so reclaiming some funds to be ringfenced for "critical" dev work seems a very worthy
cause

17:28:30 <plowsof11> purgatory has "xmrssale" "monero outreach 3" and "payment gateways"
https://github.com/plowsof/ccs-wip-list

17:28:58 <plowsof11> would be simpler to "pick one" and get it resolved

17:31:09 <plowsof11> we have an outreach proposal up for voting now - and outreach 3 has (it seems) 30+
collecting dust

17:31:31 <ofrnxmr[m]> The problem with flushing

17:31:38 <ofrnxmr[m]> Is NOTJING stops a round robin

17:31:52 <ofrnxmr[m]> They can come back and milk donors again and just keep funneling into GF

17:32:51 <plowsof11> anhdres when monero garden update

17:32:55 <ofrnxmr[m]> Like, first proposal 250xmr, gets paid 100, disappears, 150 go to gf

17:32:55 <ofrnxmr[m]> Proposer returns to complete the project at a cost of 250xmr

17:33:29 <blankpage[m]> The github page is very well organized and certainly saves me some clicks. Yes I would
say resolving any of those lost causes would be good. I suppose there could be some rule where there is a set
period for community feedback on what should be done with abandoned funds and perhaps certain proposals could
qualify for "recycled" funds if there is a big need for the work.

17:34:37 <ofrnxmr[m]> Also need some sort of rule where the proposer cannot open a new proposal for more than
the remained of the previous

17:35:09 <blankpage[m]> I.e. once a WIP CCS is certified abandoned, you could add the fate of the funds the
agenda for these meetings for X number of weeks

17:35:25 <ofrnxmr[m]> In the example k gave, that proposal would be able to return tl complete it at a cost of
150xmr, which should be sitting somewhere from the prior campaign

17:35:50 <ofrnxmr[m]> The problem is.. abandoned is only as far as greed and memory

17:36:45 <ofrnxmr[m]> People are more than happy to push something like haveno, regardless of the bleeding or
abandonment

17:36:55 <plowsof11> i think its clear to mark xmrsale as abandonned

17:36:59 <ofrnxmr[m]> Havent front end*

17:38:05 <ofrnxmr[m]> plowsof @plowsof:matrix.org:  I agree

17:38:05 <ofrnxmr[m]> Some of these ccs should be tread lighrlyl though

17:38:17 <blankpage[m]> My understanding is that ultimately  the decision rests with the mysterious "core" or
"Luigi" , but the system I just outlined at least gets the community involved in the decision making process.

17:38:17 <blankpage[m]> It would be better if the original donors could decide but obviously that is
impossible

17:41:54 <ofrnxmr[m]> Right. Its a problem to pay for goods and never receive them, and then have bad actors
campaign saying how YOU robbedtheir donors

17:41:55 <ofrnxmr[m]> Wait😃 didnt that just happen

17:42:40 <blankpage[m]> Did I miss some drama? Do I want to know? 🫣

17:43:37 <plowsof11> unrelated: the "no library left behind" was for the future developers building upon
seraphis / current code base (the c abi thing) - e.g. a small pilot ccs to "do the c abi thing" and "show the
benefits for monero-javascript" specifically (as this appears to be the most used / actively developed 'thing'

17:43:39 <plowsof11> do i have any idea what that entails? no

17:43:46 <ofrnxmr[m]> You dont want to know

17:44:17 <ofrnxmr[m]> Testnet wen

17:44:42 <blankpage[m]> What is "the c abi thing"?

17:44:54 <plowsof11> i have no idea

17:45:09 <ofrnxmr[m]> Hard to build on no-testnet

17:45:22 <plowsof11> something about turning spaghetti into lego blocks

17:45:28 <ofrnxmr[m]> Gotcha

17:45:34 <plowsof11> more info here https://github.com/seraphis-migration/strategy/issues/2

17:45:56 <ofrnxmr[m]> Yeah. Direction

17:46:30 <plowsof11> i would say the "c abi thing" is a gaping wound for alot of developers. 10 block lock
issue is a pain point for users.

17:48:59 <blankpage[m]> Well that c abi issue is outside of my current knowledge but if there is no one coming
forward to build it and it is badly needed then isn't that what the bounties website is for?

17:50:57 <SerHack> Sorry for OT: if you need assistance with Monero Integrations, please open a new ticket on
https://support.monerointegrations.com Thanks in advance!

17:50:59 <blankpage[m]> Bounty would need to be clearly specified and written by someone who understands the
problem

17:52:51 <plowsof11> thanks SerHack. indeed , ideally it would be a small 'pilot' project - which would
benefit e.g. "monero-js" (i say this as it seems the most widely used thing at the moment which would
"benefit") - i believe there is 'on going-maintenance' involved too. but yeah, have to see woodsers thoughts..
if it would even benefit them 🤷

17:53:39 <ofrnxmr[m]> SerHack:  purgatory, no?

17:53:48 <ofrnxmr[m]> Whats the story

17:56:48 <plowsof11> the goals / issues may have changed now (with it being so old) - could work something out
to put the funds towards "new improvements of monero-wp" for another contributor willing to take them up


```
Automated by [this](https://github.com/plowsof/post-libera-meeting-logs)

```
SerHack: my CCS is still opened, if anyone wants to take the bounty for improving and implementing the features I planned, go ahead and contact me.
```

# Action History
- Created by: plowsof | 2023-01-11T08:32:11+00:00
- Closed at: 2023-01-15T09:45:00+00:00
