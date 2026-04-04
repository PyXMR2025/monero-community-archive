---
title: 'Research meeting: 6 May 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/459
author: SarangNoether
assignees: []
labels: []
created_at: '2020-04-30T19:43:42+00:00'
updated_at: '2020-05-06T18:42:49+00:00'
type: issue
status: closed
closed_at: '2020-05-06T18:42:49+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 6 May 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-05-06T18:42:49+00:00
    [2020-05-06 13:01:39] <sarang> All righty! Time for the weekly research meeting
    [2020-05-06 13:01:46] <sarang> As always, we begin with GREETINGS
    [2020-05-06 13:01:52] <ArticMine> Hi
    [2020-05-06 13:02:17] → atoc joined (2fb9d2fc@47.185.210.252)
    [2020-05-06 13:02:44] <UkoeHB_> hi
    [2020-05-06 13:02:47] <atoc> hi
    [2020-05-06 13:05:12] <sarang> Let's move on to ROUNDTABLE
    [2020-05-06 13:05:22] <sarang> Any research of interest that folks wish to share?
    [2020-05-06 13:07:53] ⇐ adhux0x0f0x3f quit (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f): Remote host closed the connection
    [2020-05-06 13:08:03] <sarang> I can share a few things, I suppose
    [2020-05-06 13:08:12] <sarang> I worked up a PR to update how keys are encrypted in memory
    [2020-05-06 13:08:32] <sarang> This has follow-on effects to how they're stored on disk, and I'm making some additional updates to improve the existing unit tests and add others
    [2020-05-06 13:09:00] <sarang> and I'm finishing up a test implementation of Arcturus, the extension of Triptych that offers better proof sizes
    [2020-05-06 13:09:20] <sarang> I'd like to determine exactly what the timing differences are, since initial estimates suggested that Arcturus and Triptych would be very close
    [2020-05-06 13:09:40] → adhux0x0f0x3f joined (~adhux0x0f@gateway/tor-sasl/adhux0x0f0x3f)
    [2020-05-06 13:12:02] <kenshamir[m]> Sorry if I've missed this; are there any comparisons for Arcturus, Triptych and CLSAG ?
    [2020-05-06 13:13:59] <sgp_> hello
    [2020-05-06 13:16:40] <sarang> And kenshamir[m]: I have comparisons for CLSAG and Triptych, but this will add actual implementation data for Arcturus when finished
    [2020-05-06 13:17:20] <kenshamir[m]> Oh right, very cool
    [2020-05-06 13:17:36] <sarang> The size data is already known, FWIW
    [2020-05-06 13:17:47] <sarang> But the Arcturus timing was always an estimate based on operation counts
    [2020-05-06 13:18:00] <sarang> It's different enough in how it handles transactions that I'd like to know for sure
    [2020-05-06 13:18:04] <kenshamir[m]> concretely?
    [2020-05-06 13:18:33] <kenshamir[m]> Is there a link for it?
    [2020-05-06 13:19:29] <sarang> The size/timing data?
    [2020-05-06 13:19:40] <kenshamir[m]> Yeah, the size data
    [2020-05-06 13:19:48] <sarang> Yeah, let me pull it up
    [2020-05-06 13:20:47] <kenshamir[m]> Probably may not be that helpful for Monero, but there is a new paper out on an endomorphism that allows you to compute aG + bH faster in variable time
    [2020-05-06 13:21:00] <sarang> Page 11: https://eprint.iacr.org/2020/312.pdf
    [2020-05-06 13:21:02] <kenshamir[m]> Link : https://eprint.iacr.org/2020/454.pdf
    [2020-05-06 13:21:19] <kenshamir[m]> Thank you
    [2020-05-06 13:22:30] ⇐ kico quit (~kico@gateway/tor-sasl/kico): Remote host closed the connection
    [2020-05-06 13:22:40] <sarang> Anyway, that's what I wanted to share
    [2020-05-06 13:22:45] <sarang> Does anyone else have research of interest?
    [2020-05-06 13:25:00] <UkoeHB_> what's the gist of your encryption update?
    [2020-05-06 13:28:26] <sarang> The in-memory encryption of keys was being done with a chacha stream that was XORed with keys, instead of just encrypting the keys with chacha directly
    [2020-05-06 13:28:38] <sarang> This PR makes this change
    [2020-05-06 13:29:59] <sarang> The existing unit tests for wallet and key encryption also get some updates
    [2020-05-06 13:30:28] <UkoeHB_> ah interesting
    [2020-05-06 13:31:30] <sarang> It also transitions old encrypted keys to the new format, which needs better testing that I'm still working on
    [2020-05-06 13:32:09] ⇐ TheoStorm quit (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl): Quit: Leaving
    [2020-05-06 13:33:46] <sarang> Seems pretty quiet today!
    [2020-05-06 13:33:57] <sarang> We could always end early if there isn't more that needs to be discussed...
    [2020-05-06 13:34:41] <sgp_> I have nothing to add except to remind people that I still want coinbase outputs to be avoided entirely in non-coinbase-spend rings :p
    [2020-05-06 13:36:01] <sarang> You mean the idea that a ring containing a coinbase output must have all coinbase outputs, right?
    [2020-05-06 13:37:53] <sarang> sgp_: can you briefly recap your rationale, to ensure everyone is on the same page?
    [2020-05-06 13:38:03] <sgp_> yes that idea
    [2020-05-06 13:38:16] <sgp_> rationale is that no normal users spend coinbase outputs
    [2020-05-06 13:38:32] <sgp_> even people who mine on mining pools never spend coinbase outputs
    [2020-05-06 13:38:59] <sgp_> so the selection of these is markedly different from expected user spend behavior
    [2020-05-06 13:39:37] <sarang> When I thought about this earlier, I was concerned that it sort of kicks the can down the road one hop on the graph
    [2020-05-06 13:39:43] <sgp_> separating these will increase the effective ringsize for most (>99%) users by 10-20%
    [2020-05-06 13:40:08] <sgp_> sarang: it kicks the can down the road, but it's still MUCH better
    [2020-05-06 13:40:25] <ArticMine> Interesting
    [2020-05-06 13:40:26] <sarang> And that if a heuristic was "this coinbase probably isn't the true signer" previously, it would become "this output that came from a coinbase ring probably isn't the true signer" as a somewhat weaker heuristic
    [2020-05-06 13:40:37] <sarang> Yeah, I think it's better but doesn't totally eliminate it
    [2020-05-06 13:41:33] <sarang> If it were implemented, there would need to be a decision on what selection distribution to use, which should probably be based on a transparent-chain analysis at minimum
    [2020-05-06 13:41:42] <sgp_> it's still essentially one set of transactions separated (one ring signature? I'm struggling to explain this simply and also accurately)
    [2020-05-06 13:41:45] <sarang> to see if it matches the overall distribution
    [2020-05-06 13:42:12] <ArticMine> The idea is that an ouput from a mining pool is far more likely to e spent by a normal user
    [2020-05-06 13:42:37] <sgp_> basically the real spend of the after-coinbase output would look the same as several transactions that select this output as the decoys
    [2020-05-06 13:42:51] <sarang> Yeah
    [2020-05-06 13:43:01] <sarang> Does my statement about the analysis for a distribution make sense?
    [2020-05-06 13:43:06] <ArticMine> I agree it mitigates but does not completely eliminate the risk
    [2020-05-06 13:43:16] <sgp_> but now this accounts for the behavior that the user could just be a miner on a mining pool, for example
    [2020-05-06 13:43:28] <sgp_> which is hugely broader
    [2020-05-06 13:43:34] <sarang> But it is true that right now, the spend patterns of coinbase vs non-coinbase are assumed to be the same by the selection algorithm
    [2020-05-06 13:44:14] <sarang> It'll be very interesting to see that distribution for coinbase-only
    [2020-05-06 13:44:25] <sgp_> only solo miners can spend coinbase outputs. Miners on mining pools can also spend from-coinbase outputs
    [2020-05-06 13:44:41] <sarang> right
    [2020-05-06 13:45:09] <sgp_> so while it kicks the can down the road, in terms of practical behavior, it's a night and day improvement
    [2020-05-06 13:45:34] <sarang> I'll ping Isthmus here, since his group has access to this sort of data for other chains
    [2020-05-06 13:46:14] <sgp_> discussion on this idea has been mixed for years. I'd like to see this actually done
    [2020-05-06 13:46:41] <sgp_> 10-20% better effective ringsizes just with smarter selection
    [2020-05-06 13:46:53] → TheoStorm joined (~TheoStorm@host-p8vu8h.cbn1.zeelandnet.nl)
    [2020-05-06 13:47:56] <ArticMine> It is a significant mitigation of the issue. I do not see a clear downside to this.
    [2020-05-06 13:48:37] <sgp_> downside is to people that are running private pools. They effectively need to "churn" once by not directly sending the coinbase outputs to people
    [2020-05-06 13:48:52] <sgp_> I think this is a small tradeoff
    [2020-05-06 13:49:20] <sarang> I think it's an improvement, provided it doesn't introduce unexpected or unintended consequences to the selection distribution, and is based on distribution data from known spends where reasonable (e.g. Bitcoin)
    [2020-05-06 13:49:49] <zkao> hoi, can someone evaluate how sound this ECDSA adaptor signature is? https://joinmarket.me/blog/blog/schnorrless-scriptless-scripts/ if these ECDSA adaptor signature works, it looks like the atomic swap can be done using a scheme similar to the suggested by andytoshi-sarang (equivalent discrete logs), mixed with the game theory from h4sh3d's proposal: all game theory on bitcoin script (forcing players to act or
    [2020-05-06 13:49:49] <sgp_> I agree with that caveat, though I want to add my own caveat that I don't see how it can be worse
    [2020-05-06 13:49:49] <zkao> lose), and no need for monero refund. so it should work on monero today.
    [2020-05-06 13:50:22] <sarang> zkao: I didn't invent that cross-group discrete log idea; it was andytoshi
    [2020-05-06 13:50:39] <zkao> yes, i know, u proposed
    [2020-05-06 13:50:58] <sarang> sgp_: if the coinbase-only selection distribution ends up being very different to the overall distribution, it would introduce a heuristic for coinbase true signers
    [2020-05-06 13:51:26] <sarang> and for all we know, it could be a very different distribution in that miners/pools spend immediately or something
    [2020-05-06 13:51:43] <sgp_> luckily then we can approach coinbase with its own algo
    [2020-05-06 13:51:48] <sgp_> which we can't do now
    [2020-05-06 13:51:59] <sarang> The non-coinbase distribution could be easily modified to simply redraw if it chooses a coinbase
    [2020-05-06 13:52:09] <sgp_> if these are actually very different spend patterns, then the possibility for increased privacy is even greater
    [2020-05-06 13:52:20] <sgp_> since we can handle them separately, not together
    [2020-05-06 13:52:20] <sarang> The coinbase distribution would simply be some fixed selection distribution on block order, that doesn't need to do the shuffling method we do now
    [2020-05-06 13:52:31] <sarang> sgp_: right
    [2020-05-06 13:52:59] <sgp_> my gut suggests coinbase spends are quicker on average
    [2020-05-06 13:53:08] <sgp_> but Bitcoin data would be great for that ofc
    [2020-05-06 13:53:10] → tromp joined (~tromp@2a02:a210:ca3:2800:41ae:b290:45bb:8746)
    [2020-05-06 13:54:01] <sarang> Right
    [2020-05-06 13:54:33] <sarang> Hopefully someone like Isthmus's group can get that data, since they have easy access to the dataset AFAIK
    [2020-05-06 13:54:40] <sgp_> I still support avoiding coinbase with the stupid method of re-selecting a coinbase is chosen, though improvements can make that better. I see even this stupid model as an incremental improvement
    [2020-05-06 13:54:51] <sgp_> *if a coinbase is chosen
    [2020-05-06 13:56:22] <sgp_> what I'm trying to say is that the data on Bitcoin should help make the selections better, but that they are not prerequisites to switch since it can't be worse than it already is in my eyes
    [2020-05-06 13:57:40] <sarang> If there were no known distribution from Bitcoin etc., what selection for coinbase-only would you suggest?
    [2020-05-06 13:58:34] <sarang> Reselect-on-coinbase seems reasonably for non-coinbase rings, but there still would need to be a chosen selection distribution for coinbase-only rings
    [2020-05-06 13:58:46] <sgp_> same as current probably? I agree that's not ideal
    [2020-05-06 13:59:21] <sarang> Well, the current one takes block density into account, and that's not relevant for coinbase-only
    [2020-05-06 13:59:32] <sgp_> keeping in mind most public pools publish this data openly anyway
    [2020-05-06 14:00:10] <sgp_> so frankly the coinbase rings would be susceptible to a lot of public data causing a high proportion of heuristically dead outputs
    [2020-05-06 14:00:53] <sgp_> in the worst of cases I say ~90% of of the hashrate accounted for by public pools sharing coinbase data, so ringsize 11 doesn't really help with that in the best of cases
    [2020-05-06 14:01:02] <sgp_> *I saw ~90%
    [2020-05-06 14:01:29] <sarang> Well, at that point you could _almost_ suggest removing the requirement for nontrivial rings in coinbase-only at all
    [2020-05-06 14:01:35] <sarang> *altogether
    [2020-05-06 14:01:57] <sarang> If the thought is that analysis could reveal true signers in a huge number of cases anyway
    [2020-05-06 14:02:23] <sgp_> there's a push for pools to not share this data, but I agree that in the current case, coinbase rings should be considered to offer near-zero protection
    [2020-05-06 14:02:59] <sgp_> really any coinbase spend. in the current situation, they are still heuristically dead, just spread across normal users' transactions
    [2020-05-06 14:03:33] <sarang> Hmm, we're a bit over time
    [2020-05-06 14:03:39] <sgp_> yeah we can end
    [2020-05-06 14:03:41] <sarang> Let's move to ACTION ITEMS and then continue discussion
    [2020-05-06 14:04:12] <sarang> I have some unit tests update to make for the key encryption PR, and hopefully can get Arcturus code working in C++ with the timing data that I want
    [2020-05-06 14:06:09] <sarang> Any other updates, action items, etc. before we adjourn?
    [2020-05-06 14:06:30] <sarang> If not, adjourned!
    [2020-05-06 14:06:33] <sarang> Logs will be posted shortly


# Action History
- Created by: SarangNoether | 2020-04-30T19:43:42+00:00
- Closed at: 2020-05-06T18:42:49+00:00
