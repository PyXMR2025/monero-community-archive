---
title: 'Research meeting: 10 June 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/355
author: SarangNoether
assignees: []
labels: []
created_at: '2019-06-06T20:31:15+00:00'
updated_at: '2019-06-10T17:38:27+00:00'
type: issue
status: closed
closed_at: '2019-06-10T17:38:27+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 10 June 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. [CLSAG](https://eprint.iacr.org/2019/654)
a. Review options
b. Deployment timeline

2. Roundtable
a. Sarang: [monthly report](https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/34#note_6373), [Q3 2019 funding proposal](https://ccs.getmonero.org/proposals/sarang-2019-q3.html)
b. Surae: [Monero Konferenco](https://monerokon.com)
c. Others?

3. General questions

4. Action items

# Discussion History
## SarangNoether | 2019-06-10T17:38:27+00:00
    [2019-06-10 13:01:51] <sarang> Shall we begin the meeting?
    [2019-06-10 13:01:54] <sarang> GREETINGS
    [2019-06-10 13:01:58] <rehrar> hi
    [2019-06-10 13:02:00] <sarang> Who's present?
    [2019-06-10 13:03:54] <kinghat> ✋
    [2019-06-10 13:04:01] <rehrar> rehrar is present
    [2019-06-10 13:04:13] <sarang> I added a special agenda item to discuss CLSAG
    [2019-06-10 13:04:18] <sarang> Here's the status of it...
    [2019-06-10 13:04:37] <sarang> the preprint is finished and is posted (with identical content) in the MRL archive and the IACR archive
    [2019-06-10 13:04:52] <sarang> This does _not_ mean it has received formal peer review, because it hasn't
    [2019-06-10 13:05:07] <suraeNoether> ^
    [2019-06-10 13:05:10] <sarang> Our friend moneromooo has made excellent progress on a full codebase integration
    [2019-06-10 13:05:16] <sarang> I'm assisting as needed
    [2019-06-10 13:05:35] <sarang> I have also reached out to potential auditors to get both the crypto and the implementation checked
    [2019-06-10 13:05:38] <suraeNoether> preprints like IACR and arxiv are not peer reviewed articles, but they are often treated that way
    [2019-06-10 13:05:41] <sarang> and am waiting to hear back with details
    [2019-06-10 13:06:20] <rehrar> anyone who doesn't understand the concept of peer-reviewed doesn't understand science
    [2019-06-10 13:06:22] <sarang> In theory, if audits happened speedy quick and the code is ready, it _could_ be an October thing, but I consider that unlikely
    [2019-06-10 13:06:37] — midipoet listens
    [2019-06-10 13:06:54] <sarang> In the meantime, we'll forge ahead and see where the timeline takes us
    [2019-06-10 13:07:16] <sarang> But barring any big revelations in the process, it's looking good for being integrated into the protocol and code
    [2019-06-10 13:07:19] <rehrar> sarang: I don't think people like smooth would go for that anyways. There were people that when bps came out, wanted it to exist in the wild a little longer before implementation
    [2019-06-10 13:07:33] <rehrar> CLSAG is similar. It's existence is young.
    [2019-06-10 13:07:59] <sarang> Having the preprint out longer doesn't really do much unless it receives implementation
    [2019-06-10 13:08:10] — needmoney90 waves
    [2019-06-10 13:08:14] <sarang> Random thorough review by a qualified person is unlikely, IMO
    [2019-06-10 13:08:16] <rehrar> and thus we circle back to the same conversation as bps :D
    [2019-06-10 13:08:23] <suraeNoether> step one: convince wownero to install it wholesale
    [2019-06-10 13:08:32] <needmoney90> I was about to say that
    [2019-06-10 13:08:42] <wowario> we can do it, np
    [2019-06-10 13:08:49] <sarang> Fortunately, the math behind CLSAG is _much_ simpler than that of BPs
    [2019-06-10 13:08:51] <sarang> by a long shot
    [2019-06-10 13:08:56] <suraeNoether> won't mitigate the need for an audit
    [2019-06-10 13:08:57] <rehrar> coo'
    [2019-06-10 13:09:12] <suraeNoether> yeah, i think unlike bulletproofs, this is still an LSAG-based signature, which have been around for awhile
    [2019-06-10 13:09:14] <rehrar> sarang: is there any way to follow up on the audit requests then? Who knows. Maybe we can speed this along indeed.
    [2019-06-10 13:09:24] <sarang> The informal review that I have received (won't name names, to avoid the appearance of endorsement) has all been positive
    [2019-06-10 13:09:36] <sarang> rehrar: I made the requests over the weekend
    [2019-06-10 13:09:39] <sarang> I'll give a few days :D
    [2019-06-10 13:10:15] <rehrar> Minko.to should fund the audits since they're single handedly responsible for larger blocks :P
    [2019-06-10 13:10:33] <sarang> heh
    [2019-06-10 13:10:47] <sarang> Any other questions on CLSAG?
    [2019-06-10 13:11:35] <sarang> Otherwise, I'll carry on with audit SoW requests and assisting moneromooo with implementation
    [2019-06-10 13:11:48] <sarang> Let us move to ROUNDTABLE
    [2019-06-10 13:11:51] <sarang> suraeNoether: care to go first?
    [2019-06-10 13:12:21] <suraeNoether> well, my live has turned temporarily into konferenco administrivia
    [2019-06-10 13:12:24] <suraeNoether> life*
    [2019-06-10 13:12:48] <suraeNoether> badges have been ordered, swag bags have been ordered, etc
    [2019-06-10 13:12:56] <sarang> nice
    [2019-06-10 13:13:03] <suraeNoether> i'm scrambling behind the scenes to finish up some reimbursement of speakers, etc.
    [2019-06-10 13:13:16] — needmoney90 perks up his ears
    [2019-06-10 13:13:37] <suraeNoether> everything is going smoothly and no catastrophes yet to report
    [2019-06-10 13:14:15] <suraeNoether> we are 12 days out from the event, and i'm eager to start doing non-administrative stuff after the conference
    [2019-06-10 13:14:17] → sfhi joined (~sfhi@178.255.154.106)
    [2019-06-10 13:14:21] <sarang> https://www.youtube.com/watch?v=7trn91xkJ0w
    [2019-06-10 13:14:28] <suraeNoether> 14 days from now, my schedule is wiiiiide open
    [2019-06-10 13:15:10] <sarang> Any questions for suraeNoether ?
    [2019-06-10 13:15:11] <suraeNoether> my action items for MRL specifically that are not konferenco-related are urgent, though: finish up my research reports and begin my request for funding for the next quarter
    [2019-06-10 13:15:21] <suraeNoether> these are both on my plate *as we speak*
    [2019-06-10 13:16:05] <sarang> I've begun comparative analysis of sublinear transaction protocols
    [2019-06-10 13:16:33] <sarang> In particular, did a prototype integration of Monero-to-Lelantus output migration to get better numbers on it
    [2019-06-10 13:16:56] <sarang> I have to modify my Omniring analysis a bit once I realized that the protocol doesn't natively support plaintext fees
    [2019-06-10 13:17:20] <sarang> it's a simple change to include them as a separate account, and perhaps built-in support can be made more efficient
    [2019-06-10 13:17:27] <sarang> (I've brought this up to the authors)
    [2019-06-10 13:18:02] <sarang> Otherwise, my monthly report for May has been up for a bit: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/34#note_6373
    [2019-06-10 13:18:19] <sarang> and my 2019 Q3 funding request is also open now: https://ccs.getmonero.org/proposals/sarang-2019-q3.html
    [2019-06-10 13:18:41] <sarang> (note that this request, like the 2019 Q2 request, will be paid out immediately when funded)
    [2019-06-10 13:19:11] <rehrar> how'd that work out for you this time sarang?
    [2019-06-10 13:19:14] <sarang> I am also working on my Konferenco presentation, of course, on transaction efficiency
    [2019-06-10 13:19:14] <rehrar> pleased with that?
    [2019-06-10 13:19:37] <sarang> rehrar: it has gone very well
    [2019-06-10 13:19:54] <sarang> I think that method of payout provides the most fair value to donors and recipients, provided the trust is there
    [2019-06-10 13:20:54] <sarang> One last item: there were suggestions to have MRL-type people write up summaries of some of the methods of attack and analysis presented in Breaking Monero
    [2019-06-10 13:21:03] <sarang> including an assessment of risk
    [2019-06-10 13:21:18] <sarang> This could provide good information to people who want to know such things
    [2019-06-10 13:21:37] <sarang> I'm always wary of making claims regarding risk that might not apply to a particular individual's threat model
    [2019-06-10 13:21:55] <sarang> but posting these as summaries of Breaking Monero topics makes a lot of sense
    [2019-06-10 13:21:59] <sarang> thoughts on this from the room?
    [2019-06-10 13:22:33] <suraeNoether> i think it's a good outreach project that augments breaking monero, which is, in turn, a good outreach project
    [2019-06-10 13:23:25] <dEBRUYNE> sarang: As long as you lay out the risks and what mitigations users can utilize then it should be fine
    [2019-06-10 13:23:33] <sarang> Right
    [2019-06-10 13:23:33] <dEBRUYNE> ^ for that we don't need to specify a risk level imo
    [2019-06-10 13:23:57] <suraeNoether> i feel like this would be a good project for someone interested in learning more about Monero
    [2019-06-10 13:24:00] <sarang> The complication is that the overall risk depends heavily on what different types of information/ability an adversary has
    [2019-06-10 13:24:17] <sarang> Modifying the assumptions on your adversary can change a lot
    [2019-06-10 13:24:25] <sarang> so in no way can this be completely comprehensive
    [2019-06-10 13:24:47] <suraeNoether> the drawback to that is the delicacy of the various ideas involved, but maybe we could have someone work on some blog post summaries in a back-and-forth workshop style approach, someone who is interested in getting more involved at MRL
    [2019-06-10 13:24:56] <dEBRUYNE> We can list the assumptions needed to potentially weaken privacy right?
    [2019-06-10 13:25:18] <sarang> Sure, but a full assessment of the risks of every combination of analysis/attack methods is infeasible
    [2019-06-10 13:25:23] <rehrar> Perhaps one day somebody can make three common threat models, and look at risk for each of those defined three?
    [2019-06-10 13:25:39] <rehrar> and people can decide if they fall within or without
    [2019-06-10 13:25:42] <sarang> If Entity X and Entity Y collude and the user has Z transaction types and computation is very strong...
    [2019-06-10 13:25:46] <rehrar> and we can have tables and graphs and other science-y stuf
    [2019-06-10 13:26:12] <sarang> A big issue is always that you don't know what heuristics are "bad enough" for a given use case
    [2019-06-10 13:27:10] <dEBRUYNE> sarang: Yes, I understand it is a bit of a slippery slope
    [2019-06-10 13:27:18] <sarang> But anyway, presenting the analysis methods is, at its heart, a good thing
    [2019-06-10 13:27:29] <sarang> provided it's done very carefully and as honestly as possible
    [2019-06-10 13:27:51] <sarang> The goal is neither to scare people away nor try to push aside all claims of weaknesses
    [2019-06-10 13:29:06] <sarang> Any questions on my recent work?
    [2019-06-10 13:29:15] <sarang> Or, alternatively, does anyone else have other work to present?
    [2019-06-10 13:30:51] <sarang> righto
    [2019-06-10 13:30:58] <sarang> Well, on to ACTION ITEMS perhaps
    [2019-06-10 13:31:04] <sarang> suraeNoether already provided his
    [2019-06-10 13:31:42] <suraeNoether> <3
    [2019-06-10 13:32:01] <sarang> Mine are to complete my Konferenco presentation on transaction efficiency, continue assisting with final CLSAG codebase integration, and continue with sublinear transaction protocol analysis
    [2019-06-10 13:33:07] <sarang> I just read that the Lelantus author had made some changes to make transaction proving more efficient, but didn't see any details... so I'd also like to find out more about that for my analysis
    [2019-06-10 13:33:31] <sarang> The author and I have had some great discussions so far about making the protocol more efficient
    [2019-06-10 13:33:48] <sarang> in particular about making batching speedyfast
    [2019-06-10 13:34:05] <sarang> OK, any last thoughts, questions, or comments before we formally adjourn?
    [2019-06-10 13:34:40] <rehrar> nah
    [2019-06-10 13:34:51] <sarang> going once
    [2019-06-10 13:34:54] <sarang> going twice
    [2019-06-10 13:34:59] <sarang> adjourned!
    [2019-06-10 13:35:07] <sarang> Logs will be posted shortly to the agenda issue on github
    [2019-06-10 13:35:21] <sarang> Thanks to everyone for joining in

# Action History
- Created by: SarangNoether | 2019-06-06T20:31:15+00:00
- Closed at: 2019-06-10T17:38:27+00:00
