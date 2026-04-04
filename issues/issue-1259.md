---
title: Offline transaction signing doesn't seem to work
source_url: https://github.com/monero-project/monero/issues/1259
author: rndbr
assignees: []
labels: []
created_at: '2016-10-25T13:52:45+00:00'
updated_at: '2017-01-01T14:49:06+00:00'
type: issue
status: closed
closed_at: '2016-12-10T20:06:55+00:00'
---

# Original Description
Having issues submitting a transaction that was signed offline, using the new offline signing functionality. Am using code from the latest master (as of Oct 24ish — `v0.10.0.0-18e406a`). 

Logs (monerod, log level 3):

```
set_log 3
2016-Oct-25 09:47:06.955975 Log level is now 3
Log level is now 3
dbg    info   {2} {p1} 2016-10-25 09:47:09.689121 [utils.cpp+526 ::Thread2Number] This is a new thread (used in debug), thread id=7f512def9700

{2} {p1} 2016-10-25 09:47:09.689090 [network_throttle-detail.cpp+327 ::calculate_times] dbg <<< global-IN: speed is A=5.58791e+06 vs Max=8.58993e+09  so sl
eep: D=-9.13305 sec E=51067904 (Enow=51067937) M=8.58993e+09 W=   9.139 R=7.84523e+10 Wgood      11 History: [33792 0 0 50864128 92160 33792 0 44032 0 0 ]
m_last_sample_time=1.17426e+07

dbg    {2} {p1} 2016-10-25 09:47:09.774928 [network_throttle-detail.cpp+327 ::calculate_times] dbg <<< global-IN: speed is A=5.54581e+06 vs Max=8.58993e+09
  so sleep: D=-9.21904 sec E=51160064 (Enow=51160154) M=8.58993e+09 W=   9.225 R=7.9191e+10 Wgood      11 History: [125952 0 0 50864128 92160 33792 0 44032
 0 0 ] m_last_sample_time=1.17426e+07

2016-Oct-25 09:47:09.775005 [P2P6]Blockchain::have_block
2016-Oct-25 09:47:09.775039 [P2P6]BlockchainLMDB::block_exists
2016-Oct-25 09:47:09.775050 [P2P6]BlockchainLMDB::check_open
2016-Oct-25 09:47:09.775065 [P2P6]BlockchainLMDB::block_rtxn_start
2016-Oct-25 09:47:09.775084 [P2P6]mdb_txn_safe: destructor
2016-Oct-25 09:47:09.775106 [P2P6]block exists in main chain
2016-Oct-25 09:47:09.775127 [P2P6]Blockchain::get_tail_id
2016-Oct-25 09:47:09.775142 [P2P6]BlockchainLMDB::height
2016-Oct-25 09:47:09.775149 [P2P6]BlockchainLMDB::check_open
2016-Oct-25 09:47:09.775160 [P2P6]Blockchain::get_tail_id
2016-Oct-25 09:47:09.775168 [P2P6]BlockchainLMDB::top_block_hash
2016-Oct-25 09:47:09.775175 [P2P6]BlockchainLMDB::check_open
2016-Oct-25 09:47:09.775187 [P2P6]BlockchainLMDB::get_block_hash_from_height
2016-Oct-25 09:47:09.775195 [P2P6]BlockchainLMDB::check_open
2016-Oct-25 09:47:09.775207 [P2P6]BlockchainLMDB::block_rtxn_start
2016-Oct-25 09:47:09.775219 [P2P6]mdb_txn_safe: destructor
2016-Oct-25 09:47:09.775235 [P2P6][82.120.98.94:18080 OUT]COMMAND_TIMED_SYNC
dbg    {2} {p1} 2016-10-25 09:47:09.775328 [network_throttle-detail.cpp+327 ::calculate_times] dbg >>> global-OUT: speed is A=  572065 vs Max=4.50972e+09
so sleep: D=-9.22383 sec E= 5277300 (Enow= 5278829) M=4.50972e+09 W=   9.225 R=4.15968e+10 Wgood      11 History: [0 0 0 0 5277300 0 0 0 0 0 ] m_last_sampl
e_time=1.17426e+07

dbg    {2} {p1} 2016-10-25 09:47:09.775468 [abstract_tcp_server2.inl+543 ::do_send_chunk] do_send() NOW SENSD: packet=1529 B

dbg    {2} {p1} 2016-10-25 09:47:09.775531 [network_throttle-detail.cpp+327 ::calculate_times] dbg >>> global-OUT: speed is A=  688012 vs Max=4.50972e+09
so sleep: D=-9.22459 sec E= 6347600 (Enow= 6349129) M=4.50972e+09 W=   9.226 R=4.16003e+10 Wgood      11 History: [1070300 0 0 0 5277300 0 0 0 0 0 ] m_last
_sample_time=1.17426e+07

info   {2} {p1} 2016-10-25 09:47:09.775577 [connection_basic.cpp+283 ::do_send_handler_write] handler_write (direct) - before ASIO write, for packet=1529 B
 (after sleep)

dbg    {2} {p1} 2016-10-25 09:47:09.775656 [network_throttle-detail.cpp+327 ::calculate_times] dbg >>> global-OUT: speed is A=  804021 vs Max=4.50972e+09
so sleep: D=-9.22436 sec E= 7417900 (Enow= 7419429) M=4.50972e+09 W=   9.226 R=4.15992e+10 Wgood      11 History: [2140600 0 0 0 5277300 0 0 0 0 0 ] m_last
_sample_time=1.17426e+07

2016-Oct-25 09:47:17.820137 [RPC0]-->>simple_http_connection_handler<t_connection_context>::handle_recognize_protocol_out(*)
2016-Oct-25 09:47:17.820256 [RPC0]<<--simple_http_connection_handler<t_connection_context>::handle_recognize_protocol_out(*)
2016-Oct-25 09:47:17.820294 [RPC0]-->>simple_http_connection_handler<t_connection_context>::analize_cached_request_header_and_invoke_state(*)
2016-Oct-25 09:47:17.820323 [RPC0]-->>http_stream_filter::parse_cached_header(*)
2016-Oct-25 09:47:17.820353 [RPC0]<<--http_stream_filter::parse_cached_header(*)
2016-Oct-25 09:47:17.820375 [RPC0]<<--simple_http_connection_handler<t_connection_context>::analize_cached_request_header_and_invoke_state(*)
2016-Oct-25 09:47:17.857680 [RPC1]HTTP [127.0.0.1] GET /json_rpc
2016-Oct-25 09:47:17.857836 [RPC1]/json_rpc[get_version] processed with 0/0/0ms
2016-Oct-25 09:47:17.857873 [RPC1]HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 96
Content-Type: application/json
Last-Modified: Tue, 25 Oct 2016 13:47:17 GMT
Accept-Ranges: bytes


dbg    info   {3} {p1} 2016-10-25 09:47:17.858343 [utils.cpp+526 ::Thread2Number] This is a new thread (used in debug), thread id=7f513f9e7700

{3} {p1} 2016-10-25 09:47:17.858305 [abstract_tcp_server2.inl+543 ::do_send_chunk] do_send() NOW SENSD: packet=159 B

info   {3} {p1} 2016-10-25 09:47:17.858588 [abstract_tcp_server2.inl+528 ::do_send_chunk] do_send() NOW just queues: packet=96 B, is added to queue-size=2

dbg    {3} {p1} 2016-10-25 09:47:17.858651 [abstract_tcp_server2.inl+638 ::handle_write] handle_write() NOW SENDS: packet=96 B, from  queue size=1

2016-Oct-25 09:47:19.574203 [RPC0]-->>simple_http_connection_handler<t_connection_context>::handle_recognize_protocol_out(*)
2016-Oct-25 09:47:19.574294 [RPC0]<<--simple_http_connection_handler<t_connection_context>::handle_recognize_protocol_out(*)
2016-Oct-25 09:47:19.574319 [RPC0]-->>simple_http_connection_handler<t_connection_context>::analize_cached_request_header_and_invoke_state(*)
2016-Oct-25 09:47:19.574338 [RPC0]-->>http_stream_filter::parse_cached_header(*)
2016-Oct-25 09:47:19.574367 [RPC0]<<--http_stream_filter::parse_cached_header(*)
2016-Oct-25 09:47:19.574388 [RPC0]<<--simple_http_connection_handler<t_connection_context>::analize_cached_request_header_and_invoke_state(*)
2016-Oct-25 09:47:19.613637 [RPC1]HTTP [127.0.0.1] GET /sendrawtransaction
2016-Oct-25 09:47:19.613771 [RPC1]Blockchain::get_current_cumulative_blocksize_limit
2016-Oct-25 09:47:19.613793 [RPC1]Blockchain::have_tx
2016-Oct-25 09:47:19.613804 [RPC1]BlockchainLMDB::tx_exists
2016-Oct-25 09:47:19.613814 [RPC1]BlockchainLMDB::check_open
2016-Oct-25 09:47:19.613841 [RPC1]BlockchainLMDB::block_rtxn_start
2016-Oct-25 09:47:19.613860 [RPC1]transaction with hash 8673f4be0e2ca402eba50b8a582621db535b5512798f7e3d79d0419501cf3893 not found in db
2016-Oct-25 09:47:19.613868 [RPC1]mdb_txn_safe: destructor
2016-Oct-25 09:47:19.613876 [RPC1]PERF             ----------
2016-Oct-25 09:47:19.613885 [RPC1]Blockchain::check_tx_outputs
2016-Oct-25 09:47:19.613895 [RPC1]Transaction with id= <8673f4be0e2ca402eba50b8a582621db535b5512798f7e3d79d0419501cf3893> has at least one invalid output
2016-Oct-25 09:47:19.613907 [RPC1]PERF        0    add_tx
2016-Oct-25 09:47:19.613914 [RPC1]Transaction verification failed: <8673f4be0e2ca402eba50b8a582621db535b5512798f7e3d79d0419501cf3893>
2016-Oct-25 09:47:19.613924 [RPC1][on_send_raw_tx]: tx verification failed
2016-Oct-25 09:47:19.613944 [RPC1]/sendrawtransaction processed with 0/0/0ms
2016-Oct-25 09:47:19.613958 [RPC1]HTTP_RESPONSE_HEAD: <<
HTTP/1.1 200 Ok
Server: Epee-based
Content-Length: 275
Content-Type: application/json
Last-Modified: Tue, 25 Oct 2016 13:47:19 GMT
Accept-Ranges: bytes


dbg    {3} {p1} 2016-10-25 09:47:19.614003 [abstract_tcp_server2.inl+543 ::do_send_chunk] do_send() NOW SENSD: packet=160 B

info   {3} {p1} 2016-10-25 09:47:19.614114 [abstract_tcp_server2.inl+528 ::do_send_chunk] do_send() NOW just queues: packet=275 B, is added to queue-size=2

dbg    {3} {p1} 2016-10-25 09:47:19.614151 [abstract_tcp_server2.inl+638 ::handle_write] handle_write() NOW SENDS: packet=275 B, from  queue size=1
```

I've reproduced this twice on mainnet using the following steps:
- Generate a new address offline (using moneromooo’s offline wallet generator)
- Send 5 XMR to that address from poloniex (ended up being 5.05 XMR with polo’s fee)
- On the offline box (running the same version of monero) launch monero-wallet-cli (no monerod) as a deterministic wallet import, and enter the 25 word phrase
- On the online box, create a view wallet from the viewkey and address
- On online box run transfer command to send 1 XMR back to poloniex, with the specific payment ID they assign (i.e. `transfer <address> 1.0 <paymentID>`)
- Sign the resulting file on the offline box (i.e. using `sign_transfer`)
- Run `submit_transfer` on the online box
- The above error is returned

This is from a test address, and I'd be happy to get the address and viewkey to moneromooo if he needs it.


# Discussion History
## moneromooo-monero | 2016-10-25T20:22:34+00:00
I think https://github.com/monero-project/monero/pull/1261 fixes it, if you want to try.
The problem was that change wasn't being split, which is forbidden pre-rct.


## rndbr | 2016-10-25T20:39:00+00:00
Thanks, I'll try it out shortly.

Is there a way to spit out an in-depth assessment of the signed transaction before it is broadcast to the network (in `submit_transfer`), similar to what `sign_transfer` shows (or, even more in-depth, like a tool like https://blockchain.info/decode-tx does for raw bitcoin transactions, where change outputs, etc are shown)? That would be very useful in order to more fully confirm what a transaction will actually end up doing before finally broadcasting it out.


## moneromooo-monero | 2016-10-25T20:49:45+00:00
Sure, but that'd be running on the potentially pwned wallet, so you can't trust it anyway.


## moneromooo-monero | 2016-10-25T20:50:23+00:00
Also, note that I've just pushed an update, in case you pulled earlier.


## rndbr | 2016-10-25T20:58:07+00:00
I would guess one option would be to reprint out the same statement with `submit_transfer` that `sign_transfer` printed. And, yes, technically one couldn't trust that due to the potential for a pwned wallet. However, I see the risks as not only that, but with simple bugs as well, and in that way the feature would be useful I think.

The other option would be to have a separate utility (or `monero-wallet-cli` command) that would perform a verbose printout of the data of any (signed or unsigned) transaction file. one could call it from either/both the offline and online wallets...that would be super useful...does that feature exist anywhere?


## moneroexamples | 2016-10-25T21:27:56+00:00
> The other option would be to have a separate utility (or monero-wallet-cli command) that would perform a verbose printout of the data of any (signed or unsigned) transaction file. one could call it from either/both the offline and online wallets...that would be super useful...does that feature exist anywhere?

Yes. Monero transaction pusher lets you check  tx details of unsigned and signed data file.


## moneromooo-monero | 2016-10-25T22:08:04+00:00
I can trivially dump the JSON for the txes to the log. Guess it can't hurt.


## rndbr | 2016-10-25T22:12:16+00:00
+1 (especially since I can't find the "monero transaction pusher" and folks on IRC don't know where it is either)

at what point(s) would you dump it to the logs? optimally it would be before broadcasting it, so I could confirm the details before signing (online and/or offline box), after signing (offline box), and before broadcasting (online box).... that, or add something like an `examine_transfer` command?


## moneromooo-monero | 2016-10-25T22:25:27+00:00
done (and it's done just before the submit_transfer prompt, assuming you have the always-confirm-transfers option set). Before signing, there's no actual tx. The cold wallet creates the tx, rather than sign one made by the view wallet.


## moneroexamples | 2016-10-26T12:03:23+00:00
@rndbr 

Should have been more clear, sorry. Its a hidden service, only for tor users. Thus you cant easily find it. But its open sourced (https://github.com/moneroexamples/onion-monero-blockchain-explorer as part of the explorer) so you can run it yourself, if you are not tor user. Some screenshots how checking unsigned and signed ringct tx data files from testnet look like: http://imgur.com/a/6d0Am

Unsigned and signed tx data used in the screenshots:
http://pastebin.com/Mt2x8xHX
http://pastebin.com/Sk3W0WEV

Just in case: the pusher was updated to recent pull requiest: #1261 Thus, it wont work if transactions files are created without it.

Hope this helps


## moneromooo-monero | 2016-10-30T20:54:40+00:00
There is now a import/export outputs command pair that allows a cold wallet to learn about outputs received. That makes cold wallet usage less surprising.
submit_transfer now also prints out the transaction overview (not trustable if compromised)


## rndbr | 2016-10-31T21:36:13+00:00
great...so with the new export_outputs command, what is the proper procedure for generating and signing an offline transaction (where everything such as balances, etc "just works" as one would intuitively expect)? Is it:

Part 1 (**on hot wallet**):
- Run `export_outputs`
- Run `transfer` to generate the `unsigned_monero_tx`
- Copy both files (exported outputs and unsigned tx file) to USB key and transfer to cold wallet

Part 2 (**on cold wallet**):
- Run `import_outputs`
- Run `sign_transfer`
- Run `export_key_images`
- Copy `signed_monero_tx` and exported key images on USB key and transfer back to hot wallet

Part 3 (**on hot wallet**):
- Run `import_key_images`
- Run `submit_transfer`

If so, can we talk about how to collapse it down to a single command that exports a single file in part 1 that contains all the necessary details, and another single command that exports a single file in part 2? Or some other way to improve usability for the offline signing usecase? (e.g. with armory offline signing on bitcoin, for instance, it's just a single file)


## moneromooo-monero | 2016-11-02T14:52:52+00:00
That should work. I envisioned it as:

When you want to get a set of key images from the outputs, you do the export_outputs/import_outputs/export_key_images/import_key_images step.

When you want to transfer, you do the transfer/sign_transfer_submit transfer step.

Now, it is true that the transfer will create change, for which you need a key image, and you might want to update key images in the hot wallet. But you don't have to. But it's a good point that people might want to, just because. I'll think about it. Maybe optionally return the premade key images in the signed transfer data file.


## rndbr | 2016-11-02T15:26:17+00:00
@moneromooo-monero agreed that those steps are technically optional for an offline transfer operation, but speaking as a regular monero user (and bitcoin power user), I think it would be super helpful to provide an option to include the most recent outputs in the `unsigned_monero_tx` file, and the most recent key images in the `signed_monero_tx` file, and enhance the `sign_transaction` and `submit_transaction` commands to import the relevant data if it exists in the respective files.

IMO, this will allow an offline transfer operation to be as intuitive as possible -- i.e. when I perform a transfer, I assume (both intuitively/naively, and being a user of software such as offline armory, trezor, etc) that balances/outputs/etc will naturally be kept in sync and continue to update properly by virtue of the `transfer, sign_transfer, submit_transfer` process, and that additional fiddling is not necessary. Plus, including that information allows the process to be more streamlined: less commands, less time, less files, less complexity, less chance of error or newb problems that waste valuable support and dev time. :) 

The `transfer` command could include an optional flag to either enable or disable this 'all-in-one' export when used on a view wallet...maybe enable it by default as it aids regular users, doesn't seem to compromise privacy, and power users that want the fine grained control can disable the extra functionality if they desire. alternatively, one could not "clutter" the `transfer` and `sign_transfer` commands with this optional flag, and instead use a command-line flag to `monero-wallet-cli` that disabled the "all-in-one" exports for any `transfer/sign_transfer` commands launched in the subsequent wallet shell.


## moneromooo-monero | 2016-11-04T23:32:24+00:00
I was thinking about this. If I were to include key images for change, it would still be missing any potential new outputs received since last export_key_images call anyway, and this would have to be done. Including key images for change would help in the case where no payments are received, but otherwise not. I guess I'm a bit unsold on the idea. I see the point, and it does help, but is only partial.


## rndbr | 2016-11-09T21:30:19+00:00
But isn't that the case with the full, multi-step procedure as well? i.e. if you did all that as multiple steps, you still have files that can become out of date if the address/PK gets more transactions.

I envision the normal use-case for this (and my use-case as well) is someone that has a simple cold wallet that only they are sending and receiving from, and is sending to and from it in a serial (i.e. non-parallel) fashion. For example, one weekday they send 2K XMR to it from the exchange, and then a few weeks later as the XMR price goes up, they withdraw 1K XMR from the wallet to the exchange to sell. If you agree with this "average usecase" probably being a large fraction (majority) of XMR user cold wallet operations (based on our experience with and knowledge of offline wallet usage of other cryptocurrencies such as bitcoin and ethereum), I would make the case further that if there is something simple that can be done to drastically make the feature more noob friendly towards this use-case, then we should strongly consider it.

If you doubt that that is the most common use-case for this feature, I'd be happy to help gather user feedback to confirm or deny this hypothesis.

And in any case, I wanted to reiterate my appreciation for your work on this feature. :)


## moneromooo-monero | 2016-11-10T21:35:05+00:00
Yes, that makes sense. The files would have to include "everything", basically.
On my test wallet, the outputs set file is 25 MB, and the key images set file is 500 kB. That's a lot to add to the transactions files. I could keep a record of what was sent, but if you save something and end up forgetting to load it, or save twice, you end up with bad state.


## rndbr | 2016-11-11T14:23:19+00:00
hmm....yeah, agreed that keeping a record of what was sent is probably too error prone. Your case I'd definitely say was an outlier, given what I'd assume was a ton of transactions that it has....what might you think the "average" sizes of this data would be? (i.e. consider someone who has maybe 10-20 transactions to and 10-20 transactions from their cold wallet address, with default mixin).... and is this data already compressed in the files? Any idea how well it compresses?


## moneromooo-monero | 2016-11-13T12:29:28+00:00
It's probably a large wallet, yes. But likely nowhere as large as Poloniex's, say.

Size is 64 bytes per key image, and unknown per output, but this includes the tx that go with it, so there is some redundancy there.


## rndbr | 2016-11-14T14:21:37+00:00
Since the actual bug issues here have been resolved (save the scanning bug which is addressed in its own ticket #1339) I think we can close this issue until we get more feedback on the offline signing feature. I'd keep a simplified signing format in the back of your head, it would be cool to see :)


## moneromooo-monero | 2016-11-15T19:56:19+00:00
I've got something like that locally now. I'll probably push in a day or two if you want to test :)


## moneromooo-monero | 2016-11-15T21:26:35+00:00
https://github.com/moneromooo-monero/bitmonero/tree/rider

Please test and let me know if something's missing, or not updating properly, etc.

The inclusion of this data with the cold signing files will likely be made optional with a wallet setting soon.


## rndbr | 2016-11-16T21:28:29+00:00
Super cool! I did a simple test with a test wallet that had one input. A few minor nits:
- When submitting the signed transaction, I'm asked to confirm twice in a row:

```
Loaded 1 transactions, for XXXXXX YYYY ZZZZ, with min mixin 4. 1 key images to import. Is this okay? (Y/Yes/N/No)y
The transaction fee is 0.002000000000.
Full transaction details are available in the log file
Is this okay?  (Y/Yes/N/No)y
```
- Might be a good idea to show the payment ID on that confirmation message, if one is specified.
- Super minor nit: Put a space after the confirmation prompt, so any 'y' or 'n' entered has a space before it.

Past that, seemed to work fine....the balance seem to properly update on the wallet CLI...the transaction looks good in the Tor block explorer.

I see the PR is outstanding. Once it's pushed to master, I'll try making additional transfers of progressively larger amounts.


## moneromooo-monero | 2016-11-17T20:56:35+00:00
Thanks for testing.
This got merged now.
As for payment id, at this rate I'll end up printing everything in the tx, and it just happens it's already dumped in the log file. Do you see anything else that might be good to print apart from that ?


## rndbr | 2016-11-18T18:07:53+00:00
Not really. However, the confirmation prompt assumes knowledge of TXOs, e.g.:

`Loaded 1 transactions, for 5.000000000000, fee 0.002000000000, sending 0.750000000000 to ADDRESS1, 4.248000000000 change to ADDRESS2, with min mixin 4. 1 key images to import. Is this okay? (Y/Yes/N/No)y`

That 5.000 part could be confusing to many users (i.e. they think the program is sending that, when in reality it's just spending a 5 XMR input). Perhaps modify the wording to be more like:

`Loaded 1 transaction(s), sending 0.75 XMR to ADDRESS1, sending 4.248 XMR as change [back to?] to ADDRESS2, with min mixin 4. Using 1 5.0 XMR input for the operation, and also importing 1 key image(s). Is this okay? (Y/Yes/N/No)y`

You'll notice the modified wording, as well as the stripping of excess zeros at the end....I guess the whole thing is pretty technical anyhow, but something like the above format may be more clear for most users...?


## moneromooo-monero | 2016-11-23T21:00:30+00:00
#1369 has a fix for bad change/fee being reported in show_transfers, and removes the double prompt. No further changes for now, low priority.

## rndbr | 2016-12-10T20:06:54+00:00
thanks for you work on this. closing this item as offline transaction signing now seems to work pretty well!

## xmrdog | 2017-01-01T14:48:18+00:00
@rndbr @moneromooo-monero 

This is about rndbr's instructions for offline signing, earlier in this thread: https://github.com/monero-project/monero/issues/1259#issuecomment-257427673

Can you explain to me why `export_outputs`, `import_outputs`, `export_key_images`, and `import_key_images ` are required steps? Why is doing only `transfer`, `sign_transfer`, and `submit_transfer` not enough?

The process looks really complicated. Any plans to simplify it as it is with Bitcoin Armory? In Armory just one file needs to be transferred from hot to cold, and one file from cold to hot. Much simpler.

# Action History
- Created by: rndbr | 2016-10-25T13:52:45+00:00
- Closed at: 2016-12-10T20:06:55+00:00
