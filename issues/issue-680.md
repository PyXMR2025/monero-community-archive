---
title: 'Monero Dev Meeting: v15 network upgrade - Sat 2 April 2022 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/680
author: rbrunner7
assignees: []
labels: []
created_at: '2022-03-26T06:51:17+00:00'
updated_at: '2022-04-11T05:41:34+00:00'
type: issue
status: closed
closed_at: '2022-04-11T05:41:34+00:00'
---

# Original Description
Dev meeting dedicated to the v15 network upgrade that was orginally scheduled for March. It finally might be possible to set the fork date now. [Previous meeting](https://github.com/monero-project/meta/issues/655), [Hardfork planning issue](https://github.com/monero-project/meta/issues/630)

**Location**

#monero-dev: IRC/Libera and Matrix

**Time and date**

Saturday 2 April 2022 17:00 UTC. [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220402T170000&p1=1440).

Expected duration: ~1h.

A detailed list of the PRs that have to go into this upgrade because they are relevant for consensus and additional PRs that should or could be added will follow tomorrow.

# Discussion History
## rbrunner7 | 2022-03-27T12:48:17+00:00
Here the promised PR list:

First, the essentials, relevant for consensus or probably highly desirable to go into service:

| | PR | Issue | Last Change | Author | (Review) / Approved / Merged |
| --- | --- | --- | --- | --- | --- | 
| A | [Fee changes from ArticMine #7819](https://github.com/monero-project/monero/pull/7819) | [MRL #70](https://github.com/monero-project/research-lab/issues/70) | 2022-02-16 | @moneromooo-monero | @j-berman, @UkoeHB |
| B | [Bulletproof+ by sarang, tied to consensus #7170](https://github.com/monero-project/monero/pull/7170) | [Info](https://www.getmonero.org/2020/12/24/Bulletproofs+-in-Monero.html) | 2022-01-29 | @moneromooo-monero | (@vtnerd) |
| C | [Bump ring size to 16 for v15 #8178](https://github.com/monero-project/monero/pull/8178) | [MRL #79](https://github.com/monero-project/research-lab/issues/79) | 2022-02-13 | @j-berman | @tobtoht, @rbrunner7 |
| D | [Add view tags to outputs to reduce wallet scanning time #8061](https://github.com/monero-project/monero/pull/8061) | [MRL #73](https://github.com/monero-project/research-lab/issues/73) | 2022-02-21 | @j-berman | @moneromooo-monero, @rbrunner7, @UkoeHB |
| E | [multisig: key exchange update and refactor #7877](https://github.com/monero-project/monero/pull/7877) | - | 2022-22-02 | @UkoeHB | Merged |
| F | [Multisig: signature fixes #8149](https://github.com/monero-project/monero/pull/8149) | - | 2022-03-04 | @UkoeHB, originally @perfect-daemon | @UkoeHB on #8114, @vtnerd |

<br/>

Second, a list of PRs that looked like good and worthy candidates for one reason or another to me (@rbrunner7) when I went over everything that waits. (Certainly subjective in part, and maybe incomplete, please do comment and help to refine.)

| | PR | Issue | Last Change | Author | (Review) / Approved / Merged |
| ---- | --- | --- | --- | --- | --- | 
| G | [multisig: add post-kex verification round #8220](https://github.com/monero-project/monero/pull/8220) | - | 2022-03-25 | @UkoeHB | (@moneromooo-monero) @rbrunner7 |
| H | [multisig: add key exchange round booster #8203](https://github.com/monero-project/monero/pull/8203) | [Info](https://github.com/haveno-dex/haveno/issues/86) | 2022-03-04 | @UkoeHB | - |
| I | [wallet2: decrease the amount of data exchanged for output export #8179](https://github.com/monero-project/monero/pull/8179) | [Log](https://github.com/monero-project/meta/issues/665) | 2022-03-22 | @moneromooo-monero | @j-berman |
| J | [Daemon RPC: add a new method to get height from a timestamp #8088](https://github.com/monero-project/monero/pull/8088) | - | 2021-09-28 | @tevador | (@hyc), (@Agorist-Action) |
| K | [wallet2, RPC: Optimize RPC calls for periodic refresh from 3 down to 1 call #8076](https://github.com/monero-project/monero/pull/8076) | [#7571](https://github.com/monero-project/monero/issues/7571) | 2022-03-18 | @rbrunner7 | (@j-berman) |
| L | [RPC server: thread safety (+ small fix to on_getblockhash) #7937](https://github.com/monero-project/monero/pull/7937) | [v0.17 review](https://github.com/monero-project/monero/pull/7936) | 2022-01-09 | @j-berman | @tobtoht, @rbrunner7 (v0.17) |
| M | [connection: fix implementation #7760](https://github.com/monero-project/monero/pull/7760) | [Log](https://github.com/monero-project/meta/issues/655) | 2021-06-28 | @perfect-daemon | (@vtnerd) |
| N | [EPEE Cleanup Reorganized #8211](https://github.com/monero-project/monero/pull/8211) | - | 2022-03-26 | @jeffro256 | @tobtoht, @mj-xmr |
| O | [p2p: drop-in replacement for serialization #7999](https://github.com/monero-project/monero/pull/7999) | - | 2021-10-11 | @perfect-daemon | - |
| P | [Daemon: Store blockchain in '~/.local/share/bitmonero' by default #8202](https://github.com/monero-project/monero/pull/8202) | [GUI #3727](https://github.com/monero-project/monero-gui/issues/3727) | 2022-03-04 | @mj-xmr | - |


## rbrunner7 | 2022-03-27T12:51:19+00:00
Above list leaves out many smaller and uncontroversal PRs that will just get merged "naturally" with no special need to look at them and push them. I concentrated on important and big ones.

## mj-xmr | 2022-03-27T12:54:42+00:00
@rbrunner7 the issue for "P" is: https://github.com/monero-project/monero-gui/issues/3727

Thank you for such a comprehensive list.

## rbrunner7 | 2022-03-29T05:46:44+00:00
FYI: [RINOwallet](https://rino.io) pledged a bounty of the XMR equivalent of USD 10,000 towards the general fund if multisig does get properly fixed by this hardfork. Announcement on Reddit is [here](https://old.reddit.com/r/Monero/comments/tqj5r6/lets_fix_multisig_rino_offering_10000_completion/). Luckily, looking at the state of the 3 relevant PRs as I see them, that seems altogether doable :)

## erciccione | 2022-03-29T09:45:42+00:00
> looking at the state of the 3 relevant PRs as I see them, that seems altogether doable :)

2 of those 3 PRs have an Haveno bounty on them (https://github.com/haveno-dex/haveno/issues/103 and https://github.com/haveno-dex/haveno/issues/86) for a total of $5000. Maybe would be more effective to allocate part of RINO's bounty directly to reviewers instead? @binaryFate 

## binaryFate | 2022-03-29T12:03:00+00:00
> > looking at the state of the 3 relevant PRs as I see them, that seems altogether doable :)
> 
> 2 of those 3 PRs have an Haveno bounty on them ([haveno-dex/haveno#103](https://github.com/haveno-dex/haveno/issues/103) and [haveno-dex/haveno#86](https://github.com/haveno-dex/haveno/issues/86)) for a total of $5000. Maybe would be more effective to allocate part of RINO's bounty directly to reviewers instead? @binaryFate

1. RINO has [indicated](https://www.reddit.com/r/Monero/comments/tqj5r6/comment/i2hn1ya) that they would support developers' CCS as they can, though it's not explicitly conditional on those reviews

1. If the community organizes discussions and agrees to redirect those 10k$ from the General Fund to specific individuals once the bounty is paid, the core team would be happy to execute

## erciccione | 2022-04-03T06:25:05+00:00
Logs:

```
17:01:37 <ErCiccione> Hello folks! This meeting, like the last one, will be focused on the next network upgrade (hard fork)
17:01:42 <ErCiccione> Logs of the past meeting: https://github.com/monero-project/meta/issues/655#issuecomment-1024960649
17:01:48 <ErCiccione> Meeting agenda: https://github.com/monero-project/meta/issues/680
17:01:54 <ErCiccione> Quick round of greetings to see who is here:
17:01:58 <ErCiccione> Hello everyone!
17:02:05 <UkoeHB> hi
17:02:06 <binaryFate> hi
17:02:12 <ArticMine> hi
17:02:12 <rbrunner> Hello
17:02:16 <jberman[m]> :waves:
17:02:18 <WinslowEric[m]> Greetings!
17:02:40 <mj-xmr[m]> Present
17:02:40 <selsta> hi
17:02:41 <sech1> hi
17:03:38 <ErCiccione> Ok, thanks for being here. I would say we can explore the status of the PRs that need to be merged and the PRs that would be good to have. After we have an idea of the situation, we can decide if makes sense to set a date.
17:03:45 <ErCiccione> rbrunner made an excellet summary of the situation the we can use as a guide: https://github.com/monero-project/meta/issues/680#issuecomment-1079924577
17:04:09 <ErCiccione> I would also like to dedicate a bit of time to discuss the status of multisig in relation to the hard fork, because in-progress projects like Haveno and RINO need multisig to be robust, before being able to launch.
17:04:37 <ErCiccione> The situation in general looks good, most PRs have already been reviewed or are ready to be merged. So, that's a good start
17:04:55 <moneromooo> Oh wow, BP+ still not merged. I did that ages ago now...
17:05:17 <UkoeHB> 8149 needs to rebase onto 8061
17:05:19 <sech1> view tags not merged as well
17:05:39 <rbrunner> Maybe a gentle ping for vtnerd, as they are involved in so many important reviews ...
17:06:20 <ErCiccione> Ok, let's start with the first one i would say, fee changes
17:06:29 <ErCiccione> that mostly only needs to be merged as far as i can tell
17:06:45 <jberman[m]> fee changes looked good to me
17:07:02 <rbrunner> Including the compromise from the last meeting, right?
17:07:15 <jberman[m]> yep
17:07:21 * moneromooo gets itchy at the mention of compromise
17:07:28 <UkoeHB> I think it can be merged
17:08:24 <ErCiccione> Good. next one is bulletproof+. What's missing?
17:08:33 <selsta> I can type that up.
17:08:34 <moneromooo> Nothing AFAIK.
17:08:58 <ErCiccione> A final approval i would say
17:08:59 <UkoeHB> it doesn't have any approvals
17:09:02 <rbrunner> The final signing off of the the review?
17:09:02 <UkoeHB> 0
17:09:16 <selsta> We have BP+ audited, so in general it should be good to merge. vtnerd reviewed it a while ago but he never approved it.
17:09:48 <selsta> I asked him for an approval but he kinda started a new review from scratch, and now he is currently unavailable and it's unclear when he will have time again.
17:10:13 <UkoeHB> maybe jberman[m] and I can do brief reviews (check hard fork mechanics, glance over crypto use)
17:10:40 <jberman[m]> can do that
17:11:08 <rbrunner> The testing on Testnet should also have some value, even if something escaped review
17:11:13 <ErCiccione> nice. Thanks. We should get word from vtnerd to make sure if we should expect a review from him or not
17:11:56 <binaryFate> he's currently unavalaible and I'm not sure how quickly we can expect that word
17:12:54 <ErCiccione> alright. Next PR is to bump ringsize to 16 https://github.com/monero-project/monero/pull/8178
17:13:21 <rbrunner> Pretty simple code, uncontroversial from that point of view
17:13:27 <ErCiccione> this one shouldn't require any further discussion and only need to be merged
17:13:35 <jberman[m]> noticed a couple small merge conflicts with tests, will resolve those asap
17:13:58 <selsta> It looks approved, maybe moneromooo wants to look quickly over it too because I think you are the most experienced with such ring size bump PRs.
17:14:16 <moneromooo> Sure.
17:14:36 <jberman[m]> jberman[m]: (sorry thought this was for view tags)
17:14:45 <jberman[m]> ty moo
17:15:33 <ErCiccione> Anything else on #8178? Otherwise we can move to the next one
17:15:45 <selsta> i'd say move on
17:16:22 <ErCiccione> Allright. View tags: https://github.com/monero-project/monero/pull/8061
17:16:35 <jberman[m]> noticed a couple small merge conflicts with tests, will resolve those asap :)
17:16:42 <sech1> I not only reviewed view tags, but also implemented it in p2pool and tested it on a private testnet. All went smooth - p2pool could mine, monero-wallet-cli could see payouts.
17:16:48 <sech1> so #8061 looks good to me
17:17:16 <rbrunner> Also testet it. Works.
17:17:21 <selsta> #8061 looks ready
17:17:22 <jberman[m]> noice
17:17:45 <rbrunner> Your chance for eternal fame
17:18:00 <ErCiccione> Nice. Seems like was reviewed and tested quite extensively. I would say only final approvals are needed after jberman's fixes and then can be merged?
17:18:27 <selsta> The order in which we should merge things is also something we have to discuss later.
17:18:47 <selsta> Largest changes first and then the smaller ones I assume.
17:19:28 <rbrunner> Merging will probably limit itself with generating conflicts
17:20:33 <jberman[m]> It will have some conflicts with multisig stuff and bp+
17:21:16 <rbrunner> And RPC versions numbers are another source of conflicts
17:21:55 <sech1> RPC version is easy to resolve since we're doing a hardfork. Just use some new higher number
17:21:57 <moneromooo> Seemed like a good idea at the time...
17:22:20 <jberman[m]> One thing we also mentioned briefly in the last MRL meeting was what the "grace period" should be where tx's with view tags and without are allowed, to allow the pool to clear (ring size bump and bp+ also have this grace period). We settled on 1 day same as in the past from what I remember, so just re-affirming that
17:23:27 <selsta> IIRC we always had 1 day
17:23:49 <jberman[m]> cool
17:24:10 <selsta> #7877 is merged so #8149 next to discuss?
17:24:12 <ErCiccione> alright. We can go back to this if needed. The next PR in the list is the fixes for multisig: https://github.com/monero-project/monero/pull/8149
17:25:09 <UkoeHB> I need to rebase that when BP+ and view tags are in
17:25:28 <rbrunner> Is the original author of that PR, perfect-daemon, still, well, missing? And does that matter in any way?
17:25:35 <selsta> it kinda was reviewed by UkoeHB and vtnerd, not only vtnerd
17:25:38 <ErCiccione> I want to stress the importance of having multisig fixed as soon as possible, so would be good to also have two more PRs merged for the hf: https://github.com/monero-project/monero/pull/8220 and https://github.com/monero-project/monero/pull/8220
17:26:14 <rbrunner> That's two times 8220? :)
17:26:26 <UkoeHB> 8203 is the other one
17:27:02 <ErCiccione> lol sorry: the other one is https://github.com/monero-project/monero/pull/8203, yes
17:27:12 <UkoeHB> I need a third pr to add force updating. So 8220 -> new PR -> 8203 to get everything in
17:27:17 <rbrunner> Yeah, but 8203 is still very much at the beginning, as far as I can see. And does it harmonize with the added control round?
17:27:36 <UkoeHB> no, I will need to rebase
17:28:06 <rbrunner> But not much change in logic or even crypto? I am a bit sceptical about that, time-wise, to be honest
17:28:41 <rbrunner> Does Haveno intend to take advantage of the improvements that this would bring?
17:29:07 <UkoeHB> not too much change, at least compared to the original PR
17:29:42 <ErCiccione> rbrunner: Haveno sponsored a good portion of the changes 🙂
17:29:59 <ErCiccione> So, at the ends looks like multisig is the PR that needs the most attention
17:31:19 <ErCiccione> Oh, reminder that RINO set a bounty as well of $10000 for merging all three PRs, so that should be a good incentive for the community
17:31:49 <binaryFate> Do we lack reviews maybe because the vulnerabilities are not really public? I know some background info has been passed to few people only
17:31:59 <rbrunner> It's 4 multisig PRs, no?
17:32:08 <selsta> binaryFate: it's all public in the patch
17:32:18 <ErCiccione> rbrunner: 1 is already merged
17:32:27 <UkoeHB> we lack people actually able and willing to review
17:32:37 <binaryFate> selsta: yes but I mean some context maybe making reviewing easier
17:32:42 <binaryFate> good if not a blocker
17:33:11 <rbrunner> I think if we aim to take 8203 in, 8220 should get merged as soon as possible, to make that "interim" PR possible
17:34:14 <ErCiccione> yeah, we should probably reach to the community asking for reviewers if finding them for those changes is an issue
17:35:13 <jberman[m]> I can review general patterns and such, but don't think I'm able to do a comprehensive crypto review to spot vulnerabilities yet (I've been studying, but not there yet)
17:35:25 <selsta> I mean if we need more security then an audit would help, but I'm not sure if we will find another review for it in the community.
17:35:48 <mj-xmr[m]> Same here as jberman[m] . Even less crypto knowledge sadly.
17:35:51 <rbrunner> Certainly not with vtnerd unavailable ..
17:36:05 <selsta> rbrunner: I mean vtnerd reviewed it, unless we are talking about a different patch now
17:36:16 <ErCiccione> could/can luigi1111 give it a shot?
17:36:45 <rbrunner> I was thinking about 8220, which has no comprehensive review, but only me testing it and moneromoo looking at the code, but not the crypto, if I understood correctly
17:37:21 <UkoeHB> 8220 doesn't have any crypto changes, just key exchange protocol changes
17:37:23 <selsta> oh ok, I was still mentally at 8149
17:37:54 <rbrunner> Yeah, that might be a problem if we think we need a second review
17:38:27 <rbrunner> I would be confident enough to merge 8220 ...
17:38:35 <ErCiccione> Ok. Then we need to find somebody able to review that PR, if you know somebody, maybe ping them on the pr to catch their attention
17:38:43 <selsta> 8203 is the one without any review currently
17:39:13 <UkoeHB> is h4sh3d around? maybe he could take a look at 8220
17:39:43 <h4sh3d> Hi!
17:40:05 <UkoeHB> 8203 is on hold anyway until I can rebase onto 8220 + 1
17:40:47 <UkoeHB> hi h4sh3d :) feeling up for more multisig review?
17:40:57 <UkoeHB> this guy: https://github.com/monero-project/monero/pull/8220
17:41:31 <rbrunner> Should not hurt too much, and the code runs :)
17:41:55 <h4sh3d> Yeah sure! Time wise it will not be possible for me in the next 2-3 weeks (family getting bigger ;p) but after that for sure! If that’s not too late for you guys?
17:42:28 <UkoeHB> would it be possible to postpone multisig stuff to a post-fork point release?
17:42:42 <rbrunner> Well, looks like timewise, it's on the critical path
17:43:29 <binaryFate> While it doesn't need to be part of a HF, I'm worried that many people using Monero but not following closely may not have seen the multisig issue announcement. So having the fix in the HF is ensuring everyone will at least use updated version after that
17:43:34 <rbrunner> That would be my proposal for 8203, frankly. I think postponing all would be unfortunate
17:44:02 <rbrunner> And the rest is really so close ...
17:44:11 <ErCiccione> I would really prefer to not postpone it. That could create huge problems for Haveno. Like having to hold off launch
17:44:48 <binaryFate> Multisig wallets would usually be used for large amounts, I'm concerned some big entity out there will get hit by the vulnerabilities unless we force them to update basically (via fix being in HF)
17:45:09 <UkoeHB> I just mean release it separate from the hf, not delay review/merging (which is happening at a snails pace anyway).
17:45:30 <binaryFate> Yes but then you lose this force-to-update effect of the HF
17:45:34 <rbrunner> Isn't that a contradiction?
17:46:30 <UkoeHB> well it's up to you guys, not much I can do to speed things up on my end
17:46:50 <rbrunner> Maybe if we ask nicely moneromooo can look a bit deeper into 8220 and approve, and we merely move 8203 into a point release
17:46:53 <ArticMine> Why not release multi sig with another HF?
17:47:30 <WinslowEric[m]> Haveno would be delayed for that
17:47:43 <onions> Two HFs? Back to back? Seems like a lot of headache...
17:48:24 <r4v3r23[m]> WinslowEric[m]: fine by me. this is a monero update, not a haveno one
17:48:42 <ArticMine> What is the timeline fro multi sig review etc?
17:49:04 <binaryFate> ArticMine: IMO too extreme to abuse the HF concept just for this desirable side effect on multisig wallet code
17:49:08 <ErCiccione> We need to find reviewers, that's the problem. Pushing to another hf seems eccessive
17:50:03 <ArticMine> Fair enough but there are problems with a partial implementation of multi sig without a HF
17:50:19 <selsta> BP+ is not approved yet, then we also have to do changes to Ledger and Trezor for BP+ (which supposedly isn't much work but someone has to look into it), that will also take time. It's not like all other stuff is 100% ready and we are only waiting on multisig.
17:50:27 <selsta> We will also need time to test everything on testnet.
17:50:38 <binaryFate> what HF timeline are we talking about?
17:50:53 <ArticMine> For multi sig
17:52:15 <rbrunner> Is the loose consensus now that we must have a second review for that heavyweight multisig PR 8149?
17:52:49 <selsta> 8149 had two reviews, I doubt we will get more without an audit.
17:52:55 <UkoeHB> we will need some kind of review when I rebase
17:52:56 <rbrunner> Because if not, 8220 is peanuts in comparison, and IMHO 8203 nice to have, but not critical. Haveno may disagree.
17:53:38 <rbrunner> Ah, yes, UkoeHB reviewed the original one.
17:53:42 <binaryFate> maybe we can make a clear announcement of what exactly needs more reviews, so that external entities out there can decide to step in to finance/organize an audit?
17:53:49 <ErCiccione> 8203 is not urgent for us iirc
17:54:27 <rbrunner> So where's the problem? :)
17:54:53 <ErCiccione> Ok so, we have 5 minutes left so to wrap it up:
17:55:08 <ErCiccione> we need somebody to approve BP+, which has been already extensively reviewed
17:55:11 <ArticMine> Do we have a timeline for the HF?
17:55:12 <UkoeHB> what about getting 8149 into the HF, then 8220 + 1 + 8203 into a point release (if necessary)?
17:55:43 <sech1> we're not discussing HF date in this meeting?
17:55:47 <UkoeHB> ErCiccione: jberman[m] and I will look at the BP+ PR (probably within 1-2 weeks)
17:56:10 <jberman[m]> UkoeHB: +1
17:56:14 <ErCiccione> sech1: if we feel like we already for it sure, but we don't have much time left
17:56:34 <UkoeHB> usually dev meetings extend past the hour, I don't mind staying
17:56:41 <ArticMine> I am ok
17:56:58 <ErCiccione> shouldn't take long anyway
17:57:00 <rbrunner> A date would be nice, even as an attempt ...
17:57:06 <selsta> The problem with timeline / setting a date is difficult when some things are unclear with how long they will take. I'd like to have BP+ merged first and then someone who can look into Ledger / Trezor changes.
17:57:38 <selsta> Last time we set a date there were a lot of things unreviewed and then the date came it it became pointless because we can't just merge things unreviewed.
17:57:46 <sech1> 2 months should be enough for everything probably
17:57:51 <sech1> we have a nice date approaching https://p2pool.io/tail.html
17:58:13 <binaryFate> :)
17:58:32 <r4v3r23[m]> as a community member, holding back on a major monero upgrade that brings BP+ and higher ring sizes for the sake of an external project doesn't look like the way to go, especially if the PRs mentioned arent critical to multisig. projects should build around monero's progress, not the other way around
17:58:41 <ErCiccione> personally i find myself in the middle. I would like to set a date, because pushes people to wrap things up, but i also don't want to get to a point where we postpone it again
17:58:54 <UkoeHB> mining software might need to double check that they won't get uint64 overflow when the total supply exceeds uint64::max; iirc moneromooo fixed Monero's implementation a couple years ago
17:58:56 <selsta> So maybe someone can do an extra overview issue on multisig, with the current status of each PR and what is remaining. rbrunner something like your comment
17:59:16 <rbrunner> Who are the candidates for Ledger and Trezor changes?
17:59:26 <selsta> well usually the companies do it themselves
17:59:45 <selsta> but last time I needed a small change from Ledger they took over a month, so I feel like we will have to do the changes ourselves.
17:59:48 <ErCiccione> selsta: That would be useful
18:00:24 <UkoeHB> selsta: I guess I can write that
18:00:25 <selsta> also Trezor only updates their firmware every couple months, that was an issue the last hardfork
18:00:54 <rbrunner> Does all not sound too happy then
18:01:04 <selsta> it always works out somehow :P
18:01:36 <sech1> "uint64 overflow when the total supply exceeds uint64::max" <- this is still a few years away. Tail emission starts before 2^64
18:01:38 <ErCiccione> alright, then i would say setting a date it's premature, but we could set a date for another meeting?
18:01:54 <ErCiccione> 1 or two weeks away?
18:01:59 <UkoeHB> selsta: ah
18:02:02 <UkoeHB> sech1: ah
18:02:26 <ArticMine> Give it two weeks and look at setting the HF date then?
18:02:38 <UkoeHB> how about 2 weeks, monerotopia is this week
18:02:45 <ErCiccione> sounds good to me
18:02:55 <rbrunner> Yeah, with 2 weeks there might be a chance to have BP+ fully reviewed until then
18:03:14 <ErCiccione> yeah and we will ahve the status of multisig more clear
18:03:16 <ErCiccione> ok then
18:03:16 <ArticMine> or at least have a good idea on the timeline
18:03:37 <ErCiccione> thanks everybody for joining. Have a good rest of the day and see you in a couple of weeks
```

# Action History
- Created by: rbrunner7 | 2022-03-26T06:51:17+00:00
- Closed at: 2022-04-11T05:41:34+00:00
