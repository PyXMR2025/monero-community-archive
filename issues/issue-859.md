---
title: Monero Research Lab Meeting - Wed 05 July 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/859
author: Rucknium
assignees: []
labels: []
created_at: '2023-07-05T00:34:57+00:00'
updated_at: '2023-07-11T23:31:36+00:00'
type: issue
status: closed
closed_at: '2023-07-11T23:31:36+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: Reducing 10 block lock: https://github.com/monero-project/research-lab/issues/102#issuecomment-1577827259

3. Discuss: [Exploring Trustless zk-SNARKs for Monero's payment protocol](https://github.com/monero-project/research-lab/issues/100). What are the bottlenecks for potential implementation?

4. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

5. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

6. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#853 

# Discussion History
## UkoeHB | 2023-07-05T18:12:14+00:00
`[07-05-2023 17:00:37] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/859`
`[07-05-2023 17:00:37] <UkoeHB> 1. greetings`
`[07-05-2023 17:00:37] <UkoeHB> hello`
`[07-05-2023 17:01:00] <gingeropolous> hi`
`[07-05-2023 17:01:02] <rbrunner> Hello`
`[07-05-2023 17:01:45] <jberman[m]> Hello`
`[07-05-2023 17:01:51] <Rucknium[m]> Hi`
`[07-05-2023 17:01:56] <vtnerd>  hi`
`[07-05-2023 17:04:26] <UkoeHB> 2. discussion, what is everyone working on?`
`[07-05-2023 17:05:06] <kayabanerve[m]> 👋`
`[07-05-2023 17:05:13] <vtnerd> rmq support for lws (completed), and noise protocol for daemon p2p`
`[07-05-2023 17:05:57] <Rucknium[m]> me: The OSPEAD estimator should get closer to the true value as N increases, but when I push the number of rings from 200,000 to one million its accuracy seems to plateau. I am troubleshooting this.`
`[07-05-2023 17:06:52] <Rucknium[m]> Research community resources: WIKINDX, which powers moneroresearch.info , is going to enable "AND" as default in QuickSearch by my request. That's a small step toward better search for users: https://sourceforge.net/p/wikindx/discussion/888681/thread/1fcdd20630/`
`[07-05-2023 17:06:53] <kayabanerve[m]> I jotted down some theoretical improvements to FCMPs, but nothing much on my end.`
`[07-05-2023 17:07:03] <gingeropolous> i think i've finally made 100% of the available silicon in the research computing cluster accessible for R&D (280 threads total). random reminder that the resource is available for anyone who would find it useful.`
`[07-05-2023 17:07:05] <UkoeHB> me: I spent a short time working on the eclib abstraction before concluding that the project of switching everything to a new curve is too immense on every dimension (at least for me to handle). I am now on hiatus from Monero work, so someone else should start leading the meetings.`
`[07-05-2023 17:07:17] <jberman[m]> Me: no update on my end, just returned from traveling. Looking to start making headway on full chain membership proof integration over the next week`
`[07-05-2023 17:07:24] <Rucknium[m]> I am working on an API to integrate the MAGIC Monero Fund's fundraisers (monerofund.org) into Feather Wallet like CCS fundraisers are.`
`[07-05-2023 17:08:16] <kayabanerve[m]> gingeropolous @gingeropolous:libera.chat: How much storage is available?`
`[07-05-2023 17:08:33] <gingeropolous> 14TB SSD, 74TB HDD`
`[07-05-2023 17:08:57] <vtnerd> gotta run, sadly`
`[07-05-2023 17:09:03] <Rucknium[m]> To be blunt: Is it a good idea to use CCS funds to work on software where we don't know if the Curve Trees protocol is secure yet? Or is this part of the SeraiDEX labor exchange?`
`[07-05-2023 17:09:11] <UkoeHB> thanks for the update vtnerd `
`[07-05-2023 17:09:12] <kayabanerve[m]> I may ask to generate and store a couple hundred GB data set in the future...`
`[07-05-2023 17:09:58] <kayabanerve[m]> Rucknium @rucknium:monero.social: The Serai "labor exchange" only went up to a post I made months ago on GH.`
`[07-05-2023 17:11:23] <kayabanerve[m]> Further contributions by jberman have been at my financial guarantee. All code has been done by my effective volunteering so far, though I do plan a CCS for past and one for future, with its timeliness paid for by a distinct exchange I made with jberman @jberman:matrix.org`
`[07-05-2023 17:12:29] <kayabanerve[m]> As for if the CCS should host it... I don't see how it's distinct from anything it funds under Seraphis. This work explicitly delineates where it's unproven, and seeks said proofs with an explicit issue tracker. Part of the CCS would be to ensure its security.`
`[07-05-2023 17:12:31] <UkoeHB> 3. discussion, what to discuss today?`
`[07-05-2023 17:13:08] <kayabanerve[m]> While it isn't guaranteed to be deployed, as Seraphis effectively is, I don't see a world in which we don't transition from either CLSAG or Grootle to it.`
`[07-05-2023 17:13:41] <Rucknium[m]> Ok. I have also brought up the same issue about Seraphis for months. Maybe a year. We need security proofs.`
`[07-05-2023 17:13:56] <kayabanerve[m]> Or if not this exact impl, the same underlying theory with the same underlying research which is currently optimal.`
`[07-05-2023 17:14:03] <Rucknium[m]> Triptych has security proofs published in a peer-reviewed outlet.`
`[07-05-2023 17:14:58] <Rucknium[m]> I see a world: It's not proven secure.`
`[07-05-2023 17:15:10] <Rucknium[m]> Proofs are hard`
`[07-05-2023 17:15:30] <ofrnxmr[m]> kayabanerve[m]: Ccs is fine`
`[07-05-2023 17:15:42] <kayabanerve[m]> Sure. Part of further efforts on this work is ensuring security. I promise you it's tracked and important to me. I don't believe questioning if the CCS should fund it is appropriate when part of the CCS funding would be to prove the security. If you're unhappy with the timeline on the CT work, believing specific security sections should be done sooner than latter, I'd ask you to call that out on specific proposals. Not`
`[07-05-2023 17:15:42] <kayabanerve[m]> question CCS funding entirely.`
`[07-05-2023 17:16:54] <UkoeHB> kayabanerve[m]: CT historically means Confidential Transactions, maybe a different abbreviation would be better (or just don't abbreviate)`
`[07-05-2023 17:17:02] <Rucknium[m]> I was asking about jberman's current CCS work, not a future one. Of course, work priority can change in the course of a CCS. But proposed priority changes can be given feedback here`
`[07-05-2023 17:17:31] <gingeropolous> ah, is it curve trees?`
`[07-05-2023 17:17:36] <ofrnxmr[m]> Oh i was referring to future kaya ccs'`
`[07-05-2023 17:17:51] <UkoeHB> gingeropolous: yeah`
`[07-05-2023 17:17:58] <Rucknium[m]> I would love to see a CCS that funds work on security proofs for...anything we have on the table. That includes Seraphis, BP++, and Curve Trees.`
`[07-05-2023 17:18:40] <UkoeHB> BP++ already has a CCS for review of the paper that hasn't been fully published yet`
`[07-05-2023 17:19:15] <kayabanerve[m]> Rucknium[m]: Ah, sorry, missed that context.`
`[07-05-2023 17:19:19] <Rucknium[m]> There's no security proof in that paper. Can't review what's not there`
`[07-05-2023 17:19:29] <kayabanerve[m]> UkoeHB: Thanks for the reminder`
`[07-05-2023 17:19:58] <Rucknium[m]> This isn't a theoretical risk. A zero-knowledge protocol was recently discovered to be flawed: https://www.zksecurity.xyz/blog/posts/nova-attack/`
`[07-05-2023 17:20:03] <jberman[m]> plowsof @plowsof:libera.chat is currently on the hunt to find a suitable party to do security proofs for Seraphis`
`[07-05-2023 17:20:28] <kayabanerve[m]> Rucknium @rucknium:monero.social: Agreed re: Seraphis.`
`[07-05-2023 17:20:28] <kayabanerve[m]> Right now, Sarang, funded by Firo, is working on the VC scheme as their hours allow. That'd include a proof.`
`[07-05-2023 17:21:26] <Rucknium[m]> Can you type out your acronyms? VC?`
`[07-05-2023 17:21:26] <kayabanerve[m]> *that second part is referring to ensuring the security of curve trees which requires BP(+) be modified with a vector commitment scheme.`
`[07-05-2023 17:21:34] <Rucknium[m]> Ok`
`[07-05-2023 17:23:11] <Rucknium[m]> That's good. Recently I've seen carts being put before horses and all problems looking like nails when we all we have is hammers.`
`[07-05-2023 17:24:33] <gingeropolous> what materials would an individual need that was going to embark on security proofs on seraphis?`
`[07-05-2023 17:25:08] <gingeropolous> for Seraphis. `
`[07-05-2023 17:25:17] <UkoeHB> just the papers https://github.com/UkoeHB/Seraphis`
`[07-05-2023 17:25:31] <Rucknium[m]> IIRC part of koe's current CCS is to get the Seraphis paper to a place where someone could continue the work into writing security proofs`
`[07-05-2023 17:25:44] <gingeropolous> thanks UkoeHB .`
`[07-05-2023 17:26:03] <UkoeHB> Rucknium[m]: I already did it`
`[07-05-2023 17:26:04] <kayabanerve[m]> Rucknium @rucknium:monero.social: I asked Firo to collaborate, noting specifically the VC scheme and proof, over a month ago. `
`[07-05-2023 17:26:43] <kayabanerve[m]> Just to clarify that as we've had theoretic changes, I have followed up re: security. I didn't do this whole thing and then say we'll get security later.`
`[07-05-2023 17:27:02] <UkoeHB> gingeropolous: there are also coinstudent2048's writeups which may be a useful reference/head start https://github.com/coinstudent2048/writeups`
`[07-05-2023 17:27:06] <Rucknium[m]> UkoeHB: Great. What is the next step? I assume sarang would be a good person to write the proofs, if he would be willing, since his work with Firo has some similarities.`
`[07-05-2023 17:27:29] <UkoeHB> Rucknium[m]: like jberman[m] said, plowsof is already looking for suitable parties`
`[07-05-2023 17:30:58] <UkoeHB> ok are there any other topics? otherwise we can wrap it up`
`[07-05-2023 17:31:14] <gingeropolous> the agenda had that 10 block lock thing ....`
`[07-05-2023 17:32:39] <Rucknium[m]> kayabanerve: Do you think the 10 blocks can be reduced with Curve Trees? The threat model would be different than a decoy-based model when there are deep re-orgs.`
`[07-05-2023 17:32:42] <UkoeHB> 10 block lock is not something that should be hyper-optimized. If you reduce it too much, that might open the floodgates to attacks.`
`[07-05-2023 17:34:09] <Rucknium[m]> Myself and another researcher may look into the privacy issues with Monerujo's PocketChange (and similar application-level ways to deal with 10 block lock).`
`[07-05-2023 17:34:28] <kayabanerve[m]> Rucknium @rucknium:monero.social: Arguably? But it's indirect.`
`[07-05-2023 17:34:29] <UkoeHB> Rucknium[m]: 10 block lock mitigates the case where a reorg invalidates txs unaffiliated with the reorger`
`[07-05-2023 17:34:52] <kayabanerve[m]> With a merkle tree structure, you can choose a root from 10 blocks ago or choose the most recent root.`
`[07-05-2023 17:34:56] <kayabanerve[m]> (If we allow it (`
`[07-05-2023 17:35:22] <UkoeHB> reorgs would be much more impactful if txs used full chain membership proofs, not less impactful`
`[07-05-2023 17:35:28] <kayabanerve[m]> If you choose the most recent root, you're at risk of reorg, and you dox you're spending something from the last ten blocks`
`[07-05-2023 17:35:56] <kayabanerve[m]> BUT your privacy set is all of the last 10 blocks which is decent. That's the one benefit`
`[07-05-2023 17:36:09] <kayabanerve[m]> UkoeHB: AFAIK it's effectively the same.`
`[07-05-2023 17:36:10] <Rucknium[m]> the 10 lock lock prevents some adversarial inference of the true spend in a decoy model. AFAIK, there isn't really that problem with Curve Trees, except maybe that your wallet is using the most updated merkle tree at X most recent block height`
`[07-05-2023 17:36:11] <gingeropolous> yeah. it might be that for "select membership proofs" (of which current and seraphis are parts) might just need that 10 block lock, but perhaps the new general membership proofs don't need it`
`[07-05-2023 17:36:29] <kayabanerve[m]> You used to reorg if decoys shifted at all. Now you reorg if a tree root no longer exists.`
`[07-05-2023 17:36:44] <kayabanerve[m]> It's probably easier to detect if a TX is incompatible under merkle trees.`
`[07-05-2023 17:37:06] <UkoeHB> kayabanerve[m]: it is worse because a reorg will invalidate all txs referencing a merkle root above the reorg point. With ring sigs, you will only invalidate txs with ring members above the reorg point, which is likely to be some proportion of all reorged txs.`
`[07-05-2023 17:37:34] <Rucknium[m]> By default, won't all wallets use an updated merkle tree? So your true spend would not be able to be inferred`
`[07-05-2023 17:37:39] <kayabanerve[m]> ... Right but don't we heavily weight the most recent TXs? Isn't that likely?`
`[07-05-2023 17:37:53] <UkoeHB> Rucknium[m]: no, 10 block lock is a security measure not a privacy measure`
`[07-05-2023 17:38:00] <Rucknium[m]> tx invalidation is not the same as revealing the real spend. Different problems IMHO`
`[07-05-2023 17:38:06] <kayabanerve[m]> jberman @jberman:matrix.org: What are the odds a new TX has a ring member from the most recent 20 blocks?`
`[07-05-2023 17:38:17] <UkoeHB> kayabanerve[m]: yes but proportionally, merkle root invalidation is more impactful`
`[07-05-2023 17:38:19] <kayabanerve[m]> Doesn't the algorithm explicitly weight 10-25?`
`[07-05-2023 17:38:23] <Rucknium[m]> UkoeHB: That's not what you said in the GitHub issue about it`
`[07-05-2023 17:38:49] <kayabanerve[m]> UkoeHB: Marginally, sure.`
`[07-05-2023 17:39:05] <UkoeHB> marginally is all that matters here...`
`[07-05-2023 17:39:14] <UkoeHB> Rucknium[m]: link it...`
`[07-05-2023 17:39:58] <jberman[m]> Also on the margin, any decoys in your chosen ring could be invalidated and weaken your final chosen ring on chain`
`[07-05-2023 17:40:28] <Rucknium[m]> https://github.com/monero-project/research-lab/issues/95`
`[07-05-2023 17:40:31] <UkoeHB> jberman[m]: if you resubmit`
`[07-05-2023 17:40:57] <Rucknium[m]> > This weakens those users' ring signatures. To prevent that weakening, the 10-block-lock time is enforced. This way all decoys in a tx input are plausibly the real spend.`
`[07-05-2023 17:41:39] <Rucknium[m]> AFAIK, no other blockchain is paternalistic with the "tx invalidation" issue. Other blockchains allow users to determine the number of confirmations they accept`
`[07-05-2023 17:42:19] <kayabanerve[m]> Right, so FCMPs solve the privacy issues yet maintain reorg risk.`
`[07-05-2023 17:42:30] <UkoeHB> Rucknium[m]: https://github.com/monero-project/research-lab/issues/104#issuecomment-1186552665`
`[07-05-2023 17:42:34] <Rucknium[m]> A 51% attack for double spends has invalidated txs. That's the point.`
`[07-05-2023 17:42:43] <gingeropolous> FCMPs.....`
`[07-05-2023 17:42:50] <Rucknium[m]> kayabanerve: That's my hypothesis`
`[07-05-2023 17:42:55] <UkoeHB> privacy impact is an advantage, security is the original reason`
`[07-05-2023 17:43:06] <kayabanerve[m]> And anything spent within the most recent 10 blocks would definitively reveal it's within the most recent 10 blocks (if anything outside defaults to the 10 block old root)`
`[07-05-2023 17:43:24] <kayabanerve[m]> gingeropolous @gingeropolous:libera.chat: Full chain membership proofs.`
`[07-05-2023 17:44:01] <kayabanerve[m]> But, since it's a FCMP, those 10 blocks still probably exceed 128, right? And it's safe to re submit.`
`[07-05-2023 17:44:21] <kayabanerve[m]> Not to dismiss the reorg risk, to say privacy may be 'resolved'.`
`[07-05-2023 17:45:00] <gingeropolous> yeah i thought the main concern was privacy implications of the re-org, not the re-org itself`
`[07-05-2023 17:45:35] <jberman[m]> kayabanerve: I don't remember offhand but I would be mildly surprised if over 20% of txs have ring members from the last 20 blocks`
`[07-05-2023 17:45:53] <kayabanerve[m]> Regardless of original reasons, once we have FCMPs slated, we may want to re-evaluate privacy and security risks.`
`[07-05-2023 17:46:24] <kayabanerve[m]> Huh. I thought it'd be much higher. Never mind on my "marginally" then.`
`[07-05-2023 17:47:26] <UkoeHB> it's still marginal, the margin is just quite large`
`[07-05-2023 17:49:39] <Rucknium[m]> Yes. What is the benefit to an adversary of invalidating txs that they don't have the spend keys for (i.e. cannot perform a double-spend)? Just vandalism?`
`[07-05-2023 17:50:08] <kayabanerve[m]> DoS, yeah.`
`[07-05-2023 17:50:54] <kayabanerve[m]> I will note Zcash didn't implement a lock AFAIK and seems to do fine. I have no idea their root selection policy though (10 blocks back, 5 blocks, most recent...)`
`[07-05-2023 17:51:56] <UkoeHB> lack of an attack is not proof of security`
`[07-05-2023 17:53:30] <kayabanerve[m]> Agreed. It is potential evidence on the financial incentive to perform such DoSs though.`
`[07-05-2023 17:54:05] <Rucknium[m]> Curve Trees, if implemented, would have much less (if any?) privacy issues with a PocketChange implementation to get around the 10 block lock, so it has that to its advantage.`
`[07-05-2023 17:54:15] <rbrunner> If you can bring down a cryptocurrency with just filling blocks with large transactions, you don't anything sophisticated ...`
`[07-05-2023 17:54:23] <rbrunner> *you don't need`
`[07-05-2023 17:56:10] <gingeropolous> so FCMP could solve the 10 block lock issue either directly or indirectly ... ?`
`[07-05-2023 17:57:00] <gingeropolous> because I don't know if we'll ever have enough data to convince ourselves to lower it while using ringsigs (select membership proof). is there a better name for that, or just call it ring sigs?`
`[07-05-2023 17:57:11] <jberman[m]> Leaving a vector open to make Monero unusable via consistent 1-2 block reorgs wouldn't be great (for wallets that select from the most recent 1-2 blocks)`
`[07-05-2023 17:57:18] <gingeropolous> oh its only sending some of my message to matrix`
`[07-05-2023 17:57:26] <gingeropolous> so FCMP could solve the 10 block lock issue either directly or indirectly ... ?`
`[07-05-2023 17:58:36] <Rucknium[m]> Writing up the results from applying the Double Spend Races formula hasn't been a priority (doesn't seem time-sensitive), so I haven't done it. But what I've seen is that if the adversary has enough hashpower to re-org 5 blocks with non-negligible probability, then they have close to enough hashpower to re-org 10 blocks`
`[07-05-2023 17:59:27] <UkoeHB> imo the only real solution to 10-block-lock is allowing no-membership-proof inputs, but that is a contentious idea for sure`
`[07-05-2023 17:59:54] <kayabanerve[m]> Rucknium @rucknium:monero.social: I'm hearing we should raise to 100? /s`
`[07-05-2023 18:00:24] <Rucknium[m]> koe throwing a rabid chicken in there at the end. (I dont know what no-membership-proofs would imply)`
`[07-05-2023 18:00:43] <UkoeHB> ok that's the end of the hour, thanks for attending everyone :p`
`[07-05-2023 18:00:43] <kayabanerve[m]> FCMPs solves the privacy issues around allowing new output's to be used. It also solves the privacy on pocket change. It does nothing for security against reotgs. That's the summary.`
`[07-05-2023 18:01:06] <kayabanerve[m]> No privacy on spent output @ruckUkoeHB `
`[07-05-2023 18:01:15] <kayabanerve[m]> * Rucknium @rucknium:monero.social: `
`[07-05-2023 18:01:29] <kayabanerve[m]> No idea how my phone butchered that so much, sorry`
`[07-05-2023 18:03:16] <jberman[m]> gingeropolous @gingeropolous:libera.chat: and PocketChange doesn't fully solve the 10 block lock issue 1) when on boarding would still have to wait 10 blocks, and 2) you have to have enough "pocket change" leftover to make another follow-up tx`
`[07-05-2023 18:04:22] <jberman[m]> "Mythical L2" is also another avenue :)`

# Action History
- Created by: Rucknium | 2023-07-05T00:34:57+00:00
- Closed at: 2023-07-11T23:31:36+00:00
