---
title: 'Research meeting: 3 June 2020 @ 17:00 UTC'
source_url: https://github.com/monero-project/meta/issues/470
author: SarangNoether
assignees: []
labels: []
created_at: '2020-06-01T16:55:18+00:00'
updated_at: '2020-06-03T18:09:24+00:00'
type: issue
status: closed
closed_at: '2020-06-03T18:09:23+00:00'
---

# Original Description
Join in for the weekly Monero Research Lab meeting.

**When**: Wednesday, 3 June 2020 @ 17:00 UTC
**Where**: #monero-research-lab (freenode/matrix)

**Agenda**
1. Greetings

2. Roundtable

3. Questions

4. Action items

# Discussion History
## SarangNoether | 2020-06-03T18:09:23+00:00
    [2020-06-03 12:59:20] <sarang> OK, let's get started!
    [2020-06-03 12:59:26] <sarang> First, GREETINGS
    [2020-06-03 12:59:28] <sarang> hello
    [2020-06-03 12:59:35] <ArticMine> Hi
    [2020-06-03 13:00:37] <dEBRUYNE> hi
    [2020-06-03 13:01:02] — sarang waits for others to join
    [2020-06-03 13:01:10] <hyc> hey
    [2020-06-03 13:02:02] <Isthmus> Heyo
    [2020-06-03 13:03:02] <sarang> Next up, ROUNDTABLE, where anyone is welcome to share research of general interest
    [2020-06-03 13:03:20] <sarang> I have a few topics of interest
    [2020-06-03 13:03:41] <sarang> The recent preprint from CMU student researchers on transaction tracing has been updated to reflect suggestions and corrections: https://eprint.iacr.org/2020/593
    [2020-06-03 13:04:02] <binaryFate> hello
    [2020-06-03 13:04:15] → MSavoritias joined (~MSavoriti@44-224-rev.isper.sk)
    [2020-06-03 13:04:32] <sarang> The researchers still claim that a small but nonzero number of post-changeover (i.e. the RingCT protocol switch) transactions were traceable, which didn't correspond with other numbers I'd found
    [2020-06-03 13:04:42] <sarang> So I decided to independently run the same analysis and compare
    [2020-06-03 13:04:56] <sarang> I ran updated numbers that account for all transactions up to the beginning of this week
    [2020-06-03 13:05:38] <sarang> If you run a full chain-reaction-type analysis, there are 7303 transactions after the changeover containing at least one deducible input
    [2020-06-03 13:05:39] <sarang> However
    [2020-06-03 13:05:59] <sarang> All of those transactions spend pre-changeover outputs
    [2020-06-03 13:06:35] <sarang> So if you filter out all transactions that aren't CT-in-CT-out, there are still precisely 0 deducible transactions/inputs
    [2020-06-03 13:06:50] <sarang> But wait, there's more!
    [2020-06-03 13:07:10] <sarang> The preprint also tries to determine how effective the guess-newest age heuristic is against modern transactions
    [2020-06-03 13:07:35] <sarang> Unfortunately, it uses those 7303 (or however many were in their block range) deducible post-changeover transactions as ground truth
    [2020-06-03 13:07:48] <sarang> and assumes that holds for all post-changeover transactions
    [2020-06-03 13:08:03] <binaryFate> huh that's pretty dumb
    [2020-06-03 13:08:15] <sarang> I wouldn't say it's dumb; it just failed to account for transaction types
    [2020-06-03 13:08:44] <ArticMine> So the key here is RingCT
    [2020-06-03 13:08:54] <sarang> Because there are "full-CT" transactions post-changeover that are deducible, the entirety of their ground-truth data set is based on spends of old funds, for which the modern selection algorithm does not apply
    [2020-06-03 13:09:10] <sarang> But there is an interesting twist
    [2020-06-03 13:09:27] <dEBRUYNE> To be clear, it concerns transactions were non-RingCT outputs are essentially converted to RingCT outputs, right?
    [2020-06-03 13:09:34] <sarang> Among that ground-truth data set, the researchers find those transactions are _still_ twice as good against guess-newest from Miller et al.!
    [2020-06-03 13:09:44] <sarang> dEBRUYNE: yes, or that aren't converted to CT at all
    [2020-06-03 13:09:52] <sarang> (very limited cases involving single inputs)
    [2020-06-03 13:09:53] <moneromooo> > Because there are "full-CT" transactions post-changeover that are deducible,
    [2020-06-03 13:09:56] <moneromooo> Forgot a no, right ?
    [2020-06-03 13:10:03] <sarang> Correct, thank you
    [2020-06-03 13:10:12] <sarang> because there are NO full-CT post-changeover that are deducible (typo)
    [2020-06-03 13:10:26] <dEBRUYNE> sarang: Thanks, I guess those are dust outputs then that first have to be converted to standardized outputs
    [2020-06-03 13:10:29] <dEBRUYNE> dust or non-mixable
    [2020-06-03 13:10:48] <sarang> So the conclusions presented in the paper about transaction counts aren't wrong, but don't differentiate between type, which I think is very important
    [2020-06-03 13:11:08] <sarang> The conclusions about guess-newest are only valid for their ground-truth set, and cannot be extrapolated to CT transactions
    [2020-06-03 13:11:17] <binaryFate> The wallet warns you when you spend old outputs that privacy is lessen and it's known you should churn in that case. It should absolutely be mentioned in their paper that these transactions are particular and users are fully informed of the risk
    [2020-06-03 13:11:31] <sarang> I'm drafting an email to the authors to let them know of this, should they wish to revise again
    [2020-06-03 13:11:49] <sarang> They were very prompt in responding to my earlier email, and very quickly revised, which was great
    [2020-06-03 13:12:32] <sarang> Now that I have a complete deduced data set, I'm checking their results on effective anonymity sets of non-deduced transactions
    [2020-06-03 13:12:45] <sarang> I want to separate those by transaction type as well
    [2020-06-03 13:13:04] <sarang> Even though the preprint had errors, I'm glad they did the research
    [2020-06-03 13:13:15] <sarang> We should encourage student researchers
    [2020-06-03 13:13:21] <binaryFate> I'm unclear on the guess-newhest on this dataset
    [2020-06-03 13:13:31] <sarang> How so?
    [2020-06-03 13:14:04] <binaryFate> Since this dataset is specifically about real output being old, shouldn't that give very specific results when seeing how the heuristic performs, that can't be extended to other transactions?
    [2020-06-03 13:14:27] <sarang> Yes
    [2020-06-03 13:14:34] <sarang> That's what I was saying earlier
    [2020-06-03 13:15:09] <sarang> They assumed their ground-truth post-changeover dataset was representative of all post-changeover transactions, which is entirely false
    [2020-06-03 13:15:27] <UkoeHB_> pre-ringCT inputs could be used in rings just like modern coinbase outputs are, which makes me sad
    [2020-06-03 13:15:31] <dEBRUYNE> which I think is very important <= Yes, because uninformed readers may infer that it concerns full RingCT transactions
    [2020-06-03 13:16:40] <binaryFate> IIRC the decoy selection algorithm is very different for these transactions, only selecting non-ringct. Since all of them are very old, they are old on the tail of the gamma distribution, very different from recent one
    [2020-06-03 13:16:41] <moneromooo> Using pre-ringct outs as fake outs would help shortly after ringct, but would otherwise introduce a number of known spent outs in rings.
    [2020-06-03 13:16:54] <binaryFate> *they are all
    [2020-06-03 13:17:12] <sarang> When I finish the effective anonymity data, it should give a much more clear picture of the status of modern transactions (before and after ring increases too)
    [2020-06-03 13:17:33] <sarang> The code still needs some cleanup to make it easier for others to run this analysis, either now or in the future
    [2020-06-03 13:17:41] <UkoeHB_> interesting point moneromooo
    [2020-06-03 13:17:51] <sarang> thanks to gingeropolous for the use of a fast machine for this analysis
    [2020-06-03 13:18:46] <sarang> If the researchers choose not to revise, I can always write a new preprint that presents this data
    [2020-06-03 13:19:11] <sarang> but I strongly suspect the researchers will revise again, since they did a very prompt first revision
    [2020-06-03 13:19:30] <binaryFate> super cool that you checked all these results
    [2020-06-03 13:19:31] <hyc> sounds great
    [2020-06-03 13:19:38] <sarang> I can also post the raw data for the post-changeover deducible transactions, in case anyone wants to specifically analyze them
    [2020-06-03 13:19:47] <hyc> super cool that their work is pulblicly reproducible
    [2020-06-03 13:19:53] <sarang> Again, I'm really glad they did the analysis
    [2020-06-03 13:20:00] <sarang> Yeah, I didn't end up using their Java code though
    [2020-06-03 13:20:07] <sarang> I wanted some extra data they didn't provide, so I rewrote
    [2020-06-03 13:20:16] <sarang> but kudos to them for making all their code public, for sure
    [2020-06-03 13:20:40] <UkoeHB_> I'd like to see if the code can be adapted to a certain analysis I have in mind, so I'm looking forward to it
    [2020-06-03 13:20:41] <moneromooo> Not really. More like negative kudos for those that don't.
    [2020-06-03 13:20:46] <sarang> What analysis is that UkoeHB_?
    [2020-06-03 13:21:16] <hyc> moneromooo: yes but that still tends to be the majority these days
    [2020-06-03 13:21:49] <moneromooo> Papers without it are really hearsay. Should never be published.
    [2020-06-03 13:21:53] <UkoeHB_> getting data on ring loops, and comparing to a purely randomly generated ring db
    [2020-06-03 13:22:10] <sarang> Define ring loop
    [2020-06-03 13:22:13] <hyc> moneromooo: agreed
    [2020-06-03 13:22:31] <moneromooo> A ring is a circular construct. A loop is.... a.......
    [2020-06-03 13:22:55] <UkoeHB_> e.g. two outputs are owned by the same person, a loop is when their descendents intersect in the same tx
    [2020-06-03 13:23:07] <sarang> Oh, output merging
    [2020-06-03 13:23:14] <sarang> ?
    [2020-06-03 13:23:33] <moneromooo> Can happen by chance too (from fake outs).
    [2020-06-03 13:23:37] <sarang> yes
    [2020-06-03 13:23:55] <UkoeHB_> yeah basically, so I want to see the probability of given loop sizes happening randomly
    [2020-06-03 13:23:58] <sarang> I think the question is how likely it is to occur in practice vs not
    [2020-06-03 13:23:59] <Isthmus> @UkoeHB_ important research. Results will be probably be depressing :- (
    [2020-06-03 13:24:03] <moneromooo> If it was super fast, it'd be nice for the wallet to try and pick fake outs that generate "false positives".
    [2020-06-03 13:24:24] <sarang> There's code that will do forms of merge analysis, and it's something I have to add specifically to my check code
    [2020-06-03 13:24:48] <sarang> The graphs involved are likely quite large, so it isn't clear what the complexity of this is
    [2020-06-03 13:24:49] <Isthmus> If it was super fast, it'd be nice for the wallet to try and pick fake outs that generate "false positives" < 👍
    [2020-06-03 13:25:27] <sarang> FWIW the early analysis on output merging used deducible transactions only
    [2020-06-03 13:25:41] <UkoeHB_> right, I have some ideas about limiting the output range to first estimate exactly how long such analysis would take; can also limit the maximum loop size considered
    [2020-06-03 13:25:47] <Isthmus> UkoeHB_: to generate random data set, will have to select guesstimates for parameters like number of transactions per wallet. (really, would be a distribution, not single value)
    [2020-06-03 13:25:48] <sarang> yes
    [2020-06-03 13:26:27] <Isthmus> The interesting thing is that we may be able to establish statistical estimates of these parameterss based on the real blockchain data
    [2020-06-03 13:26:39] <UkoeHB_> Isthmus we can just use the transactions that already exist, but make the input rings randomly selected; this provides a direct comparison with the real ring db
    [2020-06-03 13:26:43] <Isthmus> Especially if rare "natural" occurrence, i.e. low false positive rate
    [2020-06-03 13:27:11] <sarang> This sort of analysis was considered as a major part of the churn framework as well
    [2020-06-03 13:27:16] <UkoeHB_> and do the randomly generated analysis multiple times for variance
    [2020-06-03 13:28:10] <Isthmus> Makes sense
    [2020-06-03 13:28:52] <sarang> Anyway, I've taken up a lot of time on that
    [2020-06-03 13:29:04] <sarang> Was there other research of interest to discuss from anyone?
    [2020-06-03 13:29:05] <Isthmus> I'll be interested in seeing plots where x-axis is # of txns made within a given wallet, and y-axis is statistical measures, like precision/accuracy/etc
    [2020-06-03 13:30:17] <Isthmus> I have a few quick updates
    [2020-06-03 13:30:19] <Isthmus> I’ve been doing some p2p network scalability research, creating some testing suites, etc. Still very early reading/planning, but hopefully will have some actionable insights for Monero.
    [2020-06-03 13:30:20] <UkoeHB_> yes it's a big project and might be worthy of a paper if it goes somewhere, we will see; I also want to see how well the gamma distribution is working by subtracting the theoretical distribution from what we have in reality
    [2020-06-03 13:30:35] <Isthmus> "see how well the gamma distribution is working by subtracting the theoretical distribution from what we have in reality" < YES PLEASE
    [2020-06-03 13:31:26] <Isthmus> @UkoeHB_ I have some algorithms floating around GitHub to identify and filter txns that use uniform decoy selection instead of correct algo. If you don't strip those out, it will introduce a bias in your results towards older oututs
    [2020-06-03 13:31:54] <Isthmus> I'll dig those up and send links
    [2020-06-03 13:31:57] ⇐ tromp quit (~tromp@2a02:a210:ca3:2800:1803:9b3f:b921:fc5c): Remote host closed the connection
    [2020-06-03 13:31:58] <UkoeHB_> cool thanks
    [2020-06-03 13:32:03] <sarang> Yeah, trying to exclude old software will be important
    [2020-06-03 13:32:12] <sarang> since there's no consensus enforcement
    [2020-06-03 13:34:07] <UkoeHB_> I think ring analysis is too scary for anyone to tackle alone, so a collaborative and incremental effort seems reliable
    [2020-06-03 13:34:14] <Isthmus> Software can't be any older than the last ring size change, right?
    [2020-06-03 13:34:29] <sarang> Sorry, I meant software using old/incorrect methods
    [2020-06-03 13:34:35] — Isthmus nods
    [2020-06-03 13:34:39] <sarang> "nonstandard" is a better term
    [2020-06-03 13:37:49] <sarang> A big reason why deterministic input sets are intriguing is because they're likely to contain many outputs from the same transactions
    [2020-06-03 13:38:05] <sarang> and therefore are included as a "standard feature" of all rings
    [2020-06-03 13:38:09] <binaryFate> "see how well the gamma distribution is working by subtracting the theoretical distribution from what we have in reality" I was doing stuff in that direction too, exciting!
    [2020-06-03 13:40:08] <UkoeHB_> I think I missed the last meeting. The Janus proposal was updated a week ago (https://github.com/monero-project/monero/issues/6456), and now the Janus mitigation is to encode the tx private key for recipients. For 2-out tx where there will only be 1 tx pub key, the 'change output' would use a 'hidden tx pub key' derived from the non-change recipient's encoded tx private key. An alternative would be for the
    [2020-06-03 13:40:08] <UkoeHB_> change output to use a unique 'derivation to scalar', however I am concerned that affects too much protocol-level code (could be wrong).
    [2020-06-03 13:41:34] ⇐ asymptotically quit (~asymptoti@gateway/tor-sasl/asymptotically): Remote host closed the connection
    [2020-06-03 13:42:44] ⇐ derpy_bridge_ quit (~derpy_bri@92.223.89.195): Remote host closed the connection
    [2020-06-03 13:43:03] → derpy_bridge joined (~derpy_bri@92.223.89.195)
    [2020-06-03 13:43:41] <binaryFate> What happens where there is a 2-out tx but none of them is change?
    [2020-06-03 13:44:01] <Isthmus> I think you have to make a 3
    [2020-06-03 13:44:08] <Isthmus> 3-output then?
    [2020-06-03 13:44:45] <UkoeHB_> The proposal is to enforce 1 tx pub key for 2-outs, and 1 key per output for >2-outs. All tx with no change output would have to be >2-out, even if it means adding a dummy output.
    [2020-06-03 13:45:03] <moneromooo> A 0 change is automatically added *only* if there's one output otherwise.
    [2020-06-03 13:45:32] <UkoeHB_> Right, and following the proposal there would be a very rare case of 2 non-change outs needing a dummy
    [2020-06-03 13:45:58] <Isthmus> It's an edge case, so I perceive this as a reasonable solution
    [2020-06-03 13:46:18] <UkoeHB_> Originally encoding the tx private key was disregarded since current tx share tx pub keys, but since we'd start enforcing more tx pub keys that problem is solved.
    [2020-06-03 13:46:36] <UkoeHB_> i.e. as a solution for Janus*
    [2020-06-03 13:47:55] → tromp joined (~tromp@2a02:a210:ca3:2800:1803:9b3f:b921:fc5c)
    [2020-06-03 13:48:51] <UkoeHB_> Well, the hidden tx pub key might be unnecessary now that I think about it.. anyway that's my dusty update.
    [2020-06-03 13:49:25] <ArticMine> but does this means that a 2 out tx always has change real or dummy
    [2020-06-03 13:49:39] <UkoeHB_> yes
    [2020-06-03 13:50:00] <ArticMine> Can this then be attacked?
    [2020-06-03 13:50:32] <UkoeHB_> the idea that there is always a change output in 2-out tx? that assumption can be made today already
    [2020-06-03 13:51:14] — Isthmus quietly mumbles that if we had a 3-output minimum this wouldn't be an issue
    [2020-06-03 13:51:24] <Isthmus> Oh no wait, it would just move the issue to n+1
    [2020-06-03 13:51:25] <sarang> Sorry, connection problems; back now
    [2020-06-03 13:51:40] <ArticMine> but not with 100% certainty
    [2020-06-03 13:52:20] <UkoeHB_> well the shenanigans around 2-out tx are mostly to optimize scanning and tx sizes, since 2-out tx are ~95% of tx
    [2020-06-03 13:53:41] <UkoeHB_> that's true ArticMine
    [2020-06-03 13:56:17] ⇐ MSavoritias quit (~MSavoriti@44-224-rev.isper.sk): Quit: MSavoritias
    [2020-06-03 13:56:17] <luigi1111w> one can assume with high certainty that every transaction contains a change output. I don't understand why that's a significant observation.
    [2020-06-03 13:56:53] <Isthmus> Most txns. Churn doesn't, for example.
    [2020-06-03 13:57:09] <sarang> ^
    [2020-06-03 13:57:18] <moneromooo> Why does it not ?
    [2020-06-03 13:57:36] <sarang> Doesn't have to
    [2020-06-03 13:57:46] <sarang> And would affect output merging later
    [2020-06-03 13:57:48] <moneromooo> Well, that's circular reasoning then.
    [2020-06-03 13:57:50] <Isthmus> Churning with change creates the loops UkoeHB_ mentioned earlier
    [2020-06-03 13:58:08] <luigi1111w> churn has two change outputs, no?
    [2020-06-03 13:58:23] <ArticMine> It can
    [2020-06-03 13:58:26] <luigi1111w> or one and a fake one
    [2020-06-03 13:58:46] <UkoeHB_> churn has an 'output to yourself' and a 'change output'; change outputs are handled differently in the code
    [2020-06-03 13:59:18] <luigi1111w> sure but this is from a network perspective
    [2020-06-03 13:59:36] <UkoeHB_> yeah
    [2020-06-03 13:59:40] <ArticMine> Or a split 2 separate wallets under the control of one person
    [2020-06-03 14:00:24] <ArticMine> It introduces uncertainty
    [2020-06-03 14:00:43] <luigi1111w> but why does it matter?
    [2020-06-03 14:01:56] <ArticMine> because even a small bias can grow.
    [2020-06-03 14:03:25] <sarang> Given the time, is there other research that needs to be brought up before adjourning?
    [2020-06-03 14:03:47] <Isthmus> I've got 2 updates, will keep brief for sake of time:
    [2020-06-03 14:03:52] <Isthmus> Our CCS for researching Monero’s post-quantum security is sooooooo close. Only 7% left, less than 40 XMR needed. https://ccs.getmonero.org/proposals/research-post-quantum-monero.html
    [2020-06-03 14:03:55] <Isthmus> If that could get topped off today, we’ll dive in immediately and have our first update at next week’s MRL meeting. :- )
    [2020-06-03 14:03:59] <Isthmus> Unrelated - I also have one of Insight’s DistSys engineers buildling “speedup” networks, i.e. highly-connected peers with high bandwidth to propagate blocks/txns through the ad hoc network faster than organic propagation. Main goal is to eliminate the long tail in block propagation times.
    [2020-06-03 14:04:03] <Isthmus> The codebase is very modular with Terraform/ansible deployment and control scripts, so could be configured to spin up a Monero speedup network in the future.
    [2020-06-03 14:04:14] <Isthmus> That's all from me.
    [2020-06-03 14:04:21] → asymptotically joined (~asymptoti@gateway/tor-sasl/asymptotically)
    [2020-06-03 14:04:31] <sarang> Nice!
    [2020-06-03 14:05:02] <sarang> I suppose I should mention that I welcome/request comments/questions/emoji on my funding proposal as well, so a decision can be made whether to open it: https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/148
    [2020-06-03 14:06:21] <luigi1111w> thanks for opening it well in advance
    [2020-06-03 14:06:32] <sarang> OK, I suppose we can formally adjourn for the sake of logging
    [2020-06-03 14:06:38] <sarang> Thanks to everyone for joining in today
    [2020-06-03 14:06:43] <sarang> Discussion can of course continue!


# Action History
- Created by: SarangNoether | 2020-06-01T16:55:18+00:00
- Closed at: 2020-06-03T18:09:23+00:00
