---
title: Monero Research Lab Meeting - Wed 09 November 2022
source_url: https://github.com/monero-project/meta/issues/750
author: Rucknium
assignees: []
labels: []
created_at: '2022-11-08T15:35:27+00:00'
updated_at: '2024-04-02T17:20:05+00:00'
type: issue
status: closed
closed_at: '2022-11-14T21:17:42+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss [Jamtis address checksums](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#748 

# Discussion History
## UkoeHB | 2022-11-09T18:11:57+00:00
`[11-09-2022 17:00:04] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/750`
`[11-09-2022 17:00:04] <UkoeHB> 1. greetings`
`[11-09-2022 17:00:04] <UkoeHB> hello`
`[11-09-2022 17:00:29] <one-horse-wagon[> Hello.`
`[11-09-2022 17:00:31] <SerHack> hi`
`[11-09-2022 17:00:34] <rbrunner> Hi`
`[11-09-2022 17:00:52] <Rucknium[m]> Hi`
`[11-09-2022 17:00:57] <dangerousfreedom> Hello`
`[11-09-2022 17:02:04] <plowsof> hi`
`[11-09-2022 17:02:46] <UkoeHB> 2. updates, what's everyone working on?`
`[11-09-2022 17:03:54] <rbrunner> Still busy writing issues about various aspects of the Seraphis wallet to build: https://github.com/seraphis-migration/wallet3/issues`
`[11-09-2022 17:04:11] <rbrunner> And of course preparing our first regular working group meeting: https://github.com/monero-project/meta/issues/751`
`[11-09-2022 17:04:42] <rbrunner> All interested parties welcome, and of course let the comments flow for the issues :)`
`[11-09-2022 17:05:14] <UkoeHB> me: completed legacy integration to seraphis multisig, legacy spending is now fully supported by the seraphis library (hurray!); also added/adding error reporting to multisig utilities so it's easier to identify problems (for UX this means it's easier to identify which signers you need to get particular messages from, for security this means identifying malicious signers in some contexts); then, on to seraphis coinbase `
`[11-09-2022 17:05:14] <UkoeHB> txs which is the final piece I plan to work on`
`[11-09-2022 17:05:24] <plowsof>  i plan to first obtain an audit of the bp++ eprint paper. I have received 2 quotes to date.  `
`[11-09-2022 17:05:24] <dangerousfreedom> I'm working on opening a jamtis/seraphis wallet compatible with the wallet2. Maybe I will have something to present next week.`
`[11-09-2022 17:05:24] <plowsof> Quarkslab estimate around 12 days of work with a daily rate of 2’370 USD tax excluded ~$28,440 (including the deliverable edition and project management). Unavailable until Q2 2023.`
`[11-09-2022 17:05:25] <plowsof> CypherStack estimate the same time frame but for a total cost of $16,500 and are available to start next month. `
`[11-09-2022 17:06:54] <Rucknium[m]> plowsof: How do the firms define "audit"? What tasks does it involve?`
`[11-09-2022 17:07:12] <UkoeHB> plowsof: did you also ask for a proof of concept implementation? https://libera.monerologs.net/monero-research-lab/20221026#c153793`
`[11-09-2022 17:08:11] <plowsof> Quarkslab where unable to quote for a PoC and would need to complete task 1 first to gauge how long it would take. These are estimates `
`[11-09-2022 17:10:57] <plowsof> " theoretical review of your eprint paper with a focus on the security aspects"`
`[11-09-2022 17:12:24] <Rucknium[m]> Do you happen to know if they have any public examples? A paper and then their review of it side-by-side?`
`[11-09-2022 17:13:25] <plowsof> i do not, i will do more probing. theyve only just got back to me with these daily rates/estimates `
`[11-09-2022 17:13:39] <UkoeHB> How about this. 1) paper review + proof of concept from CypherStack Q4 2022, 2) me: proof of concept -> full implementation Q1 2023, 3) paper review + implementation audit from Quarkslab (+ one or two more implementation audits, possibly going back to CypherStack for this) in Q2-Q4 2023.`
`[11-09-2022 17:15:48] <Rucknium[m]> Sounds Ok to me. Where is the original author in all of this?`
`[11-09-2022 17:15:50] <plowsof> i will get the wheels in motion for 1) (funding firstly) `
`[11-09-2022 17:16:01] <UkoeHB> 3. discussion (updates are over)`
`[11-09-2022 17:17:00] <UkoeHB> Rucknium[m]: I'll contact him with our plan one it gets moving`
`[11-09-2022 17:17:05] <UkoeHB> once*`
`[11-09-2022 17:20:28] <UkoeHB> any other comments on BP++?`
`[11-09-2022 17:21:43] <UkoeHB> ok we can move on to jamtis address checksums: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#64-checksum`
`[11-09-2022 17:21:44] <one-horse-wagon[> <Rucknium[m]> "plowsof: How do the firms define..." <- Very good question that I would like to see answered also.`
`[11-09-2022 17:22:37] <UkoeHB> the questions with checksums are: what algorithm to use? is it good or bad to have error correction?`
`[11-09-2022 17:23:31] <SerHack> always good`
`[11-09-2022 17:23:35] <rbrunner> So that's double the number of checksum bytes compared with today`
`[11-09-2022 17:23:54] <rbrunner> 8 instead of 4`
`[11-09-2022 17:24:08] <UkoeHB> I'm a little uncertain about error correction, it seems like it might be abusable (generate an address that looks like another address but error corrects to something else).`
`[11-09-2022 17:24:17] <Rucknium[m]> To clarify, this would all be wallet-level, right? I assume that address checksums are not possible at the blockchain consensus level.`
`[11-09-2022 17:25:04] <UkoeHB> Rucknium[m]: yes for wallets`
`[11-09-2022 17:26:16] <rbrunner> Error correction as a base-level wallet feature also could lead to all sorts of UI/UX complications.`
`[11-09-2022 17:26:42] <rbrunner> Maybe have error correction, but only offering it through a special tool, to be used in "emergencies", for recovery so to say?`
`[11-09-2022 17:27:15] <Rucknium[m]> FWIW, here's the Bitcoin Cash recommendation on error correction: https://github.com/bitcoincashorg/bitcoincash.org/blob/master/spec/cashaddr.md#error-correction`
`[11-09-2022 17:27:31] <Rucknium[m]> "BCH codes allows for error correction. However, it is strongly advised that error correction is not done in an automatic manner as it may cause funds to be lost irrecoverably if done incorrectly. It may however be used to hint a user at a possible error."`
`[11-09-2022 17:27:36] <UkoeHB> I think we should avoid conditional behavior of address strings. Better to have one format that does the same thing always.`
`[11-09-2022 17:28:11] <UkoeHB> Rucknium[m]: that's a good recommendation`
`[11-09-2022 17:28:40] <UkoeHB> but you don't need error correction for that, you just need a checksum`
`[11-09-2022 17:28:50] <rbrunner> "conditional behavior" What do you mean with this?`
`[11-09-2022 17:29:39] <UkoeHB> rbrunner: I mean addresses that deserialize to different things in different settings`
`[11-09-2022 17:29:48] <UkoeHB> based on whether or not you error correct`
`[11-09-2022 17:31:02] <UkoeHB> better to just have a try_deserialize() that internally calls is_corrupted()`
`[11-09-2022 17:32:10] <rbrunner> Not yet sure where those arguments lead regarding UI and whether we could/should offer some "address recovery tool" or not`
`[11-09-2022 17:33:03] <UkoeHB> for UI you just paste an address and it tells you 'this is an invalid address [(optional) because of reason X]'`
`[11-09-2022 17:33:12] <dangerousfreedom> I think error correction adds a layer of possible problems that we want to avoid. A checksum should be enough to say if there is a mistake in the address and if there is the user could check the address himself. If we use error correction, there might be a case where it does not do its job and if the transfer happens the funds would be lost.`
`[11-09-2022 17:34:04] <one-horse-wagon[> dangerousfreedom: agree with you completely.`
`[11-09-2022 17:34:07] <rbrunner> Is the chance of a false alarm of a checksum algorithm significantly lower than the chance of error correction failing?`
`[11-09-2022 17:35:00] <UkoeHB> rbrunner: don't think so`
`[11-09-2022 17:35:38] <dangerousfreedom> Depends on how much bytes you want to use to ensure it I guess`
`[11-09-2022 17:35:47] <UkoeHB> 8 bytes means a 64bit hash, which should have negligible failure rates for non-malicious addresses`
`[11-09-2022 17:36:23] <rbrunner> Then I ask myself what we risk if we only permit error correction in carefully designed and very clear contexts, like a dedicated recovery tool`
`[11-09-2022 17:36:26] <dangerousfreedom> Is there a limitation on the address string that we want to use?`
`[11-09-2022 17:36:36] <dangerousfreedom> Currently we are targetting a 181 characters for normal addresses`
`[11-09-2022 17:36:46] <rbrunner> Maybe that some wallet dev starts to add error correction nevertheless directly to an app ...`
`[11-09-2022 17:36:57] <UkoeHB> rbrunner: it's only carefully designed and clear in the tools that you write`
`[11-09-2022 17:38:13] <rbrunner> The saying "That's we cannot have nice things come to mind". Technically, we could do better than just moaning "Wrong!", but it's risky`
`[11-09-2022 17:38:32] <rbrunner> *That's why we`
`[11-09-2022 17:39:04] <rbrunner> Annoying, in a way`
`[11-09-2022 17:40:40] <UkoeHB> it's interesting that tevador says "The checksum can detect all errors affecting 4 or fewer characters", so there may be some advantage to using a polynomial solution instead of a hash. This way malicious addresses that only change a few characters will be detected if you can validate the checksum. On that note the checksum should probably be ordered first in the address string so users are more likely to memorize it.`
`[11-09-2022 17:40:51] <Rucknium[m]> Most software companies: "If it works, ship it!" Reminds me of the thousands of Monero transactions that all use the same outputs as decoys, revealing the real spend.`
`[11-09-2022 17:41:27] <rbrunner> Maybe people producing errors in addresses will become a less and less realistic scenario anyway; QR codes for example checksum themselves`
`[11-09-2022 17:41:48] <rbrunner> And who types 181 characters?`
`[11-09-2022 17:45:17] <rbrunner> Is there a way to estimate how many wrong characters a hash can "detect"?`
`[11-09-2022 17:45:34] <UkoeHB> rbrunner: it detects 1 wrong character with the same probability as 1000`
`[11-09-2022 17:47:32] <rbrunner> We already have hashes implemented, right, but those polynoms would have to get added?`
`[11-09-2022 17:47:46] <UkoeHB> right`
`[11-09-2022 17:48:29] <rbrunner> Well, we have versioning now for addresses, so we could very well start with hashes and see how that goes, and if the dust settled talk again about error correctio as a possible improvement`
`[11-09-2022 17:49:02] <UkoeHB> agreed, it's a fairly easy piece to switch out`
`[11-09-2022 17:49:12] <rbrunner> "now" = "with Seraphis" of course`
`[11-09-2022 17:50:31] <rbrunner> I think I move towards dangerousfreedom's viewpoint: "I think error correction adds a layer of possible problems that we want to avoid."`
`[11-09-2022 17:50:48] <rbrunner> At least for the first version of Seraphis and Jamtis`
`[11-09-2022 17:51:19] <UkoeHB> "Maybe people producing errors in addresses will become a less and less realistic scenario anyway" -> I agree, manually validating a long string is just not reasonable. It's really up to the ecosystem to make address passing robust and automated.`
`[11-09-2022 17:51:27] <dangerousfreedom> <rbrunner> "And who types 181 characters?" <- Yeah, I think that's the point nobody will make mistakes by typing it but copying mistakes may occur. A checksum would certainly detect that and the person would need to copy again the address. With error correction on the other hand might be a bit more comfortable if you miss one character but I still dont know if it is worth the risk of having it corrected to a wrong`
`[11-09-2022 17:51:27] <dangerousfreedom> address. I also dont know if this assumption is valid since you have checksum + error correction and if it passes both than you can be sure that the address is correct. Now I'm confused if I generalize my thought to an address with 1000 characters for example. Maybe error correction + checksum makes sense there.`
`[11-09-2022 17:52:04] <moneromoooo> In what case(s) would an EC mechanism would yield an unwanted address where a checksum would not ?`
`[11-09-2022 17:52:21] <rbrunner> Copying errors are probably mostly "not copying all", and there no error correction helpls. E.g. you copy only 170 characters or so.`
`[11-09-2022 17:52:28] <UkoeHB> moneromoooo: EC mechanism?`
`[11-09-2022 17:52:41] <hyc> error correction`
`[11-09-2022 17:52:44] <moneromoooo> I mean error correction vs checksum/hash.`
`[11-09-2022 17:52:46] <UkoeHB> oh error correction (not elliptic curve)`
`[11-09-2022 17:53:05] <moneromoooo> An actuve attacker will set both to what advantages them.`
`[11-09-2022 17:53:05] <hyc> ECC seems like overkill here`
`[11-09-2022 17:53:17] <hyc> and again, not useful if you just incompletely copy the string\`
`[11-09-2022 17:53:40] <UkoeHB> error correction means post-processing the address to 'fix' it, which means an error-correctable string really has two addresses within it depending if you error correct or not`
`[11-09-2022 17:53:54] <UkoeHB> a checksum is just pass/fail`
`[11-09-2022 17:54:14] <hyc> but for example, a classical ECC mech on a 32 or 64bit word can detect 2 bit errors and correct all 1-bit errors`
`[11-09-2022 17:54:25] <hyc> if there are more than 2 wrong bits, you're on your own`
`[11-09-2022 17:54:41] <rbrunner> Just re-displaying the corrected address in a wallet in a way that makes patently clear what was corrected is a challenge`
`[11-09-2022 17:54:54] <moneromoooo> Well the amount of redundant data is a tradeoff you can choose.`
`[11-09-2022 17:55:15] <moneromoooo> And, IIRC, scales fairly well for longer strings.`
`[11-09-2022 17:55:29] <moneromoooo> (meaning sublinear)`
`[11-09-2022 17:55:34] <hyc> true`
`[11-09-2022 17:55:59] <hyc> but I don't think anyone has a good idea of the threat model being protected against here`
`[11-09-2022 17:56:07] <one-horse-wagon[> Instead of typing out the entire 181 character address every time, couldn't the address when first created, have a simple nickname in your wallet that would then reference the complete address?`
`[11-09-2022 17:56:52] <one-horse-wagon[> Or even a sequential number if you are going to have many addresses`
`[11-09-2022 17:57:19] <rbrunner> Hmm, yes, but making that easy is a different problem, seems to me. We are talking about getting the 181 characters in correctly in the first place`
`[11-09-2022 17:57:54] <dangerousfreedom> hyc: True. Is anyone aware about complaints so far about the current model? Which is a simple checksum using Keccak?`
`[11-09-2022 17:57:57] <merope> some wallets already have an addressbook feature, but it doesn't help when you're copy pasting an address you've received (or when you want to send it to someone else)`
`[11-09-2022 17:58:35] <rbrunner> Can't remember any reported problems.`
`[11-09-2022 17:58:47] <hyc> seems to me those are all interactive situations`
`[11-09-2022 17:58:59] <moneromoooo> EC is really for unreliable data transmission, not defence vs active attacks.`
`[11-09-2022 17:59:01] <hyc> in which case it's perfectly fine to just checksum, say "this is wrong, try again"`
`[11-09-2022 17:59:02] <UkoeHB> Let's say an attacker wants to replace your address with something that looks similar but sends funds to the attacker. The attacker needs to generate an address that converts to a similar base58 string, but that probably takes many 'erroneous' characters to get right even with a lot of work. Therefore a checksum is superior because for large numbers of errors it has the same detection probability, whereas an error `
`[11-09-2022 17:59:02] <UkoeHB> correction polynomial apparently has lower detection rates for large numbers of errors (given the same checksum bit length).`
`[11-09-2022 17:59:24] <moneromoooo> Or unreliable store/retrieveal.`
`[11-09-2022 18:00:05] <moneromoooo> I suspect that'll only work if the address has *lots* of redundancy info in.`
`[11-09-2022 18:00:39] <hyc> it seems to me that a checksum is all that is necessary and sufficient here`
`[11-09-2022 18:00:43] <UkoeHB> If an attacker wants to replace your address with a burn address, then neither checksums nor error correction will be very useful (for long strings that can't be fully validated visually, which we are dealing with).`
`[11-09-2022 18:00:50] <rbrunner> Usually attackers nowadays just ask "Buy my NFT" and people send their XMR already over :)`
`[11-09-2022 18:02:10] <Rucknium[m]> https://www.reddit.com/r/Monero/comments/y8xmph/psa_weve_discovered_malware_that_replaces_the/`
`[11-09-2022 18:02:34] <Rucknium[m]> Would error correction make this attack easier? `
`[11-09-2022 18:02:54] <hyc> no impact`
`[11-09-2022 18:02:54] <rbrunner> Right, but as far as I remember that was blunt replacement with a completey different address, just silently / invisibly`
`[11-09-2022 18:03:14] <rbrunner> because implemented as a browser extension`
`[11-09-2022 18:03:22] <rbrunner> that can do such things`
`[11-09-2022 18:03:56] <rbrunner> So, no help from any checks, I would say`
`[11-09-2022 18:05:03] <rbrunner> So down with polynoms, we already are busy enough coding mountains of other code for Seraphis, no?`
`[11-09-2022 18:05:04] <UkoeHB> dangerousfreedom: I'd tentatively go for a checksum (we can revisit this as needed). You can use the seraphis hashing interface to access blake2b, which is faster than keccak.`
`[11-09-2022 18:06:01] <dangerousfreedom> UkoeHB: Ok. Great. I agree with everyone's answers too.`
`[11-09-2022 18:06:35] <UkoeHB> we are overtime on the meeting, but are there any other topics people wanted to cover before we wrap it up?`
`[11-09-2022 18:06:45] <plowsof> reg bp++ "audit": The deliverable is our (CypherStack) write-up which will include recommendations, notes, weaknesses, and issues (if any) of the BP++ paper. `
`[11-09-2022 18:09:46] <UkoeHB> plowsof: thanks`
`[11-09-2022 18:09:57] <UkoeHB> ok that's the end of the meeting, thanks for attending everyone`
`[11-09-2022 18:09:59] <dangerousfreedom> UkoeHB: Not from my side. Thanks Koe.`

# Action History
- Created by: Rucknium | 2022-11-08T15:35:27+00:00
- Closed at: 2022-11-14T21:17:42+00:00
