---
title: Testing RPC pay, connected wallet-cli client ID mis-identified as inactive
  for negative days value, Monerod crashes with "Aborted"
source_url: https://github.com/monero-project/monero/issues/6555
author: shermand100
assignees: []
labels: []
created_at: '2020-05-17T22:56:15+00:00'
updated_at: '2020-05-31T22:48:22+00:00'
type: issue
status: closed
closed_at: '2020-05-31T22:48:21+00:00'
---

# Original Description
A bit of a lengthy title I know put I think it's still to the point.

I've been trying this out with regards to the  rpc payment features. and the --rpc-payment-allow-free-loopback  which was added to solve issue #3038 

I'm having some stability issues I can't work out. I start the node with:

`./monerod --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --rpc-restricted-bind-port=18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=43HoAhqx9q3MR1crAjpQtYVhvzQhZgqPwSWVQMmPvYmr18qVUEjCHcsEasuCxS486rWSSg1gbGqanet67NWRsh1bQL9KkB9 --rpc-payment-credits=5 --rpc-payment-difficulty=100 --log-level=3`

Where the un-restricted port 18083 is kept behind my firewall and used by other scripts to produce stats for a user interface (print_pl, status, version, etc,)

Port 18089 restricted and port forwarded through router for external wallet access requiring payment.

The `--rpc-payment-allow-free-loopback` flag is great in that it now permits the node to start with both an unrestricted and restricted port. So it solved that initial issue.

The stability issue I have is that when a wallet-cli client submits hashes, I get what appear to be "timing" issues. Sometimes monerod will run for 5 minutes, sometimes up to 45mins before this happens. I've increased the log-level to try and get a better idea of whats causing it but I'm out of my depth, only the last couple of lines seem relevant.

Monerod (Monero 'Carbon Chamaeleon' (v0.16.0.0-4987161fa)):

```
2020-05-17 19:09:48.838 I Erasing <99cf5311b1180de437ecda16491e662d92b9f23f111d22df8f797b88fe59bce2> with 39 credits, inactive for -20633 days
2020-05-17 19:09:50.404 I client <99cf5311b1180de437ecda16491e662d92b9f23f111d22df8f797b88fe59bce2> credited for 5, now 44
Aborted
pinodexmr@PiNodeXMR:~/monero/build/release/bin $
```


It's weird my currently connected wallet-cli client (in this case id <99...) is reported as not being seen for 56.5 years? Doesn't erase it's credits, adds another 5 credits to it's balance, then terminates the node with single "Aborted" phrase.

On another occasion (so different client ID <a8a...):

```
2020-05-17 22:23:52.597 I [144.91.122.162:18080 OUT] 172 bytes sent for category command-1002 initiated by us
2020-05-17 22:24:00.320 I Erasing <a8a8e0f2dc4ae4214c0215c58c4dc38988f71f7e4b8a10ab750dada34b73762b> with 11 credits, inactive for -6463 days
2020-05-17 22:24:04.080 I HTTP [192.168.1.116] POST /get_transaction_pool_stats
2020-05-17 22:24:04.081 I HTTP [192.168.1.116] POST /get_peer_list
2020-05-17 22:24:04.081 I [192.168.1.116:36754 INC] calling /get_transaction_pool_stats
2020-05-17 22:24:04.087 I [192.168.1.116:36756 INC] calling /get_peer_list
2020-05-17 22:24:04.208 I HTTP [192.168.1.116] POST /getinfo
2020-05-17 22:24:04.223 I [192.168.1.116:36760 INC] calling /getinfo
2020-05-17 22:24:06.250 I [116.203.189.230:18080 OUT] 1799 bytes received for category command-2002 initiated by peer
2020-05-17 22:24:06.250 I [116.203.189.230:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-17 22:24:06.267 I Including transaction <2aefb06160a4e75c687d21db9072c3b311cba42cbe6dd4b87a8de7515a3cecce>
Aborted
pinodexmr@PiNodeXMR:~/monero/build/release/bin $
```

Wallet (CLI) (Monero 'Carbon Chamaeleon' (v0.16.0.0-4987161fa)) started with:

`./monero-wallet-cli --daemon-address=192.168.1.116:18089 --trusted-daemon start_mining_for_rpc
`
Errors with:

```
Error: Error mining to daemon: Found nonce, but daemon did not credit us with the expected amount
Error: Failed to start mining for RPC payment
```
Other Notes:

Using `rpc_payment_info` in the wallet cli I see my client ID, and it matched the inactive one from the daemon log each time. I've seen the above crash repeated about 6 times, each requires a manual restart of both daemon and wallet.

The daemon is 100% sync'd

I compiled Monero 0.16 from source, this is running on a Raspberry Pi, the build produced no errors. The logs above are from the wallet cli 0.16 also.

This was initially noticed when connecting to the Raspberry Pi node (v0.16) from my Windows wallet-cli (v0.15.0.5) over LAN and then also an external connection. To remove the possible version conflict I then produced the above logs/test running the node and wallet on the same device (v0.16) to mitigate the different clocks on different devices.

I've included my start commands in this because I never rule out user error?



# Discussion History
## moneromooo-monero | 2020-05-18T12:06:43+00:00
Please run with gdb, ie:

gdb ./monerod
run --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --rpc-restricted-bind-port=18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=43HoAhqx9q3MR1crAjpQtYVhvzQhZgqPwSWVQMmPvYmr18qVUEjCHcsEasuCxS486rWSSg1gbGqanet67NWRsh1bQL9KkB9 --rpc-payment-credits=5 --rpc-payment-difficulty=100 --log-level=3

Then after it does: bt full

And post the (probably multi page) output here.

## moneromooo-monero | 2020-05-18T12:08:09+00:00
Also, what's the time on your machine running monerod, and the one running the wallet ?

## shermand100 | 2020-05-18T19:44:15+00:00
> Please run with gdb, ie:
> 
> gdb ./monerod
> run --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --rpc-restricted-bind-port=18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=43HoAhqx9q3MR1crAjpQtYVhvzQhZgqPwSWVQMmPvYmr18qVUEjCHcsEasuCxS486rWSSg1gbGqanet67NWRsh1bQL9KkB9 --rpc-payment-credits=5 --rpc-payment-difficulty=100 --log-level=3
> 
> Then after it does: bt full
> 
> And post the (probably multi page) output here.

I got 2005 lines in my Putty window before the error with gdb ./monerod... Below is the last, what seems like relevant bit. [Here is a paste bin of the full 2005 lines](https://pastebin.com/Vz3VKgms) for neatness of this post, but I can dig out the entire log file if needed.

> 
> Thread 6 "monerod" received signal SIGABRT, Aborted.
> [Switching to Thread 0x5a6feff0 (LWP 32072)]
> __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
> 50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
> 

**Then bt full produces**

> (gdb) bt full
> #0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
>         set = {__val = {0, 0, 0, 33, 1517277968, 0, 33, 13677564, 1517278072,
>             1517277720, 1517277832, 3435973837, 13677760, 2147516424,
>             2147483648, 13677760, 13677472, 1517277864, 1517277872, 13677376,
>             1996482920, 1515191037, 941428179, 2192556127, 2433853511,
>             2046094773, 2154391251, 3911720874, 312995008, 4171879919,
>             187071671, 1517277800}}
>         pid = <optimized out>
>         tid = <optimized out>
>         ret = <optimized out>
> #1  0x76380230 in __GI_abort () at abort.c:79
>         save_stage = 1
>         act = {__sigaction_handler = {sa_handler = 0x329c783a,
>             sa_sigaction = 0x329c783a}, sa_mask = {__val = {2638505732,
>               3022368618, 4288634165, 2977451000, 344, 0 <repeats 23 times>,
>               1056552792, 2147483648, 1986876312, 0}}, sa_flags = 1190078464,
>           sa_restorer = 0x5a6fd334}
>         sigs = {__val = {32, 0 <repeats 31 times>}}
> #2  0x007f2038 in std::vector<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key>, std::allocator<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key> > >::operator=(std::vector<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_t--Type <RET> for more, q to quit, c to continue without paging--
> 

## shermand100 | 2020-05-18T19:46:38+00:00
> Also, what's the time on your machine running monerod, and the one running the wallet ?

Because I only have wallet-cli v0.16 on the same device as the node, this was produced locally. GMT so 1 hour ahead of what the Monerod quotes in it's logs.

I can do this (connect) from a different device (windows) but it would be with wallet-cli (v0.15.0.5)

## moneromooo-monero | 2020-05-18T21:55:42+00:00
You're missing the interesting part from gdb, it's not here nor in the paste. Note the message telling you to type for more, it's a multi page output. 



## shermand100 | 2020-05-19T17:56:46+00:00
> You're missing the interesting part from gdb, it's not here nor in the paste. Note the message telling you to type for more, it's a multi page output.

My bad, a habbit of using ctrl+c to copy, so ending it.

This time:

3 outputs for you:

1. Log level 3 Putty output of Monerod until point of crash ~2000 lines
2. bt full 65 lines
3. "type <RET> for more" Return key pressed, "Backtrace stopped: previous frame identical to this frame (corrupt stack?)" and a couple more lines after.

Because of the bt full "Backtrace stopped: previous frame identical to this frame (corrupt stack?)" when trying to view next page I repeated this to try and get a better output. This error was produced both times.

Big headers for easier scrolling...

## Log 3 Putty output of Monerod until point of crash ~2000 lines:

2020-05-19 17:43:36.877 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.877 T Blockchain::get_difficulty_for_next_block
2020-05-19 17:43:36.877 T Blockchain::get_tail_id
2020-05-19 17:43:36.877 T mdb_txn_safe: destructor
2020-05-19 17:43:36.878 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:36.878 T BlockchainLMDB::height
2020-05-19 17:43:36.878 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.878 T mdb_txn_safe: destructor
2020-05-19 17:43:36.878 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:36.878 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.878 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:36.879 T Blockchain::get_transactions
2020-05-19 17:43:36.879 T mdb_txn_safe: destructor
2020-05-19 17:43:36.879 T Blockchain::get_tail_id
2020-05-19 17:43:36.879 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.879 T mdb_txn_safe: destructor
2020-05-19 17:43:36.880 T Blockchain::get_transactions
2020-05-19 17:43:36.880 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.880 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.881 T mdb_txn_safe: destructor
2020-05-19 17:43:36.884 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:36.884 T BlockchainLMDB::height
2020-05-19 17:43:36.884 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.884 T mdb_txn_safe: destructor
2020-05-19 17:43:36.884 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:36.884 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.884 T mdb_txn_safe: destructor
2020-05-19 17:43:36.885 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.885 D /json_rpc[rpc_access_submit_nonce] processed with 0/2749/0ms
2020-05-19 17:43:36.885 T HTTP_RESPONSE_HEAD: <<
2020-05-19 17:43:36.885 T HTTP/1.1 200 Ok
2020-05-19 17:43:36.885 T Server: Epee-based
2020-05-19 17:43:36.885 T Content-Length: 208
2020-05-19 17:43:36.885 T Content-Type: application/json
2020-05-19 17:43:36.885 T Last-Modified: Tue, 19 May 2020 17:43:36 GMT
2020-05-19 17:43:36.886 T Accept-Ranges: bytes
2020-05-19 17:43:36.886 T
2020-05-19 17:43:36.886 T Moving counter buffer by 1 second 23541 < 23544 (last time 23541.8)
2020-05-19 17:43:36.886 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.886 T Moving counter buffer by 1 second 23542 < 23544 (last time 23542.8)
2020-05-19 17:43:36.886 T Moving counter buffer by 1 second 23543 < 23544 (last time 23543.8)
2020-05-19 17:43:36.886 T Throttle throttle_speed_out: packet of ~368b  (from 368 b) Speed AVG=   0[w=9.94099]    0[w=9.94099] /  Limit=16 KiB/sec  [368 0 0 781 270 0 0 0 0 0 ]
2020-05-19 17:43:36.887 T mdb_txn_safe: destructor
2020-05-19 17:43:36.887 D do_send_chunk() NOW SENSD: packet=368 B
2020-05-19 17:43:36.887 T Setting 00:30:00 expiry
2020-05-19 17:43:36.887 T Setting 00:30:00 expiry
2020-05-19 17:43:36.888 T [192.168.1.131:54281 INC] [sock 39] Async send calledback 368
2020-05-19 17:43:36.890 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:36.890 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.890 T mdb_txn_safe: destructor
2020-05-19 17:43:36.891 T Blockchain::get_transactions
2020-05-19 17:43:36.891 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:36.891 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.892 T mdb_txn_safe: destructor
2020-05-19 17:43:36.892 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.892 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.893 T Blockchain::get_transactions
2020-05-19 17:43:36.893 T mdb_txn_safe: destructor
2020-05-19 17:43:36.895 T Moving counter buffer by 1 second 23542 < 23544 (last time 23542.2)
2020-05-19 17:43:36.895 T Moving counter buffer by 1 second 23543 < 23544 (last time 23543.2)
2020-05-19 17:43:36.896 T Throttle throttle_speed_in: packet of ~115b  (from 115 b) Speed AVG=   0[w=9.951]    0[w=9.951] /  Limit=16 KiB/sec  [115 0 476 432 425 0 0 0 0 0 ]
2020-05-19 17:43:36.896 T Throttle <<< global-IN: packet of ~115b  (from 115 b) Speed AVG=   1[w=9.952]    1[w=9.952] /  Limit=8192 KiB/sec  [8052 0 476 8624 425 0 0 0 0 0 ]
2020-05-19 17:43:36.897 T HTTP HEAD:
2020-05-19 17:43:36.897 T Host: 192.168.1.116
2020-05-19 17:43:36.897 T Content-Length: 317
2020-05-19 17:43:36.897 T Content-Type: application/json; charset=utf-8
2020-05-19 17:43:36.898 T
2020-05-19 17:43:36.898 T Setting 00:30:00 expiry
2020-05-19 17:43:36.899 T Throttle throttle_speed_in: packet of ~317b  (from 317 b) Speed AVG=   0[w=9.954]    0[w=9.954] /  Limit=16 KiB/sec  [432 0 476 432 425 0 0 0 0 0 ]
2020-05-19 17:43:36.899 T Throttle <<< global-IN: packet of ~317b  (from 317 b) Speed AVG=   1[w=9.954]    1[w=9.954] /  Limit=8192 KiB/sec  [8369 0 476 8624 425 0 0 0 0 0 ]
2020-05-19 17:43:36.899 I HTTP [192.168.1.131] GET /json_rpc
2020-05-19 17:43:36.900 I [192.168.1.131:54281 INC] Calling RPC method rpc_access_info
2020-05-19 17:43:36.900 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.900 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.901 T mdb_txn_safe: destructor
2020-05-19 17:43:36.902 T Blockchain::get_tail_id
2020-05-19 17:43:36.904 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:36.904 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.904 T mdb_txn_safe: destructor
2020-05-19 17:43:36.904 T Blockchain::have_tx
2020-05-19 17:43:36.905 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:36.905 T BlockchainLMDB::height
2020-05-19 17:43:36.905 T BlockchainLMDB::tx_exists
2020-05-19 17:43:36.905 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.905 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.906 I transaction with hash eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19 not found in db
2020-05-19 17:43:36.906 T mdb_txn_safe: destructor
2020-05-19 17:43:36.906 T mdb_txn_safe: destructor
2020-05-19 17:43:36.906 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:36.906 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.907 T mdb_txn_safe: destructor
2020-05-19 17:43:36.907 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:36.907 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.907 T mdb_txn_safe: destructor
2020-05-19 17:43:36.907 T Blockchain::get_transactions
2020-05-19 17:43:36.908 D /json_rpc[rpc_access_info] processed with 0/8/0ms
2020-05-19 17:43:36.908 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.908 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.908 T HTTP_RESPONSE_HEAD: <<
2020-05-19 17:43:36.908 T HTTP/1.1 200 Ok
2020-05-19 17:43:36.908 T Server: Epee-based
2020-05-19 17:43:36.909 T Content-Length: 685
2020-05-19 17:43:36.909 T Content-Type: application/json
2020-05-19 17:43:36.909 T Last-Modified: Tue, 19 May 2020 17:43:36 GMT
2020-05-19 17:43:36.910 T Accept-Ranges: bytes
2020-05-19 17:43:36.910 T
2020-05-19 17:43:36.910 T mdb_txn_safe: destructor
2020-05-19 17:43:36.910 T Throttle throttle_speed_out: packet of ~845b  (from 845 b) Speed AVG=   0[w=9.966]    0[w=9.966] /  Limit=16 KiB/sec  [1213 0 0 781 270 0 0 0 0 0 ]
2020-05-19 17:43:36.911 D do_send_chunk() NOW SENSD: packet=845 B
2020-05-19 17:43:36.911 T Setting 00:30:00 expiry
2020-05-19 17:43:36.911 T Setting 00:30:00 expiry
2020-05-19 17:43:36.912 T [192.168.1.131:54281 INC] [sock 39] Async send calledback 845
2020-05-19 17:43:36.913 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:36.913 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.913 T mdb_txn_safe: destructor
2020-05-19 17:43:36.914 T Blockchain::get_transactions
2020-05-19 17:43:36.914 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:36.915 T BlockchainLMDB::height
2020-05-19 17:43:36.915 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.915 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.915 T mdb_txn_safe: destructor
2020-05-19 17:43:36.916 T BlockchainLMDB::get_block_already_generated_coins
2020-05-19 17:43:36.916 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.916 T mdb_txn_safe: destructor
2020-05-19 17:43:36.916 D Using 0.000000011197/byte fee
2020-05-19 17:43:36.916 T mdb_txn_safe: destructor
2020-05-19 17:43:36.919 T Blockchain::check_tx_outputs
2020-05-19 17:43:36.919 T Blockchain::check_tx_inputs
2020-05-19 17:43:36.919 T BlockchainLMDB::height
2020-05-19 17:43:36.919 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.919 T mdb_txn_safe: destructor
2020-05-19 17:43:36.920 T Blockchain::check_tx_inputs
2020-05-19 17:43:36.920 D Mixin: 10-10
2020-05-19 17:43:36.920 T Blockchain::have_tx_keyimg_as_spent
2020-05-19 17:43:36.920 T BlockchainLMDB::has_key_image
2020-05-19 17:43:36.920 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:36.965 T mdb_txn_safe: destructor
2020-05-19 17:43:36.965 T Blockchain::check_tx_input
2020-05-19 17:43:36.965 T Blockchain::scan_outputkeys_for_indexes
2020-05-19 17:43:36.965 T BlockchainLMDB::get_output_key
2020-05-19 17:43:36.966 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.129 T db3: 163
2020-05-19 17:43:37.129 T mdb_txn_safe: destructor
2020-05-19 17:43:37.129 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.129 T BlockchainLMDB::height
2020-05-19 17:43:37.129 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.130 T mdb_txn_safe: destructor
2020-05-19 17:43:37.130 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.130 T BlockchainLMDB::height
2020-05-19 17:43:37.130 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.130 T mdb_txn_safe: destructor
2020-05-19 17:43:37.130 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.130 T BlockchainLMDB::height
2020-05-19 17:43:37.130 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.130 T mdb_txn_safe: destructor
2020-05-19 17:43:37.130 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.130 T BlockchainLMDB::height
2020-05-19 17:43:37.131 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.131 T mdb_txn_safe: destructor
2020-05-19 17:43:37.131 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.131 T BlockchainLMDB::height
2020-05-19 17:43:37.131 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.131 T mdb_txn_safe: destructor
2020-05-19 17:43:37.131 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.131 T BlockchainLMDB::height
2020-05-19 17:43:37.131 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.131 T mdb_txn_safe: destructor
2020-05-19 17:43:37.132 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.132 T BlockchainLMDB::height
2020-05-19 17:43:37.132 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.132 T mdb_txn_safe: destructor
2020-05-19 17:43:37.132 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.132 T BlockchainLMDB::height
2020-05-19 17:43:37.132 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.132 T mdb_txn_safe: destructor
2020-05-19 17:43:37.132 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.132 T BlockchainLMDB::height
2020-05-19 17:43:37.132 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.132 T mdb_txn_safe: destructor
2020-05-19 17:43:37.133 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.133 T BlockchainLMDB::height
2020-05-19 17:43:37.133 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.133 T mdb_txn_safe: destructor
2020-05-19 17:43:37.133 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.133 T BlockchainLMDB::height
2020-05-19 17:43:37.133 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.133 T mdb_txn_safe: destructor
2020-05-19 17:43:37.133 T Blockchain::have_tx_keyimg_as_spent
2020-05-19 17:43:37.133 T BlockchainLMDB::has_key_image
2020-05-19 17:43:37.134 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.184 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.9)
2020-05-19 17:43:37.185 T Throttle throttle_speed_in: packet of ~115b  (from 115 b) Speed AVG=   0[w=9.23999]    0[w=9.23999] /  Limit=16 KiB/sec  [115 432 0 476 432 425 0 0 0 0 ]
2020-05-19 17:43:37.185 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.9)
2020-05-19 17:43:37.185 T Throttle <<< global-IN: packet of ~115b  (from 115 b) Speed AVG=   1[w=9.23999]    1[w=9.23999] /  Limit=8192 KiB/sec  [115 8369 0 476 8624 425 0 0 0 0 ]
2020-05-19 17:43:37.185 T HTTP HEAD:
2020-05-19 17:43:37.185 T Host: 192.168.1.116
2020-05-19 17:43:37.185 T Content-Length: 362
2020-05-19 17:43:37.185 T Content-Type: application/json; charset=utf-8
2020-05-19 17:43:37.185 T
2020-05-19 17:43:37.186 T Setting 00:29:59.748000 expiry
2020-05-19 17:43:37.187 T mdb_txn_safe: destructor
2020-05-19 17:43:37.188 T Blockchain::check_tx_input
2020-05-19 17:43:37.188 T Blockchain::scan_outputkeys_for_indexes
2020-05-19 17:43:37.188 T BlockchainLMDB::get_output_key
2020-05-19 17:43:37.189 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.235 T Throttle throttle_speed_in: packet of ~362b  (from 362 b) Speed AVG=   0[w=9.29]    0[w=9.29] /  Limit=16 KiB/sec  [477 432 0 476 432 425 0 0 0 0 ]
2020-05-19 17:43:37.235 T Throttle <<< global-IN: packet of ~362b  (from 362 b) Speed AVG=   1[w=9.291]    1[w=9.291] /  Limit=8192 KiB/sec  [477 8369 0 476 8624 425 0 0 0 0 ]
2020-05-19 17:43:37.235 I HTTP [192.168.1.131] GET /json_rpc
2020-05-19 17:43:37.236 I [192.168.1.131:54281 INC] Calling RPC method rpc_access_submit_nonce
2020-05-19 17:43:37.238 T Blockchain::get_tail_id
2020-05-19 17:43:37.382 I [202.142.33.132:18080 OUT] 9621 bytes sent for category command-2970651251 initiated by us
2020-05-19 17:43:37.383 T [202.142.33.132:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23505 < 23545 (last time 23505.2)
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23506 < 23545 (last time 23506.2)
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23507 < 23545 (last time 23507.2)
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23508 < 23545 (last time 23508.2)
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23509 < 23545 (last time 23509.2)
2020-05-19 17:43:37.383 T Moving counter buffer by 1 second 23510 < 23545 (last time 23510.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23511 < 23545 (last time 23511.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23512 < 23545 (last time 23512.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23513 < 23545 (last time 23513.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23514 < 23545 (last time 23514.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23515 < 23545 (last time 23515.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23516 < 23545 (last time 23516.2)
2020-05-19 17:43:37.384 T Moving counter buffer by 1 second 23517 < 23545 (last time 23517.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23518 < 23545 (last time 23518.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23519 < 23545 (last time 23519.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23520 < 23545 (last time 23520.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23521 < 23545 (last time 23521.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23522 < 23545 (last time 23522.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23523 < 23545 (last time 23523.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23524 < 23545 (last time 23524.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23525 < 23545 (last time 23525.2)
2020-05-19 17:43:37.385 T Moving counter buffer by 1 second 23526 < 23545 (last time 23526.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23527 < 23545 (last time 23527.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23528 < 23545 (last time 23528.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23529 < 23545 (last time 23529.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23530 < 23545 (last time 23530.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23531 < 23545 (last time 23531.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23532 < 23545 (last time 23532.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23533 < 23545 (last time 23533.2)
2020-05-19 17:43:37.386 T Moving counter buffer by 1 second 23534 < 23545 (last time 23534.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23535 < 23545 (last time 23535.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23536 < 23545 (last time 23536.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23537 < 23545 (last time 23537.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23538 < 23545 (last time 23538.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23539 < 23545 (last time 23539.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23540 < 23545 (last time 23540.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23541 < 23545 (last time 23541.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23542 < 23545 (last time 23542.2)
2020-05-19 17:43:37.387 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.2)
2020-05-19 17:43:37.388 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.2)
2020-05-19 17:43:37.388 T Throttle throttle_speed_out: packet of ~9654b  (from 9654 b) Speed AVG=   0[w=9.438]    0[w=9.438] /  Limit=16 KiB/sec  [9654 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.388 D do_send_chunk() NOW SENSD: packet=9654 B
2020-05-19 17:43:37.388 T handler_write (direct) - before ASIO write, for packet=9654 B (after sleep)
2020-05-19 17:43:37.388 T Setting 00:05:00 expiry
2020-05-19 17:43:37.388 D [202.142.33.132:18080 OUT] LEVIN_PACKET_SENT. [len=9621, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:37.389 T [202.142.33.132:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:37.389 T [202.142.33.132:18080 OUT] [sock 33] release
2020-05-19 17:43:37.389 T [202.142.33.132:18080 OUT] [sock 33] Async send calledback 9654
2020-05-19 17:43:37.389 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.5)
2020-05-19 17:43:37.390 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.5)
2020-05-19 17:43:37.390 T dbg >>> global-OUT: speed is A= 281.842 vs Max=2.09715e+06  so sleep: D=-9.44281 sec E=    2662 (Enow=   12316) M=2.09715e+06 W=   9.445 R=1.98049e+07 Wgood      11 History: [0 0 2662 0 0 0 0 0 0 0 ] m_last_sample_time= 23545.4
2020-05-19 17:43:37.390 T Throttle >>> global-OUT: packet of ~9654b  (from 9654 b) Speed AVG=   0[w=9.446]    0[w=9.446] /  Limit=2048 KiB/sec  [9654 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.403 T db3: 214
2020-05-19 17:43:37.403 T mdb_txn_safe: destructor
2020-05-19 17:43:37.403 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.404 T BlockchainLMDB::height
2020-05-19 17:43:37.404 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.405 T mdb_txn_safe: destructor
2020-05-19 17:43:37.405 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.405 T BlockchainLMDB::height
2020-05-19 17:43:37.405 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.406 T mdb_txn_safe: destructor
2020-05-19 17:43:37.406 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.406 T BlockchainLMDB::height
2020-05-19 17:43:37.407 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.407 T mdb_txn_safe: destructor
2020-05-19 17:43:37.407 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.407 T BlockchainLMDB::height
2020-05-19 17:43:37.408 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.409 T mdb_txn_safe: destructor
2020-05-19 17:43:37.409 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.410 T BlockchainLMDB::height
2020-05-19 17:43:37.410 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.411 T mdb_txn_safe: destructor
2020-05-19 17:43:37.412 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.412 T BlockchainLMDB::height
2020-05-19 17:43:37.413 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.413 T mdb_txn_safe: destructor
2020-05-19 17:43:37.414 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.415 T BlockchainLMDB::height
2020-05-19 17:43:37.415 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.416 T mdb_txn_safe: destructor
2020-05-19 17:43:37.416 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.417 T BlockchainLMDB::height
2020-05-19 17:43:37.418 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.418 T mdb_txn_safe: destructor
2020-05-19 17:43:37.419 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.419 T BlockchainLMDB::height
2020-05-19 17:43:37.420 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.420 T mdb_txn_safe: destructor
2020-05-19 17:43:37.421 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.421 T BlockchainLMDB::height
2020-05-19 17:43:37.421 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.422 T mdb_txn_safe: destructor
2020-05-19 17:43:37.422 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:37.422 T BlockchainLMDB::height
2020-05-19 17:43:37.423 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.423 T mdb_txn_safe: destructor
2020-05-19 17:43:37.423 T BlockchainLMDB::height
2020-05-19 17:43:37.424 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.424 T mdb_txn_safe: destructor
2020-05-19 17:43:37.500 T BlockchainLMDB::height
2020-05-19 17:43:37.500 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.501 T mdb_txn_safe: destructor
2020-05-19 17:43:37.501 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:37.501 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.502 T mdb_txn_safe: destructor
2020-05-19 17:43:37.502 T BlockchainLMDB::batch_start
2020-05-19 17:43:37.502 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:37.503 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:37.504 T BlockchainLMDB::need_resize
2020-05-19 17:43:37.504 D DB map size:     98557263872
2020-05-19 17:43:37.504 D Space used:      88234479616
2020-05-19 17:43:37.505 D Space remaining: 10322784256
2020-05-19 17:43:37.505 D Size threshold:  0
2020-05-19 17:43:37.505 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:37.506 T batch transaction: begin
2020-05-19 17:43:37.506 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:37.506 T BlockchainLMDB::remove_txpool_tx
2020-05-19 17:43:37.507 T BlockchainLMDB::add_txpool_tx
2020-05-19 17:43:37.507 T BlockchainLMDB::batch_stop
2020-05-19 17:43:37.508 T batch transaction: committing...
2020-05-19 17:43:37.518 T mdb_txn_safe: destructor
2020-05-19 17:43:37.518 T batch transaction: end
2020-05-19 17:43:37.519 I Transaction added to pool: txid <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19> weight: 2605 fee/byte: 11197.6
2020-05-19 17:43:37.519 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:37.520 T BlockchainLMDB::height
2020-05-19 17:43:37.520 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.520 T mdb_txn_safe: destructor
2020-05-19 17:43:37.520 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:37.521 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.521 T mdb_txn_safe: destructor
2020-05-19 17:43:37.521 I client <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> sends nonce: 110, current
2020-05-19 17:43:37.521 T BlockchainLMDB::batch_start
2020-05-19 17:43:37.521 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:37.522 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:37.522 T BlockchainLMDB::need_resize
2020-05-19 17:43:37.522 D DB map size:     98557263872
2020-05-19 17:43:37.523 D Space used:      88234479616
2020-05-19 17:43:37.523 D Space remaining: 10322784256
2020-05-19 17:43:37.523 D Size threshold:  0
2020-05-19 17:43:37.524 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:37.524 T batch transaction: begin
2020-05-19 17:43:37.524 T BlockchainLMDB::batch_stop
2020-05-19 17:43:37.525 T batch transaction: committing...
2020-05-19 17:43:37.525 T mdb_txn_safe: destructor
2020-05-19 17:43:37.525 T batch transaction: end
2020-05-19 17:43:37.526 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.526 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.527 T mdb_txn_safe: destructor
2020-05-19 17:43:37.527 T Blockchain::get_transactions
2020-05-19 17:43:37.528 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.528 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.528 T mdb_txn_safe: destructor
2020-05-19 17:43:37.528 T Blockchain::get_transactions
2020-05-19 17:43:37.528 D tx added: <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>
2020-05-19 17:43:37.534 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.535 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.535 T mdb_txn_safe: destructor
2020-05-19 17:43:37.538 D We have all needed txes for this fluffy block
2020-05-19 17:43:37.539 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.539 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.539 D Couldn't use largePages for RandomX VM
2020-05-19 17:43:37.539 T mdb_txn_safe: destructor
2020-05-19 17:43:37.542 D We have all needed txes for this fluffy block
2020-05-19 17:43:37.543 T BlockchainLMDB::batch_start
2020-05-19 17:43:37.544 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:37.544 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:37.545 T BlockchainLMDB::need_resize
2020-05-19 17:43:37.545 D DB map size:     98557263872
2020-05-19 17:43:37.546 D Space used:      88234479616
2020-05-19 17:43:37.546 D Space remaining: 10322784256
2020-05-19 17:43:37.547 D Size threshold:  0
2020-05-19 17:43:37.547 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:37.548 T batch transaction: begin
2020-05-19 17:43:37.548 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:37.549 T BlockchainLMDB::update_txpool_tx
2020-05-19 17:43:37.549 T BlockchainLMDB::batch_stop
2020-05-19 17:43:37.550 T batch transaction: committing...
2020-05-19 17:43:37.556 T mdb_txn_safe: destructor
2020-05-19 17:43:37.557 T batch transaction: end
2020-05-19 17:43:37.557 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:37.557 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.558 T mdb_txn_safe: destructor
2020-05-19 17:43:37.558 T Blockchain::have_tx
2020-05-19 17:43:37.558 T BlockchainLMDB::tx_exists
2020-05-19 17:43:37.559 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.559 T mdb_txn_safe: destructor
2020-05-19 17:43:37.559 D tx <4200b41a6b55d0991929958f5d465a00a428718fd252456222e69b4cf28cee2f> already have transaction in blockchain
2020-05-19 17:43:37.560 T BlockchainLMDB::height
2020-05-19 17:43:37.560 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.560 T mdb_txn_safe: destructor
2020-05-19 17:43:37.561 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.561 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.561 T mdb_txn_safe: destructor
2020-05-19 17:43:37.561 T Blockchain::get_transactions
2020-05-19 17:43:37.562 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.562 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.562 T mdb_txn_safe: destructor
2020-05-19 17:43:37.564 D Queueing 1 transaction(s) for Dandelion++ fluffing
2020-05-19 17:43:37.565 D [183.82.83.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:37.565 I [183.82.83.167:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:37.565 I [183.82.83.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:37.566 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:37.566 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.566 T mdb_txn_safe: destructor
2020-05-19 17:43:37.566 T Blockchain::have_tx
2020-05-19 17:43:37.566 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.566 T BlockchainLMDB::tx_exists
2020-05-19 17:43:37.567 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.567 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.567 T mdb_txn_safe: destructor
2020-05-19 17:43:37.567 D tx <4200b41a6b55d0991929958f5d465a00a428718fd252456222e69b4cf28cee2f> already have transaction in blockchain
2020-05-19 17:43:37.567 T mdb_txn_safe: destructor
2020-05-19 17:43:37.568 T BlockchainLMDB::height
2020-05-19 17:43:37.568 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.568 T Blockchain::get_transactions
2020-05-19 17:43:37.568 I Including transaction <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:37.568 T mdb_txn_safe: destructor
2020-05-19 17:43:37.568 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.569 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.569 T Blockchain::prepare_handle_incoming_blocks
2020-05-19 17:43:37.569 T mdb_txn_safe: destructor
2020-05-19 17:43:37.572 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.572 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.572 T mdb_txn_safe: destructor
2020-05-19 17:43:37.572 T Blockchain::get_transactions
2020-05-19 17:43:37.573 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.573 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.573 T mdb_txn_safe: destructor
2020-05-19 17:43:37.575 T BlockchainLMDB::batch_start
2020-05-19 17:43:37.576 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:37.576 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:37.576 T BlockchainLMDB::get_estimated_batch_size
2020-05-19 17:43:37.576 T BlockchainLMDB::height
2020-05-19 17:43:37.576 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.577 T mdb_txn_safe: destructor
2020-05-19 17:43:37.577 D [get_estimated_batch_size] m_height: 2101897  block_start: 2101397  block_stop: 2101896
2020-05-19 17:43:37.577 D estimated average block size for batch: 24857
2020-05-19 17:43:37.577 D calculated batch size: 559282496
2020-05-19 17:43:37.577 D increase size: 559282496
2020-05-19 17:43:37.577 T BlockchainLMDB::need_resize
2020-05-19 17:43:37.578 D DB map size:     98557263872
2020-05-19 17:43:37.578 D Space used:      88234479616
2020-05-19 17:43:37.578 D Space remaining: 10322784256
2020-05-19 17:43:37.578 D Size threshold:  559282496
2020-05-19 17:43:37.578 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:37.578 T batch transaction: begin
2020-05-19 17:43:37.579 T BlockchainLMDB::height
2020-05-19 17:43:37.579 D block_batches: 0
2020-05-19 17:43:37.579 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:37.579 T BlockchainLMDB::height
2020-05-19 17:43:37.579 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:37.580 T Blockchain::have_block
2020-05-19 17:43:37.580 T BlockchainLMDB::block_exists
2020-05-19 17:43:37.581 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:37.581 D Skipping remainder of prepare blocks. Blocks exist.
2020-05-19 17:43:37.581 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:37.581 T Blockchain::add_new_block
2020-05-19 17:43:37.581 T Blockchain::have_block
2020-05-19 17:43:37.582 T BlockchainLMDB::block_exists
2020-05-19 17:43:37.582 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:37.582 T block with id = <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> already exists
2020-05-19 17:43:37.582 T Blockchain::cleanup_handle_incoming_blocks
2020-05-19 17:43:37.582 T BlockchainLMDB::batch_stop
2020-05-19 17:43:37.582 T batch transaction: committing...
2020-05-19 17:43:37.583 T mdb_txn_safe: destructor
2020-05-19 17:43:37.583 T batch transaction: end
2020-05-19 17:43:37.583 T BlockchainLMDB::prune_worker
2020-05-19 17:43:37.583 T mdb_txn_safe: abort()
2020-05-19 17:43:37.583 D Pruning not enabled, nothing to do
2020-05-19 17:43:37.583 T mdb_txn_safe: destructor
2020-05-19 17:43:37.584 T Blockchain::prepare_handle_incoming_blocks
2020-05-19 17:43:37.584 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.584 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.584 D miner::resume: 4 -> 3
2020-05-19 17:43:37.584 T mdb_txn_safe: destructor
2020-05-19 17:43:37.584 T Blockchain::get_transactions
2020-05-19 17:43:37.585 T Setting 00:04:59.046000 expiry
2020-05-19 17:43:37.585 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.585 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.585 T mdb_txn_safe: destructor
2020-05-19 17:43:37.588 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.588 T [51.158.78.247:18080 OUT] [sock 32] Async send calledback 2662
2020-05-19 17:43:37.589 T dbg >>> global-OUT: speed is A= 1277.06 vs Max=2.09715e+06  so sleep: D=-9.63787 sec E=   12316 (Enow=   14978) M=2.09715e+06 W=   9.644 R=2.02126e+07 Wgood      11 History: [9654 0 2662 0 0 0 0 0 0 0 ] m_last_sample_time= 23545.6
2020-05-19 17:43:37.589 T Throttle >>> global-OUT: packet of ~2662b  (from 2662 b) Speed AVG=   1[w=9.645]    1[w=9.645] /  Limit=2048 KiB/sec  [12316 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.589 T Moving counter buffer by 1 second 23530 < 23545 (last time 23530.1)
2020-05-19 17:43:37.589 T Moving counter buffer by 1 second 23531 < 23545 (last time 23531.1)
2020-05-19 17:43:37.590 T Moving counter buffer by 1 second 23532 < 23545 (last time 23532.1)
2020-05-19 17:43:37.590 T Moving counter buffer by 1 second 23533 < 23545 (last time 23533.1)
2020-05-19 17:43:37.590 T Moving counter buffer by 1 second 23534 < 23545 (last time 23534.1)
2020-05-19 17:43:37.590 T Moving counter buffer by 1 second 23535 < 23545 (last time 23535.1)
2020-05-19 17:43:37.590 T Moving counter buffer by 1 second 23536 < 23545 (last time 23536.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23537 < 23545 (last time 23537.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23538 < 23545 (last time 23538.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23539 < 23545 (last time 23539.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23540 < 23545 (last time 23540.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23541 < 23545 (last time 23541.1)
2020-05-19 17:43:37.591 T Moving counter buffer by 1 second 23542 < 23545 (last time 23542.1)
2020-05-19 17:43:37.592 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.1)
2020-05-19 17:43:37.592 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.1)
2020-05-19 17:43:37.592 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=   0[w=9.645]    0[w=9.645] /  Limit=16 KiB/sec  [8192 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.592 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=   1[w=9.648]    1[w=9.648] /  Limit=8192 KiB/sec  [8669 8369 0 476 8624 425 0 0 0 0 ]
2020-05-19 17:43:37.593 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.593 T dbg <<< global-IN: speed is A= 2753.21 vs Max=8.38861e+06  so sleep: D=-9.64464 sec E=   26563 (Enow=   34755) M=8.38861e+06 W=   9.648 R=8.09067e+07 Wgood      11 History: [8669 8369 0 476 8624 425 0 0 0 0 ] m_last_sample_time= 23545.6
2020-05-19 17:43:37.593 T mdb_txn_safe: destructor
2020-05-19 17:43:37.593 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:37.593 T Blockchain::get_transactions
2020-05-19 17:43:37.594 T BlockchainLMDB::batch_start
2020-05-19 17:43:37.594 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:37.594 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:37.594 T BlockchainLMDB::get_estimated_batch_size
2020-05-19 17:43:37.594 T BlockchainLMDB::height
2020-05-19 17:43:37.594 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.594 T mdb_txn_safe: destructor
2020-05-19 17:43:37.594 D [get_estimated_batch_size] m_height: 2101897  block_start: 2101397  block_stop: 2101896
2020-05-19 17:43:37.595 D estimated average block size for batch: 24857
2020-05-19 17:43:37.595 D calculated batch size: 559282496
2020-05-19 17:43:37.595 D increase size: 559282496
2020-05-19 17:43:37.595 T BlockchainLMDB::need_resize
2020-05-19 17:43:37.595 D DB map size:     98557263872
2020-05-19 17:43:37.595 D Space used:      88234479616
2020-05-19 17:43:37.595 D Space remaining: 10322784256
2020-05-19 17:43:37.595 D Size threshold:  559282496
2020-05-19 17:43:37.595 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:37.595 T batch transaction: begin
2020-05-19 17:43:37.596 T BlockchainLMDB::height
2020-05-19 17:43:37.596 D block_batches: 0
2020-05-19 17:43:37.596 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:37.596 T BlockchainLMDB::height
2020-05-19 17:43:37.596 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:37.597 T Blockchain::have_block
2020-05-19 17:43:37.597 T BlockchainLMDB::block_exists
2020-05-19 17:43:37.597 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:37.597 D Skipping remainder of prepare blocks. Blocks exist.
2020-05-19 17:43:37.597 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:37.598 T Blockchain::add_new_block
2020-05-19 17:43:37.598 I [51.158.78.247:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:37.598 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:37.598 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.598 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.599 T mdb_txn_safe: destructor
2020-05-19 17:43:37.601 T Blockchain::have_block
2020-05-19 17:43:37.602 T BlockchainLMDB::block_exists
2020-05-19 17:43:37.602 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:37.602 T block with id = <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> already exists
2020-05-19 17:43:37.602 T Blockchain::cleanup_handle_incoming_blocks
2020-05-19 17:43:37.603 T BlockchainLMDB::batch_stop
2020-05-19 17:43:37.603 T batch transaction: committing...
2020-05-19 17:43:37.603 T mdb_txn_safe: destructor
2020-05-19 17:43:37.603 T batch transaction: end
2020-05-19 17:43:37.603 T BlockchainLMDB::prune_worker
2020-05-19 17:43:37.603 T mdb_txn_safe: abort()
2020-05-19 17:43:37.604 D Pruning not enabled, nothing to do
2020-05-19 17:43:37.604 T mdb_txn_safe: destructor
2020-05-19 17:43:37.604 D miner::resume: 3 -> 2
2020-05-19 17:43:37.604 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.605 T Setting 00:04:59.216000 expiry
2020-05-19 17:43:37.605 T [5.79.64.237:18080 OUT] [sock 35] Async send calledback 7045
2020-05-19 17:43:37.605 T dbg >>> global-OUT: speed is A= 1550.36 vs Max=2.09715e+06  so sleep: D=-9.65319 sec E=   14978 (Enow=   22023) M=2.09715e+06 W=   9.661 R=2.02456e+07 Wgood      11 History: [12316 0 2662 0 0 0 0 0 0 0 ] m_last_sample_time= 23545.7
2020-05-19 17:43:37.605 T Throttle >>> global-OUT: packet of ~7045b  (from 7045 b) Speed AVG=   1[w=9.661]    1[w=9.661] /  Limit=2048 KiB/sec  [19361 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.606 T Moving counter buffer by 1 second 23530 < 23545 (last time 23530.1)
2020-05-19 17:43:37.606 T Moving counter buffer by 1 second 23531 < 23545 (last time 23531.1)
2020-05-19 17:43:37.606 T Moving counter buffer by 1 second 23532 < 23545 (last time 23532.1)
2020-05-19 17:43:37.606 T Moving counter buffer by 1 second 23533 < 23545 (last time 23533.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23534 < 23545 (last time 23534.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23535 < 23545 (last time 23535.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23536 < 23545 (last time 23536.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23537 < 23545 (last time 23537.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23538 < 23545 (last time 23538.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23539 < 23545 (last time 23539.1)
2020-05-19 17:43:37.607 T Moving counter buffer by 1 second 23540 < 23545 (last time 23540.1)
2020-05-19 17:43:37.608 T Moving counter buffer by 1 second 23541 < 23545 (last time 23541.1)
2020-05-19 17:43:37.608 T Moving counter buffer by 1 second 23542 < 23545 (last time 23542.1)
2020-05-19 17:43:37.608 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.1)
2020-05-19 17:43:37.608 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.1)
2020-05-19 17:43:37.608 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=   0[w=9.661]    0[w=9.661] /  Limit=16 KiB/sec  [8192 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.609 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=   2[w=9.664]    2[w=9.664] /  Limit=8192 KiB/sec  [16861 8369 0 476 8624 425 0 0 0 0 ]
2020-05-19 17:43:37.609 T dbg <<< global-IN: speed is A= 3595.96 vs Max=8.38861e+06  so sleep: D=-9.66066 sec E=   34755 (Enow=   42947) M=8.38861e+06 W=   9.665 R=8.10411e+07 Wgood      11 History: [16861 8369 0 476 8624 425 0 0 0 0 ] m_last_sample_time= 23545.7
2020-05-19 17:43:37.609 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:37.610 I [5.79.64.237:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:37.610 I Including transaction <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>
2020-05-19 17:43:37.610 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.610 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:37.611 T mdb_txn_safe: destructor
2020-05-19 17:43:37.611 T Blockchain::get_transactions
2020-05-19 17:43:37.611 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.611 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.611 T mdb_txn_safe: destructor
2020-05-19 17:43:37.612 T Blockchain::get_transactions
2020-05-19 17:43:37.612 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.612 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.612 T mdb_txn_safe: destructor
2020-05-19 17:43:37.614 I Including transaction <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>
2020-05-19 17:43:37.615 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.615 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.616 T mdb_txn_safe: destructor
2020-05-19 17:43:37.618 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:37.619 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.619 T mdb_txn_safe: destructor
2020-05-19 17:43:37.619 T Blockchain::have_tx
2020-05-19 17:43:37.619 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.619 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.620 T mdb_txn_safe: destructor
2020-05-19 17:43:37.620 T Blockchain::get_transactions
2020-05-19 17:43:37.620 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.621 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.621 T mdb_txn_safe: destructor
2020-05-19 17:43:37.621 T Blockchain::get_transactions
2020-05-19 17:43:37.621 T BlockchainLMDB::tx_exists
2020-05-19 17:43:37.621 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.621 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.622 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.622 T mdb_txn_safe: destructor
2020-05-19 17:43:37.632 I [194.71.130.90:18080 OUT] 12228 bytes sent for category command-2970913395 initiated by us
2020-05-19 17:43:37.633 T [194.71.130.90:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:37.633 T Moving counter buffer by 1 second 23507 < 23545 (last time 23507.9)
2020-05-19 17:43:37.633 T Moving counter buffer by 1 second 23508 < 23545 (last time 23508.9)
2020-05-19 17:43:37.633 T Moving counter buffer by 1 second 23509 < 23545 (last time 23509.9)
2020-05-19 17:43:37.633 T Moving counter buffer by 1 second 23510 < 23545 (last time 23510.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23511 < 23545 (last time 23511.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23512 < 23545 (last time 23512.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23513 < 23545 (last time 23513.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23514 < 23545 (last time 23514.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23515 < 23545 (last time 23515.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23516 < 23545 (last time 23516.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23517 < 23545 (last time 23517.9)
2020-05-19 17:43:37.634 T Moving counter buffer by 1 second 23518 < 23545 (last time 23518.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23519 < 23545 (last time 23519.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23520 < 23545 (last time 23520.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23521 < 23545 (last time 23521.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23522 < 23545 (last time 23522.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23523 < 23545 (last time 23523.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23524 < 23545 (last time 23524.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23525 < 23545 (last time 23525.9)
2020-05-19 17:43:37.635 T Moving counter buffer by 1 second 23526 < 23545 (last time 23526.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23527 < 23545 (last time 23527.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23528 < 23545 (last time 23528.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23529 < 23545 (last time 23529.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23530 < 23545 (last time 23530.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23531 < 23545 (last time 23531.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23532 < 23545 (last time 23532.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23533 < 23545 (last time 23533.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23534 < 23545 (last time 23534.9)
2020-05-19 17:43:37.636 T Moving counter buffer by 1 second 23535 < 23545 (last time 23535.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23536 < 23545 (last time 23536.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23537 < 23545 (last time 23537.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23538 < 23545 (last time 23538.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23539 < 23545 (last time 23539.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23540 < 23545 (last time 23540.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23541 < 23545 (last time 23541.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23542 < 23545 (last time 23542.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.9)
2020-05-19 17:43:37.637 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.9)
2020-05-19 17:43:37.638 T Throttle throttle_speed_out: packet of ~12261b  (from 12261 b) Speed AVG=   0[w=9.689]    0[w=9.689] /  Limit=16 KiB/sec  [12261 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.638 D do_send_chunk() NOW SENSD: packet=12261 B
2020-05-19 17:43:37.638 T handler_write (direct) - before ASIO write, for packet=12261 B (after sleep)
2020-05-19 17:43:37.638 T Setting 00:05:00 expiry
2020-05-19 17:43:37.638 D [194.71.130.90:18080 OUT] LEVIN_PACKET_SENT. [len=12228, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:37.639 T [194.71.130.90:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:37.639 T [194.71.130.90:18080 OUT] [sock 26] release
2020-05-19 17:43:37.639 T [194.71.130.90:18080 OUT] [sock 26] Async send calledback 12261
2020-05-19 17:43:37.639 I [195.201.12.110:18080 OUT] 12228 bytes sent for category command-2970913395 initiated by us
2020-05-19 17:43:37.639 T dbg >>> global-OUT: speed is A= 2271.58 vs Max=2.09715e+06  so sleep: D=-9.68333 sec E=   22023 (Enow=   34284) M=2.09715e+06 W=   9.695 R=2.03099e+07 Wgood      11 History: [19361 0 2662 0 0 0 0 0 0 0 ] m_last_sample_time= 23545.7
2020-05-19 17:43:37.639 T [195.201.12.110:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:37.640 T Throttle >>> global-OUT: packet of ~12261b  (from 12261 b) Speed AVG=   2[w=9.695]    2[w=9.695] /  Limit=2048 KiB/sec  [31622 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23529 < 23545 (last time 23529.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23530 < 23545 (last time 23530.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23531 < 23545 (last time 23531.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23532 < 23545 (last time 23532.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23533 < 23545 (last time 23533.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23534 < 23545 (last time 23534.9)
2020-05-19 17:43:37.640 T Moving counter buffer by 1 second 23535 < 23545 (last time 23535.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23536 < 23545 (last time 23536.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23537 < 23545 (last time 23537.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23538 < 23545 (last time 23538.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23539 < 23545 (last time 23539.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23540 < 23545 (last time 23540.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23541 < 23545 (last time 23541.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23542 < 23545 (last time 23542.9)
2020-05-19 17:43:37.641 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.9)
2020-05-19 17:43:37.642 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.9)
2020-05-19 17:43:37.642 T Throttle throttle_speed_out: packet of ~12261b  (from 12261 b) Speed AVG=   0[w=9.695]    0[w=9.695] /  Limit=16 KiB/sec  [12261 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.642 D do_send_chunk() NOW SENSD: packet=12261 B
2020-05-19 17:43:37.642 T handler_write (direct) - before ASIO write, for packet=12261 B (after sleep)
2020-05-19 17:43:37.642 T Setting 00:05:00 expiry
2020-05-19 17:43:37.642 D [195.201.12.110:18080 OUT] LEVIN_PACKET_SENT. [len=12228, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:37.643 T [195.201.12.110:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:37.643 T [195.201.12.110:18080 OUT] [sock 38] release
2020-05-19 17:43:37.696 I transaction with hash 35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040 not found in db
2020-05-19 17:43:37.697 T mdb_txn_safe: destructor
2020-05-19 17:43:37.698 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:37.699 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.700 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.700 T mdb_txn_safe: destructor
2020-05-19 17:43:37.702 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.703 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.703 T mdb_txn_safe: destructor
2020-05-19 17:43:37.703 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.703 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.703 T mdb_txn_safe: destructor
2020-05-19 17:43:37.703 T Blockchain::get_transactions
2020-05-19 17:43:37.703 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.703 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.704 T mdb_txn_safe: destructor
2020-05-19 17:43:37.706 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.706 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.707 T mdb_txn_safe: destructor
2020-05-19 17:43:37.707 T Blockchain::get_transactions
2020-05-19 17:43:37.707 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.707 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.707 T mdb_txn_safe: destructor
2020-05-19 17:43:37.710 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.710 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.710 T mdb_txn_safe: destructor
2020-05-19 17:43:37.710 T Blockchain::get_transactions
2020-05-19 17:43:37.710 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.710 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.711 T mdb_txn_safe: destructor
2020-05-19 17:43:37.713 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.714 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.714 T mdb_txn_safe: destructor
2020-05-19 17:43:37.714 T Blockchain::get_transactions
2020-05-19 17:43:37.714 T Blockchain::get_transactions
2020-05-19 17:43:37.714 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.714 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.714 T mdb_txn_safe: destructor
2020-05-19 17:43:37.717 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.717 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.717 T mdb_txn_safe: destructor
2020-05-19 17:43:37.717 T Blockchain::get_transactions
2020-05-19 17:43:37.718 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.718 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.718 T mdb_txn_safe: destructor
2020-05-19 17:43:37.721 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.721 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.721 T mdb_txn_safe: destructor
2020-05-19 17:43:37.721 T Blockchain::get_transactions
2020-05-19 17:43:37.721 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.721 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.721 T mdb_txn_safe: destructor
2020-05-19 17:43:37.724 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.724 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.724 T mdb_txn_safe: destructor
2020-05-19 17:43:37.725 T Blockchain::get_transactions
2020-05-19 17:43:37.725 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.725 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.725 T mdb_txn_safe: destructor
2020-05-19 17:43:37.728 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.728 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.728 T mdb_txn_safe: destructor
2020-05-19 17:43:37.728 T Blockchain::get_transactions
2020-05-19 17:43:37.728 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.728 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.728 T mdb_txn_safe: destructor
2020-05-19 17:43:37.731 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.731 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.732 T mdb_txn_safe: destructor
2020-05-19 17:43:37.734 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.735 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.735 T mdb_txn_safe: destructor
2020-05-19 17:43:37.735 T Blockchain::get_transactions
2020-05-19 17:43:37.735 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.735 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.735 T mdb_txn_safe: destructor
2020-05-19 17:43:37.738 T BlockchainLMDB::get_txpool_tx_blob
2020-05-19 17:43:37.738 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.738 T mdb_txn_safe: destructor
2020-05-19 17:43:37.738 T Blockchain::get_transactions
2020-05-19 17:43:37.738 T BlockchainLMDB::get_tx_blob
2020-05-19 17:43:37.739 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.739 I [62.121.116.122:18080 OUT] 9619 bytes sent for category command-2970651251 initiated by us
2020-05-19 17:43:37.739 T mdb_txn_safe: destructor
2020-05-19 17:43:37.742 D We have all needed txes for this fluffy block
2020-05-19 17:43:37.742 T [62.121.116.122:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:37.742 D We have all needed txes for this fluffy block
2020-05-19 17:43:37.742 T Moving counter buffer by 1 second 23543 < 23545 (last time 23543.4)
2020-05-19 17:43:37.742 T Moving counter buffer by 1 second 23544 < 23545 (last time 23544.4)
2020-05-19 17:43:37.743 T Throttle throttle_speed_out: packet of ~9652b  (from 9652 b) Speed AVG=   0[w=9.798]    0[w=9.798] /  Limit=16 KiB/sec  [9652 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.743 D do_send_chunk() NOW SENSD: packet=9652 B
2020-05-19 17:43:37.743 T handler_write (direct) - before ASIO write, for packet=9652 B (after sleep)
2020-05-19 17:43:37.743 T Setting 00:05:00 expiry
2020-05-19 17:43:37.744 D [62.121.116.122:18080 OUT] LEVIN_PACKET_SENT. [len=9619, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:37.744 T [62.121.116.122:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:37.744 T [62.121.116.122:18080 OUT] [sock 34] release
2020-05-19 17:43:37.745 T [62.121.116.122:18080 OUT] [sock 34] Async send calledback 9652
2020-05-19 17:43:37.745 T dbg >>> global-OUT: speed is A= 3498.37 vs Max=2.09715e+06  so sleep: D=-9.78273 sec E=   34284 (Enow=   43936) M=2.09715e+06 W=     9.8 R=2.05178e+07 Wgood      11 History: [31622 0 2662 0 0 0 0 0 0 0 ] m_last_sample_time= 23545.8
2020-05-19 17:43:37.745 T Throttle >>> global-OUT: packet of ~9652b  (from 9652 b) Speed AVG=   3[w=9.801]    3[w=9.801] /  Limit=2048 KiB/sec  [41274 0 2662 0 0 0 0 0 0 0 ]
2020-05-19 17:43:37.779 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:37.780 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.780 T mdb_txn_safe: destructor
2020-05-19 17:43:37.781 T Blockchain::have_tx
2020-05-19 17:43:37.781 T BlockchainLMDB::tx_exists
2020-05-19 17:43:37.781 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.782 I transaction with hash 35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040 not found in db
2020-05-19 17:43:37.782 T mdb_txn_safe: destructor
2020-05-19 17:43:37.782 T BlockchainLMDB::height
2020-05-19 17:43:37.783 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.783 T mdb_txn_safe: destructor
2020-05-19 17:43:37.783 T BlockchainLMDB::get_block_already_generated_coins
2020-05-19 17:43:37.784 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.784 T mdb_txn_safe: destructor
2020-05-19 17:43:37.784 D Using 0.000000011197/byte fee
2020-05-19 17:43:37.784 T Blockchain::check_tx_outputs
2020-05-19 17:43:37.784 T Blockchain::check_tx_inputs
2020-05-19 17:43:37.785 T BlockchainLMDB::height
2020-05-19 17:43:37.785 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.785 T mdb_txn_safe: destructor
2020-05-19 17:43:37.785 T Blockchain::check_tx_inputs
2020-05-19 17:43:37.785 D Mixin: 10-10
2020-05-19 17:43:37.785 T Blockchain::have_tx_keyimg_as_spent
2020-05-19 17:43:37.785 T BlockchainLMDB::has_key_image
2020-05-19 17:43:37.785 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.833 T mdb_txn_safe: destructor
2020-05-19 17:43:37.833 T Blockchain::check_tx_input
2020-05-19 17:43:37.834 T Blockchain::scan_outputkeys_for_indexes
2020-05-19 17:43:37.834 T BlockchainLMDB::get_output_key
2020-05-19 17:43:37.834 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:37.989 I [51.158.78.247:18080 OUT] 9619 bytes sent for category command-2970651251 initiated by us
2020-05-19 17:43:37.990 T [51.158.78.247:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:37.990 T Moving counter buffer by 1 second 23543 < 23546 (last time 23543.5)
2020-05-19 17:43:37.991 T Moving counter buffer by 1 second 23544 < 23546 (last time 23544.5)
2020-05-19 17:43:37.992 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.5)
2020-05-19 17:43:37.992 T Throttle throttle_speed_out: packet of ~9652b  (from 9652 b) Speed AVG=   0[w=9.046]    0[w=9.046] /  Limit=16 KiB/sec  [9652 0 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:37.993 D do_send_chunk() NOW SENSD: packet=9652 B
2020-05-19 17:43:37.994 T handler_write (direct) - before ASIO write, for packet=9652 B (after sleep)
2020-05-19 17:43:37.995 T Setting 00:05:00 expiry
2020-05-19 17:43:37.995 D [51.158.78.247:18080 OUT] LEVIN_PACKET_SENT. [len=9619, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:37.996 T [51.158.78.247:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:37.997 T [51.158.78.247:18080 OUT] [sock 32] release
2020-05-19 17:43:38.077 T db3: 244
2020-05-19 17:43:38.078 T mdb_txn_safe: destructor
2020-05-19 17:43:38.078 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.078 T BlockchainLMDB::height
2020-05-19 17:43:38.078 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.078 T mdb_txn_safe: destructor
2020-05-19 17:43:38.078 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.079 T BlockchainLMDB::height
2020-05-19 17:43:38.079 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.079 T mdb_txn_safe: destructor
2020-05-19 17:43:38.079 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.079 T BlockchainLMDB::height
2020-05-19 17:43:38.079 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.080 T mdb_txn_safe: destructor
2020-05-19 17:43:38.080 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.080 T BlockchainLMDB::height
2020-05-19 17:43:38.080 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.080 T mdb_txn_safe: destructor
2020-05-19 17:43:38.080 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.080 T BlockchainLMDB::height
2020-05-19 17:43:38.081 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.081 T mdb_txn_safe: destructor
2020-05-19 17:43:38.081 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.081 T BlockchainLMDB::height
2020-05-19 17:43:38.081 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.081 T mdb_txn_safe: destructor
2020-05-19 17:43:38.082 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.082 T BlockchainLMDB::height
2020-05-19 17:43:38.082 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.082 T mdb_txn_safe: destructor
2020-05-19 17:43:38.082 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.082 T BlockchainLMDB::height
2020-05-19 17:43:38.083 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.083 T mdb_txn_safe: destructor
2020-05-19 17:43:38.083 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.083 T BlockchainLMDB::height
2020-05-19 17:43:38.083 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.083 T mdb_txn_safe: destructor
2020-05-19 17:43:38.083 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.083 T BlockchainLMDB::height
2020-05-19 17:43:38.084 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.084 T mdb_txn_safe: destructor
2020-05-19 17:43:38.084 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.084 T BlockchainLMDB::height
2020-05-19 17:43:38.084 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.084 T mdb_txn_safe: destructor
2020-05-19 17:43:38.085 T BlockchainLMDB::height
2020-05-19 17:43:38.085 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.085 T mdb_txn_safe: destructor
2020-05-19 17:43:38.126 T BlockchainLMDB::height
2020-05-19 17:43:38.126 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.127 T mdb_txn_safe: destructor
2020-05-19 17:43:38.127 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:38.127 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.127 T mdb_txn_safe: destructor
2020-05-19 17:43:38.127 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.128 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.128 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.128 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.128 D DB map size:     98557263872
2020-05-19 17:43:38.128 D Space used:      88234479616
2020-05-19 17:43:38.128 D Space remaining: 10322784256
2020-05-19 17:43:38.129 D Size threshold:  0
2020-05-19 17:43:38.129 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.129 T batch transaction: begin
2020-05-19 17:43:38.129 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:38.129 T BlockchainLMDB::remove_txpool_tx
2020-05-19 17:43:38.130 T BlockchainLMDB::add_txpool_tx
2020-05-19 17:43:38.130 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.130 T batch transaction: committing...
2020-05-19 17:43:38.138 T mdb_txn_safe: destructor
2020-05-19 17:43:38.138 T batch transaction: end
2020-05-19 17:43:38.139 I Transaction added to pool: txid <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040> weight: 1772 fee/byte: 58391.6
2020-05-19 17:43:38.139 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.139 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.139 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.139 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.140 D DB map size:     98557263872
2020-05-19 17:43:38.140 D Space used:      88234479616
2020-05-19 17:43:38.140 D Space remaining: 10322784256
2020-05-19 17:43:38.140 D Size threshold:  0
2020-05-19 17:43:38.140 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.140 T batch transaction: begin
2020-05-19 17:43:38.141 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.141 T batch transaction: committing...
2020-05-19 17:43:38.141 T mdb_txn_safe: destructor
2020-05-19 17:43:38.141 T batch transaction: end
2020-05-19 17:43:38.141 D tx added: <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:38.145 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.145 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.145 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.145 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.145 D DB map size:     98557263872
2020-05-19 17:43:38.145 D Space used:      88234479616
2020-05-19 17:43:38.146 D Space remaining: 10322784256
2020-05-19 17:43:38.146 D Size threshold:  0
2020-05-19 17:43:38.146 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.146 T batch transaction: begin
2020-05-19 17:43:38.146 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:38.147 T BlockchainLMDB::update_txpool_tx
2020-05-19 17:43:38.147 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.147 T batch transaction: committing...
2020-05-19 17:43:38.153 T mdb_txn_safe: destructor
2020-05-19 17:43:38.153 T batch transaction: end
2020-05-19 17:43:38.154 D Queueing 1 transaction(s) for Dandelion++ fluffing
2020-05-19 17:43:38.154 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.155 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.155 D [183.82.83.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.156 I [183.82.83.167:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.156 I [183.82.83.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.156 T mdb_txn_safe: destructor
2020-05-19 17:43:38.156 D tx <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>already have transaction in tx_pool
2020-05-19 17:43:38.156 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.156 I [51.158.78.247:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.157 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.159 I Including transaction <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.160 I Including transaction <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>
2020-05-19 17:43:38.162 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.162 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.162 T mdb_txn_safe: destructor
2020-05-19 17:43:38.162 T Blockchain::have_tx
2020-05-19 17:43:38.163 T BlockchainLMDB::tx_exists
2020-05-19 17:43:38.163 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.196 I [217.209.85.167:18080 OUT] 8784 bytes sent for category command-2970651251 initiated by us
2020-05-19 17:43:38.196 T [217.209.85.167:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:38.196 T Moving counter buffer by 1 second 23543 < 23546 (last time 23543.7)
2020-05-19 17:43:38.197 T Moving counter buffer by 1 second 23544 < 23546 (last time 23544.7)
2020-05-19 17:43:38.197 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.7)
2020-05-19 17:43:38.197 T Throttle throttle_speed_out: packet of ~8817b  (from 8817 b) Speed AVG=   0[w=9.252]    0[w=9.252] /  Limit=16 KiB/sec  [8817 0 0 5271 0 0 0 0 0 0 ]
2020-05-19 17:43:38.198 D do_send_chunk() NOW just queues: packet=8817 B, is added to queue-size=2
2020-05-19 17:43:38.198 T [217.209.85.167:18080 OUT] [sock 37] Async send requested 5271
2020-05-19 17:43:38.199 D [217.209.85.167:18080 OUT] LEVIN_PACKET_SENT. [len=8784, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:38.199 T [217.209.85.167:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:38.199 T [217.209.85.167:18080 OUT] [sock 37] release
2020-05-19 17:43:38.221 I transaction with hash 28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac not found in db
2020-05-19 17:43:38.221 T mdb_txn_safe: destructor
2020-05-19 17:43:38.222 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:38.292 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.293 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.293 T mdb_txn_safe: destructor
2020-05-19 17:43:38.293 T Blockchain::have_tx
2020-05-19 17:43:38.294 T BlockchainLMDB::tx_exists
2020-05-19 17:43:38.294 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.294 I transaction with hash 28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac not found in db
2020-05-19 17:43:38.295 T mdb_txn_safe: destructor
2020-05-19 17:43:38.295 T BlockchainLMDB::height
2020-05-19 17:43:38.295 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.296 T mdb_txn_safe: destructor
2020-05-19 17:43:38.296 T BlockchainLMDB::get_block_already_generated_coins
2020-05-19 17:43:38.296 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.296 T mdb_txn_safe: destructor
2020-05-19 17:43:38.297 D Using 0.000000011197/byte fee
2020-05-19 17:43:38.297 T Blockchain::check_tx_outputs
2020-05-19 17:43:38.298 T Blockchain::check_tx_inputs
2020-05-19 17:43:38.298 T BlockchainLMDB::height
2020-05-19 17:43:38.298 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.298 T mdb_txn_safe: destructor
2020-05-19 17:43:38.299 T Blockchain::check_tx_inputs
2020-05-19 17:43:38.299 D Mixin: 10-10
2020-05-19 17:43:38.299 T Blockchain::have_tx_keyimg_as_spent
2020-05-19 17:43:38.300 T BlockchainLMDB::has_key_image
2020-05-19 17:43:38.300 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.336 T mdb_txn_safe: destructor
2020-05-19 17:43:38.336 T Blockchain::check_tx_input
2020-05-19 17:43:38.336 T Blockchain::scan_outputkeys_for_indexes
2020-05-19 17:43:38.337 T BlockchainLMDB::get_output_key
2020-05-19 17:43:38.337 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.500 T db3: 162
2020-05-19 17:43:38.500 T mdb_txn_safe: destructor
2020-05-19 17:43:38.500 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.500 T BlockchainLMDB::height
2020-05-19 17:43:38.501 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.501 T mdb_txn_safe: destructor
2020-05-19 17:43:38.501 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.502 T BlockchainLMDB::height
2020-05-19 17:43:38.502 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.502 T mdb_txn_safe: destructor
2020-05-19 17:43:38.502 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.503 T BlockchainLMDB::height
2020-05-19 17:43:38.503 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.503 T mdb_txn_safe: destructor
2020-05-19 17:43:38.504 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.504 T BlockchainLMDB::height
2020-05-19 17:43:38.504 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.505 T mdb_txn_safe: destructor
2020-05-19 17:43:38.505 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.505 T BlockchainLMDB::height
2020-05-19 17:43:38.506 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.506 T mdb_txn_safe: destructor
2020-05-19 17:43:38.506 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.506 T BlockchainLMDB::height
2020-05-19 17:43:38.507 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.507 T mdb_txn_safe: destructor
2020-05-19 17:43:38.507 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.508 T BlockchainLMDB::height
2020-05-19 17:43:38.508 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.508 T mdb_txn_safe: destructor
2020-05-19 17:43:38.508 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.509 T BlockchainLMDB::height
2020-05-19 17:43:38.509 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.509 T mdb_txn_safe: destructor
2020-05-19 17:43:38.510 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.510 T BlockchainLMDB::height
2020-05-19 17:43:38.510 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.511 T mdb_txn_safe: destructor
2020-05-19 17:43:38.511 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.511 T BlockchainLMDB::height
2020-05-19 17:43:38.511 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.512 T mdb_txn_safe: destructor
2020-05-19 17:43:38.512 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:38.512 T BlockchainLMDB::height
2020-05-19 17:43:38.512 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.513 T mdb_txn_safe: destructor
2020-05-19 17:43:38.513 T BlockchainLMDB::height
2020-05-19 17:43:38.513 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.514 T mdb_txn_safe: destructor
2020-05-19 17:43:38.556 T BlockchainLMDB::height
2020-05-19 17:43:38.557 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.557 T mdb_txn_safe: destructor
2020-05-19 17:43:38.557 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:38.557 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.558 T mdb_txn_safe: destructor
2020-05-19 17:43:38.558 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.558 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.559 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.559 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.559 D DB map size:     98557263872
2020-05-19 17:43:38.560 D Space used:      88234479616
2020-05-19 17:43:38.560 D Space remaining: 10322784256
2020-05-19 17:43:38.560 D Size threshold:  0
2020-05-19 17:43:38.560 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.561 T batch transaction: begin
2020-05-19 17:43:38.561 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:38.561 T BlockchainLMDB::remove_txpool_tx
2020-05-19 17:43:38.562 T BlockchainLMDB::add_txpool_tx
2020-05-19 17:43:38.562 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.562 T batch transaction: committing...
2020-05-19 17:43:38.570 T mdb_txn_safe: destructor
2020-05-19 17:43:38.570 T batch transaction: end
2020-05-19 17:43:38.570 I Transaction added to pool: txid <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac> weight: 1774 fee/byte: 11200.6
2020-05-19 17:43:38.571 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.571 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.571 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.572 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.572 D DB map size:     98557263872
2020-05-19 17:43:38.572 D Space used:      88234479616
2020-05-19 17:43:38.572 D Space remaining: 10322784256
2020-05-19 17:43:38.573 D Size threshold:  0
2020-05-19 17:43:38.573 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.573 T batch transaction: begin
2020-05-19 17:43:38.573 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.574 T batch transaction: committing...
2020-05-19 17:43:38.574 T mdb_txn_safe: destructor
2020-05-19 17:43:38.575 T batch transaction: end
2020-05-19 17:43:38.575 D tx added: <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.575 T Blockchain::prepare_handle_incoming_blocks
2020-05-19 17:43:38.575 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.575 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.576 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.576 T BlockchainLMDB::get_estimated_batch_size
2020-05-19 17:43:38.576 T BlockchainLMDB::height
2020-05-19 17:43:38.576 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.576 T mdb_txn_safe: destructor
2020-05-19 17:43:38.576 D [get_estimated_batch_size] m_height: 2101897  block_start: 2101397  block_stop: 2101896
2020-05-19 17:43:38.576 D estimated average block size for batch: 24857
2020-05-19 17:43:38.576 D calculated batch size: 559282496
2020-05-19 17:43:38.576 D increase size: 559282496
2020-05-19 17:43:38.577 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.577 D DB map size:     98557263872
2020-05-19 17:43:38.577 D Space used:      88234479616
2020-05-19 17:43:38.577 D Space remaining: 10322784256
2020-05-19 17:43:38.577 D Size threshold:  559282496
2020-05-19 17:43:38.577 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:38.577 T batch transaction: begin
2020-05-19 17:43:38.577 T BlockchainLMDB::height
2020-05-19 17:43:38.577 D block_batches: 0
2020-05-19 17:43:38.578 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:38.578 T BlockchainLMDB::height
2020-05-19 17:43:38.578 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:38.578 T Blockchain::have_block
2020-05-19 17:43:38.579 T BlockchainLMDB::block_exists
2020-05-19 17:43:38.579 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:38.579 D Skipping remainder of prepare blocks. Blocks exist.
2020-05-19 17:43:38.579 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:38.579 T Blockchain::add_new_block
2020-05-19 17:43:38.579 T Blockchain::have_block
2020-05-19 17:43:38.579 T BlockchainLMDB::block_exists
2020-05-19 17:43:38.579 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:38.579 T block with id = <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> already exists
2020-05-19 17:43:38.579 T Blockchain::cleanup_handle_incoming_blocks
2020-05-19 17:43:38.580 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.580 T batch transaction: committing...
2020-05-19 17:43:38.580 T mdb_txn_safe: destructor
2020-05-19 17:43:38.580 T batch transaction: end
2020-05-19 17:43:38.580 T BlockchainLMDB::prune_worker
2020-05-19 17:43:38.580 T mdb_txn_safe: abort()
2020-05-19 17:43:38.580 D Pruning not enabled, nothing to do
2020-05-19 17:43:38.580 T mdb_txn_safe: destructor
2020-05-19 17:43:38.580 T Blockchain::prepare_handle_incoming_blocks
2020-05-19 17:43:38.581 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.581 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.581 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.581 T BlockchainLMDB::get_estimated_batch_size
2020-05-19 17:43:38.581 T BlockchainLMDB::height
2020-05-19 17:43:38.581 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.581 T mdb_txn_safe: destructor
2020-05-19 17:43:38.581 D [get_estimated_batch_size] m_height: 2101897  block_start: 2101397  block_stop: 2101896
2020-05-19 17:43:38.581 D estimated average block size for batch: 24857
2020-05-19 17:43:38.581 D calculated batch size: 559282496
2020-05-19 17:43:38.582 D increase size: 559282496
2020-05-19 17:43:38.582 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.582 D DB map size:     98557263872
2020-05-19 17:43:38.582 D Space used:      88234479616
2020-05-19 17:43:38.582 D Space remaining: 10322784256
2020-05-19 17:43:38.582 D Size threshold:  559282496
2020-05-19 17:43:38.582 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:38.582 T batch transaction: begin
2020-05-19 17:43:38.582 T BlockchainLMDB::height
2020-05-19 17:43:38.583 D block_batches: 0
2020-05-19 17:43:38.583 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:38.583 T BlockchainLMDB::height
2020-05-19 17:43:38.583 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:38.583 T Blockchain::have_block
2020-05-19 17:43:38.584 T BlockchainLMDB::block_exists
2020-05-19 17:43:38.584 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:38.584 D Skipping remainder of prepare blocks. Blocks exist.
2020-05-19 17:43:38.584 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:38.584 T Blockchain::add_new_block
2020-05-19 17:43:38.584 T Blockchain::have_block
2020-05-19 17:43:38.584 T BlockchainLMDB::block_exists
2020-05-19 17:43:38.584 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:38.585 T block with id = <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> already exists
2020-05-19 17:43:38.585 T Blockchain::cleanup_handle_incoming_blocks
2020-05-19 17:43:38.585 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.585 T batch transaction: committing...
2020-05-19 17:43:38.585 T mdb_txn_safe: destructor
2020-05-19 17:43:38.585 T batch transaction: end
2020-05-19 17:43:38.585 T BlockchainLMDB::prune_worker
2020-05-19 17:43:38.585 T mdb_txn_safe: abort()
2020-05-19 17:43:38.585 D Pruning not enabled, nothing to do
2020-05-19 17:43:38.585 T mdb_txn_safe: destructor
2020-05-19 17:43:38.586 D miner::resume: 2 -> 1
2020-05-19 17:43:38.586 T BlockchainLMDB::batch_start
2020-05-19 17:43:38.586 T Setting 00:05:00 expiry
2020-05-19 17:43:38.586 T [195.201.12.110:18080 OUT] [sock 38] Async send calledback 12261
2020-05-19 17:43:38.586 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.8)
2020-05-19 17:43:38.587 T dbg >>> global-OUT: speed is A= 4556.73 vs Max=2.09715e+06  so sleep: D=-9.61988 sec E=   43936 (Enow=   56197) M=2.09715e+06 W=   9.642 R=2.01768e+07 Wgood      11 History: [0 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.6
2020-05-19 17:43:38.587 T Throttle >>> global-OUT: packet of ~12261b  (from 12261 b) Speed AVG=   4[w=9.642]    4[w=9.642] /  Limit=2048 KiB/sec  [12261 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23530 < 23546 (last time 23530.1)
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23531 < 23546 (last time 23531.1)
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23532 < 23546 (last time 23532.1)
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23533 < 23546 (last time 23533.1)
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23534 < 23546 (last time 23534.1)
2020-05-19 17:43:38.587 T Moving counter buffer by 1 second 23535 < 23546 (last time 23535.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23536 < 23546 (last time 23536.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23537 < 23546 (last time 23537.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23538 < 23546 (last time 23538.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23539 < 23546 (last time 23539.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23540 < 23546 (last time 23540.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23541 < 23546 (last time 23541.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23542 < 23546 (last time 23542.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23543 < 23546 (last time 23543.1)
2020-05-19 17:43:38.588 T Moving counter buffer by 1 second 23544 < 23546 (last time 23544.1)
2020-05-19 17:43:38.589 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.1)
2020-05-19 17:43:38.589 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=   0[w=9.643]    0[w=9.643] /  Limit=16 KiB/sec  [8192 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.589 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.7)
2020-05-19 17:43:38.589 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=   3[w=9.645]    3[w=9.645] /  Limit=8192 KiB/sec  [8192 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.589 T dbg <<< global-IN: speed is A= 4452.77 vs Max=8.38861e+06  so sleep: D=-9.63969 sec E=   42947 (Enow=   51139) M=8.38861e+06 W=   9.645 R=8.08652e+07 Wgood      11 History: [8192 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.6
2020-05-19 17:43:38.589 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.590 I [195.201.12.110:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.590 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.593 I Including transaction <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>
2020-05-19 17:43:38.593 D miner::resume: 1 -> 0
2020-05-19 17:43:38.593 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:38.594 T Setting 00:04:57.973000 expiry
2020-05-19 17:43:38.594 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:38.594 T [217.209.85.167:18080 OUT] [sock 37] Async send calledback 5271
2020-05-19 17:43:38.594 T BlockchainLMDB::need_resize
2020-05-19 17:43:38.595 T dbg >>> global-OUT: speed is A= 5823.52 vs Max=2.09715e+06  so sleep: D= -9.6227 sec E=   56197 (Enow=   61468) M=2.09715e+06 W=    9.65 R=2.01813e+07 Wgood      11 History: [12261 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.595 D DB map size:     98557263872
2020-05-19 17:43:38.595 T Throttle >>> global-OUT: packet of ~5271b  (from 5271 b) Speed AVG=   5[w=9.651]    5[w=9.651] /  Limit=2048 KiB/sec  [17532 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.595 D Space used:      88234479616
2020-05-19 17:43:38.596 T Setting 00:05:00 expiry
2020-05-19 17:43:38.596 D handle_write() NOW SENDS: packet=8817 B, from  queue size=1
2020-05-19 17:43:38.596 T handler_write (after write, from queue=1) - before ASIO write, for packet=8817 B (after sleep)
2020-05-19 17:43:38.596 D Space remaining: 10322784256
2020-05-19 17:43:38.597 T Moving counter buffer by 1 second 23530 < 23546 (last time 23530)
2020-05-19 17:43:38.597 D Size threshold:  0
2020-05-19 17:43:38.597 T Moving counter buffer by 1 second 23531 < 23546 (last time 23531)
2020-05-19 17:43:38.597 T Moving counter buffer by 1 second 23532 < 23546 (last time 23532)
2020-05-19 17:43:38.597 T Moving counter buffer by 1 second 23533 < 23546 (last time 23533)
2020-05-19 17:43:38.597 T Moving counter buffer by 1 second 23534 < 23546 (last time 23534)
2020-05-19 17:43:38.598 T Moving counter buffer by 1 second 23535 < 23546 (last time 23535)
2020-05-19 17:43:38.598 T Moving counter buffer by 1 second 23536 < 23546 (last time 23536)
2020-05-19 17:43:38.598 D Percent used: 89.5261  Percent threshold: 89.9999
2020-05-19 17:43:38.598 T Moving counter buffer by 1 second 23537 < 23546 (last time 23537)
2020-05-19 17:43:38.598 T batch transaction: begin
2020-05-19 17:43:38.598 T Moving counter buffer by 1 second 23538 < 23546 (last time 23538)
2020-05-19 17:43:38.599 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:38.599 T Moving counter buffer by 1 second 23539 < 23546 (last time 23539)
2020-05-19 17:43:38.599 T Moving counter buffer by 1 second 23540 < 23546 (last time 23540)
2020-05-19 17:43:38.599 T Moving counter buffer by 1 second 23541 < 23546 (last time 23541)
2020-05-19 17:43:38.599 T Moving counter buffer by 1 second 23542 < 23546 (last time 23542)
2020-05-19 17:43:38.599 T BlockchainLMDB::update_txpool_tx
2020-05-19 17:43:38.600 T Moving counter buffer by 1 second 23543 < 23546 (last time 23543)
2020-05-19 17:43:38.600 T Moving counter buffer by 1 second 23544 < 23546 (last time 23544)
2020-05-19 17:43:38.600 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545)
2020-05-19 17:43:38.600 T Throttle throttle_speed_in: packet of ~8192b  (from 8192 b) Speed AVG=   0[w=9.65199]    0[w=9.65199] /  Limit=16 KiB/sec  [8192 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.600 T Throttle <<< global-IN: packet of ~8192b  (from 8192 b) Speed AVG=   4[w=9.65599]    4[w=9.65599] /  Limit=8192 KiB/sec  [16384 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.600 T BlockchainLMDB::batch_stop
2020-05-19 17:43:38.601 T dbg <<< global-IN: speed is A= 5296.08 vs Max=8.3886e+06  so sleep: D= -9.6497 sec E=   51139 (Enow=   59331) M=8.3886e+06 W= 9.65599 R=8.09492e+07 Wgood      11 History: [16384 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.6
2020-05-19 17:43:38.601 T batch transaction: committing...
2020-05-19 17:43:38.601 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.601 I [217.209.85.167:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.602 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.605 I Including transaction <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>
2020-05-19 17:43:38.607 T mdb_txn_safe: destructor
2020-05-19 17:43:38.607 T batch transaction: end
2020-05-19 17:43:38.608 D Queueing 1 transaction(s) for Dandelion++ fluffing
2020-05-19 17:43:38.608 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.608 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.608 T mdb_txn_safe: destructor
2020-05-19 17:43:38.609 D tx <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>already have transaction in tx_pool
2020-05-19 17:43:38.609 T Setting 00:04:48.809000 expiry
2020-05-19 17:43:38.612 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.612 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.612 T mdb_txn_safe: destructor
2020-05-19 17:43:38.612 D tx <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>already have transaction in tx_pool
2020-05-19 17:43:38.613 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.613 I [5.79.64.237:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.613 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.613 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.614 I [51.158.78.247:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.615 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.616 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.616 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.616 I Including transaction <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>
2020-05-19 17:43:38.616 T mdb_txn_safe: destructor
2020-05-19 17:43:38.617 D tx <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>already have transaction in tx_pool
2020-05-19 17:43:38.620 I Including transaction <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>
2020-05-19 17:43:38.621 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.621 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.621 T mdb_txn_safe: destructor
2020-05-19 17:43:38.621 D tx <e0ce526df456ce093df30853f0927325d103806bc1dc0d7ee4cab8a2fbb241b8>already have transaction in tx_pool
2020-05-19 17:43:38.622 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.622 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.622 I [217.209.85.167:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.622 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.625 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.625 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.625 T mdb_txn_safe: destructor
2020-05-19 17:43:38.625 D tx <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>already have transaction in tx_pool
2020-05-19 17:43:38.625 I Including transaction <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>
2020-05-19 17:43:38.626 I [195.201.12.110:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.626 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.629 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.629 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.629 T mdb_txn_safe: destructor
2020-05-19 17:43:38.629 I Including transaction <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>
2020-05-19 17:43:38.629 D tx <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>already have transaction in tx_pool
2020-05-19 17:43:38.630 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.630 I [5.79.64.237:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.630 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.633 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.633 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.633 I Including transaction <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>
2020-05-19 17:43:38.633 T mdb_txn_safe: destructor
2020-05-19 17:43:38.633 T Setting 00:05:00 expiry
2020-05-19 17:43:38.633 D tx <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>already have transaction in tx_pool
2020-05-19 17:43:38.634 T [51.158.78.247:18080 OUT] [sock 32] Async send calledback 9652
2020-05-19 17:43:38.634 T dbg >>> global-OUT: speed is A=  6344.1 vs Max=2.09715e+06  so sleep: D=-9.65877 sec E=   61468 (Enow=   71120) M=2.09715e+06 W=   9.689 R=2.02578e+07 Wgood      11 History: [17532 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.634 T Throttle >>> global-OUT: packet of ~9652b  (from 9652 b) Speed AVG=   6[w=9.69]    6[w=9.69] /  Limit=2048 KiB/sec  [27184 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.634 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.6)
2020-05-19 17:43:38.635 T Throttle throttle_speed_in: packet of ~7937b  (from 7937 b) Speed AVG=   0[w=9.69]    0[w=9.69] /  Limit=16 KiB/sec  [7937 8192 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.635 T Throttle <<< global-IN: packet of ~7937b  (from 7937 b) Speed AVG=   5[w=9.69]    5[w=9.69] /  Limit=8192 KiB/sec  [24321 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.635 T dbg <<< global-IN: speed is A= 6095.97 vs Max=8.38861e+06  so sleep: D=-9.68377 sec E=   59076 (Enow=   67013) M=8.38861e+06 W=   9.691 R=8.12349e+07 Wgood      11 History: [24321 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.635 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.635 I [51.158.78.247:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.636 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.637 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.637 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.637 T mdb_txn_safe: destructor
2020-05-19 17:43:38.637 D tx <8822f98c6d881b38b315ecc8522b14aed21fa274f96e200d4b1bf8556bd98fb7>already have transaction in tx_pool
2020-05-19 17:43:38.638 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.638 I [195.201.12.110:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.638 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.640 I Including transaction <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>
2020-05-19 17:43:38.641 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.641 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.641 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.641 I [217.209.85.167:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.641 I Including transaction <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>
2020-05-19 17:43:38.642 T mdb_txn_safe: destructor
2020-05-19 17:43:38.642 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.642 D tx <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>already have transaction in tx_pool
2020-05-19 17:43:38.642 T Setting 00:04:59.816000 expiry
2020-05-19 17:43:38.642 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.7)
2020-05-19 17:43:38.642 T Throttle throttle_speed_in: packet of ~7937b  (from 7937 b) Speed AVG=   0[w=9.698]    0[w=9.698] /  Limit=16 KiB/sec  [7937 8192 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.643 T Throttle <<< global-IN: packet of ~7937b  (from 7937 b) Speed AVG=   5[w=9.698]    5[w=9.698] /  Limit=8192 KiB/sec  [32258 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.643 T dbg <<< global-IN: speed is A= 6909.27 vs Max=8.38861e+06  so sleep: D=-9.69082 sec E=   67013 (Enow=   74950) M=8.38861e+06 W=   9.699 R=8.12941e+07 Wgood      11 History: [32258 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.643 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.643 I [5.79.64.237:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.644 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.645 I Including transaction <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>
2020-05-19 17:43:38.647 I Including transaction <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>
2020-05-19 17:43:38.648 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.649 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.649 T mdb_txn_safe: destructor
2020-05-19 17:43:38.650 D tx <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>already have transaction in tx_pool
2020-05-19 17:43:38.651 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2627, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.652 I [51.158.78.247:18080 OUT] 2627 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.653 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.654 I [62.121.116.122:18080 OUT] 3570 bytes sent for category command-2970126963 initiated by us
2020-05-19 17:43:38.654 T [62.121.116.122:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:38.654 T Moving counter buffer by 1 second 23545 < 23546 (last time 23545.8)
2020-05-19 17:43:38.654 T Throttle throttle_speed_out: packet of ~3603b  (from 3603 b) Speed AVG=   1[w=9.71]    1[w=9.71] /  Limit=16 KiB/sec  [3603 9652 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.655 D do_send_chunk() NOW SENSD: packet=3603 B
2020-05-19 17:43:38.655 T handler_write (direct) - before ASIO write, for packet=3603 B (after sleep)
2020-05-19 17:43:38.655 T Setting 00:05:00 expiry
2020-05-19 17:43:38.655 D [62.121.116.122:18080 OUT] LEVIN_PACKET_SENT. [len=3570, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:38.655 T [62.121.116.122:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:38.655 T [62.121.116.122:18080 OUT] [sock 34] release
2020-05-19 17:43:38.656 T [62.121.116.122:18080 OUT] [sock 34] Async send calledback 3603
2020-05-19 17:43:38.657 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.657 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.657 T mdb_txn_safe: destructor
2020-05-19 17:43:38.657 D tx <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>already have transaction in tx_pool
2020-05-19 17:43:38.657 T dbg >>> global-OUT: speed is A=  7322.9 vs Max=2.09715e+06  so sleep: D=-9.67774 sec E=   71120 (Enow=   74723) M=2.09715e+06 W=   9.712 R=2.02964e+07 Wgood      11 History: [27184 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.658 I Including transaction <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>
2020-05-19 17:43:38.659 T Throttle >>> global-OUT: packet of ~3603b  (from 3603 b) Speed AVG=   7[w=9.714]    7[w=9.714] /  Limit=2048 KiB/sec  [30787 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.660 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.660 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.661 T mdb_txn_safe: destructor
2020-05-19 17:43:38.661 D tx <8baaf3fdd7fcb88593e8d3611b21d9001a47bbeb98ae8e8deadd7cd837ab8458>already have transaction in tx_pool
2020-05-19 17:43:38.661 T Setting 00:05:00 expiry
2020-05-19 17:43:38.661 T [217.209.85.167:18080 OUT] [sock 37] Async send calledback 8817
2020-05-19 17:43:38.661 T dbg >>> global-OUT: speed is A= 7689.92 vs Max=2.09715e+06  so sleep: D=-9.68053 sec E=   74723 (Enow=   83540) M=2.09715e+06 W=   9.717 R=2.03033e+07 Wgood      11 History: [30787 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.662 T Throttle >>> global-OUT: packet of ~8817b  (from 8817 b) Speed AVG=   7[w=9.717]    7[w=9.717] /  Limit=2048 KiB/sec  [39604 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:38.662 T Throttle throttle_speed_in: packet of ~8160b  (from 8160 b) Speed AVG=   0[w=9.717]    0[w=9.717] /  Limit=16 KiB/sec  [16352 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.662 T Throttle <<< global-IN: packet of ~8160b  (from 8160 b) Speed AVG=   6[w=9.718]    6[w=9.718] /  Limit=8192 KiB/sec  [40418 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.662 T dbg <<< global-IN: speed is A= 7735.44 vs Max=8.38861e+06  so sleep: D=-9.70884 sec E=   75173 (Enow=   83333) M=8.38861e+06 W=   9.718 R=8.14453e+07 Wgood      11 History: [40418 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.662 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.663 I [217.209.85.167:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.663 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.664 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.664 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.664 T mdb_txn_safe: destructor
2020-05-19 17:43:38.665 D tx <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>already have transaction in tx_pool
2020-05-19 17:43:38.665 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2627, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.665 I [5.79.64.237:18080 OUT] 2627 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.665 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.666 I Including transaction <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>
2020-05-19 17:43:38.668 I Including transaction <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>
2020-05-19 17:43:38.669 T Setting 00:05:00 expiry
2020-05-19 17:43:38.670 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.670 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.670 T mdb_txn_safe: destructor
2020-05-19 17:43:38.670 D tx <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>already have transaction in tx_pool
2020-05-19 17:43:38.670 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2627, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.671 I [217.209.85.167:18080 OUT] 2627 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.671 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.671 T Throttle throttle_speed_in: packet of ~7937b  (from 7937 b) Speed AVG=   0[w=9.727]    0[w=9.727] /  Limit=16 KiB/sec  [16129 0 0 0 0 0 0 0 0 0 ]
2020-05-19 17:43:38.672 T Throttle <<< global-IN: packet of ~7937b  (from 7937 b) Speed AVG=   7[w=9.728]    7[w=9.728] /  Limit=8192 KiB/sec  [48355 16861 8369 0 476 8624 425 0 0 0 ]
2020-05-19 17:43:38.673 T dbg <<< global-IN: speed is A=  8542.5 vs Max=8.38861e+06  so sleep: D= -9.7189 sec E=   83110 (Enow=   91047) M=8.38861e+06 W=   9.729 R=8.15297e+07 Wgood      11 History: [48355 16861 8369 0 476 8624 425 0 0 0 ] m_last_sample_time= 23546.7
2020-05-19 17:43:38.674 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.674 I Including transaction <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>
2020-05-19 17:43:38.675 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2629, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.676 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.676 T mdb_txn_safe: destructor
2020-05-19 17:43:38.676 D tx <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>already have transaction in tx_pool
2020-05-19 17:43:38.676 I [195.201.12.110:18080 OUT] 2629 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.677 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.678 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.678 I [5.79.64.237:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.678 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.680 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.680 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.680 T mdb_txn_safe: destructor
2020-05-19 17:43:38.680 D tx <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>already have transaction in tx_pool
2020-05-19 17:43:38.680 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.681 I [51.158.78.247:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.681 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.681 I Including transaction <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:38.683 I Including transaction <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>
2020-05-19 17:43:38.684 I Including transaction <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:38.685 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.685 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.685 T mdb_txn_safe: destructor
2020-05-19 17:43:38.685 D tx <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>already have transaction in tx_pool
2020-05-19 17:43:38.685 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.685 I [5.79.64.237:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.685 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.689 I Including transaction <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.690 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.690 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.690 T mdb_txn_safe: destructor
2020-05-19 17:43:38.691 D tx <0120f06cd1fedf575c61d30a2dabb73282bf296e818e63c987f97cdd3e0b9099>already have transaction in tx_pool
2020-05-19 17:43:38.694 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=2627, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.694 I [195.201.12.110:18080 OUT] 2627 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.695 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.696 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.696 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.697 T mdb_txn_safe: destructor
2020-05-19 17:43:38.698 D tx <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>already have transaction in tx_pool
2020-05-19 17:43:38.699 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.700 I [217.209.85.167:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.702 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.702 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.702 T mdb_txn_safe: destructor
2020-05-19 17:43:38.702 D tx <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>already have transaction in tx_pool
2020-05-19 17:43:38.703 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.703 I [51.158.78.247:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.703 I Including transaction <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>
2020-05-19 17:43:38.704 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.705 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.706 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.706 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.706 T mdb_txn_safe: destructor
2020-05-19 17:43:38.706 D tx <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>already have transaction in tx_pool
2020-05-19 17:43:38.706 T Setting 00:05:00 expiry
2020-05-19 17:43:38.708 I Including transaction <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.709 I Including transaction <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:38.710 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.711 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.711 T mdb_txn_safe: destructor
2020-05-19 17:43:38.712 D tx <eb4c2cf3ead5e04393453e02f7840b8e49f58661de4c0be3ca55607a9df79e19>already have transaction in tx_pool
2020-05-19 17:43:38.712 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1794, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.713 I [195.201.12.110:18080 OUT] 1794 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.713 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.716 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.716 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.716 T mdb_txn_safe: destructor
2020-05-19 17:43:38.716 D tx <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>already have transaction in tx_pool
2020-05-19 17:43:38.716 T Setting 00:05:00 expiry
2020-05-19 17:43:38.718 I Including transaction <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>
2020-05-19 17:43:38.719 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.720 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.720 T mdb_txn_safe: destructor
2020-05-19 17:43:38.720 D tx <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>already have transaction in tx_pool
2020-05-19 17:43:38.720 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.720 I [217.209.85.167:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.720 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.724 I Including transaction <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.724 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.725 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.725 T mdb_txn_safe: destructor
2020-05-19 17:43:38.725 D tx <35f14dcbb3ec4c1378c292674059f49f21a48cecf804bcb4b6150bb629bae040>already have transaction in tx_pool
2020-05-19 17:43:38.726 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:38.726 I [195.201.12.110:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:38.727 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:38.729 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.729 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.729 T mdb_txn_safe: destructor
2020-05-19 17:43:38.729 D tx <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>already have transaction in tx_pool
2020-05-19 17:43:38.729 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=190, flags1, r?=1, cmd = 1002, v=1
2020-05-19 17:43:38.730 I [217.209.85.167:18080 OUT] 190 bytes received for category command-1002 initiated by peer
2020-05-19 17:43:38.730 T Blockchain::have_block
2020-05-19 17:43:38.730 T BlockchainLMDB::block_exists
2020-05-19 17:43:38.730 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.730 T mdb_txn_safe: destructor
2020-05-19 17:43:38.730 D block <117ec58883edac4e1a14fbef2da73ba4ca9c4962e5c65504923c99d9ab8715ba> found in main chain
2020-05-19 17:43:38.732 I Including transaction <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>
2020-05-19 17:43:38.736 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:38.737 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.738 T mdb_txn_safe: destructor
2020-05-19 17:43:38.739 D tx <28b56298a9d74d7572d2d36710a0013f14a5fdcb19e90cdaeb7a56827e3d5cac>already have transaction in tx_pool
2020-05-19 17:43:38.740 T Setting 00:05:00 expiry
2020-05-19 17:43:38.746 T Blockchain::get_tail_id
2020-05-19 17:43:38.747 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:38.747 T BlockchainLMDB::height
2020-05-19 17:43:38.747 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.747 T mdb_txn_safe: destructor
2020-05-19 17:43:38.747 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:38.747 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.747 T mdb_txn_safe: destructor
2020-05-19 17:43:38.747 T BlockchainLMDB::get_block_cumulative_difficulty  height: 2101896
2020-05-19 17:43:38.747 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.748 T mdb_txn_safe: destructor
2020-05-19 17:43:38.748 T BlockchainLMDB::get_blockchain_pruning_seed
2020-05-19 17:43:38.748 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:38.748 T mdb_txn_safe: destructor
2020-05-19 17:43:38.748 D [217.209.85.167:18080 OUT] COMMAND_TIMED_SYNC
2020-05-19 17:43:38.750 I [217.209.85.167:18080 OUT] 10692 bytes sent for category command-1002 initiated by peer
2020-05-19 17:43:38.751 T Throttle throttle_speed_out: packet of ~10725b  (from 10725 b) Speed AVG=   1[w=9.807]    1[w=9.807] /  Limit=16 KiB/sec  [19542 0 0 5271 0 0 0 0 0 0 ]
2020-05-19 17:43:38.752 D do_send_chunk() NOW SENSD: packet=10725 B
2020-05-19 17:43:38.752 T handler_write (direct) - before ASIO write, for packet=10725 B (after sleep)
2020-05-19 17:43:38.752 T Setting 00:05:00 expiry
2020-05-19 17:43:38.752 D [217.209.85.167:18080 OUT] LEVIN_PACKET_SENT. [len=10692, flags2, r?=0, cmd = 1002, ver=1
2020-05-19 17:43:38.752 T Setting 00:05:00 expiry
2020-05-19 17:43:38.753 T [217.209.85.167:18080 OUT] [sock 37] Async send calledback 10725
2020-05-19 17:43:38.753 T dbg >>> global-OUT: speed is A= 8517.54 vs Max=2.09715e+06  so sleep: D=-9.76714 sec E=   83540 (Enow=   94265) M=2.09715e+06 W=   9.808 R=2.04853e+07 Wgood      11 History: [39604 41274 0 2662 0 0 0 0 0 0 ] m_last_sample_time= 23546.8
2020-05-19 17:43:38.753 T Throttle >>> global-OUT: packet of ~10725b  (from 10725 b) Speed AVG=   8[w=9.809]    8[w=9.809] /  Limit=2048 KiB/sec  [50329 41274 0 2662 0 0 0 0 0 0 ]
2020-05-19 17:43:39.740 I [5.79.64.237:18080 OUT] 8786 bytes sent for category command-2970651251 initiated by us
2020-05-19 17:43:39.741 T [5.79.64.237:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:39.741 T Moving counter buffer by 1 second 23544 < 23547 (last time 23544.4)
2020-05-19 17:43:39.741 T Moving counter buffer by 1 second 23545 < 23547 (last time 23545.4)
2020-05-19 17:43:39.741 T Moving counter buffer by 1 second 23546 < 23547 (last time 23546.4)
2020-05-19 17:43:39.741 T Throttle throttle_speed_out: packet of ~8819b  (from 8819 b) Speed AVG=   0[w=9.796]    0[w=9.796] /  Limit=16 KiB/sec  [8819 0 0 7045 0 0 0 0 0 0 ]
2020-05-19 17:43:39.741 D do_send_chunk() NOW SENSD: packet=8819 B
2020-05-19 17:43:39.741 T handler_write (direct) - before ASIO write, for packet=8819 B (after sleep)
2020-05-19 17:43:39.742 T Setting 00:05:00 expiry
2020-05-19 17:43:39.742 D [5.79.64.237:18080 OUT] LEVIN_PACKET_SENT. [len=8786, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:39.742 T [5.79.64.237:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:39.742 T [5.79.64.237:18080 OUT] [sock 35] release
2020-05-19 17:43:39.742 T [5.79.64.237:18080 OUT] [sock 35] Async send calledback 8819
2020-05-19 17:43:39.743 T Moving counter buffer by 1 second 23546 < 23547 (last time 23546.8)
2020-05-19 17:43:39.743 T dbg >>> global-OUT: speed is A= 9620.84 vs Max=2.09715e+06  so sleep: D=-9.75221 sec E=   94265 (Enow=  103084) M=2.09715e+06 W=   9.798 R=2.04536e+07 Wgood      11 History: [0 50329 41274 0 2662 0 0 0 0 0 ] m_last_sample_time= 23547.8
2020-05-19 17:43:39.743 T Throttle >>> global-OUT: packet of ~8819b  (from 8819 b) Speed AVG=   9[w=9.799]    9[w=9.799] /  Limit=2048 KiB/sec  [8819 50329 41274 0 2662 0 0 0 0 0 ]
2020-05-19 17:43:39.764 I client <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> credited for 5, now 10
2020-05-19 17:43:39.764 T Blockchain::get_difficulty_for_next_block
2020-05-19 17:43:39.764 T Blockchain::get_tail_id
2020-05-19 17:43:39.764 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:39.764 T BlockchainLMDB::height
2020-05-19 17:43:39.764 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.764 T mdb_txn_safe: destructor
2020-05-19 17:43:39.764 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:39.765 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.765 T mdb_txn_safe: destructor
2020-05-19 17:43:39.765 T Blockchain::get_tail_id
2020-05-19 17:43:39.765 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:39.765 T BlockchainLMDB::height
2020-05-19 17:43:39.765 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.765 T mdb_txn_safe: destructor
2020-05-19 17:43:39.765 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:39.765 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.765 T mdb_txn_safe: destructor
2020-05-19 17:43:39.766 D /json_rpc[rpc_access_submit_nonce] processed with 1/2529/0ms
2020-05-19 17:43:39.766 T HTTP_RESPONSE_HEAD: <<
2020-05-19 17:43:39.766 T HTTP/1.1 200 Ok
2020-05-19 17:43:39.766 T Server: Epee-based
2020-05-19 17:43:39.766 T Content-Length: 209
2020-05-19 17:43:39.766 T Content-Type: application/json
2020-05-19 17:43:39.766 T Last-Modified: Tue, 19 May 2020 17:43:39 GMT
2020-05-19 17:43:39.766 T Accept-Ranges: bytes
2020-05-19 17:43:39.766 T
2020-05-19 17:43:39.767 T Moving counter buffer by 1 second 23544 < 23547 (last time 23544.9)
2020-05-19 17:43:39.767 T Moving counter buffer by 1 second 23545 < 23547 (last time 23545.9)
2020-05-19 17:43:39.767 T Moving counter buffer by 1 second 23546 < 23547 (last time 23546.9)
2020-05-19 17:43:39.767 T Throttle throttle_speed_out: packet of ~369b  (from 369 b) Speed AVG=   0[w=9.82199]    0[w=9.82199] /  Limit=16 KiB/sec  [369 0 0 1213 0 0 781 270 0 0 ]
2020-05-19 17:43:39.767 D do_send_chunk() NOW SENSD: packet=369 B
2020-05-19 17:43:39.767 T Setting 00:30:00 expiry
2020-05-19 17:43:39.768 T Setting 00:30:00 expiry
2020-05-19 17:43:39.768 T [192.168.1.131:54281 INC] [sock 39] Async send calledback 369
2020-05-19 17:43:39.787 T Moving counter buffer by 1 second 23545 < 23547 (last time 23545.2)
2020-05-19 17:43:39.787 T Moving counter buffer by 1 second 23546 < 23547 (last time 23546.2)
2020-05-19 17:43:39.788 T Throttle throttle_speed_in: packet of ~115b  (from 115 b) Speed AVG=   0[w=9.84299]    0[w=9.84299] /  Limit=16 KiB/sec  [115 0 477 432 0 476 432 425 0 0 ]
2020-05-19 17:43:39.788 T Moving counter buffer by 1 second 23546 < 23547 (last time 23546.7)
2020-05-19 17:43:39.788 T Throttle <<< global-IN: packet of ~115b  (from 115 b) Speed AVG=   8[w=9.84299]    8[w=9.84299] /  Limit=8192 KiB/sec  [115 48355 16861 8369 0 476 8624 425 0 0 ]
2020-05-19 17:43:39.788 T HTTP HEAD:
2020-05-19 17:43:39.788 T Host: 192.168.1.116
2020-05-19 17:43:39.789 T Content-Length: 310
2020-05-19 17:43:39.789 T Content-Type: application/json; charset=utf-8
2020-05-19 17:43:39.789 T
2020-05-19 17:43:39.789 T Setting 00:30:00 expiry
2020-05-19 17:43:39.789 T Throttle throttle_speed_in: packet of ~310b  (from 310 b) Speed AVG=   0[w=9.84499]    0[w=9.84499] /  Limit=16 KiB/sec  [425 0 477 432 0 476 432 425 0 0 ]
2020-05-19 17:43:39.790 T Throttle <<< global-IN: packet of ~310b  (from 310 b) Speed AVG=   8[w=9.84499]    8[w=9.84499] /  Limit=8192 KiB/sec  [425 48355 16861 8369 0 476 8624 425 0 0 ]
2020-05-19 17:43:39.790 I HTTP [192.168.1.131] GET /json_rpc
2020-05-19 17:43:39.790 I [192.168.1.131:54281 INC] Calling RPC method get_info
2020-05-19 17:43:39.790 T Blockchain::get_tail_id
2020-05-19 17:43:39.791 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:39.791 T BlockchainLMDB::height
2020-05-19 17:43:39.791 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.791 T mdb_txn_safe: destructor
2020-05-19 17:43:39.791 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:39.791 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.791 T mdb_txn_safe: destructor
2020-05-19 17:43:39.793 D client <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> paying 1 for get_info, 9 left
2020-05-19 17:43:39.797 T Blockchain::get_tail_id
2020-05-19 17:43:39.797 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:39.798 T BlockchainLMDB::height
2020-05-19 17:43:39.798 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.798 T mdb_txn_safe: destructor
2020-05-19 17:43:39.798 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:39.799 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.799 T mdb_txn_safe: destructor
2020-05-19 17:43:39.799 T Blockchain::get_difficulty_for_next_block
2020-05-19 17:43:39.799 T Blockchain::get_tail_id
2020-05-19 17:43:39.799 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:39.799 T BlockchainLMDB::height
2020-05-19 17:43:39.799 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.800 T mdb_txn_safe: destructor
2020-05-19 17:43:39.800 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:39.800 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.800 T mdb_txn_safe: destructor
2020-05-19 17:43:39.800 T Blockchain::get_total_transactions
2020-05-19 17:43:39.800 T BlockchainLMDB::get_tx_count
2020-05-19 17:43:39.801 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.801 T mdb_txn_safe: destructor
2020-05-19 17:43:39.801 T BlockchainLMDB::get_txpool_tx_count
2020-05-19 17:43:39.801 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.801 T mdb_txn_safe: destructor
2020-05-19 17:43:39.801 T BlockchainLMDB::get_block_cumulative_difficulty  height: 2101896
2020-05-19 17:43:39.802 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:39.802 T mdb_txn_safe: destructor
2020-05-19 17:43:39.802 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:39.802 T Blockchain::get_current_cumulative_block_weight_median
2020-05-19 17:43:39.814 D /json_rpc[get_info] processed with 0/23/1ms
2020-05-19 17:43:39.815 T HTTP_RESPONSE_HEAD: <<
2020-05-19 17:43:39.815 T HTTP/1.1 200 Ok
2020-05-19 17:43:39.815 T Server: Epee-based
2020-05-19 17:43:39.815 T Content-Length: 1386
2020-05-19 17:43:39.815 T Content-Type: application/json
2020-05-19 17:43:39.815 T Last-Modified: Tue, 19 May 2020 17:43:39 GMT
2020-05-19 17:43:39.815 T Accept-Ranges: bytes
2020-05-19 17:43:39.816 T
2020-05-19 17:43:39.816 T Throttle throttle_speed_out: packet of ~1547b  (from 1547 b) Speed AVG=   0[w=9.87099]    0[w=9.87099] /  Limit=16 KiB/sec  [1916 0 0 1213 0 0 781 270 0 0 ]
2020-05-19 17:43:39.816 D do_send_chunk() NOW SENSD: packet=1547 B
2020-05-19 17:43:39.816 T Setting 00:30:00 expiry
2020-05-19 17:43:39.817 T Setting 00:30:00 expiry
2020-05-19 17:43:39.817 T [192.168.1.131:54281 INC] [sock 39] Async send calledback 1547
2020-05-19 17:43:40.064 I [202.142.33.132:18080 OUT] 6177 bytes sent for category command-2970389107 initiated by us
2020-05-19 17:43:40.064 T [202.142.33.132:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:40.065 T Moving counter buffer by 1 second 23545 < 23548 (last time 23545.4)
2020-05-19 17:43:40.065 T Moving counter buffer by 1 second 23546 < 23548 (last time 23546.4)
2020-05-19 17:43:40.065 T Moving counter buffer by 1 second 23547 < 23548 (last time 23547.4)
2020-05-19 17:43:40.065 T Throttle throttle_speed_out: packet of ~6210b  (from 6210 b) Speed AVG=   1[w=9.11999]    1[w=9.11999] /  Limit=16 KiB/sec  [6210 0 0 9654 0 0 0 0 0 0 ]
2020-05-19 17:43:40.065 D do_send_chunk() NOW SENSD: packet=6210 B
2020-05-19 17:43:40.066 T handler_write (direct) - before ASIO write, for packet=6210 B (after sleep)
2020-05-19 17:43:40.066 T Setting 00:05:00 expiry
2020-05-19 17:43:40.066 D [202.142.33.132:18080 OUT] LEVIN_PACKET_SENT. [len=6177, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:40.067 T [202.142.33.132:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:40.067 T [202.142.33.132:18080 OUT] [sock 33] release
2020-05-19 17:43:40.067 T [202.142.33.132:18080 OUT] [sock 33] Async send calledback 6210
2020-05-19 17:43:40.067 T Moving counter buffer by 1 second 23547 < 23548 (last time 23547.8)
2020-05-19 17:43:40.067 T dbg >>> global-OUT: speed is A= 11299.4 vs Max=2.09715e+06  so sleep: D=-9.07325 sec E=  103084 (Enow=  109294) M=2.09715e+06 W=   9.123 R=1.90292e+07 Wgood      11 History: [0 8819 50329 41274 0 2662 0 0 0 0 ] m_last_sample_time= 23548.1
2020-05-19 17:43:40.067 T Throttle >>> global-OUT: packet of ~6210b  (from 6210 b) Speed AVG=  11[w=9.123]   11[w=9.123] /  Limit=2048 KiB/sec  [6210 8819 50329 41274 0 2662 0 0 0 0 ]
2020-05-19 17:43:40.366 T Moving counter buffer by 1 second 23547 < 23548 (last time 23547.8)
2020-05-19 17:43:40.366 T Throttle throttle_speed_in: packet of ~115b  (from 115 b) Speed AVG=   0[w=9.42099]    0[w=9.42099] /  Limit=16 KiB/sec  [115 425 0 477 432 0 476 432 425 0 ]
2020-05-19 17:43:40.366 T Moving counter buffer by 1 second 23547 < 23548 (last time 23547.8)
2020-05-19 17:43:40.366 T Throttle <<< global-IN: packet of ~115b  (from 115 b) Speed AVG=   8[w=9.42199]    8[w=9.42199] /  Limit=8192 KiB/sec  [115 425 48355 16861 8369 0 476 8624 425 0 ]
2020-05-19 17:43:40.367 T HTTP HEAD:
2020-05-19 17:43:40.367 T Host: 192.168.1.116
2020-05-19 17:43:40.367 T Content-Length: 362
2020-05-19 17:43:40.367 T Content-Type: application/json; charset=utf-8
2020-05-19 17:43:40.367 T
2020-05-19 17:43:40.368 T Setting 00:29:59.471000 expiry
2020-05-19 17:43:40.415 T Throttle throttle_speed_in: packet of ~362b  (from 362 b) Speed AVG=   0[w=9.46999]    0[w=9.46999] /  Limit=16 KiB/sec  [477 425 0 477 432 0 476 432 425 0 ]
2020-05-19 17:43:40.415 T Throttle <<< global-IN: packet of ~362b  (from 362 b) Speed AVG=   8[w=9.47099]    8[w=9.47099] /  Limit=8192 KiB/sec  [477 425 48355 16861 8369 0 476 8624 425 0 ]
2020-05-19 17:43:40.416 I HTTP [192.168.1.131] GET /json_rpc
2020-05-19 17:43:40.416 I [192.168.1.131:54281 INC] Calling RPC method rpc_access_submit_nonce
2020-05-19 17:43:40.419 T Blockchain::get_tail_id
2020-05-19 17:43:40.420 T BlockchainLMDB::top_block_hash
2020-05-19 17:43:40.420 T BlockchainLMDB::height
2020-05-19 17:43:40.420 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:40.421 T mdb_txn_safe: destructor
2020-05-19 17:43:40.421 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:40.421 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:40.422 T mdb_txn_safe: destructor
2020-05-19 17:43:40.422 I client <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> sends nonce: 116, current
2020-05-19 17:43:40.904 I [194.71.130.90:18080 OUT] 3570 bytes sent for category command-2970126963 initiated by us
2020-05-19 17:43:40.904 T [194.71.130.90:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:40.905 T Moving counter buffer by 1 second 23545 < 23548 (last time 23545.7)
2020-05-19 17:43:40.905 T Moving counter buffer by 1 second 23546 < 23548 (last time 23546.7)
2020-05-19 17:43:40.905 T Moving counter buffer by 1 second 23547 < 23548 (last time 23547.7)
2020-05-19 17:43:40.906 T Throttle throttle_speed_out: packet of ~3603b  (from 3603 b) Speed AVG=   1[w=9.96]    1[w=9.96] /  Limit=16 KiB/sec  [3603 0 0 12261 0 0 0 0 0 0 ]
2020-05-19 17:43:40.906 D do_send_chunk() NOW SENSD: packet=3603 B
2020-05-19 17:43:40.906 T handler_write (direct) - before ASIO write, for packet=3603 B (after sleep)
2020-05-19 17:43:40.907 T Setting 00:05:00 expiry
2020-05-19 17:43:40.907 D [194.71.130.90:18080 OUT] LEVIN_PACKET_SENT. [len=3570, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:40.907 T [194.71.130.90:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:40.908 T [194.71.130.90:18080 OUT] [sock 26] release
2020-05-19 17:43:40.908 T [194.71.130.90:18080 OUT] [sock 26] Async send calledback 3603
2020-05-19 17:43:40.909 T dbg >>> global-OUT: speed is A= 10968.9 vs Max=2.09715e+06  so sleep: D=-9.91154 sec E=  109294 (Enow=  112897) M=2.09715e+06 W=   9.964 R=2.07867e+07 Wgood      11 History: [6210 8819 50329 41274 0 2662 0 0 0 0 ] m_last_sample_time=   23549
2020-05-19 17:43:40.909 T Throttle >>> global-OUT: packet of ~3603b  (from 3603 b) Speed AVG=  10[w=9.965]   10[w=9.965] /  Limit=2048 KiB/sec  [9813 8819 50329 41274 0 2662 0 0 0 0 ]
2020-05-19 17:43:41.154 I [195.201.12.110:18080 OUT] 3570 bytes sent for category command-2970126963 initiated by us
2020-05-19 17:43:41.154 T [195.201.12.110:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:41.154 T Moving counter buffer by 1 second 23545 < 23549 (last time 23545.7)
2020-05-19 17:43:41.155 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546.7)
2020-05-19 17:43:41.155 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547.7)
2020-05-19 17:43:41.155 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.7)
2020-05-19 17:43:41.155 T Throttle throttle_speed_out: packet of ~3603b  (from 3603 b) Speed AVG=   1[w=9.21]    1[w=9.21] /  Limit=16 KiB/sec  [3603 0 0 0 12261 0 0 0 0 0 ]
2020-05-19 17:43:41.155 D do_send_chunk() NOW SENSD: packet=3603 B
2020-05-19 17:43:41.155 T handler_write (direct) - before ASIO write, for packet=3603 B (after sleep)
2020-05-19 17:43:41.156 T Setting 00:05:00 expiry
2020-05-19 17:43:41.156 D [195.201.12.110:18080 OUT] LEVIN_PACKET_SENT. [len=3570, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:41.156 T [195.201.12.110:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:41.156 T [195.201.12.110:18080 OUT] [sock 38] release
2020-05-19 17:43:41.157 T [195.201.12.110:18080 OUT] [sock 38] Async send calledback 3603
2020-05-19 17:43:41.157 T Moving counter buffer by 1 second 23548 < 23549 (last time 23549)
2020-05-19 17:43:41.157 T dbg >>> global-OUT: speed is A= 12255.4 vs Max=2.09715e+06  so sleep: D=-9.15782 sec E=  112897 (Enow=  116500) M=2.09715e+06 W=   9.212 R=1.92061e+07 Wgood      11 History: [0 9813 8819 50329 41274 0 2662 0 0 0 ] m_last_sample_time= 23549.2
2020-05-19 17:43:41.157 T Throttle >>> global-OUT: packet of ~3603b  (from 3603 b) Speed AVG=  11[w=9.213]   11[w=9.213] /  Limit=2048 KiB/sec  [3603 9813 8819 50329 41274 0 2662 0 0 0 ]
2020-05-19 17:43:41.362 I Erasing <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> with 9 credits, inactive for -22356 days
2020-05-19 17:43:41.362 I Erasing <98a01dc3b4c8f2877d367267355a8bf6ee9e002ffd384cd3f1021ef9374925db> with 0 credits, inactive for -22121 days
2020-05-19 17:43:41.404 I [51.158.78.247:18080 OUT] 3570 bytes sent for category command-2970126963 initiated by us
2020-05-19 17:43:41.404 T [51.158.78.247:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:41.404 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546)
2020-05-19 17:43:41.405 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547)
2020-05-19 17:43:41.405 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548)
2020-05-19 17:43:41.405 T Throttle throttle_speed_out: packet of ~3603b  (from 3603 b) Speed AVG=   1[w=9.46]    1[w=9.46] /  Limit=16 KiB/sec  [3603 0 0 9652 0 0 2662 0 0 0 ]
2020-05-19 17:43:41.405 D do_send_chunk() NOW SENSD: packet=3603 B
2020-05-19 17:43:41.405 T handler_write (direct) - before ASIO write, for packet=3603 B (after sleep)
2020-05-19 17:43:41.406 T Setting 00:05:00 expiry
2020-05-19 17:43:41.406 D [51.158.78.247:18080 OUT] LEVIN_PACKET_SENT. [len=3570, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:41.406 T [51.158.78.247:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:41.407 T [51.158.78.247:18080 OUT] [sock 32] release
2020-05-19 17:43:41.407 T [51.158.78.247:18080 OUT] [sock 32] Async send calledback 3603
2020-05-19 17:43:41.407 T dbg >>> global-OUT: speed is A= 12311.1 vs Max=2.09715e+06  so sleep: D= -9.4071 sec E=  116500 (Enow=  120103) M=2.09715e+06 W= 9.46299 R=1.97288e+07 Wgood      11 History: [3603 9813 8819 50329 41274 0 2662 0 0 0 ] m_last_sample_time= 23549.4
2020-05-19 17:43:41.407 T Throttle >>> global-OUT: packet of ~3603b  (from 3603 b) Speed AVG=  12[w=9.46299]   12[w=9.46299] /  Limit=2048 KiB/sec  [7206 9813 8819 50329 41274 0 2662 0 0 0 ]
2020-05-19 17:43:41.732 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546.7)
2020-05-19 17:43:41.733 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547.7)
2020-05-19 17:43:41.733 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.7)
2020-05-19 17:43:41.733 T Throttle throttle_speed_in: packet of ~1829b  (from 1829 b) Speed AVG=   1[w=9.788]    1[w=9.788] /  Limit=16 KiB/sec  [1829 0 0 7937 8192 0 0 0 0 0 ]
2020-05-19 17:43:41.733 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.5)
2020-05-19 17:43:41.734 T Throttle <<< global-IN: packet of ~1829b  (from 1829 b) Speed AVG=   8[w=9.789]    8[w=9.789] /  Limit=8192 KiB/sec  [1829 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.734 T dbg <<< global-IN: speed is A= 8769.13 vs Max=8.38861e+06  so sleep: D=-9.77872 sec E=   85841 (Enow=   87670) M=8.38861e+06 W=   9.789 R=8.20302e+07 Wgood      11 History: [1829 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.8
2020-05-19 17:43:41.734 D [51.158.78.247:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:41.734 I [51.158.78.247:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:41.735 I [51.158.78.247:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:41.738 I Including transaction <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:41.742 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:41.742 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.742 T mdb_txn_safe: destructor
2020-05-19 17:43:41.742 T Blockchain::have_tx
2020-05-19 17:43:41.742 T BlockchainLMDB::tx_exists
2020-05-19 17:43:41.742 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.759 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546.7)
2020-05-19 17:43:41.760 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547.7)
2020-05-19 17:43:41.760 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.7)
2020-05-19 17:43:41.760 T Throttle throttle_speed_in: packet of ~1358b  (from 1358 b) Speed AVG=   1[w=9.815]    1[w=9.815] /  Limit=16 KiB/sec  [1358 0 0 16352 0 0 0 0 0 0 ]
2020-05-19 17:43:41.760 T Throttle <<< global-IN: packet of ~1358b  (from 1358 b) Speed AVG=   8[w=9.816]    8[w=9.816] /  Limit=8192 KiB/sec  [3187 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.761 T dbg <<< global-IN: speed is A= 8883.35 vs Max=8.38861e+06  so sleep: D=-9.80557 sec E=   87199 (Enow=   88557) M=8.38861e+06 W=   9.816 R=8.22554e+07 Wgood      11 History: [3187 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.8
2020-05-19 17:43:41.761 T Setting 00:04:57.262000 expiry
2020-05-19 17:43:41.761 T Throttle throttle_speed_in: packet of ~471b  (from 471 b) Speed AVG=   1[w=9.817]    1[w=9.817] /  Limit=16 KiB/sec  [1829 0 0 16352 0 0 0 0 0 0 ]
2020-05-19 17:43:41.762 T Throttle <<< global-IN: packet of ~471b  (from 471 b) Speed AVG=   8[w=9.817]    8[w=9.817] /  Limit=8192 KiB/sec  [3658 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.762 T dbg <<< global-IN: speed is A= 8929.52 vs Max=8.38861e+06  so sleep: D=-9.80754 sec E=   87670 (Enow=   88141) M=8.38861e+06 W=   9.818 R=8.22717e+07 Wgood      11 History: [3658 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.8
2020-05-19 17:43:41.762 D [217.209.85.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:41.763 I [217.209.85.167:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:41.763 I [217.209.85.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:41.766 I Including transaction <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:41.772 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546.7)
2020-05-19 17:43:41.773 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547.7)
2020-05-19 17:43:41.773 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.7)
2020-05-19 17:43:41.773 T Throttle throttle_speed_in: packet of ~1346b  (from 1346 b) Speed AVG=   1[w=9.828]    1[w=9.828] /  Limit=16 KiB/sec  [1346 0 0 7937 8192 0 0 0 0 0 ]
2020-05-19 17:43:41.773 T Throttle <<< global-IN: packet of ~1346b  (from 1346 b) Speed AVG=   8[w=9.829]    8[w=9.829] /  Limit=8192 KiB/sec  [5004 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.773 T dbg <<< global-IN: speed is A= 9056.47 vs Max=8.38861e+06  so sleep: D=-9.81836 sec E=   89016 (Enow=   90362) M=8.38861e+06 W=   9.829 R=8.23626e+07 Wgood      11 History: [5004 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.8
2020-05-19 17:43:41.774 T Setting 00:04:58.237000 expiry
2020-05-19 17:43:41.774 T Throttle throttle_speed_in: packet of ~483b  (from 483 b) Speed AVG=   1[w=9.83]    1[w=9.83] /  Limit=16 KiB/sec  [1829 0 0 7937 8192 0 0 0 0 0 ]
2020-05-19 17:43:41.774 T Throttle <<< global-IN: packet of ~483b  (from 483 b) Speed AVG=   8[w=9.83]    8[w=9.83] /  Limit=8192 KiB/sec  [5487 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.775 T dbg <<< global-IN: speed is A= 9104.68 vs Max=8.38861e+06  so sleep: D=-9.81932 sec E=   89499 (Enow=   89982) M=8.38861e+06 W=    9.83 R=8.23705e+07 Wgood      11 History: [5487 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.8
2020-05-19 17:43:41.775 D [5.79.64.237:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:41.775 I [5.79.64.237:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:41.775 I [5.79.64.237:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:41.779 I Including transaction <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:41.792 I transaction with hash dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45 not found in db
2020-05-19 17:43:41.792 T mdb_txn_safe: destructor
2020-05-19 17:43:41.793 T Blockchain::get_current_cumulative_block_weight_limit
2020-05-19 17:43:41.814 T Moving counter buffer by 1 second 23546 < 23549 (last time 23546.7)
2020-05-19 17:43:41.815 T Moving counter buffer by 1 second 23547 < 23549 (last time 23547.7)
2020-05-19 17:43:41.815 T Moving counter buffer by 1 second 23548 < 23549 (last time 23548.7)
2020-05-19 17:43:41.815 T Throttle throttle_speed_in: packet of ~1346b  (from 1346 b) Speed AVG=   1[w=9.87]    1[w=9.87] /  Limit=16 KiB/sec  [1346 0 0 16129 0 0 0 0 0 0 ]
2020-05-19 17:43:41.815 T Throttle <<< global-IN: packet of ~1346b  (from 1346 b) Speed AVG=   8[w=9.871]    8[w=9.871] /  Limit=8192 KiB/sec  [6833 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.816 T dbg <<< global-IN: speed is A= 9203.22 vs Max=8.38861e+06  so sleep: D=-9.86014 sec E=   90845 (Enow=   92191) M=8.38861e+06 W=   9.871 R=8.27131e+07 Wgood      11 History: [6833 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.9
2020-05-19 17:43:41.816 T Setting 00:04:59.608000 expiry
2020-05-19 17:43:41.816 T Throttle throttle_speed_in: packet of ~483b  (from 483 b) Speed AVG=   1[w=9.872]    1[w=9.872] /  Limit=16 KiB/sec  [1829 0 0 16129 0 0 0 0 0 0 ]
2020-05-19 17:43:41.817 T Throttle <<< global-IN: packet of ~483b  (from 483 b) Speed AVG=   8[w=9.872]    8[w=9.872] /  Limit=8192 KiB/sec  [7316 477 425 48355 16861 8369 0 476 8624 425 ]
2020-05-19 17:43:41.817 T dbg <<< global-IN: speed is A= 9250.28 vs Max=8.38861e+06  so sleep: D= -9.8621 sec E=   91328 (Enow=   91811) M=8.38861e+06 W=   9.873 R=8.27294e+07 Wgood      11 History: [7316 477 425 48355 16861 8369 0 476 8624 425 ] m_last_sample_time= 23549.9
2020-05-19 17:43:41.817 D [195.201.12.110:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:41.818 I [195.201.12.110:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:41.818 I [195.201.12.110:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:41.821 I Including transaction <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:41.866 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:41.866 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.866 T mdb_txn_safe: destructor
2020-05-19 17:43:41.866 T Blockchain::have_tx
2020-05-19 17:43:41.866 T BlockchainLMDB::tx_exists
2020-05-19 17:43:41.866 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.866 I transaction with hash dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45 not found in db
2020-05-19 17:43:41.867 T mdb_txn_safe: destructor
2020-05-19 17:43:41.867 T BlockchainLMDB::height
2020-05-19 17:43:41.867 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.867 T mdb_txn_safe: destructor
2020-05-19 17:43:41.867 T BlockchainLMDB::get_block_already_generated_coins
2020-05-19 17:43:41.867 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.868 T mdb_txn_safe: destructor
2020-05-19 17:43:41.868 D Using 0.000000011197/byte fee
2020-05-19 17:43:41.868 T Blockchain::check_tx_outputs
2020-05-19 17:43:41.868 T Blockchain::check_tx_inputs
2020-05-19 17:43:41.868 T BlockchainLMDB::height
2020-05-19 17:43:41.869 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.869 T mdb_txn_safe: destructor
2020-05-19 17:43:41.869 T Blockchain::check_tx_inputs
2020-05-19 17:43:41.869 D Mixin: 10-10
2020-05-19 17:43:41.869 T Blockchain::have_tx_keyimg_as_spent
2020-05-19 17:43:41.869 T BlockchainLMDB::has_key_image
2020-05-19 17:43:41.870 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.917 T mdb_txn_safe: destructor
2020-05-19 17:43:41.918 T Blockchain::check_tx_input
2020-05-19 17:43:41.918 T Blockchain::scan_outputkeys_for_indexes
2020-05-19 17:43:41.918 T BlockchainLMDB::get_output_key
2020-05-19 17:43:41.918 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:41.995 T Moving counter buffer by 1 second 23544 < 23550 (last time 23544)
2020-05-19 17:43:41.996 T Moving counter buffer by 1 second 23545 < 23550 (last time 23545)
2020-05-19 17:43:41.996 T Moving counter buffer by 1 second 23546 < 23550 (last time 23546)
2020-05-19 17:43:41.996 T Moving counter buffer by 1 second 23547 < 23550 (last time 23547)
2020-05-19 17:43:41.996 T Moving counter buffer by 1 second 23548 < 23550 (last time 23548)
2020-05-19 17:43:41.996 T Moving counter buffer by 1 second 23549 < 23550 (last time 23549)
2020-05-19 17:43:41.996 T Throttle throttle_speed_in: packet of ~1829b  (from 1829 b) Speed AVG=   1[w=9.05099]    1[w=9.05099] /  Limit=16 KiB/sec  [1829 0 0 0 0 0 7937 0 0 8192 ]
2020-05-19 17:43:41.997 T Moving counter buffer by 1 second 23549 < 23550 (last time 23549.8)
2020-05-19 17:43:41.997 T Throttle <<< global-IN: packet of ~1829b  (from 1829 b) Speed AVG=   9[w=9.05199]    9[w=9.05199] /  Limit=8192 KiB/sec  [1829 7316 477 425 48355 16861 8369 0 476 8624 ]
2020-05-19 17:43:41.997 T dbg <<< global-IN: speed is A= 10243.2 vs Max=8.3886e+06  so sleep: D= -9.0419 sec E=   92732 (Enow=   94561) M=8.3886e+06 W= 9.05299 R=7.58493e+07 Wgood      11 History: [1829 7316 477 425 48355 16861 8369 0 476 8624 ] m_last_sample_time=   23550
2020-05-19 17:43:41.997 D [183.82.83.167:18080 OUT] LEVIN_PACKET_RECEIVED. [len=1796, flags1, r?=0, cmd = 2002, v=1
2020-05-19 17:43:41.998 I [183.82.83.167:18080 OUT] 1796 bytes received for category command-2002 initiated by peer
2020-05-19 17:43:41.998 I [183.82.83.167:18080 OUT] Received NOTIFY_NEW_TRANSACTIONS (1 txes)
2020-05-19 17:43:42.001 I Including transaction <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:42.189 T db3: 271
2020-05-19 17:43:42.189 T mdb_txn_safe: destructor
2020-05-19 17:43:42.189 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.189 T BlockchainLMDB::height
2020-05-19 17:43:42.190 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.190 T mdb_txn_safe: destructor
2020-05-19 17:43:42.190 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.190 T BlockchainLMDB::height
2020-05-19 17:43:42.190 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.190 T mdb_txn_safe: destructor
2020-05-19 17:43:42.190 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.191 T BlockchainLMDB::height
2020-05-19 17:43:42.191 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.191 T mdb_txn_safe: destructor
2020-05-19 17:43:42.191 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.191 T BlockchainLMDB::height
2020-05-19 17:43:42.191 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.191 T mdb_txn_safe: destructor
2020-05-19 17:43:42.191 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.191 T BlockchainLMDB::height
2020-05-19 17:43:42.191 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.191 T mdb_txn_safe: destructor
2020-05-19 17:43:42.191 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.192 T BlockchainLMDB::height
2020-05-19 17:43:42.192 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.192 T mdb_txn_safe: destructor
2020-05-19 17:43:42.192 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.192 T BlockchainLMDB::height
2020-05-19 17:43:42.192 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.192 T mdb_txn_safe: destructor
2020-05-19 17:43:42.192 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.192 T BlockchainLMDB::height
2020-05-19 17:43:42.192 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.192 T mdb_txn_safe: destructor
2020-05-19 17:43:42.193 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.193 T BlockchainLMDB::height
2020-05-19 17:43:42.193 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.193 T mdb_txn_safe: destructor
2020-05-19 17:43:42.193 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.193 T BlockchainLMDB::height
2020-05-19 17:43:42.193 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.193 T mdb_txn_safe: destructor
2020-05-19 17:43:42.193 T Blockchain::is_tx_spendtime_unlocked
2020-05-19 17:43:42.193 T BlockchainLMDB::height
2020-05-19 17:43:42.193 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.193 T mdb_txn_safe: destructor
2020-05-19 17:43:42.194 T BlockchainLMDB::height
2020-05-19 17:43:42.194 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.194 T mdb_txn_safe: destructor
2020-05-19 17:43:42.238 T BlockchainLMDB::height
2020-05-19 17:43:42.238 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.239 T mdb_txn_safe: destructor
2020-05-19 17:43:42.239 T BlockchainLMDB::get_block_hash_from_height
2020-05-19 17:43:42.240 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.240 T mdb_txn_safe: destructor
2020-05-19 17:43:42.240 T BlockchainLMDB::batch_start
2020-05-19 17:43:42.241 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:42.241 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:42.241 T BlockchainLMDB::need_resize
2020-05-19 17:43:42.242 D DB map size:     98557263872
2020-05-19 17:43:42.242 D Space used:      88234479616
2020-05-19 17:43:42.242 D Space remaining: 10322784256
2020-05-19 17:43:42.242 D Size threshold:  0
2020-05-19 17:43:42.243 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:42.243 T batch transaction: begin
2020-05-19 17:43:42.244 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:42.244 T BlockchainLMDB::remove_txpool_tx
2020-05-19 17:43:42.244 T BlockchainLMDB::add_txpool_tx
2020-05-19 17:43:42.245 T BlockchainLMDB::batch_stop
2020-05-19 17:43:42.245 T batch transaction: committing...
2020-05-19 17:43:42.253 T mdb_txn_safe: destructor
2020-05-19 17:43:42.254 T batch transaction: end
2020-05-19 17:43:42.254 I Transaction added to pool: txid <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45> weight: 1774 fee/byte: 11200.7
2020-05-19 17:43:42.254 T BlockchainLMDB::batch_start
2020-05-19 17:43:42.255 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:42.255 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:42.255 T BlockchainLMDB::need_resize
2020-05-19 17:43:42.256 D DB map size:     98557263872
2020-05-19 17:43:42.256 D Space used:      88234479616
2020-05-19 17:43:42.256 D Space remaining: 10322784256
2020-05-19 17:43:42.256 D Size threshold:  0
2020-05-19 17:43:42.257 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:42.257 T batch transaction: begin
2020-05-19 17:43:42.257 T BlockchainLMDB::batch_stop
2020-05-19 17:43:42.258 T batch transaction: committing...
2020-05-19 17:43:42.258 T mdb_txn_safe: destructor
2020-05-19 17:43:42.258 T batch transaction: end
2020-05-19 17:43:42.259 D tx added: <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>
2020-05-19 17:43:42.262 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:42.262 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.263 T mdb_txn_safe: destructor
2020-05-19 17:43:42.263 D tx <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>already have transaction in tx_pool
2020-05-19 17:43:42.263 T BlockchainLMDB::batch_start
2020-05-19 17:43:42.264 T BlockchainLMDB::check_and_resize_for_batch
2020-05-19 17:43:42.264 T [check_and_resize_for_batch] checking DB size
2020-05-19 17:43:42.264 T BlockchainLMDB::need_resize
2020-05-19 17:43:42.264 D DB map size:     98557263872
2020-05-19 17:43:42.265 D Space used:      88234479616
2020-05-19 17:43:42.265 D Space remaining: 10322784256
2020-05-19 17:43:42.265 D Size threshold:  0
2020-05-19 17:43:42.266 D Percent used: 89.5261  Percent threshold: 90.0000
2020-05-19 17:43:42.266 T batch transaction: begin
2020-05-19 17:43:42.266 T BlockchainLMDB::get_txpool_tx_meta
2020-05-19 17:43:42.266 T BlockchainLMDB::update_txpool_tx
2020-05-19 17:43:42.267 T Setting 00:04:56.854000 expiry
2020-05-19 17:43:42.267 T BlockchainLMDB::batch_stop
2020-05-19 17:43:42.267 T batch transaction: committing...
2020-05-19 17:43:42.273 T mdb_txn_safe: destructor
2020-05-19 17:43:42.273 T batch transaction: end
2020-05-19 17:43:42.273 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:42.274 D Queueing 1 transaction(s) for Dandelion++ fluffing
2020-05-19 17:43:42.274 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.274 T mdb_txn_safe: destructor
2020-05-19 17:43:42.274 D tx <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>already have transaction in tx_pool
2020-05-19 17:43:42.275 T Setting 00:04:57.831000 expiry
2020-05-19 17:43:42.278 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:42.278 T Setting 00:04:59.494000 expiry
2020-05-19 17:43:42.279 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.279 T mdb_txn_safe: destructor
2020-05-19 17:43:42.279 D tx <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>already have transaction in tx_pool
2020-05-19 17:43:42.279 T Setting 00:04:59.240000 expiry
2020-05-19 17:43:42.283 T BlockchainLMDB::txpool_has_tx
2020-05-19 17:43:42.283 T BlockchainLMDB::block_rtxn_start
2020-05-19 17:43:42.283 T mdb_txn_safe: destructor
2020-05-19 17:43:42.283 D tx <dea2fdc411734713f6d9bc1e2e9f64caa1b3d3a8001d34f597ca85d9a9f01e45>already have transaction in tx_pool
2020-05-19 17:43:42.284 T Setting 00:04:45.499000 expiry
2020-05-19 17:43:42.358 I [217.209.85.167:18080 OUT] 3572 bytes sent for category command-3104344691 initiated by us
2020-05-19 17:43:42.358 T [217.209.85.167:18080 OUT] [levin_protocol] -->> start_outer_call
2020-05-19 17:43:42.358 T Moving counter buffer by 1 second 23546 < 23550 (last time 23546.8)
2020-05-19 17:43:42.359 T Moving counter buffer by 1 second 23547 < 23550 (last time 23547.8)
2020-05-19 17:43:42.359 T Moving counter buffer by 1 second 23548 < 23550 (last time 23548.8)
2020-05-19 17:43:42.359 T Moving counter buffer by 1 second 23549 < 23550 (last time 23549.8)
2020-05-19 17:43:42.359 T Throttle throttle_speed_out: packet of ~3605b  (from 3605 b) Speed AVG=   2[w=9.414]    2[w=9.414] /  Limit=16 KiB/sec  [3605 0 0 0 19542 0 0 5271 0 0 ]
2020-05-19 17:43:42.360 D do_send_chunk() NOW SENSD: packet=3605 B
2020-05-19 17:43:42.360 T handler_write (direct) - before ASIO write, for packet=3605 B (after sleep)
2020-05-19 17:43:42.360 T Setting 00:05:00 expiry
2020-05-19 17:43:42.360 D [217.209.85.167:18080 OUT] LEVIN_PACKET_SENT. [len=3572, flags1, r?=0, cmd = 2002, ver=1
2020-05-19 17:43:42.361 T [217.209.85.167:18080 OUT] [levin_protocol] <<-- finish_outer_call
2020-05-19 17:43:42.361 T [217.209.85.167:18080 OUT] [sock 37] release
2020-05-19 17:43:42.361 T [217.209.85.167:18080 OUT] [sock 37] Async send calledback 3605
2020-05-19 17:43:42.361 T Moving counter buffer by 1 second 23549 < 23550 (last time 23549.5)
2020-05-19 17:43:42.362 T dbg >>> global-OUT: speed is A= 12753.8 vs Max=2.09715e+06  so sleep: D=-9.35939 sec E=  120103 (Enow=  123708) M=2.09715e+06 W=   9.417 R=1.96288e+07 Wgood      11 History: [0 7206 9813 8819 50329 41274 0 2662 0 0 ] m_last_sample_time= 23550.4
2020-05-19 17:43:42.362 T Throttle >>> global-OUT: packet of ~3605b  (from 3605 b) Speed AVG=  12[w=9.417]   12[w=9.417] /  Limit=2048 KiB/sec  [3605 7206 9813 8819 50329 41274 0 2662 0 0 ]
2020-05-19 17:43:42.616 I client <3405e69406082063e40d1cc0a631a4ad0e0b8a6eaaf1df71dde21bd087996ded> credited for 5, now 14

Thread 6 "monerod" received signal SIGABRT, Aborted.
[Switching to Thread 0x5a7feff0 (LWP 23755)]
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50      ../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb)


## bt full

(gdb) bt full
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
        set = {__val = {0, 0, 2096218807, 189497231, 1518326228, 1978252153, 999730225, 4196136017, 1497398264, 96, 96, 1090699150, 3471035746,
            3192895496, 3605679987, 2606098142, 1868450146, 76974984, 0, 2015174133, 1518326276, 0, 0, 1518326312, 1986402492, 1, 1518326300, 0,
            0, 76974984, 0, 0}}
        pid = <optimized out>
        tid = <optimized out>
        ret = <optimized out>
#1  0x76380230 in __GI_abort () at abort.c:79
        save_stage = 1
        act = {__sigaction_handler = {sa_handler = 0x514feac0, sa_sigaction = 0x514feac0}, sa_mask = {__val = {46, 46, 4294967295, 0, 0,
              1363954433, 1518326648, 2, 12707800, 1518326960, 15320684, 1518326656, 0, 1364025600, 46, 46, 1518326784, 1431655765, 1081464149,
              258, 1363954224, 196, 196, 16968952, 0, 1518326936, 1986592768, 16968880, 1518327768, 96, 96, 1986876418}}, sa_flags = 4098,
          sa_restorer = 0x1}
        sigs = {__val = {32, 0 <repeats 31 times>}}
#2  0x007f2038 in std::vector<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key>, std::allocator<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key> > >::operator=(std::vector<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key>, std::allocator<boost::variant<cryptonote::txin_gen, cryptonote::txin_to_script, cryptonote::txin_to_scripthash, cryptonote::txin_to_key> > > const&) ()
No symbol table info available.
#3  0x007f2c58 in cryptonote::block::operator=(cryptonote::block const&) ()
No symbol table info available.
#4  0x008cdbf8 in cryptonote::rpc_payment::submit_nonce(crypto::public_key const&, unsigned int, crypto::hash const&, long long&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, unsigned long long&, crypto::hash&, cryptonote::block&, unsigned int, bool&) ()
No symbol table info available.
#5  0x007c246c in cryptonote::core_rpc_server::on_rpc_access_submit_nonce(epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_ACCESS_SUBMIT_NONCE::request_t> const&, epee::misc_utils::struct_init<cryptonote::COMMAND_RPC_ACCESS_SUBMIT_NONCE::response_t>&, epee::json_rpc::error&, epee::net_utils::connection_context_base const*) ()
No symbol table info available.
#6  0x008bdb44 in bool cryptonote::core_rpc_server::handle_http_request_map<epee::net_utils::connection_context_base>(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) ()
No symbol table info available.
#7  0x008c9c70 in cryptonote::core_rpc_server::handle_http_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&, epee::net_utils::connection_context_base&) ()
No symbol table info available.
#8  0x00826d7c in epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base>::handle_request(epee::net_utils::http::http_request_info const&, epee::net_utils::http::http_response_info&) ()
No symbol table info available.
#9  0x007ebdc8 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_request_and_send_response(epee::net_utils::http::http_request_info const&) ()
No symbol table info available.
#10 0x007ec260 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_retriving_query_body()
    ()
No symbol table info available.
#11 0x008999e8 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_buff_in(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&) ()
No symbol table info available.
#12 0x0089a090 in epee::net_utils::http::simple_http_connection_handler<epee::net_utils::connection_context_base>::handle_recv(void const*, unsigned int) ()
No symbol table info available.
#13 0x0089a2a8 in epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::handle_read(boost::system::error_code const&, unsigned int) ()
No symbol table info available.
#14 0x007f6980 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int>&) ()
No symbol table info available.
#15 0x007f7fa8 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
No symbol table info available.
#16 0x007f8300 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
No symbol table info available.
#17 0x007f8518 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
No symbol table info available.
#18 0x007c5768 in boost::asio::detail::epoll_reactor::descriptor_state::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
No symbol table info available.
#19 0x006a4f2c in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
No symbol table info available.
#20 0x006a5078 in boost::asio::detail::scheduler::run(boost::system::error_code&) ()
No symbol table info available.
#21 0x006b15ac in epee::net_utils::boosted_tcp_server<epee::net_utils::http::http_custom_handler<epee::net_utils::connection_context_base> >::worker_thread() ()
No symbol table info available.
#22 0x76976cdc in ?? () from /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.67.0
No symbol table info available.
#23 0x764bd494 in start_thread (arg=0x5a7feff0) at pthread_create.c:486
        ret = <optimized out>
        start = <optimized out>
        pd = 0x5a7feff0
        unwind_buf = {cancel_jmp_buf = {{jmp_buf = {1009024672, 269501184, 1996482920, 1518333936, 1948230864, 338, 2130699986, 1518333936, 0,
                1518332716, 0 <repeats 54 times>}, mask_was_saved = 0}}, priv = {pad = {0x0, 0x0, 0x0, 0x0}, data = {prev = 0x0, cleanup = 0x0,
--Type <RET> for more, q to quit, c to continue without paging--

## Next page

              canceltype = 0}}}
        not_first_call = <optimized out>
#24 0x76440578 in ?? () at ../sysdeps/unix/sysv/linux/arm/clone.S:73 from /lib/arm-linux-gnueabihf/libc.so.6
No locals.
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
(gdb)



## moneromooo-monero | 2020-05-19T18:04:23+00:00
Helpful, thanks. I think I know what the problem is, I'll make a patch.

## shermand100 | 2020-05-19T18:07:28+00:00
> Helpful, thanks. I think I know what the problem is, I'll make a patch.

TBH I'm kinda thankful it's actually a real error. After I submitted it I had the gut feeling this was going to be another lesson in why not to mess around with single board computers. Haha

## moneromooo-monero | 2020-05-19T18:27:08+00:00
Please try the last patch in https://github.com/moneromooo-monero/bitmonero/tree/rpl

## shermand100 | 2020-05-19T21:50:05+00:00
Sure, and just to clarify how I'm doing it:

I've removed my old Monero files

Downloaded v0.16 again with `git clone --recursive -b release-v0.16 https://github.com/monero-project/monero.git`

Replaced the files `src/rpc/rpc_payment.cpp` and `src/rpc/rpc_payment.h` with the changes you've made linked above.

I build with
`USE_SINGLE_BUILDDIR=1 make`

And will repeat my testing to see what the new outcome is.
It will compile overnight on an Odroid XU4 this time so it's got a bit more power.

Edit: 20/05 pm
The very old drive I use for testing and tinkering became unfixably read only and needed re-formatting. I've copied the blockchain back on from elsewhere but is 2000 blocks behind and will complete sync at some point whilst I'm sleeping.
I hope to get some testing done in the morning before work (early am GMT 21/05)

## shermand100 | 2020-05-21T15:45:32+00:00
> Please try the last patch in https://github.com/moneromooo-monero/bitmonero/tree/rpl

The latest patch built without error, sync was fine and continued to be stable for many hours.

Problems occurred again when connecting the wallet-cli (same start commands as above with local ip now changed ending 127):

## monerod output (wallet connected)

came home from work to find the monerod terminal screen filling with:

> ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒


I used ctrl+c to stop the node
then:
#### bt full

Thread 1 "monerod" received signal SIGINT, Interrupt.
0xb66b0524 in __libc_do_syscall () from /lib/arm-linux-gnueabihf/libpthread.so.0
(gdb) bt full
#0  0xb66b0524 in __libc_do_syscall () from /lib/arm-linux-gnueabihf/libpthread.so.0
No symbol table info available.
#1  0xb66ab67e in pthread_cond_wait@@GLIBC_2.4 () from /lib/arm-linux-gnueabihf/libpthread.so.0
No symbol table info available.
#2  0x00680c1e in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
No symbol table info available.
#3  0xb6a9f4ce in boost::thread::join_noexcept() () from /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.67.0
No symbol table info available.
#4  0x0087b834 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned int, bool, boost::thread_attributes const&) ()
No symbol table info available.
#5  0x0087caee in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
No symbol table info available.
#6  0x00694b1a in daemonize::t_p2p::run() ()
No symbol table info available.
#7  0x006877a4 in daemonize::t_daemon::run(bool) ()
No symbol table info available.
#8  0x006bf41a in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
No symbol table info available.
#9  0x006c3e5a in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
No symbol table info available.
#10 0x00660816 in main ()
No symbol table info available.
(gdb)


## Wallet-cli

> Monero 'Carbon Chamaeleon' (v0.16.0.0-4987161fa)
> Logging to /home/pinodexmr/monero/build/release/bin/monero-wallet-cli.log
> [New Thread 0xb4042ff0 (LWP 7460)]
> Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
> Wallet file name (or Ctrl-C to quit): TestWallet
> Wallet and key files found, loading...
> Wallet password:
> Opened wallet: 42FUdmpe5sFEGKjGSmiWWVAXeNEX2N1Vai88kLytws3P93kdraPbhYCZ416NJHLkFrVYLMTL3F98SG3spFSZbB2ERnrtkF8
> **********************************************************************
> Use the "help" command to see a simplified list of available commands.
> Use the "help_advanced" command to see an advanced list of available commands.
> Use "help_advanced <command>" to see a command's documentation.
> **********************************************************************
> Starting refresh...
> [New Thread 0xb352fff0 (LWP 7564)]
> [New Thread 0xb302eff0 (LWP 7565)]
> [New Thread 0xb2b2dff0 (LWP 7566)]
> [New Thread 0xb262cff0 (LWP 7567)]
> [New Thread 0xb212bff0 (LWP 7568)]
> [New Thread 0xb1c2aff0 (LWP 7569)]
> [New Thread 0xb1729ff0 (LWP 7570)]
> Error: refresh failed: payment required.. Blocks received: 0
> [New Thread 0xb1228ff0 (LWP 7571)]
> Background refresh thread started
> [wallet 42FUdm (out of sync)]: start_mining_for_rpc
> [wallet 42FUdm (out of sync)]: [Thread 0xb1729ff0 (LWP 7570) exited]
> [Thread 0xb1c2aff0 (LWP 7569) exited]
> [Thread 0xb212bff0 (LWP 7568) exited]
> [Thread 0xb262cff0 (LWP 7567) exited]
> [Thread 0xb2b2dff0 (LWP 7566) exited]
> [Thread 0xb302eff0 (LWP 7565) exited]
> [Thread 0xb352fff0 (LWP 7564) exited]
> [Thread 0xb4042ff0 (LWP 7460) exited]
> [Thread 0xb44c1010 (LWP 7457) exited]

Program terminated with signal SIGKILL, Killed.
The program no longer exists.

#### bt full


(gdb) bt full
No stack.
(gdb)

The wallet-cli was taking a very long time to start RPC Mining so I left it whilst at work.

I will repeat this again to see if this a repeatable fault, or was just unlucky this first time.

## moneromooo-monero | 2020-05-21T15:48:56+00:00
Looks like some weird other problem got to you first. Doesn't seem related.

## shermand100 | 2020-05-21T15:53:43+00:00
Yeah I wasn't around to see it fail so I'm going to see if it repeats

## shermand100 | 2020-05-22T11:44:17+00:00
@moneromooo-monero Whatever has been changed seems to prevent any commands being passed from the wallet to to daemon.
So I can open the wallet file, enter the password, it connects to the daemon and realises it needs the RPC_payment.

At the wallet command line neither `rpc_payment_info` or `start_mining_for_rpc` work as expected.

Both commands process for approx 20mins before stating "Killed"

### Output:


> Monero 'Carbon Chamaeleon' (v0.16.0.0-4987161fa)
> Logging to ./monero-wallet-cli.log
> Specify wallet file name (e.g., MyWallet). If the wallet doesn't exist, it will be created.
> Wallet file name (or Ctrl-C to quit): TestWallet
> Wallet and key files found, loading...
> Wallet password:
> Opened wallet: 44S1EpwmRmVAKyRjyXiTTNNj8s6WJav1XFxSTQad1fRfRA7fVEkwTM689hAZMgKYoiGoCNCvipU2cHm1LGLEP7cv8JgdWuz
> **********************************************************************
> Use the "help" command to see a simplified list of available commands.
> Use the "help_advanced" command to see an advanced list of available commands.
> Use "help_advanced <command>" to see a command's documentation.
> **********************************************************************
> Background mining not enabled. Run "set setup-background-mining 1" to change.
> Starting refresh...
> Error: refresh failed: payment required.. Blocks received: 0
> Background refresh thread started
> [wallet 44S1Ep (out of sync)]: start_mining_for_rpc
> [wallet 44S1Ep (out of sync)]: Killed



## moneromooo-monero | 2020-05-22T13:15:02+00:00
Works for me. "Killed" is the OOM killer. Looks likely that your wallet is trying to use more RAM that the system is able to give it. Try again, run start_mining_for_rpc, wait a minute, then run:
gdb monero-wallet-cli \`pidof monero-wallet-cli\`  (use the path to the binary if it's not in . for the first argument)
thread apply all bt


## shermand100 | 2020-05-22T16:49:37+00:00
@moneromooo-monero 
Ok, apologies for that last distraction then. That was a system resource issue.

Unfortunately I'm then back to a variation of the original problem.

### Setup

Running your modified Monero v.16 node on an Odroid XU4 Armbian. Node runs happily.

Wallet-cli v0.15.0.5 Windows PC plenty of resources, no RAM issue, can send commands and receive cli feedback fine.

### Issue

The variation on the original issue is that despite checking and double checking internet time settings and zones on the node and wallet, both are sync'd with internet time, the payment of mining credits is sporadic due to the node falsely marking the connected wallet as inactive for a now positive number of days. This seems to cause the node to delete the wallets held credits.

### Symptoms - I have heavily edited the following logs so they are chronological and show what I hope are relevant lines

## Wallet-cli

Monero 'Carbon Chamaeleon' (v0.15.0.5-release)
Logging to E:\Cryptocurrencies\Monero\Monero GUI Wallet\monero-wallet-cli.log
Wallet password:
Opened wallet: 4BAbwt75aiV46ntopaip71jMffp6mDR1q8PbvZz4WwPNWmM84yq8AEXNxhk5Bah8wHAAbdpUywUNTNgKc8ruDXBVBGLwZX8
**********************************************************************
Use the "help" command to see the list of available commands.
Use "help <command>" to see a command's documentation.
**********************************************************************
Starting refresh...
Error: refresh failed: payment required.. Blocks received: 0
Background refresh thread started
[wallet 4BAbwt (out of sync)]: Daemon requests payment at diff 1000, with 0.050000 credits/hash. Run start_mining_for_rpc to start mining to pay for RPC access, or use another daemon
[wallet 4BAbwt (out of sync)]: start_mining_for_rpc
Starting mining for RPC access: diff 1000, 0.050000 credits/hash
Run stop_mining_for_rpc to stop
[wallet 4BAbwt (out of sync)]: rpc_payment_info
RPC client ID: <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232>
RPC client secret key: <557b91cebdaadc98aaf59670037bfa8b0b31cc-removed>
Using daemon: 192.168.1.127:18089
Payments required for node use, current credits: 0
Credits target: 50000
Credits spent this session: 0
Difficulty: 1000, 50 credits per hash found, 0.05 credits/hash
Not mining
[wallet 4BAbwt (out of sync)]: Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing
[wallet 4BAbwt (out of sync)]: Error: Error mining to daemon: Found nonce, but daemon errored out with error -18: Stale payment, continuing
[wallet 4BAbwt (out of sync)]: Error: Error mining to daemon: Found nonce, but daemon did not credit us with the expected amount
[wallet 4BAbwt (out of sync)]: Error: Failed to start mining for RPC payment
[wallet 4BAbwt (out of sync)]: Error: Error mining to daemon: Found nonce, but daemon did not credit us with the expected amount
[wallet 4BAbwt (out of sync)]: Error: Failed to start mining for RPC payment


## Monerod 

2020-05-22 16:33:21.611 I Erasing <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> with 190 credits, inactive for 9429 days
...
2020-05-22 16:33:43.925 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> sends nonce: 8476, current
...
2020-05-22 16:33:57.756 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> sends nonce: 10410, current
...
2020-05-22 16:33:59.348 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> credited for 50, now 200
...

#### ***SENT ANOTHER COMMAND via WALLET "rpc_payment_info" approx here***

2020-05-22 16:37:21.614 I Erasing <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> with 439 credits, inactive for 6478 days
...
2020-05-22 16:38:13.967 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> sends nonce: 22023, current
...
2020-05-22 16:40:37.776 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> credited for 50, now 99
...
2020-05-22 16:41:21.617 I Erasing <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> with 399 credits, inactive for 4062 days
...
2020-05-22 16:41:37.080 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> credited for 50, now 50

## Wallet-cli

[wallet 4BAbwt (out of sync)]: rpc_payment_info
RPC client ID: <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232>
RPC client secret key: <557b91cebdaadc98aaf59670-removed>
Using daemon: 192.168.1.127:18089
Payments required for node use, current credits: 39
Credits target: 50000
Credits spent this session: 242
Credit discrepancy this session: 1278 (528.099%)
Difficulty: 1000, 50 credits per hash found, 0.05 credits/hash
Mining for payment at 191.2 H/s
Estimated time till 50000 credits target mined: 1 hours
[wallet 4BAbwt (out of sync)]:

## Monerod


2020-05-22 16:44:21.618 I Erasing <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> with 80 credits, inactive for 1764 days
...
2020-05-22 16:44:25.064 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> sends nonce: 40472, current
...
2020-05-22 16:44:26.656 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> credited for 50, now 50
...
2020-05-22 16:44:27.359 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> sends nonce: 40591, current
2020-05-22 16:44:28.826 I client <5fd351948851957b719888c347108a4d12cbad117915354d5e786764bd59c232> credited for 50, now 99



Edited for some embarrassingly bad spelling

## moneromooo-monero | 2020-05-22T16:55:46+00:00
But it doesn't crash anymore, right ? :)

Please paste the output of this command on the machines running both daemon and wallet:
date +%s


## shermand100 | 2020-05-22T17:25:22+00:00
No more crashes. All good on that front.

Monerod on Armbian

pinodexmr@PiNodeXMR:~$ date +%s
1590168263


Windows Wallet-cli
C:\Users\danie>time /t
18:24
C:\Users\danie>date /t
22/05/2020

**Edit:** added date command for windows to avoid major discrepancy 

**Edit2:** + Human readable

pinodexmr@PiNodeXMR:~$ date +%c
Fri 22 May 2020 06:30:42 PM BST

**Edit3:** I put the windows wallet-cli v0.15.0.5 and wallet file+keys on a USB drive and ran the same from my laptop. The same inactive for an irrational number of days with erase issue exists.

Occasional 

2020-05-22 18:09:28.430 W Very stale nonce

from monerod

**Edit4:**
Using edits so I don't span you with notifications I hope.

I've seen on monerod several negative values for "inactive" for days scroll past, so I think the original issue still exists

Is it relevant that it is erasing at 1 minute intervals? Does that give a clue?

2020-05-22 18:12:26.941 I Erasing <eb238e0a6131068e12a9be3fb6c3368c7ba3359ba3c7c97cc8a3ab909227801d> with 249 credits, inactive for -9381 days


2020-05-22 18:13:26.943 I Erasing <eb238e0a6131068e12a9be3fb6c3368c7ba3359ba3c7c97cc8a3ab909227801d> with 34 credits, inactive for -10232 days


2020-05-22 18:14:26.944 I Erasing <eb238e0a6131068e12a9be3fb6c3368c7ba3359ba3c7c97cc8a3ab909227801d> with 0 credits, inactive for -10801 days

2020-05-22 18:15:26.945 I Erasing <eb238e0a6131068e12a9be3fb6c3368c7ba3359ba3c7c97cc8a3ab909227801d> with 0 credits, inactive for -11840 days

2020-05-22 18:16:27.318 I Erasing <eb238e0a6131068e12a9be3fb6c3368c7ba3359ba3c7c97cc8a3ab909227801d> with 50 credits, inactive for -12187 days









## moneromooo-monero | 2020-05-22T18:57:26+00:00
I think I found what's going on, please try this patch:
https://paste.debian.net/1148331/

Apply by saving the patch in a file (ie, FILENAME) and:

patch -p1 < FILENAME


## shermand100 | 2020-05-22T19:12:29+00:00
Apologies again I need a little more clarification on how to apply this patch.

I've created the file. Called it FILENAME (because it's as good as any) with:

`nano FILENAME`

Pasted in the contents of the file from the link and saved it.

Changed permission of /home/pinodexmr/FILENAME to 777 to prevent issues.

Then I'm not applying it right, trying to use:

./monerod patch -pl < /home/pinodexmr/FILENAME

unrecognised option '-pl'

So I'm not understanding correctly, I've tried some variations (thats a -p(one) I'm just copy/pasting from your comment.


## selsta | 2020-05-22T19:15:49+00:00
Instead of

`./monerod patch -pl < /home/pinodexmr/FILENAME`

do

`patch -p1 < /home/pinodexmr/FILENAME`

Edit: oops see mooos comment

## moneromooo-monero | 2020-05-22T19:24:41+00:00
p1, not pl. Like one.

## shermand100 | 2020-05-22T19:34:04+00:00
Thanks for that. I'm learning all sorts today.

It asked a few questions but I think I've answered them as intended:

> pinodexmr@PiNodeXMR:~/monero/build/release/bin$ patch -p1 < /home/pinodexmr/FILENAME
> can't find file to patch at input line 5
> Perhaps you used the wrong -p or --strip option?
> The text leading up to this was:
> --------------------------
> |diff --git a/src/rpc/rpc_payment.cpp b/src/rpc/rpc_payment.cpp
> |index 6cd52523f..e9f184030 100644
> |--- a/src/rpc/rpc_payment.cpp
> |+++ b/src/rpc/rpc_payment.cpp
> --------------------------
> File to patch: /home/pinodexmr/monero/src/rpc/rpc_payment.cpp
> patching file /home/pinodexmr/monero/src/rpc/rpc_payment.cpp
> can't find file to patch at input line 44
> Perhaps you used the wrong -p or --strip option?
> The text leading up to this was:
> --------------------------
> |diff --git a/src/rpc/rpc_payment_signature.cpp b/src/rpc/rpc_payment_signature.cpp
> |index 559f3a1e9..b2ec27817 100644
> |--- a/src/rpc/rpc_payment_signature.cpp
> |+++ b/src/rpc/rpc_payment_signature.cpp
> --------------------------
> File to patch: /home/pinodexmr/monero/src/rpc/rpc_payment_signature.cpp
> patching file /home/pinodexmr/monero/src/rpc/rpc_payment_signature.cpp
> pinodexmr@PiNodeXMR:~/monero/build/release/bin$

### Testing again results in 

2020-05-22 19:27:44.227 I Erasing <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> with 0 credits, inactive for -12041 days

2020-05-22 19:28:44.228 I Erasing <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> with 0 credits, inactive for -12774 days

2020-05-22 19:28:57.720 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> sends nonce: 594, current

2020-05-22 19:28:59.336 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> credited for 50, now 50

2020-05-22 19:30:44.229 I Erasing <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> with 0 credits, inactive for -13830 days

2020-05-22 19:31:09.974 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> credited for 50, now 50

2020-05-22 19:31:25.290 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> sends nonce: 4574, current

2020-05-22 19:31:26.804 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> credited for 50, now 149

2020-05-22 19:31:43.023 I client <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> credited for 50, now 199

2020-05-22 19:31:44.230 I Erasing <8b14107818971ee6bc275572d2deb7b33266073f54a49388178b8d93abeac4c5> with 199 credits, inactive for -14966 days

______________________________________________________________

Because I have lots of monero related commands in crontabs for getting statistics I have removed all of those to (as of about an hour ago before you made that patch). That should remove more external variables my end.

However did I apply the patch correctly?

Editing to try to remove awful formatting

## moneromooo-monero | 2020-05-22T20:52:32+00:00
Sorry, I forgot to say: please run with --log-level 0,daemon.rpc.payment:DEBUG
Most of the interesting logs for this bug aren't on by default.

## shermand100 | 2020-05-22T21:12:40+00:00
So below is a short log of that debug command. It's raw/un-edited but I'd say uneventful. 

One Error at timestamp 21:04:25.756  of:

E [192.168.1.108:51203 INC] Failed to on_get_blocks()

And two:

W Very stale nonce

I do notice though that for the short time my wallet-cli ID does own some credits, it doesn't seem to be spending them to sync the wallet. Should it be spending them more proactively?

#### The Log:

pinodexmr@PiNodeXMR:~/monero/build/release/bin$ ./monerod --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --rpc-restricted-bind-port=18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=43HoAhqx9q3MR1crAjpQtYVhvzQhZgqPwSWVQMmPvYmr18qVUEjCHcsEasuCxS486rWSSg1gbGqanet67NWRsh1bQL9KkB9 --rpc-payment-credits=50 --rpc-payment-difficulty=1000 --log-level 0,daemon.rpc.payment:DEBUG
2020-05-22 20:53:35.232 I Monero 'Carbon Chamaeleon' (v0.16.0.0-4987161fa)
2020-05-22 20:53:35.232 I Initializing cryptonote protocol...
2020-05-22 20:53:35.232 I Cryptonote protocol initialized OK
2020-05-22 20:53:35.240 I Initializing core...
2020-05-22 20:53:35.240 I Loading blockchain from folder /home/pinodexmr/.bitmonero/lmdb ...
2020-05-22 20:53:35.247 W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2020-05-22 20:54:45.410 I Loading checkpoints
2020-05-22 20:54:45.420 I Core initialized OK
2020-05-22 20:54:45.420 I Initializing p2p server...
2020-05-22 20:54:45.476 I p2p server initialized OK
2020-05-22 20:54:45.477 I Initializing core RPC server...
2020-05-22 20:54:45.484 W The RPC server is accessible from the outside, but no RPC payment was setup. RPC access will be free for all.
2020-05-22 20:54:45.484 I Binding on 0.0.0.0 (IPv4):18083
2020-05-22 20:54:45.486 I core RPC server initialized OK on port: 18083
2020-05-22 20:54:45.486 I Initializing restricted RPC server...
2020-05-22 20:54:45.488 I loading rpc payments data from /rpcpayments.bin
2020-05-22 20:54:45.488 I Binding on 0.0.0.0 (IPv4):18089
2020-05-22 20:54:45.489 I restricted RPC server initialized OK on port: 18089
2020-05-22 20:54:45.489 I Starting core RPC server...
2020-05-22 20:54:45.490 I core RPC server started ok
2020-05-22 20:54:45.491 I Starting restricted RPC server...
2020-05-22 20:54:45.492 I restricted RPC server started ok
2020-05-22 20:54:45.517 I Starting p2p net loop...
2020-05-22 20:54:46.520 I
2020-05-22 20:54:46.520 I **********************************************************************
2020-05-22 20:54:46.521 I The daemon will start synchronizing with the network. This may take a long time to complete.
2020-05-22 20:54:46.521 I
2020-05-22 20:54:46.522 I You can set the level of process detailization through "set_log <level|categories>" command,
2020-05-22 20:54:46.523 I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2020-05-22 20:54:46.523 I
2020-05-22 20:54:46.524 I Use the "help" command to see a simplified list of available commands.
2020-05-22 20:54:46.524 I Use the "help_advanced" command to see an advanced list of available commands.
2020-05-22 20:54:46.525 I Use "help_advanced <command>" to see a command's documentation.
2020-05-22 20:54:46.526 I **********************************************************************
2020-05-22 20:54:47.499 I
2020-05-22 20:54:47.500 I **********************************************************************
2020-05-22 20:54:47.500 I You are now synchronized with the network. You may now start monero-wallet-cli.
2020-05-22 20:54:47.501 I
2020-05-22 20:54:47.501 I Use the "help" command to see a simplified list of available commands.
2020-05-22 20:54:47.501 I Use the "help_advanced" command to see an advanced list of available commands.
2020-05-22 20:54:47.501 I **********************************************************************
2020-05-22 20:54:48.218 I [72.176.56.185:18080 OUT] Sync data returned a new top block candidate: 2104140 -> 2104141 [Your node is 1 blocks (2.0 minutes) behind]
2020-05-22 20:54:48.218 I SYNCHRONIZATION started
2020-05-22 20:55:00.315 I Synced 2104141/2104142 (99%, 1 left)
2020-05-22 20:55:00.317 I [34.221.218.73:18080 OUT] Sync data returned a new top block candidate: 2104141 -> 2104142 [Your node is 1 blocks (2.0 minutes) behind]
2020-05-22 20:55:00.318 I SYNCHRONIZATION started
2020-05-22 20:55:12.743 I Synced 2104142/2104142
2020-05-22 20:55:12.745 I SYNCHRONIZED OK
2020-05-22 20:55:12.774 I SYNCHRONIZED OK
2020-05-22 20:55:51.447 D Not enough credits: 0 < 1
2020-05-22 20:55:56.390 D Not enough credits: 0 < 1
2020-05-22 20:56:18.017 D Not enough credits: 0 < 1
2020-05-22 20:56:45.488 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 0 credits, inactive for -24375 days
2020-05-22 20:57:08.617 D Not enough credits: 0 < 1
2020-05-22 20:57:13.766 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 459, current
2020-05-22 20:57:15.306 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 20:57:22.926 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 1165, current
2020-05-22 20:57:24.506 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 100
2020-05-22 20:57:27.523 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 1433, current
2020-05-22 20:57:29.092 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 150
2020-05-22 20:57:42.369 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 2674, current
2020-05-22 20:57:43.935 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 200
2020-05-22 20:57:45.489 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 200 credits, inactive for 24749 days
2020-05-22 20:57:56.637 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 3846, current
2020-05-22 20:57:58.103 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 20:57:58.166 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 20:58:00.118 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 4026, current
2020-05-22 20:58:01.585 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 99
2020-05-22 20:58:45.490 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 99 credits, inactive for 24175 days
2020-05-22 21:00:00.250 D Not enough credits: 0 < 1
2020-05-22 21:00:14.129 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 6139, current
2020-05-22 21:00:15.674 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:00:15.738 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:00:34.045 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 7847, current
2020-05-22 21:00:35.671 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 99
2020-05-22 21:00:45.490 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 99 credits, inactive for 22583 days
2020-05-22 21:00:50.063 W Very stale nonce
2020-05-22 21:00:50.242 D Not enough credits: 0 < 1
2020-05-22 21:00:51.038 W Very stale nonce
2020-05-22 21:00:51.074 D Not enough credits: 0 < 1
2020-05-22 21:00:58.912 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 9941, current
2020-05-22 21:01:00.393 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:01:00.454 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:01:02.599 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 10131, current
2020-05-22 21:01:04.064 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 99
2020-05-22 21:01:04.767 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 10192, current
2020-05-22 21:01:06.225 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 149
2020-05-22 21:01:14.799 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 10988, current
2020-05-22 21:01:16.376 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 199
2020-05-22 21:01:18.039 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 11133, current
2020-05-22 21:01:19.499 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 249
2020-05-22 21:01:31.468 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_transaction_pool_hashes, 248 left
2020-05-22 21:01:31.502 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 11 for get_transactions, 237 left
2020-05-22 21:01:31.612 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_blocks, 236 left
2020-05-22 21:01:45.113 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 50 for get_blocks, 186 left
2020-05-22 21:01:45.491 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 186 credits, inactive for 21705 days
2020-05-22 21:02:14.741 D Not enough credits: 0 < 1
2020-05-22 21:02:21.296 D Not enough credits: 0 < 1
2020-05-22 21:02:27.952 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 12286, current
2020-05-22 21:02:29.605 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:02:33.194 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 12616, current
2020-05-22 21:02:34.747 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 100
2020-05-22 21:02:44.465 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 13511, current
2020-05-22 21:02:45.973 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 150
2020-05-22 21:02:45.973 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 150 credits, inactive for 21131 days
2020-05-22 21:02:49.295 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 13806, current
2020-05-22 21:02:50.922 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:03:14.355 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 15992, current
2020-05-22 21:03:15.972 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 100
2020-05-22 21:03:16.024 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 99 left
2020-05-22 21:03:16.578 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 16032, current
2020-05-22 21:03:18.040 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 149
2020-05-22 21:03:20.939 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 16301, current
2020-05-22 21:03:22.401 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 199
2020-05-22 21:03:45.975 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 199 credits, inactive for 20497 days
2020-05-22 21:03:47.728 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 18642, current
2020-05-22 21:03:49.185 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:03:49.244 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:04:00.816 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_transaction_pool_hashes, 48 left
2020-05-22 21:04:00.856 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 19 for get_transactions, 29 left
2020-05-22 21:04:01.010 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_blocks, 28 left
2020-05-22 21:04:10.416 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 27 for get_blocks, 1 left
2020-05-22 21:04:25.755 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_blocks, 0 left
2020-05-22 21:04:25.756 E [192.168.1.108:51203 INC] Failed to on_get_blocks()
2020-05-22 21:04:45.975 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 0 credits, inactive for 19690 days
2020-05-22 21:06:57.778 D Not enough credits: 0 < 1
2020-05-22 21:07:23.250 D Not enough credits: 0 < 1
2020-05-22 21:07:33.166 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 20161, current
2020-05-22 21:07:34.641 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:07:34.693 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:07:45.977 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 49 credits, inactive for 17503 days
2020-05-22 21:09:02.248 D Not enough credits: 0 < 1
2020-05-22 21:09:14.277 D Not enough credits: 0 < 1
2020-05-22 21:09:22.640 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 21389, current
2020-05-22 21:09:24.249 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:09:24.307 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:09:45.978 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 49 credits, inactive for 16234 days
2020-05-22 21:10:00.880 D Not enough credits: 0 < 1
2020-05-22 21:10:15.226 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> sends nonce: 22676, current
2020-05-22 21:10:16.765 I client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> credited for 50, now 50
2020-05-22 21:10:16.817 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_info, 49 left
2020-05-22 21:10:42.247 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_transaction_pool_hashes, 48 left
2020-05-22 21:10:42.294 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 23 for get_transactions, 25 left
2020-05-22 21:10:42.593 D client <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> paying 1 for get_blocks, 24 left
2020-05-22 21:10:45.979 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 24 credits, inactive for 15328 days
2020-05-22 21:10:51.024 D Not enough credits: 0 < 23
2020-05-22 21:11:45.979 I Erasing <0c73aa35fc139dd8a4d0bad545b3a2b2454278cddb1b908c8b3c696ee6e7af1a> with 0 credits, inactive for 15328 days
2020-05-22 21:12:01.104 D Not enough credits: 0 < 1



## moneromooo-monero | 2020-05-22T21:35:25+00:00
The patch does not seem to have been applied.

## shermand100 | 2020-05-22T21:42:02+00:00
That's inconvenient as I copy/pasted the output and once I resolved the file paths it seemed happy.

I'm happy to re-install your version of monero again with the two edited .cpp files? 
It will take about 4 hours to compile if I do that.

Or I can try and re-apply the same patch again?

Edit: Re-reading that this morning sounded as if my tone was off. What I mean is that it's inconvenient when these things don't perform as expected, but I'm happy to keep pursuing/testing solutions when required. I hope it's not too complicated a fix.

Can the edit from the patch be added manually?

## moneromooo-monero | 2020-05-22T22:05:43+00:00
I pushed the patch to the https://github.com/moneromooo-monero/bitmonero/commits/rpl branch now. You can copy src/rpc/rpc_payment.* from that branch.

## shermand100 | 2020-05-31T18:26:32+00:00
This seems to have solved it. Thank you.

Sorry for the delay. Until I checked today I wasn't aware of your last message for some reason.

So I compiled Monero again with your patch to the two files this morning and it has been successfully running for several hours without issue this afternoon.

- Credits no longer erase.
- Wallet through RPC mining payments has synchronised with the node

I can see the fix performing the update_time function each minute.

> 2020-05-31 18:24:21.380 I now 1590949461, t 1590949423, last_request_timestamp 1590949423583180, update_time 1590949421, erase 0, bounds -2147483648 2147483647

I will leave it running to reach it's mining/credit target, and for a few days after but all seems good.

Thanks again.

## moneromooo-monero | 2020-05-31T18:44:25+00:00
Thanks for the logs.
So the reason is your time_t is signed 32 bits. This is a bit unexpected and you're gonna have some surprises in 2038 if you're still running that by then.

## shermand100 | 2020-05-31T21:09:07+00:00
Right, that makes sense for the wild difference in time before this fix.

My last question regarding this before I think this can be closed would be about the application of this fix. Are the two files you made changes to likely to get worked into the master Monero release?
Or are the files 32bit exclusive and so their inclusion would break Monero builds on 64bit systems?

If they are 32bit exclusive then for context you may recognise my username from the PiNodeXMR project and I'm asking this because I have quite a few users looking forward to running their nodes on single board computers (SBC) with the RPC_pay flag. The project as of recently allows builds on any Armbian supported SBCs (not just Raspberry Pis) however an official Armbian 64bit OS isn't always available even though the board has 64bit architecture (in the case of some Odroids), so they may take a couple of years to catch up.

As a work around now there is this fix I could tweak my install scripts to detect a 32bit OS and so pull in your files before building Monero? If this can't be worked into the master Monero release?

## moneromooo-monero | 2020-05-31T22:21:26+00:00
The patch will be merged to master. In the meantime, you can certainly apply this patch to anything that might need it.

## shermand100 | 2020-05-31T22:48:21+00:00
Will do, and thanks again for the fix.



# Action History
- Created by: shermand100 | 2020-05-17T22:56:15+00:00
- Closed at: 2020-05-31T22:48:21+00:00
