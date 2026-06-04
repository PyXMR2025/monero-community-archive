---
title: Monero Research Lab Meeting - Wed 27 May 2026, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1395
author: j-berman
assignees: []
labels: []
created_at: '2026-05-25T15:46:22+00:00'
updated_at: '2026-06-02T16:55:19+00:00'
type: issue
status: closed
closed_at: '2026-06-02T16:55:19+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

Live log: https://libera.monerologs.net/monero-research-lab

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/meeting.html?p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686.

4. [Monero-PSK](https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502).

5. [FCMP beta stressnet](https://github.com/seraphis-migration/monero/releases/).

6. [FCMP++ integration audit](https://github.com/seraphis-migration/monero/issues/294).

7. [CCS proposal: ProbeLab P2P Network Metrics Proposal](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667).

8. Any other business

Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: j-berman (Rucknium can't make it and requested I substitute)

Previous meeting agenda/logs:

https://github.com/monero-project/meta/issues/1393

# Discussion History
## j-berman | 2026-06-02T16:55:19+00:00
```
17:00:25 <br-m> <jberman> Meeting time! https://github.com/monero-project/meta/issues/1395
17:00:35 <br-m> <neptunian:unredacted.org> Hooray.
17:00:45 <br-m> <jberman> I'll be substituting for Rucknium today
17:00:48 <br-m> <jberman> 1. Greetings
17:00:50 <tevador> Hi
17:01:00 <br-m> <neptunian:unredacted.org> Hello.
17:01:00 <br-m> <sgp_> Hi
17:01:06 <rbrunner> Hello
17:01:12 <br-m> <vtnerd> hi
17:01:23 <br-m> <jpk68:matrix.org> Hello
17:01:51 <br-m> <syntheticbird> Hi
17:01:57 <br-m> <jberman> 2. Updates. What is everyone working on?
17:01:59 <br-m> <redsh4de:matrix.org> hi
17:02:29 <br-m> <gingeropolous> hi
17:02:49 <br-m> <vtnerd> me: created lws 1.0 beta branch, and having otherwise been looking at serialization stuff in monerod/lws/lwsf
17:03:35 <br-m> <neptunian:unredacted.org> I'm currently reading up on Raccoon, Raccoon-G, and other possible schemes for PQ-DSA (See MRL issue 159). 
17:03:44 <br-m> <jberman> me: beta stressnet v2 (we just released v2.0 which includes an auto rollback to address a stressnet-specific consensus issue in v1), FCMP++ integration audit handling some suggestions (the phase 1 audit went well, only informational suggestions found, and it seemed solidly deep. Final report I anticipate will be ready soon)
17:03:48 <tevador> me: updated the Jamtis specs and drafted Monero-PSK
17:03:59 <br-m> <gingeropolous> me: waiting on monerosim approval / issues, debating diving into running dns ban list experiments with it
17:04:33 <rbrunner> Polyseed in the RPC wallet server
17:05:09 <br-m> <jberman> 3. Post-Quantum Encryption ( https://github.com/monero-project/research-lab/issues/151 ).
17:05:20 <br-m> <jeffro256> Howdy 
17:06:05 <br-m> <ofrnxmr> > 2025-11-07 02:12:19.109    E wrong miner tx in block: , b.miner_tx.vin.size() != 1
17:06:05 <br-m> <ofrnxmr> I think i found the cause of this, and possibly fixed it. Hard to reproduce though, so, yeah. Testing
17:06:45 <tevador> I updated Jamtis specs to reflect what was discussed in the past few meetings. https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832
17:07:13 <tevador> Still a lot of work left, mainly in the appendix.
17:07:36 <br-m> <diego:cypherstack.com> hi
17:07:38 <br-m> <diego:cypherstack.com> CS has a thing
17:09:18 <br-m> <jberman> tevador you mentioned Monday that the Jamtis-PQ solves the weaknesses in the filter-assist tier from Jamtis-Seraphis (specifically that the tier can't link  enotes to known addresses and that it can't know if the same address received >1 enote) using an additional identify-received key. Tbc, that's an additional pub key in the address
17:10:08 <br-m> <jberman> Was my rationale above accurate in explaining the stronger justification for an additional pubkey? "With the addition of PQ protection, seems the additional key has a more marginal impact on address sizes now"
17:11:08 <tevador> Yes, the additional pubkey only adds ~40 characters, which is small compared to the address length of 400 characters
17:11:21 <tevador> And the benefits are definitely worth it I think
17:12:06 <br-m> <jberman> I would agree, that's a significant benefit for much lower cost than it originally was
17:12:29 <rbrunner> But only relatively?
17:12:50 <rbrunner> 40 of 400 is 10%, 40 of 200 is 20%
17:13:03 <tevador> Yes, the addition of PQ encryption shifted the scale
17:13:38 <rbrunner> Ok. I think that's a valid point of view :)
17:13:53 <tevador> Also a notable change in the specs is that the secondary view tag is constructed differently so a quantum attacker cannot always decide if an enote belongs to the wallet with a high probability. https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832#682-component-derivations
17:14:22 <tevador> I think this is also worth the extra 3 bytes in each address.
17:14:25 <br-m> <neptunian:unredacted.org> tevador to clarify regarding Appendix B (Interactive payments) in the Jamtis spec, I just want to know if atomic swaps will become a concern in the future.
17:15:11 <tevador> neptunian: I don't follow. Why would an optional interactive payment protocol have any effect on atomic swaps?
17:16:12 <br-m> <neptunian:unredacted.org> I just realised I misread it. Disregard what I said lol
17:17:22 <br-m> <jberman> Arguably an atomic swap protocol may be more included to use the interactive protocol (since atomic swaps are interactive) and would benefit
17:17:31 <br-m> <jberman> more inclined*
17:18:05 <tevador> Yes, it might be beneficial for atomic swaps, not concerning.
17:18:27 <br-m> <neptunian:unredacted.org> Good to know. Thanks.
17:18:39 <tevador> The interactive protocol is there to enhance the overall PQ resistance, but it's not always possible to use it. Jamtis of course supports traditional non-interactive transactions.
17:19:27 <tevador> I will add a clarification in Appendix B.
17:20:22 <br-m> <jberman> PQ protection on view tags is a nice added bonus. That would bring Option A closer to Option B in terms sounds like
17:20:38 <br-m> <jberman> From this table: https://github.com/monero-project/research-lab/issues/151#issuecomment-4412416686
17:22:03 <tevador> Yes, but it works only in some cases, notably for enotes that have been received to an address the QA doesn't know and the wallet must not have received more than 1 enote to the same address.
17:23:04 <br-m> <jberman> Ha, that pesky caveat. Still a solid improvement that I agree is worth an additional 3 bytes in each address
17:24:22 <br-m> <jberman> Anything further on PQ encryption today? Thank you tevador for your continued quality work on this
17:25:35 <br-m> <neptunian:unredacted.org> Unless someone wants to talk on the question of Jamtis enforcement, I have nothing further to add.
17:25:57 <tevador> I think that can be left for later.
17:26:25 <br-m> <jberman> What's the question of Jamtis enforcement? As in enforcement at consensus?
17:27:14 <br-m> <neptunian:unredacted.org> @jberman: Yes. https://gist.github.com/tevador/639d083c994c1ef9401832c08e2b7832?permalink_comment_id=6097146#gistcomment-6097146
17:27:19 <tevador> Jamtis requires a special tx-extra field. The question is if nodes should enforce its presence.
17:27:52 <tevador> Transactions lacking this field cannot be sending to a Jamtis address, which leaks information.
17:28:24 <tevador> It's similar to the issue with the number of transaction public keys and subaddresses.
17:28:32 <br-m> <jberman> I'd lean toward Option 3B
17:29:23 <br-m> <jberman> Ideally we'd also enforce a consistent tx format for tx pubkeys and subaddresses at consensus
17:29:29 <br-m> <neptunian:unredacted.org> @jberman: My thinking as well. I was in favour of 3A or 3B
17:30:37 <tevador> CSIDH-1024 key validation takes ~10 ms of CPU time (for options 3A vs 3B)
17:30:54 <br-m> <jberman> Part of the leaning toward deprecating tx extra was hardening protocol fields in tx format at consensus. I think enforcing consistent tx formats is a good goal
17:31:40 <br-m> <neptunian:unredacted.org> tevador: Would it be possible for 3A to come first with 3B after as to minimise metadata leakage? 
17:31:54 <br-m> <jberman> Key validation = decompressing the point? So wallets will need to do it anyway? If it was the case that if consensus doing it could save the wallet some ops during scanning, I'd be more inclined for 3A
17:32:05 <br-m> <jpk68:matrix.org> Is the key only put in tx_extra because that allows Jamtis to be a soft fork?
17:32:33 <br-m> <jpk68:matrix.org> Rather than adding a separate field
17:33:29 <tevador> jberman: key validation is similar to checking if an EC point is on the curve. It needs to be done before acting on the public key with a private key to avoid attacks.
17:33:43 <br-m> <syntheticbird> epic matrix parsing
17:34:03 <br-m> <neptunian:unredacted.org> @syntheticbird: lol
17:34:04 <tevador> jpk68: exactly, Jamtis is supposed to be a soft fork
17:34:15 <br-m> <vtnerd> an attacker could re-use the same key too right? meaning 3A is of marginal use compared to 3b
17:36:00 <tevador> I was thinking it would be mostly to deter lazy wallet developers, but yeah, they can just ship a hardcoded valid CSIDH key...
17:36:17 <tevador> Not sure if it's a real concern
17:36:50 <br-m> <jberman> or they could chuck other things into the tx that pass validation. I agree it seems doing extra crypto ops validation on the key at consensus is probably of marginal benefit here
17:37:14 <br-m> <vtnerd> I don’t think its an issue, other than de-compressing the point has somewhat low utility
17:37:57 <br-m> <jberman> presumably wallets would break if the key is invalid too, so lazy wallet devs would be deterred by having a broken wallet
17:39:52 <br-m> <neptunian:unredacted.org> I doubt it would manifest in a significant manner if it's only in lazy-dev-wallets.
17:40:32 <br-m> <jberman> We can circle back to this convo in a future meeting, but Option 3B seems sanest to me fwiw
17:40:41 <tevador> Agreed
17:40:57 <br-m> <neptunian:unredacted.org> @jberman: That sounds good.
17:41:06 <br-m> <jberman> 4. Monero-PSK ( https://gist.github.com/tevador/9169235b3c0c97e735f58a8c2ba92502 )
17:42:49 <tevador> This would be another addressing protocol backward compatible with Carrot, but with different tradeoffs.
17:43:21 <br-m> <jberman> Another advantage to Monero-PSK is PQ resistance no? Just using symmetric encryption rather than a key exchange protocol
17:43:56 <tevador> Yes, but the PQ resistance is kind of moot because it requires the address to stay secret and Jamtis has the same property when addresses are kept secret.
17:44:27 <br-m> <jberman> Ah, I see
17:45:05 <br-m> <neptunian:unredacted.org> I am very concerned about the enote construction being stateful. That is already mentioned in the disadvantages section, though.
17:45:11 <tevador> My claim is that we don't want *two* new address formats, so the choice should be either Jamtis or Monero-PSK, but not both.
17:45:35 <br-m> <jberman> I think Monero-PSK is a neat idea to think on. The disadvantages are pretty significant and I have a hard time swallowing them, but an interesting thought experiment
17:45:48 <br-m> <neptunian:unredacted.org> Having both would also make enforcement that much harder.
17:46:13 <br-m> <jberman> I also agree we ideally wouldn't want two new address formats
17:46:47 <tevador> Monero-PSK doesn't need any enforcement since it doesn require any extra on-chain data.
17:46:57 <br-m> <jpk68:matrix.org> It would be unfortunate to make the protocol more fragmented. Sort of like what SSL did (someone made this analogy last week)
17:47:52 <br-m> <neptunian:unredacted.org> Correct me if I'm wrong, however, since it would be Jamtis XOR Monero-PSK, adopting 3B would lead to possible metadata leakage with Monero-PSK addresses, no? 
17:48:16 <br-m> <sgp_> Fwiw I think instant syncing is going to be worth it in a non-negligible number of cases, but it I had to pick one or the other, it wouldn't be the option that forces an interactive payment
17:48:25 <br-m> <jberman> The core benefit of Monero-PSK is that the daemon stores extra query-able data per tx that enables someone to efficiently query for their txs, no?
17:49:05 <tevador> neptunian: no
17:49:25 <br-m> <sgp_> "Alice needs to keep track of the number of generated addresses, "address lookahead" is needed in order to restore from a seed"
17:49:26 <br-m> <sgp_> What happens if this is unknown? Is there a major disadvantage to picking a large/excessive lookahead number?
17:49:44 <tevador> sgp_: Monero-PSK doesn't require interactive payments, only interactive address exchange.
17:50:30 <tevador> sgp_: Yes, the same as current subaddress lookahead. Unexpectedly high value = wallet will not detect the payment
17:50:30 <br-m> <sgp_> tevador: Sorry that's what I meant
17:51:11 <br-m> <sgp_> tevador: I don't see this as a meaningful downside then
17:51:49 <tevador> The "lookahead" issues are very similar to what we have now with subaddresses. However, Jamtis doesn't have those issues.
17:52:15 <tevador> So it's a downside compared to Jamtis.
17:52:49 <br-m> <hbs:matrix.org> the lookahead is not interactive in the sense PSK would be (needing coordination between both parties) so it varies quite significantly
17:54:09 <br-m> <hbs:matrix.org> or you mean identifying the last index could be done by a lookahead mechanism
17:54:09 <tevador> Yes, with Monero-PSK, the damage is much greater if you give the same address to 2 people.
17:55:07 <br-m> <vtnerd> hmm. how to re-synchronize on recovery from seed?
17:55:14 <br-m> <neptunian:unredacted.org> What would happen if Bob lost his local database and restores from his seed under Monero-PSK?
17:55:26 <tevador> Blockchain lookahead only works if the address was used. If you give 100 addresses to 100 people who never pay you, you have to remember to always skip those addresses.
17:55:59 <br-m> <vtnerd> correct, but then recovery means it PSK can never be re-used?
17:56:32 <br-m> <vtnerd> as-in if you recover from seed in a PSK environment, you can only recover existing addresses but not give out new ones
17:56:40 <tevador> When restoring a waller from a seed, the user would have to manually tell the wallet to skip 100 addresses that have been given out but not used.
17:57:11 <br-m> <sgp_> Ideally there would be both formats :( the wallet UI would differentiate between "single use" addresses and "reusable" addresses. I think most people will have a better experience with single use addresses and no syncing. I'm sorry that this comment isn't particularly helpful, but I do appreciate the work that went into PSK in chasing better UX
17:58:19 <rbrunner> Maybe now that the basic idea is "born" people will take it, run with it, and improve
17:58:42 <br-m> <sgp_> Fwiw I'm not actually suggesting that both (in their current forms) should be used together, but they both have their merits
17:58:51 <br-m> <jberman> Worth emphasizing: if you give out the same subaddress to 2 different people today, they can't infer which enotes on chain are yours. But with this scheme, if you do that, they can. It brings Monero closer to Bitcoin's privacy properties too
17:59:10 <br-m> <neptunian:unredacted.org> rbrunner: I hope so, but that's why I agree with @jberman:monero.social's sentiment of it being an interesting thought experiment.
17:59:12 <rbrunner> All enotes?
17:59:29 <rbrunner> (two persons receiving the same address)
17:59:30 <tevador> Only enotes sent to the reused address.
17:59:35 <br-m> <jberman> the enotes received to that address*
17:59:50 <rbrunner> Oh, that does not sound so drastic
18:00:25 <rbrunner> Little trade-off, enjoy these benefits, but remember to not do A), B) and C)
18:00:25 <tevador> It's slightly better than Bitcoin because it doesn't leak to external observers.
18:00:50 <br-m> <jberman> Personally I think the filter-assist tier has an improved tradeoff profile of fast sync with better privacy properties
18:01:08 <br-m> <sgp_> I consider that limitation to be acceptable. Unlike with Bitcoin there's no future graph analysis to cluster addresses
18:01:25 <br-m> <jberman> (The filter-assist tier in Jamtis-PQ)
18:01:33 <rbrunner> Yeah, filter-assist is almost like giving out your view key today, but without giving out the view key :)
18:02:10 <br-m> <sgp_> If fast enough, then yeah it may be "good enough"
18:03:01 <br-m> <neptunian:unredacted.org> I'm still anxious about Monero-PSK being stateful with the presented UX risks (i.e. manual skipping) 
18:03:11 <br-m> <hbs:matrix.org> Isn't it too complex for users and could lead to many errors where addresses would be reused?
18:03:23 <tevador> Jamtis is more versatile. It can support static addresses and "almost" instant sync with filter assist.
18:03:39 <rbrunner> Maybe dumb idea, but can't you just send something yourself to otherwise unused addresses, so no skips needed?
18:05:24 <br-m> <neptunian:unredacted.org> rbrunner: I think that risks breaking sender privacy.
18:06:01 <rbrunner> Ah, yes, you would need to have something like a secret with yourself ...
18:06:11 <br-m> <sgp_> filter assist requires an always running server though
18:06:41 <br-m> <jberman> fwiw I think Monero-PSK would be much more attractive if Jamtis-PQ still had those old privacy issues in the filter-assist tier from Jamtis-Seraphis. but because Jamtis-PQ doesn't, it's a more attractive set of tradeoffs to me
18:07:37 <br-m> <jberman> @sgp_: this is true, and tbc, one that specifically has a key that a user provides to it
18:07:46 <br-m> <jberman> to scan the chain with
18:08:10 <br-m> <jeffro256> @sgp_: Or for you to temporarily do full scans 
18:08:35 <br-m> <sgp_> is the expectation that wallet providers run filter assist scanning for their users? or is the expectation that it is used in similar situations as LWS is today? or do we not know :)
18:09:55 <br-m> <hbs:matrix.org> Relying on a wallet provider poses a lot of issues, centralization,possible censorship, leaks...
18:10:09 <tevador> Filter-assist is a replcement for LWS.
18:10:26 <tevador> and services like MyMonero
18:11:24 <br-m> <hbs:matrix.org> not mentioning the burden on said provider who could be tempted to raise their existing fees or make user pay for their service.
18:12:06 <br-m> <neptunian:unredacted.org> @hbs:matrix.org: Maybe the wallet provider could provide a default? Like how Cake has their own nodes to default to? I still agree with the issues, though.
18:12:14 <br-m> <jeffro256> @hbs:matrix.org: As long as running a monero daemon remains relatively low cost, good luck charging for LWS services
18:14:41 <tevador> MyMonero had users
18:14:52 <br-m> <sgp_> like I said, if I had to pick one, it would be jamtis-pq
18:15:18 <br-m> <syntheticbird> @sgp_: about the same. my heart is towards jamtis-pq
18:15:20 <br-m> <sgp_> but instant sync without needing a server is a huge UX win for "most users"
18:15:38 <br-m> <neptunian:unredacted.org> @sgp_: Ditto.
18:15:52 <br-m> <hbs:matrix.org> @syntheticbird: +1
18:16:17 <br-m> <redsh4de:matrix.org> @syntheticbird: +1
18:17:11 <br-m> <vtnerd> tevador: it would just be integrated into LWS as an option … ?
18:17:42 <br-m> <jberman> I had concern with more of the ecosystem moving toward filter assisted services with the old set of privacy issues, but I have less concern with it now considering Jamtis-PQ's improved privacy profile for it
18:17:51 <br-m> <jberman> I could imagine both 1) more people running LWS for one (and it ending up a first class binary alongside monerod)
18:18:13 <br-m> <jberman> and 2) more MyMonero-like wallet service providers offering it
18:19:08 <tevador> vtnerd: yes, it should be an option (possibly the only option for Jamtis)
18:19:20 <br-m> <jberman> the centralization / censorship risk is mitigated to a degree because wallets technically always sync via daemon too. wallets can include both a daemon to point to and LWS e.g.
18:19:30 <br-m> <hbs:matrix.org> @jberman: Regulatory pressure may reduce the number of entities willing to provide such services more than it would increase it
18:19:31 <br-m> <jberman> technically can always sync via daemon*
18:20:26 <br-m> <jberman> There is a notable privacy risk with more centralized service providers too collecting txs (and doing timing analysis on users using the service to send txs)
18:20:58 <br-m> <vtnerd> yeah I would have to look at the overhead of storage+transmission, some wallets may still want full filtering (seems like you think this should never happen)
18:22:04 <br-m> <jberman> I'd argue a "better" model would be for wallets to point to distinct daemon and LWS (ideally controlled by separate entities). Use daemon + tor/i2p/some mixnet for construction / submitting txs, and LWS for scanning
18:22:32 <br-m> <jpk68:matrix.org> @syntheticbird: +1
18:23:45 <tevador> vtnerd: my concern is that "full filtering" will win due to being easier to implement and we'll lose the privacy benefits
18:24:08 <br-m> <sgp_> I think this discussion can be deferred since it seems people are in favor of jamtis-pq even if no FilterAssist servers are widely used
18:24:23 <br-m> <jberman> @hbs:matrix.org: Fwiw, MyMonero doesn't exist anymore and there is I think just 1 centralized LWS operator out there today? Edge wallet? Sky Wallet requires users to bring their own LWS ya?
18:25:07 <br-m> <sgp_> two distinct use-cases for LWS. Partially trusted (like using their remote node) can use FilterAssist, while at home I can self host with ViewAll no prob
18:28:47 <br-m> <jberman> Ok, moving on to next agenda item
18:29:13 <br-m> <jberman> 5. FCMP beta stressnet. ( https://github.com/seraphis-migration/monero/releases/ )
18:29:49 <br-m> <jberman> We launched v2.0, which solved a stressnet-specific consensus issue in beta stressnet v1, and also solved a few other issues identified during the stressnet
18:30:53 <br-m> <jeffro256> Right now, the testnet difficulty is spiked but is coming down, so the fork date will probably end up hppening tomorrow
18:31:00 <br-m> <jberman> v2 auto rolls back the chain in order to revert the consensus issue, and will fork from the current testnet in ~500 blocks
18:32:25 <br-m> <jberman> We'll see how the relaunch goes and continue tackling issues identified
18:33:27 <br-m> <jberman> Any further questions/comments on beta?
18:34:08 <br-m> <jberman> 6. FCMP++ integration audit. ( https://github.com/seraphis-migration/monero/issues/294 )
18:35:01 <br-m> <jberman> The audit went well, only information issues identified. Currently working on remediations for the informationals, and still awaiting the final document
18:35:59 <br-m> <jberman> There was one item from Phase 1B that they were not able to complete a comprehensive audit on within the time allotted (though they did look into it)
18:36:22 <br-m> <jeffro256> Is it okay if you list which one that is?
18:36:25 <br-m> <jberman> Specifically this item: "Verify the claim that no output or commitment detectable as a valid receive on the Monero blockchain today (or at any point in the past) would cause output_to_tuple to throw. This is critical because it means that an output that is detectable as a valid receive under existing/prior rules would not be spendable after FCMP++ goes into effect. "
18:37:28 <UkoeHB> Were my comments here included in the audit? https://github.com/seraphis-migration/monero/issues/294#issuecomment-4086444878
18:37:56 <br-m> <jberman> It's an important item. I think it's understandable that it wasn't completed within the timeframe. I do think they were rigorous in the items they did explore
18:38:37 <br-m> <jberman> I had updated both those bullets to try to cover those comments a while back 
18:39:55 <br-m> <jberman> (prior to the audit)
18:40:11 <UkoeHB> It didn't include equivalence of the unbiased hash to point impls.
18:41:19 <br-m> <jberman> > which may simply involve verifying that the C++ implementation is fully Elligator2-spec-compliant
18:41:19 <br-m> <jberman> it included that part
18:42:31 <UkoeHB> You mean the audit included that? It isn't in the bullets that I can see, unless I am blind.
18:42:49 <UkoeHB> Wait I see it now!
18:42:55 <br-m> <jberman> > Does the implementation match Elligator 2 as specified in the Elligator paper: https://eprint.iacr.org/2013/325.pdf ? We are aware the implementation does not match the IRTF specification.
18:43:05 <br-m> <jberman> That was added after/from your coment
18:43:23 <br-m> <jberman> and prior to the audit
18:43:52 <br-m> <jberman> and the audit did include that
18:44:50 <UkoeHB> The remark about being off-spec implies it could not match with the rust version, hence my being anal about this. Do we even have any test vectors the rust version is checking?
18:46:20 <br-m> <jberman> Will look closer post meeting (also pinging @kayabanerve:matrix.org ). One of the valid suggestion they made during the audit was also to add more test vectors with known answer tests for various items
18:47:33 <UkoeHB> Thanks. Does the fcmp C API expose any code paths that actually depend on the rust version of the Hp impls?
18:48:49 <br-m> <jberman> That's a good q. I'm not sure, also can look into that
18:49:43 <br-m> <jeffro256> Off the top of my head, I want to say that the FCMP membership verification and SA/L verification is independent of the hash-to-point function chosen 
18:50:12 <UkoeHB> Yeah sal is independent.
18:52:20 <br-m> <jberman> Further comments on integration audit? I'll get back to those q's, and continuing on remediation / awaiting final report
18:53:02 <br-m> <diego:cypherstack.com> oh uh
18:53:05 <br-m> <diego:cypherstack.com> are we on code audit?
18:53:08 <br-m> <diego:cypherstack.com> I have the completed version from CS
18:53:42 <br-m> <diego:cypherstack.com> https://mrelay.p2pool.observer/m/cypherstack.com/jQquPPViperLiEQRRqJSzixs.pdf (FCMP_Code_Implementation_Audit.pdf)
18:55:01 <br-m> <jberman> Nice, thank you ! 🙏
18:56:19 <br-m> <jberman> Will take a closer look
18:57:08 <br-m> <luke:cypherstack.com> All feedback would be much appreciated! Also, there is a rather elegant proof about the unbiasedness of the hash to point scheme included. 
18:58:07 <br-m> <jberman> Will do in the coming days
18:58:40 <br-m> <jberman> 7. CCS proposal: ProbeLab P2P Network Metrics Proposal. ( https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/667 )
18:59:18 <br-m> <yiannisbot:matrix.org> Hi everyone myself and @dennis_tra:matrix.org  are around.
19:00:24 <br-m> <dennis_tra:matrix.org> Hi everyone
19:00:42 <br-m> <yiannisbot:matrix.org> We've received feedback from the community during the last few MRL meetings and have revised the proposal.
19:01:28 <br-m> <yiannisbot:matrix.org> Consensus seems to have been that Milestone 1 on general metrics and dashboards should be removed from the scope of the project and instead focus on Milestone 2. We've revised the proposal accordingly and expanded the scope of Milestone 2 with more details.
19:04:07 <br-m> <freeman:cypherstack.com> @luke:cypherstack.com: When he thinks your proof is elegant 🥰💍🤩
19:04:59 <br-m> <jberman> @ofrnxmr:monero.social @sgp_:monero.social @boog900:monero.social do you guys have further thoughts on the updated proposal? Apologies I haven't been following this item closely
19:05:08 <br-m> <luke:cypherstack.com> Unironically, it might be one of the nicest proofs I have ever seen. All the pieces just smoothly fit together.
19:06:11 <br-m> <boog900> > We will try to quantify how big of a role do spy nodes play. The Dandelion++ paper assumes that spy nodes do not play a role and therefore ignores them in the analysis
19:06:25 <br-m> <boog900> I am not sure I understand that 
19:07:26 <br-m> <ofrnxmr> @jberman: It was just updated abt an hr ago
19:07:35 <br-m> <boog900> The whole point of D++ is to minimize the spying ability of spy nodes 
19:08:50 <br-m> <yiannisbot:matrix.org> @boog900: Yup, at this stage and given we're not going to analyse the D++ specifics (e.g., message propagation), we're going to look at how spy nodes affect the network from a connectivity point of view as a first step. 
19:09:19 <br-m> <yiannisbot:matrix.org> This particular recommendation was originally from @rucknium:monero.social
19:13:24 <br-m> <jberman> @ofrnxmr: Seems people could use more time to grok/weigh the updated proposal
19:14:20 <br-m> <boog900> IMO I would want the proposal focused on investigating solutions, so I like the few points focused on that
19:14:47 <br-m> <yiannisbot:matrix.org> @jberman: Sure, but also, I'd suggest to contribute to the issue so that we make faster progress ;-) 
19:15:15 <br-m> <boog900> I don't know if you saw, but I made an issue for proving connections: https://github.com/monero-project/research-lab/issues/160
19:15:45 <br-m> <boog900> tevador also gave a proposal in there too
19:16:44 <br-m> <boog900> it would be good for those to be included in the analysis
19:19:11 <br-m> <yiannisbot:matrix.org> @boog900:monero.social: I didn't see this - thanks for the pointer. Regarding solutions: we don't know which solution would work at this stage, so it's difficult to list it. If the community has clearer view, please share and we can focus our investigation accordingly. But it doesn't seem to be the case from what I gather the  [... too long, see https://mrelay.p2pool.observer/e/iN7-oocLZ0ZheHRl ]
19:19:37 <br-m> <yiannisbot:matrix.org> @boog900: Let me have a look at the details and will get back to this thread and/or add it to the proposal.
19:21:39 <br-m> <sgp_> I also don't fully understand the comment here, but overall I think the changes are in the right direction > <@boog900> > We will try to quantify how big of a role do spy nodes play. The Dandelion++ paper assumes that spy nodes do not play a role and therefore ignores them in the analysis
19:23:19 <br-m> <jberman> Thank you guys. Feel free to keep discussing. I'll close the meeting here
19:23:40 <br-m> <boog900> @yiannisbot:matrix.org: We have had a few ideas: https://github.com/monero-project/research-lab/issues/126 and that link I just sent.
19:24:11 <br-m> <boog900> But if we knew what would work we wouldn't need to investigate 
19:24:37 <br-m> <boog900> The reason they are still here is we don't know how to get rid of them 
19:24:59 <br-m> <sgp_> Mandatory kyc to run a node, ez /s
19:25:52 <br-m> <yiannisbot:matrix.org> @boog900: Exactly, that's what we also want to investigate. But we also don't have a solution off the shelf 😂
19:27:15 <br-m> <boog900> That's fair, but then I don't think we need more research to tell us we have a problem 
19:28:22 <br-m> <yiannisbot:matrix.org> @boog900: But this way the problem will just remain, no?
19:28:52 <br-m> <boog900> I mean we already know we have a problem 
19:30:29 <br-m> <yiannisbot:matrix.org> Sure, we don't plan to do a study to confirm there's a problem. We'd like to get closer to a solution, or ideally find a solution. If there's no research around it then it will just continue to be a problem.
```

# Action History
- Created by: j-berman | 2026-05-25T15:46:22+00:00
- Closed at: 2026-06-02T16:55:19+00:00
