---
title: 'Research meeting: 12 August 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/498
author: SarangNoether
assignees: []
labels: []
created_at: '2020-08-11T15:20:03+00:00'
updated_at: '2020-08-12T18:26:35+00:00'
type: issue
status: closed
closed_at: '2020-08-12T18:26:34+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 12 August 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## umma08 | 2020-08-11T19:25:08+00:00
I (midipoet) would like to add an agenda item to the -lab meeting for open discussion:

**tl;dr we need sarang to be a member of ISO TC307. it costs $2200. if possible, and the community agrees, we should try and get it absorbed by the CCS.** 

**2. Discussion of Sarang becoming a member of:**
[International Standards Organisation Technical Committee 307 - Blockchain and distributed ledgers](https://www.iso.org/committee/6266604.html)

Just to give a bit of background to this. I have become involved in ISO TC307 for the last few months. One of the documents the ISO have been working on is:

**[ISO/TR 23244 Privacy and Personally Identifiable Information protection considerations](https://www.iso.org/standard/75061.html).** 

The final text went for ballot to the respective delegations (national bodies). I fed this into #monero-research-lab, as there is mention and description of a few elements relevant to Monero (ring sigs, stealth addresses, pederson commitments, etc). 

Sarang felt that some amendments were required to the text. I fed these comments back into WG2 - Security, Privacy and Identity. The workgroup agreed that the document should be amended, so they opened up the text for comments from members of the work group. 

I propose to ensure Sarang can engage on behalf of the Monero community (instead of going through me). I feel this would be more effiecient and correct (as i am nowhere near as technical). This would allow me to work on aspects that i feel suited to (Governance, Identity, PII/PIA/DPIA), while Sarang can represent Monero (and open source cryptocurrency/networks in general) on some of the more technical documents/elements - of which the WGs will be moving into shortly, like Zero Knowledge Proofs, Multi-party Computation, etc. 

**Long story short:**
Membership by the ITIC (US National Standards Body) is ~$2200 per year, and the national mirror commitee for ISO TC307. There are reduced rates, but its not clear whether we are able to access them. Either way, i woud like a discussion opened on whether the fee for this membership should be absorbed by a CCS. There are about 2-4 meetings a month (two hours). they are not mandatory. There are also in person events (covid restricted now) once or twice a year, where much work is done on standards. 

Personally, i feel that having representation from privacy centric and/or open source communities is extremely important, as these documents do actually end up having influence at both policy level (legislation) and at the level of wider adoption (e.g. CBDCs and corporate/premissioned chains). This may end up impacting on us in one way or another. 

Please note, that the request for comments/input into TR 23244 **is now**, and runs for a remaining two weeks approx (we have lost a week or so getting this sorted for one reason or another). 

Also please note, that **NOT ALL** countries charge for membership. My country does not, for example. I assume it's an ideology thing. Not my issue, blame capatalism or something or other. 




## Mitchellpkt | 2020-08-12T03:06:55+00:00
I might not have internet during the meeting tomorrow. 

I'm cool with sponsoring some or all of the ITIC membership. It's pretty standard for tech employers to set aside funds for personal professional/career development as part of a competitive benefits package. A privacy/Monero-savvy voice in ITIC is also likely to be beneficial for the wider community as well, so it seems like a win-win to me.

Posted the Milestone 1 update on the pq-Monero CCS merge request. (We had the first draft a few weeks ago, but we made a few updates as research progressed)

## SarangNoether | 2020-08-12T18:26:34+00:00
    [2020-08-12 12:59:18] <sarang> OK, let's get started with our meeting!
    [2020-08-12 12:59:25] <sarang> Agenda: https://github.com/monero-project/meta/issues/498
    [2020-08-12 12:59:28] <sarang> First, GREETINGS
    [2020-08-12 12:59:29] <sarang> hello
    [2020-08-12 12:59:36] <ArticMine> Hi
    [2020-08-12 12:59:37] <moneromooo> GREETINGS
    [2020-08-12 13:00:21] <sarang> Are midipoet and/or Isthmus here?
    [2020-08-12 13:00:30] <midipoet> yep
    [2020-08-12 13:00:38] <midipoet> thanks for the ping. was making tea
    [2020-08-12 13:00:43] <sarang> great
    [2020-08-12 13:00:50] <sarang> Let's move right to ROUNDTABLE then
    [2020-08-12 13:00:56] <sarang> midipoet: you had posted in the agenda something to discuss
    [2020-08-12 13:01:33] <midipoet> i did
    [2020-08-12 13:01:59] <midipoet> https://github.com/monero-project/meta/issues/498#issuecomment-672216054
    [2020-08-12 13:02:14] <midipoet> i am not sure if people had managed to read/digest
    [2020-08-12 13:02:44] <midipoet> am happy to provide context/answer questions about this
    [2020-08-12 13:02:51] <sarang> The gist is that you (midipoet) have been working with an ISO technical group regarding privacy and PII in blockchain applications
    [2020-08-12 13:03:05] <midipoet> yes, that and some other WGs
    [2020-08-12 13:03:08] <sarang> and that I (sarang) have been providing some feedback on the working draft of a document for this
    [2020-08-12 13:03:36] <sarang> Fortunately these comments have halted the process for the document and allowed for a return to a comment period
    [2020-08-12 13:03:45] <sarang> However, you had suggested that I join the process formally
    [2020-08-12 13:04:00] <sarang> Unfortunately, my country's representation requires a steep annual fee to join (grrrrr)
    [2020-08-12 13:04:31] <sarang> I had questioned whether or not this should be considered a good value for the community and ecosystem
    [2020-08-12 13:04:37] <sgp_> Hello
    [2020-08-12 13:04:39] <sarang> hi
    [2020-08-12 13:05:19] <midipoet> "halted is not technically correct. As far as i know the document stands, with request for amendments/corrections/addendums. there is a 4 week process for this (of which 2 have passed)
    [2020-08-12 13:05:24] → hashes4merkle joined (~hashes4me@x590cb5ac.dyn.telefonica.de)
    [2020-08-12 13:05:25] <sarang> The comment period for this document is only a couple of additional weeks, but I've provided midipoet with a detailed list of recommended changes
    [2020-08-12 13:05:33] <sarang> ok thanks midipoet
    [2020-08-12 13:06:10] <sarang> Isthmus mentioned in a subsequent comment to the agenda issue that his organization may be interested in sponsoring this fee
    [2020-08-12 13:06:13] <sgp_> The membership agreement includes a possible fee waiver so I will help Sarang try that first
    [2020-08-12 13:06:21] <sarang> but I have not spoken with Isthmus directly about this option
    [2020-08-12 13:06:50] <sarang> Anyway, I am willing and interested to join the group and continue to provide technical feedback, but I do not like the steep pay-to-play nature of the U.S.'s involvement
    [2020-08-12 13:07:00] <midipoet> sgp_: great idea. for the record, the convener John Greaves is well versed in open source, and as far as i know works for Consensys Health (for better or worse)
    [2020-08-12 13:07:01] <ArticMine> So if I understand correctly is the  fee the only barrier?
    [2020-08-12 13:07:12] <sarang> Yes
    [2020-08-12 13:07:17] <sarang> and the fairly short timeline, I suppose
    [2020-08-12 13:07:46] <sarang> But again, I already have prepared a detailed list of recommended changes to correct many technical errors
    [2020-08-12 13:07:52] <midipoet> also, bear in mind it seems to be a yearly fee. however, there is potential to get a reduced rate down to ~$1370 or even ~$400
    [2020-08-12 13:07:58] <sgp_> The fee will not be a problem and you should join, though I will still try to get it waived
    [2020-08-12 13:08:38] <sarang> Note that I'm sure my affiliation would not be listed as "Monero" or anything like that, since I don't "work for" Monero
    [2020-08-12 13:09:16] <midipoet> i think you just go under the national delegation (ie US - ITIC)
    [2020-08-12 13:09:29] <midipoet> that's how it is done for the most, afaict
    [2020-08-12 13:09:46] <sarang> I mean only that the decision of whether or not to support this idea should not be made on the assumption that the name "Monero" gets to appear in standards-related materials
    [2020-08-12 13:09:52] <sarang> because it almost certainly will not
    [2020-08-12 13:10:03] <midipoet> i don't even think the authors get names
    [2020-08-12 13:10:05] <midipoet> *named
    [2020-08-12 13:10:06] <sarang> and I don't intend to favor Monero or any project in my partipation
    [2020-08-12 13:10:10] <sarang> *participation
    [2020-08-12 13:10:22] <midipoet> it's really about ensuring the actual docs are as correct as we would like
    [2020-08-12 13:10:25] <sgp_> Then what are we paying you for /s
    [2020-08-12 13:10:26] <sarang> right
    [2020-08-12 13:10:30] <sarang> sigh
    [2020-08-12 13:10:44] <midipoet> and also about ensuring the perspectives of open source/decentralised/permissionless networks are catered for
    [2020-08-12 13:10:52] <sarang> My goal is to ensure technical correctness, a goal which I don't think was met by the initial draft that I saw
    [2020-08-12 13:10:54] <ArticMine> ^ this is key
    [2020-08-12 13:11:01] <midipoet> as for the most part, in these groups, they are not (though they are respected)
    [2020-08-12 13:11:41] <sarang> So how do folks think we should proceed?
    [2020-08-12 13:12:15] <sgp_> Definitely join, though ask first to waive fee
    [2020-08-12 13:12:38] <sarang> It seems the fee structure assumes members are part of large rich companies
    [2020-08-12 13:12:47] <ArticMine> either waive or raise the fee
    [2020-08-12 13:12:58] <ArticMine> or a combination of both
    [2020-08-12 13:13:10] <midipoet> i vote join, especially given the time, as there will be some intro/admin/setup to do on the side of ITIC. sarang will also have to learn the ISO IT system - which is HORRIBLE
    [2020-08-12 13:13:17] <sarang> o_0
    [2020-08-12 13:13:47] <sarang> midipoet: do you think there will be adequate time to properly raise my concerns and suggestions before the comment timeline has elapsed?
    [2020-08-12 13:13:52] <sarang> I had _many_ suggestions
    [2020-08-12 13:14:09] <ArticMine> <sarang> It seems the fee structure assumes members are part of large rich companies <--- Which is why the technical balance sarang will bring is so important
    [2020-08-12 13:14:17] <sarang> ArticMine: I agree
    [2020-08-12 13:14:28] <midipoet> sarang: yes - but you will have to tone it down to a few key ones.
    [2020-08-12 13:14:34] <sarang> That will be tough
    [2020-08-12 13:14:41] <sarang> I thought the document was severely lacking
    [2020-08-12 13:14:53] <midipoet> otherwise the WG wont have time to find consensus
    [2020-08-12 13:14:57] <midipoet> and that is more important
    [2020-08-12 13:15:13] <sarang> If they add "cryptographic constructions and protocols are different" then I will be happy
    [2020-08-12 13:15:19] <sarang> and if they properly define Pedersen commitments...
    [2020-08-12 13:15:24] <midipoet> no, i get it
    [2020-08-12 13:15:35] <midipoet> the urgency is in there, not here
    [2020-08-12 13:16:44] <sarang> The risk with raising the fee is that I'd have to join now and pay out of pocket, and hope that such a CCS is accepted and funded, or otherwise sponsored by a group like Isthmus's company
    [2020-08-12 13:16:57] <sarang> (note that any such company would specifically _not_ have any say over how I participate)
    [2020-08-12 13:17:48] <sarang> I do not think the CCS process should be adjusted for this particular case
    [2020-08-12 13:19:08] <midipoet> would you mind rolling it into the next three CCSs? to distribute the cost over the course of the year membership?
    [2020-08-12 13:19:31] <midipoet> you would obviously have to absorb the direct cost immediately though...
    [2020-08-12 13:20:23] <sarang> I think it best to have a separate CCS, to make it very clear what the intent and purpose and cost are
    [2020-08-12 13:20:39] <sarang> The group claim that they do not prorate fees, and the membership period ends in November
    [2020-08-12 13:21:01] <sarang> It also appears like there is a separate mandatory fee of something like $300 on top of the $2200 (which is itself lowered for "small organizations")
    [2020-08-12 13:21:08] <Isthmus> Hey, driving through mountains, have internet for about 30 seconds every 5 minutes, lol.
    [2020-08-12 13:21:08] <Isthmus> Here was my comment: "I'm cool with sponsoring some or all of the ITIC membership. It's pretty standard for tech employers to set aside funds for personal professional/career development as part of a competitive benefits package. A privacy/Monero-savvy voice in ITIC is also likely to be beneficial for the wider community as well, so it seems like a win-win to me."
    [2020-08-12 13:21:08] <Isthmus> To clarify, I cannot offer Insight's benefit package to sarang. I was commenting that since sarang is employed by Monero, covering something like this would be in line with industry best practices.
    [2020-08-12 13:21:13] <sarang> So the cost is likely around $2500 maximum (all USD)
    [2020-08-12 13:21:36] <sarang> Isthmus: was I misinterpreting the nature of an Insight sponsorship?
    [2020-08-12 13:21:42] <sarang> Perhaps I misread
    [2020-08-12 13:21:53] <Isthmus> I didn't say anything about Insight
    [2020-08-12 13:21:57] <Isthmus> Sorry :- (
    [2020-08-12 13:21:59] <sarang> OK, then I definitely misread
    [2020-08-12 13:22:04] <sarang> Ignore everything I said earlier about Insight!
    [2020-08-12 13:22:16] <sarang> Also, I am not employed "by Monero" to be clear
    [2020-08-12 13:22:26] <Isthmus> yea yea you know what I mean
    [2020-08-12 13:22:41] ⇐ hashes4merkle quit (~hashes4me@x590cb5ac.dyn.telefonica.de): Remote host closed the connection
    [2020-08-12 13:22:52] <sarang> I read "I'm cool with sponsoring" as implying Insight, which was obviously not correct
    [2020-08-12 13:22:58] <sarang> Apologies for the confusion
    [2020-08-12 13:23:17] <sgp_> I think we are all cool with this and are now talking in circles lol
    [2020-08-12 13:23:26] <ArticMine> Yes
    [2020-08-12 13:23:29] <sarang> OK, I'll join out of pocket, look into a fee reduction or waiver, and propose a CCS for the remainder
    [2020-08-12 13:23:47] <sarang> and hope for the best :D
    [2020-08-12 13:24:00] <midipoet> i would be a bit wary of relying on the creation and fulfilment of a CCS before joining. that seems like it may take a week (min) in itself
    [2020-08-12 13:24:26] <midipoet> i understand why sarang does not want to pay out of pocket however
    [2020-08-12 13:24:28] <sarang> Yes, I mean join out of pocket and _then_ propose the CCS, to avoid missing the timeline for comment
    [2020-08-12 13:24:28] <Isthmus> +1 to sgp/sarang/artic
    [2020-08-12 13:24:46] <sarang> The CCS process takes time, and should not be rushed for this
    [2020-08-12 13:24:50] <midipoet> sarang: ah understood. yes, then i agree.
    [2020-08-12 13:25:04] <sarang> OK thanks midipoet for your involvement in this standards process
    [2020-08-12 13:25:12] <sarang> This is the time to get involved!
    [2020-08-12 13:25:14] <sarang> Moving on
    [2020-08-12 13:25:24] <sarang> Isthmus: you had posted some material to the agenda
    [2020-08-12 13:26:13] <sarang> Care to discuss now?
    [2020-08-12 13:27:30] <sarang> Namely, Isthmus referenced this CCS update: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/142#note_10181
    [2020-08-12 13:28:23] → hashes4merkle joined (~hashes4me@x590cb5ac.dyn.telefonica.de)
    [2020-08-12 13:28:25] <sarang> I think this is fascinating, and commented that I might recommend more clearly labeling the risk assessments to make it _exceptionally_ clear what is vulnerable _today_ versus what would be vulnerable given a hypothetical future quantum adversary
    [2020-08-12 13:28:46] <sarang> on the assumption that graphs, charts, plots, etc. will be shared out of context and could be misinterpreted, either accidentally or intentionally
    [2020-08-12 13:29:15] <sgp_> agreed with your comment sarang
    [2020-08-12 13:29:52] <sarang> e.g. the light-red category (labeled 1) could easily be misinterpreted as meaning "vulnerable today" when it's not the case
    [2020-08-12 13:30:17] <sgp_> the scale also seems weird; is 6 the highest protection or is 4?
    [2020-08-12 13:30:38] <midipoet> i know the answer to this one. 6 is higher than 4
    [2020-08-12 13:31:48] <sarang> It appears that Isthmus may be away right now, but that chart is full of interesting information
    [2020-08-12 13:31:56] <sarang> I really look forward to the full repots
    [2020-08-12 13:31:59] <sarang> s/repots/reports
    [2020-08-12 13:32:00] <monerobux> sarang meant to say: I really look forward to the full reports
    [2020-08-12 13:32:03] <sarang> goot bot
    [2020-08-12 13:33:29] <sarang> I've been working on Triptych/Arcturus optimizations, BP+, some detailed lit review relating to interesting hash-based attacks, some MRL-0010 analysis relevant to the recent swap proposal
    [2020-08-12 13:33:44] <sarang> Nothing quite as succinct as Isthmus's chart =p
    [2020-08-12 13:33:55] <sarang> Does anyone else have research of interest to share with the channel?
    [2020-08-12 13:34:11] <ArticMine> Yes
    [2020-08-12 13:34:16] <sarang> Please go ahead!
    [2020-08-12 13:34:31] <ArticMine> I have a short update on issue 70 https://github.com/monero-project/research-lab/issues/70
    [2020-08-12 13:34:33] <sarang> (Note that I will have to duck out of the meeting at 17:40 UTC for an appointment, so please continue/conclude without me if needed)
    [2020-08-12 13:35:54] → caralho joined (uid209547@gateway/web/irccloud.com/x-pquvsruvxamdbpqv)
    [2020-08-12 13:35:58] <ArticMine> I reviewed the comments and there is a likely change making the longterm median a floor for the short term median
    [2020-08-12 13:36:21] <ArticMine> I am looking at the spam risk implications of this first
    [2020-08-12 13:36:28] <ArticMine> that is all
    [2020-08-12 13:36:30] ⇐ tromp_ quit (~tromp@ip-213-127-104-154.ip.prioritytelecom.net): Remote host closed the connection
    [2020-08-12 13:36:50] <sarang> OK thanks ArticMine!
    [2020-08-12 13:36:59] <sarang> Does anyone else wish to share anything of interest?
    [2020-08-12 13:39:15] <sarang> If not, I suppose we can go ahead and adjourn early; discussion can of course continue, but logs posted to the agenda will end here
    [2020-08-12 13:39:19] <sarang> Thanks to everyone for joining!


# Action History
- Created by: SarangNoether | 2020-08-11T15:20:03+00:00
- Closed at: 2020-08-12T18:26:34+00:00
