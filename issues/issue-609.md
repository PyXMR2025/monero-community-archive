---
title: 'Community Workgroup Meeting: 18 September 2021 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/609
author: Keiji-C
assignees: []
labels: []
created_at: '2021-09-12T17:05:58+00:00'
updated_at: '2021-09-19T22:32:32+00:00'
type: issue
status: closed
closed_at: '2021-09-19T22:32:32+00:00'
---

# Original Description
**Location**

[Libera.chat, #monero-community](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-community:monero.social?via=matrix.org&via=monero.social)

**Time**

18:00 UTC
20:00 CET
19:00 Irish Time
14:00 Eastern Time
11:00 Pacific Time
03:00 (2021/09/**19**) 日本標準時 


[Use this timezone calculator to convert UTC to your time zone](https://www.timeanddate.com/worldclock/converter.html?iso=20210918T180000&p1=1440&p2=28&p3=111&p4=tz_et&p5=49&p6=179&p7=70&p8=224&p9=48&p10=136&p11=248).

**Moderator**
carrington

**Proposed Meeting Items**

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

- Introduction
- Greetings
- Community highlights
- CCS updates
- Workgroup report
    a. Daemon/CLI workgroup     
    b. Localization workgroup
    c. GUI workgroup 
    d. Outreach workgroup
    e. Defcon workgroup
    f. Website workgroup
    g. Policy workgroup
    h. Malware workgroup
- Open ideas time
- Confirm next meeting date/time

# Discussion History
## carrington1859 | 2021-09-19T00:34:45+00:00
18:00:25 -carrington[m]> The scheduled community meeting begins now!
18:00:25 -carrington[m]> https://github.com/monero-project/meta/issues/609
18:00:25 -carrington[m]> In general, this is an opportunity for individuals or workgroups to update each other on work across the Monero ecosystem, and spark further discussion on specific issues. CCS proposals are also discussed in these meetings to gauge community consensus on moving these to the crowd funding stage.
18:01:00 -crypto_grampy[m]> Hi
18:01:06 -carrington[m]> 1. Greetings & introductions
18:01:14 -sosse[m]1> Hello
18:02:35 -Rucknium[m]> Hi. N.B. I will submit a CCS to the ideas stage within a week.
18:03:12 -escapethe3ra[m]1> Hello everyone, I'm the maintainer of Monero Observer.
18:03:35 -xmrscott[m]> Hi
18:04:09 -carrington[m]> 2. Community highlights
18:04:09 -carrington[m]> Are there any pieces of Monero-news from the previous 2 weeks which people would like to discuss?
18:07:34 -carrington[m]> To be fair, there doesn't seem to be much exciting news in the previous 2 weeks other than the ciphertrace news which has been discussed at length
18:08:49 -escapethe3ra[m]1> Actually I think I have one. Considering a) the recently disclosed Matrix clients vulnerability and b) the fact that this is not the most private and well-established protocol out there, I would like to propose we discuss a potential addition of a Monero XMPP server. Sincerely, it's a pain to use this with Whonix/Tails. 
18:09:04 -carrington[m]> 3. CCS updates
18:09:04 -carrington[m]> There is presently only 1 CCS idea for discussion which is a proposal to maintain and publish the Monero Observer news website 
18:09:04 -carrington[m]> https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/248
18:11:24 -carrington[m]> I see your point, but I'm  not sure "private" communication channels should be community-maintained infrastructures
18:12:45 -carrington[m]> The monero matrix server mainly exists for the public channels. Individuals can arrange whatever secure comms they like on their own. Just my opinion of course
18:14:07 -escapethe3ra[m]1> Alright, so you believe there should be no Monero privacy communication channels for the public, did I read that right?
18:14:28 -msvb-lab> Are we having a meeting now, like is indicated in the agenda? https://github.com/monero-project/meta/issues/609/
18:14:57 -escapethe3ra[m]1> carrington[m]: And what does "community" mean in this context?
18:17:18 -crypto_grampy[m]> I think there are 2 arguments here.  1 is about public vs private spaces for discussions and 2. Is matrix a safe protocol for discussions period 
18:17:31 -xmrscott[m]> I would also argue it's reasonably well established. Both the French and German governments see fit to use it
18:18:45 -xmrscott[m]> Lest people forget there have been vulns like ShellShock in the last 5 years on much more well established software
18:18:59 -Rucknium[m]> The recent vulnerability was only in certain clients and it would only be a problem if the server were t be malicious; hopefully the Monero server isn't malicious ;)
18:19:23 -Rucknium[m]> I think the bigger issue with Matrix is that the IRC-Matrix bridges keep breaking.
18:19:26 -escapethe3ra[m]1> All valid points. But there is no argument when it comes to XMPP being "not so well established". 5 years is nothing compared to 22 years of XMPP.
18:20:12 -carrington[m]> -escapethe3ra[m]1> "Alright, so you believe there..." -- No, I just think that the main motivation for the matrix server is facilitating public discussions about Monero rather than "one on one" conversations which can be arranged however people like
18:20:14 -carrington[m]> -escapethe3ra[m]1> "And what does "community" mean..." -- Well the matrix server is maintained by the Monero Core team under the Monero Space banner/brand. 
18:20:14 -xmrscott[m]> Sure. If you want to establish an 'official' bridge though ultimately you'd need to convince Core+pigeons
18:20:15 -carrington[m]> Gah ironically my matrix client is glitching. Did those two replies come through?
18:20:30 -xmrscott[m]> s/bridge/XMPP bridge
18:20:47 -xmrscott[m]> carrington[m]: Yes
18:20:52 -escapethe3ra[m]1> carrington[m]: Got it, thanks for clarifying. That's what I thought initially.
18:23:07 -carrington[m]> Anyways, unless people have further strong opinions on this we can move on to discussing escapethe3ra @escapethe3ra:matrix.org 's CCS proposal
18:25:56 -carrington[m]> My personal opinion is that the proposal is reasonable and the quality of the the author work will be judged by people over the 3 months to determine if a potential second proposal is worthwhile
18:26:37 -xmrscott[m]> Same. Furthermore, I'm sure there are people who'd be happy to review for typos, etc before an official release
18:27:14 -carrington[m]> My only negative point is that other "Monero news" projects have been started and abandoned in the past (see e.g. Revuo & Monero Moon)
18:27:41 -carrington[m]> But of course if this happens then people will just not donate to a second proposal so the problem fixes itself sorta
18:27:42 -plowsof[m]> fwiw the monero moon(?) creator recently posted on reddit to state that he has not abandoned the project and has been busy 
18:28:12 -plowsof[m]> he intends to meet the proposal milestones still
18:28:58 -Rucknium[m]> RE: Monero Moon: Well, if you are running a news service, continuity is pretty important.
18:29:42 -carrington[m]> I have not used the site (https://www.monero.observer/) enough to give feedback on style/content but I hope the author will take on board whatever feedback comes from the community
18:30:26 -escapethe3ra[m]1> Yes, community feedback is an essential part of my workflow and I don't have any plans to change that.
18:31:21 -Rucknium[m]> I have a bit of feedback on Observer: I thought the most recent MRL meeting was mischaracterized somewhat. I don't think the meeting participants were "torn" about Seraphis/Triptych. Of course, you have editorial control after all, so it's all up to you. 
18:32:45 -carrington[m]> If a little hyperbole brings more eyes on MRL stuff that is good in my book 😆
18:33:17 -Rucknium[m]> Does MRL need more drama? 🐄
18:33:30 -escapethe3ra[m]1> I guess that's the main difference between MO and other "similar" projects like Monero Moon. It's hard trying to find your voice while sticking with facts and the journalistic approach, which I want to implement on the site.
18:33:37 -carrington[m]> Anyways if no one has strong points against the proposal I will add a comment about this meeting to the gitlab issue
18:34:14 -Rucknium[m]> I think the proposal is good :D
18:34:19 -plowsof[m]> escapethe3ra[m]1: are you monero moon or monero oberver? someone with your username on reddit said they're from monero moon 
18:34:26 -carrington[m]> Although I cannot do that until I have access to my gitlab account tomorrow. Luigi may already have moved it to funding stage by then 🤷‍♂️
18:34:48 -carrington[m]> Someone else feel free to add a comment sooner 
18:34:54 -escapethe3ra[m]1> Drama was certainly not my intention, sorry if anyone interpreted that article in such a way.
18:35:06 -escapethe3ra[m]1> plowsof[m]: Monero Observer.
18:35:59 -escapethe3ra[m]1> carrington[m]: Thanks for the trust.
18:36:31 -carrington[m]> 4. Workgroup reports
18:36:31 -carrington[m]> I will leave the floor open for workgroup members to take the mic and we can triage if there are multiple
18:37:06 -escapethe3ra[m]1> Rucknium and anyone else that's a reader of MO, please don't feel like you can't get in touch with me anytime you see something that can be better on the site, I always reply to all emails.
18:37:28 -carrington[m]> (Because, mea culpa, I did not spread this meeting to all relevant workgroups as I should have)
18:37:44 -Rucknium[m]> Note: I have a question for feedback about my forthcoming CCS
18:37:50 -carrington[m]> -msvb-lab> "Are we having a meeting now..." -- Yes
18:39:05 -carrington[m]> Rucknium[m]: Go ahead, there seems to be no one desperate to discuss their work today
18:41:02 -Rucknium[m]> Ok great. I have a little conundrum: Some details of my plan for execution of my CCS are "sensitive" -- I have a Vulnerability Response Process submission under review. So I'm thinking that it would be "best" if I were able to be pretty vague about what my research roadmap would entail, but I don't know how the community would respond to that.
18:41:47 -Rucknium[m]> I may be overthinking it because I could just discuss goals and not many people would be interested in the mechanics about how to reach goals or would be able to understand them anyway.
18:42:34 -Rucknium[m]> Basically, I don't know how people would respond to me saying, "Just trust me on this one". Of course, key community members have reviewed my plan, so they can vouch for it.
18:42:58 -utxobr[m]> Rucknium: imho, totally fine to be vague to not reveal anything too sensitive - if i'm donating, it's because I trust 
18:43:40 -carrington[m]> If key community members "in the loop" add comments vouching for the importance of the work that should be good enough IMO
18:44:48 -carrington[m]> As long as goals, qualifications/skills & milestones are clear that is all that really matters
18:45:23 -Rucknium[m]> I also think that people would be more willing to "just trust" if they truly knew the status quo. For example, did you know that the current mixin selection algorithm was developed by non-statisticians who were in part funded by the U.S. government, one of whom sits on the board of Zcash?
18:46:35 -Rucknium[m]> I think I have my answer BTW. We can close this topic.
18:47:02 -carrington[m]> Well funding and being boards is less important to me than lack of technical expertise
18:47:18 -carrington[m]> Anyways since no workgroups are jumping up let's move on
18:47:23 -carrington[m]> 5. open ideas time
18:47:58 -carrington[m]> No rules here folks, go nuts
18:50:18 -msvb-lab> There is a subtopic Defcon workgroup, which is not relevant so early (for DC30) but if other event discussion exists, should we review?
18:50:40 -msvb-lab> For example progress on Monerokon or the Puerto Rico event?
18:50:57 -sosse[m]1> So I have read a post in reddit. (https://www.reddit.com/r/Monero/comments/pqm1tq/monero_is_not_a_currency_at_all_its_a_censorship/?utm_medium=android_app&utm_source=share) how you could send messages via TX multiply them by 10^12 and read them as ASCII characters. I found that idea cool, my question is would it be possible to develop a client in wich someone can chat with another person via this? Where the chat is secured by the xmr
18:50:57 -sosse[m]1> blockchain? A wallet for each account there deposit like 0.01 xmr and you can chat and the messages arrive to the other persons account wallet for that client? Or are the fees to high for this
18:51:10 -msvb-lab> There was a third event as well, maybe we were counting 33C3?
18:51:28 -msvb-lab> I mean 37C3.
18:51:47 -carrington[m]> msvb-lab: I think this late in the meeting we should keep this to monero-events, but perhaps an effort for regular meetings there would be a good idea
18:52:08 -msvb-lab> Okay, then we cancel the Defcon workgroup topic.
18:52:12 -netrik182> I would like to suggest monero talks' CCS proposal to consider spreading the word about the current recruiting effort the community is organizing 
18:52:44 -netrik182> Since Doug will be doing outreach through their YT channel 
18:52:58 -netrik182> That might be a good addition 
18:53:06 -carrington[m]> msvb-lab: We can just move the discussion to that channel for general chat as the meeting ends in less than 10 mins
18:53:34 -Rucknium[m]> sosse:  I think in general Monero developers are cold on this idea due to the possibility of blockchain bloat. Monero suffers particularly from blockchain bloat compared to other coins since even "light wallets" must scan the entire blockchain due to privacy.
18:53:57 -sosse[m]1> What is bloat?
18:54:26 -Rucknium[m]> netrik182: I think this is OK to share publicly: I am already in contact with Sunita about this. She reached out to me.
18:56:21 -Rucknium[m]> sosse: Too many "unnecessary" transactions on the blockchain.
18:57:33 -carrington[m]> -netrik182> "I would like to suggest monero..." -- Good idea! You should reach out to Doug on this I think, maybe get him to reach out to Rucknium  or get him to read the pinned reddit post
18:57:52 -carrington[m]> Regarding the messaging idea I agree it is possible in the low fee environment but I don't think it would be sustainable or wise from a bloat perspective
18:58:07 -carrington[m]> Anyways, I have to run pretty soon
18:58:17 -carrington[m]> The final agenda item is agreeing next meeting
18:58:24 -Rucknium[m]> I have a controversial idea:
18:58:29 -Rucknium[m]> Oh ok. We can close
18:58:38 -carrington[m]> I suggest same day/time in 2 weeks
18:59:50 -carrington[m]> I will make an effort to post logs, agenda and spread the word once I have access to my accounts tomorrow if no one else has done those tasks
19:00:12 -Rucknium[m]> Maybe I will throw it out there and people can think about it. Well, actually it is not my idea, or is not new anyway. But I think it could be a good idea to have a "manager" or "director" role for MRL. It is discussed here in the comments:
19:00:12 -Rucknium[m]> https://www.reddit.com/r/Monero/comments/n2njsk/how_to_increase_the_number_of_cryptographers_and/
19:00:42 -xmrscott[m]> Sure, 2 weeks sounds good
19:01:37 -escapethe3ra[m]1> carrington[m]: Sounds good. Saturday 2 Oct @ 1800 UTC.
19:01:54 -escapethe3ra[m]1> Will post on MO.
19:02:33 -carrington[m]> Thanks all for coming. Conversations can of course continue on anything discussed in the meeting slot

# Action History
- Created by: Keiji-C | 2021-09-12T17:05:58+00:00
- Closed at: 2021-09-19T22:32:32+00:00
