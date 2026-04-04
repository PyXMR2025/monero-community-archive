---
title: '[Bug] --daemon is not an invalid argument'
source_url: https://github.com/monero-project/monero/issues/8182
author: elibroftw
assignees: []
labels: []
created_at: '2022-02-16T20:35:39+00:00'
updated_at: '2022-02-19T18:14:04+00:00'
type: issue
status: closed
closed_at: '2022-02-19T18:14:04+00:00'
---

# Original Description
I used `--daemon` instead of `--detach` accidentally and got some weird command line argument parsing errors. The error message changes if I use `--daemon` as the first argument or the last argument.

# Discussion History
## selsta | 2022-02-16T22:55:47+00:00
`--daemon` is not a valid option / setting for monerod. See `./monerod --help`.

## elibroftw | 2022-02-16T23:05:20+00:00
Well then I should be given that error message. The error message I get is that --config-file is not an option


## elibroftw | 2022-02-16T23:05:40+00:00
Try it yourself `monerod --daemon --config-file=monerod.conf`

I get on both UBuntu 20.04 and Windows
```
C:\Users\maste>monerod --daemon --config-file=monerod.conf
2022-02-16 23:05:49.718 I Monero 'Oxygen Orion' (v0.17.3.0-release)
Monero 'Oxygen Orion' (v0.17.3.0-release)
Commands:
  alt_chain_info [blockhash]
  apropos <keyword> [<keyword> ...]
  ban [<IP>|@<filename>] [<seconds>]
  banned <address>
  bans
  bc_dyn_stats <last_block_count>
  check_blockchain_pruning
  diff
  exit
  flush_cache [bad-txs] [bad-blocks]
  flush_txpool [<txid>]
  hard_fork_info
  help [<command>]
  hide_hr
  in_peers <max_number>
  is_key_image_spent <key_image>
  limit [<kB/s>]
  limit_down [<kB/s>]
  limit_up [<kB/s>]
  mining_status
  out_peers <max_number>
  output_histogram [@<amount>] <min_count> [<max_count>]
  pop_blocks <nblocks>
  print_bc <begin_height> [<end_height>]
  print_block <block_hash> | <block_height>
  print_cn
  print_coinbase_tx_sum <start_height> [<block_count>]
  print_height
  print_net_stats
  print_pl [white] [gray] [pruned] [publicrpc] [<limit>]
  print_pl_stats
  print_pool
  print_pool_sh
  print_pool_stats
  print_status
  print_tx <transaction_hash> [+hex] [+json]
  prune_blockchain
  relay_tx <txid>
  rpc_payments
  save
  set_bootstrap_daemon (auto | none | host[:port] [username] [password]) [proxy_ip:proxy_port]
  set_log <level>|<{+,-,}categories>
  show_hr
  start_mining <addr> [<threads>|auto] [do_background_mining] [ignore_battery]
  status
  stop_daemon
  stop_mining
  sync_info
  unban <address>
  update (check|download)
  version

Unknown command: --config-file=monerod.conf

```

## selsta | 2022-02-16T23:22:04+00:00
`daemon` is a special keyword for the command line argument parser so it doesn't print the usual help screen but instead It tries to send `--config-file=monerod.conf` as a command which obviously doesn't exist.

Now why daemon is a special keyword, I don't know. There is probably a reason for it but I'm not going to debug it.

## elibroftw | 2022-02-16T23:35:25+00:00
Can you document somewhere then at least? 

## selsta | 2022-02-16T23:38:01+00:00
I don't know why you entered --daemon in the first place. It's not a documented keyword.

## elibroftw | 2022-02-16T23:38:59+00:00
Well like I said, I got caught up in the moment and read --detach as --daemon because I was trying to create a systemd service. So much daemon my brain thought detact was daemon. 

## selsta | 2022-02-16T23:43:09+00:00
I don't see the point in documenting things to **not** enter. Documentation works the other way around, only valid keywords get documented in the `--help` screen. Everything else will be broken in some way, ideally with the correct error message.

If someone wants to fix this that the correct error message shows up then this can get merged, but this has such a low priority that I won't bother with it.

## selsta | 2022-02-16T23:51:33+00:00
I can reopen this want but I doubt anyone will fix this as it's a harmless edge case in the command line parser.

Please also update the issue title and first post to make it more clear what you are reporting.

## jeffro256 | 2022-02-19T18:11:01+00:00
To add, running only `monerod --daemon` gives the following error message:

    Failed to parse arguments: the required argument for option '--daemon_command' is missing

I assume then that maybe `--daemon` is aliased or something to `--daemon_command`. 

## selsta | 2022-02-19T18:14:04+00:00
@jeffro256 thanks, that solves the question

seems to be an alias that was maybe kept for backwards compatibility

# Action History
- Created by: elibroftw | 2022-02-16T20:35:39+00:00
- Closed at: 2022-02-19T18:14:04+00:00
