---
title: Monero Research Lab Meeting - Wed 21 February 2024, 17:00 UTC
source_url: https://github.com/monero-project/meta/issues/970
author: Rucknium
assignees: []
labels:
- meeting
- MRL
created_at: '2024-02-21T15:37:58+00:00'
updated_at: '2024-02-27T17:28:00+00:00'
type: issue
status: closed
closed_at: '2024-02-27T17:28:00+00:00'
---

# Original Description
Location: [Libera.chat, #monero-research-lab](https://libera.chat/) | [Matrix](https://matrix.to/#/#monero-research-lab:monero.social?via=matrix.org&via=monero.social)

[Join the Monero Matrix server if you don't already have a Matrix account.](https://forum.monero.space/d/79-how-to-join-the-monero-core-team-matrix-server-web)

Time: 17:00 UTC [Check in your timezone](https://www.timeanddate.com/worldclock/converter.html?iso=20211027T170000&p1=1440)

Main discussion topics:

1. Greetings

2. Updates. What is everyone working on?

3. Discuss: [Removing/Fixing/Encrypting monero's timelocks](https://github.com/monero-project/research-lab/issues/78)

4. @jeffro256 ["In short, I want to make `Blockchain::get_adjusted_time()` monotonic (barring reorgs) on the next network upgrade."](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

5. @jeffro256  [I'd like to discuss disallowing v1 transactions for "unmixable" input amounts in the next network upgrade.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

6. @jeffro256 [ I think we can improve how the nodes handle alternative blocks in a way that might naturally reduce the number of reorgs on the network.](https://github.com/monero-project/meta/issues/966#issuecomment-1936243293)

7. Any other business

8. Confirm next meeting agenda


Please comment on GitHub in advance of the meeting if you would like to propose an agenda item.

Logs will be posted here after the meeting.

Meeting chairperson: Rucknium

Previous meeting agenda/logs:

#966 

# Discussion History
## Rucknium | 2024-02-27T17:28:00+00:00
Log:

> __< r​ucknium:monero.social >__ Meeting time! https://github.com/monero-project/meta/issues/970     

> __< r​ucknium:monero.social >__ 1) Greetings     

> __< v​tnerd:monero.social >__ Hi     

> __< rbrunner >__ Hello     

> __< h​into.janaiyo:matrix.org >__ hello     

> __< r​ucknium:monero.social >__ jeffro256: Ping because you have items on the agenda     

> __< j​effro256:monero.social >__ Howdy     

> __< j​effro256:monero.social >__ Thanks 4 ping     

> __< r​ucknium:monero.social >__ 2) Updates. What is everyone working on?     

> __< r​ucknium:monero.social >__ me: OSPEAD. I did some preliminary calculations of the privacy impact of a transition period to a new decoy selection algorithm without a hard fork. The numbers do not look as bad as I expected.     

> __< v​tnerd:monero.social >__ Me: finished some zmq hardening stuff in lws, and switched to updating an old Dane/TSLA branch for wallet verification. Not sure if anyone will use it, but it allows tls cert verification via dnssec instead of root ca     

> __< j​effro256:monero.social >__ me: working on changes to seraphis lib that would make the new transaction class more non-malleable, and combining serialization processes of old and new txs     

> __< h​into.janaiyo:matrix.org >__ working on cuprate's db still - i believe i've found a potential data race in `monerod`'s db code and wanted some opinions     

> __< r​ucknium:monero.social >__ jeffro256: Are Seraphis txs more or less malleable than current Monero txs?     

> __< 0​xfffc:matrix.org >__ me: done with the rw lock. I am starting to look at lmdb backend for wallet.     

> __< h​into.janaiyo:matrix.org >__ i will create a more clear issue on it in the core repo later today - i'm eating right now :)     

> __< j​effro256:monero.social >__ Nothing to do with an inherent Seraphis property, just how fields are coded in the Seraphis PoC. I have the same issue with the format that `rctSigsPrunable` has where some fields are redundant and don't effect serialization and identification, which can lead to subtle future bugs     

> __< r​ucknium:monero.social >__ 3) Discussion     

> __< j​effro256:monero.social >__ 0xFFFC: I can't tell you what to do, but I personally wouldn't recommend trying to add lmdb to wallet2 since most of that work will be scrapped in the near future with the seraphis wallet     

> __< j​effro256:monero.social >__ Would anyone like to discuss point 4 about making `get_adjusted_time()` monotonic when there's no reorgs?     

> __< j​effro256:monero.social >__ It requires a hardfork BTW     

> __< rbrunner >__ Ah, ok, "wallet" does not yet have an LMDB backend of course. Should probably be discussed further, yeah     

> __< r​ucknium:monero.social >__ Yes. Any hint why it was set to be non-monotonic in the first place?     

> __< r​ucknium:monero.social >__ And what do other blockchains do?     

> __< j​effro256:monero.social >__ There's this comment in the code:     

> __< j​effro256:monero.social >__ > // return minimum of ~current block time and adjusted median time     

> __< j​effro256:monero.social >__ > // we do this since it's better to report a time in the past than a time in the future     

> __< j​effro256:monero.social >__ Sounds like their rational was that it would be better that unlock_time'ed outputs stay locked for longer? I don't really understand the motivation behind it     

> __< j​effro256:monero.social >__ Other blockchains don't have an unlock_time like we do ;)     

> __< rbrunner >__ Maybe a dumb question, but is anything of your proposal still revelant after unlock_time is gone?     

> __< r​ucknium:monero.social >__ But don't they use median timestamps for things? And Alex said last week that bitcoin has them     

> __< 0​xfffc:matrix.org >__ I use your advice actually. Thanks. I will contact you to talk about this in detail.     

> __< rbrunner >__ IMHO chances look good that we can get rid of that feature after all     

> __< j​effro256:monero.social >__ No, `get_adjusted_time()` only affects unlock_time'ed txs     

> __< r​ucknium:monero.social >__ Is it irrelevant for the 60 block lock on coinbase outputs since that lock uses block height, not timestamps?     

> __< j​effro256:monero.social >__ Yes we use median timestamps for bounding new timestamps and calculating difficulty, but we use a separate algorithm (`get_adjusted_time()`) for unlocking outputs     

> __< j​effro256:monero.social >__ Yes it is irrelevant for coinbase outputs since their unlock_time is always less than 500 million, so it gets interpreted as a block height, not a timestamp     

> __< j​effro256:monero.social >__ Original PR is here btw: https://github.com/monero-project/monero/pull/6745     

> __< rbrunner >__ Ah, it's not even for *all* such timelocks, only really for the timestamp based ones? That looks pretty unimportant, then, IMHO     

> __< v​tnerd:monero.social >__ 0xFFFC: the wallet was never converted to lmdb because of lack of encryption. I know hyc mentioned adding encryption support to lmdb, but I don't know what happened to that     

> __< rbrunner >__ And as as said, let's nuke those locks anyway :)     

> __< 0​xfffc:matrix.org >__ Yes. I talked to him. He actually added encryption capability just to address this I believe.     

> __< a​lex:agoradesk.com >__ Here's the BIP for OP_CHECKLOCKTIMEVERIFY if y'all need it     

> __< a​lex:agoradesk.com >__ https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki     

> __< j​effro256:monero.social >__ Yes, only for timestamp-interpreted unlock_times. However, we are still honoring the time locks, even if we remove them from further transactions. This change would make it easier for seraphis wallet implementors to confidently provide support for timestamped unlocking of legacy outputs without as much logic     

> __< 0​xfffc:matrix.org >__ jeffro256: what about adding lmdb storage directly to seraphis wallet?     

> __< j​effro256:monero.social >__ The change itself would be pretty tiny in scope, but it would  make the behavior of the small existing timestamp locked outputs more standard     

> __< rbrunner >__ I thought you can count existing timestamp based lock on the blockchain on a single hand? Don't have a link ready however     

> __< hyc >__ LMDB encryption support was added ~4 years ago     

> __< j​effro256:monero.social >__ I'm certainly in favor of adding LMDB support to the seraphis wallet, especially the enote store at some point in the future (as long as it can be encrypted)     

> __< hyc >__ all that was left was to find someone to do the wallet code rewrite     

> __< 0​xfffc:matrix.org >__ hyc thanks \o/     

> __< r​ucknium:monero.social >__ If I understand the unlock time behavior, about 14 txs have used the unix timestamp lock method since the Aug 2022 hard fork: https://github.com/monero-project/research-lab/issues/78#issuecomment-1944249619     

> __< hyc >__ ah, I'm wrong. added it in 2017. 7 years ago.     

> __< r​ucknium:monero.social >__ rbrunner: You will need 3 hands     

> __< rbrunner >__ I see, yes :)     

> __< 0​xfffc:matrix.org >__ Great. Let catch up about this in detail in private discussion. I am done with rwlock. And looking for this to start working on.     

> __< ofrnxmr >__ Rwlock is 9181?     

> __< rbrunner >__ I humble propose to not loose another minute of jeffro256's precious time on those then. No problem if they unlock a day too early, if you ask me ...     

> __< 0​xfffc:matrix.org >__ ofrnxmr yes     

> __< j​effro256:monero.social >__ Just want to point out, since I haven't yet, that the monotonic change would be a -2, +1 line change     

> __< j​effro256:monero.social >__ Actually a little more since we need to check HF version, so it would be like 5 lines total changed     

> __< rbrunner >__ And no "shooting into foot" during the 1 day hardfork transition period?     

> __< j​effro256:monero.social >__ Shouldn't be, since we aren't asserting rules about txs coming into the mempool, just changing how we interpret already on-chain txs, it shouldn't even need a transition period. But I'll double-check that     

> __< rbrunner >__ Those 14 txs do get a lot of attention :)     

> __< j​effro256:monero.social >__ lol yeah edge cases tend to do that. IMO tho, it should be a very targeted and non-controversial change. The absolute delta in unlock time in terms of real-life time should be very small (~10 minutes in worst case), but it helps weird mempool behavior where a transaction is valid and then it temporarily isn't, with no control by user spending those funds or using them as decoys     

> __< j​effro256:monero.social >__ Also, if we choose to move forward and ban future transactions from having non-zero unlock_time, you can bet that new people will construct just to say that they did for fun     

> __< rbrunner >__ May be yes.     

> __< rbrunner >__ Work is done, or almost so, we may well pull it through ...     

> __< r​ucknium:monero.social >__ The decoy issue is a good point. The recipients of the timelocked txs might not try to spend in that narrow problem window, but other users may the outputs as decoys.     

> __< rbrunner >__ So the "waiting for next hardfork" queue will get 1 entry more     

> __< r​ucknium:monero.social >__ jeffro256: You had two other issues to discuss.     

> __< j​effro256:monero.social >__ Another edge case! Disallowing any and all v1 transactions     

> __< rbrunner >__ Sounds a bit heavier as an issue then     

> __< rbrunner >__ That would not lead to any enotes unspendable? Just spendable in a different way?     

> __< j​effro256:monero.social >__ v1 transactions are still allowed when one is spending "dust" amounts and the number of total global outputs with that amount is less than the ring size. This was a good exception when MLSAGs needed at least 2 ring members, but we don't need this rule with CLSAGs, since you can make a ring with 1 member (correct me if wrong). The problem with allowing v1 transactions is that the t<clipped messag     

> __< j​effro256:monero.social >__ ransaction outputs aren't hidden amounts, so the sender privacy chaining from those transactions is bad     

> __< rbrunner >__ So you get as many rings as dust enotes to spend?     

> __< rbrunner >__ Just rings of size 1?     

> __< j​effro256:monero.social >__ Yes     

> __< rbrunner >__ Don't know enough to really assess, but doesn't sound too bad to me     

> __< rbrunner >__ But again, if there are so few such transactions now, the privacy degredation also is nothing wild, I guess     

> __< a​lex:agoradesk.com >__ By the way, jeffro256 , would the timelock puzzle you proposed last week be trustless? In the sense of, how would the recipient of the timelock puzzle not be able to claim that we solved the puzzle ourselves and took the coins back?     

> __< r​ucknium:monero.social >__ This is a privacy improvement for those txs? Would those txs eventually be all spent (if the users did not lose the keys), so the issue slowly disappaers?     

> __< j​effro256:monero.social >__ Alex | LocalMonero | AgoraDesk: I would have to look more carefully, but I assume you would do it the same way coins are transferred to someone's stealth address and they can't claim that you stole them: by adding one of their public keys to the destination point. If only they know their private key to that address, if you add that point to the on-chain destination, you need to al<clipped messag     

> __< j​effro256:monero.social >__ so know the private key of the address to know the private key of the on-chain destination     

> __< a​lex:agoradesk.com >__ Got it.     

> __< j​effro256:monero.social >__ Those txs will eventually all be spent, yes     

> __< rbrunner >__ Hmmm ... I guess that would take considerably more than 5 lines to change and add     

> __< r​ucknium:monero.social >__ I don't know if the risk is worth the reward. Privacy benefit for a very small number of txs, but a possible protocol risk of making them unspendable.     

> __< rbrunner >__ And more time for testing     

> __< plowsof >__ sigh      

> __< j​effro256:monero.social >__ Even if we don't change the consensus rules, it would probably be a good idea to refactor `wallet2::create_unmixable_sweep_transactions()` so that it doesn't create v1 transactions by default for users who are just using that command     

> __< j​effro256:monero.social >__ The consensus code changes would also probably be about 5 lines tho     

> __< rbrunner >__ :)     

> __< rbrunner >__ I just hope that very soon you will run out of such edge cases to unearth. A mountain of coding for Seraphis and Jamtis is waiting     

> __< rbrunner >__ Certainly worth to have a good look at any of them, but not to automatically act and remove then, IMHO     

> __< rbrunner >__ Not sure who would feel tempted to use a method called `reate_unmixable_sweep_transactions`, but well, strange things happen     

> __< j​effro256:monero.social >__ Well okay we can move onto the third topic then: changing the condition under which we switch to alternative chains     

> __< r​ucknium:monero.social >__ We'll end the meeting here. jeffro256 's third item can go into next meeting.     

> __< j​effro256:monero.social >__ kk     

> __< 0​xfffc:matrix.org >__ Thanks everyone     

> __< rbrunner >__ +1     

> __< j​effro256:monero.social >__ rbrunner7: It's accessible by running the `sweep_unmixable` command     

> __< j​effro256:monero.social >__ Thanks everyone     

> __< j​effro256:monero.social >__ I appreciate the time and discussion     

> __< h​into.janaiyo:matrix.org >__ `monerod` db data race I mentioned earlier, comments appreciated - I assume I'm missing outer context that makes this impossible https://github.com/monero-project/monero/issues/9193     

# Action History
- Created by: Rucknium | 2024-02-21T15:37:58+00:00
- Closed at: 2024-02-27T17:28:00+00:00
