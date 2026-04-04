---
title: Monero Research Lab Meeting - 20 January 2021 @ 17 UTC
source_url: https://github.com/monero-project/meta/issues/544
author: SamsungGalaxyPlayer
assignees: []
labels: []
created_at: '2021-01-19T19:32:14+00:00'
updated_at: '2021-01-20T20:31:51+00:00'
type: issue
status: closed
closed_at: '2021-01-20T20:31:51+00:00'
---

# Original Description
Time: 17 UTC

Location: #monero-research-lab

Main discussion topics:

* Bulletproofs+ audit(s) (updates only; no action/decision necessary at meeting)
* Triptych (continued discussion)
     * How to handle multisig wallet "conversions" that will be required to spend Triptych funds received in a legacy multisig wallet?
* v15 ringsize


# Discussion History
## SamsungGalaxyPlayer | 2021-01-20T20:31:44+00:00
```
[2021-01-20 11:00:10] <sgp_> MRL meeting time
[2021-01-20 11:00:13] <sgp_> https://github.com/monero-project/meta/issues/544
[2021-01-20 11:00:19] <sgp_> 1. Greetings
[2021-01-20 11:00:24] <ArticMine> Hi
[2021-01-20 11:00:56] <TheCharlatan> Hey
[2021-01-20 11:01:25] <sgp_> ping knaccc sarang dEBRUYNE Isthmus moneromooo 
[2021-01-20 11:01:44] <sgp_> some people may show up after Biden's speech (happening now)
[2021-01-20 11:02:11] <zkao> hello
[2021-01-20 11:02:16] → jonathancross joined (jonf3nmatr@gateway/shell/matrix.org/x-wzuktjwejrheichc)
[2021-01-20 11:02:21] <sgp_> before then, I will give a brief BP+ update
[2021-01-20 11:02:41] <sgp_> sarang gave me some emails to contact asking for SoWs, and I will email them today
[2021-01-20 11:02:49] <lederstrumpf> hi
[2021-01-20 11:03:06] <sgp_> the other BP+ audit was moved, funded, and started since last meeting so that's quick
[2021-01-20 11:03:30] <sgp_> any questions on BP+ audits before we move on?
[2021-01-20 11:04:01] <ArticMine> Any idea on timeline
[2021-01-20 11:06:23] <sgp_> "about 1 month"
[2021-01-20 11:06:39] <ArticMine> Thanks
[2021-01-20 11:07:29] <sgp_> okay, let's actually skip to v15 ringsize if sarang isn't here to discuss triptych
[2021-01-20 11:07:38] <ArticMine> Yes I agree
[2021-01-20 11:07:43] <sgp_> https://github.com/monero-project/research-lab/issues/79
[2021-01-20 11:07:54] <sgp_> there are a few different opinions on this one
[2021-01-20 11:08:26] <sgp_> I personally think a bump from 11->15 is most appropriate
[2021-01-20 11:08:41] <sgp_> ArticMine: you suggest a higher number ~19-25 still, right?
[2021-01-20 11:08:45] — dEBRUYNE here
[2021-01-20 11:08:50] <ArticMine> Yes 21
[2021-01-20 11:09:23] <sgp_> I took a look at the CPU benchmark numbers you shared
[2021-01-20 11:09:48] <sgp_> the increase you noted was for the high-end hardware that's often out of stock at the moment, from what I can tell
[2021-01-20 11:10:20] <sgp_> looking at benchmark per dollar, my best estimate is 25% increase
[2021-01-20 11:10:32] <dEBRUYNE> Wouldn't 21 raise the verification time significantly? Presuming we merely implement Bulletproofs+
[2021-01-20 11:11:26] <sgp_> I don't have specific numbers for 21
[2021-01-20 11:11:26] → Benny84Hickle joined (~Benny84Hi@static.57.1.216.95.clients.your-server.de)
[2021-01-20 11:11:30] <sgp_> but yes
[2021-01-20 11:11:38] <ArticMine> I saw your response. I find the high end as the best indicator. Basically "value" is more often than not junk going back to the pc jr in the 1980's.
[2021-01-20 11:13:04] <ArticMine> One is better off with slightly older high end from a cost vs return perspective than the newest "value"
[2021-01-20 11:13:05] <sgp_> 15 would increase verification (of the signature and balance, NOT the entire transaction) by 35%
[2021-01-20 11:13:30] <ArticMine> It is a 2x increase for the signature verification
[2021-01-20 11:13:31] <sgp_> 17 would increase 54$
[2021-01-20 11:13:41] <sgp_> *54%
[2021-01-20 11:13:45] <ArticMine> for 22
[2021-01-20 11:14:39] <ArticMine> but also it bring the size close to where Triptych would come in
[2021-01-20 11:15:22] <ArticMine> One thing to keep in mind is that one we go into the dynamic blocksize we have to be very careful how we increase the tx size
[2021-01-20 11:15:52] <ArticMine> It can be done, but it can require modification of the long term median right after the fork
[2021-01-20 11:16:18] <dEBRUYNE> I'd prefer to impement a ring size bump with Triptych
[2021-01-20 11:16:23] <dEBRUYNE> implement*
[2021-01-20 11:16:41] <sgp_> I think going for a 100% increase in verification is optimistic
[2021-01-20 11:17:01] <sgp_> I fear it's too aggressive
[2021-01-20 11:17:09] ⇐ Benny84Hickle quit (~Benny84Hi@static.57.1.216.95.clients.your-server.de): Ping timeout: 272 seconds
[2021-01-20 11:17:12] <sgp_> especially since it doesn't specifically address any threat model
[2021-01-20 11:17:26] <ArticMine> I am figuring an on triptych coming in with a ring size of ~64 at least
[2021-01-20 11:17:53] <sgp_> yeah, 64 or 128 (I'll probably push for the latter thinking ahead)
[2021-01-20 11:18:08] <ArticMine> So a more gradual increase does make sense
[2021-01-20 11:18:29] <sgp_> well, there are pretty major costs right now for minor benefits
[2021-01-20 11:18:44] <sgp_> knaccc is for 16 I believe for the churning numbers he shared
[2021-01-20 11:18:46] <ArticMine> By the way wownero is running ring 22
[2021-01-20 11:19:16] <ArticMine> Yes that is based upon an arbritary mix set of 1,000,000
[2021-01-20 11:19:29] <ArticMine> after 4 churns
[2021-01-20 11:19:31] <sgp_> yeah I agree it's quite arbitrary
[2021-01-20 11:20:00] <ArticMine> SO there is a gain with each level of increase
[2021-01-20 11:20:47] <sgp_> just to stress again why I am proposing an increase to begin with:
[2021-01-20 11:21:10] <dEBRUYNE> I think at 64 the verification time would remain approximately similar right?
[2021-01-20 11:21:10] <sgp_> 11 is still "safe" in my opinion, but the buffer has narrowed more than I feel comfortable with personally
[2021-01-20 11:21:24] <sgp_> dEBRUYNE: approximately, yes
[2021-01-20 11:21:38] <sgp_> https://user-images.githubusercontent.com/12520755/103604734-97fff000-4ed7-11eb-8bc7-76f0044b4e1a.png
[2021-01-20 11:22:17] <sgp_> sorry that's size not verification time
[2021-01-20 11:22:21] ⇐ hashes4merkle quit (~hashes4me@gateway/tor-sasl/hashes4merkle): Quit: Take Care!
[2021-01-20 11:22:30] <ArticMine> The crossover is well above 15 closer to 21
[2021-01-20 11:23:03] <ArticMine> between CLSAG and Triptych
[2021-01-20 11:23:40] <ArticMine> more if we extrapolate Triptych to 64 or 128
[2021-01-20 11:24:31] <ArticMine> Verification time is linear with anonymity size
[2021-01-20 11:25:00] <sgp_> dEBRUYNE: do you still think keeping it at 11 is best?
[2021-01-20 11:25:22] <ArticMine> It is still linear with triptych
[2021-01-20 11:25:33] <dEBRUYNE> As far as I can see, the probability of Triptych getting implemented is fairly reasonable
[2021-01-20 11:25:37] <sgp_> yeah but is the slope less? iirc the slope is less
[2021-01-20 11:25:41] <dEBRUYNE> So I am wondering if this discussion is somewhat fruitless in the first place
[2021-01-20 11:26:02] <sgp_> well, everyone else isn't confident that triptych will happen very soon
[2021-01-20 11:26:14] <sgp_> signs point to v15 without triptych
[2021-01-20 11:26:28] <dEBRUYNE> No, but I think end of the year is still a reasonable target
[2021-01-20 11:26:44] <dEBRUYNE> And to fork merely for Bulletproofs+ seems kind of wasteful
[2021-01-20 11:26:45] <ArticMine> There are issue with multi sig wallets
[2021-01-20 11:26:47] <sgp_> so in any case we still have a time v15 without triptych to select a ringsize
[2021-01-20 11:27:03] <dEBRUYNE> ArticMine: Yes, but nothing that cannot be overcome as far as I can see
[2021-01-20 11:27:16] <sgp_> it can be overcome but just not hastily
[2021-01-20 11:27:21] <sgp_> it's a huge change
[2021-01-20 11:27:30] <ArticMine> ^ that is my point
[2021-01-20 11:27:35] <dEBRUYNE> Sure, but why the rush to implement Bulletproofs+
[2021-01-20 11:27:38] <ArticMine> It take time
[2021-01-20 11:27:41] <sgp_> BP+ is a quite minor change by comparison
[2021-01-20 11:27:48] <dEBRUYNE> The optimizations are marginal
[2021-01-20 11:27:50] <sgp_> take the efficiency gain today
[2021-01-20 11:28:01] <ArticMine> They do add up
[2021-01-20 11:28:06] <sgp_> taking the gain doesn't delay triptych
[2021-01-20 11:28:07] <dEBRUYNE> We also have to remind ourselves that the ecosystem grew a lot
[2021-01-20 11:28:21] <sgp_> if we were pushing triptych back, I would agree
[2021-01-20 11:28:23] <dEBRUYNE> Not sure if they change the transaction format, but in that case wallets would have to add logic for Bulletproofs+ too
[2021-01-20 11:28:27] <sgp_> but that doesn't appear to be the case
[2021-01-20 11:28:28] <dEBRUYNE> (the ones that use custom code)
[2021-01-20 11:28:48] <dEBRUYNE> Also if we add a HF in say August, we cannot do one for Triptych in say November/December
[2021-01-20 11:29:00] <sgp_> triptych frankly will not happen in 2021
[2021-01-20 11:29:05] <ArticMine> There is also issue 70 in mrl
[2021-01-20 11:29:14] <ArticMine> Tha twill need a hard fork
[2021-01-20 11:29:18] <dEBRUYNE> That seems like a bit of a preliminary inference
[2021-01-20 11:29:24] <sgp_> August is also later than it needs to be for BP+
[2021-01-20 11:29:53] <sgp_> May maybe?
[2021-01-20 11:30:08] <dEBRUYNE> 5-6 months after our previous HF?
[2021-01-20 11:30:12] <dEBRUYNE> Which didn't go particularly smooth either
[2021-01-20 11:30:45] <sgp_> 7 months I guess, could push back more, not technical reason to however
[2021-01-20 11:30:53] <sgp_> *no technical
[2021-01-20 11:31:11] <dEBRUYNE> Apart from the fact that it puts a strain on the ecosystem
[2021-01-20 11:31:17] <dEBRUYNE> It's what was discussed in the blog
[2021-01-20 11:31:26] <dEBRUYNE> https://www.getmonero.org/2020/09/01/note-scheduled-upgrades.html
[2021-01-20 11:31:45] <sgp_> I simply do not see triptych as being implemented as optimistically as you
[2021-01-20 11:32:58] <dEBRUYNE> Perhaps sarang or moneromooo can weigh in, but I think having 9 months is definitely doable
[2021-01-20 11:34:02] <sgp_> well, moo said they don't want to touch that code, so we would need someone like sarang to start running with it
[2021-01-20 11:34:14] <sgp_> then we would need to notify everyone of the upcoming change
[2021-01-20 11:34:27] <sgp_> then we would need to make super clear resources for users of multisig wallets
[2021-01-20 11:34:36] <selsta> BP+ will require changes to HW wallets, right?
[2021-01-20 11:34:38] <sgp_> and give them time to coordinate and "convert"
[2021-01-20 11:35:40] <dEBRUYNE> As far as I know they don't necessarily need to convert existing funds
[2021-01-20 11:35:45] <dEBRUYNE> Merely generate a new wallet for Triptych funds
[2021-01-20 11:36:24] <sgp_> we discussed a major issue last week, where they need to "convert" to a non-multisig wallet to spend triptych funds
[2021-01-20 11:36:39] <sgp_> that conversion period will take a lot of education
[2021-01-20 11:37:29] <sgp_> point is, unless we have someone ready to run with the idea, we're kinda hoping for something that isn't even penciled in currently
[2021-01-20 11:37:36] <sgp_> we can work on getting everything outlined
[2021-01-20 11:37:45] <sgp_> but we don't currently have anyone working on this
[2021-01-20 11:37:53] <sgp_> nor has sarang said "I will do this if I get the $$$"
[2021-01-20 11:38:06] <ArticMine> BP+ does not need any of the conversions that Triptych will need
[2021-01-20 11:38:41] <ArticMine> So I way we need to proceed with BP+
[2021-01-20 11:38:43] <dEBRUYNE> I suppose we can assess the viability again in a few months, but it also seems to be a bit preliminary to say that we can fork BP+ in summer
[2021-01-20 11:38:59] <sgp_> well, at that point we lose the efficiency gain anyway haha
[2021-01-20 11:39:40] <dEBRUYNE> Not sure I am following
[2021-01-20 11:39:47] <dEBRUYNE> The gain starts counting from the moment it is implemented
[2021-01-20 11:40:08] <sgp_> I don't want BP+ to be something we delay and hope that triptych will come together in a few months
[2021-01-20 11:40:21] <sgp_> if we want to commit to triptych, it will take significant active effort
[2021-01-20 11:40:34] <sgp_> else we're delaying bp+ for no reason
[2021-01-20 11:40:44] <sgp_> *no significant reason
[2021-01-20 11:41:35] <dEBRUYNE> I meant that in 1-2 months we probably have a fairer assessment of the viability of Triptych in 2021 (end of)
[2021-01-20 11:42:25] <sgp_> okay, so what are the specific next steps we need to take to figure that out
[2021-01-20 11:42:34] <ArticMine> ... but even with say Triptych at the end of 2021 it still makes sens to go ahead with BP+
[2021-01-20 11:42:42] <ArticMine> sense
[2021-01-20 11:43:01] <sgp_> ArticMine: if it actually is 2021, I'm less for BP+ right now
[2021-01-20 11:43:30] <ArticMine> It depends when in 2021
[2021-01-20 11:43:31] <sgp_> to dE's point, a 5% gain isn't worth an upgrade headache for that time period, at least imo
[2021-01-20 11:43:31] <u29601mg6ba93j[m> I think a definite gain soon (BP+ and ring size increase) is a great hedge against the real possibility that triptych will  take longer than we hope to implement. We can argue about which CPUs to benchmark but ArticMine is right that they have advanced a lot over the past 2 years. That should be accounted for when looking at verification times. The tx size increases are not large enough to be problematic
[2021-01-20 11:43:31] <u29601mg6ba93j[m> for the ring sizes we are discussing
[2021-01-20 11:44:01] <sgp_> that being said, if we feel the ringsize needs to be increased before EOY, then our hands are tied and we should do one earlier
[2021-01-20 11:44:53] <sgp_> quick vote
[2021-01-20 11:44:58] <ArticMine> I see as there are enough incremental inprovements to make it worthwhile overall
[2021-01-20 11:45:23] <sgp_> Do you believe it's critical to increase the ringsize before the end of the year? Y/N
[2021-01-20 11:45:30] <ArticMine> Y
[2021-01-20 11:45:34] <u29601mg6ba93j[m> Y
[2021-01-20 11:45:39] <sgp_> N
[2021-01-20 11:46:00] <moneromooo> triptych will depend on whether sarang or someone with a similar level of clue either adds it to monero, or adds a *production quality* python implementation that I can convert to C++.
[2021-01-20 11:47:46] <sgp_> ArticMine u29601mg6ba93j[m: why do you feel that an "immediate" (very soon timeline) ringsize increase is necessary?
[2021-01-20 11:48:17] <ArticMine> I am also concerned about the regulatory issues
[2021-01-20 11:48:40] <sgp_> is that the main reason or a side reason?
[2021-01-20 11:49:29] <ArticMine> It is a major reason. There is also the multiple attack vectors mining, CTRs, etc
[2021-01-20 11:49:45] <ArticMine> They can have a cumulative effect
[2021-01-20 11:49:46] <sgp_> I personally don't see a regulatory difference 11 vs (eg) 25
[2021-01-20 11:50:14] <sethsimmons> <sgp_ "Do you believe it's critical to "> Y
[2021-01-20 11:50:27] <sethsimmons> Sorry I'm late 🙂
[2021-01-20 11:50:33] <gingeropolous> Y for me as well
[2021-01-20 11:50:51] <sgp_> sethsimmons gingeropolous why do you feel it's essential to increase the ringsize Q2?
[2021-01-20 11:50:57] <u29601mg6ba93j[m> Mostly because we are all guessing about how soon Triptych can be implemented. Moneromooo just mentioned one key dependency (availability of Sarang) that we cannot be certain of yet. We cant go back in time. Skipping BP+ and ring size increases now, will become a regret if Triptych gets delayed for 1 year or more
[2021-01-20 11:51:27] → kowalabearhugs joined (b94187ad@185.65.135.173)
[2021-01-20 11:51:43] → Febo joined (59d411cd@89-212-17-205.static.t-2.net)
[2021-01-20 11:51:44] <u29601mg6ba93j[m>  * @sgp_  Mostly because we are all guessing about how soon Triptych can be implemented. Moneromooo just mentioned one key dependency (availability of Sarang) that we cannot be certain of yet. We cant go back in time. Skipping BP+ and ring size increases now, will become a regret if Triptych gets delayed for 1 year or more
[2021-01-20 11:52:14] <sethsimmons> <sgp_ "sethsimmons gingeropolous why do"> EOY is still a long ways off and there will surely be new threats to the network by then. As you’ve said, I feel that 11 is OK for the moment most likely, but I definitely would like to see a bump before EOY
[2021-01-20 11:52:44] <sgp_> is there a date everyone has in mind for "11 really needs to go by then"
[2021-01-20 11:53:02] <ArticMine> ASAP
[2021-01-20 11:53:52] <gingeropolous> 1. triptych implementation timeline unknowns. 2. using every opportunity available to strengthen the network within reasonable technical limitations. This goes to my viewpoint that we have enjoyed seemless protocol upgrades and their is no sign of ossification, but ...
[2021-01-20 11:55:42] <sethsimmons> Takes a good bit of time to plan and deploy a HF across the ecosystem, so ASAP for me as well.
[2021-01-20 11:56:09] <sgp_> last chance to respond on this q, then I'll ask another
[2021-01-20 11:56:17] <binaryFate> lurking, I support ASAP for >11 too
[2021-01-20 11:56:29] <UkoeHB__> I do not think multisig wallets would need to convert to non-multisig to spend Triptych funds, unless Triptych-friendly multisig isn't implemented (it's a non-trivial task)
[2021-01-20 11:57:40] <sgp_> UkoeHB__: can you read sarang's statements form last meeting and clarify? https://github.com/monero-project/meta/issues/542
[2021-01-20 11:58:06] <sgp_> second q time
[2021-01-20 11:58:24] <Lyza> dunno how relevant this would be considered, but there's been a lot of patches recently to address ongoing attacks and a consensus change would make them effectively mandatory which could be a plus
[2021-01-20 11:58:30] <sgp_> if the decision is to increase ringsize ASAP, how early can we have v15
[2021-01-20 11:58:35] ⇐ Febo quit (59d411cd@89-212-17-205.static.t-2.net): Quit: Ping timeout (120 seconds)
[2021-01-20 11:59:07] <sethsimmons> As soon as BP+ is audited and all issues are corrected. Maybe mid-late April?
[2021-01-20 11:59:08] <selsta> earliest July IMO
[2021-01-20 11:59:13] <sethsimmons> That may be too soon though.
[2021-01-20 12:00:28] <dEBRUYNE> As a general comment, I don't like this push for a hard fork 'ASAP'
[2021-01-20 12:00:54] <dEBRUYNE> We informally decided to slow them down due to the strain on the ecosystem and now I see a few people here pushing again for one within 5-6 months of the previous one
[2021-01-20 12:00:59] <sgp_> is anyone for a sprint? thinking like April. Just trying to feel this out
[2021-01-20 12:01:08] <dEBRUYNE> Hard pass from me
[2021-01-20 12:01:09] <sethsimmons> ASAP as in "as soon as we can reasonably deploy one across the ecosystem".
[2021-01-20 12:01:32] <ArticMine> Yes of course
[2021-01-20 12:01:49] <UkoeHB__> sgp_: afaict he said two things A) Triptych multisig is non-trivial and may not work on hardware devices, B) he thought maybe it reveals a private key to all participants but appeared to walk that back here https://monerologs.net/monero-research-lab/20210115
[2021-01-20 12:02:23] <ArticMine> My take ~9 months since the last HF
[2021-01-20 12:02:37] <selsta> that would be July / August
[2021-01-20 12:02:50] <ArticMine> Yes that makes sense to me
[2021-01-20 12:02:55] <knaccc> btw I don't have a strong opinion yet on ring sizes, because I'm not sure what the stats will look like on verificaiton times for a year's worth of blockchain
[2021-01-20 12:02:57] <sethsimmons> I'd get behind July/August.
[2021-01-20 12:02:58] <sgp_> I agree that if we are waiting until that time, we have a few weeks to put together a triptych plan
[2021-01-20 12:03:12] <sethsimmons> Don't want to make things too painful for ecosystem participants.
[2021-01-20 12:03:38] <gingeropolous> so July / august would put us at April 2022 for triptych if we're gong for ~9 months in between
[2021-01-20 12:03:46] <sgp_> If we can get triptych in Dec 2021 actually, then I personally think that's better than BP+ in July/August
[2021-01-20 12:03:48] <dEBRUYNE> Does BP+ change the transaction format by the way?
[2021-01-20 12:04:00] <dEBRUYNE> UkoeHB__ ^
[2021-01-20 12:04:14] <sethsimmons> <sgp_ "If we can get triptych in Dec 20"> If that's possible I could get behind that. But that seems highly optimistic.
[2021-01-20 12:04:18] → supus joined (~supus@2001:171b:2278:ca70:7d6a:d1d0:effa:ffb3)
[2021-01-20 12:04:34] <sgp_> the main reason to do v15 quickly is if the current ringsize is determined to be unsafe (think like an emergency)
[2021-01-20 12:04:35] <selsta> dEBRUYNE: yes, afaik Trezor will have to update their firmware and Ledger update their app
[2021-01-20 12:04:37] <UkoeHB__> not sure dEBRUYNE
[2021-01-20 12:04:46] <selsta> at least I think so
[2021-01-20 12:05:13] <sgp_> if we're thinking an increase many months away, that doesn't seem to me like people think it's an emergency
[2021-01-20 12:05:17] <gingeropolous> but BP+ also works for triptych right?
[2021-01-20 12:05:26] <sgp_> gingeropolous: yes
[2021-01-20 12:05:30] → Febo joined (59d411cd@89-212-17-205.static.t-2.net)
[2021-01-20 12:06:02] <u29601mg6ba93j[m> <selsta "that would be July / August"> 9 months seems like a good compromise. I would prefer faster but balance that preference to what dEBRUYNE said about challenges for ecosystem  and our goal to decrease fork frequency
[2021-01-20 12:06:19] <sethsimmons> <sgp_ "if we're thinking an increase ma"> Its not an "emergency", no.
[2021-01-20 12:06:38] <sethsimmons> Necessity if Triptych is not possible this year, yes IMO.
[2021-01-20 12:06:52] <sethsimmons> But doesn't require wrecking the ecosystem to get it quickly.
[2021-01-20 12:07:13] <Lyza> echoing knaccc 's concern.
[2021-01-20 12:07:14] <Lyza> it keeps being said that the given verification time increases are not for the entire transaction, but those are exactly the numbers that seem most relevant to the verification time discussion
[2021-01-20 12:07:29] <dEBRUYNE> <sgp_> the main reason to do v15 quickly is if the current ringsize is determined to be unsafe (think like an emergency) <= Is it?
[2021-01-20 12:07:30] <TheCharlatan> Since bulletproofs+ does not only change proof verification, but also proof creation, it will require a wallet side update.
[2021-01-20 12:07:33] <dEBRUYNE> I am skeptical of that statement to be honest
[2021-01-20 12:07:47] <sgp_> if I can summarize things a bit just so we don't talk in circles
[2021-01-20 12:08:01] <dEBRUYNE> TheCharlatan: Thanks. That means MyMonero etc. need to upgrade too, which will be a hassle
[2021-01-20 12:08:07] <sgp_> we are a few months away from the soonest anyone wants to have a network upgrade
[2021-01-20 12:08:08] <dEBRUYNE> Especially if they have to upgrade a few months later again for Triptych
[2021-01-20 12:08:28] <sgp_> that gives us a small amount of time (not a huge amount!) to feel out a triptych action plan
[2021-01-20 12:08:47] <sgp_> if within a month we don't have a triptych plan, seems like most people are for BP+ and a ringsize bump in July
[2021-01-20 12:09:00] <sgp_> since people don't want to drag their feet forever
[2021-01-20 12:09:33] <sgp_> if however triptych is actually doable by EOY, I see strong arguments for pushing v15 to Dec to not delay Triptych by 6+ months
[2021-01-20 12:09:48] <Lyza> agree
[2021-01-20 12:09:53] <sgp_> is the above in contrast to anyone's thinking?
[2021-01-20 12:09:56] <gingeropolous> that logic seems sound to me as well
[2021-01-20 12:10:04] <sethsimmons> No, agreed here.
[2021-01-20 12:10:31] <UkoeHB__> it's reasonable
[2021-01-20 12:10:36] <sethsimmons> Is initiating HF planning in late Feb/early march sufficient time for forking in July?
[2021-01-20 12:11:11] <sgp_> imo yes, we need 3 months on the planning side for a relatively "small" upgrade like BP+
[2021-01-20 12:11:25] <ArticMine> That is reasonable. Aim for July / August and if Triptych is viable by December then delay to include Triptych
[2021-01-20 12:11:36] <gingeropolous> i would put forth that if triptych is not seen doable by EOY, we consider a ringsize bump without BP+. This would put the least strain on the ecosystem (no 3rd party upgrades etc) but still get everyone on the same software, which re: p2p attacks, is good
[2021-01-20 12:11:40] <sethsimmons> OK, good with me then.
[2021-01-20 12:12:14] <sgp_> okay, I will make a visual showing the rough timeline options then
[2021-01-20 12:12:14] <sethsimmons> <gingeropolous "i would put forth that if tripty"> That's a good alternative but I'd prefer to make the fork "worth it" with some important upgrade like BP+
[2021-01-20 12:12:35] <sethsimmons> It causes ecosystem strain either way simply HFing, although without BP+ would be lessened.
[2021-01-20 12:12:39] <gingeropolous> but BP+ is gonna cause 3rd parties to have to fiddle, and then they're gonna have to fiddle again with triptych
[2021-01-20 12:12:47] <ArticMine> There is also MRL 70 fee stabilization
[2021-01-20 12:12:59] <gingeropolous> i guess good info would be how ready are 3rd party things to fiddle
[2021-01-20 12:13:08] <sethsimmons> <gingeropolous "but BP+ is gonna cause 3rd parti"> How significant is this fiddling?
[2021-01-20 12:13:10] <sgp_> any immediately pressing matters to address at this meeting?
[2021-01-20 12:13:15] <gingeropolous> ledger, trezor, mymonero
[2021-01-20 12:13:27] <selsta> all mobile wallets too
[2021-01-20 12:13:28] <sethsimmons> They all have to update for HF anyways.
[2021-01-20 12:13:41] <u29601mg6ba93j[m> <ArticMine "There is also MRL 70 fee stabili"> Do you feel that should be done by July fork or can it wait for Triptych?
[2021-01-20 12:13:41] <TheCharlatan> gingeropolous I don't think that is true r.e. no 3rd party upgrades if only the ring size is bumped. The wallets still need to update to create larger transactions.
[2021-01-20 12:13:43] <sgp_> to reiterate, my personal action items are: 1) contact for second BP+ audit, 2) make visual of timeline options
[2021-01-20 12:14:01] <ArticMine> It should be done by the July fork
[2021-01-20 12:14:31] <u29601mg6ba93j[m> > <@freenode_ArticMine:matrix.org> There is also MRL 70 fee stabilization
[2021-01-20 12:14:31] <u29601mg6ba93j[m>  * Do you feel that should be done by July fork (if applicable) or can it wait for Triptych (perhaps not until 2022)?
[2021-01-20 12:14:36] <TheCharlatan> I don't think bulletproofs+ will bring much more fiddling once it is reviewed and in a stable state.
[2021-01-20 12:14:43] <gingeropolous> ok
[2021-01-20 12:14:44] <ArticMine> because we could go into the adaptive blocksize and then the recent attack could have bite
[2021-01-20 12:15:17] <TheCharlatan> The only thing that significantly changes for the hardware wallets will be some message sizes. The bulletproofs are anyway already done by the monero wallet, not the device firmware.
[2021-01-20 12:15:30] <u29601mg6ba93j[m> <ArticMine "because we could go into the ada"> That is a great point, especially if adoption increases significantly this year
[2021-01-20 12:15:42] <selsta> TheCharlatan: so less work than CLSAG?
[2021-01-20 12:15:45] <selsta> that would be good
[2021-01-20 12:16:01] <TheCharlatan> Yes, definitely less work than CLSAG.
[2021-01-20 12:16:05] <ArticMine> basically if we are into the adaptive blocksize an attack for a matter of hours can trigger a fee increase that can take months or even years to correct
[2021-01-20 12:17:00] <ArticMine> There is a real incentive here for an attack similar to what happen recently
[2021-01-20 12:17:27] <ArticMine> but it only works if we are in the adaptive blocksize not in the penalty free zone
[2021-01-20 12:17:32] <UkoeHB__> ArticMine: have you published your latest recommendations yet?
[2021-01-20 12:17:58] <ArticMine> I have them finalized not published yet
[2021-01-20 12:18:18] <UkoeHB__> cool I look forward to it
[2021-01-20 12:18:18] <ArticMine> I expect within a week
[2021-01-20 12:19:07] <u29601mg6ba93j[m> Since it is coming within a week. Can we have another vote next week(same as before except adding MRL70 to the July Bp+ and ringsize increase fork)?
[2021-01-20 12:19:22] <ArticMine> We can meet in a week
[2021-01-20 12:19:28] <ArticMine> same time
[2021-01-20 12:19:38] <dEBRUYNE> Sounds good
[2021-01-20 12:19:49] <sethsimmons> Thanks all!
[2021-01-20 12:24:06] <ArticMine> Thanks
[2021-01-20 12:24:17] <gingeropolous> Thanks everyone!
[2021-01-20 12:24:21] <sgp_> thanks!
```

# Action History
- Created by: SamsungGalaxyPlayer | 2021-01-19T19:32:14+00:00
- Closed at: 2021-01-20T20:31:51+00:00
