---
title: Monero Research Lab Meeting - Wed 23 November 2022
source_url: https://github.com/monero-project/meta/issues/757
author: Rucknium
assignees: []
labels: []
created_at: '2022-11-22T16:00:07+00:00'
updated_at: '2022-11-29T15:02:23+00:00'
type: issue
status: closed
closed_at: '2022-11-29T15:02:23+00:00'
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

#755 

# Discussion History
## UkoeHB | 2022-11-23T18:11:32+00:00
`[11-23-2022 17:00:13] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/757`
`[11-23-2022 17:00:13] <UkoeHB> 1. greetings`
`[11-23-2022 17:00:13] <UkoeHB> hello`
`[11-23-2022 17:00:32] <one-horse-wagon[> Hello`
`[11-23-2022 17:00:36] <rbrunner> Hi`
`[11-23-2022 17:00:39] <vtnerd> hi`
`[11-23-2022 17:00:42] <tevador> Hi`
`[11-23-2022 17:00:56] <jberman[m]> hello`
`[11-23-2022 17:01:03] <jeffro256[m]> howdy`
`[11-23-2022 17:01:10] <Rucknium[m]> Hi`
`[11-23-2022 17:01:10] <plowsof> hi`
`[11-23-2022 17:02:14] <UkoeHB> 2. updates, what's everyone working on?`
`[11-23-2022 17:02:48] <vtnerd> Ive been IT work unfortunately, a multi-system meltdown over here`
`[11-23-2022 17:02:55] <vtnerd> good news is that two laptops still work`
`[11-23-2022 17:03:28] <vtnerd> more guidance on my haskell->c++ bp++ port next week hopefully`
`[11-23-2022 17:03:48] <Rucknium[m]> Looking into how the dynamic block size + fees work. Translated spackle_xmr 's Python simulation code to R.`
`[11-23-2022 17:04:05] <jeffro256[m]> Working on how best to do community node selection`
`[11-23-2022 17:04:34] <jberman[m]> Stress testing daemons when hit with lots of txs, almost done setting up the framework. Then moving over to Seraphis input selection which I've started to look into a bit more`
`[11-23-2022 17:04:39] <jeffro256[m]> vtnerd you're working on a haskell port of bp++?`
`[11-23-2022 17:05:20] <vtnerd> no theres an existing bp++ in haskell that needs to be c++ or some suitable language for the monero daemon`
`[11-23-2022 17:06:16] <UkoeHB> me: I finished all the seraphis lib multisig work. The last feature added is a method demoing how to fully validate a multisig tx proposal so you can know with very high confidence if a multisig tx proposal is destined to fail or not (alternatively: destined to succeed if you have an honest subgroup that doesn't necessarily include the proposer). This method is kind of a capstone feature of the library that is only `
`[11-23-2022 17:06:16] <UkoeHB> possible due to many design decisions. Now I am in the middle of adding a coinbase tx type, which is the final component of the library before I stop writing code and move on to other things (e.g. updating the seraphis paper).`
`[11-23-2022 17:06:34] <vtnerd> jeffro256[m]: it'll help with getting some rough numbers for seraphis - the ring size maybe could be bigger with it`
`[11-23-2022 17:08:43] <vtnerd> UkoeHB: kind of related: Im going to go over the jamtis spec again, and post some comments this week, possibly about reserving some subkeys `
`[11-23-2022 17:09:06] <plowsof> if we've not all seen, the bp++ author contacted and said they are working on a draft of the paper with security proofs (estimated to be ready soon) we can discuss later how to proceed, at the moment it seems we're going to wait for that until pushing forward with the 1st funding round for the review/audit from cypherstack`
`[11-23-2022 17:09:10] <vtnerd> but it shouldn't impact anything in seraphis or jamtis really`
`[11-23-2022 17:09:29] <UkoeHB> vtnerd: ok, keep in mind there have been some changes to the spec (can find them in my comments toward the end of the comment section)`
`[11-23-2022 17:09:48] <vtnerd> plowsof: are you saying that I should hold off implementing until the math checks out?`
`[11-23-2022 17:10:25] <UkoeHB> you shouldn't need to wait`
`[11-23-2022 17:10:29] <vtnerd> ok`
`[11-23-2022 17:10:53] <UkoeHB> I mean, if a vulnerability appears then just scrap it, but otherwise :)`
`[11-23-2022 17:11:06] <vtnerd> I mean it primarily just be me burning CCS funds ultimately if the security proofs dont work out for some reason`
`[11-23-2022 17:12:11] <UkoeHB> well that's kind just how R&D works, sometimes dead ends crop up`
`[11-23-2022 17:12:15] <dangerousfreedom> Hello guys, I posted this on the wallet group this week. Maybe you have some thoughts?... (full message at <https://libera.ems.host/_matrix/media/v3/download/libera.chat/ff9f9e2f3a12a791227ab1c48a8169162e0898f5>)`
`[11-23-2022 17:12:50] * dangerousfreedom uploaded an image: (247KiB) < https://libera.ems.host/_matrix/media/v3/download/matrix.org/ftIfRyFMmrxnGYwzquKftmai/image.png >`
`[11-23-2022 17:12:55] <UkoeHB> tevador: ^`
`[11-23-2022 17:15:12] <tevador> I got an email from rbrunner with similar comments. I'll draft a reply because it will be too complex for this meeting.`
`[11-23-2022 17:16:25] <rbrunner> So it's not a given then we just copy the choices of the BTC people and are probably set?`
`[11-23-2022 17:16:31] <sgp[m]> hello all`
`[11-23-2022 17:17:25] <tevador> Bitcoin had slightly different goals. We definitely should not use the bech32 polynomial.`
`[11-23-2022 17:18:04] <rbrunner> Alright, interesting, but a bit unfortunate ...`
`[11-23-2022 17:18:09] <dangerousfreedom> tevador: Ok. Thank you :)`
`[11-23-2022 17:18:32] <rbrunner> Will be interesting to see whether you conjure a good alternative out of some hat.`
`[11-23-2022 17:18:49] <UkoeHB> 3. in case anyone is waiting on me, we can move to discussion`
`[11-23-2022 17:19:14] <one-horse-wagon[> tevador: Your Rid in Jamtis is going to be 25 characters long.  Since wallet addresses are 183 characters long, couldn't the Rid reference more than one address?`
`[11-23-2022 17:19:30] <tevador> We don't need to go through the same effort as they did to find a polynomial. Our addresses are almost 5x longer, so we don't need to squeeze every bit of error detection out of a short checksum.`
`[11-23-2022 17:20:24] <Rucknium[m]> At the risk of breaking loose consensus, who are the stakeholders in the checksum decision? And has anyone reached out to them?`
`[11-23-2022 17:21:02] <tevador> one-horse-wagon[: of course, the mapping is not 1:1, but it's infeasible to find a different address with the same RID.`
`[11-23-2022 17:21:30] <rbrunner> Rucknium: Not sure what you mean with reaching out to stakeholders, probably most of them here right now, as far as deciding is concerned.`
`[11-23-2022 17:21:57] <dangerousfreedom> tevador: Yeah, probably a larger checksum would outperform a hash algorithm and we should be fine anyways.`
`[11-23-2022 17:22:25] <Rucknium[m]> rbrunner: Doesn't every wallet have to implement this? Does every merchant have to implement this?`
`[11-23-2022 17:23:07] <rbrunner> It will be part of the core code, implemented once, used by many people, except if they want to go Rust, or JavaScript, or something else special`
`[11-23-2022 17:23:41] <tevador> Ultimately, the checksum is a minor part of the specs.`
`[11-23-2022 17:23:56] <rbrunner> Ah, I see, maybe I'm wrong, because it's part of the UIs to check checksums`
`[11-23-2022 17:23:58] <tevador> We should not spend months of work on this.`
`[11-23-2022 17:24:08] <rbrunner> and they may be written in a plethora of languages.`
`[11-23-2022 17:24:25] <rbrunner> So maybe something simple to be calculated in a few lines of code really would be nice, no?`
`[11-23-2022 17:24:39] <rbrunner> As those polynomials seem to be`
`[11-23-2022 17:25:34] <rbrunner> Maybe better than people hunting down hash algorithm implementations in PHP, JavaScript, WASM, whatever`
`[11-23-2022 17:25:39] <one-horse-wagon[> tevador: Couldn't someone then take a Rid and reverse engineer it to another wallet address?  What would be the implication of that?  `
`[11-23-2022 17:26:02] <Rucknium[m]> The way things are going, Seraphis is going to be presented as a fait accompli package deal to stakeholders. There is a risk in that.`
`[11-23-2022 17:26:08] <dangerousfreedom> Rucknium[m]: It is part of the consensus. All the wallets follow the rules of what is implemented on the core. It is possible for another wallet implementation to do something different but then they will only be able to open it in their software.`
`[11-23-2022 17:26:45] <rbrunner> Yeah, but it's not merely wallets. Think of all those web frontends that should probably be able to check addresses themselves`
`[11-23-2022 17:27:03] <Rucknium[m]> I thought I had it clarified to me that address checksums are not blockchain consensus rules`
`[11-23-2022 17:27:39] <tevador> one-horse-wagon[: yes, they could. With about the same effort as deriving a private key from a public key (120-bit security).`
`[11-23-2022 17:28:01] <rbrunner> Well, but the address format is part of the whole package. Of course somebody could dream up a completely different format, but that would not fly`
`[11-23-2022 17:28:17] <dangerousfreedom> Rucknium[m]: It is not part of the blockchain consensus. I mean consensus in the common sense meaning here.`
`[11-23-2022 17:28:44] <UkoeHB> there are protocol consensus rules that are ironclad, and ecosystem interoperability conventions that can be ignored if you don't want interop`
`[11-23-2022 17:28:51] <Rucknium[m]> So, who is included in consensus and who is not?`
`[11-23-2022 17:29:03] <UkoeHB> address formats and 'how you assemble data in an enote' are interop things`
`[11-23-2022 17:29:05] <tevador> We should avoid the bitcoin situation of having multiple address formats in use at the same time.`
`[11-23-2022 17:29:32] <UkoeHB> yeah agreed`
`[11-23-2022 17:29:43] <vtnerd> yeah the myried of address types confuses even me at times`
`[11-23-2022 17:29:46] <rbrunner> You mean who is included in discussions about these question? Yes, no formal invitations to join went out to the broader ecosystem`
`[11-23-2022 17:30:10] <vtnerd> its difficult to remember which is the "best" one or some such thing`
`[11-23-2022 17:30:42] <rbrunner> So you could understand it as "fait accompli" in a certain sense.`
`[11-23-2022 17:31:03] <rbrunner> But of course we are not actively hiding.`
`[11-23-2022 17:32:32] <Rucknium[m]> We have a community relations person on payroll now : plowsof . I don't mean to slow things down. Just thinking of the social side of Seraphis.`
`[11-23-2022 17:33:34] <rbrunner> I certainly would not mind to have devs from, say, Kraken, or Ledger, or however at least as readers in the workgroup`
`[11-23-2022 17:34:23] <rbrunner> I just doubt whether that will work out. So far we mostly seemed to manage "What? Monero hardfork? When?" from those people, to put it bluntly.`
`[11-23-2022 17:34:46] <rbrunner> But maybe I am mistaken, and it gets considerably better if we have somebody on our side who cares about contacts.`
`[11-23-2022 17:35:07] <Rucknium[m]> This is how Bitcoin Cash is doing it now. Defining stakeholders in each upgrade decision and reaching out to them for support/neutral/reject statements: https://github.com/bitjson/cashtokens/blob/master/stakeholders.md`
`[11-23-2022 17:36:19] <rbrunner> Looks certainly nice`
`[11-23-2022 17:37:05] <plowsof> i'll take this up then `
`[11-23-2022 17:37:15] <UkoeHB> Do we have any other research-related topics to cover today?`
`[11-23-2022 17:37:39] <UkoeHB> maybe any updates about opsead? I haven't been really paying attention there`
`[11-23-2022 17:37:44] <jeffro256[m]> decoy selection, right?`
`[11-23-2022 17:38:02] <rbrunner> super decoy selection :)`
`[11-23-2022 17:38:27] <UkoeHB> ospead*`
`[11-23-2022 17:39:17] <Rucknium[m]> I am waiting for feedback from isthmus and ArticMine. On Friday posted part of what I submitted to them two months ago: https://github.com/Rucknium/OSPEAD/blob/main/OSPEAD-Fully-Specified-Estimation-Plan-PUBLIC.pdf`
`[11-23-2022 17:40:20] <Rucknium[m]> ^ This is basically a big menu of options to choose from. It will likely be narrowed down.`
`[11-23-2022 17:40:47] <tevador> That PDF needs an abstract.`
`[11-23-2022 17:41:31] <one-horse-wagon[> Rucknium: rbrunner was chosen as Administrator last week and he's in charge of calling meetings, trying to reach a consensus and moving the Serophis project to fruition.  The weekly meeting times are posted and interested parties are certainly invited, one and all.  Trouble is, few people care enough to do so, so he has to work with the ones that do show up and go from there.    The consensus in the Monero community is more`
`[11-23-2022 17:41:31] <one-horse-wagon[> than apparent--they want Seraphis and what it could do.`
`[11-23-2022 17:42:01] <Rucknium[m]> tevador: You're right. It does. I will write something`
`[11-23-2022 17:42:48] <rbrunner> one-horse-wagon: Right, but I think we could reach farther out indeed, by directly contacting third-parties who may not follow our issues, or the subreddit`
`[11-23-2022 17:43:50] <rbrunner> Even if they end up saying "Go ahead, we trust you" they may appreciate getting contacted`
`[11-23-2022 17:44:17] <rbrunner> And that in t`
`[11-23-2022 17:44:32] <rbrunner> turn may help implementation and deployment`
`[11-23-2022 17:44:41] <rbrunner> in about 2 years times or so`
`[11-23-2022 17:45:02] <UkoeHB> ok well seeing how we are out of research topics maybe we should wrap up the meeting here`
`[11-23-2022 17:45:07] <jeffro256[m]> A repo can be opened to create a master list of "stake holders" and categorize them and perhaps list contact info`
`[11-23-2022 17:45:48] <Rucknium[m]> Tentatively, I think that exchanges basically determine which coin fork is the majority one. They decide which fork is the true "Monero", which gets propagated to swap providers, merchants, etc.`
`[11-23-2022 17:46:56] <tevador> Most exchanges barely hold any XMR.`
`[11-23-2022 17:47:04] <rbrunner> Well, I think if we can't deliver a result that leaves little doubt, we have not done a good job.`
`[11-23-2022 17:47:28] <one-horse-wagon[> Rucknium: There is not too many exchanges out there.  `
`[11-23-2022 17:47:33] <nioc> exchanges determine monero hardforks? lol`
`[11-23-2022 17:47:58] <Rucknium[m]> If miners sell to exchanges, then miners will make mining decisions based on what fork gets them fiat (or BTC, or...)`
`[11-23-2022 17:48:14] <rbrunner> No, but they indeed could try to ignore the forked coin, Monero Seraphis, to death, if they really don't like it.`
`[11-23-2022 17:48:18] <ArticMine[m]> The majority economic consensus does `
`[11-23-2022 17:48:39] <nioc> yes`
`[11-23-2022 17:48:48] <jeffro256[m]> > Tentatively, I think that exchanges basically determine which coin fork is the majority one. They decide which fork is the true "Monero", which gets propagated to swap providers, merchants, etc.`
`[11-23-2022 17:48:48] <jeffro256[m]> I think that's more true of Bcash and other BTC forks in that family tree, but Monero hard forks tend to not to as contentious, so exchanges have historically not had much sway in picking monero hard forks`
`[11-23-2022 17:49:11] <rbrunner> Yeah, but I don't think we ever had such a big hardfork.`
`[11-23-2022 17:49:30] <rbrunner> Exchanges won't jump up and down with joy if they hear about our new addresses, I would think`
`[11-23-2022 17:49:35] <Rucknium[m]> Seraphis is going to be backward-incompatible in ways that no other Monero hard fork has been. `
`[11-23-2022 17:50:00] <tevador> But the improvements seraphis brings are massive.`
`[11-23-2022 17:50:26] <rbrunner> "Massive" for an exchange may mean something else :) Like "making massive amounts of money"`
`[11-23-2022 17:50:54] <rbrunner> First they will have to *spend* money, to adjust`
`[11-23-2022 17:50:59] <ArticMine[m]> The key here is notice `
`[11-23-2022 17:51:39] <rbrunner> Hopefully that will make a difference, yes`
`[11-23-2022 17:52:50] <rbrunner> plowsof is well motivated, they will start to move things :)`
`[11-23-2022 17:53:10] <tevador> Has there been an "official" notice (on getmonero.org) that seraphis is in the works and the what the consequences will be?`
`[11-23-2022 17:53:28] <rbrunner> Not yet, no.`
`[11-23-2022 17:54:17] <one-horse-wagon[> C'mon fellas.  Seraphis is a long way off even to get to a testnet.  You start advertising now, you're potentially talking about vaporware.`
`[11-23-2022 17:54:18] <Rucknium[m]> I think Core has a big email list that they use when hard forks are coming. The list, or part of it, could be used to call for input/notice.`
`[11-23-2022 17:55:04] <ArticMine[m]> Do we have a realistic timeline?`
`[11-23-2022 17:55:20] <rbrunner> I would say no.`
`[11-23-2022 17:55:38] <tevador> one-horse-wagon[: vaporware usually doesn't have a nearly complete C++ implementation`
`[11-23-2022 17:55:51] <rbrunner> We have something like a very rough first estimate of "2 years until the Seraphis hardfork"`
`[11-23-2022 17:56:41] <rbrunner> I think you can word it in a way that it does not come over like an advertising`
`[11-23-2022 17:56:54] <one-horse-wagon[> I say when you get a testnet up and going, advertise then, if it works successfully.  Otherwise, keep it as it is--in development.`
`[11-23-2022 17:57:34] <rbrunner> Maybe that would be a good subject for our workgroup meeting on Monday to go deeper into?`
`[11-23-2022 17:57:50] <one-horse-wagon[> Remember the Kovri debacle?`
`[11-23-2022 17:57:50] <Rucknium[m]> one-horse-wagon: That's fait accompli. You can go that route, but you can have problems`
`[11-23-2022 17:58:29] <rbrunner> In the sense of promising too much?`
`[11-23-2022 17:58:31] <UkoeHB> tevador: https://www.getmonero.org/2021/12/22/what-is-seraphis.html`
`[11-23-2022 17:58:56] <UkoeHB> seraphis works fine, the only remaining pieces are standard wallet dev work (albeit a large volume)`
`[11-23-2022 17:59:04] <jberman[m]> ^ I also gave a presentation at Monerokon on some of Seraphis/Jamtis major feature upgrades and how they'd impact users. The video/audio didn't turn out great, I'm doing another one covering the same things next week`
`[11-23-2022 17:59:09] <Rucknium[m]> In the sense of having a protocol that few stakeholders had input on. Then when stakeholders see it, they might not like it. Then what?`
`[11-23-2022 17:59:10] <rbrunner> Yes, what is on the table as proposal would be sort of a follow-up to that`
`[11-23-2022 18:00:29] <rbrunner> "Then what" is really difficult question, because I would say for many architectural decisions the train already departed`
`[11-23-2022 18:00:38] <UkoeHB> so far the only thing people in general have remarked on in terms of 'input' is wanting to keep wallet accounts`
`[11-23-2022 18:00:48] <rbrunner> If they really, really won't like those, well, bad luck`
`[11-23-2022 18:00:50] <one-horse-wagon[> Rucknium[m]: You start making decisions by committee, you go nowhere.  Especially in the early stages.`
`[11-23-2022 18:01:38] <rbrunner> But reactions when getting contacted will already tell us something, I hope`
`[11-23-2022 18:01:51] <ArticMine[m]> When can we get a testnet implementation?`
`[11-23-2022 18:02:03] <rbrunner> Maybe in 1 year?`
`[11-23-2022 18:02:11] <hyc> users want stronger privacy, ringsize 128 (ringsize bazillion), want send/recv viewkeys`
`[11-23-2022 18:02:26] <hyc> if there's no other way to get these, then that's life`
`[11-23-2022 18:02:47] <ArticMine[m]> What is still needed?`
`[11-23-2022 18:03:11] <rbrunner> A wallet, for example, to replace `wallet2`, in a way`
`[11-23-2022 18:03:19] <UkoeHB> ArticMine[m]: daemon updates, wallet implementation`
`[11-23-2022 18:03:34] <rbrunner> A brand-new transaction type, that somehow has to harmonize with the whole codebase`
`[11-23-2022 18:04:26] <jberman[m]> and audits/deep review`
`[11-23-2022 18:04:44] <UkoeHB> jberman[m]: yes, although those aren't a blocker for a testnet`
`[11-23-2022 18:04:48] <rbrunner> And for a testnet making sense, at least a wallet app with some usable interface, maybe CLI double plus :)`
`[11-23-2022 18:05:10] <jberman[m]> true`
`[11-23-2022 18:05:15] <UkoeHB> unless you want a more aggressive merge strategy so the feature branch(es) don't get too out of hand`
`[11-23-2022 18:05:58] <rbrunner> As they say, "the mind boggles", if you only start to make a list ...`
`[11-23-2022 18:06:24] <UkoeHB> btw on that note I will start making some small PRs to upstream things in my seraphis_lib branch`
`[11-23-2022 18:06:33] <UkoeHB> maybe next week? we will see`
`[11-23-2022 18:07:45] <UkoeHB> ok we are past the hour so I'll call it here, thanks for attending everyone`
`[11-23-2022 18:08:01] <isthmus> 👋`
`[11-23-2022 18:08:05] <dangerousfreedom> Thanks koe.`
`[11-23-2022 18:08:08] <rbrunner> A pleasure, as always.`
`[11-23-2022 18:08:12] <isthmus> Quick update from my end - I’m finally on vacation for the first time in forever, so I should finally have more time to get into the weeds with full OSPEAD writeup. I did give it a high-level read when initially delivered, and nothing jumped out as obviously problematic. `
`[11-23-2022 18:08:12] <isthmus> Also, we have a TON of documents pertaining to transaction tree analysis floating around in overleaf drafts and obscure repos. I’m going to try to find and compile all of these by the end of year into a compendium of transaction tree analysis that should nicely complement / contextualize the OSPEAD research.`
`[11-23-2022 18:08:17] <ArticMine[m]> Thanks `
`[11-23-2022 18:08:49] <jeffro256[m]> thanks all!`
`[11-23-2022 18:08:59] <Rucknium[m]> Thanks a bunch, isthmus`
`[11-23-2022 18:09:23] <plowsof> thx`

# Action History
- Created by: Rucknium | 2022-11-22T16:00:07+00:00
- Closed at: 2022-11-29T15:02:23+00:00
