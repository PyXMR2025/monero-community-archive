---
title: Monero Research Lab Meeting - Wed 22 December 2021 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/642
author: Rucknium
assignees: []
labels: []
created_at: '2021-12-21T15:47:43+00:00'
updated_at: '2021-12-28T17:31:46+00:00'
type: issue
status: closed
closed_at: '2021-12-28T17:31:46+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

3. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

4. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

5. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

6. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

7. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

8. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

9. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

10. Any other business

11. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#640 

# Discussion History
## UkoeHB | 2021-12-22T18:14:46+00:00
```
[12-22-2021 17:00:12] <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/642
[12-22-2021 17:00:12] <UkoeHB> 1. greetings
[12-22-2021 17:00:12] <UkoeHB> hello
[12-22-2021 17:00:23] <tevador> hi
[12-22-2021 17:00:26] <sgp_> hello!
[12-22-2021 17:00:30] <rbrunner> Hallo
[12-22-2021 17:00:55] <Rucknium[m]> Hi
[12-22-2021 17:00:58] <jberman[m]> hello :)
[12-22-2021 17:04:49] <mj-xmr[m]> Hello!
[12-22-2021 17:06:10] <dEBRUYNE> hi
[12-22-2021 17:06:27] <sethsimmons> Hey everyone 🙂
[12-22-2021 17:06:31] <UkoeHB> 2. discuss Seraphis address schemes: https://github.com/monero-project/research-lab/issues/92 https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024
[12-22-2021 17:06:31] <UkoeHB> Does anyone have any comments/questions about this?
[12-22-2021 17:06:56] <UkoeHB> My goal today is to narrow down the choice to 1-3 options.
[12-22-2021 17:07:35] <dEBRUYNE> I think many users would appreciate a view key that has full functionality, i.e., shows the balance, plus incoming and outgoing transactions
[12-22-2021 17:07:48] <dEBRUYNE> Thus, arguably we already should reduce the options to the schemes that include this
[12-22-2021 17:08:01] <UkoeHB> That is everything except Plain A
[12-22-2021 17:08:33] <dEBRUYNE> OK ty
[12-22-2021 17:08:37] <sgp_> Doesn't reduce it too much :p
[12-22-2021 17:08:47] <dEBRUYNE> Mitigating the janus attack seems like an easy win if we have to change address scheme anyway
[12-22-2021 17:09:03] <Lyza> I feel like 5 wallet tiers might be a bit confusing for users, though I see 2 are only intended for merchants so maybe it won't be so bad
[12-22-2021 17:09:37] <Lyza> speaking to tevador's proposal
[12-22-2021 17:09:45] <tevador> The merchant tiers are there mainly to facilitate the phase out of integrated addresses.
[12-22-2021 17:10:10] <Lyza> interesting -- would you anticipate them falling out of use eventually then?
[12-22-2021 17:10:23] <Rucknium[m]> Why does it say "detect" a Janus attack rather than "thwart" a Janus attack?
[12-22-2021 17:10:32] <dEBRUYNE> Lyza: Would be less confusing then having integrated, sub, and public addresses, plus view key / spend key
[12-22-2021 17:10:38] <dEBRUYNE> Which we have currently 
[12-22-2021 17:11:12] <sethsimmons> I, personally, am quite in favor of JAMTIS, as it encapsulates both a solid address scheme and a great new address approach.
[12-22-2021 17:11:15] <tevador> Rucknium[m]: I think saying "detect Janus outputs" would be more accurate
[12-22-2021 17:11:37] <tevador> since you can't prevent people from sending them
[12-22-2021 17:11:40] <sethsimmons> The address format necessary to facilitate that seems to be a solid fit an matches basically what I would want from the address schemes anyways.
[12-22-2021 17:11:49] <Lyza> <dEBRUYNE> true but not as simple as the proposals with three tiers so ig I'm just asking about the benefits of the other 2
[12-22-2021 17:12:03] <dEBRUYNE> True yes
[12-22-2021 17:12:43] <UkoeHB> tevador: you might want to add a comment to the proposal noting that your scheme does not support integrated addresses (no more encrypted PIDs)
[12-22-2021 17:13:17] <tevador> FWIW, the merchant tiers can be easily removed and introduced later if needed, it doesn't affect the core of the protocol
[12-22-2021 17:13:41] <sethsimmons> tevador: Oh, that's an important detail 🙂
[12-22-2021 17:14:02] <Lyza> yeah good to know
[12-22-2021 17:14:10] <sethsimmons> Even better, then.
[12-22-2021 17:14:25] <sgp_> How important is it that the first tier of any system allows for which of the two: a) view tags only, or b) incoming outputs (no amounts)
[12-22-2021 17:14:57] <UkoeHB> can you restate the question?
[12-22-2021 17:15:15] <dEBRUYNE> sgp_: As far as I can see, with a) we can improve privacy of light wallets
[12-22-2021 17:16:02] <sethsimmons> Which tier 1 would satisfy in JAMTIS, AFAICT.
[12-22-2021 17:16:17] <jberman[m]> They do more than improve privacy of light wallets. I personally like tevador 's view tag approach or Janus B because they offer this tier
[12-22-2021 17:16:29] <sgp_> I don't think I have a super strong opinion of Janus B vs Janus E, but Janus B is more in-line with current expectations
[12-22-2021 17:16:41] <dEBRUYNE> jberman[m]: Can you elaborate on 'more'?
[12-22-2021 17:16:55] <jberman[m]> It increases the attractiveness of using tier 1 for [background client-side scanning](https://github.com/monero-project/monero/issues/8082) too, or in running your own light wallet server, such as [monero-lws](https://github.com/vtnerd/monero-lws) or [openmonero](https://github.com/moneroexamples/openmonero), and granting tier 1 permission to that server. A perpetual scanning process running on a device poses a security issue:
[12-22-2021 17:16:55] <jberman[m]> the key is hot and available to an attacker. If this key only reveals received outputs and not amounts, then the security properties of perpetually scanning the chain on a device are stronger
[12-22-2021 17:17:45] <UkoeHB> sgp_: JAMTIS is in the middle of that, it lets you compute all view tags, and additionally find incoming outputs (no amounts) for just addresses you know about (which may not be super useful in practice).
[12-22-2021 17:17:53] <sethsimmons> jberman[m]: This ^ Big step forward for the viability and privacy of lightwallets
[12-22-2021 17:18:14] <tevador> Actually, I think even revealing received outputs without amounts might be too strong. JAMTIS Tier 1 only reveals view tags, so there are decoy outputs that don't bwlong to the wallet.
[12-22-2021 17:18:25] <sethsimmons> Very, very important we have strong LWS support moving forward as the chain grows in usage.
[12-22-2021 17:18:32] <sgp_> UkoeHB: got it, I have no idea if this is useful in practice but it could be used by expert users in theory
[12-22-2021 17:18:52] <sethsimmons> And yet do so without revealing critical information in the case of a malicious 3rd-party LWS
[12-22-2021 17:19:08] <jberman[m]> tevador: this is why I like the view tag scheme too
[12-22-2021 17:19:48] <tevador> Revealing outputs means Tier 1 could heuristically detect real spends via change outputs, reducing the effectiveness of the rings that use them as decoys.
[12-22-2021 17:19:51] <Rucknium[m]> Can we ask businesses that currently use Monero what type of features they would want in an address scheme? What can we do to make their lives easier (and therefore make prospective XMR-accepting businesses more likely to accept XMR)? LocalMonero has already weighed in, but we should get more businesses in on the conversation.
[12-22-2021 17:19:57] <sgp_> sethsimmons: to be clear, revealing the view tag is still bad, it's just less bad :) So idk how much it will actually matter in practice but at least there's some deniability so that's something
[12-22-2021 17:20:25] <sethsimmons> sgp_: It's still much better than the current system.
[12-22-2021 17:20:42] <tevador> revealing the view tags is the least bad thing that can still be used to speed up wallet sync
[12-22-2021 17:20:44] <sethsimmons> Obviously the end-user should be running the LWS, but I like that this protects even those that won't/can't as much as possible.
[12-22-2021 17:21:03] <UkoeHB> tevador: since JAMTIS tier 1 can see nominal spend keys for all outputs, any time there is a duplicate they will know that is a real spend key
[12-22-2021 17:21:13] <sgp_> Is there anyone here who thinks reducing the first tier from view received outputs (no amounts) to view tags is a bad idea?
[12-22-2021 17:21:29] <ErCiccione> Rucknium[m]: I will report back for Haveno
[12-22-2021 17:21:35] <UkoeHB> sgp_: to do that, addresses need to be 1 key longer
[12-22-2021 17:21:39] <sethsimmons> sgp_: First tier of which scheme?
[12-22-2021 17:22:17] <sethsimmons> Oh Janus B
[12-22-2021 17:22:20] <sgp_> UkoeHB: I like this one, this sentence sold me (other tradeoffs aside)
[12-22-2021 17:22:21] <tevador> UkoeHB: true. It has some limitations, but introducing a separate key for view tags would have its own issues.
[12-22-2021 17:22:49] <tevador> Such as needing 2 public keys per output.
[12-22-2021 17:22:53] <jberman[m]> On view tags, I think it would be useful to benchmark performance of this approach (with various T's) to gauge exactly how useful this tier would be (how long would it take to scan the prior year's worth of outputs, how many outputs). I think it would be useful to see how significant this speed-up is to better gauge the proposal. would this speed-up be significant enough that we can be confident people will be very happy with
[12-22-2021 17:22:53] <jberman[m]> tier 1 in the long run, even when volume picks up a lot?
[12-22-2021 17:23:19] <sgp_> in practice with JAMTIS, I would run my own LWS and provide my publicly-known addresses to it for better efficiency, and then eat the slightly lower efficiency for the slightly better privacy (which appears to be a net win)
[12-22-2021 17:23:36] <sgp_> * better privacy for the other addresses (which appears
[12-22-2021 17:23:44] <UkoeHB> jberman[m]: you mean a tier than can only compute view tags, no nominal spend keys?
[12-22-2021 17:23:58] <jberman[m]> UkoeHB: yep
[12-22-2021 17:24:55] <tevador> That would also be an optiont, but it has downsides: 1 more pubkey in each address and 1 more pubkey in each output.
[12-22-2021 17:25:02] <UkoeHB> sgp_: I think the only benefit to filtering on addresses in the LWS would be less bandwidth/storage costs, not computation time.
[12-22-2021 17:27:50] <tevador> Btw, a basic JAMTIS address is 139 characters (other schemes with 3 keys would be similar).
[12-22-2021 17:28:09] <tevador> That's about 50% longer than current addresses.
[12-22-2021 17:28:24] <sgp_> suppose 1 more use-case: someone wanted to provide proof of receiving funds, but they didn't want to reveal all the future spending. As I'm reading this, they could do this with JAMTIS with the known receiving addresses, correct?
[12-22-2021 17:29:08] <UkoeHB> Are fluffypony or LocalMonero here to give their opinions on JAMTIS? They had a lot to say on the MRL issue
[12-22-2021 17:29:23] <fluffypony> what's a jamtis
[12-22-2021 17:29:27] <monerobull[m]> tevador: It's not like you can currently type them anyways
[12-22-2021 17:29:35] <UkoeHB> fluffypony: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024
[12-22-2021 17:29:51] <rbrunner> If I look at all the new possibilities of JAMTIS I really worry about A) all the functions wallets will need to handle everything, and B) the effort of users to learn about everything
[12-22-2021 17:30:02] <rbrunner> *all the new functions
[12-22-2021 17:31:03] <sgp_> while I'm also concerned about explaining the complexity, it provides better base privacy out of the box so I see it as lower overall risk
[12-22-2021 17:31:11] <fluffypony> rbrunner: but that would be abstracted from users
[12-22-2021 17:31:25] <fluffypony> and most wallets will just create a basic address and be done with it
[12-22-2021 17:31:30] <tevador> sgp_: you can prove that an address belongs to you. That's different than proving you received funds.
[12-22-2021 17:31:42] <rbrunner> Can you get away with only handle basic addresses?
[12-22-2021 17:31:54] <fluffypony> rbrunner: on the receipt side, sure
[12-22-2021 17:32:03] <dEBRUYNE> jberman[m]: Thanks, makes sense
[12-22-2021 17:32:11] <fluffypony> and on the sending side MyMonero for eg. uses the CLI code transcoded into JS
[12-22-2021 17:32:18] <fluffypony> or WASM I mean
[12-22-2021 17:32:26] <fluffypony> so it's a different world, we don't need to write stuff from scratch
[12-22-2021 17:32:46] <sgp_> tevador: hmm, so with JAMTIS are we losing the ability to show addresses receive specific outputs without also revealing balance+spend? If so, I must have misunderstood then
[12-22-2021 17:33:04] <fluffypony> tevador: one thing that we should do on addresses is start them with something, eg. xmr, so that they're immediately visually identifiable - that can just be stripped before processing
[12-22-2021 17:33:14] <fluffypony> ie. eVuKRDtxGWvdDMVX7wHS5dQFk8DgF8rvXZ7kKWMiNps25NLwiwSfriqaksdkxWVgMXVyiw54EbULLQ9FzcC4XcxhbRfCsVW2Uzx8Qjsgs7LPrJ1GHx5NX5ao6fwh2yy3oxLt7pvUcxB should be xmreVuKRDtxGWvdDMVX7wHS5dQFk8DgF8rvXZ7kKWMiNps25NLwiwSfriqaksdkxWVgMXVyiw54EbULLQ9FzcC4XcxhbRfCsVW2Uzx8Qjsgs7LPrJ1GHx5NX5ao6fwh2yy3oxLt7pvUcxB
[12-22-2021 17:33:37] <rbrunner> Hmm ... we still don't have all wallets propery support subaddresses, and/or integrated addresses, and now we invent new things by the bucketload, and hope for support. May be pretty optimistic
[12-22-2021 17:34:03] <UkoeHB> sgp_: a seraphis receive proof would be pretty much the same as it is currently
[12-22-2021 17:34:13] <sgp_> rbrunner: this streamlines many of those things though tbh
[12-22-2021 17:34:15] <tevador> sgp_: maybe I misunderstood that question, JAMTIS is no different than the current scheme in that regard. 
[12-22-2021 17:34:18] <fluffypony> rbrunner: fwiw MyMonero has supported payments to subaddresses for ages, there's just too much UX load on implementing it in the wallet
[12-22-2021 17:34:43] <tevador> fluffypony: sure, the base58 version could have a "xmr" prefix
[12-22-2021 17:34:53] <sgp_> UkoeHB: yes but what is that, something else that needs to be shared out of band in addition to a tier 1 viewing key?
[12-22-2021 17:35:01] <rbrunner> Yes, that's one of my points: How many new screens, input boxes, radio buttons etc. you will need to support all that stuff
[12-22-2021 17:35:01] <fluffypony> tevador: also would we not want the checksum to be something a little more useful / robust, eg. Reed-Solomon?
[12-22-2021 17:35:30] <UkoeHB> sgp_: if you just want to prove ownership of 1 output, you only need 1 receive proof (no tier 1 key)
[12-22-2021 17:35:32] <tevador> If the new functions are deemed too much to implement, they can be added later. Just keep the header bits and everything can be added later.
[12-22-2021 17:35:36] <dEBRUYNE> rbrunner: As far as I understood, in Seraphis there will only be one type of address basically
[12-22-2021 17:36:01] <fluffypony> rbrunner: right - and my point is that you wouldn't, you'd just have a basic address in 90% of the cases. all the other fancy bits are mostly useful to checkout flows in merchant applications, so they'd be generated by a point of sale app
[12-22-2021 17:36:06] <rbrunner> Well, if I look over the JAMTIS proposal, I see a bewildering number of possible addresses
[12-22-2021 17:36:36] <rbrunner> Yeah, maybe I over-estimate what the "normal" user would have to deal with
[12-22-2021 17:36:38] <tevador> fluffypony: I was thinking about different checksums, but base58 is not very compatible with these. I can elaborate later if needed.
[12-22-2021 17:36:40] <sgp_> UkoeHB: currently, I can provide a view key and people can see all outputs coming into that wallet. With JAMTIS, that is not possible unless you also share outgoing right?
[12-22-2021 17:37:06] <fluffypony> tevador: no need - was just curious 
[12-22-2021 17:37:12] <UkoeHB> sgp_: a tier 1 + set of addresses will show all outputs incoming to those addresses (no amounts)
[12-22-2021 17:38:08] <sgp_> UkoeHB: okay that is the best of both worlds, sorry I got confused in the middle there so thank you for clarifying
[12-22-2021 17:38:11] <UkoeHB> * if the person with tier 1 learns about your addresses from a third party, it is the same
[12-22-2021 17:38:53] <fluffypony> besides the base58 prefix I really have no further comments, this has my full support
[12-22-2021 17:38:55] <tevador> Yes, and Tier 2 can see everything including amounts and spends
[12-22-2021 17:40:09] <jberman[m]> <UkoeHB> "tevador: since JAMTIS tier 1 can..." <- can you expand on this more, when would there be a duplicate here?
[12-22-2021 17:41:13] <UkoeHB> jberman[m]: any two outputs owned by the same address will have the same nominal spend key, if scanning with a find-received key
[12-22-2021 17:42:59] <jberman[m]> what would the benefit of view tags still be in that case? couldn't you easily determine outputs owned by the same address via nominal spend keys then?
[12-22-2021 17:43:22] <tevador> Yes, if they are provided to Tier 1, you can.
[12-22-2021 17:43:32] <TheCharlatan> tevador , is there a minimum subset of features that a wallet could implement for JAMTIS as the proposal stands now? It's a bit confusing to me what the minimal features would be.
[12-22-2021 17:43:36] <tevador> Tier 1 cannot derive spend keys.
[12-22-2021 17:44:14] <UkoeHB> Overall, I think tier 1 has a lot of pitfalls to keep in mind, but there aren't any realistic ways around those issues without A) eliminating third-party scanning, B) adding cost to addresses, the chain, and LWS scanning, C) greatly increasing the power of third-party scanning
[12-22-2021 17:44:29] <tevador> TheCharlatan: yes, the basic address without metadata (mainnet header byte 0xe0)
[12-22-2021 17:44:30] <sgp_> Is it correct that a merchant address for the 1.5 wallet tier can see all incoming outputs for the wallet because they can generate addresses independently? That's my understanding
[12-22-2021 17:45:02] <tevador> sgp_: no, they can only generate addresses for one account.
[12-22-2021 17:45:06] <UkoeHB> > what would the benefit of view tags still be in that case? couldn't you easily determine outputs owned by the same address via nominal spend keys then?
[12-22-2021 17:45:06] <UkoeHB> Only if > 1 output are owned by the same address.
[12-22-2021 17:45:40] <sgp_> tevador: okay, thanks for clarifying
[12-22-2021 17:46:06] <sgp_> At this point I'm quite sold on the tiers for JAMTIS, really great work here
[12-22-2021 17:46:35] <tevador> As UkoeHB said, Tier 1 is a compromise.
[12-22-2021 17:46:47] <TheCharlatan> tevador , so the content lined out in 7.3 may be omitted?
[12-22-2021 17:47:23] <UkoeHB> oh wow, TheCharlatan long time no see
[12-22-2021 17:48:19] <tevador> TheCharlatan: yes, but then the signatures don't make much sense because they would not cover the whole payment uri (if amount and description are given separately).
[12-22-2021 17:48:37] <tevador> so you can remove 7.3 and 7.4 together
[12-22-2021 17:49:00] <tevador> the address becomes: header byte, K1, K2, K3, checksum
[12-22-2021 17:49:20] <TheCharlatan> ok, got it
[12-22-2021 17:51:26] <tevador> I was also looking into other checksum options, but the problem of base58 is that a single character typo may change up to 8 bytes, which doesn't play well with any polynomial based checksums.
[12-22-2021 17:53:05] <sech1> can they be adopted to base58?
[12-22-2021 17:53:09] <sech1> Math should be similar
[12-22-2021 17:53:34] <tevador> nope, you need the base to be a prime power
[12-22-2021 17:53:56] <tevador> base 59 might work
[12-22-2021 17:54:46] <TheCharlatan> as far as I can recollect this one of the reasons bitcoin moved to base 32 (but could be mistaken)
[12-22-2021 17:55:03] <moneromooo> Does it require more data in the output (ie, currently amount and pubkey) ?
[12-22-2021 17:55:21] <UkoeHB> Before we end the meeting, is there anyone who has an objection to JAMTIS, or thinks another scheme should be included in the list of choices?
[12-22-2021 17:55:41] <UkoeHB> rbrunner: ?
[12-22-2021 17:55:54] <tevador> moneromooo: no, except it might need a separate pubkey for each output
[12-22-2021 17:55:57] <jberman[m]> Could 8 (recipient authentication/everything related to this) be omitted as well and supported by any address scheme at a future time? As I see it, the most critical component is an additional asymmetric key pair for identity verification; couldn't we theoretically implement a protocol that accomplishes the same goal of identity verification alongside any of the proposed address schemes, at any point in the future?
[12-22-2021 17:56:09] <rbrunner> Only a quite general one, more "gut feeling" like, that this is just too much, basically of everything :)
[12-22-2021 17:56:37] <rbrunner> Falling in love with complexity because of all the possibilities it offers, nerd's dream
[12-22-2021 17:56:37] <moneromooo> I read that as "no, except maybe yes". Can you expand a bit please ?
[12-22-2021 17:57:06] <tevador> jberman[m]: as I said, the authentication features could be added later, provided the header byte format is kept.
[12-22-2021 17:57:35] <rbrunner> "Remember the time when an cryptocurrency address was just ... an address, and not everything but the kitchen sink".
[12-22-2021 17:58:06] <UkoeHB> rbrunner: there is also 'learning from experience'
[12-22-2021 17:58:11] <jberman[m]> tevador: got it
[12-22-2021 17:58:17] <tevador> moneromooo: this is related to Janus detection, I think UkoeHB had some option with only one pubkey if it's a 2-out tx with one change output.
[12-22-2021 17:58:19] <rbrunner> But I seems I am quite lonely here with these gut feelings :)
[12-22-2021 17:58:41] <rbrunner> Is also mostly a technical meeting, no wonder
[12-22-2021 17:58:49] <Rucknium[m]> Is there a way that we could make this info digestible for Monero-accepting businesses, so we can reach out to them to get their point of view?
[12-22-2021 17:59:49] <tevador> ^ second that, I'd like to hear some feedback on the merchant wallet functions
[12-22-2021 18:00:11] <Rucknium[m]> Or maybe we should have a general feedback survey, like, "What are the biggest pain points in dealing with Monero?"
[12-22-2021 18:01:03] <UkoeHB> tevador: moneromooo My goal for the new protocol is 2-out tx have 1 txo pubkey (leveraging the change/dummy output, which is mandatory for 2-outs), and >2-out tx have 1 txo pubkey per output.
[12-22-2021 18:01:38] <rbrunner> How does the common complaint "Can't generate subaddresses without knowing a secret key" translate to JAMTIS?
[12-22-2021 18:01:53] <tevador> So it should be the same as now if all outputs go to a subaddress.
[12-22-2021 18:01:58] <UkoeHB> right
[12-22-2021 18:02:10] <tevador> rbrunner: that's why JAMTIS has Tier 0
[12-22-2021 18:02:20] <rbrunner> Ah, ok
[12-22-2021 18:03:00] <tevador> I heard that was a common complaint against using subaddresses 
[12-22-2021 18:03:38] <moneromooo> "1 txo pubkey" means one more from the one we have now, right ?
[12-22-2021 18:03:47] <UkoeHB> no, it means 1
[12-22-2021 18:03:53] <rbrunner> And this has all the usual "can't correlate" active, i.e. I can't see which Tier 0 addresses are the same wallet? Or may be I confuse things now
[12-22-2021 18:04:02] <moneromooo> And 2 out txes would have... what per output ?
[12-22-2021 18:04:09] <UkoeHB> 0.5 per output
[12-22-2021 18:04:19] <moneromooo> I see.
[12-22-2021 18:04:33] <moneromooo> So better than now then ?
[12-22-2021 18:04:46] <moneromooo> Just making really sure I got it right :)
[12-22-2021 18:04:52] <tevador> rbrunner: Tier 0 is only for merchants, addresses generated by Tier 0 can be linked together off chain. 
[12-22-2021 18:05:08] <UkoeHB> the txo pubkey is the 'transaction public key' and 'additional tx keys', which are horribly named
[12-22-2021 18:05:50] <tevador> ^yes, I also found the naming to be confusing
[12-22-2021 18:06:57] <TheCharlatan> it's a really nice proposal tevador
[12-22-2021 18:08:57] <UkoeHB> rbrunner: all Tier 0 addresses would have two common keys, so all addresses from one merchant account would be linkable
[12-22-2021 18:09:21] <SerHack> I read the proposal, thanks tevador for your work
[12-22-2021 18:09:34] <sgp_> I'm absolutely staggered by the amount of information in the proposal
[12-22-2021 18:09:37] <UkoeHB> non-merchant account addresses would not be linkable
[12-22-2021 18:10:46] <tevador> I will try to incorporate the feedback from this meeting
[12-22-2021 18:10:56] <rbrunner> sgp_: Positively or negatively staggered?
[12-22-2021 18:11:13] <UkoeHB> We are past the hour, so I will call the meeting here. It seems there is a general consensus to pursue JAMTIS. Future action items include A) getting feedback from merchants, B) deciding how much of the API to support out-of-the-box.
[12-22-2021 18:11:26] <UkoeHB> Thanks for attending everyone
[12-22-2021 18:11:29] <sgp_> positive, though I need to think about sections 7+8+9
```

# Action History
- Created by: Rucknium | 2021-12-21T15:47:43+00:00
- Closed at: 2021-12-28T17:31:46+00:00
