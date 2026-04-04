---
title: Daemon stalls / becomes unresponsive upon start_mining
source_url: https://github.com/monero-project/monero/issues/309
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-06-05T02:53:54+00:00'
updated_at: '2015-06-11T03:24:47+00:00'
type: issue
status: closed
closed_at: '2015-06-11T03:24:47+00:00'
---

# Original Description
Okay, so this keeps happening. 

http://pastebin.com/rV8SpgnT

so i stared at log level 3 for a while during normal operations. Then I sent the start_mining commmand from the wallet. Then this happens. I had the log at level 3 when I sent the command. I then grep -C'd around the last start_mining command with a 500 line window.

as of writing this, in the 22 minutes that have passed since sending the command, bitmonerod is still nonresponsive. I had sent the "exit" command before the following set_log 3

2015-Jun-04 22:46:54.961432 [RPC1]Blockchain::get_current_blockchain_height
2015-Jun-04 22:46:54.961657 [RPC1]BlockchainLMDB::height
2015-Jun-04 22:46:54.961807 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.961972 [RPC1]Blockchain::get_block_id_by_height
2015-Jun-04 22:46:54.962196 [RPC1]BlockchainLMDB::get_block_hash_from_height
2015-Jun-04 22:46:54.962346 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.962539 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.962706 [RPC1]Blockchain::have_tx_keyimges_as_spent
2015-Jun-04 22:46:54.962872 [RPC1]Blockchain::have_tx_keyimg_as_spent
2015-Jun-04 22:46:54.963104 [RPC1]BlockchainLMDB::has_key_image
2015-Jun-04 22:46:54.963254 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.963424 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.963591 [RPC1]Blockchain::get_current_blockchain_height
2015-Jun-04 22:46:54.963840 [RPC1]BlockchainLMDB::height
2015-Jun-04 22:46:54.963989 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.964156 [RPC1]Blockchain::get_block_id_by_height
2015-Jun-04 22:46:54.964381 [RPC1]BlockchainLMDB::get_block_hash_from_height
2015-Jun-04 22:46:54.964531 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.964726 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.964893 [RPC1]Blockchain::have_tx_keyimges_as_spent
2015-Jun-04 22:46:54.965059 [RPC1]Blockchain::have_tx_keyimg_as_spent
2015-Jun-04 22:46:54.965282 [RPC1]BlockchainLMDB::has_key_image
2015-Jun-04 22:46:54.965432 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.965603 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.965769 [RPC1]Blockchain::get_current_blockchain_height
2015-Jun-04 22:46:54.966018 [RPC1]BlockchainLMDB::height
2015-Jun-04 22:46:54.966168 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.966333 [RPC1]Blockchain::get_block_id_by_height
2015-Jun-04 22:46:54.966558 [RPC1]BlockchainLMDB::get_block_hash_from_height
2015-Jun-04 22:46:54.966708 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.966913 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.967105 [RPC1]Blockchain::have_tx_keyimges_as_spent
2015-Jun-04 22:46:54.967272 [RPC1]Blockchain::have_tx_keyimg_as_spent
2015-Jun-04 22:46:54.967482 [RPC1]BlockchainLMDB::has_key_image
2015-Jun-04 22:46:54.967628 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.967803 [RPC1]mdb_txn_safe: destructor
2015-Jun-04 22:46:54.967970 [RPC1]Blockchain::get_current_blockchain_height
2015-Jun-04 22:46:54.968194 [RPC1]BlockchainLMDB::height
2015-Jun-04 22:46:54.968344 [RPC1]BlockchainLMDB::check_open
2015-Jun-04 22:46:54.968498 Read command: set_log 2
2015-Jun-04 22:46:54.968529 [RPC1]Blockchain::get_block_id_by_height
2015-Jun-04 22:46:54.968747 Log level is now 2

If I kill the program (because it obviously won't shut down) and restart it, it works fine, until I start mining again. 


# Discussion History
## Gingeropolous | 2015-06-05T02:56:59+00:00
bitmonero v0.8.8.7-431397a, according to the daemon "help" response


## Gingeropolous | 2015-06-05T02:59:14+00:00
all I can tell is that the next command is

"2015-Jun-04 22:24:04.186277 [RPC1]Blockchain::create_block_template"

and then things get loopy. 


## tewinget | 2015-06-05T06:03:33+00:00
Interesting.  I see a bunch of db reads, which is normal, but past that idk what's going on.


## Gingeropolous | 2015-06-08T11:31:03+00:00
This seems to be specific to my box at home. When I compiled on a cloud instance, it worked fine (daemon mined and sent transaction on testnet). I don't know whats going on with my environment at home or if its worth investigating. 


## Gingeropolous | 2015-06-11T03:24:47+00:00
so, when compiled properly (with make release-static-64), the daemon can mine again.

at least I can close issues. 


# Action History
- Created by: Gingeropolous | 2015-06-05T02:53:54+00:00
- Closed at: 2015-06-11T03:24:47+00:00
