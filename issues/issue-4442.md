---
title: ' Help with  Parameters that is needed!'
source_url: https://github.com/monero-project/monero/issues/4442
author: jdscott0
assignees: []
labels: []
created_at: '2018-09-25T17:26:39+00:00'
updated_at: '2018-09-26T13:29:00+00:00'
type: issue
status: closed
closed_at: '2018-09-26T13:26:57+00:00'
---

# Original Description
Having trouble with my monero wallet gui 0.12.3.0 , the issue is Exactly one parameter is needed: check, download, or update. How to fix this 

# Discussion History
## moneromooo-monero | 2018-09-25T20:06:21+00:00
Not much info. Describe what you did, and where is this message showing.

## jdscott0 | 2018-09-25T20:31:52+00:00
Okay, I went to setting because  my balance is 0.00, and then  to show status [9/25/2018 3:22 PM] Height: 502372/502372 (100.0%) on mainnet, not mining, net hash 17.51 MH/s, v1, update needed, 0(out)+0(in) connections, uptime 0d 0h 4m 27s. Then I went to th powershell window and I retrieve this Exactly one parameter is needed: check, download, or update.So now I stuck also receive this  [0m
2018-09-25 20:18:06.115 [P2P0]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1380    [1;31m**********************************************************************[0m
2018-09-25 20:18:06.171 [P2P0]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1381    [1;31mLast scheduled hard fork time shows a daemon update is needed soon.[0m
2018-09-25 20:18:06.228 [P2P0]  WARN    global  src/cryptonote_core/cryptonote_core.cpp:1382    [1;31m**********************************************************************[0m
help
Monero 'Lithium Luna' (v0.12.3.0-release)

## moneromooo-monero | 2018-09-25T23:11:51+00:00
Your daemon is synced to about a third of the blockchain, and doesn't have any network connection. You seem to have an OK version so not sure why it could not find any in 4 minutes.

About the "one parameter is needed: check, download, or update." message, what is outputting it ? It's not clear in your post.

## iDunk5400 | 2018-09-25T23:54:11+00:00
The easiest way to fix that issue is not to type `update` in the daemon window of your GUI.

## jdscott0 | 2018-09-26T13:26:15+00:00
> The easiest way to fix that issue is not to type `update` in the daemon window of your GUI.

Every time I do that it gives me this below.
update
Exactly one parameter is needed: check, download, or update
unknown command: update
Monero 'Lithium Luna' (v0.12.3.0-release)
Commands:
  alt_chain_info
  ban <IP> [<seconds>]
  bans
  bc_dyn_stats <last_block_count>
  diff
  exit
  flush_txpool [<txid>]
  hard_fork_info
  help [<command>]
  hide_hr
  in_peers <max_number>
  is_key_image_spent <key_image>
  limit [<kB/s>]
  limit_down [<kB/s>]
  limit_up [<kB/s>]
  out_peers <max_number>
  output_histogram [@<amount>] <min_count> [<max_count>]
  print_bc <begin_height> [<end_height>]
  print_block <block_hash> | <block_height>
  print_cn
  print_coinbase_tx_sum <start_height> [<block_count>]
  print_height
  print_pl
  print_pl_stats
  print_pool
  print_pool_sh
  print_pool_stats
  print_status
  print_tx <transaction_hash> [+hex] [+json]
  relay_tx <txid>
  save
  set_log <level>|<{+,-,}categories>
  show_hr
  start_mining <addr> [<threads>] [do_background_mining] [ignore_battery]
  start_save_graph
  status
  stop_daemon
  stop_mining
  stop_save_graph
  sync_info
  unban <IP>
  update (check|download)
  version

## jdscott0 | 2018-09-26T13:26:57+00:00
> The easiest way to fix that issue is not to type `update` in the daemon window of your GUI.


## jdscott0 | 2018-09-26T13:29:00+00:00
> Your daemon is synced to about a third of the blockchain, and doesn't have any network connection. You seem to have an OK version so not sure why it could not find any in 4 minutes.
> 
> About the "one parameter is needed: check, download, or update." message, what is outputting it ? It's not clear in your post.

The GUI and I taught when you have 100% you was connect to the network, so what I have to do next?

# Action History
- Created by: jdscott0 | 2018-09-25T17:26:39+00:00
- Closed at: 2018-09-26T13:26:57+00:00
