---
title: 'Monero Dev Meeting: v15 network upgrade - Sat 29 January 2022 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/655
author: erciccione
assignees: []
labels: []
created_at: '2022-01-27T15:52:26+00:00'
updated_at: '2022-01-30T08:32:27+00:00'
type: issue
status: closed
closed_at: '2022-01-30T08:32:27+00:00'
---

# Original Description
Dev meeting dedicated to the v15 network upgrade that was scheduled for March.

#### Location

#monero-dev: [IRC/Libera](irc://irc.libera.chat/#monero-dev) and [Matrix](https://matrix.to/#/!VDQXWJoFsesLtbGdTT:monero.social)

#### Time and date

Saturday 29 January 2022 17:00 UTC. [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220129T170000&p1=1440).

Expected duration: ~1h.

#### Topics in discussion

1. Greetings
2. Confirm and officialise ringsize 16
3. Status of changes that should go in the next hard fork:

- Status of view tags PR (https://github.com/monero-project/monero/pull/8061)
- Stauts of fee changes PR (https://github.com/monero-project/monero/pull/7819)
- Status of bulletproofs+ PR (https://github.com/monero-project/monero/pull/7170)

4. Reassess schedule for rollout (the original plan: https://github.com/monero-project/meta/issues/630)
5. Discuss potential Features to be added for next hard fork:

- https://github.com/monero-project/research-lab/issues/88
- https://github.com/monero-project/monero/pull/7877
- https://github.com/monero-project/monero/pull/7760
- https://github.com/monero-project/monero/pull/6410

6. ?

Please let me know if you want to add/edit meeting items.

Chat log will be posted below after meeting has concluded.

Logs of the last dev meeting: https://github.com/monero-project/meta/issues/633

#### Moderator

ErCiccione

# Discussion History
## SamsungGalaxyPlayer | 2022-01-27T15:55:32+00:00
I additionally would like a decision to be made on https://github.com/monero-project/monero/pull/6410, so that we know if we need to design the Thorchain implementation around a custom `tx_extra` field or a standard encrypted memo.

## erciccione | 2022-01-27T16:01:29+00:00
@SamsungGalaxyPlayer I intentionally only added the items that require an hard fork, to focus the discussion since we are already late. I also haven't added any of the other changes suggested as "potential features" in https://github.com/monero-project/meta/issues/630. We can add all the "potential features" in a single meeting point at the end, so we are sure the HF related stuff is discussed first?

## SamsungGalaxyPlayer | 2022-01-27T16:02:58+00:00
I don't care personally about the format, but it would help substantially if a decision about 6410 could be made, since this implementation is currently ongoing.

## rottenwheel | 2022-01-27T16:04:54+00:00
Thanks for closing the [original issue](https://github.com/monero-project/meta/issues/652), created more than a week ago, posted widely through [Monero Observer](https://www.monero.observer/monero-development-workgroup-meeting-29-january-2022/), [Monero Moon](https://medium.com/themoneromoon/the-monero-moon-issue-28-307de4b1db15) and [Revuo Monero](https://localmonero.co/revuo/weekly/104).

Date in issue description is wrong. Fix it.

> Time and date
> 
> Saturday 22 January 2022 17:00 UTC. Check in your timezone.

Saturday 29 January 2022 17:00 UTC. [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20220129T170000&p1=1440).

## hyc | 2022-01-27T16:14:03+00:00
> I additionally would like a decision to be made on [monero-project/monero#6410](https://github.com/monero-project/monero/pull/6410), so that we know if we need to design the Thorchain implementation around a custom `tx_extra` field or a standard encrypted memo.

IMO If thorchain needs more info it should be managed on their side of things. You can embed the monero txid, signed by the monero sender key, in a thorchain memo field and go from there.


## escapethe3RA | 2022-01-28T00:36:47+00:00
> Thanks for closing the [original issue](https://github.com/monero-project/meta/issues/652), created more than a week ago, posted widely through [Monero Observer](https://www.monero.observer/monero-development-workgroup-meeting-29-january-2022/), [Monero Moon](https://medium.com/themoneromoon/the-monero-moon-issue-28-307de4b1db15) and [Revuo Monero](https://localmonero.co/revuo/weekly/104).

Updated MO report.

## carrington1859 | 2022-01-29T18:13:23+00:00
```
17:00:35 <ErCiccione> It's meeting time!
17:00:39 <ErCiccione> Hello folks! This is an important meeting focused on the next network upgrade (hard fork). Code freeze supposed to be on January 15th, but the changes needed haven't been merged yet. During this meeting we'll explore the status of these PRs, so that after we can decided new dates.
17:00:54 <ErCiccione> After that, we will take a look at other features/changes waiting to be merged that would be cool to have in the next network upgrade, but that do not strictly require a hard fork. The full agenda is here: https://github.com/monero-project/meta/issues/655
17:01:01 <ErCiccione> for reference, the logs of the last meeting are here : https://github.com/monero-project/meta/issues/633
17:01:16 <ErCiccione> See also this excellent overview of the v15 hard fork: https://github.com/monero-project/meta/issues/630
17:01:20 <ErCiccione> So let's start with a round of greetings to see who is here today.
17:01:24 <ErCiccione> Hey everyone, thanks for joining.
17:01:31 <ArticMine> Hi
17:01:32 <vtnerd_> Hello
17:01:34 <rbrunner> Hello
17:01:44 <jberman[m]> :waves:
17:01:54 <xmrscott[m]> Hello
17:02:34 <Rucknium[m]1> Hi
17:03:53 <moneromooo> hi
17:04:16 <ErCiccione> Ok, let's proceed to the second point of the agenda:
17:04:25 <carrington[m]> Howdy
17:04:30 <UkoeHB> hi
17:04:37 <ErCiccione> 2. Ringsize 16. There were still some doubts during the last dev meeting. Do we want to confirm 16 as the next ringsize or more discussion is needed?
17:04:52 <ArticMine> I say confirm
17:05:20 <Scalability> +1
17:05:35 <rbrunner> +1
17:05:56 <rbrunner> Such a nice number :)
17:06:15 <selsta> we also have to talk about multisig which currently isn't in the agenda as far as I can see
17:06:29 <UkoeHB> ok with me, would have comparable verification costs to a likely seraphis implementation
17:06:40 <xmrscott[m]> +1
17:06:54 <rbrunner> selsta: It's in 5.
17:07:18 <rbrunner> But sure a candidate for 3.
17:07:48 <selsta> IMO it should be something we want to release before the hardfork
17:07:48 <ErCiccione> yeah multisig doesn't require a hard fork, so we can discuss it later. Very important topic indeed
17:08:01 <Rucknium[m]1> I support increase of ring size to 16.
17:08:12 <selsta> but yes lets talk about it later
17:08:27 <Scalability> 16 ring size it is then, no?
17:08:44 <ErCiccione> everyone present agrees on 16. That was easy. We can make it official at this point
17:08:48 <ErCiccione> 16 it is
17:09:23 <ErCiccione> now let's talk about the r PRs that require a hard fork that still need to be merged:
17:09:33 <ErCiccione> 3a. view tags (https://github.com/monero-project/monero/pull/8061).
17:09:41 <ErCiccione> The review of the PR seems to be still ongoing. @jberman could you give us an update of where things stand at the moment?
17:10:01 <UkoeHB> We got some feedback about Siphash, from the Siphash author, on the view tag PR: https://github.com/monero-project/monero/pull/8061#issuecomment-1024939341
17:10:49 <UkoeHB> jtgrassie and vtnerd_ were the ones expressing skepticism about it originally
17:12:06 <jberman[m]> Commit coming today in response to rbrunner 's comments related to making sure there is a smooth transition at the fork (users who update wallets before the fork will have their tx's processed without view tags for a grace period, to allow smooth transition, and will include a way to not cause a breaking change on one of the internal structs)
17:12:36 <rbrunner> Eagerly awaiting this!
17:12:37 <jberman[m]> + addressing their other comments
17:13:05 <jberman[m]> there will also be merge conflicts between this PR and bulletproofs+, happy to take care of them
17:13:38 <ErCiccione> Sounds good. Will it only need final reviews + merge after or are there other blockers?
17:13:38 <rbrunner> I have the code of this PR running at my MoneroTech web wallet as "TechNet" as a functional test. Works beautifully.
17:14:18 <jberman[m]> regarding the re-opening of Siphash versus Keccak discussion, whatever is decided there is super simple to change in the code. I already have the code using Siphash written
17:15:30 <moneromooo> Without knowing the background, switching to a custom hash for only 1% or 2% speedup seems odd.
17:15:41 <UkoeHB> To resolve that question, hopefully jtgrassie and/or vtnerd_ can respond to Mr. Aumasson
17:15:55 <rbrunner> Personally I would like to forego that re-opening ...
17:16:02 <jberman[m]> > Will it only need final reviews + merge after or are there other blockers?
17:16:02 <jberman[m]> some downstream ecosystem folks will likely need new code to to handle view tags (wallets will need to use new code to construct/scan for tx's with view tags)
17:16:29 <jberman[m]> - I don't know the extent of what changes will need to be made to accommodate them it will vary by software (not sure how much is re-used from the core repo)
17:16:29 <jberman[m]> - these changes can likely need to be done alongside changes to support bulletproofs+ I would think
17:17:49 <ErCiccione> got it. Usually we give enough time to members of the ecosystem to adapt to the post-hard fork changes, so that shouldn't be an issue.
17:18:05 <rbrunner> So good we publish the software 1 month before hardfork, right?
17:18:16 <selsta> yes
17:18:30 <ErCiccione> if there are no further comments let's proceed to the next PR:
17:18:38 <UkoeHB> View scanning is a central UX bottleneck, so I think it would be unwise to leave any inch on the table, for no compelling reason.
17:19:30 <ErCiccione> 3b. Fee changes from Articmine (https://github.com/monero-project/monero/pull/7819)
17:19:37 <ErCiccione> The PR seems to be mostly ready and reviewed. Only some minor conflicts that need to be fixed. moneromooo could you give us a quick update?
17:19:53 <selsta> UkoeHB suggested a second review
17:19:59 <moneromooo> AFAIK this is ready. Let me go see the last comments...
17:20:30 <rbrunner> "second review" as in "more eyes"?
17:20:31 <moneromooo> Yes, nothing since, so nothing to add.
17:20:38 <UkoeHB> IMO all big PRs need at least 2 reviewers.
17:21:09 <jberman[m]> I can review this
17:21:10 <carrington[m]> Are the growth numbers from Justins comment here accurate? If so, I have grave concerns about chain growth attacks
17:21:10 <carrington[m]> https://github.com/monero-project/research-lab/issues/70#issuecomment-785193630
17:22:01 <carrington[m]> Especially in light of the flood attack last year
17:22:11 <UkoeHB> My estimate is Monero won't be able to realistically exceed Bitcoin volume: https://github.com/monero-project/research-lab/issues/91#issuecomment-1018641072
17:22:20 <jberman[m]> I'll review 7819
17:22:23 <UkoeHB> Might be worth contemplating an upper limit on block size
17:22:28 <ArticMine> No
17:22:34 <UkoeHB> To avoid stability problems around verification costs
17:22:45 <ArticMine> This has caused very serious problems for bitcooin
17:22:46 <ErCiccione> thanks jberman 🙂
17:22:57 <ArticMine> Thanks jberman
17:22:59 <UkoeHB> ArticMine: bitcoin doesn't have a verification bottleneck
17:23:03 <carrington[m]> The combination of allowing 14x growth in block size per year with the very low fees could lead to a disaster
17:23:10 <ArticMine> Verification can be addressed
17:23:15 <UkoeHB> How?
17:23:36 <ArticMine> With the use of graphic processors and multithreding
17:23:52 <UkoeHB> That only kicks the can, it doesn't solve it
17:24:03 <ArticMine> Actually it does
17:24:23 <ArticMine> once we take a hard look ant the numbers
17:24:43 <UkoeHB> your next project...?
17:24:43 <ArticMine> The overall limit is bandwidth by the way
17:25:03 <ArticMine> I have been looking hard at this
17:25:44 <UkoeHB> In any case, answering this question is the same as 'contemplating the need for a block size limit'. Let's not answer it in this meeting.
17:26:46 <UkoeHB> However, does it need to be answered before the fee PR can be merged? carrington[m] 's concerns
17:27:12 <carrington[m]> Limiting verification to GPU owners is a TERRIBLE tradeoff IMO. Dynamic block size is fantastic up to a point, but there are other ways to scale transactions.
17:27:29 <rbrunner> Well, what's allowed *now* as a yearly blocksize growth?
17:27:34 <luigi1111w> hello i'm sorta here
17:27:44 <ArticMine> Most consumer device have intergrated graphics that can be used
17:27:59 <selsta> most servers don't
17:28:02 <selsta> by default
17:28:17 <rbrunner> And drivers can make you crazy.
17:28:47 <ArticMine> No with current tools such as Open CL
17:28:47 <xmrscott[m]> Also agree limiting to GPUs is a bad idea especially given current shortage of them
17:28:50 <UkoeHB> rbrunner: I think the longterm median can rise 5x per year with current growth rate
17:29:08 <carrington[m]> Reminder that last year someone added 700MB to the block chain for $1000 in fees
17:29:35 <ArticMine> Yes but no on a sustained basis this is the reason for the long term median
17:29:48 <ArticMine> The cosst of the kind of span adds up
17:29:53 <ArticMine> spam
17:29:56 <carrington[m]> https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60
17:30:20 <UkoeHB> The short-term can rise up to 50x the long term. So you could have 75MB blocks after one year of maximal growth.
17:30:26 <ArticMine> I mean in that example the LT median dod not even move at all
17:30:47 <ErCiccione> seems like there are some heavy skepticisms about this. Maybe it needs more focused discussion before we include it in a network upgrade?
17:31:08 <selsta> or a separate MRL meeting for this?
17:31:29 <ArticMine> It has been hashed over and over agan
17:31:43 <UkoeHB> The fee PR is necessary, the question is about growth rate.
17:31:49 <carrington[m]> 100%
17:32:15 <ArticMine> The growth rate of the LT median is necessasry over the short term
17:32:26 <ArticMine> 2 - 3 months
17:33:05 <ArticMine> Any dynamic blocksize can be scaled to insane limites given enoght time
17:33:14 <ArticMine> insane limits
17:33:39 <Scalability> think the fee PR has been discussed for months since artic first came up with it. similar to beating a dead horse. beyond deliberating further, why not run a quick poll for yes or no and move forward depending on the outcome? akin to how we reached final consensus re: ring size bump 16.
17:33:46 <Scalability> just sayin.
17:33:48 <ErCiccione> Clearly more discussion is needed, let's have this discussion in a dedicated MRL meeting, let's move on to the next point
17:33:50 <jberman[m]> I agree a cap of 14x/yr seems high, and I agree it would be ideal to target CPU's to allow syncing on any commodity device, raspberry pi or server included. I'm for another MRL meeting to discuss
17:34:20 <ArticMine> commodity devices have graphics
17:34:24 <carrington[m]> As Justin pointed out, hitting a growth ceiling doesn't break the network. It just causes a temporary fee market. We don't have to rely on a fee market to exist like BTC, but avoiding it completely in exchange for huge chain bloat is nonsensical to me.
17:34:45 <ErCiccione> please set a date for a focused discussion on this, we need consensus on such important change and until that's reached, there is no point in discussing it here. Moving on:
17:34:46 <carrington[m]> Sorry, JustinE to be clear
17:34:57 <ArticMine> Actually it can trigger the issue 70
17:35:16 <UkoeHB> There is a point where normal node operators have to shut down, since they can't verify new blocks fast enough. And also a point that happens way earlier than that, where normal node operators can't verify the chain, since it takes too long to catch up. These breakpoints are stability issues for the network, and they have NOT been discussed.
17:35:24 <ArticMine> If we allow the st median boe be above the lt median for an extend pereiod of time
17:35:32 <Rucknium[m]1> Would it be advisable to implement a slightly more complicated blocksize limit function to permit short-term spikes (to accommodate sudden adoption), but not allow huge cumulative growth over long periods?
17:35:47 <ArticMine> That is what the LT median does
17:35:52 <UkoeHB> Ok ErCiccione we will address it in the next MRL meeting.
17:36:13 <ErCiccione> yes please, let's move on
17:36:15 <carrington[m]> This seems like a good problem for that guy who was looking into the difficulty adjustment recently, control theory and all that
17:36:21 <ErCiccione> 3c. Bulletproofs+ (https://github.com/monero-project/monero/pull/7170)
17:36:32 <ErCiccione> Not much action on the PR lately. Are we waiting for more reviews moneromooo?
17:36:35 <moneromooo> Why ? Come on, they're discussing something importand and on topoc.
17:36:45 <moneromooo> At least wait till they're both done.
17:37:12 <selsta> ErCiccione: vtnerd is working on the review
17:37:37 <ErCiccione> moneromooo: we have a lot of point in the agenda and this is a discussion that has been going on for a long time. If we want to use this meeting to discuss this sure, but i think the hard fork is more importna, especially because we are already postponing it 
17:37:57 <UkoeHB> moneromooo: could you amend the PR comment for 7170 with a link to the audit report on BP+?
17:38:55 <moneromooo> Gah, november, ping me if you comment on a PR from me :S
17:39:08 <ErCiccione> there is always time at the end of the meeting to discuss whatever, but at least let's try to organise this HF first
17:39:13 <moneromooo> I dio not have the audit report. No idea where it is.
17:40:13 <UkoeHB> moneromooo: https://suyash67.github.io/homepage/assets/pdfs/bulletproofs_plus_audit_report_v1.1.pdf
17:40:19 <moneromooo> ty
17:41:00 <ErCiccione> ok, so waiting for vtnerds final review and then can be merged i guess
17:41:28 <selsta> yes
17:41:42 <ErCiccione> so, the situation is: 2 of the 3 PRs that require a hard fork are mostly ready to go. The issue is with the fee changes, since there seems to be some disagreements.
17:42:09 <ErCiccione> Do we feel comfortable in already talking about dates or we want the discussion about the fee changes to be completed first?
17:42:18 <carrington[m]> To clarify, the theory AND implementation of BP+ have been audited, yes?
17:42:35 <selsta> yes
17:43:36 <ArticMine> The fee changes are predicated on the LT median scaling
17:43:51 <jberman[m]> I think it makes sense to wait until the fee change discussion is completed so we don't end up putting out more conflicting dates
17:44:03 <Scalability> discussion re: fee changes is to occur wednesday next week. there are three other potential PRs that could be included before hf as per agenda
17:44:12 <ArticMine> So we need to dealt with fee change dicussin before we proceed with the dates
17:44:21 <ArticMine> for the HF
17:44:21 <selsta> it would be good to have bp+ merged soon so that we can contact hardware wallets for integration
17:44:32 <ErCiccione> jberman: my feeling too
17:44:37 <carrington[m]> A dedicated MRL meeting sounds good, I'll be there
17:44:46 <dEBRUYNE> <selsta> it would be good to have bp+ merged soon so that we can contact hardware wallets for integration <= +1
17:44:50 <ErCiccione> let's freeze the hard fork until the fee discussion is completed then
17:45:00 <dEBRUYNE> We need to be aware that third-party wallets may also require code changes
17:45:13 <dEBRUYNE> So they need to be properly informed of the changes (view tags and BP+)
17:45:31 <ErCiccione> yeah we will do the usual code freeze
17:45:34 <ErCiccione> + let everyone know.
17:45:44 <ErCiccione> *plus let everyone know
17:45:52 <jberman[m]> I'm happy to assist any ecosystem participants with needed changes too
17:46:07 <dEBRUYNE> Right, but want to point out that we may have to allot a bit more time
17:46:20 <dEBRUYNE> Or we need some people dedicated to reaching out and assisting (thanks jberman[m] for offering already)
17:46:46 <carrington[m]> To confirm, if wallets haven't implemented viewtags at the hardfork will their slower previous method continue to work?
17:47:01 <UkoeHB> yes
17:47:18 <ErCiccione> dEBRUYNE: I think we are in a good spot, we have more people that could help compared to the past hard fork. ANd things went always fine in past
17:47:27 <selsta> most normal wallets use wallet2 so it should be a non issue for them
17:47:27 <moneromooo> That explains why it's a candidate for a fork so fast. Nice :)
17:47:57 <jberman[m]> UkoeHB: wallet scanning could still work in theory, but parsing/serializing will probably cause issues. Plus, if we require view tags as the PR does, then they won't be able to construct tx's
17:48:11 <UkoeHB> true
17:48:39 <jberman[m]> the PR as is has a grace period, which I think moneromooo you were intended for BP+ as well?
17:48:42 <dEBRUYNE> ErCiccione: True, but still would like it to go as orderly as possible and not cause any users to not be able to properly use their wallets
17:48:55 <jberman[m]> sorry, willl have a grace period
17:49:00 <ErCiccione> dEBRUYNE: of course. 100% agree
17:49:08 <Scalability> any comments re: multisig PR? https://github.com/monero-project/monero/pull/7877 UkoeHB vtnerd_
17:49:22 <moneromooo> I don't remember whether I added a placeholder fork. A double fork is probably best.
17:49:44 <jberman[m]> https://github.com/monero-project/monero/pull/7170/files#diff-f7570aa4359fd6b0d59a74fbd2d314d06e48a4ffb2475f97e2193b968833abffR74-R75
17:50:04 <ErCiccione> yeah double fork is what we did in past no? 1 fork adds the changes the other one enforces them?
17:50:12 <UkoeHB> I believe vtnerd_ needs final approval, and h4sh3d also said he is reviewing the changes I made.
17:50:13 <vtnerd_> Reviewing it, probably a ship it soon
17:50:14 <moneromooo> When needed, yes.
17:50:17 <ErCiccione> Scalability: will talk about that in a bit
17:50:30 <jberman[m]> I have a commit for view tags will submit today that also implements double fork
17:50:48 <Scalability> thanks vtnerd_ UkoeHB.
17:50:54 <jberman[m]> what do we want the spacing in between forks to be?
17:50:59 <dEBRUYNE> ErCiccione: Yes
17:51:00 <moneromooo> Oh, that reminds me there was a bug with txes being checked when added to the pool before a fork, and not checked again at the fork.
17:51:15 <moneromooo> Did that get merged ? I had a patch for this IIRC.
17:51:19 <selsta> yes
17:51:22 <selsta> it got merged
17:51:27 <moneromooo> Thanks
17:51:29 <jberman[m]> that was merged: https://github.com/monero-project/monero/pull/7169
17:51:54 <moneromooo> Your lookup speed is commendable :o
17:52:33 <jberman[m]> hehe, I have these links from discussion with rbrunner in the view tag PR, who pointed out my view tag PR should also implement the double fork thing
17:52:38 <selsta> luigi1111w: regarding the multisig crypto changes https://github.com/monero-project/monero/pull/8149, any news regarding extra review? you added the important label :D
17:52:54 <luigi1111w> that's cuz it's important :D
17:53:06 <luigi1111w> I hear someone is reviewing it, need to figure out their schedule though yet
17:53:34 <rbrunner> Would be really nice to get the whole multisig stuff into the hardfork as well, for organizational reasons: Everybody will have to update.
17:53:41 <luigi1111w> jberman[m] we should already double fork for ring size/bp I think, so it's ok
17:53:53 <luigi1111w> rbrunner agreed, would really like to see all the ms fixes we have included
17:54:18 <ErCiccione> rbrunner: yeah absolutely, we will need them for Haveno too, so the faster is in, the better
17:54:51 <rbrunner> I made a lot of functional tests with them, up to 3/5 multisig, which all worked
17:55:02 <jberman[m]> (the consensus rules I initially included for view tags didn't follow the double fork pattern is what I meant)
17:55:04 <rbrunner> Does not replace reviews, of course, but still
17:55:47 <ErCiccione> ok, there are other PRs that are marked as nice to have for the HF:
17:55:59 <ErCiccione> https://github.com/monero-project/research-lab/issues/88
17:56:10 <ErCiccione> https://github.com/monero-project/monero/pull/7760
17:56:17 <ErCiccione> https://github.com/monero-project/monero/pull/6410
17:56:32 <ErCiccione> meeting time is almost over, so if anyone has anything to say about any of these, please go ahead
17:56:37 <jberman[m]> Re: multisig, In the past I said I'd review, but I don't have the crypto knowledge to spot significant issues. h4sh3d  I think is currently re-reviewing changes and does
17:56:54 <selsta> jberman[m]: can you give an update on binning?
17:56:59 <selsta> I think it's not planned for this HF
17:57:06 <selsta> if I remember correctly
17:57:22 <jberman[m]> The algorithm in the linked issue is in a state where it is review-able. Personally I don't feel I have compelling enough evidence to push it further i.e. it is not a critically necessary update in my opinion, and needing to find agreement on its parameter choices + getting the implementation into the code seems a tall task considering
17:57:44 <selsta> so yes, I would remove it from the HF list
17:58:25 <rbrunner> It's probably much too late to even try to get 7760 in, no?
17:58:31 <selsta> https://github.com/monero-project/monero/pull/7760 fixes so many existing bugs with the daemon it would be really nice to include it but I don't know yet how we will get it reviewed
17:58:54 <selsta> but it's not something that requires a HF
17:59:01 <ErCiccione> It's stuff that can be done regardless of the HF afaik, so it's ok
17:59:58 <moneromooo> Maybe in a .1 right after the release ? That way it can get long term testing by people who update to it, but most merchants etc won't.
18:00:36 <moneromooo> Though I guess it'd interfere with the usual brown bag fixes.
18:00:48 <h4sh3d> Jberman[m]: ukoeHB: I’m on it, I think I can complete the re-review by the end of next week
18:00:55 <rbrunner> So the fork release becomes something like an LTS release :)
18:00:58 <selsta> I have been running it on my nodes for half a year now
18:01:00 <Scalability> awesome, thanks h4sh3d
18:01:02 <jberman[m]> ^that sounds good to me
18:01:02 <selsta> it's stable :D
18:02:04 <ErCiccione> Nice! Anything else hard fork related? Otherwise we can end the meeting, as we are past the hour
18:02:18 <moneromooo> For the fee issue, could the people who see a problem make a sample case (ideally worst case with ArticMine's current patch and worst case they'd be grudgingly OK with), then ArticMine can see whether he'd be happy with a parameter change that'd prevent those cases while still allowing enough growth ?
18:02:39 <Scalability> view tags and bp+ almost ready to be shipped. fee pr to be discussed during mrl meeting next week. binning post-poned for now. it's looking good as far as i can tell...
18:03:09 <Scalability> ErCiccione: i guess it would be wise to decide if we will have a follow up dev meeting next week, or in two weeks, to hopefully pick dates for hf?
18:03:43 <selsta> multisig is also ready, just getting some extra reviews
18:04:01 <ErCiccione> No need for a follow up meeting until the situation of the fee changes is clarified and consensus is reached IMO
18:04:16 <Scalability> that is what the MRL meeting on wednesday is there for...
18:04:28 <Scalability> there will be consensus because that is an hour long meeting run by UkoeHB.
18:04:38 <UkoeHB> We will see
18:04:51 <Scalability> if you want to be conservative, why not schedule the next dev meeting for dates in two weeks instead of one?
18:05:01 <Scalability> either way there has to be another dev meeting. dates are to be decided still
18:05:02 <ErCiccione> this is a discussion that has been ongoing for months, don't assume it will be clarified in one meeting
18:05:11 <ArticMine> <moneromooo> For the fee issue, could the people who see a problem make a sample case (ideally worst case with ArticMine's current patch and worst case they'd be grudgingly OK with), then ArticMine can see whether he'd be happy with a parameter change that'd prevent those cases while still allowing enough growth ? Could this be posted to MRL issue 70 
18:05:28 <ErCiccione> I don't think there are the basis to schedule another HF dedicated meeting at the moment
18:05:32 <Scalability> not assuming. it's been discussed for months. decisions have to be taken.
18:05:39 <Scalability> OK.
18:05:54 <ArticMine> and cross referenced to pull 7819
18:06:02 <carrington[m]> I'll reread all the relevant threads etc. so I can have an informed opinion on Wednesday
18:07:06 <ErCiccione> Ok the meeting is over folks. Thanks a lot for joining, next appointment is at the next MRL meeting, where fee changes will be discussed, but feel free to continue the conversation here now!
```

# Action History
- Created by: erciccione | 2022-01-27T15:52:26+00:00
- Closed at: 2022-01-30T08:32:27+00:00
