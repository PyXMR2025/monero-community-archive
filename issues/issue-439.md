---
title: 'Research meeting: 19 February 2020 @ 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/439
author: SarangNoether
assignees: []
labels: []
created_at: '2020-02-13T22:40:21+00:00'
updated_at: '2020-02-19T19:15:07+00:00'
type: issue
status: closed
closed_at: '2020-02-19T19:15:07+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 19 February 2020 @ 18:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-02-19T19:15:07+00:00
    [2020-02-19 13:00:49] <sarang> OK, let's get started with the meeting
    [2020-02-19 13:00:50] <sarang> GREETINGS
    [2020-02-19 13:01:11] <sgp_> hello :)
    [2020-02-19 13:01:17] <n3ptune> Hello
    [2020-02-19 13:02:56] — needmonero90 waves
    [2020-02-19 13:03:01] <needmonero90> I caught the meeting!
    [2020-02-19 13:03:09] <needmonero90> I would like to note that the meetings are not listed in the calendar
    [2020-02-19 13:03:14] <needmonero90> idk if thats intentional
    [2020-02-19 13:03:37] <sarang> Which calendar?
    [2020-02-19 13:03:42] <UkoeHB_> Hi
    [2020-02-19 13:03:45] <sarang> And how are meetings applied to it?
    [2020-02-19 13:04:25] <ArticMine> Hi
    [2020-02-19 13:04:38] <sarang> Meeting times/agendas are always listed as meta repo github issues
    [2020-02-19 13:05:20] <sarang> Anyway, does anyone wish to begin the ROUNDTABLE with research topics of interest?
    [2020-02-19 13:05:39] <UkoeHB_> Yes
    [2020-02-19 13:05:48] <sarang> Take it away UkoeHB_
    [2020-02-19 13:06:55] <UkoeHB_> I finished designing an escrowed marketplace 'protocol' which hopefully solves issues encountered by rbrunner in his openbazaar integration analysis. Also, multisig and txtangle have been finalized.
    [2020-02-19 13:06:58] <UkoeHB_> https://www.pdf-archive.com/2020/02/19/zerotomoneromaster-v1-0-28/zerotomoneromaster-v1-0-28.pdf
    [2020-02-19 13:07:28] <sarang> Neat
    [2020-02-19 13:07:31] <UkoeHB_> Finally, I had an idea for reducing minimum fee variability, and likewise for putting antispam directly in the protocol instead of relying on minimum fee
    [2020-02-19 13:07:36] <sarang> Are you seeking analysis on those?
    [2020-02-19 13:07:40] <UkoeHB_> Which is issue #70
    [2020-02-19 13:07:52] <UkoeHB_> They are open for comments any time anywhere
    [2020-02-19 13:08:39] <UkoeHB_> Ah and sarang provided a draft for a tx knowledge proof chapter
    [2020-02-19 13:08:59] <sarang> aye
    [2020-02-19 13:09:00] <UkoeHB_> (not really my research :p)
    [2020-02-19 13:09:16] <sarang> Heh, it's more of a summary of what's in the codebase (and some changes)
    [2020-02-19 13:10:20] <sarang> I look forward to reading the update draft you linked
    [2020-02-19 13:10:40] <UkoeHB_>  A number of topics here are lonely and want attention btw https://github.com/monero-project/research-lab/issues
    [2020-02-19 13:11:11] <UkoeHB_> \end
    [2020-02-19 13:11:27] <sarang> Thanks UkoeHB_
    [2020-02-19 13:11:33] <sarang> Any questions or comments on those topics from anyone?
    [2020-02-19 13:11:41] <ArticMine> Yes
    [2020-02-19 13:11:48] <sarang> Please go ahead!
    [2020-02-19 13:12:16] <ArticMine> I have taken a look at issue 70
    [2020-02-19 13:12:40] <ArticMine> It actually has serious implications
    [2020-02-19 13:13:10] <ArticMine> When the LT medium increases substantially
    [2020-02-19 13:13:44] <ArticMine> I do have an idea for a solution
    [2020-02-19 13:14:05] <ArticMine> Very preliminary at this stage
    [2020-02-19 13:14:41] <ArticMine> As for an interim fix
    [2020-02-19 13:15:36] <ArticMine> The est is to pay the high or at least normal fee for escrows that are expected to last past the next hard fork
    [2020-02-19 13:16:18] <ArticMine> I will have comments on the issue in the next two weeks
    [2020-02-19 13:16:40] <ArticMine> end
    [2020-02-19 13:17:07] <sarang> Thanks ArticMine
    [2020-02-19 13:17:20] <sarang> Any other questions/comments from the topics presented by UkoeHB_?
    [2020-02-19 13:18:32] <sarang> Righto
    [2020-02-19 13:18:38] <sarang> I'll share a few things
    [2020-02-19 13:19:01] <sarang> First, the Stanford Blockchain Conference is happening right now (and the next couple of days), and has streaming available: https://cbr.stanford.edu/sbc20/
    [2020-02-19 13:19:38] <sarang> Second, I did some math/code related to multiparty stuff for next-gen protocols
    [2020-02-19 13:20:10] <sarang> Third, I worked on code and write-ups for transaction proofs, both for an updated PR and for inclusion in Zero to Monero for better documentation
    [2020-02-19 13:20:32] <sarang> Fourth, I used chain data from n3ptune and friends to do better estimates of the cumulative effects of next-gen protocols
    [2020-02-19 13:20:41] <sarang> both in chain growth and verification time
    [2020-02-19 13:21:01] <sarang> Major caveat: these assume the same input/output distribution as the current chain, and are _estimates_only_
    [2020-02-19 13:21:12] <sarang> and apply to post-bulletproof chain data only
    [2020-02-19 13:21:33] <sarang> https://usercontent.irccloud-cdn.com/file/ijaEAI7m/size.png
    [2020-02-19 13:21:58] <sarang> ^ this link shows the total chain growth estimates for various protocols with varying ring size
    [2020-02-19 13:22:12] <sarang> namely, from 16 to 1024 in powers of 2 (lines for visual aid only)
    [2020-02-19 13:22:38] <UkoeHB_> Sarang would you mind adding an indicator for MLSAG and CLSAG at the 11 ring size 'point'? For reference
    [2020-02-19 13:23:02] <sarang> Sure, let me grab that data from my spreadsheet
    [2020-02-19 13:23:07] <sarang> hold please
    [2020-02-19 13:23:18] <UkoeHB_> Or the super steep slope from 11 to 20 lol that goes off that chart
    [2020-02-19 13:24:02] <sarang> Heh, I had that data but didn't include it since it's crazy linear
    [2020-02-19 13:24:25] <sarang> I'm running the N=11 code for MLSAG/CLSAG, which I don't have handy 
    [2020-02-19 13:24:44] <sarang> Anyway, I'll pull up the time data while we wait
    [2020-02-19 13:24:55] <sarang> https://usercontent.irccloud-cdn.com/file/T7uWoFEp/time.png
    [2020-02-19 13:25:10] <sarang> ^ verification time estimate for _group_operations_only_ at varying ring sizes
    [2020-02-19 13:25:15] <UkoeHB_> I think it's interesting that all these protocols/signature schemes are similar size on the small end
    [2020-02-19 13:26:08] <sarang> All the verification times are linear (up to a logarithmic term due to multiexp)
    [2020-02-19 13:26:16] <UkoeHB_> Where is tryptich multi hiding?
    [2020-02-19 13:26:34] <sarang> It's underneath Triptych-single
    [2020-02-19 13:26:42] <sarang> They're essentially indistinguishable
    [2020-02-19 13:26:59] <selsta> Does Triptych single have advantages over multi?
    [2020-02-19 13:27:02] <sarang> RCT3-multi suffers due to input padding requirements that still have a linear verification effect
    [2020-02-19 13:27:15] <sarang> selsta: a complete soundness proof :)
    [2020-02-19 13:27:33] <sarang> Update on MLSAG/CLSAG size estimates...
    [2020-02-19 13:27:44] <UkoeHB_> Could you make a smaller graph from 0 to 128 ring size? Since those large ones seem pretty unreasonable
    [2020-02-19 13:27:56] <sarang> At N=11, MLSAG for that chain range is 7.84 GB, while CLSAG is 5.84 GB
    [2020-02-19 13:28:25] <sarang> (the actual size of that chain range is 7.9 GB)
    [2020-02-19 13:29:47] <sarang> https://usercontent.irccloud-cdn.com/file/DFhClmEe/time-small.png
    [2020-02-19 13:29:54] <sarang> ^ same time data, zoomed in
    [2020-02-19 13:30:29] <UkoeHB_> Perfect thanks :) are time estimates for CLSAG/MLSAG available?
    [2020-02-19 13:30:37] <sarang> Heh, just writing that out
    [2020-02-19 13:30:58] <sarang> I have very early estimates on that, which are tricky since multiexp doesn't apply, and hashing is nontrivial
    [2020-02-19 13:31:30] <sarang> MLSAG N=11 estimate is 29.9 hours for that chain range (but I have _not_ double-checked it)
    [2020-02-19 13:32:21] <ArticMine> What hardware was used for the verification time calculations?
    [2020-02-19 13:32:46] <sarang> It's a single core on a 2.1 GHz Opteron machine, with a bonkers amount of RAM
    [2020-02-19 13:33:01] <sarang> I would rely on the timing data only for comparisons, not absolute values
    [2020-02-19 13:33:32] <ArticMine> age of CPU?
    [2020-02-19 13:33:34] <sarang> I am still in the process of getting CLSAG data, which requires additional test code
    [2020-02-19 13:34:05] <sarang> It's a gen-3 Opteron, if that's what you mean
    [2020-02-19 13:34:14] <UkoeHB_> Is there a way others could run the same tests?
    [2020-02-19 13:34:15] <sarang> Again, only estimates using performance test code
    [2020-02-19 13:34:25] <sarang> For next-gen protocols, it's quite easy
    [2020-02-19 13:34:26] <ArticMine> Yes great it does give an idea thanks
    [2020-02-19 13:34:33] <sarang> Well, somewhat easy
    [2020-02-19 13:35:02] <sarang> You need to get multiexp performance timing data and use a linear interpolation that you plug into the simulator
    [2020-02-19 13:35:21] <sarang> For MSLAG/CLSAG you need to run more operation performance data
    [2020-02-19 13:35:44] <sarang> This is the simulator, which is still WIP: https://github.com/SarangNoether/skunkworks/blob/sublinear/estimate.py
    [2020-02-19 13:36:59] — Isthmus ducks in for 30 seconds
    [2020-02-19 13:37:10] <Isthmus> https://usercontent.irccloud-cdn.com/file/HuPcfLdT/image.png
    [2020-02-19 13:37:11] <sarang> But again, it's tricky to do comparisons between MLSAG/CLSAG and the next-gens
    [2020-02-19 13:37:19] — Isthmus ducks back out
    [2020-02-19 13:37:26] <Isthmus> (drive by data)
    [2020-02-19 13:38:00] <sarang> Wow, that's quite low
    [2020-02-19 13:38:09] <Isthmus> Oh yeah, the numbers are one thing. But moreso, we should all be more alarmed that analyzing something like this is possible for an outside observer
    [2020-02-19 13:38:17] <Isthmus> ;-)
    [2020-02-19 13:38:32] <sarang> Yep, and has certainly been a topic of interest!
    [2020-02-19 13:38:33] <Isthmus> It's a privacy risk to use subaddresses right now...
    [2020-02-19 13:38:51] <Isthmus> Anyways, I gotta bounce, sorry to spam n run
    [2020-02-19 13:40:37] <sarang> OK thanks for sharing the data Isthmus
    [2020-02-19 13:41:10] <sarang> Another good reminder that I/O structure reveals some information about subaddress use
    [2020-02-19 13:41:33] <sarang> Since Isthmus had to leave, were there other questions/comments on the data that I shared above?
    [2020-02-19 13:42:55] <sarang> UkoeHB_: if you want to run tests as well, let me know after the meeting and I can let you know how to get the numbers you'll need
    [2020-02-19 13:43:26] <UkoeHB_> My computer is quite weak, was just asking for viewers :)
    [2020-02-19 13:43:32] <sgp_> sarang: can you remind us on the plans to fix this subaddress thing?
    [2020-02-19 13:43:33] <sarang> ah ok
    [2020-02-19 13:44:22] <sarang> Requiring separate tx keys per output is a good idea, but IIRC didn't have a huge amount of support when last brought up
    [2020-02-19 13:44:56] <sarang> FWIW the size data that I presented for next-gens assumes a separate tx key per output
    [2020-02-19 13:45:31] <UkoeHB_> Is that necessary for the protocols?
    [2020-02-19 13:45:48] <sarang> For the proving systems, you mean? No, not at all
    [2020-02-19 13:45:58] <sarang> They don't care how you get signing keys
    [2020-02-19 13:47:06] <UkoeHB_> Can you estimate the amount of additional pub key data? Num outs * 32 and num tx * 32?
    [2020-02-19 13:47:21] <sgp_> sarang: why did it not get support now? complexity? size? verification time?
    [2020-02-19 13:47:26] <sarang> My numbers for MLSAG/CLSAG include separate tx keys too!
    [2020-02-19 13:47:57] ⇐ phire quit (phire@119.252.27.69): *.net *.split
    [2020-02-19 13:48:45] <sarang> Also: n3ptune's dataset includes the pubkey counts
    [2020-02-19 13:48:53] <sarang> So I could run that separately for a more direct count
    [2020-02-19 13:49:39] → phire joined (phire@119.252.27.69)
    [2020-02-19 13:49:51] <UkoeHB_> With only 3% subaddress adoption, the difference is likely on the order of 100MB
    [2020-02-19 13:50:08] <UkoeHB_> Or 2% of total size I think
    [2020-02-19 13:50:10] <sarang> that's probably a good order-of-magnitude estimate
    [2020-02-19 13:50:51] <sarang> But IIRC scanning requires checking all pubkeys
    [2020-02-19 13:51:09] <sarang> So either there needs to be a specified correlation, or there's added complexity in scanning
    [2020-02-19 13:51:19] <UkoeHB_> I think it costs ~1GB for 30mill pub keys btw
    [2020-02-19 13:51:29] <sarang> I think moneromooo had a better idea of the impacts, when it was brought up earlier
    [2020-02-19 13:52:42] <sarang> FWIW I think it's a good idea unless it's very compelling not to due to complexity
    [2020-02-19 13:54:20] <sarang> OK, we're running up to the one-hour mark...
    [2020-02-19 13:54:21] <sgp_> obviously without this change, the impacts are quite negative for network privacy........
    [2020-02-19 13:55:00] <sarang> It's differentiated data, but it doesn't leak _which_ outputs are subaddress-destined
    [2020-02-19 13:55:20] <sarang> (not that I'm saying that's a good reason to keep the current approach)
    [2020-02-19 13:55:25] → rottensox joined (~rottensox@unaffiliated/rottensox)
    [2020-02-19 13:55:31] <UkoeHB_> It's quite a lot of unused data, I'm a bit skeptical
    [2020-02-19 13:55:32] <sgp_> just reveals "one of this outputs goes to a subaddres?"
    [2020-02-19 13:55:42] <sarang> UkoeHB_:?
    [2020-02-19 13:55:54] <UkoeHB_> A lot of dummy data
    [2020-02-19 13:55:55] <sarang> sgp_: it reveals the number of subaddress outputs
    [2020-02-19 13:56:20] <UkoeHB_> sarang all it reveals is at least one of the outputs must be to a subaddress
    [2020-02-19 13:56:35] <sarang> Doesn't it reveal the total number of sub outs?
    [2020-02-19 13:56:42] <UkoeHB_> No
    [2020-02-19 13:57:21] <sarang> orly
    [2020-02-19 13:57:33] <UkoeHB_> How would it?
    [2020-02-19 13:57:48] <UkoeHB_> Number of additional pub keys always equals number of outs
    [2020-02-19 13:57:53] <UkoeHB_> Even if nonsubaddress
    [2020-02-19 13:58:13] <UkoeHB_> How is the CLSAG paper going?
    [2020-02-19 13:58:42] <sarang> Hmm, for some reason I thought otherwise; noted
    [2020-02-19 13:58:53] <sarang> I'm still waiting for suraeNoether
    [2020-02-19 13:59:03] <sarang> He wanted to continue working on his ideas for the security model
    [2020-02-19 13:59:11] <sarang> So unfortunately I am not the one to ask
    [2020-02-19 14:00:03] <sarang> OK, is there anything else of interest to share?
    [2020-02-19 14:00:23] <sarang> (Would be a good idea to continue discussing this after meeting, or on an issue, to keep it alive)
    [2020-02-19 14:00:58] <sgp_> definitely need an issue for it
    [2020-02-19 14:01:05] <sarang> All righty then; thanks to everyone for attending today
    [2020-02-19 14:01:09] <sarang> We are adjourned!


# Action History
- Created by: SarangNoether | 2020-02-13T22:40:21+00:00
- Closed at: 2020-02-19T19:15:07+00:00
