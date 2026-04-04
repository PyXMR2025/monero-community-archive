---
title: '[Features Requests/Proposals] Wallet2 improvements'
source_url: https://github.com/monero-project/monero/issues/62
author: Neozaru
assignees: []
labels: []
created_at: '2014-07-15T21:17:06+00:00'
updated_at: '2016-10-29T09:56:35+00:00'
type: issue
status: closed
closed_at: '2016-10-29T09:56:35+00:00'
---

# Original Description
I propose a discussion about what should be added/improved in Wallet2, in order to provide more information in rpcwallet, simplewallet or programs which on their top.
- Adding blocks timestamp cache : The objective is to know the "human" date (epoch) of transactions (or other events) from their block height. As they only contains block height when saved to wallet2. 
  Two solutions : 
  -- Adding a map in Wallet2 containing the mapping "block_height -> timestamp". The map can easily be filled during refreshes processes as all required blocks are scanned. This involves an average of +30% size of Wallet2 data file. 
  -- Another solution could come with database implementation, because blocks information should be easily accessible from Wallet2 and/or other classes.
- Memorizing transaction spending time. As far I know, when we ask for incoming transfers, we can access the block time of the transaction (received), but for "sent/spendable" status, we only have a boolean (is the output spent or not). It could be interesting to have an additional parameter "spent_block_time". This can be achieved by adding a line in 'process_new_transaction'.
- Memorizing transaction amounts/destinations : I'm doubtful about this, but it could be useful to save destinations somewhere when sending transactions. Like a "software" history (not contained in the blockchain). The main problem I consider is privacy and how to protect/backup this history. This feature could be a pain to implement properly (give the choice to users, backup it, etc) and may not be in the Privacy coin philosophy. Nevertheless this can be discussed.

Note : As I don't know boost::serialize behaviour (wallet2 data is stored this way), adding new data or modifying structures in Wallet2 could be harmful. Adding a "data structure version" flag (wallet2-specific version) could resolve this problem (if the version flag of local data file is lower than xxx, a full refresh is done and required structure are reinit correctly).

I haven't reviewed all internal data structures and information, so if I missed something, some of these proposals could be useless or almost existing.

(stopped here after remembering I was not in a Forum)


# Discussion History
## Neozaru | 2014-08-06T20:08:13+00:00
Completed point 2 : https://github.com/Neozaru/bitmonero/tree/wallet2_improvements

For each _transfer_ structure, spent_block_height was added. Rescanning is required for old wallets (added a "reset" command)


## fluffypony | 2014-08-06T20:10:32+00:00
@Neozaru awesome - do you want to rebase and PR it so we can test that specific PR? Easier than waiting till the end when more sand has shifted underneath it, I predict:)


## Neozaru | 2014-08-06T20:19:57+00:00
Since I merged it with another branch, I will firstly integrate it in a custom branch with current master and let you know if/when the merge is OK.
I also need to set up a build environment on Windows and test on it (will be useful for all other branches)


## fluffypony | 2016-10-29T09:55:07+00:00
This is mostly implemented, so closing this old issue. Thank you for all your work in the earliest days of Monero's existence, @Neozaru :)


# Action History
- Created by: Neozaru | 2014-07-15T21:17:06+00:00
- Closed at: 2016-10-29T09:56:35+00:00
