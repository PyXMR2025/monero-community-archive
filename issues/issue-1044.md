---
title: Monero Research Lab Meeting - Wed 24 July 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/1044
author: Rucknium
assignees: []
labels: []
created_at: '2024-07-24T14:58:03+00:00'
updated_at: '2024-08-07T14:40:03+00:00'
type: issue
status: closed
closed_at: '2024-08-07T14:40:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://web.archive.org/web/20230128130949/https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. [Stress testing `monerod`](https://github.com/monero-project/monero/issues/9348)

4. Research [Pre-Seraphis Full-Chain Membership Proofs](https://www.getmonero.org/2024/04/27/fcmps.html).

5. Auditing the math of the new addressing protocol for legacy addresses.

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#1041 

# Discussion History
## Rucknium | 2024-07-26T16:42:10+00:00
Log:

> __< 0​xfffc:monero.social >__ My apologies in advance. I will be late for the meeting. I have few minor updates. I finished the sync-before-verify PR. But eventually decided ( with boog ) to not move forward with it. If anyone else wants can take a look at it [1]. Instead of it, we decided to move forward with a PR that checks hardfork and verify only if necessary [2].     

> __< 0​xfffc:monero.social >__ Other than these, I have started to work on the issue boog explained here [3]. The gist is to send txis only if it is necessary and peers asks.      

> __< 0​xfffc:monero.social >__ 1. https://github.com/spackle-xmr/monero/pull/13#issuecomment-2234543784     

> __< 0​xfffc:monero.social >__ 2. https://github.com/monero-project/monero/pull/9404     

> __< 0​xfffc:monero.social >__ 3. https://github.com/monero-project/monero/issues/9334     

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/1044     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< rbrunner >__ Hello     

> __< j​berman:monero.social >__ *waves*     

> __< j​effro256:monero.social >__ howdy     

> __< o​ne-horse-wagon:monero.social >__ Hello!     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< c​haser:monero.social >__ hello     

> __< j​berman:monero.social >__ me: finishing up initial migration of cryptonote outputs into the curve trees merkle tree for fcmp's + growing the tree as the node syncs, and cleaning up the grow_tree + trim_tree impl as I go     

> __< r​ucknium:monero.social >__ me: Reading many papers on gossip protocols and network topology. I am writing comments to these two PRs: "tx_memory_pool: make double spends a no-drop offense" https://github.com/monero-project/monero/pull/9218  "Fix embargo timeout in dandelion++" https://github.com/monero-project/monero/pull/9295     

> __< j​effro256:monero.social >__ me: drafting a distilled document for the the new addressing protocol for legacy addresses for formal auditing (hopefully). will talk more about it later in the meeting...     

> __< r​ucknium:monero.social >__ 3) Stress testing monerod https://github.com/monero-project/monero/issues/9348     

> __< j​effro256:monero.social >__ anything interesting break this week? ;)     

> __< r​ucknium:monero.social >__ AFAIK, no new incidents on stressnet. There is discussion in #monero-stressnet:monero.social  ( ##monero-stressnet on IRC) about how long stressnet should continue and how.     

> __< r​ucknium:monero.social >__ The original plan was to run it for two months (which would end about August 10th), but it could be extended if it is helpful for development.     

> __< r​ucknium:monero.social >__ and/or the stressnet could be restarted when FCMP++ are ready to test     

> __< rbrunner >__ As you explained, Rucknium, actually stressing amounts to quite some work, right?     

> __< o​ne-horse-wagon:monero.social >__ Has there been any actionable results from the stress testing so far that could be taken in the Monero codebase?     

> __< j​effro256:monero.social >__ https://github.com/monero-project/monero/pull/9404 https://github.com/monero-project/monero/pull/9395     

> __< rbrunner >__ Yes. An astonishingly high number, if you ask me.     

> __< r​ucknium:monero.social >__ Many community volunteers are running stressnet nodes. About 40 nodes at the beginning. Now about 25. They were told at the beginning that it would run for about 2 months and the blockchain would grow to about 50GB. It is 50GB now.     

> __< j​effro256:monero.social >__ https://github.com/monero-project/monero/issues/9388     

> __< j​berman:monero.social >__ +1, it's definitely been valuable     

> __< v​tnerd:monero.social >__ Hi, sorry for being late     

> __< o​ne-horse-wagon:monero.social >__ I've asked this question before.  Does it help the stress net to do some mining on it?  I do it and it seems like I'm almost the only one.     

> __< r​ucknium:monero.social >__ one-horse-wagon: Yes because it creates network conditions to test re-org/orphan block behavior     

> __< r​ucknium:monero.social >__ But not at a high hash rate     

> __< r​ucknium:monero.social >__ Actually we wouldn't have found the invalid blocks issue without multiple nodes mining AFAIK     

> __< o​ne-horse-wagon:monero.social >__ Gotcha.  I've toned it down a lot but the coins still come flying in.     

> __< r​ucknium:monero.social >__ If you have lots of mined coins that you don't plan to spam, it is good to send them to the wallets of people who are spamming so we can use the coins for tx fees. I think that's just spackle and me.     

> __< o​ne-horse-wagon:monero.social >__ Rucknium: Post your wallet address and I'll send you a few thousand.     

> __< j​effro256:monero.social >__ Do you know of anyone that has used p2pool to mine on the stressnet? Might produce interesting results     

> __< r​ucknium:monero.social >__ jeffro256: AFAIK, p2pool is not set up on stressnet. Yes, could be interesting if someone wants to set it up.     

> __< r​ucknium:monero.social >__ AFAIK, the p2pool could merge-mine with Monero mainnet now. Or at least I think that change enabling that is in a PR somewhere.     

> __< r​ucknium:monero.social >__ 4) Research Pre-Seraphis Full-Chain Membership Proofs. https://www.getmonero.org/2024/04/27/fcmps.html     

> __< r​ucknium:monero.social >__ kayabanerve , kayabanerve : Anything on FCMP for this meeting?     

> __< r​ucknium:monero.social >__ Or anyone else have something about FCMP?     

> __< r​ucknium:monero.social >__ 5) Auditing the math of the new addressing protocol for legacy addresses. ( jeffro256 's item)     

> __< j​effro256:monero.social >__ I would like to have the new addressing protocol, which I call Carrot (Cryptonote Address on Rerandomiable-RingCT-Output Transactions), deployed alonsgide the initial deployment of FCMP++ for two main reasons: 1) so we can actually leverage FCMP++'s forward secrecy and outgoing view key properties ASAP, and 2) once Jamtis is ready for deployment, there will be a smooth transition <clipped messag     

> __< j​effro256:monero.social >__ without transaction fingerprinting issues. However, I don't want the Carrot integration to slow down FCMP++, so I would like to get it audited as soon as possible. I have written almost all of the code we need to deploy Carrot (there are still kinks with payment IDs to be worked out soon), so that should not be a limiting factor. The limiting factor will probably be auditing the m<clipped messag     

> __< j​effro256:monero.social >__ ath and code. To this end, I have begun to draft a document that outlines all the details for the Carrot, distilled from tevador's Jamtis-RCT gist. After this is done, I want to propose that it gets audited with funding from the CCS. This should be a relatively straight forward audit, and I don't forsee any issues. After that, then the code auditing can begin. Luckily, FCMPs and <clipped messag     

> __< j​effro256:monero.social >__ Carrot mainly touch separate parts of the transaction (inputs and outputs, respectively), so development and integration can be parallelized nicely.     

> __< j​effro256:monero.social >__ I discussed this earlier in the week in the NWLB meeting     

> __< j​berman:monero.social >__ fcmp implementation timeline still on pace. I think within 3-4 months it'll be ready for stressnet     

> __< rbrunner >__ Viewed from the outside, a fork to FCMPs without anything Jamtis in it does look like quite a wasted chance, IMHO.     

> __< rbrunner >__ So in a timeframe of 3 to 4 months there could be room for it, yes?     

> __< j​effro256:monero.social >__ Well the new addressing protocol is not technically Jamtis, but is backwards compatible with existing addresses but obtains nice properties such as forward secrecy, OVKs, and Janus protection     

> __< j​effro256:monero.social >__ jberman: tx output construction code for Carrot is basically done, scanning code is basically done, if audits go smoothly (which they should), then the only task remaining is to integrate with wallet2, which with your async wallet scanning code we were already planning to do     

> __< rbrunner >__ Ah, yes, I did not read all. So able to separate.     

> __< j​effro256:monero.social >__ Carrot would also be indistinguishable from Jamtis on-chain, so we can switch to Jamtis easily with no loss of privacy in our own time     

> __< j​berman:monero.social >__ I have no issue with pushing it forward in parallel. Once fcmp's are done we can see where jamtis-rct is at and decide at that point what the best rollout strategy is     

> __< j​berman:monero.social >__ so +1 from me pushing auditing forwards     

> __< rbrunner >__ "Jamtis" brings, in addition, new long addresses, which means wallet changes?     

> __< j​effro256:monero.social >__ rbrunner7: IMO you're right it *would* be a wasted chance if we didn't do *Carrot* because then we don't fully leverage the FCMP features     

> __< rbrunner >__ i.e. wallet UI changes, which could be quite heavy, and might derail the time line     

> __< j​effro256:monero.social >__ Yes IMO the biggest issue with Jamtis is the friction of updating addresses. Carrot doesn't have that problem which should speed up adoption     

> __< rbrunner >__ Does anything change for hardware wallets with Carrot? Maybe things change anyway because of FCMPs?     

> __< rbrunner >__ With or without Carrot, I mean     

> __< j​berman:monero.social >__ "transaction fingerprinting issues" -> can you elaborate on the fingerprints?     

> __< j​effro256:monero.social >__ Yes HWs will have to update for FCMPs anyway on the input / spendkey side of things. For Carrot specifically, the HWs dont have to change *too* much. The ECDH key derivation is exactly the same     

> __< j​effro256:monero.social >__ Depending on if the HW supports OVKs, the key image derivation might have to change     

> __< rbrunner >__ Thanks. So they will have to move anyway, not a strong argument against Carrot early.     

> __< j​effro256:monero.social >__ jberman: 3-byte view tags, encrypted address tags / carrot randomness, and X25519 epehemeral pubkeys are not present in the current Cryptonote address protocol     

> __< j​effro256:monero.social >__ Onetime addresses, amount commitments, and encrypted amounts will look the same to external observers, though     

> __< j​berman:monero.social >__ "That means wallets can send payments to both new and old addresses and the resulting transactions will be indistinguishable in the blockchain" -> when sending to an old address, would dummy values go on chain?     

> __< j​effro256:monero.social >__ They aren't really "dummy" tx values in Carrot since all tx elements from Jamtis are used someway or another. For example, the X25519 ephemeral pubkeys are just the the new way to encode analogues of the "main"/"additional" tx pubkeys     

> __< j​berman:monero.social >__ I see in section 6.7, looks like it takes care of eliminating the fingerprints no?     

> __< j​effro256:monero.social >__ The place that *would* be used for Jamtis encrypted address tags is used to encode a "randomness" in carrot used to rederive the ephemeral private key to mitigate Janus attacks     

> __< j​effro256:monero.social >__ Yes, I don't think there's a section explicitly mentioning fingerprinting issues, but that was part of the design     

> __< rbrunner >__ You mean attention was given, while designing things, to avoid such fingerprinting issues?     

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ Alright. We have to implement this almost for the catchy name alone :)     

> __< j​berman:monero.social >__ so ultimately whenever jamtis-rct rolls out, and network consensus requires txs to spec, then we won't have fingerprinting issues, no? I'm trying to see why rolling out with fcmp's avoids fingerprinting issues     

> __< j​effro256:monero.social >__ Okay good question. Scenario 1) we stick with the old cryptonote addressing protocol with FCMP++ rollout and then try to switch to Carrot and Jamtis later. Scenario 2) we rollout with Carrot initially with FCMP++ then support Jamtis later. In scenario 1, there will be instantly noticeable difference between old Cryptonote address txs and Carrot/Jamtis transactions which splits the<clipped messag     

> __< j​effro256:monero.social >__  network into 2 anonymity pools     

> __< j​effro256:monero.social >__ With scenario 2, whenever we switch to Jamtis, there is no difference between Jamtis and Carrot transactions; All post FCMP++ txs look the same     

> __< j​effro256:monero.social >__ That's why I would like to rollout Carrot with FCMP++: to avoid the fingerprinting issues that come with supporting the new Jamtis address types     

> __< k​ayabanerve:matrix.org >__ Apologies     

> __< j​berman:monero.social >__ In scenario 1, I figure a hard frok to switch to Carrot/Jamtis is expected to require all txs be to spec, like the switch to requiring view tags at consensus     

> __< j​effro256:monero.social >__ A switch to Carrot/Jamtis need not be a hardfork     

> __< k​ayabanerve:matrix.org >__ I'm very interested in Carrot explicitly for F-S.     

> __< rbrunner >__ But only if we already have Carrot, I guess?     

> __< rbrunner >__ I.e. later adding Jamtis to the mix does not need a new hardfork     

> __< j​berman:monero.social >__ Scenario 2 includes consensus rules that require e.g. 3 byte view tags etc., no?     

> __< j​effro256:monero.social >__ Nope, we don't need Carrot even to start that addressing protocol since they can just put the scanning data in tx_extra     

> __< j​effro256:monero.social >__ jberman: what I did initally for testing was put the first byte of the view tag in the `tx_out` and the other 2 in tx_extra     

> __< j​effro256:monero.social >__ No hardfork needed     

> __< rbrunner >__ It's all a bit confusing. Maybe lay it out all carefully in your document, and then people can study and try to understand.     

> __< j​berman:monero.social >__ but then you'll have 2 anon pools, txs that include that extra data in extra and the ones that don't     

> __< j​effro256:monero.social >__ jberman: this is the situation that I'm trying to avoid but having Carrot roll out initially *with the upcoming hardfork*     

> __< j​effro256:monero.social >__ *by having     

> __< rbrunner >__ Anyway, right now for me it sounds as if going for Carrot is worthwhile even if it should not having to do anything with avoiding fingerprinting     

> __< rbrunner >__ Also known as a "no brainer" if that opinion has merit     

> __< j​effro256:monero.social >__ Ideally, since everyone is updating for FCMPs mandatorily anyways, they also receive the Carrot updates and all post-FCMP++ txs use Carrot (or Jamtis since we can't tell as an external observer)     

> __< j​berman:monero.social >__ to achieve the goal of indistinguishable txs I figure we'd want consensus to enforce the new tx format / not use extra     

> __< rbrunner >__ Certainly     

> __< j​effro256:monero.social >__ I disagree to a certain extent. I think view tags shouldn't be inside the `tx_out` structs and should be hoisted to `tx_extra`. Then there should be relay rules which dictate the contents of `tx_extra` to reduce fingerprinting     

> __< rbrunner >__ Sounds strange.     

> __< j​effro256:monero.social >__ As we've discussed before though, there's not much we can do to stop people from *purposefully* screwing up their fingerprint in txs. However, we *can* prevent accidental mistakes     

> __< j​effro256:monero.social >__ (or people putting large blobs in tx_extra)     

> __< j​effro256:monero.social >__ (or other actively so far off from normal that trivial heuristics catches it)     

> __< j​effro256:monero.social >__ *activity     

> __< k​ayabanerve:matrix.org >__ The consensus rule of FCMP++s already enables: if fcmp++, xyz, with a hard boundary.     

> __< rbrunner >__ Maybe that's stuff for another meeting, or a discussion after the meeting proper, but a solid argument pro view tags in tx_extra would surprise me     

> __< k​ayabanerve:matrix.org >__ I disagree we need additional consensus rules.     

> __< k​ayabanerve:matrix.org >__ I'm unsure I'm for TX v3 at this time though.     

> __< rbrunner >__ Is there something to fear from a new tx version?     

> __< k​ayabanerve:matrix.org >__ (or any deep structural changes with the fcmp++ fork)     

> __< rbrunner >__ Not sure a component or two more in a tx are already "deep structural changes" ...     

> __< rbrunner >__ Maybe I underestimate?     

> __< j​effro256:monero.social >__ rbrunner: a new tx version means extra technical debt and requiring a hard fork which adds even more friction to Monero adoption IMO     

> __< rbrunner >__ That tx_extra would't process itself alone either     

> __< j​effro256:monero.social >__ It's justified for FCMP++ IMO b/c if the privacy benefits     

> __< rbrunner >__ I think now you lost me :)     

> __< j​berman:monero.social >__ MyMonero is an example of a wallet that uses a pretty heavily modified version of the monero core code to construct txs. I can pretty easily imagine they only end up implementing fcmp++'s and not the other changes necessary for Carrot     

> __< rbrunner >__ Anyway, probably not that important     

> __< k​ayabanerve:matrix.org >__ TX extra is entirety out if consensus so it would in fact process itself     

> __< k​ayabanerve:matrix.org >__ jberman: If a TX is FCMP++, just only scan per Carrot.     

> __< k​ayabanerve:matrix.org >__ MyMonero can legacy send but it'd effectively be a custom protocol and their failure.     

> __< j​berman:monero.social >__ I guess if relay rules enforce the Carrot changes, then that changes things. Would have to introduce relay rules that parse tx extra etc., which I would argue is more complex than new explicit types     

> __< rbrunner >__ Maybe MyMonero throws in the towel, who knows. Will get interesting.     

> __< endogenic >__ more like they use the libs others will release     

> __< k​ayabanerve:matrix.org >__ *I do know wallets would need updating. Updating wallets is simpler to also updating the output definitions :/ IIRC they're unversioned and not an enum.     

> __< j​effro256:monero.social >__ jberman: Yes I agree that this in an issue. Could be worth discussing relay rules to at least combat fingerprinting. Really, let's say you're a lazy dev and don't care if your users get F-S, Janus protection, or OVKs with Carrot. You can add dummy encrypted address tags and view tags. The only real cryptographic code that you need to implement is the functions converting points fr<clipped messag     

> __< j​effro256:monero.social >__ om X25519 to Ed25519 and vice versa     

> __< j​effro256:monero.social >__ So even for the laziest wallet devs, you only really need `CovertPubkey1`, `CovertPubkey2`, and `NormalizeX` functions from Jamtis-RCT     

> __< k​ayabanerve:matrix.org >__ jberman: We don't need relay rules if we just don't scan TXs with legacy extra.     

> __< rbrunner >__ I really think we shouldn't even explain to lazy devs how to be maximally lazy :)     

> __< rbrunner >__ And get away with it.     

> __< k​ayabanerve:matrix.org >__ As jeffro says, there's ways to cheat implementing Carrot and one can do so. Relay rules/strict typing wouldn't catch that.     

> __< j​berman:monero.social >__ ya, fair arguments     

> __< k​ayabanerve:matrix.org >__ But if we only scan Carrot, it does mandate sending as Carrot.     

> __< rbrunner >__ And everybody will still find all transactions?     

> __< k​ayabanerve:matrix.org >__ No relay rules needed.     

> __< j​berman:monero.social >__ I mean they have to change scanning on their end too     

> __< k​ayabanerve:matrix.org >__ FCMP++ TXs would have a distinct scan procedure (Carrot). All prior TXs would be fine.     

> __< rbrunner >__ If somebody can just put in any old random data, I don't see how that would work out for everybody overall.     

> __< rbrunner >__ For things they don't feel like implementing     

> __< rbrunner >__ Maybe it is so, but somehow does not sound right     

> __< k​ayabanerve:matrix.org >__ That's presumably always a risk, yet wallet2 would handle it. The concern is completely custom impls aiui     

> __< j​berman:monero.social >__ Carrot scanning is distinct code from FCMP++ scanning     

> __< k​ayabanerve:matrix.org >__ Wat     

> __< endogenic >__ so make custom impls. everyone will adapt     

> __< k​ayabanerve:matrix.org >__ What's FCMP++ scanning in your context?     

> __< endogenic >__ myMonero doesn't even really have a scale advantage     

> __< endogenic >__ so it's not worth worrying about whether or not they're going to be able to scale their implementation     

> __< k​ayabanerve:matrix.org >__ Outputs are versioned, my bad, sorry. I drop my strict typing concerns.     

> __< endogenic >__ that's very kind of you guys to worry about someone who scammed the entire community though     

> __< endogenic >__ lol     

> __< j​berman:monero.social >__ it's not worrying about them necessarily, it's about what goes on the chain / maximizing the anon set     

> __< k​ayabanerve:matrix.org >__ Ignoring that, if we do change Carrot, I do think we need multiple months of the finalized spec *and a full d/wallet-rpc* available.     

> __< j​effro256:monero.social >__ Agreed     

> __< s​yntheticbird:monero.social >__ multiple months ? more than 3-4 months ?     

> __< j​effro256:monero.social >__ Which is why it's nice that the code is mainly done     

> __< rbrunner >__ *smile*     

> __< k​ayabanerve:matrix.org >__ I'm not asking the final FCMP++ + Carrot (FCMP+++? FCMP#?) bins be available for three months (I'm unsure HF timelines). I'm asking the Carrot spec and bin be available for four.     

> __< j​effro256:monero.social >__ I will try to work out a first draft the formal doc by next MRL meeting if y'all think its a good idea     

> __< j​berman:monero.social >__ fcmp++ scanning for full wallets = keeping full paths in the tree saved locally, light wallet fcmp++ scanning = nothing really for legacy     

> __< k​ayabanerve:matrix.org >__ SyntheticBird: if it's public for one month, and I take a month to implement, the new monero-serai is available for 0 days prior to fork.     

> __< k​ayabanerve:matrix.org >__ I need to impl it, test it, have it audited, and release with my own distance to the fork.     

> __< k​ayabanerve:matrix.org >__ I can do that once I have a final spec and ref impl (even if unaudited with potential slight changes upcoming) but I do need that.     

> __< rbrunner >__ So, to put it a bit bluntly, with Serai you have one of those "custom implementations" on your hand     

> __< k​ayabanerve:matrix.org >__ jberman: I'd more call that tree management and think it's fine to say scanning an output, determining if you can spend it, would be Carrot for all FCMP++ TXs. We wouldn't even attempt the legacy scan protocol. I hear you if you want to note the FCMP++ pipeline re: scanning is more involved though.     

> __< rbrunner >__ Is the goal a public release of Serai together with the FCMP++ hardfork?     

> __< k​ayabanerve:matrix.org >__ rbrunner: and downstream consumers :D People like my work :D     

> __< rbrunner >__ Yes, yes :)     

> __< k​ayabanerve:matrix.org >__ But yes, and I do plan to follow the specification properly.     

> __< j​effro256:monero.social >__ jberman: TBF the light wallet servers themselves have to do the FCMP changes to the wallet. Most of the time the development of the LW clients and LWS is tightly couple / done by the same people     

> __< rbrunner >__ I just only now understand that yet one more ball is up in the air that may complicate things then     

> __< k​ayabanerve:matrix.org >__ I wouldn't shim it unless there was no other way to do it in a sufficiently timely fashion.     

> __< j​berman:monero.social >__ actually ... ! ... light wallet servers should do the same thing as full wallets when scanning, no? at least for legacy. I don't think light wallet impls need decoy paths at all. light wallet servers just keep full paths saved for all received outputs     

> __< j​berman:monero.social >__ (sorry slightly off topic)     

> __< k​ayabanerve:matrix.org >__ Re: timeline, that hasn't been the plan prior. I think Serai may beat FCMP++s.     

> __< rbrunner >__ If no Carrot derails the poor thing :)     

> __< j​berman:monero.social >__ anyway yes, I'm noting that tree management is distinct code necessary to scan for fcmp++'s, compared to code necessary for Carrot scanning     

> __< j​effro256:monero.social >__ jberman: true yeah as long as the LWS has access to a *trusted* daemon they can just trivially store paths in a databse yeah?     

> __< j​berman:monero.social >__ all this to say, Carrot isn't a trivial amount of code on top of fcmp++'s. all the more reason to make progress on it asap, but I'm still pretty iffy on rolling it out with fcmp++'s     

> __< k​ayabanerve:matrix.org >__ I'd rather just do burning bug + F-S.     

> __< k​ayabanerve:matrix.org >__ I'm not against Carrot if it's made accessible to review, implement, and test by devs not working on FCMP++ but I do share the concerns.     

> __< j​effro256:monero.social >__ AFAIK almost all full wallets in use *today* use `wallet2` for tx construction, correct?     

> __< j​berman:monero.social >__ afaik yep     

> __< j​effro256:monero.social >__ So it's mainly light wallet codebases that would need explicit updating?     

> __< k​ayabanerve:matrix.org >__ I'm right here :(     

> __< j​berman:monero.social >__ sending to the new addresses will probably require some trivial changes too     

> __< k​ayabanerve:matrix.org >__ My codebase would need explicit updating :(     

> __< j​effro256:monero.social >__ I know I know !! lol     

> __< j​effro256:monero.social >__ Not to exclude kayaba....     

> __< j​effro256:monero.social >__ I was just trying to think of other more obscure wallets     

> __< j​effro256:monero.social >__ That don't use `wallet2`     

> __< k​ayabanerve:matrix.org >__ Ledger has on-device scanning     

> __< k​ayabanerve:matrix.org >__ Trezor has a python reimpl of sending     

> __< j​berman:monero.social >__ also UI changes for handling the new addresses. e.g. let's say no UI changes are made, then you recover a seed that has received to a new address     

> __< j​effro256:monero.social >__ Wdym by "new addresses" here? Jamtis or regenerated Cryptonote-style addresses?     

> __< j​effro256:monero.social >__ Sending is exactly the same for old/new Cryptonote addresses     

> __< j​berman:monero.social >__ true trezor reimplemented wallet2, forgot that     

> __< j​effro256:monero.social >__ Scanning is slightly different if you use a new address with OVKs     

> __< j​berman:monero.social >__ Jamtis generated addresses = new addresses     

> __< j​berman:monero.social >__ I'm thinking I will await your spec and think on it more then     

> __< j​effro256:monero.social >__ For Jamtis addresses, weren't we going to use a different seed format anyways (Polyseed)?     

> __< j​effro256:monero.social >__ That would signal to the wallet which type of scanning to do     

> __< j​effro256:monero.social >__ But Trezor / Ledger DO have their own seed formats...     

> __< j​berman:monero.social >__ Feather and Cake (not sure of others in production) support polyseed today     

> __< j​effro256:monero.social >__ I did not know that. That makes the UI problems hairier     

> __< j​effro256:monero.social >__ Is there not a "Jamtis" flag bit in the Polyseed specs?     

> __< j​berman:monero.social >__ probably would make sense for there to be one     

> __< j​effro256:monero.social >__ Okay just looked I don't think it's in there explicitly, maybe tevadoe mentioned it at some point... this is probably a good application for those feature bits     

> __< j​effro256:monero.social >__ As long as we make sure production wallets today aren't already using them for vendor specific things     

> __< j​effro256:monero.social >__ BTW thanks everyone for all the helpful input! 


# Action History
- Created by: Rucknium | 2024-07-24T14:58:03+00:00
- Closed at: 2024-08-07T14:40:03+00:00
