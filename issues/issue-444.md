---
title: 'Research meeting: 4 March 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/444
author: SarangNoether
assignees: []
labels: []
created_at: '2020-02-29T18:08:38+00:00'
updated_at: '2020-03-04T18:45:27+00:00'
type: issue
status: closed
closed_at: '2020-03-04T18:45:27+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 4 March 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-03-04T18:45:27+00:00
    [2020-03-04 13:00:15] <sarang> Let's start the meeting!
    [2020-03-04 13:00:20] <sarang> First, GREETINGS
    [2020-03-04 13:00:21] <sarang> hello
    [2020-03-04 13:00:28] <sgp_> hi
    [2020-03-04 13:00:46] — sarang will wait a couple of minutes
    [2020-03-04 13:02:08] <sgp_> [meta] I added the MRL meetings with reminders to the Google Calendar I have if you are ok using Google: https://calendar.google.com/calendar/embed?src=itmaraubkfoe4aq2oquoaogsuk%40group.calendar.google.com&ctz=UTC
    [2020-03-04 13:02:47] <sarang> Does using that link leak any information to you? (presumably it leaks IP information to Google)
    [2020-03-04 13:02:59] <sgp_> not to me, just Google
    [2020-03-04 13:03:23] <sarang> roger
    [2020-03-04 13:03:26] <sarang> OK, continuing on
    [2020-03-04 13:03:31] <sarang> Next up is the ROUNDTABLE
    [2020-03-04 13:03:48] <UkoeHB_> hi
    [2020-03-04 13:03:50] <sarang> I've been getting the multi-input version of Triptych updated for posting to the IACR preprint archive
    [2020-03-04 13:04:01] <sarang> as well as minor edits to the original preprint as I come across them
    [2020-03-04 13:04:34] <sarang> Posting to IACR (with suitable caveats about non-standard cryptographic hardness assumptions) can increase the visibility of the idea, and hopefully encourage feedback
    [2020-03-04 13:05:07] <sarang> It's pretty slow going, but progressing well
    [2020-03-04 13:05:14] <sarang> Any particular questions on that before I pass the baton?
    [2020-03-04 13:08:05] <sarang> OK, next up!
    [2020-03-04 13:08:16] <sarang> Does anyone else have research of interest to share and discuss?
    [2020-03-04 13:09:39] — sarang will wait a bit; there's plenty of time
    [2020-03-04 13:10:04] <Isthmus> Yo
    [2020-03-04 13:10:21] <sarang> Hello Isthmus
    [2020-03-04 13:10:29] <sarang> Did you wish to share anything, or just observing?
    [2020-03-04 13:10:33] <Isthmus> I’ve been pretty busy in meatspace, sadly no time for data spelunking
    [2020-03-04 13:10:41] <sarang> OK, no problem! Simply checking
    [2020-03-04 13:10:48] <sarang> It's a fairly quiet day today anyway
    [2020-03-04 13:11:18] <sarang> UkoeHB_?
    [2020-03-04 13:11:20] <sarang> suraeNoether?
    [2020-03-04 13:11:22] <sarang> Others?
    [2020-03-04 13:11:22] <Isthmus> Oh yes, actually
    [2020-03-04 13:11:25] <sarang> ah ok
    [2020-03-04 13:11:28] <sarang> carry on Isthmus
    [2020-03-04 13:11:51] <Isthmus> Wait there’s too much traffic for voiced text, let me look back pewter in four minutes
    [2020-03-04 13:12:00] <sarang> roger
    [2020-03-04 13:12:05] <sarang> Someone else, then?
    [2020-03-04 13:12:10] <UkoeHB_> need about 10mins
    [2020-03-04 13:13:04] <sarang> OK, in that case, let's pause the meeting for 10 minutes or so; I show the time is 18:12, so let's reconvene at 18:22 or so
    [2020-03-04 13:13:11] — sarang pauses the meeting
    [2020-03-04 13:17:21] <sgp_> sarang: want to talk about Triptych naming at some point?
    [2020-03-04 13:17:37] <sarang> That seems like a suitably off-topic idea during this break =p
    [2020-03-04 13:17:52] <sarang> Right now, the multi-input Triptych preprint uses the name "Triptych-2"
    [2020-03-04 13:17:59] <sarang> this is boring and not descriptive
    [2020-03-04 13:18:04] <sarang> I am open to better naming ideas
    [2020-03-04 13:18:20] <sarang> Note that I can revise the older paper if that's helpful (this has been done to add features and fix errors)
    [2020-03-04 13:19:14] <hyc> what part of the original "triptych" is triple?
    [2020-03-04 13:19:17] <sarang> The benefits of Triptych-2 are using a single proof for all spends (instead of separate proofs with commitment offsets), and handling balance assertions directly within the proof
    [2020-03-04 13:19:19] <sgp_> I originally recommended Triptyzk as a half joke, but part of me thinks it's a good idea
    [2020-03-04 13:19:33] <hyc> Polyptych
    [2020-03-04 13:19:34] <sarang> The idea was that the three parts to Triptych are signing keys, commitment keys, and linking tags
    [2020-03-04 13:19:47] <sarang> Heh, a polyptic sounds like something a surgeon would remove :/
    [2020-03-04 13:19:54] <UkoeHB_> lmao
    [2020-03-04 13:20:19] <sarang> FWIW there's basically no change to the SHVZK property or proof between the two versions
    [2020-03-04 13:20:29] <sarang> They're almost identical
    [2020-03-04 13:20:58] <sgp_> that's partially why adding "zk" now makes no sense. It's more about proactively naming for the Twitter trolls/idiots
    [2020-03-04 13:21:47] <UkoeHB_> B-Triptych and E-Triptych for basic and extended 🤔
    [2020-03-04 13:21:57] <sarang> Triptych Classic and New Triptych
    [2020-03-04 13:22:26] <hyc> Triptych and Antikythera :P
    [2020-03-04 13:23:05] <sarang> Just what we need; something equally hard to pronounce =p
    [2020-03-04 13:23:19] — sarang resumes the meeting
    [2020-03-04 13:23:19] <moneromooo> Technology so old nobody remembers how it works.
    [2020-03-04 13:23:27] <hyc> yes... and indecipherable, and considered too advanced for its time
    [2020-03-04 13:23:38] <kinghat> i havent been paying that close attention but have we "shelved" CLSAG?
    [2020-03-04 13:23:57] <sarang> suraeNoether just told me he's now happy with the revised security model for CLSAG
    [2020-03-04 13:24:29] <sarang> Nothing has changed with the algorithms themselves, apart from a small change to hash function inputs
    [2020-03-04 13:25:08] <UkoeHB_> it sounded like suraeNoether was considering advocating to skip CLSAG and go directly to next-gen in a year or two
    [2020-03-04 13:25:16] <sarang> I disagree
    [2020-03-04 13:25:40] <sarang> CLSAG is a straightforward change that's well understood
    [2020-03-04 13:26:25] — moneromooo moves mouse over merge button
    [2020-03-04 13:26:32] <kinghat> 😂
    [2020-03-04 13:26:53] <sarang> Anyway, he made very recent updates that I'll review (more on this during ACTION ITEMS) for IACR posting
    [2020-03-04 13:26:55] <sarang> Anyway
    [2020-03-04 13:27:04] <sarang> UkoeHB_ and Isthmus both wanted to share some work
    [2020-03-04 13:27:18] <selsta> Will CSLAG require a paid review?
    [2020-03-04 13:27:29] <sarang> Nothing "requires" paid review
    [2020-03-04 13:27:36] <selsta> for you to be comfortable with it
    [2020-03-04 13:27:37] <sarang> But it's probably a good idea :)
    [2020-03-04 13:27:51] <sarang> I'm very comfortable with the math
    [2020-03-04 13:28:09] <Isthmus> Hm, upon more consideration, discussing it today might be the wrong order of operations
    [2020-03-04 13:28:17] <Isthmus> Nothing pressing or dangerous
    [2020-03-04 13:28:17] <sarang> The total estimate for math+code review by Teserakt was ~$15000 USD, which is quite reasonable IMO
    [2020-03-04 13:28:28] <sarang> Isthmus: how so?
    [2020-03-04 13:28:36] <sarang> Now you have everyone intrigued
    [2020-03-04 13:29:08] <UkoeHB_> happy to announce a final proofreading draft of ZtM2 is ready. Note that I decided not to go into Bulletproofs since it's frankly way too much detailed math to be worth it. Anyone who wants to learn bulletproofs should just read the original paper. https://www.pdf-archive.com/2020/03/04/zerotomoneromaster-v1-1-0/zerotomoneromaster-v1-1-0.pdf
    [2020-03-04 13:29:10] <Isthmus> A poorly-framed thought experiment is worse than no thought experiment at all 😅
    [2020-03-04 13:29:21] <sarang> UkoeHB_: great!
    [2020-03-04 13:29:36] <sarang> Will this be renamed to 2.0 after review?
    [2020-03-04 13:29:59] <sarang> Or will the title be incremented to "One to Monero" :D:D:D
    [2020-03-04 13:30:17] <UkoeHB_> Ill make a reddit post asking for proofreaders, and if anyone knows someone who wants to proofread go ahead and pass it around. Not much is likely to change between now and publication in ~1.5-2months. The proofreading period is 3 weeks.
    [2020-03-04 13:30:34] <UkoeHB_> I think Ill just remove the version number
    [2020-03-04 13:30:36] <UkoeHB_> maybe
    [2020-03-04 13:31:14] <midipoet> UkoeHB_: fair play
    [2020-03-04 13:31:15] <sarang> Name them based on the most recent Monero version name?
    [2020-03-04 13:32:21] <sarang> Anyway, great to hear the update is nearing completion
    [2020-03-04 13:32:28] <hyc> Zero to Monero, Hero Edition
    [2020-03-04 13:32:50] <UkoeHB_> yes I want to meet the hero who reads the whole thing :)
    [2020-03-04 13:32:53] <hyc> the more -ero suffixes in the title, the better :P
    [2020-03-04 13:33:24] <sarang> Does anyone else wish to share research of interest?
    [2020-03-04 13:35:59] <sarang> OK, we can move on to ACTION ITEMS, then
    [2020-03-04 13:36:21] <sarang> I am completing the Triptych-2/NewTriptych/E-Triptych/etc. preprint for IACR posting
    [2020-03-04 13:36:41] <sarang> and reviewing the (hopefully final) changes to CLSAG that I received from suraeNoether
    [2020-03-04 13:36:53] <sarang> Anyone else?
    [2020-03-04 13:37:58] <UkoeHB_> proofreading, and listening to proofreader feedback if and when it appears; starting now will probably spend a lot less time with Monero as this project wraps up
    [2020-03-04 13:38:29] <sarang> I think a reddit post is a great idea to encourage readers to take a look
    [2020-03-04 13:39:02] <sarang> ZtM is such a valuable resource
    [2020-03-04 13:40:50] <sarang> Short meeting today! But that's fine
    [2020-03-04 13:40:59] <sarang> Any other questions, comments, etc. as we wrap up?
    [2020-03-04 13:42:51] <sarang> All right! Let's adjourn
    [2020-03-04 13:42:55] <sarang> Thanks to everyone for attending
    [2020-03-04 13:43:01] <sarang> Logs will be posted shortly to the GitHub issue


# Action History
- Created by: SarangNoether | 2020-02-29T18:08:38+00:00
- Closed at: 2020-03-04T18:45:27+00:00
