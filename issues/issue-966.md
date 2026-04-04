---
title: Monero Research Lab Meeting - Wed 14 February 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/966
author: Rucknium
assignees: []
labels: []
created_at: '2024-02-09T14:16:59+00:00'
updated_at: '2024-09-22T05:44:17+00:00'
type: issue
status: closed
closed_at: '2024-02-22T14:51:03+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Discuss: [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78)

3. Any other business

4. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#965 

# Discussion History
## jeffro256 | 2024-02-09T16:38:43+00:00
As for the the timelocks, I would like to specifically discuss whether or not banning by relay rule until the next network upgrade is an effective short-term solution. I obviously think that it is, if nothing else, a way to reduce the propagation, and if we're committed to deprecating it in the future, this is a step we should take even if it's not perfect. Also, just removing the ability of the user to craft timelocked transactions in the core wallet software will likely reduce the number on-chain, even if no network or relay rules were modified. 

Secondly, I want to toss up the idea of a small modification to the consensus rules also related to the unlock time. In short, I want to make `Blockchain::get_adjusted_time()` monotonic (barring reorgs) on the next network upgrade. The reason for this is that if you have time-locked outputs in your input rings, decoy or true-spend, and you send a transaction into the mempool, it may be accepted now but actually be invalid for several blocks based on the timestamps of the new blocks on top of the chain pushing the value of `Blockchain::get_adjusted_time()` into the past. This is because of these lines: https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/cryptonote_core/blockchain.cpp#L4029-L4035. They take into account the latest block timestamp instead of only the median timestamp, and take the minimum between them. If we only make the adjusted time a function only of the median timestamp, we will have a monotonic clock since the median timestamp increases monotonically. This means that if any transaction output is unlocked now, it will always be unlocked in the future if there isn't a reorg.

Thirdly, I'd like to discuss disallowing v1 transactions for "unmixable" input amounts in the next network upgrade. The reason for this is that the output amounts of v1 transactions obviously aren't confidential, which reduces overall network privacy. And since CLSAG signatures can still work on a ring of size 1, this shouldn't lead to anyone having their dust locked like with MLSAG signatures. There have only ever been 462 v1 transactions since Hardfork v6 in September 2017 as of the time of this writing.

Fourthly, I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network. On [this line](https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d5/src/cryptonote_core/blockchain.cpp#L2122) of `Blockchain::handle_alternative_block()`, we can see that the blockchain code will attempt to switch to an alternative chain if the cumulative work is strictly higher than the main chain. It is important to note that the work calculated for a given block is NOT a function of the contents of that specific block, but rather the timestamps of a window of blocks before that block. This means that two individuals who are mining a top block for the same chain will create blocks who have equal cumulative work. If these two individuals propagate their blocks at roughly the same time, this will leave the network temporarily split with two different top blocks. There should be a deterministic, fair method to decide between these two chains. This way, shallow alternate chains are handled quickly and all mining participants can mine on the same chain. Some methods could include picking the "smaller"/"larger" block ID, "smaller"/"larger" PoW hash, etc. 

## Cactii1 | 2024-02-10T00:05:42+00:00
Monero should not be removing functionality, it should be adding functionality.

Time locks have the potential to be used for important things.

One example: I'm the owner of playmonero.com and I could use that feature to allow a player to decide when a bet is placed. No interaction from me, other than programing it into the game (right now this is not implemented and it ignores any time locked bets).

The point is that there are use cases for it. Maybe these things are currently apparent, but someone else might be able to think of something.

Don't remove it if it's not broken.

## jeffro256 | 2024-02-10T00:33:58+00:00
> One example: I'm the owner of playmonero.com and I could use that feature to allow a player to decide when a bet is placed.

You could send the desired time info off-chain so that this transaction is indistinguishable from other transactions. You could also encode it in the bottom digits of the amount. You could encrypt it in `tx_extra`. There's a lot of ways to transmit data which don't involve time-locking funds. 

> Don't remove it if it's not broken.

But that's the point: it *is* broken, insofar as it actively makes the main use case of Monero, digital cash, worse. Even if you don't utilize the `unlock_time` feature, you must always be aware of it when you process payments, select decoys, or select inputs, else you will suffer the consequences. 

> The point is that there are use cases for it. Maybe these things are currently apparent, but someone else might be able to think of something.

If you can find a novel use case which can't be approximated by time-lock puzzles or an interactive third-party service, please post it here or in the original thread.

At any rate, I hope to see you in Wednesday's meeting!

## iamamyth | 2024-02-10T17:14:40+00:00
> But that's the point: it is broken, insofar as it actively makes the main use case of Monero, digital cash, worse. Even if you don't utilize the unlock_time feature, you must always be aware of it when you process payments, select decoys, or select inputs, else you will suffer the consequences.

Just to expand on this point: Cash is *never* unspendable; the protocol-enforced 10-block timelock reflects the drift between ideal behavior versus implementation realities. The timelock mechanism other protocols support (and implementors actually use) conditions a transfer's execution on the timelock, rather than executing the transfer unconditionally and then locking the funds, meaning the funds are never unspendable.

## Rucknium | 2024-02-15T21:11:13+00:00
Log

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/966     

> __< d​angerousfreedom:matrix.org >__ Alex | LocalMonero | AgoraDesk: Yes     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< d​angerousfreedom:matrix.org >__ Hi     

> __< a​lex:agoradesk.com >__ hi     

> __< j​effro256:monero.social >__ Howdy     

> __< rbrunner >__ Hello     

> __< xFFFC0000 >__ hi everybody     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. And some empirical analysis of unlock time...posting....now     

> __< j​effro256:monero.social >__ Working on seraphis tx serialization     

> __< xFFFC0000 >__ me: locking mechanism for blockchain.cpp      

> __< r​ucknium:monero.social >__ Discuss: Removing/Fixing/Encrypting monero's timelocks https://github.com/monero-project/research-lab/issues/78     

> __< rbrunner >__ I can give a short report about my contribution, a Reddit post: https://old.reddit.com/r/Monero/comments/1amomjj/timelocks_let_us_finally_retire_a_rarely_used_and/     

> __< r​ucknium:monero.social >__ We don't have to decide on time locks today. I hope we can finish discussion by 18:00, but if we really need it we can extend the time to 18:30 at teh most.     

> __< plowsof >__ Thanks for current usage stats Rucknium     

> __< rbrunner >__ The post got a fair share of attention and comments. Noteworthy are the 99% upvotes     

> __< rbrunner >__ I didn't actually count, but I would guess 8 or even 9 out of every 10 comments are pro removal     

> __< rbrunner >__ IMHO nothing really surprising surfaced, e.g. a novel use of timelocks that so far nobody ever thought of     

> __< r​ucknium:monero.social >__ Here are the usage stats and some estimates of the privacy impact on users who are creating txs with custom lock times: https://github.com/monero-project/research-lab/issues/78#issuecomment-1944249619     

> __< rbrunner >__ Well, that's not a guess, more of an estimate about reading everything     

> __< a​lex:agoradesk.com >__ If I may, I'd like to point out how we use timelocks occasionally and how to us it's a good feature.     

> __< a​lex:agoradesk.com >__ Sometimes, we ban a certain user permanently from our platform. Sometimes, that user tries to return to the platform. We catch them and warn them not to return again or there will be consequences.     

> __< r​ucknium:monero.social >__ On usage, I have findings that are similar to what TheCharlatan found many years ago. 95% of custom unlock times have no effect since the wallet developer(s) do not understand that block height is absolute. And I have new findings on the privacy impact. The real spend can be correctly guessed in 34-91% of the custom unlock times that I evaluated.     

> __< a​lex:agoradesk.com >__ They ignore us and return to our platform. In these cases, we take the XMR that they placed in the arbitration bond and send it to them in a timelocked transaction to disincentivize them from trying to return again.     

> __< a​lex:agoradesk.com >__ It's quite effective.     

> __< j​effro256:monero.social >__ It could be that the developers DO understand that the height is absolute, but they're putting other meta information in that field     

> __< plowsof >__ USDT can even close accounts. Also effective lol     

> __< plowsof >__ The fact that you can punish people (deserving or not) is terrible     

> __< r​ucknium:monero.social >__ So this is a "light punishment" use of custom unlock time. Instead of extreme punishment of not sending them any XMR at all.     

> __< rbrunner >__ Well, that does have a novel edge, as far as I am concerned     

> __< r​ucknium:monero.social >__ Could there be a compromise? Maybe wallet2 can consider custom-locked outputs as "not received" by default. Depends on how much other wallets follow wallet2 I guess.     

> __< rbrunner >__ But anyway, I think we should be careful, it's not only the question whether those timelocks have uses - they have - but whether they are net positive     

> __< a​lex:agoradesk.com >__ Additionally, I can think of cases where a person might know ahead of time that they will be entering a dangerous situation (travel, jail, mandatory conscription, etc) and want to ensure that their coins will not be spent until they are out of the situation, so they send themselves a timelocked tx.     

> __< j​effro256:monero.social >__ localMonero's use case can be replicated by choosing to send the funds later or sending to a time lock puzzle     

> __< j​effro256:monero.social >__ That use case too can also be solved with a time lock puzzle     

> __< rbrunner >__ Yeah, and like the use case with rents, subscriptions and similar pay-ahead things: Very dangerous if circumstances change, and the XMR absolutely can't     

> __< a​lex:agoradesk.com >__ Choosing to send the funds later is quite problematic as the person might start to claim that we never intend to send them and start some sort of reputation damaging action. A timelocked tx prevents that.     

> __< j​effro256:monero.social >__ You could send the funds to them in a time lock puzzle and prove that thr y will be able to access the funds after s bounded amount of computation     

> __< a​lex:agoradesk.com >__ The main concern with timelocks is that it's tx-based and not output-based, which, I agree, can lead to serious problems if the person utilizing them is not aware of this and doesn't send the desired timelock to a separate wallet first to ensure separation.     

> __< rbrunner >__ Well, can't they claim coercion, which also can be an offense, and damage your reputation nevertheless?     

> __< a​lex:agoradesk.com >__ Their claim won't have credit since there are records of them being banned and warned not to return.     

> __< a​lex:agoradesk.com >__ You'll have to PM me with the details about the time lock puzzle, not sure how to implement it.     

> __< rbrunner >__ You have the same records if you just send them later ... but whatever.     

> __< plowsof >__ Wheres the sense of power/control in that?      

> __< a​lex:agoradesk.com >__ We have the same records, but while the coins are with us the person can still claim we're just keeping them. With a timelocked tx they can't.     

> __< d​angerousfreedom:matrix.org >__ Are you aware of someone applying it in Monero?     

> __< rbrunner >__ Fair enough.     

> __< rbrunner >__ The way I see the matter after reading the comments on Reddit and on jeffro256's PR https://github.com/monero-project/monero/pull/9151: Yes, there are certainly usecases, but for me they in no way outweigh the negatives     

> __< j​effro256:monero.social >__ The main concerns with time locks for 99.9% users is that 1) receiving time locked funds leads to confusion why it isnt spendable 2) you can't pick locked decoys which degrades on chain privacy and makes making non fingerprint able decoy selection harder 3) you cant pick locked decoys which can open you up to privacy attacks from an untrusted daemon 4) it makes transactions less u<clipped messag     

> __< j​effro256:monero.social >__ niform which degrades on chain privacy     

> __< rbrunner >__ By the way, I reviewed that PR, looks good, it would probably no problem to activate it     

> __< rbrunner >__ (technically)     

> __< a​lex:agoradesk.com >__ I also disagree over the notion that this is especially unintuitive for developers. Even bitcoin has timelocks. It may be a question of a lack of documentation, but to me it seems rather weird that a developer scanning for deposits to the wallet using the JSON-RPC would just completely ignore the "unlock_time" parameter staring right at him. Perhaps the dev is very inexperienced.     

> __< r​ucknium:monero.social >__ jeffro256: Isn't (2) and (3) true for coinbase txs, which have a 60 block lock? I checked a few block heights. The share of the probability mass of the decoy selection algorithm "blocked" by coinbase lock time is 0.2% to 2.0%     

> __< j​effro256:monero.social >__ No but you could do this completely off-chain, no hacky consensus rules required     

> __< a​lex:agoradesk.com >__ The unintuitive part is that the lock is per TX as opposed to per output.     

> __< r​ucknium:monero.social >__ ^ At least one Monero payment channel proposed protocol uses time lock puzzles. Did they write the code to implement it? I don't think so.     

> __< plowsof >__ Some devs use monero libraries which may not unlock_time aware      

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ "unintuitive" is a very mild name for a completely braindead and borderline-unusable design, IMHO     

> __< plowsof >__ The problem with this PR not disabling with a hardfork is that devs are more likely to not care about unlock_time      

> __< rbrunner >__ Well, that's probably a separate discussion, should be reach consensus to remove the feature at all     

> __< rbrunner >__ *should we     

> __< j​effro256:monero.social >__ However, if you were going to use a feature which picks non-coinbase anyways like that PR I wrote, you would be able to tell where an output is coinbase unlocked before you even request it based on its height     

> __< a​lex:agoradesk.com >__ I'm not here to say that timelocks are essential, I'm merely offering our usecase for it, as it seems that nobody else could come up with usecases.     

> __< a​lex:agoradesk.com >__ If jeffro256 could explain to me how to implement the time lock puzzle then our usecase won't be relevant anymore.     

> __< plowsof >__ Mochi101 recently found many big instant swap sites unaware of unlock time. We then added a red warning to the rpc docs     

> __< r​ucknium:monero.social >__ FWIW, the privacy problem scales up with usage. Right now usage of custom unlock time is very low. Nonstandard txs fees, which about 5% of txs use now I think, are a much bigger problem.     

> __< rbrunner >__ Nobody indeed came up with that, as far as I could see. But earlier discussions are full of mentions of "self discipline" approaches, for example     

> __< rbrunner >__ Or as already mentioned subscriptions, regular "payouts" (unlocking in waves, so to say) cases     

> __< rbrunner >__ But that's about it.     

> __< plowsof >__ For me localmonero being able to punish people is precisely a reason to remove it      

> __< rbrunner >__ lol     

> __< r​ucknium:monero.social >__ The ability to punish can promote good outcomes. That's about half of game theory.     

> __< a​lex:agoradesk.com >__ With respect to big instant swap sites, their devs are probably subpar. Seeing the unlock_time in the API is trivial and given that timelocks are present most cryptos it's not something that they'd never think about. Sounds like a bad library or something.     

> __< plowsof >__ The best use case for unlockntime.isnt going to "save" it if its provably broken and bad for privacy      

> __< rbrunner >__ Sure. If all were roses with timelocks except that subpar devs don't understand them, then yeah, let's start an education push. But that's not the case.     

> __< j​effro256:monero.social >__ If I find a library that does it already I will send it to you. The general idea behind the math is pretty simple tho: you basically just make a small RSA ring and then try to brute force the secret key. It can be provable before you do it that there is 1 solution because of the way RSA is structured     

> __< a​lex:agoradesk.com >__ Yeah it's not like we're out to get people. We just want various types of exploiters to stay away from our platform. This is a minimally invasive and soft way of effectively doing it.     

> __< a​lex:agoradesk.com >__ Our devs were aware of timelocks in XMR from the getgo, way back in 2017. So are most devs I feel. Again, I'm not here to judge people, and I agree that simpler is better. I'm just saying that timelocks are not weird in crypto.     

> __< r​ucknium:monero.social >__ It sounds like we may have a viable compromise if a time lock puzzle protocol is implemented for Monero. (But that costs labor time.)     

> __< a​lex:agoradesk.com >__ Now, just because something is not weird in crypto doesn't mean it's desireble in XMR     

> __< rbrunner >__ Maybe it turns out like with those "Mordinals": On our own we couldn't reach consensus about removing or limiting tx_extra. It took an actual attack to move us.     

> __< plowsof >__ Even the argument that subpar devs are unaware of it doesnt matter.. it is broken and bad for privacy      

> __< rbrunner >__ Maybe somebody should send around thousands of timelocked dust transactions to all ecosystem players ...     

> __< r​ucknium:monero.social >__ Does Bitcoin or its cousins have the same type of time lock as Monero? They have a different type, I know. But they also have one like Monero?     

> __< a​lex:agoradesk.com >__ That's fine. I'm cool with the removal. The simplicty and privacy of the XMR protocol is more important than our use case. I just wanted to mention it.     

> __< rbrunner >__ I don't know, but you would think there must be stories like locking for thousands of years by accident then, which I *never* heard     

> __< r​ucknium:monero.social >__ rbrunner: I don't think dust amounts will matter much. The problem happens when you think you have a legitimate large payment for something and take action based on that false belief.     

> __< a​lex:agoradesk.com >__ There's a per-address timelock. Meaning you send BTC to a p2sh address where the script says you can only spend the coins at this address after a certain time.     

> __< r​ucknium:monero.social >__ rbrunner IIRC, you can only lock for 4 years maximum without re-compiling the binaries. So, it's hard to do accidentally     

> __< rbrunner >__ Yes, it would need a dedicated attacker, just any script kiddie won't do     

> __< rbrunner >__ Anyway, I surely hope that we will reach consensus on our own this time, without anything bad happening first of course     

> __< r​ucknium:monero.social >__ Maybe a year ago someone said they were paid 10's of XMR in a locked tx. In #monero I think. It's not just a theoretical risk.     

> __< rbrunner >__ I think that non-consensus on tx_extra limits are forever in the blockchain in the form of a few gigabytes of Mordinals rubbish :)     

> __< r​ucknium:monero.social >__ plowsof, do you remember?     

> __< plowsof >__ It was an owner of a swap site iirc .. basically a competitor draining their reserves      

> __< a​lex:agoradesk.com >__ This exact exploit was an immediate consideration for us when we were originally developing our platform. It's trivial to sidestep - just read `unlock_time`.     

> __< r​ucknium:monero.social >__ https://libera.monerologs.net/monero/20230119#c191161  "Hello everyone, I have an exchanger connected to a Monero server. 2 days ago, I saw that 133 Moneros were blocked in my account for a period of 4 years. How is this possible?"     

> __< plowsof >__ Was btcpaysever unlock time unaware      

> __< r​ucknium:monero.social >__ AFAIK, we have no guides about how to make a Monero wallet.     

> __< r​ucknium:monero.social >__ From what I have seen, I would guess that most "third-party" code that receives XMR isn't aware of lock time. Or at least that was the state a year+ ago.     

> __< rbrunner >__ Well, as I said, even with perfect documentation and no more subpar devs around ever timelocks *still* have grave problems     

> __< a​lex:agoradesk.com >__ Yeah, a unified guide of "what to worry about when integrating XMR" would solve most of this I think.     

> __< a​lex:agoradesk.com >__ However, rbrunner is right. If it's a hazard to privacy it should be removed, just like tx_extra.     

> __< plowsof >__ The use cases are motivation for a fixed/real solution     

> __< d​angerousfreedom:matrix.org >__ I never used timelocks so my opinion is irrelevant but I would be in favor of disabling it (for the sake of privacy) for future transactions but not void the current ones that uses it. I think a robust and easy to use multisig would fix many of the timelock issues. One could simply trust a 3rd party (which could be himself) to relay his tx when the time comes. Another example woul<clipped me     

> __< d​angerousfreedom:matrix.org >__ d be using google that offers the possibility to send messages after some inactivity time in your account. So basically there are many ways to handle when to send a transaction in the future that dont need to be on-chain.     

> __< rbrunner >__ That discussion with the victim of the locked XMR on monerologs.net is gold ...     

> __< rbrunner >__ Maybe we should use the remaining regular 10 minutes of meeting time for an attempt to find out where we stand, and where we go from here, i.e. after this meeting?     

> __< r​ucknium:monero.social >__ One or both of Trezor and Ledger had an unlock time "vulnerability".     

> __< a​lex:agoradesk.com >__ I think that existing timelocks should be honored, but for the sake of simplifying XMR and strengthening privacy they should be removed, assuming that time lock puzzles are a practical solutions as jeffro256 says.     

> __< rbrunner >__ In any case, as mentioned, at least coding is almost done. A second review would probably be good.     

> __< j​effro256:monero.social >__ I'm of the same opinion: no more new non-zero tx unlock times, but honor the old unlock times.     

> __< r​ucknium:monero.social >__ I don't think we should ask jeffro to implement time lock puzzles because he is working on tasks with higher priority. But if we could have the off-chain time lock puzzles working, that would be a good compromise.     

> __< rbrunner >__ Ditto     

> __< a​lex:agoradesk.com >__ Not honoring the existing timelocks will lead to a crisis of confidence. If the XMR protocol won't honor one contract, why would it honor others?     

> __< rbrunner >__ Yes. I don't think anybody voted for removing all locks, period.     

> __< rbrunner >__ The "Free the locked XMR" movement :)     

> __< j​effro256:monero.social >__ I wanted to talk about a slight change to the unix-time-based unlock times: Secondly, I want to toss up the idea of a small modification to the consensus rules also related to the unlock time. In short, I want to make Blockchain::get_adjusted_time() monotonic (barring reorgs) on the next network upgrade. The reason for this is that if you have time-locked outputs in your input rin<clipped messag     

> __< j​effro256:monero.social >__ gs, decoy or true-spend, and you send a transaction into the mempool, it may be accepted now but actually be invalid for several blocks based on the timestamps of the new blocks on top of the chain pushing the value of Blockchain::get_adjusted_time() into the past. This is because of these lines: https://github.com/monero-project/monero/blob/059028a30a8ae9752338a7897329fe8012a310d<clipped messag     

> __< j​effro256:monero.social >__ 5/src/cryptonote_core/blockchain.cpp#L4029-L4035. They take into account the latest block timestamp instead of only the median timestamp, and take the minimum between them. If we only make the adjusted time a function only of the median timestamp, we will have a monotonic clock since the median timestamp increases monotonically. This means that if any transaction output is unlocke<clipped messag     

> __< j​effro256:monero.social >__ d now, it will always be unlocked in the future if there isn't a reorg.     

> __< j​effro256:monero.social >__ From this comment: https://github.com/monero-project/meta/issues/966#issuecomment-1936243293     

> __< j​effro256:monero.social >__ It might not be worth the effort, but it make the behavior of the like 8 locked transfers more reliable     

> __< rbrunner >__ Maybe xFFFC0000 would be ready to look into these puzzles? So jeffro256 can continue with his indeed essential things.     

> __< xFFFC0000 >__ Sure. I can take a look. But keep in mind mooo asked me to take a look at locking for blockchain.cpp and I am right now working on fixing locking mechanism on blockchain.cpp. Right after than I can jump into the puzzle thing. which should not take long.      

> __< rbrunner >__ Nice.     

> __< a​lex:agoradesk.com >__ Thanks for taking care of our usecase guys <3     

> __< rbrunner >__ All in all, things look a lot less controversial than back then with tx_extra. Maybe we will succeed this time.     

> __< r​ucknium:monero.social >__ Would monotonic block time help anything else besides unlock time? And "Median timestamp increases monotonically" is that because of consensus rules on how much mined blocks' timestamps can differ from neighboring blocks?     

> __< j​effro256:monero.social >__ No. Yes     

> __< r​ucknium:monero.social >__ AFAIK, the downside of time lock puzzles is that time-to-solution depends on CPU speed, so it's not as precise as depending on block height. But for a "punishment" use case, that is probably not a problem.     

> __< j​effro256:monero.social >__ new incoming block timestamps cannot be less than the median of the last 60, which increases median of the next 60     

> __< j​effro256:monero.social >__ Yes for punishment and self-control use cases, which is most, the time doesn't have to be exact IMO     

> __< r​ucknium:monero.social >__ I think we don't have to extend the meeting time. The result is that xFFFC0000 will evaluate implementing an off-chain time lock puzzle as a compromise, when he has time.     

> __< j​effro256:monero.social >__ There's another couple of things id like to discuss if people are willing     

> __< j​effro256:monero.social >__ From that same comment I linked: Thirdly, I'd like to discuss disallowing v1 transactions for "unmixable" input amounts in the next network upgrade. The reason for this is that the output amounts of v1 transactions obviously aren't confidential, which reduces overall network privacy. And since CLSAG signatures can still work on a ring of size 1, this shouldn't lead to anyone havin<clipped messag     

> __< j​effro256:monero.social >__ g their dust locked like with MLSAG signatures. There have only ever been 462 v1 transactions since Hardfork v6 in September 2017 as of the time of this writing.     

> __< r​ucknium:monero.social >__ Ok we can continue     

> __< rbrunner >__ Looks like stuff for a handful of meetings, if done carefully, IMHO.     

> __< j​effro256:monero.social >__ We can end the meeting officially and discuss this laster     

> __< r​ucknium:monero.social >__ Ok. --- Meeting end ---     



## xmrrmxntom | 2024-09-22T05:44:16+00:00
@Cactii1 

<h1>A Plea to Restore a Crucial Feature in XMR</h1>
<p>As a computer science student and a long-time follower of XMR & Dr. Daniel Kim (sweetwater.consulting), I'm compelled to share my thoughts on a feature that I believe is <strong>important</strong> to the value proposition of XMR. I've created an account specifically to express my disappointment and frustration with the removal of the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature.</p>
<h2>A Personal Journey with XMR</h2>
<p>I've been following the XMR project since 2018, and its value proposition was evident to me even back then. However, I wasn't technical enough to fully appreciate its features. This year, I became proficient enough to run a full node and use the CLI, which is when I discovered the <code>locked_transfers</code> and <code>locked_sweep_all</code> features. I immediately utilized them, and they have been <strong>invaluable</strong> to me.</p>
<p>As someone who has impulsively sold assets like NVIDIA, BTC, and TSLA before they reached their full potential, I've come to realize that XMR is a <strong>long-term play</strong> that will appreciate in value over the next 5-20 years. The ability to lock transactions for an extended period has been a <strong>game-changer</strong> for me, allowing me to make sacrifices that my future self will appreciate.</p>
<h2>The Value of Locked Transactions</h2>
<p>The <code>locked_transfers</code> and <code>locked_sweep_all</code> feature was a <strong>unique selling point</strong> for XMR, offering me the ability to make long-term commitments to the blockchain. By removing this feature, we're depriving users of a valuable tool that would help them appreciate the embedded on-chain hodl properties of the XMR blockchain.</p>
<h2>A Call to Action</h2>
<p>I urge the XMR community to reconsider the removal of this feature and to implement safeguards to prevent similar decisions in the future. Specifically, I request:</p>
<ol>
<li><strong>Reinstatement of the feature</strong>: Bring back the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature to allow users to make long-term commitments to the blockchain.</li>
<li><strong>Safeguards for feature deprecation</strong>: Establish a formal, non-trivial process or procedure to determine whether a feature should be deprecated, ensuring that user feedback and concerns are taken into account and valued.</li>
<li><strong>Improvement or alternative</strong>: If the feature cannot be reinstated, explore alternative solutions that would provide similar functionality and benefits to users.</li>
</ol>
<h2>Conclusion</h2>
<p>As more users join the XMR community, they will come to appreciate the unique properties of the blockchain. I firmly believe that the <code>locked_transfers</code> and <code>locked_sweep_all</code> feature helps users <strong>HODL</strong> with the long-term success of XMR. I hope that my plea will be heard, and we can work together to restore this important feature.</p>
<h2>A Final Appeal</h2>
<p>I've gone from hearing about XMR as the real <strong>privacy-focused vision</strong> of BTC, to buying some XMR on an exchange, to self-custodying on Exodus wallet, and finally to downloading and running the CLI. XMR is <strong>beautiful</strong>, and it's <strong>idealistic</strong>. Please keep or reimplement this feature.</p>

https://reddit.com/r/Monero/comments/mwrm6g/how_to_lock_send_future_monero_to_yourself_with/

<p>This was the post and feature that motivated me to dedicate a weekend last semester to read the documentation, compile from source, and use the CLI.</p>
<p>…Please keep this feature…</p>

# Action History
- Created by: Rucknium | 2024-02-09T14:16:59+00:00
- Closed at: 2024-02-22T14:51:03+00:00
