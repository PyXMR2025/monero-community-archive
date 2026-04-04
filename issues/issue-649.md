---
title: Monero Research Lab Meeting - Wed 12 January 2022 @ 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/649
author: Rucknium
assignees: []
labels: []
created_at: '2022-01-12T00:48:58+00:00'
updated_at: '2022-01-18T17:17:50+00:00'
type: issue
status: closed
closed_at: '2022-01-18T17:17:50+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Revisit @tevador 's idea to record account indices in the tx, to improve robustness of output recovery: https://libera.monerologs.net/monero-research-lab/20211230 . Additional reading: https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357

3. Focus on Seraphis address schemes and hopefully reach some kind of decision (or get closer, maybe narrow down the choices to 2 or 3). [Schemes](https://github.com/monero-project/research-lab/issues/92) [@tevador proposal](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024)

4. Adaptive CPU regulation for improved mining performance ( maxwellsdemon )

5. Further analysis of July-Aug 2021 tx volume anomaly ( Isthmus / Mitchellpkt - see [these meeting logs](https://github.com/monero-project/meta/issues/621#issuecomment-948953655)) [Previous analysis](https://mitchellpkt.medium.com/fingerprinting-a-flood-forensic-statistical-analysis-of-the-mid-2021-monero-transaction-volume-a19cbf41ce60) with [Reddit discussion](https://www.reddit.com/r/Monero/comments/pvm634/fingerprinting_a_flood_forensic_statistical/)

6. Improvements to the mixin selection algorithm ( [Decoy Selection Algorithm - Areas to Improve](https://github.com/monero-project/research-lab/issues/86), [JBerman's weekly updates](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/249#note_11480), [Binning PoC](https://github.com/monero-project/research-lab/issues/88), [OSPEAD](https://ccs.getmonero.org/proposals/Rucknium-OSPEAD-Fortifying-Monero-Against-Statistical-Attack.html) ) @j-berman @Rucknium

7. Seraphis/Triptych/Lelantus Spark ( [UkoeHB's Seraphis Proof of Concept work](https://repo.getmonero.org/monero-project/ccs-proposals/-/merge_requests/256), [Seraphis repo](https://github.com/UkoeHB/Seraphis), [Lelantus Spark](https://eprint.iacr.org/2021/1173) & [Tripych Multisig](https://github.com/cypherstack/triptych-multisig/blob/main/main.pdf) )

8. MRL META: "Cat herding", i.e. prioritization of research areas and features. Active recruitment of technical talent, MRL structure, funding (@Rucknium & others) [Reddit discussion](https://www.reddit.com/r/Monero/comments/pkg3d6/the_monero_project_should_actively_recruit/)

9. Examine sample size and random seed matters in Monero's unit tests. IRC discussion: [monero-dev](https://libera.monerologs.net/monero-dev/20211018#c39593) , [monero-research-lab](https://libera.monerologs.net/monero-research-lab/20211018)

10. Multisig Drijvers attack mitigation [Technical note](https://github.com/UkoeHB/drijvers-multisig-tech-note) , [Haveno bounty](https://github.com/haveno-dex/haveno/issues/103)

11. Any other business

12. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: UkoeHB

Previous meeting agenda/logs:

#646 

# Discussion History
## Rucknium | 2022-01-14T08:18:20+00:00
### Meeting log:
From https://libera.monerologs.net/monero-research-lab/20220112

```
17:00:29 <UkoeHB> meeting time: https://github.com/monero-project/meta/issues/649
17:00:36 <UkoeHB> 1. greetings
17:00:36 <UkoeHB> hello
17:00:56 <ArticMine[m]> Hi
17:01:02 <rbrunner> Hello
17:01:47 <Rucknium[m]> Hi
17:03:17 <tevador> hi
17:03:31 <jberman[m]> howdy
17:04:19 <UkoeHB> 2. discussion; today I want to discuss this https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4025357 and the following comment https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4026264
17:04:57 <UkoeHB> Anyone have thoughts/comments/questions other than tevador and I?
17:05:58 <jberman[m]> On method 3: account keys must be pre-computed, meaning "account"-level subaddresses (i) would need to be pre-loaded in a lookup table? I didn't have enough time to fully grok that method
17:06:21 <jberman[m]> (for non-change/self-spends)
17:06:27 <UkoeHB> not subaddresses, the account key itself (used to generated addresses for that account)
17:06:45 <rbrunner> Do I get that this can be seen as a quite broad question / decision of how to support accounts under Seraphis / JAMTIS, and if yes how?
17:06:50 <UkoeHB> Basically users would have to tell their software which accounts to look in for funds.
17:07:39 <UkoeHB> rbrunner: the follow-up comment is about whether/how to support accounts. The original post is about how to efficiently map outputs to addresses/accounts when scanning.
17:07:43 <tevador> rbrunner: it's more about optimizing output recognition (which accnt/addr the output belongs to)
17:07:57 <jberman[m]> but there can be tons of account keys, which has a similar issue as method 1 where you need a lookup table, no?
17:08:28 <rbrunner> Yeah, but if you basically get rid of rigid account schemes, that does not matter so much anymore, or can get simplified, right?
17:08:47 <tevador> jberman[m]: hence my proposal to remove the account keys
17:09:41 <tevador> after listing the pros and cons, I think it's a no-brainer, but I'd like to hear opinions
17:10:13 <rbrunner> As far as I can see use of accounts has stayed pretty much a "power user" feature, not even all wallets support them, they are not exactly a roaring success story if you want to be brutally honest
17:10:20 <UkoeHB> jberman[m]: yes, but at some point the purpose/utility of an 'account' becomes lost if you are generating a lot of them; realistically, the set of accounts should be strictly bounded
17:10:26 <rbrunner> Thus if we can simplify there, why not?
17:10:55 <tevador> yes, we also proposed slashing the account index to 16 bits
17:11:43 <tevador> rbrunner: it was mostly for merchants
17:11:55 <UkoeHB> I think accounts should either be fully supported, or not at all.
17:12:06 <rbrunner> Interesting. Did it succeed there? Do we know?
17:12:08 <tevador> but even without account-level tiers, there is still one tier that can generate addresses, but cannot see outputs
17:12:48 <tevador> I have no idea how people or merchants use accounts currently
17:13:14 <UkoeHB> Although on second thought, maybe partial support would be ok... if users want to categorize their funds somehow, 'accounts' is the most reasonable way.
17:13:26 <tevador> I think accounts are a wallet-level feature
17:13:35 <rbrunner> Well, at least I have not seen a building up of pressure "When will you finally support accounts?" for wallet that don't support them (yet)
17:14:02 <UkoeHB> Yeah, but the reference implementation will probably be 99% of users
17:14:39 <tevador> still, it's probably cleaner if the address specs are agnostic to that feature
17:14:41 <jberman[m]> I think deprecating "accounts" needs feedback from more users. I use them and it's nice because I get streamlined bookkeeping and a nice abstraction for how funds are spent, without needing to go a deeper level and actually select which outputs I want to spend
17:14:47 <rbrunner> Not sure, I think Feather Wallet has made inroads compared with the GUI, and I think they did a conscious decision to not support accounts, because too complicated UX wise
17:15:58 <rbrunner> Yes, that's why I liked the approach in the latest comment of a uniform address space that only the wallet logically manages in some "compartments", however you call them
17:16:11 <rbrunner> If that really flies
17:16:38 <tevador> I think the main question today is if 8 bytes longer addresses and 8 bytes larger outputs are worth the optimization of output detection
17:16:46 <UkoeHB> Maybe we can keep accounts with the simplified scheme but rename them to like 'balance categories' or something to reflect that they aren't 'hard' delineations in the wallet.
17:17:43 <Rucknium[m]> BTC and several other coins have accounts as well. From my observations, accounts are rarely used. Part of it is a chicken-and-egg problem. Wallets don't support them since users don't use them, and vice versa.
17:17:58 <UkoeHB> My personal opinion is that 8 bytes is a pricey worthy of robust output recovery.
17:17:58 <Rucknium[m]> Maybe merchants and exchanges are using them, though. 
17:18:17 <UkoeHB> price*
17:18:18 <rbrunner> What do you mean with "output recovery" exactly?
17:18:26 <UkoeHB> view scanning
17:18:39 <monerobull[m]> Rucknium[m]: I have like 10 wallets since I didn't understand accounts at first
17:19:09 <UkoeHB> With a subaddress table you can have outputs outside the table (this prevents PID address mapping, and similar schemes).
17:19:14 <Rucknium[m]> One of the numbers in the BTC derivation paths for BIP44/49-compliant wallets is for account numbers.
17:20:12 <rbrunner> And with 8 bytes those "outside the table" problems are (forgive the pun) off the table i.e. solved?
17:20:49 <UkoeHB> Right; another example: 'generate random subaddress' without needing to know all the subaddresses you already generated
17:21:04 <jberman[m]> good pun rbrunner 
17:21:35 <rbrunner> Everything that simplifies has my immediate sympathy :)
17:22:15 <UkoeHB> (with 'generate random' and 40-bit addresses, a collision will occur 50% of the time over 1mill generations)
17:24:45 <tevador> I think the output scanning layer would simply return "this output goes to this 56-bit index" and the higher layers would interpret that somehow (could even be a flat 56-bit address space)
17:25:33 <UkoeHB> right
17:25:43 <rbrunner> Is it 40 bit if we keep a reasonable number of fixed accounts?
17:25:52 <UkoeHB> 40 bit with 16bits of accounts
17:25:58 <rbrunner> Ah ok
17:26:21 <UkoeHB> or 'categories' maybe ^.^
17:27:46 <rbrunner> One of the nice aspect of today's account is that they restore from the blockchain. If we loose that seems to me we devalue them quite a bit. But can't have all, I guess
17:28:19 <tevador> ^ that aspect would not be lost
17:28:34 <rbrunner> Even with a flat space of 56 bits?
17:28:42 <rbrunner> On the lowest level
17:29:00 <tevador> you don't lose anything, that's just a different interpretation of the same data
17:29:31 <tevador> you could treat the 56 bits as 16+40 bits and get accounts
17:29:51 <rbrunner> Hmm, yes, but this may then - at least potentially - differ from wallet to wallet.
17:30:18 <rbrunner> I mean wallet app to wallet app
17:30:19 <UkoeHB> the reference implementation sets the standard, and it is up to other wallets to follow/go a different way
17:30:24 <tevador> one thing is what is written in the specs, actual implementation is another thing
17:30:59 <jberman[m]> So if we kept 16 bit "accounts"/categories, the client would precompute 2^16 keys and keep them in memory, right? And if accounts are deprecated, this isn't necessary?
17:31:06 <UkoeHB> wallets already have the freedom to do something different with indices (not that any of them do, afaik)
17:31:37 <tevador> jberman[m]: exactly
17:31:53 <UkoeHB> jberman[m]: that is an option, though imo only categories the user manually adds should be precomputed
17:32:16 <rbrunner> Or if accounts are pushed one or two levels up the processing hierarchy, if I understand correctly
17:32:19 <tevador> the point is that if the account index is used for key derivation then accounts become mandatory for all wallets
17:32:23 <UkoeHB> It would take 2.6s to set up Blowfish contexts for 65k keys.
17:33:28 <jberman[m]> are collisions possible today too? or would that be new
17:33:43 <UkoeHB> collisions where/
17:33:44 <jberman[m]> possible within reason
17:34:15 <rbrunner> That you can find two pairs (account, address within account) that result in the same subaddress?
17:34:19 <jberman[m]> <UkoeHB> "(with 'generate random' and 40-..." <- here
17:34:34 <tevador> with 64-bit PIDs, collisions are possible if you have 100+ millions of them
17:34:40 <UkoeHB> yes generating a random 32-bit subaddress index will also have collisions
17:35:12 <tevador> with 32 bits, you will get collisions with ~thousands
17:35:35 <rbrunner> Because the reach the same ECC point or whatever within the precision used? Or something like that :)
17:36:05 <tevador> it's extremely unlikely that two different addresses will have the same key
17:36:05 <UkoeHB> It is just an index that is random, not the ECC point
17:36:27 <rbrunner> Anyway, if we also can have collisions *with* accounts, that's not a definite pro of them.
17:36:33 <UkoeHB> If you randomly generate the same index twice (collision), then you'll get the same adddress
17:37:09 <rbrunner> No, I mean whether you can number through all possible accounts and all possible address within them and never get the same subaddress twice
17:37:49 <rbrunner> with a guarantee
17:37:50 <UkoeHB> yes, the set of all possible addresses won't contain collisions except with negligible probability. You need 2^128 random ECC points to get 50% chance of collision.
17:38:26 <rbrunner> Ok, so probably not in this universe anymore
17:38:55 <jberman[m]> who's generating random subaddresses and why does a collision at the index matter? users increment them
17:39:34 <tevador> I think that was one argument merchants used against subaddresses, "you can generate PIDs at random"
17:39:52 <UkoeHB> I mean if you forget how many addresses you have. Or maybe you have some service generating addresses for you and don't want them to collide with addresses you generate on your own machine.
17:39:59 <rbrunner> I think that would just be a particularly easy implemenation for merchant system, because they don't have to "slog" around info where they stand with the counter
17:41:51 <rbrunner> So we have now possible collision rates for random subaddresses on the table which are a bit uncomfortably high, seems to me
17:42:08 <jberman[m]> that strikes me as not-so-robust today
17:42:10 <Rucknium[m]> rbrunner: slog = schlepp?
17:42:10 <tevador> with the encrypted address tags, merchants could generate indices randomly, but they would still have to check for collisions. I think even with PID this is required unless you have just a few orders overall
17:42:14 <UkoeHB> Btw in the future we might hear complaints that 40-56 bits is too small for PIDs... don't you need like 10-16 bytes for robust PIDS?
17:42:23 <rbrunner> Yeah, "schlepp"
17:42:35 <jberman[m]> ideally merchant system would use a shared counter to generate addresses
17:43:20 <tevador> with the lookup table based search, a shared counter is a requirement
17:45:12 <rbrunner> My head hurts, with so many conflicting pros and cons ...
17:45:20 <rbrunner> Difficult decisions
17:46:03 <UkoeHB> what are the conflicting things? the only con to 'make a change' is the addition of 8 bytes to outputs/addresses
17:46:50 <rbrunner> Well, if that does not open the way to successfully generate random subaddresses without fear / checking for addresses, that's maybe a con?
17:46:51 <jberman[m]> one thing that's nice: I think method 2 is inferior to either method 1 or method 3, so that one can be eliminated to reduce decision surface
17:47:09 <UkoeHB> there are two things we are discussing: 8 bytes for more robust output discovery, whether/how to deprecate accounts (a basically unrelated question)
17:48:13 <tevador> jberman[m]: you mean method 1 is inferior to 2 and 3? 2 can do the same thing as 1, but adds more options
17:48:58 <UkoeHB> rbrunner: maybe you'd like to propose going to 16 bytes (we need a multiple of 64 bits with blowfish, unless we can find a good 32-bit cypher and can do 12 bytes)?
17:49:17 <tevador> 16 bytes is overkill
17:49:36 <UkoeHB> I just mean to reduce collision rates*
17:50:46 <tevador> that's a lot of blockchain bloat just to make merchants spend a bit less on development
17:50:51 <jberman[m]> collisions are possible across any scheme we're looking at, no? I don't see how in any scheme, someone can without fear successfully generate random subaddresses without checking for collisions
17:51:07 <rbrunner> I think I have through the info in the gist more thourougly than I did so far, I suspect I have some gaps in my understanding
17:51:52 <tevador> I don't think avoiding collisions when randomly generating wallet addresses should the the goal.
17:52:04 <rbrunner> tevador: good arguments IMHO
17:52:38 <jberman[m]> tevador: I agree
17:52:52 <rbrunner> Maybe that possible goal turns out to be a mere detraction
17:54:30 <rbrunner> But then again, if people generate subaddresses, say, "sensibly", how robust must our output discovery be?
17:55:26 <rbrunner> Will we ever not catch one?
17:55:31 <rbrunner> Realistically
17:55:35 <tevador> AFAIK the github repo gets a lot of issues like "wrong wallet balance" etc.
17:55:50 <tevador> all of that would be gone with this scheme
17:56:12 <rbrunner> True, like Reddit, but at least there I have the impression it's almost simply restore height.
17:56:32 <tevador> https://github.com/monero-project/monero/issues/8138
17:56:36 <rbrunner> And not people fooling around with "exotic" subaddresses, far out or otherwise
17:56:39 <jberman[m]> here's a recent one: https://github.com/monero-project/monero/issues/8138
17:57:17 <jberman[m]> I think the added cost of 8 bytes per output for robust subaddress discovery is a solid cost
17:57:26 <rbrunner> Which could solve with just using suitable startup parameters?
17:57:28 <jberman[m]> And deprecating accounts is something I'd imagine would need community feedback on
17:58:14 <tevador> we don't want to deprecate accounts, that was never proposed by anyone AFAIK
17:58:18 <jberman[m]> well everything needs community feedback obviously, but more knowledge on how accounts are used from community members would help
17:58:25 <UkoeHB> 'suitable startup parameters' will always be a hacky solution prone to edge cases
17:58:43 <rbrunner> Sure, but if I understand correctly there are ways to keep accounts and still simplify things like key generation / handlich right?
17:58:54 <tevador> the proposal was to deprecate account-level wallets in jamtis
17:59:33 <tevador> e.g. I can create a wallet that can only access account number 1
18:00:08 <rbrunner> Ah, now I understand that. That does sound like a little overkill, at first hearing.
18:00:16 <rbrunner> IMHO
18:00:24 <UkoeHB> what is overkill?
18:00:32 <tevador> Was my comment not clear? https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4026264
18:00:37 <rbrunner> To have such fine-grained view wallet types?
18:01:16 <rbrunner> No, I think the comment is clear, I should have going back to look up the tiers ... my bad probably ...
18:02:06 <rbrunner> I mean, only few people use accounts, how many people then will use a view-only wallet that is restricted to a single account?
18:02:51 <tevador> It was originally meant as a feature for merchants and I thought it had no downsides, but it turned out to have downsides.
18:05:15 <rbrunner> Personally I don't have a problem if those account-only view wallets turn out to be nothing mere than a fleeting dream :)
18:05:15 <jberman[m]> "and it would be up to the wallet how that address space is divided." -> in other words, a wallet can say "the first 1000 addresses are -> account 1, next 1000 addresses are account 2" etc. something like that but with more sensible figures? is that how accounts would be kept?
18:06:32 <tevador> exactly
18:07:00 <rbrunner> Good. I was also understanding it this way, and I became convinced today that would work out.
18:07:04 <tevador> the main point is that the addressing scheme would become independent of how accounts are defined (and if they are defined)
18:07:04 <UkoeHB> right now the 64-bit address is mapped into 2 32-bit address/subaddress indices; that mapping is wallet-defined
18:07:28 <UkoeHB> 64-bit address index*
18:07:33 <rbrunner> If the reference implementation goes ahead and proposes something sensible that people then follow, except if they have good reasons not to
18:08:05 <rbrunner> No need to hard-code this so deep, even into the blockchain like today
18:08:49 <jberman[m]> I follow, I like
18:09:03 <tevador> OK. So I will update the proposal not to assume any particular structure for the address index. 56-bit indexes also seems sensible to me
18:09:16 <UkoeHB> no objections from me
18:10:15 <UkoeHB> is there a consensus about the 8-byte encrypted address tag? do we need more feedback (not many attendees today)?
18:11:11 <rbrunner> Hard to say, with the gaps in my understanding I detected today ...
18:11:30 <rbrunner> A bit out my league :)
18:12:28 <jberman[m]> I like em
18:14:07 <UkoeHB> Well, maybe there are not strong negative feelings. tevador if you are on-board and willing, it might be fine to add the 8-byte tags to jamtis. The final iteration of jamtis will require and get a lot more scrutiny.
18:14:42 <UkoeHB> We are past the hour now, so I will call the meeting here. Thanks for attending everyone.
18:14:55 <Rucknium[m]> Are we getting closer to a "menu" that would be understandable for merchants, exchanges, wallet developers, and users?
18:14:58 <rbrunner> Very interesting today, thanks
18:15:58 <tevador> I think we are converging on a proposal that might be close to final
18:16:44 <tevador> Just give me some time to update the gist
18:16:59 <UkoeHB> Yeah the only open question in my mind is exact semantics for the reference implementation of accounts/addresses.
18:20:49 <UkoeHB> After consulting a thesaurus... 'address category' is probably the best alternative (just 'category' on the user-facing side) :)
18:23:35 <UkoeHB> I want to capture that an 'account' doesn't have any strict significance. They are more like collections/groups of addresses for organizing your balance...
```

# Action History
- Created by: Rucknium | 2022-01-12T00:48:58+00:00
- Closed at: 2022-01-18T17:17:50+00:00
