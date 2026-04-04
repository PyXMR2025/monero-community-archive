---
title: 'Monero Tech Meeting #140 - Monday, 2025-10-06, 18:00 UTC'
source_url: https://github.com/monero-project/meta/issues/1277
author: rbrunner7
assignees: []
labels: []
created_at: '2025-10-05T08:19:36+00:00'
updated_at: '2025-10-06T19:33:07+00:00'
type: issue
status: closed
closed_at: '2025-10-06T19:33:07+00:00'
---

# Original Description
Location is the Matrix room *No Wallet Left Behind*, #no-wallet-left-behind:monero.social ([Matrix.to link](https://matrix.to/#/#no-wallet-left-behind:monero.social)), Libera IRC channel #no-wallet-left-behind.

You find the log of the last meeting [here](https://github.com/monero-project/meta/issues/1273).


# Discussion History
## rbrunner7 | 2025-10-06T19:33:07+00:00
````
<r​brunner7> Meeting time. Hello! https://github.com/monero-project/meta/issues/1277
<j​effro256> howdy
<j​berman> *waves*
<s​needlewoods> hey
<h​into> hello
<s​yntheticbird> hi
<r​brunner7> Ok, with the "gang" complete, on to the reports from last week!
<j​effro256> stressnet!
<s​needlewoods> worked on some bugs and on `sweep_*` commands, `sweep_single` is still in progress
<s​needlewoods> `grep "\<m_wallet\>" src/simplewallet/simplewallet.cpp -c` gives 23 results
<s​needlewoods> just saw [this comment](https://github.com/seraphis-migration/monero/pull/130#issuecomment-3367470453) about estimated restore height on wallet creation today, will try to look into it this week
<r​brunner7> One bug down, next one waiting, is the impression that I got from afar about stressnet. But that's progress of course
<s​needlewoods> and I have a comment and two questions, can drop the comment now and the questions at the end of the meeting if that's okay!?
<r​brunner7> No problem
<h​into> me: finishing an initial impl proposal for PoWER, should be ready before the next MRL meeting
<h​into> I may as well ask this here, were there any thoughts on ZMQ? It can relay transactions as well: https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/rpc/
<h​into> daemon_handler.cpp#L104-L105
<j​berman> me: basically exclusively stressnet + opened another daemon RPC PR from the integration to main monero repo
<j​effro256> My personal opinion: the restore height, if off-chain, should instead be specified by a "restore date". If the wallet is doing a first-time refresh, then it can guess the height from the date, being conservative.
<sneedlewoods> +1
<o​frnxmr> I think this estimate is likely worse on testnet
<o​frnxmr> On mainnet, it seems to be 20k blocks in the past, which seems OK to me. But if testnet is guessing into the future, thats a problem
<r​brunner7> Sounds reasonable, but if the API offers already a call that accepts a height, maybe we should continue to support that. Asking for a date as a single possibility if offline would be an UI issue.
<ofrnxmr> +1
<spirobel> +1
<j​effro256> Me: basically same as j-berman, working through stressnet issues, monitorying the network health through my personal node, clarifying a lot of details about the implementation of Carrot. We already opened 2 PRs amending consensus rules for the next stressnet
<j​berman> One issue with current is that a wallet doesn't have a daemon connection at that stage of wallet creation, and so it estimates based on hardcoded values in the client
<ofrnxmr> +1
<j​berman> I think the wallet should be able to make a daemon connection, although that's a little tricky still considering GUI's configs
<j​berman> I think that avenue is worth investigating first
<j​effro256> This is a good idea
<r​brunner7> Aren't some parameter values that you may need to connect possibly in the wallet itself?
<j​berman> Yes but I believe current flow is wallet creation before initializing the wallet with those params
<r​brunner7> Anyway, a directed investigation will clear things up
<j​berman> If there is a successful simple way to make the daemon connection first when setting that initial restore height with the estimate (step 1 in that PR linked above), then I think it's ok to remove that secondary check for "if it's a new wallet -> update restore height and then persist that new wallet to keys file" (i.e. no need to even do step 2)
<r​brunner7> On the other hand, if the new PolySeeds with restore height in them become more prevalent, the urgency slowly goes down
<j​berman> Yep
<r​brunner7> On the third hand restoring with seed should be as foolproof as possible. Many people are already pretty stressed out probably when doing so :)
<j​berman> If wallet is offline or cannot establish a connection to the daemon for whatever reason (and is creating a new legacy seed), I think a reasonable estimate could be to just use the latest hardcoded checkpoint
<o​frnxmr> The latest hardcoded checkpoint might be months or even years behind
<o​frnxmr> (Depending on when you last updated the wallet)
<s​pirobel:kernal.eu> its just one http call to get info .json daemon connection sounds so big :)
<r​brunner7> The restore height could easily go further back than the last checkpoint? Maybe I am missing something about the general idea.
<j​berman> this is only applicable when creating a new wallet
<r​brunner7> Ah, I see
<o​frnxmr> creating new wallet while offline needs to set a restore height, but if offline would need to estimate it based on some value
<o​frnxmr> I would assume that it currently uses checkpoint time value + n days * 720 - some number to add a safezone
<o​frnxmr> But testnet times are probably out of wack
<j​effro256> Which is why I think storing a restore date (like Polyseed) is the best long-term solution. But if we can make a connection during wallet init to determine a real height in the chain based on date, then that could be an easy win in the short-term
<r​brunner7> Yeah, and lacking checkpoints on testnet being off more
<ofrnxmr> +1
<j​berman> it's using hardcoded fork v2's values lol:
<j​berman> ```
<j​berman> uint64_t wallet2::get_approximate_blockchain_height() const
<j​berman> {
<j​berman>   // time of v2 fork
<j​berman>   const time_t fork_time = m_nettype == TESTNET ? 1448285909 : m_nettype == STAGENET ? 1520937818 : 1458748658;
<j​berman>   // v2 fork block
<j​berman>   const uint64_t fork_block = m_nettype == TESTNET ? 624634 : m_nettype == STAGENET ? 32000 : 1009827;
<j​berman>   // avg seconds per block
<j​berman>   const int seconds_per_block = DIFFICULTY_TARGET_V2;
<j​berman>   // Calculated blockchain height
<o​frnxmr> "so the estimation is way off. Lets not fix it tho"
<r​brunner7> Well, the estimated numbers of blocks off are right there, no?
<j​berman> that could use an improvement for sure. I'm ok with using latest hardcoded value + some extremely conservative estimate (e.g. assume 4 minute blocks, or give 2 weeks of leeway)
<ofrnxmr> +1
<o​frnxmr> Gotta love the comments. At least they are helpful
<o​frnxmr> on master, blockchain.cpp, line 2083/2084, is a FIXME that asks the qiestion about whether alt chains can have checkpoints. This `is_a_checkpoint` condition doesnt trigger when there is a reorg that comes before receiving a dns checkpoint
<s​needlewoods> will have to test this, but think we may could use [this](https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/wallet/api/wallet_manager.cpp#L250-L258) `WalletManagerImpl::blockchainHeight()` method
<o​frnxmr> tldr: reorg handling is broken, and this is the main blocker for dns checkpoint rollout
<o​frnxmr> 0xfffc and i failed to fix it.. so any help ia greatly appreciated
<r​brunner7> Is there a GitHub issue already documenting this problem, and offering a place for discussion?
<o​frnxmr> Its on the dns checkpoint pr
<r​brunner7> Ok
<o​frnxmr> https://github.com/monero-project/monero/pull/10075
<r​brunner7> By the way, does stressnet already get stressed? Is it already far enough along for spamming to start?
<o​frnxmr> Spamming has started
<o​frnxmr> Txpool is >100mb atm, and someone mined with a lot of hashrate,, so blocks are slow atm
<s​needlewoods> my node already oomed twice
<o​frnxmr> Spackle and i have noticed some issues with block propagation and disconnects
<j​effro256> Really? What amount of RAM is the machine running on?
<o​frnxmr> I also think (unrelated to fcmo/stressnet) that fluffyblocks isnt working properly
<s​needlewoods> 8GB and 1GB swap
<j​effro256> Myabe hitting new serialization / spam limits ?
<s​needlewoods> nothing in the logs though, just vanished
<j​berman> I think this may be it
<o​frnxmr> https://www.zerobin.net/?8bc88251cad0e881#btN+g6cdxiNCkx1ie5T6DmhpzFUne3IzKZDG1uULkaU=
<o​frnxmr> This is what it looks like when i receive a new block
<o​frnxmr> Connection logs here https://matrix.to/#/!sgiUzbrYPvMAvwQKTG/$5K51MAULjli9CJ6UdXFUnM3h0R66L0ti6AHiR66om80?via=monero.social&via=matrix.org&via=xmr.mx
<j​berman> is your node currently still stuck like that?
<o​frnxmr> No, it syncs the block eventually
<r​brunner7> Lol
<o​frnxmr> Sorry, starts a couple msgs above https://matrix.to/#/!sgiUzbrYPvMAvwQKTG/$x8jp2Lbp4hB3GW7M4Pd2SRhZd6jlW6qDLBkWsmlBTHs?via=monero.social&via=matrix.org&via=xmr.mx
<o​frnxmr> I did _not_ have these issues on my 4 host + proxied private testnet
<r​brunner7> Ok, with this all discussed, maybe we continue with your comments and questions, SNeedlewoods
<s​needlewoods> I really like the detailed output for `transfer/sweep` commands with `set print-ring-members 1`. At least the part that shows the enote pub key and enote amount.
<s​needlewoods> So I tested with `alpha1.1` (haven't checked the code), the setting is still present, but after setting it the output didn't change when making a tx (I assume that's because `simple_wallet::process_ring_members()` gets skipped with FCMP++s!?).
<s​needlewoods> Would be nice to have a wallet setting like `print-tx-enotes-in` for the FCMP++ update, which shows some enote info for inputs used in txs like `print-ring-members` does (except for the information about ring members)
<s​needlewoods> Example: Old output for `transfer/sweep` with `print-ring-members` set
<s​needlewoods> `Input 1/3 (<enote public key>): amount=0.005000000000`
<s​needlewoods> Question 1
<s​needlewoods> I considered to add `outputs=<N>` argument to `sweep_below` and `sweep_unmixable` commands. The arg is present in all the other `sweep_*` commands, but on second thought, I assume there is a bigger privacy concern for `sweep_unmixable` e.g. if someone uses this exotic method the resulting tx will already stick out on the blockchain AFAIU. On the other hand merging enotes that were<clipped 
<s​needlewoods>  split before is always a privacy concern, don't know if it would be worse in this case. So any opinions on adding `outputs` arg to `sweep_below` or `sweep_unmixable`?
<s​needlewoods> Question 2
<s​needlewoods> Noticed there is a difference on the confirmation prompt between `transfer` and `sweep_*` in the total amount shown
<s​needlewoods> transfer shows total sent as just the amount, fees _not_ included
<s​needlewoods> sweep shows total sent as amount + fee, so the actual total sent amount
<s​needlewoods> I think I'd leave it like that, but make it clear with new prompt messages if fees are included or excluded. Do you agree this is reasonable or any other suggestions?
<s​needlewoods> Old transfer: `Sending 0.004000000000.  The transaction fee is 0.000044110000`
<s​needlewoods> New transfer: `Sending 0.004000000000.  Excluding the transaction fee of 0.000044110000`
<s​needlewoods> Old sweep: `Sweeping 0.004011810000 for a total fee of 0.000102900000.`
<s​needlewoods> New sweep: `Sweeping 0.004011810000 including total fee of 0.000102900000.`
<s​needlewoods> that's it for now
<r​brunner7> I think question 2 is easy to answer: Make things clearer / harder to mis-interpret is almost always a win, so I would go with the improved messages.
<r​brunner7> That, and leaving the logic as-is, there may be reasons it's like that, and anyway people are used to it to function that way probably
<r​brunner7> Will that `sweep_unmixable` command itself survive the hardfork to FCMP++?
<s​needlewoods> thank you for the quick feedback
<r​brunner7> Maybe Rucknium would have input for your question 1.
<o​frnxmr> btw Sweep_below is just an extra arg to sweep_all when using rpc
<r​brunner7> Don't have an opinion myself right now, don't know enough.
<o​frnxmr> So i assume sweep_below accepts the same args as sweep all, since sweep_below is itself just an arg
<o​frnxmr> Sweep_unmixable or sweep_dust is its own endpoint, so no comment there. Never used it
<r​brunner7> Being conservative and not, or at least not yet, adding new things beyond the immediate migration to the Wallet API could be a thing, the job being already quite big without any improvements ...
<r​brunner7> I know the temptation well however, as you are already there, and seeing things clearly, why not ... :)
<j​effro256> If you're talking about adding a new API endpoint for sweep unmixable to the wallet API, I'd personally just keep the current API in wallet2: no arguments, you get what you get
<r​brunner7> Alright, anything else left for today's meeting?
<b​oog900> should this ever be exposed publicly ?
<b​oog900> or is it like the restricted RPC interface
<b​oog900> some of the methods look to expose sensitive data like `get_peer_list`
<j​effro256> This is existing right? Not with the FCMP++ code ?
<s​needlewoods> this part https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/wallet/api/wallet.cpp#L1697-L1705 already handles sweeps, so if we add optional argument `std::string key_image = ""` we could also call `m_wallet.create_transaction_single()`, no new function needed
<h​into> I'd guess on interfaces that are (or are supposed to be) for trusted internal use, PoW checks get skipped?
<s​needlewoods> yes questions are related to my current work on CLI, only first comment is related to FCMP++
<b​oog900> yeah
<jberman> +1
<j​effro256> Oh I see. I think that I would simply keep it as-is
<s​needlewoods> jeffro you saw this ^? if sweep_unmixable wont make it to FCMP then I agree there is no need to add it to Wallet API now
<j​effro256> Oh yeah, unmixable sweep will be useless after FCMP++ since A) FCMP++ transactions can spend "unmixable" pre-RingCT outputs, and B) v1 transactions are banned after hard fork v17
<s​needlewoods> awesome
<b​oog900> FWIW I don't _know_ if the ZMQ RPC interface is supposed to be just internal or not
<s​needlewoods> rbrunner may end the meeting now :)
<r​ucknium> SNeedlewoods: Unmixables are an extremely small share of txs today.
<r​brunner7> Alright :) Feel free to use the room for further detail discussions of course. Thanks everybody for attending, read you again next week!
<s​needlewoods> thanks everyone!
<s​yntheticbird> thanks delicious meeting
<s​needlewoods> and I'll leave `sweep_below` for now, but keep it in my notes that we could add an `outputs=<N>` argument to it later
<rucknium> +1
<jeffro256> +1
<o​frnxmr> sneedlewoods
<o​frnxmr> Does that work on the existing rpc?
<o​frnxmr> I dont know why sweep_below has its own command in cli, but it an arg on rpc. Maybe cli is just a shortcut?
<j​effro256> Yeah it makes sense to consolidate that. Although I would argue for both to have it listed like a receipt: sub-total (sum of amounts in outputs), fee, total (outputs  + fee)
<ofrnxmr> +1
<s​needlewoods> I don't know about RPC, but in the CLI they call the same underlying `sweep_main()` method, though they handle their arguments independently AFAICT
<o​frnxmr> https://docs.getmonero.org/rpc-library/wallet-rpc/#sweep_all
<o​frnxmr> "below_amount - unsigned int; (Optional) Include outputs below this amount."
<s​needlewoods> https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/simplewallet/simplewallet.cpp#L201-L204
<j​effro256> This way, you're not relying on English language to disambiguate, you can discern which number is which total through math
<sneedlewoods> +1
<o​frnxmr> I think its an oversight?
<s​needlewoods> ah wait, the underlying method does handle `output` arg for all of them https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/simplewallet/simplewallet.cpp#L7033
<s​needlewoods> so I have to test it, maybe just wrong usage messages .... that never happened before /s
<s​needlewoods> @ofrnxmr you're right, the `outputs` argument already works for `sweep_below`, it's just missing from `USAGE_SWEEP_BELOW`
<ofrnxmr> +1
<o​frnxmr> Lets revisit on 2 weeks time and decide how to move fwd with that /s :D lolol
<v​tnerd> crap, missed meeting this week. still testing carrot integration in lws. only subaddresses+balance-key needs to be tested, spends are currently being tracked
<o​frnxmr> Nice easy pr
<s​needlewoods> sorry I mixed something up here. The Wallet API already has an old method for sweep_umixable [src](https://github.com/monero-project/monero/blob/8e9ab9677f90492bca3c7555a246f2a8677bd570/src/wallet/api/wallet.cpp#L1791)
<s​needlewoods> The change I talked about here was in regards to `sweep_single`, for which we do not have a method in the Wallet API currently. That can be solved by adding the key image arg to `createTransactionMultDest()` instead of making a new function.
````


# Action History
- Created by: rbrunner7 | 2025-10-05T08:19:36+00:00
- Closed at: 2025-10-06T19:33:07+00:00
