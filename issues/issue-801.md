---
title: Monero Research Lab Meeting - Wed 22 February 2023, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/801
author: Rucknium
assignees: []
labels: []
created_at: '2023-02-20T19:33:26+00:00'
updated_at: '2023-02-28T16:10:58+00:00'
type: issue
status: closed
closed_at: '2023-02-28T16:10:58+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2.  Discuss: [Consider removing the tx_extra field](https://github.com/monero-project/monero/issues/6668).

3. Improvements to the decoy selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

4. Seraphis. ( [UkoeHB's Seraphis Proof of Concept work](https://ccs.getmonero.org/proposals/seraphis-wallet-poc-2.html), [Seraphis repo](https://github.com/UkoeHB/Seraphis) ).

5. MRL Meta: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [MoneroResearch.info repository of Monero-related research papers](https://moneroresearch.info/), [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

6. Any other business

7. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#797 

# Discussion History
## UkoeHB | 2023-02-22T18:01:47+00:00
`[02-22-2023 17:01:22] <UkoeHB> meeting time https://github.com/monero-project/meta/issues/801`
`[02-22-2023 17:01:22] <UkoeHB> 1. greetings`
`[02-22-2023 17:01:22] <UkoeHB> hello`
`[02-22-2023 17:01:36] <one-horse-wagon[> Hello.`
`[02-22-2023 17:01:48] <rbrunner> Hi`
`[02-22-2023 17:01:51] <shalit[m]> Hello`
`[02-22-2023 17:01:52] <ArticMine[m]> Hi`
`[02-22-2023 17:01:54] <Rucknium[m]> Hi`
`[02-22-2023 17:02:14] <dangerousfreedom> Hello`
`[02-22-2023 17:02:31] <ashok> hello`
`[02-22-2023 17:03:15] <UkoeHB> 2. updates, what's everyone working on?`
`[02-22-2023 17:03:32] <blankpage[m]> Hello`
`[02-22-2023 17:05:11] <Rucknium[m]> me: OSPEAD coding work. Also set up a little C++ exercise for Geometry Labs/isthmus.`
`[02-22-2023 17:07:13] <dangerousfreedom> me: trying to catch up with the new curve discussion and structuring what needs to be done for the wallet transaction history`
`[02-22-2023 17:07:26] <UkoeHB> me: getting back into my todo list, these are the major items on it: refactor enote store to use block id checkpoints, refactor enote scanning to use a re-usable state machine that can be adapted to scanning backends, review dangerousfreedom's seraphis knowledge proofs PR, then finally update the seraphis paper`
`[02-22-2023 17:08:42] <shalit[m]> me: need to push my mocks to github(the mocks should demonstrate a way to use 2 different transaction classes)`
`[02-22-2023 17:10:32] <blankpage[m]> What are these "two different transaction classes" for? `
`[02-22-2023 17:10:53] <UkoeHB> 3. discussion; today we were supposed to return to the tx_extra discussion, however the lower turnout makes me unsure if we can resolve it in this meeting`
`[02-22-2023 17:12:04] <rbrunner> In any case, I have a question there, because I lost track a bit in all the discussion`
`[02-22-2023 17:12:16] <shalit[m]> So currently we are using a single transaction class, but with seraphis we are adding a new transaction class, and we want a nice way to treat both of them, without, for example, save in each place that treats transaction two lists, one for storing cryptonote transaction classes and second for storing seraphis transactions`
`[02-22-2023 17:12:26] <rbrunner> There was the proposal to mandate encryption for the tx_extra data`
`[02-22-2023 17:12:34] <rbrunner> And check that with some heurisitic`
`[02-22-2023 17:12:49] <rbrunner> Where does that discussion stand? Is that reasonably possible to achieve?`
`[02-22-2023 17:13:34] <Rucknium[m]> I don't know. We shouldn't use a heuristic by the way. Do a rigorous statistical test.`
`[02-22-2023 17:14:12] <rbrunner> I meant to include that. I am pretty sure you can't prove something is encrypted`
`[02-22-2023 17:14:28] <rbrunner> I think what you can hope for is an algorithm that says "This is probably encrypted"`
`[02-22-2023 17:14:41] <Rucknium[m]> I scratched the surface of cryptographic randomness tests. It can be complicated. If we treat it as just an unordered set, it is pretty simple Chi-squared test or similar. If it is an ordered  sequence , then it gets more complicated.`
`[02-22-2023 17:14:44] <rbrunner> and then hope that this does not fail and reject properly encrypted stuff sometimes`
`[02-22-2023 17:15:15] <Rucknium[m]> You can set the rejection probability by choosing the p-value to reject below`
`[02-22-2023 17:15:23] <Rucknium[m]> That's what a p value is`
`[02-22-2023 17:15:23] <UkoeHB> My take is you can't force people to not opt-out of privacy. In the case of a statistical test you can mask your payload with a fixed random bytestring for example.`
`[02-22-2023 17:15:37] <Rucknium[m]> It's the probability of a false positive`
`[02-22-2023 17:16:05] <blankpage[m]> Thanks shalit I remember reading this in the chat at some point now that you've explained`
`[02-22-2023 17:16:07] <Rucknium[m]> UkoeHB: Yeah. There is a question of how someone might try to directly fool the test`
`[02-22-2023 17:16:17] <rbrunner> That would almost count as encryption, no?`
`[02-22-2023 17:16:49] <merope> You probably want some form of deniable encryption then`
`[02-22-2023 17:16:59] <rbrunner> I see this more as a political question: If the Monero Project gets attacked, we can show that we took reasonable precautions to ask for encryption`
`[02-22-2023 17:17:18] <rbrunner> Attacked in the sense of politics: Somebody wants to throw mud at us`
`[02-22-2023 17:17:29] <UkoeHB> 'political precaution' isn't in the design goals of the project`
`[02-22-2023 17:17:37] <rbrunner> :)`
`[02-22-2023 17:18:21] <rbrunner> Alright, but I got my personal question answered: That question is not settled, I can't assume encryption enforcement is on the table as option`
`[02-22-2023 17:18:31] <Rucknium[m]> If you wanted an answer on the feasibility of a statistical test, I could have researched it in more depth for this meeting.`
`[02-22-2023 17:19:13] <UkoeHB> anyway, here is the choice matrix for the tx_extra, we can at least discuss it with the people here`
`[02-22-2023 17:19:13] <UkoeHB> A) [remove tx extra]: cost is tx utility flexibility tied to hardfork (or steganography)`
`[02-22-2023 17:19:13] <UkoeHB> B) [keep tx extra in some optimized form]: cost is uniformity and scaling trade-offs depending on the solution`
`[02-22-2023 17:19:13] <UkoeHB>     1) leave as unlimited-size TLV field`
`[02-22-2023 17:19:13] <UkoeHB>     2) mandate maximum tx extra size (e.g. anything in 0 - 1000 bytes)`
`[02-22-2023 17:19:13] <UkoeHB>     3) mandate optional fixed-length tx extra size + encrypt by default`
`[02-22-2023 17:19:13] <UkoeHB>     4) mandate fixed-length tx extra for all txs + encrypt by default`
`[02-22-2023 17:19:14] <UkoeHB>     5) other`
`[02-22-2023 17:19:19] <rbrunner> I don't think that would be important enough, if only I am curious about this, while forming my opinion about tx_extra removal yes/no`
`[02-22-2023 17:19:43] <Rucknium[m]> I said last meeting "If there is a need/desire for a statistical check of the randomness (encrypted status) of the tx_extra field, I can help search for an appropriate statistical test." Maybe I should have asked for an affirmative "yes" if that statement was ambiguous.`
`[02-22-2023 17:20:25] <rbrunner> Guilty. I somehow missed that.`
`[02-22-2023 17:20:40] <BusyBoredom[m]> Encrypting by default makes sense. Everyone who wants that privacy will have it without thinking. Trying to enforce does not make sense. If someone is trying to flood the network with identifiable outputs, they can just publish they don't need tx_extra for that in the first place so I don't see what the randomness check buys us. `
`[02-22-2023 17:20:54] <rbrunner> So that's now a "no" from me: I don't think that merits further investigation right now.`
`[02-22-2023 17:20:57] <vtnerd> here, but late, sorry`
`[02-22-2023 17:21:01] <BusyBoredom[m]> They can just publish their view key*`
`[02-22-2023 17:21:09] <UkoeHB> sorry Rucknium[m] your comment may have been lost in all the activity of last meeting`
`[02-22-2023 17:21:33] <Rucknium[m]> It's fine. No offense taken at all.`
`[02-22-2023 17:22:10] <rbrunner> In that matrix you propose, can we mix the points 1 to 5? I would like maximum length plus an attempt at asking for encryption`
`[02-22-2023 17:23:05] <rbrunner> Looks like that would be a new, additional number`
`[02-22-2023 17:23:29] <merope> Just an outsider's opinion: to me, the optional fixed-length tx_extra (with encryption on top) seems like the best compromise between all options. Users who don't need it don't have to pay extra fees and there's less bloat, and those who do will be still indistinguishable from eachother, so we'll have no idea what they're actually doing. Yes, it's still technically a puddle, but it would be a uniform puddle`
`[02-22-2023 17:23:34] <vtnerd> a maximum or fixed?`
`[02-22-2023 17:23:54] <ArticMine[m]> My take is to narrow it down to A or B3. Thoughts`
`[02-22-2023 17:24:06] <UkoeHB> rbrunner: B) 2) mandate maximum tx extra size (e.g. anything in 0 - 1000 bytes) (option: encrypted by default)`
`[02-22-2023 17:24:07] <vtnerd> actually maximum makes most sense`
`[02-22-2023 17:24:18] <Rucknium[m]> I think it may be hard to require changes to tx_extra by changing node relay rules. About half of all nodes were running old software in the August hard fork. At best, the mining pool and p2pool nodes (maybe) would reject the txs when they came to them if they were running new new-rules nodes.`
`[02-22-2023 17:24:57] <merope> Also, the pros and cons of each point can be hashed and rehashed ad infinitum. I think the best option is to choose an arbiter (either an individual, or a small group) that we "trust", who will make a final decision on the matter`
`[02-22-2023 17:25:15] <merope> And that decision will be final`
`[02-22-2023 17:25:17] <vtnerd> basically tevador was on the right track with that pr, as per usual lol`
`[02-22-2023 17:25:23] <ArticMine[m]> The problem of max size is that it really leads to tx fingerprinting `
`[02-22-2023 17:25:27] <rbrunner> UkoeHB: That 2) sounds good to me :)`
`[02-22-2023 17:25:29] <moneromooo> I kinda like the stego option, despite the ring size decrease to the recipient (and only the recipient).`
`[02-22-2023 17:26:09] <vtnerd> yeah but you gotta know what your doing if you dont follow the guidelines posted by core`
`[02-22-2023 17:26:24] <vtnerd> as in core will set guidelines for tx_extra, and so forth`
`[02-22-2023 17:26:28] <rbrunner> "stego option" does not look like an option to me, just the likely consequence of removing tx_extra`
`[02-22-2023 17:26:43] <vtnerd> so you can make it variables size with a cap, but we'll set a tighter spec for normal usage`
`[02-22-2023 17:26:53] <moneromooo> Otherwise B3.`
`[02-22-2023 17:27:07] <blankpage[m]> Max size (instead of FIXED size) would lead to all sorts of fungibility puddles`
`[02-22-2023 17:27:47] <vtnerd> yeah but youre just destroying your own privacy first, everyone elses second`
`[02-22-2023 17:27:53] <rbrunner> Yes, but still progress, as the most blatant nonsense is prevented`
`[02-22-2023 17:28:31] <ArticMine[m]> blankpage[m]: 👍`
`[02-22-2023 17:29:13] <rbrunner> Just to make sure: In any fixed size discussion, it's already assumed that tx_extra is ONLY there if somebody puts something there?`
`[02-22-2023 17:29:27] <rbrunner> I.e. the "normal" uses we have today are away`
`[02-22-2023 17:29:44] <rbrunner> With additional keys and such, don't remember exactly`
`[02-22-2023 17:29:47] <ArticMine[m]> Yes `
`[02-22-2023 17:30:25] <blankpage[m]> rbrunner: that is the difference between B3 & B4 surely`
`[02-22-2023 17:31:01] <rbrunner> Hmm, not sure, I think it's a technicality that does not yet occur here`
`[02-22-2023 17:31:15] <rbrunner> But anyway, it's important to understand the proposal`
`[02-22-2023 17:31:22] <UkoeHB> vtnerd: the tx_extra as a generic field has a broad range of 'default behavior'. Since our goal is 'private by default', imo we should think about all natural uses of the tx_extra as part of the design scope - which includes any field someone adds for their personal project, etc. That what B3 and B4 are all about - setting up the field so all default-conforming uses (both 'not using it at all' and 'using it with some `
`[02-22-2023 17:31:22] <UkoeHB> personal field but following spec') have a higher degree of privacy than we have now.`
`[02-22-2023 17:32:02] <Rucknium[m]> Selecting coinbase outputs in rings might be having more effect on reducing effective ring size right now than tx_extra ever will. And we haven't made real moves to address it besides sech1's work on p2pool output efficiency: https://github.com/monero-project/research-lab/issues/109`
`[02-22-2023 17:32:21] <vtnerd> a lot of words ukoehb, but you might be in the minority atm`
`[02-22-2023 17:33:27] <rbrunner> Maybe`
`[02-22-2023 17:33:27] <vtnerd> the project is about continually improvement, sometimes it takes a while ... anyone enough rambling from me`
`[02-22-2023 17:33:36] <vtnerd> *anyway`
`[02-22-2023 17:33:48] <ArticMine[m]> The option is 0 (effective) A or a small fixed size say 256 bytes. This is enforced by consequences. `
`[02-22-2023 17:33:48] <ArticMine[m]> Randomness Is enforced only by default encryption and multiple randomness tests via node relay `
`[02-22-2023 17:33:49] <UkoeHB> vtnerd: to be more blunt, design choices have to be focused on our design goals`
`[02-22-2023 17:34:10] <UkoeHB> which are: privacy, security, scalability, longevity`
`[02-22-2023 17:34:20] <ArticMine[m]> Enforced by consensus `
`[02-22-2023 17:34:28] <rbrunner> Well, discussing our design goals would probably end in a similar going round and round ...`
`[02-22-2023 17:35:15] <rbrunner> As soon as I try to add "flexibility" or "real-world usefulness" in there probably ...`
`[02-22-2023 17:35:25] <ArticMine[m]> I believe we can start by eliminating options a clear majority disagree with `
`[02-22-2023 17:36:00] <UkoeHB> rbrunner: those are secondary goals, I listed the primary goals`
`[02-22-2023 17:36:07] <blankpage[m]> The difference between B3 & B4 (whether the fixed soze encrypted blob is mandatory or not) comes down to scaling of storage requirements, because these blobs have very low verification costs. It seems to me that scalability of verification is likely to cause problems long before scalability of storage/bandwidth.`
`[02-22-2023 17:36:45] <xmrack[m]> I’d vote to remove the tx_extra field (A) and enforce a certain number of outputs for each transaction (2,4,8,16) to prevent output stego`
`[02-22-2023 17:37:09] <vtnerd> I think you might be out voted on that now xmrack[m]`
`[02-22-2023 17:37:11] <UkoeHB> xmrack[m]: that doesn't prevent output stegonography`
`[02-22-2023 17:37:24] <vtnerd> yeah exactly, and it doesn't solve the problem`
`[02-22-2023 17:37:34] <rbrunner> I only see B) 1) as having clear majority against right now ...`
`[02-22-2023 17:37:51] <ArticMine[m]> Actually bandwidth is the biggest scaling challenge`
`[02-22-2023 17:37:51] <ArticMine[m]> Verification can be processed in parallel`
`[02-22-2023 17:37:51] <ArticMine[m]> This is why I do not like B4`
`[02-22-2023 17:38:21] <rbrunner> And B) 5, we seem to have no other clear proposals`
`[02-22-2023 17:39:22] <rbrunner> Anyway, from the pro fixed size voters, what do you imagine as a reasonable fixed size?`
`[02-22-2023 17:40:05] <ArticMine[m]> 0 or 256 bytes `
`[02-22-2023 17:40:13] <rbrunner> Maybe we could make those proposals a bit more precise for a vote in the near future`
`[02-22-2023 17:40:56] <UkoeHB> ArticMine[m]: I was wondering if maybe 128 bytes per output would be more useful (2-out txs would be 256 bytes)`
`[02-22-2023 17:41:04] <xmrack[m]> If the consensus is for something in option B. I’d prefer either 3 or 4`
`[02-22-2023 17:41:32] <rbrunner> Ah, per output is of course a possible variant`
`[02-22-2023 17:41:48] <ArticMine[m]> 128 bytes or 0 is fine `
`[02-22-2023 17:42:25] <rbrunner> But then people may produce many dummy output to get their GIF or JPEG into there, surely`
`[02-22-2023 17:42:51] <ArticMine[m]> Per output is messy `
`[02-22-2023 17:42:53] <Rucknium[m]> In my scratch of the surface at cryptographically randomness tests, most tests had O(N^2) complexity at worst case. That may matter if we want a fixed/max size + statistical test of randomness.`
`[02-22-2023 17:44:00] <ArticMine[m]> We have the nodes pick a test at random from a set that can change over time `
`[02-22-2023 17:44:00] <UkoeHB> ArticMine[m]: how so?`
`[02-22-2023 17:44:23] <rbrunner> 256 is a nice round number. Anybody here who thinks they cannot live with that?`
`[02-22-2023 17:44:39] <moneromooo> Randomness test is only useful as a sanity check for stupid clients. Someone can still "encrypt" with a well known secret key, which should defeat any statistical test (that works).`
`[02-22-2023 17:44:55] <blankpage[m]> If the blob is fixed per output, it would require fees per output to scale much quicker than now surely`
`[02-22-2023 17:45:09] <ArticMine[m]> moneromooo: That is the point `
`[02-22-2023 17:45:25] <kgsphinx[m]> As an outsider that might consider integrating with Monero, I'd find a fixed tx_extra with encryption to be the better choice.  0 or 256, 1000, whatever.  If you think you can actually validate randomness efficiently then that'd be fine.  I'd just rather not suffer random failures because of this. `
`[02-22-2023 17:45:39] <ArticMine[m]> The only safe way is encryption `
`[02-22-2023 17:46:49] <UkoeHB> I don't really understand how a statistical test is useful if the default wallet behavior is to encrypt the field.`
`[02-22-2023 17:47:16] <ArticMine[m]> Otherwise you stand the risk of being caught by some "randomness" test`
`[02-22-2023 17:47:20] <moneromooo> Kicking third party wallets in the butt till they bother encrypting :)`
`[02-22-2023 17:47:30] <UkoeHB> shades of opting out? seems like a pointless exerciese`
`[02-22-2023 17:47:54] <rbrunner> Well, I am sure lawyers have a nice term for that, "reasonable effort" (of the project) maybe, but anyway, that's again "political" :)`
`[02-22-2023 17:48:01] <Rucknium[m]> There are going to be random failures of valid (encrypted) tx_extra contents. The failure rate can be set by the p value. If you set the p very very low, then you will have more false negatives (i.e. let a transaction through yet tx_extra is not encrypted).`
`[02-22-2023 17:49:06] <Rucknium[m]> So you could set p to 0.00001 or something and we would expect 0.001% of all valid tx_extra contents to not be relayed by nodes.`
`[02-22-2023 17:49:41] <rbrunner> Is this also dependent on the length? Is the false positive danger bigger with shorter lengths?`
`[02-22-2023 17:49:56] <moneromooo> Yes. If you have 1 bit, then... `
`[02-22-2023 17:49:57] <UkoeHB> in my view it's fairly black and white: either an implementer tries to be default-conforming, or he doesn't and all bets are off. If encrypting is too much of a pain, then the implementer will just find some cheap workaround to a statistical test.`
`[02-22-2023 17:50:10] <moneromooo> I like using extreme values as a sanity check.`
`[02-22-2023 17:50:14] <blankpage[m]> I agree that statistical tests seem relatively pointless. The effort for someone to create a blob of the correct length with clear text identifiable text is much higher than typing troll comments in the tx_extra field as it is now`
`[02-22-2023 17:50:47] <ArticMine[m]> We  make the default encryption `
`[02-22-2023 17:50:50] <Rucknium[m]> rbrunner: The false negative danger would be greater when the length is shorter. Usually with these tests you, the decider, set the false positive probability (that's the p value).`
`[02-22-2023 17:51:36] <rbrunner> Yeah, moneromooo's 1 bit argument is pretty convincing. But I guess with 256 bytes we get something working reasonably.`
`[02-22-2023 17:52:20] <Rucknium[m]> So if the tx_extra byte length is really short, then it might be pointless to do a test since you would have to set p to be low and only catch really unencrypted text rarely`
`[02-22-2023 17:52:49] <rbrunner> Yes, but even that cheap workaround will prevent we have blatant nonsense in the blockchain open for everybody to pick up trivially`
`[02-22-2023 17:53:11] <Rucknium[m]> This is just general statistical theory that almost certainly applies to a more specific test. I have not looked deeply into what specific tests could be used`
`[02-22-2023 17:53:35] <Rucknium[m]> But here are some materials I was looking at:`
`[02-22-2023 17:53:37] <xmrack[m]> The statistical test sounds “hacky” and bad UX for those handful of users`
`[02-22-2023 17:53:40] <Rucknium[m]> https://cran.r-project.org/web/packages/CryptRndTest/vignettes/CryptRndTest.pdf`
`[02-22-2023 17:53:40] <Rucknium[m]> https://raw.githubusercontent.com/terrillmoore/NIST-Statistical-Test-Suite/master/assets/nistspecialpublication800-22r1a.pdf`
`[02-22-2023 17:53:40] <Rucknium[m]> https://github.com/terrillmoore/NIST-Statistical-Test-Suite`
`[02-22-2023 17:53:40] <Rucknium[m]> https://cran.r-project.org/web/packages/RDieHarder/vignettes/RDieHarder.pdf`
`[02-22-2023 17:53:43] <UkoeHB> rbrunner: that is a bad argument, there are many trivial ways to put nonsense in the blockchain with a statistical test`
`[02-22-2023 17:54:06] <kgsphinx[m]> Intuitively the shorter the field, the more failures you'd have.  Probably deserves some research.  All for an encrypted fixed length field if you send it.`
`[02-22-2023 17:54:07] <UkoeHB> for example, you can XOR each set of 32 bytes with one of the key images; trivial to decrypt`
`[02-22-2023 17:54:12] <rbrunner> Ok, maybe I am not used to think like an adversary ...`
`[02-22-2023 17:55:15] <blankpage[m]> Testing for "randomness" doesn't stop determined individuals from harming their privacy. Seems the only practical impact is causing occasional tx failure. Just making encrypt the default is good enough.`
`[02-22-2023 17:55:16] <Rucknium[m]> I agree that there are multiple ways to get around these types of statistical tests by a determined programmer.`
`[02-22-2023 17:55:26] <rbrunner> Can't we solve that random failure problem easily? Allow to hash after encryption, have a counter how many times you hashed, hash until the test is ok`
`[02-22-2023 17:55:40] <UkoeHB> in the end we'd just look stupid for trying, if some one-liner is all you need to decrypt the field`
`[02-22-2023 17:56:12] <moneromooo> You can't, since 000000...00000 is very likely a valid ciphertext.`
`[02-22-2023 17:57:10] <Rucknium[m]> Zcash has an encrypted memo field. I'm not sure how they do it. Maybe they encrypt with users' private keys.`
`[02-22-2023 17:57:48] <rbrunner> Which immediately takes away much of its usefulness for our tx_extra if true.`
`[02-22-2023 17:57:48] <Rucknium[m]> They are looking to improve it by the way for messaging: https://forum.zcashcommunity.com/t/rfp-zcash-memo-field-secure-messaging-extension/44069`
`[02-22-2023 18:00:11] <xmrack[m]> “Zcash lacks several essential features necessary for secure messaging, such as being signed to verify the origin of messages” `
`[02-22-2023 18:00:11] <xmrack[m]> Doesnt sound like they use their private key`
`[02-22-2023 18:00:34] <UkoeHB> we are at the end of the hour so I'll call it here, we will return to the tx_extra discussion in the next meeting`
`[02-22-2023 18:01:04] <UkoeHB> thanks everyone`
`[02-22-2023 18:01:06] <blankpage[m]> Anyway I vote b3 or b4, leaning towards b3. My reasoning is that two puddles is not as good as one puddle, but perhaps on a practical level two puddles is good enough considering the space savings compared to mandatory fixed size blobs. And two puddles is much better than potentially hundreds of puddles of the present situation.`

# Action History
- Created by: Rucknium | 2023-02-20T19:33:26+00:00
- Closed at: 2023-02-28T16:10:58+00:00
