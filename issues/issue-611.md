---
title: Monero Research Lab Meeting - Wed 22 September 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/611
author: carrington1859
assignees: []
labels: []
created_at: '2021-09-15T19:39:09+00:00'
updated_at: '2021-09-22T19:21:56+00:00'
type: issue
status: closed
closed_at: '2021-09-22T19:21:56+00:00'
---

# Original Description
https://forum.monero.space/d/110-monero-research-lab-meeting-wed-22-september-2021-at-1700-utc

Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Time:
17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20210922T170000&p1=1440)

Main discussion topics:

1. Greetings
2. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's recent update](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480) ) @j-berman @Rucknium
3. Analysis of July-Aug 2021 tx volume anomaly ( isthmus { @Mitchellpkt } )
4. Triptych vs. alternatives ( [Lelantus Spark](https://eprint.iacr.org/2021/1173) , [Seraphis](https://github.com/UkoeHB/Seraphis) , [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )
5. Removing/fixing/encrypting unlock time ( [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78) ) (it also affects [binning](https://github.com/monero-project/research-lab/issues/84))
6. MRL META: Active recruitment of technical talent, MRL structure (@Rucknium & others)
7. Any other business
8. Confirm next meeting agenda

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: ?


# Discussion History
## janowitz | 2021-09-20T18:26:18+00:00
`Analysis of July-Aug 2021 tx volume anomaly ( isthmus { @Mitchellpkt } )`

Can't wait for the analysis tbh, since after two weeks of "normal" pattern we see again some anomaly...

## carrington1859 | 2021-09-21T09:13:57+00:00
> `Analysis of July-Aug 2021 tx volume anomaly ( isthmus { @Mitchellpkt } )`
> 
> Can't wait for the analysis tbh, since after two weeks of "normal" pattern we see again some anomaly...

You might be correct: https://bitinfocharts.com/comparison/monero-transactions.html#6m

Worth bringing up at the meeting for sure!

## UkoeHB | 2021-09-22T18:00:52+00:00
```
[2021-09-22 17:01:28] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/611 I will take chair unless someone else steps up
[2021-09-22 17:01:31] <UkoeHB> 1. greetings
[2021-09-22 17:01:33] <UkoeHB> hello
[2021-09-22 17:01:48] <Rucknium[m]> Hi
[2021-09-22 17:01:49] <rbrunner> hi there
[2021-09-22 17:01:55] <Halver[m]> Hello
[2021-09-22 17:01:57] <asdf234[m]> hello! here to watch
[2021-09-22 17:01:59] <jberman> Hello
[2021-09-22 17:02:15] <carrington[m]> Howdy
[2021-09-22 17:03:04] <UkoeHB> Today we will skip updates in favor of agenda items.
[2021-09-22 17:03:14] <UkoeHB> 2. Improvements to the mixin selection algorithm
[2021-09-22 17:03:14] <wfaressuissia> Hello
[2021-09-22 17:03:40] <sethsimmons> Hi all
[2021-09-22 17:04:13] <gingeropolous> hi
[2021-09-22 17:04:43] <rottenstonks> waddap.
[2021-09-22 17:04:56] <Rucknium[m]> Mixin selection algo: I submitted my Vulnerability Response Process submission a week ago. moneromooo has looked at it. Not sure exactly what I can share from that conversation. Anyway, I expect to have a draft CCS by tomorrow or Friday and do the PR thing on the CCS website
[2021-09-22 17:05:13] <Rucknium[m]> Work is proceeding apace
[2021-09-22 17:05:34] <Rucknium[m]> jberman has some updates on enforcement of the distribution at the consensus level I think
[2021-09-22 17:06:13] <jberman> Reminder of 4 areas are:
[2021-09-22 17:06:27] <jberman> 1. Integer truncation in the wallet (e.g.: `3 / 2 = 1`)
[2021-09-22 17:06:27] <jberman> 2. Binning
[2021-09-22 17:06:28] <jberman> 3. Modifying the distribution estimator (@Rucknium spearheading this)
[2021-09-22 17:06:28] <jberman> 4. Validating correct algo used at consenus
[2021-09-22 17:06:43] <Rucknium[m]> I guess I have also been taking a dip into the  literature. The number of papers on Monero has been increasing rapidly. That's part of the agenda item on MRL structure.
[2021-09-22 17:06:49] <jberman> [1] Integer truncation is still out for review in PR 7798, nothing to update there
[2021-09-22 17:07:32] <jberman> [2] Binning is still mostly relevant to discuss in context of what to do with timelocks, again
[2021-09-22 17:08:03] <jberman> [3] Ruck's update clarifies what he's up to there
[2021-09-22 17:08:54] <jberman> [4] Validating the correct algo used at consensus: I shared a poc for validation at consensus level, but imo it is still premature to get deep into the weeds going through it
[2021-09-22 17:09:39] <Rucknium[m]> I agree that [4] is going to be very tricky. It will need months of dedicated study.
[2021-09-22 17:09:46] <UkoeHB> [2] Binning: I think if we want large rings, then this will become a problem if timelocks aren't changed. To reference large rings without any deterministic compression techniques, requires a lot of data. Suppose 100 ring members - at 2-5 bytes per varint offset, this can be 200-500 bytes (vs 20-40 bytes currently with 11 ring members).
[2021-09-22 17:10:31] <sethsimmons> AFAICT timelocks have no support, and could be removed without any major ecosystem effect.
[2021-09-22 17:10:39] <gingeropolous> ^
[2021-09-22 17:10:59] <sethsimmons> I haven't heard from a single person or project that uses them, atomic swaps do not rely on them, and wallets do not normally use/allow them except official CLI.
[2021-09-22 17:11:06] <UkoeHB> It would be helpful for people to look at the alternative solutions and express opinions/ideas (instead of silently agreeing).
[2021-09-22 17:11:22] <sethsimmons> I don't think there are any issues with deprecation there.
[2021-09-22 17:11:27] <Rucknium[m]> Seth For Privacy: jberman has written up some initial thoughts about ecosystem impact here:
[2021-09-22 17:11:27] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/78#issuecomment-924622985
[2021-09-22 17:12:01] <jberman> I think the most interesting known use case for it is proof of unspent funds
[2021-09-22 17:12:10] <jberman> Described there and in that discussion
[2021-09-22 17:12:23] <carrington[m]> Alternative solutions?
[2021-09-22 17:12:24] <moneromooo> FWIW I removed unlock_time for all txes except coinbase and nothing broke.
[2021-09-22 17:12:46] <rbrunner> You mean in a test branch of yours?
[2021-09-22 17:12:53] <moneromooo> Yes (TF).
[2021-09-22 17:13:21] <Rucknium[m]> People in r/Monero are railing against Binance and saying that Binance and other exchanges should release info on proof of funds. Could time locks help with that? Just throwing out ideas.
[2021-09-22 17:13:42] <moneromooo> Proof of balance does not use timelocks.
[2021-09-22 17:14:04] <noizecore[m]> encryption option sounds like the best bet besides the increase in t size
[2021-09-22 17:14:15] <noizecore[m]> how much bigger are we talking?
[2021-09-22 17:14:20] <noizecore[m]> s/t/tx/
[2021-09-22 17:14:26] <UkoeHB> noizecore[m]: something like 25-50%
[2021-09-22 17:14:46] <sethsimmons> Just read the jberman details, still all for removal.
[2021-09-22 17:14:58] <jberman> Right, people/Binance could use that proof of balance (get_reserve_proof) instead
[2021-09-22 17:15:14] <sethsimmons> The size/verification loss due to encryption is way too major, and leaving un-encrypted goes against a core tenet of Monero -- standardize TXs as much as possible.
[2021-09-22 17:15:22] <noizecore[m]> UkoeHB: and besides that it has a clear benefit over all other options yeah?
[2021-09-22 17:15:27] <sethsimmons> Not to mention the issues with binning etc.
[2021-09-22 17:15:30] <moneromooo> It does leak private info though (ie, which outputs are yours IIRC).
[2021-09-22 17:16:05] <sethsimmons> Increased dev time and no real use case ATM.
[2021-09-22 17:16:08] <UkoeHB> it does? I haven't looked at it too closely
[2021-09-22 17:16:37] <moneromooo> Though that could be mitigated. It uses 1-rings IIRC. Could be made to use 11-rings or whatever else.
[2021-09-22 17:2021-] <sethsimmons> The encrypted option would involve extra dev work AFAIK.
[2021-09-22 17:2021-] <moneromooo> In fact, it could use huge rings since we don't really care that much about size or verification time.
[2021-09-22 17:2021-] <Halver[m]> My understanding is that, if needed, a timelock feature can probably be implemented on the client side.
[2021-09-22 17:2021-] <Halver[m]> (but I may be wrong ?).
[2021-09-22 17:2021-] <Halver[m]> So I don't see as crucial to put such a feature in the protocol.
[2021-09-22 17:2021-] <Halver[m]> s///
[2021-09-22 17:2021-] <moneromooo> Anyway, for unlock_time, my preference is remove and add later if needed for L2 purposes or the like (and possibly with different semantics).
[2021-09-22 17:18:22] <gingeropolous> +1
[2021-09-22 17:18:30] <sethsimmons> moneromooo: Agreed!
[2021-09-22 17:18:44] <UkoeHB> I also prefer to remove. It is a legacy thing mainly used to lock coinbase outputs (probably added for that purpose originally).
[2021-09-22 17:19:17] <sethsimmons> Can coinbase outputs be locked another way?
[2021-09-22 17:19:34] <sethsimmons> What happens to the 60 block lock if unlock_time is removed?
[2021-09-22 17:19:43] <noizecore[m]> UkoeHB: how would this affect UX?
[2021-09-22 17:19:44] <sgp_[m]> hi all, sorry I'm late
[2021-09-22 17:19:45] <moneromooo> You could keep it for them.
[2021-09-22 17:19:46] <sethsimmons> Or can it be used for just coinbase without effecting binning?
[2021-09-22 17:19:50] <jberman> Just an implementation detail, not an issue sethsimmons
[2021-09-22 17:20:09] <sethsimmons> Ok, great :)
[2021-09-22 17:20:10] <rbrunner> Just hardcode then?
[2021-09-22 17:20:15] <UkoeHB> noizecore[m]: it would simplify UX a bit, by removing some options
[2021-09-22 17:20:35] <jberman> Ok, I think we can move on from timelocks, don't need to take up the whole time on it
[2021-09-22 17:20:55] <UkoeHB> jberman Rucknium[m] anything else to add about agenda item 2? Points we should put more attention on?
[2021-09-22 17:20:55] <jberman> Summary: consensus continues to form strongly for removing and bringing back if desired
[2021-09-22 17:21:15] <Rucknium[m]> No, I am done with item 2
[2021-09-22 17:21:49] <sgp_[m]> moneromooo: +1
[2021-09-22 17:22:02] <UkoeHB> jberman: ?
[2021-09-22 17:23:00] <UkoeHB> 3. Analysis of July-Aug 2021 tx volume anomaly
[2021-09-22 17:23:16] <UkoeHB> isthmus: 
[2021-09-22 17:23:47] <Rucknium[m]> According to my impression, we have produced overwhelming evidence that the tx volume anomaly was due to the actions of a single entity...
[2021-09-22 17:24:14] <Rucknium[m]> Furthermore, doing so was incredibly cheap if our calculations were correct.
[2021-09-22 17:24:40] <Rucknium[m]> isthmus seems not to be here right now, but myself jberman, carrington, and gingeropolous have helped
[2021-09-22 17:24:59] <Rucknium[m]> I think the results will be released within a day or two
[2021-09-22 17:25:15] <rottenstonks> 👀 single entity?
[2021-09-22 17:25:16] <Rucknium[m]> But on every metric we looked at, the conclusion seems inescapabale.
[2021-09-22 17:25:19] <UkoeHB> I think the fee analysis has generally considered spam in the minimum penalty free zone of 300kB to be acceptable.
[2021-09-22 17:25:27] <carrington[m]> The conclusions are spooky and should motivate a network upgrade ASAP
[2021-09-22 17:25:29] <sgp_[m]> approx how many transactions do you think we created this way?
[2021-09-22 17:25:49] <moneromooo> "we" ?
[2021-09-22 17:26:06] <gingeropolous> lulz. prolly "were"
[2021-09-22 17:26:07] <rottenstonks> as in the monero network?
[2021-09-22 17:26:20] <sgp_[m]> hehe, "were"
[2021-09-22 17:26:35] <Rucknium[m]> This isn't group consensus, but it is my impression that the characteristics of the anomaly do not fit an actual malicious actor. They better fit an academic researcher or just some greyhat hacker that did it for the lulz (it would have been cheap enough to do it for lulz)
[2021-09-22 17:27:08] <sgp_[m]> what would make you think that
[2021-09-22 17:27:47] <UkoeHB> It could also be a malicious entity testing things out.
[2021-09-22 17:27:53] <Rucknium[m]> 1) They did not try to hide their actions at all
[2021-09-22 17:27:53] <Rucknium[m]> 2) The "flood" wasn't quite enough to seriously harm privacy
[2021-09-22 17:28:27] <Rucknium[m]> UkoeHB  Yes, that is one possibility.
[2021-09-22 17:28:44] <sgp_[m]> I'll wait for the writeup, but I have many other questions still
[2021-09-22 17:28:51] <rbrunner> Me too
[2021-09-22 17:28:53] <Rucknium[m]> isthmus thinks that a hardfork, or whatever is needed, needs to come soon to fix the low fee issue.
[2021-09-22 17:28:54] <gingeropolous> yes .. this is important to discuss, but i dunno how productive this can be if the report isn't available for review etc. 
[2021-09-22 17:29:01] <wfaressuissia> "[4] is going to be very tricky. It will need months of dedicated study." can you define few verifiable metrics that will be improved and can be verified ?
[2021-09-22 17:29:26] <wfaressuissia> s/and can be verified//
[2021-09-22 17:29:43] <rbrunner> People probably won't agree that we have a "low fee issue"
[2021-09-22 17:29:46] <Rucknium[m]> wfaressuissia[m]: That's earlier in the agenda, but what do you mean?
[2021-09-22 17:29:51] <carrington[m]> Fee increase + ruck and jbermans decoy selection work would go a long way to mitigating such an attack
[2021-09-22 17:30:34] <Rucknium[m]> A single tx can be like one tenth of one cent, right?
[2021-09-22 17:31:07] <rbrunner> Would that made such a flood considerably more expensive already?
[2021-09-22 17:31:11] <UkoeHB> Rucknium[m]: have you looked at the fee cost if tx volume was high enough to eat into the penalty zone? Minimum fees are very very low for a reason.
[2021-09-22 17:31:50] <sgp_[m]> we already have a proposal for the base fee increase
[2021-09-22 17:31:54] <wfaressuissia> In general, bad decoy selection amplify efficiency of spam attack, but doesn't ideal decoy selection isn't a protection against spam attack
[2021-09-22 17:32:02] <Rucknium[m]> isthmus did the fee calcs. He said "The anomalous transaction volume was paying standard fees, which at the time was about 0.000015 XMR per transaction with this construction"
[2021-09-22 17:32:05] <wfaressuissia> s/doesn't//
[2021-09-22 17:32:14] <sgp_[m]> and yeah it's definitely more complicated than base fee * txs, that's 1 thing floodxmr messed up in v1 of their paper
[2021-09-22 17:32:50] <rottenstonks> https://github.com/monero-project/research-lab/issues/70
[2021-09-22 17:33:38] <rottenstonks> https://github.com/monero-project/monero/pull/7819
[2021-09-22 17:33:45] <Rucknium[m]> Sorry, isthmus calcs say that the fee would have been about 0.003USD/tx , not 0.001USD/tx as I stated above. Still, very low.
[2021-09-22 17:34:18] <sgp_[m]> yeah cheap in any case
[2021-09-22 17:34:24] <gingeropolous> well, that chain needs to be active for ring sigs to do their thing
[2021-09-22 17:34:28] <gingeropolous> *the chain
[2021-09-22 17:34:40] <gingeropolous> im just stating obvious things
[2021-09-22 17:35:45] <carrington[m]> Monero needs to walk the tightrope between fees being low enough to allow a big crowd to hide in, and high enough to prevent flood or big bang attacks. I don't think tx volume would plummet if fees were $0.01
[2021-09-22 17:35:51] <UkoeHB> > "[4] is going to be very tricky. It will need months of dedicated study." can you define few verifiable metrics that will be improved and can be verified ?
[2021-09-22 17:35:51] <UkoeHB> I am also curious about this.
[2021-09-22 17:36:00] <Rucknium[m]> I suppose we can wait until the results are published and then discuss more. I expected publication by now, but there are just so many rabbit holes to go down. There still are, but the rest of the rabbit holes will have to wait.
[2021-09-22 17:36:15] <Rucknium[m]> UkoeHB: What do you mean by metrics?
[2021-09-22 17:36:26] <moneromooo> Maths :)
[2021-09-22 17:36:42] <gingeropolous> so, whats the goal here? try and find ways to prevent flood attack? or mitigate the effect of flood attack?
[2021-09-22 17:36:52] <UkoeHB> he probably means, how to assess if a proposal for enforcing distribution is worth pursuing?
[2021-09-22 17:37:00] <sgp_[m]> can't prevent really
[2021-09-22 17:37:10] <Rucknium[m]> Do you mean what criteria might be used to enforce the distribution used?
[2021-09-22 17:37:21] <jberman> [4] is validating tx's ring members match the expected distribution of decoys. It would prevent older implementations of the decoy selection algo from making their way onto the chain
[2021-09-22 17:37:21] <jberman> We could go through the chain and identify blatantly incorrect rings as a % of all rings
[2021-09-22 17:37:27] <moneromooo> How will you assess whether a given change is beneficial compared to what we have.
[2021-09-22 17:37:44] <gingeropolous> to me, prevention is fee based. mitigation is ringsize a bajillion and smarter ring member selection
[2021-09-22 17:37:45] <moneromooo> (I assume that's what is meant by metrics)
[2021-09-22 17:37:52] <jberman> openmonero is using a blatantly old implementation of the decoy selection algo that I believe can be fingerprinted
[2021-09-22 17:38:02] <Rucknium[m]> UkoeHB: We already sort of know it's worth looking at since txs that don't follow the standard can stick out like a sore thumb.l  The problem will get worse if and when ring size increases.
[2021-09-22 17:38:03] <jberman> I think we can identify openmonero tx's
[2021-09-22 17:39:16] <rbrunner> Somehow I am not quite comfortable with the thought that 1 greyhat hacker or 1 bored dev does some flooding, once, and *bang* we all already have to pay higher fees ...
[2021-09-22 17:39:40] <rottenstonks> whoa, whoa. big if true. jberman
[2021-09-22 17:39:53] <UkoeHB> I think the main cost of enforcing a distribution, as has been mention by others, it lack of flexibility to update decoy selection ad hoc in the face of unforseeable problems. Updating the algorithm inserts an extra dependency on core that isn't savory in the long run.
[2021-09-22 17:39:59] <sgp_[m]> rbrunner: the proposal for this upgrade was written and discussed before this attack
[2021-09-22 17:40:16] <rottenstonks> rbrunner: did you through MRL 70 yet?
[2021-09-22 17:40:19] <Rucknium[m]> If a truly malicious party floods the blockchain with txs and therefore owns a huge share of the outputs, they could trace nearly all txs.
[2021-09-22 17:40:25] <gingeropolous> interesting UkoeHB 
[2021-09-22 17:40:26] <rbrunner> Only a cursory glance.
[2021-09-22 17:40:27] <carrington[m]> If we had binning we could have deterministic rings without the need for statistical tests, yes?
[2021-09-22 17:40:32] <rottenstonks> k.
[2021-09-22 17:40:45] <Rucknium[m]> That's my understanding of what a FloodXMR attack involves
[2021-09-22 17:40:48] <jberman> That's my understanding carrington[m]
[2021-09-22 17:41:17] <rbrunner> Well, maybe truly malicious entities can also fees that are quite a lot higher ...
[2021-09-22 17:41:27] <sgp_[m]> okay there are a bunch of different overlapping topics right now being discussed at the same time
[2021-09-22 17:41:33] <sgp_[m]> moneromooo: I want to get back to this
[2021-09-22 17:41:41] <Rucknium[m]> rbrunner: This is also true
[2021-09-22 17:42:30] <Rucknium[m]> sgp_: I think some ideas have already been floated. We don't have to enumerate all of them. It's an ongoing process.
[2021-09-22 17:44:45] <Halver[m]> short paper (2014) from MRL about floodXMR
[2021-09-22 17:44:47] <Halver[m]> https://www.getmonero.org/resources/research-lab/pubs/MRL-0001.pdf
[2021-09-22 17:45:09] <rbrunner> I wonder how that complicated and time consuming [4] will fare if we are constrained for dev and/or researcher time and have many other important things.
[2021-09-22 17:45:20] <carrington[m]> We can probably conclude this agenda item I guess? Summary is that anomaly analysis should motivate urgent work towards a network upgrade
[2021-09-22 17:45:26] <UkoeHB> ok let's get back on track
[2021-09-22 17:45:26] <UkoeHB> - [4] enforced distribution: TBD needs research (also needs to clearly describe how to evaluate if a proposal to enforce distribution is better than what we have, and doesn't weaken Monero's long-term viability)
[2021-09-22 17:45:26] <UkoeHB> - fee changes: there is PR #7819 that will probably be mergable by next week or later this week; it will increase base fees, and adjusts the algorithm according to MRL #70
[2021-09-22 17:45:26] <UkoeHB> - spam: a report is incoming from isthmus
[2021-09-22 17:45:49] <UkoeHB> 4. Triptych vs. alternatives; any new questions/comments?
[2021-09-22 17:46:14] <sgp_[m]> yes all sounds good koe
[2021-09-22 17:46:42] <sgp_[m]> oh quick update just for visibility
[2021-09-22 17:46:50] <noizecore[m]> UkoeHB: yes how close are we to a decision? is triptych more or less off the table?
[2021-09-22 17:46:52] <sgp_[m]> on lelantus spark
[2021-09-22 17:46:55] <UkoeHB> Seraphis has been updated, and Spark is being updated, to fix an issue brought up by nwk (thanks :)). It causes a slight efficiency loss, but otherwise is a good step forward.
[2021-09-22 17:47:34] <sgp_[m]> an outside researcher found a vulnerability that would have allowed a view key holder to burn funds
[2021-09-22 17:47:38] <endogenic> fwiw it is customary, every time someone says lelantus, to belt out the word as if it is a magical incantation 
[2021-09-22 17:47:43] <wfaressuissia> Was it always the case that any cryptography update had final stage in form of binary predicate (safe / unsafe) implemented by security audit / paid peer review ?
[2021-09-22 17:47:52] <sgp_[m]> this is being remedied
[2021-09-22 17:48:14] <UkoeHB> noizecore[m]: probably no closer than last week. I think Triptych is considered a fall-back if Seraphis/Spark fall through somehow.
[2021-09-22 17:48:36] <sgp_[m]> agreed more or less 👍️
[2021-09-22 17:48:45] <UkoeHB> wfaressuissia: only since bulletproofs/CLSAG/bp+ I think
[2021-09-22 17:48:47] <ArticMine> I would agree with UkoeHB
[2021-09-22 17:49:14] <rbrunner> "allowed a view key holder to burn funds" huh?
[2021-09-22 17:49:17] <sethsimmons> UkoeHB: Agreed
[2021-09-22 17:49:20] <ArticMine> Sorry I got confused o nthe time
[2021-09-22 17:49:23] <wfaressuissia> Also does successfully passed audit / paid review for Seraphis / <any other decen. anon. paym. system> implementation is the only requirement to use it for monero ?
[2021-09-22 17:49:32] <gingeropolous> wfaressuissia, not in the earliest days. i forget if ringct went through that kind of gauntlet. 
[2021-09-22 17:49:39] <wfaressuissia> s/does//
[2021-09-22 17:49:44] <sgp_[m]> wfaressuissia[m]: no not always, RingCT originally was not audited (which ended up being really bad)
[2021-09-22 17:49:58] <sgp_[m]> and then we ended up being lucky
[2021-09-22 17:50:01] <UkoeHB> rbrunner: yeah the key image contained only view key material, so a view key holder could make a malicious output to burn funds found in the view-only wallet
[2021-09-22 17:50:29] <rbrunner> Ugh ... thanks for the info
[2021-09-22 17:50:38] <noizecore[m]> UkoeHB: yeah i picked that up, Seraphis would be more beneficial for tx-chaining right? 
[2021-09-22 17:51:03] <UkoeHB> noizecore[m]: yes, depending on design decisions (and assuming no issues are found)
[2021-09-22 17:51:04] <sgp_[m]> it definitely sucks but it can be addressed luckily, and it's good it was caught so early
[2021-09-22 17:51:20] <gingeropolous> wfaressuissia, i wouldn't say thats the only requirement
[2021-09-22 17:51:53] <noizecore[m]> whats the latest on BP+? 
[2021-09-22 17:51:59] <UkoeHB> > Also does successfully passed audit / paid review for Seraphis / <any other decen. anon. paym. system> implementation is the only requirement to use it for monero ?
[2021-09-22 17:51:59] <UkoeHB> There are also: utility, efficiency/size cost
[2021-09-22 17:52:16] <ArticMine> Do we have any figures?
[2021-09-22 17:52:18] <gingeropolous> and apparently multisignature happiness
[2021-09-22 17:52:34] <rbrunner> Exactly :)
[2021-09-22 17:52:38] <UkoeHB> noizecore[m]: pretty sure it's audited and waiting to be plugged in
[2021-09-22 17:53:10] <carrington[m]> BP+ is implemented, doubly audited and live on Wownero
[2021-09-22 17:53:12] <UkoeHB> ArticMine: not yet, still a lot of work on my end to get perf mock ups how I want them
[2021-09-22 17:53:17] <rottenstonks> ye, bp+ is ready to be rolled.
[2021-09-22 17:53:20] <carrington[m]> Last I checked
[2021-09-22 17:53:22] <rottenstonks> has been ready for a good while.
[2021-09-22 17:53:45] <noizecore[m]> so whats the next step? are we still bundling it with the next protocol upgrade?
[2021-09-22 17:53:50] <rottenstonks> ye, wownero has had bp+ for months...
[2021-09-22 17:53:52] <sgp_[m]> ArticMine: still early for real numbers to compare apples:apples
[2021-09-22 17:54:01] <noizecore[m]> from what I understand Seraphis/LS are still a while off
[2021-09-22 17:54:43] <UkoeHB> is there an upcoming dev meeting to discuss bp+ planning?
[2021-09-22 17:54:43] <sgp_[m]> @r4v3r23:matrix.org: that's more of a dev question
[2021-09-22 17:54:48] <rottenstonks> noizecore[m]: no. there'll be a dev meeting to decide if we have a slight ring size increase, bp+ and whatever else, while we switch off to triptych, or lelantus and seraphis.
[2021-09-22 17:55:00] <rottenstonks> UkoeHB: aye, there is.
[2021-09-22 17:55:01] <noizecore[m]> UkoeHB: +1
[2021-09-22 17:55:37] <rottenstonks> or was... not seeing the issue on meta now. smh.
[2021-09-22 17:55:52] <UkoeHB> ok meeting is reaching the 1hr mark; should be punt the last agenda item (6. MRL META: Active recruitment of technical talent, MRL structure) to next week?
[2021-09-22 17:56:26] <Rucknium[m]> UkoeHB: I think that's fine. And yes, let's do same time next week
[2021-09-22 17:57:24] <rottenstonks> k thx, see ya next week. bai.
[2021-09-22 17:57:35] <UkoeHB> thanks for the meeting everyone
[2021-09-22 17:58:26] <gingeropolous> thanks all!
```

# Action History
- Created by: carrington1859 | 2021-09-15T19:39:09+00:00
- Closed at: 2021-09-22T19:21:56+00:00
