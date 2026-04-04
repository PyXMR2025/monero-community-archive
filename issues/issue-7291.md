---
title: '[PROPOSAL] Add advanced command to monero-wallet-cli: scan_block'
source_url: https://github.com/monero-project/monero/issues/7291
author: hMihaiDavid
assignees: []
labels: []
created_at: '2021-01-07T19:39:59+00:00'
updated_at: '2021-01-12T13:14:54+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I propose to add a command to monero-wallet-cli that allows an advanced user to specify a list of block heights that the client will scan for outputs.

## Motivation

If an advanced user doesn't want to wait for scanning the whole blockchain for outputs they own (when, for example, restoring the wallet from a mnemonic seed), currently they can specify the block height to start the scanning from (by using the '--restore-height' or the interactive prompt during initialization). However, this can still be a lengthy process since the user would have to specify, ideally, the block height of the first transaction directed to them. This can still take a long time if restoring a paper wallet first used several years ago (all blocks from that height to the latest one will be scanned).

If an advanced user can omit the initial scanning, they can specify the list of blocks with all the known outputs by hand using the proposed command. These could be stored along the seed in a paper wallet. I am not aware for a current mechanism that implements this feature (either for block heights or tx hashes).

The user could omit the initial scanning by just specifying as restore height the current block or current date, which would take very little time to initialize.

## Discussion

I am aware that starting a full node for the first time will still need to linearly traverse the whole blockchain. However, this command would help the restore time for paper wallets using a remote node already synced, either a trusted or untrusted node. There may be privacy concerns by leaking block ids of user's outputs to untrusted nodes which may be interesting to discuss.

Please let me know if this is already implemented or if the devs consider this as a very unnecessary feature that would not be merged.

If it is deemed to be somewhat worthwhile I would like to start developing this feature to alleviate dev time.



Have a nice day.

# Discussion History
## moneromooo-monero | 2021-01-07T21:53:55+00:00
I think it might be useful, and should be a fairly simple shell over the mid-level wallet2 functions.

## moneromooo-monero | 2021-01-07T21:55:36+00:00
In fact, an ordered list of txids is probably best. A user will know these, but not necessarily the block heights they got mined, and this'll be even faster.

## hMihaiDavid | 2021-01-08T19:01:50+00:00
Hi @moneromooo-monero ,
Please correct me if I'm wrong, I'm completely new to the monero codebase.

I couldn't find any wallet2.h exported API to use from simplewallet.c that would allow to retrieve any tx in the blockchain by hash, or any block by hash or height. wallet2 exposes the high-level functionality of a wallet, so implementing this would require to get into wallet2.

Apparently wallet2::refresh(), called on init, would do a fast scan of the blockchain and starting with the restore height it would iterate over the outputs of transactions in the blocks to detect and update the balance of the wallet (process_parsed_blocks -> process_new_blockchain_entry -> process_new_transaction -> scan_output) I think this information is cached so subsequent refresh() will be very fast. These operations are not accesible by simplewallet, all simplewallet can do is call refresh().


My idea for implementing the feature is to export a new wallet2 API to simplewallet that internally implements the operation of
scanning a tx by hash in a way similar to or invoking process_new_transaction (after retrieving it from the daemon). I'm writting this to ask if my information and my approach are correct or if there is a much simpler take on this.

## moneromooo-monero | 2021-01-08T20:52:37+00:00
The wallet does not deal with the blockchain. The daemon does. You ask the daemon for the data you need.

## moneromooo-monero | 2021-01-08T21:01:47+00:00
And yes, your last paragraph is what you should do.

## hMihaiDavid | 2021-01-11T21:42:06+00:00
In commit f23dbe24af0c504297939f35e478f4cf63412859 of my fork I implemented the command scan_tx. Please review my code when you can.

I have a couple of issue I'd like to raise:
- Calling process_new_transaction outside of refresh seems to ask for the wallet password although it cannot prompt for it because apparently the command code is running in a background thread (?) and this seems forbidden (see simple_wallet::on_get_password). I did a little workaround in simplewallet::scan_tx but I'm not sure if it's correct.

- When calling process_new_transaction in wallet2::scan_tx I have no way of getting the block_version so I set it to 0. The response from the node doesn't have this information. Same for the boolean indicating whether this is a miner tx or not.

After resolving this command, I'd like to add a similar command for block heights instead of txids. My initial idea was to write on paper some information for fast recovery of a paper wallet, and tx hashes seem very long.

Have a nice day.

## selsta | 2021-01-12T11:51:27+00:00
@hMihaiDavid please open a PR, it will result in more people seeing it

## Gingeropolous | 2021-01-12T13:14:54+00:00
this would be great. seems similar to my idea of a "fast forward". The user mostly knows when they receive transactions. This would be awesome. 

# Action History
- Created by: hMihaiDavid | 2021-01-07T19:39:59+00:00
