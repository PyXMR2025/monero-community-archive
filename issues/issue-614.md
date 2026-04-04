---
title: Monero Dev Meeting - Sun 03 October 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/614
author: carrington1859
assignees: []
labels: []
created_at: '2021-09-22T19:28:13+00:00'
updated_at: '2021-10-03T21:02:05+00:00'
type: issue
status: closed
closed_at: '2021-10-03T21:02:05+00:00'
---

# Original Description
Location: [Libera.chat, #monero-dev](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-dev:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211003T170000&p1=1440)

Main discussion topics:

1. Greetings

2. BP+ ( [1st Audit](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/197) , [2nd Audit](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/215) both have useful links)
3. Fee changes ( [PR](https://github.com/monero-project/monero/pull/7819) , [Discussion](https://github.com/monero-project/research-lab/issues/70), [Older Discussion](https://github.com/monero-project/monero/issues/5711) )
4. Decoy selection algorithm changes  ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) )
5. [Ringsize increase](https://github.com/monero-project/research-lab/issues/79)
6. Removing unlock time ( [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
7. Proposal to deprecate integrated addresses (Discussions on [github](https://github.com/monero-project/monero/issues/7889) & [reddit](https://www.reddit.com/r/Monero/comments/pbixk6/request_for_community_input_proposal_to_deprecate/)).
8. Any other business
9. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: ?


# Discussion History
## boogerlad | 2021-09-22T23:56:20+00:00
I'd like to kill integrated addresses

## carrington1859 | 2021-09-28T12:41:11+00:00
> I'd like to kill integrated addresses

Added. I suspect there won't be enough time to address all the issues listed here. We'll see what happens.

## ArticMine | 2021-10-03T04:12:33+00:00
I am requesting that due to the recent developments agenda item 2 be discussed after agenda item 5. Thanks.

## carrington1859 | 2021-10-03T16:03:33+00:00
> I am requesting that due to the recent developments agenda item 2 be discussed after agenda item 5. Thanks.

Makes sense. Done.

## UkoeHB | 2021-10-03T19:23:59+00:00
```
[10-03-2021 17:05:41] <moneromooo> Hello people. Someone wanted a meeting. So since they do not seem to be around yet, anyone wants to talk about dev related things ?
[10-03-2021 17:05:45] <Rucknium[m]> <carrington[m]> "I can only be present intermitte..." <- ^ Does someone want to volunteer to moderate?
[10-03-2021 17:05:50] <sgp_1> Who is running? :)
[10-03-2021 17:05:53] <monerobull[m]> Well, lets start with point one on the agenda. Thanks to everyone for coming. Who would like to tell us about BP+?
[10-03-2021 17:06:14] <moneromooo> It's ready to go in, code wise. Can't recall whether it's been audited now.
[10-03-2021 17:06:18] <selsta> BP+ is basically ready, it's missing an approval on Github. Wownero has been running it for a couple months.
[10-03-2021 17:06:31] <selsta> It is audited.
[10-03-2021 17:06:40] <monerobull[m]> Seems to have been audited twice, anyone audited the audits?
[10-03-2021 17:06:41] <Inge> There was no change in ring size for BP+ impl?
[10-03-2021 17:06:55] <moneromooo> BP+ does not care about rings.
[10-03-2021 17:06:55] <selsta> Ring size is separate.
[10-03-2021 17:07:53] <rbrunner> I guess that missing aproval on GitHub is a formularity then?
[10-03-2021 17:07:54] <monerobull[m]> Could someone quickly summarize what BP+ adds to BPs?
[10-03-2021 17:08:15] <moneromooo> It doesn't add, it removes :D
[10-03-2021 17:08:19] <moneromooo> (bytes)
[10-03-2021 17:08:23] <vtnerd_> there are some source code conflicts that need to be resolved
[10-03-2021 17:08:27] <sgp_1> BP+ are simply more efficient than BP
[10-03-2021 17:08:42] <moneromooo> For the BP patch, vtnerd ?
[10-03-2021 17:08:51] <vtnerd_> yeah, thats what Github says
[10-03-2021 17:09:03] <moneromooo> OK, I'll fix then soon then. Thanks.
[10-03-2021 17:09:28] <monerobull[m]> Sounds great. Anything else to add to the topic or do we move on to the next one?
[10-03-2021 17:10:13] <sgp_1> One minor BP+ thing
[10-03-2021 17:10:44] <sgp_1> Any progress on using the BP+ storage for a txid - type/soze string or not yet?
[10-03-2021 17:11:07] <sgp_1> s/soze/size
[10-03-2021 17:11:34] <moneromooo> I did work on that recently ish, but it kinda sucked, only the sender can retrieve the data without leaking the index of the real spend.
[10-03-2021 17:11:37] <rbrunner> As something like an tx_extra alternative?
[10-03-2021 17:12:32] <moneromooo> It was better for.... forgot its name... the pre-seraphis ring algorithm from sarang, where you send 32 bytes without leakage. But I've not done the code for it yet. And might not since we might use seraphis instead.
[10-03-2021 17:12:35] <sgp_1> moneromooo: Ah okay thanks
[10-03-2021 17:12:58] <rbrunner> Triptych :)
[10-03-2021 17:13:03] <moneromooo> Right :D
[10-03-2021 17:13:30] <moneromooo> Does seraphis allow such stashage without leakage btw ?
[10-03-2021 17:13:58] <sgp_1> I think only Koe, Aaron, or Aram could answer that right now
[10-03-2021 17:16:22] <jberman> Moving on to 3? Fee changes
[10-03-2021 17:16:29] <monerobull[m]> Alright, the next topic is about changes to transaction fees. Ive read into it a little and it doesnt seem to be of the highest priority right now since it seems to only be important should there be a drastic increase to the amount of daily transactions but it should still be looked at.
[10-03-2021 17:16:59] <moneromooo> It's ready AFAIK. ukoeHB reviewed it.
[10-03-2021 17:17:06] <sgp_1> No it definitely is high priority
[10-03-2021 17:17:16] <Rucknium[m]> In my view, its priority has become more urgent due to the tx volume anomaly
[10-03-2021 17:17:32] <ArticMine> There is a consensus change here. If current trends continue we could reach the penalty zone in 12 - 18 months
[10-03-2021 17:18:21] <ArticMine> The consensus portion needs tp go into the next HF
[10-03-2021 17:18:24] <rbrunner> Hmmm ... would that mean more than simply growing blocks?
[10-03-2021 17:18:34] <rbrunner> (Reaching the penalty zone)
[10-03-2021 17:18:40] <sgp_1> ArticMine you need an agreement on the ringsize to finalize this right?
[10-03-2021 17:19:38] <ArticMine> The current formulation allows for a ring size up to 26
[10-03-2021 17:20:01] <sgp_1> Ah so no blocker there then re ringsize for now
[10-03-2021 17:20:23] <ArticMine> So with the discussion between 15 - 25 there is no blocker
[10-03-2021 17:21:32] <monerobull[m]> Anything else on the topic? Maybe someone can tell us how or if this will impact regular users at all?
[10-03-2021 17:22:19] <sgp_1> Marginally higher base fees, greater fee downward pressure at large volumes
[10-03-2021 17:22:22] <moneromooo> They'll pay peanuts in fees instead of fifts of peanuts.
[10-03-2021 17:22:41] <rbrunner> Well, would this be the right time to settle on a number already? If not, what is still missing for doing so?
[10-03-2021 17:23:08] <sgp_1> rbrunner: If this is re ringsize wait for 5 pls
[10-03-2021 17:23:21] <ArticMine> thanks
[10-03-2021 17:23:23] <rbrunner> Oh, ok, separate topic. Sorry.
[10-03-2021 17:23:39] <sgp_1> :)
[10-03-2021 17:23:57] <monerobull[m]> We still got a lot of headroom so this shouldnt be a problem. Good job ArticMine.
[10-03-2021 17:24:13] <ArticMine> Thanks
[10-03-2021 17:24:36] <monerobull[m]> Moving on to the next topic: Decoy selection algorithm changes
[10-03-2021 17:24:53] <moneromooo> Indeed, the pdf was very detailed/precise.
[10-03-2021 17:25:07] <Rucknium[m]> I don't know if jberman is here right now. Anyway, "my portion" of improvements to the decoy selection algorithm have been much discussed recently, to say the least. I have a CCS proposal in the "idea" stage.
[10-03-2021 17:25:07] <moneromooo> Thorough it the word I was looking for :D
[10-03-2021 17:25:40] <moneromooo> Yeah! More code, less, er, other things.
[10-03-2021 17:25:57] <jberman> Patching integer truncation is still sitting in PR 7798
17:25:57 * moneromooo approves of this planned work
[10-03-2021 17:26:02] <Rucknium[m]> The following is new public information. Previously I had said publicly that an "applied statistician" was reviewing my HackerOne submission.
[10-03-2021 17:26:18] <Rucknium[m]> Now I can say that :
[10-03-2021 17:26:18] <Rucknium[m]> Syksy, who holds a Ph.D. in biostatistics, is in the process of examining the HackerOne submission.
[10-03-2021 17:26:28] <Rucknium[m]> Syksy links his username to his real identity, so interested individuals can do their own due diligence if they prefer. moneromooo could comment as well.
[10-03-2021 17:26:31] <sgp_1> Are there any others besides 7798 that are waiting for merge
[10-03-2021 17:27:01] <monerobull[m]> rucknium, some people are really concerned since you want to keep some part of your work undisclosed to the public. Can you explain what exactly that would be? 
[10-03-2021 17:27:21] <binaryFate> I don't think we should even discuss that at the moment at all.
[10-03-2021 17:27:43] <jberman> sgp_1 nope, nothing else at the moment in PR stage
[10-03-2021 17:27:49] <selsta> sgp_1: any other what?
[10-03-2021 17:27:50] <sgp_1> Agreed
[10-03-2021 17:28:11] <Rucknium[m]> monerobull[m]: I'm not sure that at the end of the day, that will be the case. I think I shouldn't disclose everything right now, as my CCS proposal is being discussed and possibly funded. But later, maybe, probably, most things will be released. It's out  of my hands, anyway
[10-03-2021 17:28:15] <ArticMine> <binaryFate> I don't think we should even discuss that at the moment at all <--- agree
[10-03-2021 17:28:23] <sgp_1> In this dev meeting, I'm more interested in making sure all the desired decoy updates for this round are in and ready to go
[10-03-2021 17:28:33] <jberman> I also recommended in 7798 to reduce the "recent spend window" where the algo selects an output from [10-03-2021 the recent window] if gamma suggests an output < lock time
[10-03-2021 17:29:19] <jberman> I recommended reducing it from 50 blocks to 10, because 50 was selected assuming integer truncation would not be patched, and so 50 selected a wider portion of the very recent blocks
[10-03-2021 17:29:32] <UkoeHB> re: fee PR, I’d like someone else to review as well in case I missed some detail. vtnerd selsta maybe?
[10-03-2021 17:29:44] <rbrunner> You mean the code in 7798 does that? Not sure how to understand "recommended"
[10-03-2021 17:29:45] <selsta> it's too complicated for me
[10-03-2021 17:29:57] <selsta> I doubt I can review much there but I can take a look
[10-03-2021 17:29:58] <sgp_1> jberman: Seems reasonable, and luckily this is an edge case
[10-03-2021 17:30:19] <UkoeHB> Maybe one of the guys who show up saying ‘let me do something’ could review?
[10-03-2021 17:30:23] <jberman> rbrunner The code in 7798 doesn't do that, it's sech1' PR . I'll create a new PR
[10-03-2021 17:30:26] <monerobull[m]> Unrelated: is anyone keeping notes or should i do that?
[10-03-2021 17:30:40] <moneromooo> Do we stil have a recent spend window ? I thought that was gone with the switch to gamma...
[10-03-2021 17:30:41] <vtnerd_> UkoeHB - already put the fee PR review in my todo list ...
[10-03-2021 17:30:44] <UkoeHB> monerobull[m]: usually we post all the logs in the issue
[10-03-2021 17:30:49] <UkoeHB> Great thanks vtnerd
[10-03-2021 17:31:22] <sgp_1> monerobull[m]: It would be helpful for you to later post the logs and a neutral summary on GitHub and forum.monero.space if you're offering :)
[10-03-2021 17:31:47] <vtnerd_> the recent spend window is when gamma "selects" blocks 0-10
[10-03-2021 17:31:57] <jberman> Right
[10-03-2021 17:32:07] <jberman> Wait no sorry
[10-03-2021 17:32:09] <moneromooo> Oh a new thing. OK, sorry, don;'t mind me.
[10-03-2021 17:32:11] <vtnerd_> tossing that result ruins the intended distribution
[10-03-2021 17:32:14] <monerobull[m]> sgp_1: Sorry, I dont have a clue how i would do that, best i can do is a reddit post with a summery on each topic ^^
[10-03-2021 17:32:30] <UkoeHB> Someone else can get it no worries
[10-03-2021 17:33:00] <jberman> vtnerd as in, if the gamma selects an output 5 blocks ago, and then tosses, it ruins the intended distribution youre' saying?
[10-03-2021 17:33:51] <vtnerd_> correct, that was the change I saw for monero-lws, no? to _not_ throwaway selections in the locked phase
[10-03-2021 17:34:14] <jberman> Yep. Didn't see moo's question
[10-03-2021 17:35:04] <vtnerd_> moo was just unclear what recent spend window meant, because it sounded like an older algorithm used a few years back
[10-03-2021 17:35:04] <jberman> Idea is to re-select an output at random from the "recent spend window"
[10-03-2021 17:35:42] <jberman> Will submit a PR to drop that window from blocks 10-60 (what it is now), to blocks 10-20
[10-03-2021 17:36:20] <sgp_1> And this only impacts txs with a lock_time or all txs?
[10-03-2021 17:36:31] <jberman> All txs
[10-03-2021 17:37:18] <jberman> Next up on that list is "binning"
[10-03-2021 17:37:35] <sgp_1> I assume you're choosing 10 because it's a better fit? Can you include data for that in the PR you make?
[10-03-2021 17:39:23] <jberman> 7798 shows the impact of what it would look like on the distribution for early blocks on a chart. I don't exactly know what framework to use to actually determine "better fit", since there is no guaranteed way to know as far as we know
[10-03-2021 17:40:48] <UkoeHB> > what it would look like 
[10-03-2021 17:40:48] <UkoeHB> the integer truncation I assume fix
[10-03-2021 17:40:56] <UkoeHB> fix I assume*
[10-03-2021 17:41:26] <jberman> shows what fixing integer truncation + modifying the recent spend window look like, with different windows
[10-03-2021 17:41:47] <jberman> e.g. https://user-images.githubusercontent.com/26468430/132962516-f71800a4-0cfa-4b91-bc1e-28ecbceac330.png
[10-03-2021 17:42:09] <UkoeHB> re: binning, jberman were you hoping to push for binning in the upcoming hard fork?
[10-03-2021 17:42:27] <jberman> I think that depends on unlock time
[10-03-2021 17:42:48] <jberman> it seems there is a lot of support for deprecating unlock times
[10-03-2021 17:43:25] <jberman> is it reasonable to push for deprecation of a feature that soon?
[10-03-2021 17:43:28] <Rucknium[m]> I would like to have a statistician look at binning before it is implemented in production code.
[10-03-2021 17:43:31] <monerobull[m]> If everyone agrees we can discuss unlock times right now and ringsizes after.
[10-03-2021 17:43:32] <UkoeHB> Maybe another question would be, do we want to introduce significant new changes/PRs for the next hard fork?
[10-03-2021 17:43:54] <UkoeHB> Or take what we have and wrap it up?
[10-03-2021 17:43:54] <Rucknium[m]> I mean, I have "looked at" it, but not really examined it with much scrutiny.
[10-03-2021 17:44:36] <sgp_1> I'm definitely somewhat worried about trying to squeeze binning in
[10-03-2021 17:44:44] <jberman> UkoeHB my thinking is no, would rather not hold up the other changes in the pipeline, and take time to get other things done right
[10-03-2021 17:45:06] <sgp_1> jberman: I just eyeballed it, but 10 or 15 seem the most sensible so I say it looks good
[10-03-2021 17:45:09] <rbrunner> Code-wise, binning would basically starting from zero, right?
[10-03-2021 17:45:26] <moneromooo> Binning really ought to go in with seraphis/triptych/whatever.
[10-03-2021 17:46:07] <sgp_1> moneromooo: I generally agree with this yes
[10-03-2021 17:46:10] <UkoeHB> That makes the most sense to me.
[10-03-2021 17:46:58] <jberman> What I was trying to show with 86 is that binning as a fallback for any inconsistencies in the gamma/other timing related analysis would still be sensible to consider with ring sizes close to today's/slightly higher
[10-03-2021 17:47:03] <jberman> MRL issue 86
[10-03-2021 17:47:56] <binaryFate> I suspect it's pretty easy to prove that a slight increase of the ring + some binning does not degrade situation wrt. now
[10-03-2021 17:48:08] <binaryFate> (and of course is very likely to improve it)
[10-03-2021 17:48:29] <Rucknium[m]> If binning does what it says it does, then it seems to me that it would reduce the statistical attack surface of ring signatures.
[10-03-2021 17:48:48] <Rucknium[m]> I am not certain that it does what it says since I haven't examined it closely.
[10-03-2021 17:49:53] <moneromooo> Actually I was thinking of binning including parametric ring description. Binning alone is wallet only so could go in.
[10-03-2021 17:50:17] <moneromooo> Though it'd likely mean other wallets would not follow suit, or with a delay, giving isthmus more puddles.
[10-03-2021 17:50:25] <sgp_1> It appears to me we have 2 potential options right now: 1) skip binning, or 2) do very simple binning to get the easy win(s). Is that fair, and is 2 a realistic goal for a very short time period?
[10-03-2021 17:50:47] <jberman> I think 2 is realistic for a very short time period, yes
[10-03-2021 17:51:02] <jberman> But moo is right it has the issue of more puddles
[10-03-2021 17:51:13] <Rucknium[m]> Who has vetted binning?
[10-03-2021 17:51:19] <UkoeHB> Yeah with small rings, binning makes sense to be wallet-side.
[10-03-2021 17:51:30] <moneromooo> Nobody, since there's no proposed algorithm yet.
[10-03-2021 17:51:37] <UkoeHB> You'd probably only get 2-3 ring members per bin
[10-03-2021 17:51:40] <Rucknium[m]> Isn't it directly from Moser et al. (2018)? Or have more papers discussed it?
[10-03-2021 17:52:19] <Rucknium[m]> moneromooo: Then (2) above seems infeasible.
[10-03-2021 17:52:24] <sgp_1> I feel a little lost on tracking the progress of binning, so a clear summary of the situation and desired change would help me
[10-03-2021 17:52:36] <binaryFate> not sure everyone has same definition of "very simple binning" in mind 
[10-03-2021 17:52:59] <UkoeHB> Rucknium[m]: these guys also basically advocate for binning https://petsymposium.org/2021/files/papers/issue3/popets-2021-0047.pdf
[10-03-2021 17:53:00] <ArticMine> The question I have with binning is number of bins and number of ring ring member per ring
[10-03-2021 17:53:17] <jberman> I'll write up a PoC for "very simple binning" in the wallet, and that can be vetted/reviewed
[10-03-2021 17:53:30] <ArticMine> per bin
[10-03-2021 17:53:30] <UkoeHB> Thanks jberman 
[10-03-2021 17:53:35] <sgp_1> Okay cool, maybe it's best to wait for that
[10-03-2021 17:53:39] <binaryFate> thanks 
[10-03-2021 17:53:44] <Rucknium[m]> UkoeHB: Yeah I saw that paper. Haven't gone line-by-line though.
[10-03-2021 17:54:10] <UkoeHB> Their 'partitioning' concept is essentially binning.
[10-03-2021 17:54:19] <moneromooo> One funny thing is that if Alice splits an output (to herself), someone might use both of these in a ring since they're contiguous.
[10-03-2021 17:54:43] <moneromooo> That might be good. Not sure...
[10-03-2021 17:54:50] <Rucknium[m]> Which makes me suspicious of their work since they don't cite it as specifically coming from Moser et al. (2018). Trying to hide that it isn't too novel?
[10-03-2021 17:55:12] <moneromooo> (assuming binning picks contiguous outputs and not outputs in the same general area).
[10-03-2021 17:55:16] <jberman> I wasn't thinking of selecting contiguous outputs
[10-03-2021 17:55:20] <Rucknium[m]> I mean, that's a research ethics issue
[10-03-2021 17:55:32] <sgp_1> rucknium[m]: There have probably been dozens of papers over the years that recommend binning of some form
[10-03-2021 17:55:50] <Rucknium[m]> sgp_[m]: Send them my way then
[10-03-2021 17:56:06] <monerobull[m]> Waiting for jbermans writeup sounds good, do we move on to the next point on the list? Its the porposed ringsize increase. Im not sure how urgent this is, till when do we need to decide this?
[10-03-2021 17:56:40] <UkoeHB> Partitioning is like 'one big bin', while Moser's binning is like 'several bins from the gamma'. Moser's binning is technically 'mimicking + partitioning' in that paper (which they advocate for).
[10-03-2021 17:56:40] <sgp_1> I think unless someone has a strong argument otherwise, we go with ringsize 16
[10-03-2021 17:57:09] <moneromooo> lol
[10-03-2021 17:57:22] <sgp_1> There's roughly strong support for anywhere 15-19
[10-03-2021 17:57:33] <sgp_1> And knaccc made the best argument for 16 in particular imo
[10-03-2021 17:57:38] <ArticMine> This is a hard fork. My though here is can we accommodate binning with the choice of ring size
[10-03-2021 17:58:04] <monerobull[m]> Ringsize 16 because it would be compatible with the tryptich alternative, right?
[10-03-2021 17:58:21] <sgp_1> monerobull[m]: No it would significantly change then
[10-03-2021 17:58:23] <jberman> Binning not dependent on ring size, in theory could just have remainder in a separate smaller bin
[10-03-2021 17:58:26] <UkoeHB> monerobull[m]: triptych/etc/ would have ring size 64-256
[10-03-2021 17:58:51] <jberman> But probably would be nicer to have equal sized bins
[10-03-2021 17:59:06] <ArticMine> for example 8 bins 2 ring members per bin 16 or 3 members per bin 24
[10-03-2021 17:59:28] <binaryFate> what is the best argument for 16? missed that
[10-03-2021 17:59:34] <UkoeHB> I think 16 is good, less than 50% increase in per-ring-member cost.
[10-03-2021 17:59:56] <ArticMine> 8 bins 2 member per bin
[10-03-2021 18:00:14] <ArticMine> also using a per of 2 for the number of bins
[10-03-2021 18:00:20] <ArticMine> power
[10-03-2021 18:00:30] <sgp_1> binaryFate: knaccc shared relatively favorable churning characteristics for that number in particular. Besides that, it's similar to 15-17, so it's the only number that really stands out
[10-03-2021 18:00:44] <ArticMine> the next I would consider is 24 8 bins 3 members per bin
[10-03-2021 18:00:59] * monerobull[m] uploaded an image: (17KiB) < https://libera.ems.host/_matrix/media/r0/download/matrix.org/uIOghXobQrJjHxVUgfrSStqC/image.png >
[10-03-2021 18:02:00] <binaryFate> Ok I always found this psychologic "1 million" target arbitrary. But nothing against it anyway.
[10-03-2021 18:02:17] <binaryFate> Slightly sad we depart from primes :)
[10-03-2021 18:02:41] <sgp_1> ArticMine: I think this is fair to consider with the binning discussion once we can review the overview. I'm not against this if there is a substantial gain in privacy
[10-03-2021 18:03:03] <sgp_1> binaryFate: I agree it's arbitrary
[10-03-2021 18:03:41] <binaryFate> ArticMine's reason is a good one, we don't know how/if we put binning in place before next-gen signature schemes, but with 16 we'd be more flexible
[10-03-2021 18:03:51] <jberman> wrt number of bin members and bins, Moser did some solid analysis on that front. Need to review and probably research further to arrive at a solid decision. But going with ring size 16, and 2 members per bin, you get the benefit of binning, and still maintain the highest degree of the current implementation. So I think it's a sensible incremental
[10-03-2021 18:03:52] <jberman> approach
[10-03-2021 18:04:50] <jberman> 7 "bins" would be gamma selected, basically, as opposed to the current 10
[10-03-2021 18:05:07] <sgp_1> vtnerd, are you still skeptical about binning? Do you see the anonymity in practice dropping from today's 11 to 8 tomorrow (if we went with 8bin by 2 output)?
[10-03-2021 18:06:19] <ArticMine> Yes which I why I would consider 24 as the next alternative. with the option of 12 bins 2 elements per bin or 8 bins with 3 elements per bin 
[10-03-2021 18:07:04] <monerobull[m]> It sounds like everyone is onboard with ringsize 16, not sure what happens now but I assume we move on to "removing unlock time". There is currently no real use for it and out of the last million blocks less than 200 transactions utelized this feature, most of which were falsly configured anyways.
[10-03-2021 18:07:41] <vtnerd_> eh I don't know, I keep changing my mind about binning
[10-03-2021 18:08:25] <jberman> did MRL issue 86 have any impact on your thoughts, or was that all a wash :)
[10-03-2021 18:08:40] <vtnerd_> theres a point where binning is clearly recuding/revealing time windows, otoh it helps when the attacker definitely knows a time window 
[10-03-2021 18:09:57] <jberman> the argument that it's a backup if the gamma is missing outputs doesn't have much strength you think?
[10-03-2021 18:10:17] <vtnerd_> so from 11->8 reduces possible spend timeframes, but still might be a win. its just hard to quantify
[10-03-2021 18:10:26] <Rucknium[m]> vtnerd_: So, binning may not strictly improve privacy under all threat models? Is that what you are saying? It may reduce privacy for some threat models?
[10-03-2021 18:11:13] <sgp_1> Yeah binning is strictly better for some and strictly worse for others, so it's a balancing act
[10-03-2021 18:11:15] <ArticMine> I depends on how well one trusts the the gamma
[10-03-2021 18:11:50] <jberman> It definitely could reduce privacy in some ways, if the gamma was perfect, and if there is no timing footprint, then you'd want the highest number of gamma selected outputs
[10-03-2021 18:12:22] <Rucknium[m]> ArticMine: It seems there are varying opinions about how well to trust the gamma distribution. hmmm
[10-03-2021 18:12:57] <vtnerd_> Rucknium[m]: Im not certain, because I would have to spend more sketching out a potential tracing tool
[10-03-2021 18:13:04] <Rucknium[m]> "there is no timing footprint" ... There seems to be some sort of sleep-wake cycle in the data. Not surprising, I suppose.
[10-03-2021 18:13:24] <Rucknium[m]> vtnerd_: Seems like binning has not been fully vetted
[10-03-2021 18:13:25] <binaryFate> Rucknium[m]: both ArticMine and I (and few others) are reviewing your submission, so I'd let related discussion for later once feedback is gathered and this discussion can be more public
[10-03-2021 18:13:27] <sgp_1> jberman: It's fair to assume there could be a timing footprint however in some cases, and that taking the gamma loss is still a net + overall
[10-03-2021 18:13:50] <vtnerd_> taken to the extreme, if you've got only 2 bins, this effectively tells the attacker that the real output was received within 2 time windows
[10-03-2021 18:14:08] <Rucknium[m]> binaryFate: Understood.
[10-03-2021 18:14:09] <binaryFate> It seems to me not everyone has the same definition of binning, or that we mix binning with current ring size with binning with increased ring size. Not sure it's very productive in that context.
[10-03-2021 18:14:12] <sgp_1> We could not compromise at all and choose 11 bins, 2 outputs per bin :p
[10-03-2021 18:14:30] <ArticMine> Then ring 22
[10-03-2021 18:14:56] <sgp_1> Seems wasteful but hey no hard decisions
[10-03-2021 18:14:58] <vtnerd_> otoh, I don't know how valuable that is in tracing
[10-03-2021 18:15:01] <UkoeHB> This uncertainty is why I originally did not propose binning for small ring sizes. If the ring size greatly increases, then you can have _both_ an incremental gain in time windows, _and_ start mitigating known-timing analysis.
[10-03-2021 18:15:04] <ArticMine> or increase the gamma to 12v with ring 24
[10-03-2021 18:15:38] <binaryFate> Personally I'd wait to see jberman write up to elaborate more, so at least we have a basis for more structured discussion
[10-03-2021 18:16:01] <jberman> (y) 
[10-03-2021 18:16:14] <sgp_1> I think we're all roughly on the same page of understanding
[10-03-2021 18:17:25] <vtnerd_> jberman: MRL 86 didn't change my thinking about binning specifically, but helped highlight 2 difficulties in the distribution selection 
[10-03-2021 18:17:28] <selsta> how would binning affect verification time?
[10-03-2021 18:18:16] <jberman> A simple wallet-only approach wouldn't affect it at all
[10-03-2021 18:19:01] <vtnerd_> oh no sorry, no jberman it did highlight why binning would be useful
[10-03-2021 18:19:51] <vtnerd_> it just didn't change that there may be a downside
[10-03-2021 18:20:12] <jberman> Makes sense :)
[10-03-2021 18:20:29] <monerobull[m]> I assume we now move on to "removing unlock time". There is currently no real use for it and out of the last million blocks less than 200 transactions utelized this feature, most of which were falsly configured anyways. Best case someone forces themselves to hodl for a few years, worst case its used in a malicious way to lock funds forever. In any case they currently make transactions stand out from the rest.
[10-03-2021 18:21:19] <jberman> Every time it's brought up in these meetings, everyone kind of just repeats no one wants it
[10-03-2021 18:21:27] <rbrunner> One question about dropping unlock_time that came up again today on Reddit: Could Monero, without any big technical effort or problems, honor locks for "old" transactions after the hardfork?
[10-03-2021 18:21:40] <moneromooo> Yes.
[10-03-2021 18:21:56] <rbrunner> Any connection with binning, perhaps?
[10-03-2021 18:22:07] <moneromooo> Or with range proofs ?
[10-03-2021 18:23:05] <UkoeHB> rbrunner: 1) if small-ring-size binning is implemented (wallet-side), then it is easy to work around past locked outputs; 2) if large-ring-size binning is implemented (deterministic), then all outputs would be segregated from old outputs anyway (new key image construction), so no concern
[10-03-2021 18:23:30] <rbrunner> If old locks stay valid, those HODLers could now lock before the hardfork, and all is good :)
[10-03-2021 18:24:14] <moneromooo> Oh, one thing lock time was good at: some people like proof of burn for some reason.
[10-03-2021 18:24:59] <ArticMine> Yes the application where the lock time is > age of universe 
[10-03-2021 18:25:21] <rbrunner> But I think there are other ways to burn?
[10-03-2021 18:25:53] <jberman> Can't you send to 0 address and provide the tx key?
[10-03-2021 18:25:54] <moneromooo> Yes, presumably sending to a public key that looks not random.
[10-03-2021 18:25:56] <vtnerd_> send the funds to point at infinity?
[10-03-2021 18:26:44] <moneromooo> I like that. I sent monero to infinity. Actually I dn't like that at all, I just like the sound of it.
[10-03-2021 18:27:35] <jberman> in the related MRL issue (78), yorha-0x talked about the use case where you want someone holding Monero for a set duration to perform some role for that period of time
[10-03-2021 18:28:50] <jberman> they used it for smooth to prove unspent funds, and there are alternatives to proving unspent funds
[10-03-2021 18:29:10] <jberman> but that's a use case at least
[10-03-2021 18:30:01] <jberman> not sure how practical it is and no one seems to be using it for that purpose
[10-03-2021 18:30:27] <rbrunner> On the other hand, 200 txs in a million is pretty damning, thinking of it. Maybe just the psychological problem of letting go something.
[10-03-2021 18:31:41] <jberman> by damning, you're saying "low", right?
[10-03-2021 18:32:09] <rbrunner> Yes, it seems to speak loud and clearly that nobody really wants and nobody really needs
[10-03-2021 18:32:20] <rbrunner> Despite some ideas that we may have.
[10-03-2021 18:32:42] <jberman> Agree
[10-03-2021 18:32:42] <UkoeHB> rbrunner: afaik there has never been a hard fork to remove a consensus feature (just a wallet feature - unencrypted payment ids)
[10-03-2021 18:33:18] <rbrunner> Yes, I agree it's worth it to be careful to take something away.
[10-03-2021 18:33:40] <rbrunner> But maybe we have done "due diligence" now already.
[10-03-2021 18:33:55] <monerobull[m]> imop there should just be a reddit post pinned on the sub for a few days before its removed telling people if they want to force hodl, they now have the last chance to lock funds.
[10-03-2021 18:34:15] <moneromooo> 0-rings got removed I guess.
[10-03-2021 18:34:45] <moneromooo> The ability to claim less block reward than you can.
18:34:52 * moneromooo unashamed pedant
[10-03-2021 18:35:36] <jberman> I think that's a comparable thing, considering it's something no one really uses :)
[10-03-2021 18:36:16] <jberman> reddit post sounds good to me
[10-03-2021 18:36:34] <ArticMine> It will provide useful feedback
[10-03-2021 18:36:40] <monerobull[m]> for some outside perspective, im not a dev, just a  regular user. if you told me privacy improves and blockchain grows a little slower in exchange for some feature that is barely ever used, id be happy you made the change
[10-03-2021 18:37:07] <rbrunner> A general Reddit post then, not just a few days before deadline, for the HODLers?
[10-03-2021 18:37:37] <rbrunner> If yes, I was thinking about doing one, but in the end was too lazy until now ...
[10-03-2021 18:37:55] <monerobull[m]> i dont think you need to pin this for another 12 months, would probably lead to peole experimenting and some locking funds forever
[10-03-2021 18:38:51] <rbrunner> In any case, just an post to inform about the dropping of a feature
[10-03-2021 18:39:10] <rbrunner> Because unused or not, dropping features is special
[10-03-2021 18:39:23] <rbrunner> at least to some degree
[10-03-2021 18:39:53] <monerobull[m]> Ill make a post asking for feedback
[10-03-2021 18:40:25] <rbrunner> Nice
[10-03-2021 18:41:25] <monerobull[m]> Alright, last specifically named topic for today: integrated addresses
[10-03-2021 18:42:21] <rbrunner> Seems quite a big topic, given that time is quite advanced already. Maybe next meeting?
[10-03-2021 18:42:21] <monerobull[m]> do the exchanges already use subadresses?
[10-03-2021 18:43:07] <monerobull[m]> everyone ok with that?
[10-03-2021 18:43:10] <rbrunner> Well, maybe not big, but potentially controversal and multi-faceted
[10-03-2021 18:43:52] <monerobull[m]> Any other business?
[10-03-2021 18:44:15] <selsta> A lot of exchanges / merchants still use integrated addresses. It would be a controversial change.
[10-03-2021 18:44:51] <binaryFate> let's push to next meeting, not sure everyone is still around with enough time. Large enough topic indeed
[10-03-2021 18:44:54] <selsta> yep
[10-03-2021 18:45:58] <jberman> IIRC one of the hopes for this meeting was to think about/set a date for next hard fork. Is there any loose idea on that?
[10-03-2021 18:46:50] <jberman> or still too early to say
[10-03-2021 18:47:16] <monerobull[m]> Not specifically on the list but unless there is more on the tryptic / alternatives front, i dont think any time soon?
[10-03-2021 18:47:30] <monerobull[m]> s/tryptic/tryptich/
[10-03-2021 18:48:02] <ArticMine> The idea for this HF is before tryptic / alternatives
[10-03-2021 18:48:20] <binaryFate> Nov/Dec still ballpark target for me. But I think most important is we keep rolling the dev (and mrl) meetings regularly, then it should become clear enough quickly
[10-03-2021 18:48:32] <rbrunner> Yes, seems to me with BP+ ready, and no binning "adventures" we could be ready pretty soon
[10-03-2021 18:48:55] <jberman> sounds good to me
[10-03-2021 18:49:06] <ArticMine> binning does not need a HF
[10-03-2021 18:49:18] <ArticMine> once ring size is chosen
[10-03-2021 18:49:23] <rbrunner> Ah, yes
[10-03-2021 18:49:31] <monerobull[m]> Would it be possible to aim for something like a saturday? I hated having to watch the eth london fork at work lol
[10-03-2021 18:49:43] <jberman> it would be nice to do in a HF I think, to try and get wallets to conform selection algos at the same time
[10-03-2021 18:49:46] <UkoeHB> one topic not on the agenda (maybe for next time): this big multisig PR is open and I'm hoping to get it in with the next big release https://github.com/monero-project/monero/pull/7877
[10-03-2021 18:51:03] <ArticMine> Time for next meeting?
[10-03-2021 18:51:43] <UkoeHB> Oct 10 or 17 at 1700 UTC?
[10-03-2021 18:51:59] <jberman> In for that
[10-03-2021 18:52:46] <monerobull[m]> 1 or two weeks, what do you guys think
[10-03-2021 18:53:15] <rbrunner> 2 weeks seems fine to me
[10-03-2021 18:53:18] <ArticMine> October 17
[10-03-2021 18:54:28] <monerobull[m]> Sounds good, ill gather feedback for the removal of timelocks till then.
[10-03-2021 18:55:34] <monerobull[m]> Thanks for taking the time everyone, have a nice day. Next meeting in 2 weeks.
[10-03-2021 18:55:48] <ArticMine> Thanks 
[10-03-2021 19:00:44] <utxobr[m]> <UkoeHB> "one topic not on the agenda (..." <- might be worth asking for reviews a couple times during the week here so we get more eyes on it
[10-03-2021 19:01:26] <rottenstonks> 15-17 ring size bump, bp+ and what else? temporary hardfork wen sir?
[10-03-2021 19:04:56] <UkoeHB> utxobr[m]: ok I will bring it up some more :) it is probably difficult to review, especially since very few people know much about multisig
[10-03-2021 19:11:38] <UkoeHB> looks like stoffu did most of the review for the original implementation
[10-03-2021 19:12:34] <ArticMine> <rottenstonks> 15-17 ring size bump, bp+ and what else? temporary hardfork wen sir? Ring size, BP+ and issue 70 / fees are the HF needed changes
```

# Action History
- Created by: carrington1859 | 2021-09-22T19:28:13+00:00
- Closed at: 2021-10-03T21:02:05+00:00
