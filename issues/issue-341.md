---
title: 'Research meeting: 6 May 2019 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/341
author: SarangNoether
assignees: []
labels: []
created_at: '2019-05-03T15:50:35+00:00'
updated_at: '2019-05-06T17:40:05+00:00'
type: issue
status: closed
closed_at: '2019-05-06T17:40:05+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Monday, 6 May 2019 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable
a. Sarang
b. Surae
c. Others?

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2019-05-06T17:40:05+00:00
    [2019-05-06 12:59:29] <sarang> OK, let's begin
    [2019-05-06 12:59:33] <sarang> ping suraeNoether et al.
    [2019-05-06 12:59:54] <sarang> First on the agenda, GREETINGS
    [2019-05-06 12:59:56] <sarang> hello
    [2019-05-06 13:00:39] <sgp_> hello
    [2019-05-06 13:00:42] — sarang hears only crickets
    [2019-05-06 13:00:49] — sarang also hears sgp_
    [2019-05-06 13:01:04] <sarang> I'll wait a couple of minutes to see if others join
    [2019-05-06 13:01:55] <suraeNoether> hey guys
    [2019-05-06 13:02:01] — dEBRUYNE just reading
    [2019-05-06 13:02:02] <suraeNoether> thank you for your patience
    [2019-05-06 13:02:13] — suraeNoether was thinking about HMAC things
    [2019-05-06 13:02:22] <sarang> Since suraeNoether went first last time, I'll go first in the ROUNDTABLE
    [2019-05-06 13:02:45] <sarang> the DLSAG signature paper has been submitted to a conference in a short form, and the IACR preprint is forthcoming
    [2019-05-06 13:02:55] <sarang> Thanks to our coauthors for their excellent work on this
    [2019-05-06 13:03:06] <sarang> The submission process is arduous and irritating
    [2019-05-06 13:03:36] <sarang> Zcoin published an intriguing Zerocoin protocol flaw recently: https://zcoin.io/cryptographic-description-of-zerocoin-attack/
    [2019-05-06 13:03:47] <sarang> Sooooo we won't be switching to Zerocoin anytime soon!
    [2019-05-06 13:04:02] <sarang> My monthly report is available on CCS: https://repo.getmonero.org/monero-project/ccs-proposals/merge_requests/34#note_5903
    [2019-05-06 13:04:16] <suraeNoether> is there an issue with DLSAG key images that will impact the publication process?
    [2019-05-06 13:04:26] <sarang> I updated the CLSAG protocol code to reflect key prefixing, which had been left out mistakenly
    [2019-05-06 13:04:40] <sarang> Doubtful
    [2019-05-06 13:04:49] <sarang> It's an interesting construction regardless
    [2019-05-06 13:05:25] <sarang> moneromooo asked about doing a CLSAG key image offset (like we do in BPs) to save time while avoiding subgroup issues
    [2019-05-06 13:05:38] <sarang> Doing so would save ~315 us per signature on my test machine
    [2019-05-06 13:06:00] <sarang> But it was also noted that there could easily be room for error depending on implementation
    [2019-05-06 13:06:24] <sarang> Note that the CLSAG test code already performs this offset on the auxiliary key image, but this isn't used for linking anyway
    [2019-05-06 13:06:39] <sarang> I had also been interested in BP generalizations to arbitrary input lengths
    [2019-05-06 13:06:50] <sarang> I have code for it: https://github.com/SarangNoether/skunkworks/tree/pybullet-np2
    [2019-05-06 13:07:13] <sarang> Unfortunately this requires the verifier to compute all inner product rounds and loses computational efficiency
    [2019-05-06 13:07:43] <sarang> It may be possible to modify the algorithm to do the single-round version, but it is not clear to me how to do so cleanly
    [2019-05-06 13:08:34] <sarang> Currently, I'm working on updating some formal definitions for suraeNoether for CLSAG, and have been doing some code and timing tests for a paper that was presented to me
    [2019-05-06 13:08:50] <sarang> Any particular questions on this work?
    [2019-05-06 13:09:24] <suraeNoether> just curious when you sleep :D
    [2019-05-06 13:10:21] <sarang> lol
    [2019-05-06 13:10:25] <sarang> Go ahead, suraeNoether !
    [2019-05-06 13:10:43] <suraeNoether> my update is shorter: unforgeability proof for CLSAG is nearly complete, but I'm holding off on continuing to write on this before I get some comments back from sarang. some of my protocols as described have a few mismatches with our current approaches, and I don't want to write proofs for the wrong protocols.
    [2019-05-06 13:11:06] <suraeNoether> i'm working on my talk for the magical crypto conference (i'm leaving tomorrow for that and I'll be back home on sunday)
    [2019-05-06 13:11:14] <sarang> Well, they'd be correct for our implementation AFAICT, but not for a neat generalization you were working on
    [2019-05-06 13:11:24] <suraeNoether> oh! well, still
    [2019-05-06 13:11:30] <suraeNoether> since the proofs will be for the general case
    [2019-05-06 13:11:40] <sarang> Right
    [2019-05-06 13:12:21] <suraeNoether> anyway, i'm also trying to solve a problem with the dlsag key images that I thought had been solved, and I'm continuing to review a semi-secret paper for a colleague
    [2019-05-06 13:12:45] <suraeNoether> (the last semi-secret paper ended up being DLSAG, which is the groundwork for monero lightning, so y'all know if we're keeping it semi-secret it's pretty neato burrito)
    [2019-05-06 13:13:33] <dEBRUYNE> Is that semi-secrit paper related to Monero?
    [2019-05-06 13:13:42] <suraeNoether> my action items for today involve a breaking monero episode, further DLSAG research, further semi-secret research, and writing my MCC talk
    [2019-05-06 13:14:02] <suraeNoether> dEBRUYNE: yes
    [2019-05-06 13:14:11] <dEBRUYNE> Cool
    [2019-05-06 13:14:15] <suraeNoether> but i can't go further yet
    [2019-05-06 13:14:28] <sgp_> when is the earliest you expect to switch back to the bipartite graph paper?
    [2019-05-06 13:14:29] <suraeNoether> in being public about the contents, I mean
    [2019-05-06 13:15:28] <suraeNoether> sgp_: thank you for reminding me about that, this is an ongoing project, sgp_, and I've been putting in work regularly on that paper to try to get my simulations working appropriately.
    [2019-05-06 13:15:43] <suraeNoether> actually putting work regularly into the simulations, because the paper is on hold until the sims are done
    [2019-05-06 13:16:25] <suraeNoether> sarang and I are trading some projects back and forth; when i hand him clsag or dlsag, i work on MRL11 until he hands me something back, and it's like the tides
    [2019-05-06 13:16:26] <suraeNoether> :P
    [2019-05-06 13:16:54] <suraeNoether> i don't have a good timeline on completing it and getting results, however
    [2019-05-06 13:17:53] <sgp_> All I'm doing is making sure is that it doesn't fall by the wayside. There are a million things to do, I just want to make sure this remains in the top 3
    [2019-05-06 13:18:02] <suraeNoether> ^ absolutely
    [2019-05-06 13:18:35] <suraeNoether> i'll make a little descriptive blurb and make a link to it here later today so that people can see the current state of the thing
    [2019-05-06 13:18:50] <sarang> perfect
    [2019-05-06 13:18:56] <sarang> Any other questions for suraeNoether ?
    [2019-05-06 13:19:14] <suraeNoether> i want to ensure that folks in the community are aware of the progress on each of these projects, and we definitely have a *lot* of projects/spinning plates
    [2019-05-06 13:19:43] <sarang> If anyone else has relevant research to present, now is a great time
    [2019-05-06 13:19:55] <sgp_> none from me. looking forward to seeing the MCC recording/slides
    [2019-05-06 13:20:10] <sarang> As am I
    [2019-05-06 13:21:00] <sarang> Ok, how about ACTION ITEMS
    [2019-05-06 13:21:27] <sarang> I'll be rewriting some definitions today to streamline suraeNoether's CLSAG generalization for the proofs
    [2019-05-06 13:21:48] <sarang> Finishing up that timing data I mentioned earlier
    [2019-05-06 13:21:59] <sarang> getting another couple of Breaking Monero out the door
    [2019-05-06 13:22:12] <sarang> Reviewing some output selection stuff
    [2019-05-06 13:22:23] <sarang> etc.
    [2019-05-06 13:22:26] <sarang> Others?
    [2019-05-06 13:22:52] <suraeNoether> I mentioned mine already
    [2019-05-06 13:22:56] <sarang> that you did
    [2019-05-06 13:22:58] <suraeNoether> and sgp_  reminded me to re-add matching to my list
    [2019-05-06 13:23:16] <suraeNoether> does anyone have any questions about konferenco or complaints or more action items to be added to the list of stuff to do for the research conference?
    [2019-05-06 13:23:23] ⇐ Cryptonic quit (~cryptonic@77.50.8.63): Remote host closed the connection
    [2019-05-06 13:23:31] <suraeNoether>  i'm asking this because sgp_ just reminded me how human and fallible my memory is for big lists of stuff to do :D
    [2019-05-06 13:23:32] <sarang> The speaking agenda for the conference is all set?
    [2019-05-06 13:23:43] → Cryptonic joined (~cryptonic@77.50.8.63)
    [2019-05-06 13:23:59] <suraeNoether> yep, i believe i'm waiting on two TBA titles. i need to add two sponsors to our list, Tari and Symas
    [2019-05-06 13:24:13] ⇐ Cryptonic quit (~cryptonic@77.50.8.63): Remote host closed the connection
    [2019-05-06 13:24:16] <sarang> I'm excited to speak and serve as panel moderator
    [2019-05-06 13:24:19] <suraeNoether> those sponsors are on the t-shirt design, but not the website
    [2019-05-06 13:24:23] <suraeNoether> oh man that's going to be a good panel
    [2019-05-06 13:24:55] <suraeNoether> i'm anticipating pretty rough questions for Voorhees and Gavigan actually
    [2019-05-06 13:25:45] <sarang> FYI questions for the panel will be submitted by the audience and then selected by moderators
    [2019-05-06 13:26:01] <sarang> to ensure quality and avoid the inevitable "a few follow-up questions..."
    [2019-05-06 13:26:28] <sarang> Since we have time, here's an open question... now that the next point release is being finalized, any thoughts from the room about desired changes for the next network upgrade?
    [2019-05-06 13:26:54] <suraeNoether> ^ i'm curious about this a lot
    [2019-05-06 13:27:04] <suraeNoether> the other day sarang asked me what i want to see in the next upgrade
    [2019-05-06 13:27:05] <sgp_> another ringsize revisit. 2 output min. payment ID stuff
    [2019-05-06 13:27:26] <suraeNoether> the next big change i want to see is CLSAG, since it'll be basically cutting our blockchain rate of growth by half
    [2019-05-06 13:27:36] <sarang> 25%
    [2019-05-06 13:27:36] <suraeNoether> but 2-out min and deprecating pay_id is on my list also
    [2019-05-06 13:27:38] <sarang> ish
    [2019-05-06 13:27:54] <suraeNoether> oh yeah there are some constants
    [2019-05-06 13:28:20] <sgp_> any chance for dandelion++? I don't know how long this would take
    [2019-05-06 13:28:31] <sarang> Probably not by fall, but it's not consensus
    [2019-05-06 13:28:36] <sarang> any client release could do it
    [2019-05-06 13:28:39] <sgp_> right, jut curious
    [2019-05-06 13:28:54] — suraeNoether thinks actually percentage is a bad metric anyway: we uniformly save *this many* hash-to-scalars and *this many* hash-to-points and so on with CLSAG, and so on
    [2019-05-06 13:29:12] <sgp_> are you anticipating any work on your end for RandomX? code is frozen and needs to be reviewed
    [2019-05-06 13:29:13] <suraeNoether> i heard a rumor that tari is looking into ristretto and monero's protocol
    [2019-05-06 13:29:30] <suraeNoether> i'm thinking we should invite someone from tari to give us an update on that for the meeting after next or something like that
    [2019-05-06 13:29:33] <sarang> sgp_: I'm working with hyc to solicit statements of work from reviewers
    [2019-05-06 13:29:43] <sarang> We have 4 interested firms
    [2019-05-06 13:29:52] <sgp_> great!
    [2019-05-06 13:30:24] <sarang> Once we get publicly-releasable statements we can put them on GitHub
    [2019-05-06 13:30:47] <sgp_> do you expect those within the month?
    [2019-05-06 13:30:52] <sarang> yes
    [2019-05-06 13:31:39] <suraeNoether> i'm very excited about that
    [2019-05-06 13:32:04] <suraeNoether> are the firms all auditing firms? should we consider trying to bring in a hardware firm to assess that end of the implementation?
    [2019-05-06 13:32:10] <suraeNoether> like, code-auditing i mean
    [2019-05-06 13:32:44] <sarang> We're getting reviewers with backgrounds in hardware design
    [2019-05-06 13:33:11] <sarang> It's tough because at some level "can this be built into hardware efficiently" is answered by designing such hardware
    [2019-05-06 13:33:49] <sarang> Part of the process will be getting feedback on which reviewers' experience aligns most closely with our goals
    [2019-05-06 13:33:59] <suraeNoether> fair nuff
    [2019-05-06 13:34:36] <sgp_> I don't have any other consensus-related questions and comments
    [2019-05-06 13:34:43] <sarang> Anyone else have any?
    [2019-05-06 13:35:31] <sarang> Righto!
    [2019-05-06 13:35:48] <sarang> In that case, thanks to everyone for participating today. Logs will be posted shortly to the GitHub agenda issue
    [2019-05-06 13:35:53] <sgp_> I have a really quick announcement
    [2019-05-06 13:35:56] <sarang> sure
    [2019-05-06 13:36:41] <sgp_> If you are interested in speaking, running a workshop, and/or volunteering at the Monero Village at Defcon in August, please fill out the CFP by June 3: http://monerovillage.org
    [2019-05-06 13:36:59] <sgp_> We already have some good submissions
    [2019-05-06 13:37:20] <sgp_> (done)
    [2019-05-06 13:37:20] <sarang> When https?
    [2019-05-06 13:37:30] <sgp_> whenever rehrar gets the time
    [2019-05-06 13:37:36] <sarang> :D
    [2019-05-06 13:37:42] <sarang> OK, we are now adjourned
    [2019-05-06 13:37:57] * sarang set the topic to Research meeting Mondays @ 17:00 UTC. Be excellent to each other.

# Action History
- Created by: SarangNoether | 2019-05-03T15:50:35+00:00
- Closed at: 2019-05-06T17:40:05+00:00
