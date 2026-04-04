---
title: Non-RingCT outputs fail to mix when blackballs are present
source_url: https://github.com/monero-project/monero/issues/4233
author: jamespic
assignees: []
labels: []
created_at: '2018-08-07T16:09:55+00:00'
updated_at: '2018-09-21T19:08:57+00:00'
type: issue
status: closed
closed_at: '2018-09-21T19:08:57+00:00'
---

# Original Description
(This was first identified in [this Reddit thread](https://www.reddit.com/r/Monero/comments/8r6eef/safely_splitting_monero_originalclassiczerolegacy/e3llfyo))

When attempting to send pre-RingCT outputs with certain (common) denominations, and an up-to-date blackball list (such as the one at https://s3.amazonaws.com/monero-legacy-blackball/blackballs.gz), some outputs fail to be mixed. The following is an except from a log of an attempt to send a transaction with a pre-RingCT output worth 3.0XMR.

```
2018-08-05 23:47:29.365	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6299	Looking for 7 outputs of size 3.000000000000
2018-08-05 23:47:29.365	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1243/11: idx 190299 (real [redacted]), unlocked 1, key <0a8ff499c69b5e960673a85cf5039288be5cf9caf9149e4029c30dc74daa2f98>
2018-08-05 23:47:29.366	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1244/11: idx 233929 (real [redacted]), unlocked 1, key <69f1add6ae122568c4590a9767baa89bcac51443bc579db283e1da74bf97b5ba>
2018-08-05 23:47:29.366	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1245/11: idx 255397 (real [redacted]), unlocked 1, key <ac57bcf57502438b385ca490561715414a50344052ff365f987a6ba7b800e73e>
2018-08-05 23:47:29.367	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1236/11: idx 129437 (real [redacted]), unlocked 1, key <bec0ecd78ab3c9d43c120cbad99471fed50b2222aa41bacd311c1a1ed22192f3>
2018-08-05 23:47:29.367	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1242/11: idx 189049 (real [redacted]), unlocked 1, key <63af4349c29129700c2a08f16c8bae49377eb22ee973dca7f6882fe479559f7d>
2018-08-05 23:47:29.368	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1238/11: idx 158488 (real [redacted]), unlocked 1, key <61c5969546e357229d4c82b2241a8e24cf1c5710a5c984e09ee08635e448e59e>
2018-08-05 23:47:29.369	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1241/11: idx 181400 (real [redacted]), unlocked 1, key <101bac30bf5fb99f6ba7a4fe94e06f33e7a1bd756392a63053f19cf2fd85c0ab>
2018-08-05 23:47:29.370	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1235/11: idx 127438 (real [redacted]), unlocked 1, key <ce26799f4662c50cb91dd258195459c6b8a1d118e15f96bfbcfb7db61054e9d9>
2018-08-05 23:47:29.370	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1240/11: idx 178148 (real [redacted]), unlocked 1, key <05f9ff6595ed907300bc5271a873441553c33f5e5dfd024fce54cf96c1f44773>
2018-08-05 23:47:29.371	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1237/11: idx 154632 (real [redacted]), unlocked 1, key <471ca983346c68e3f6fc75147edf7d394df71da9d61bcc22c61fbda7cd7cf7b4>
2018-08-05 23:47:29.371	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6303	Index 1239/11: idx 158650 (real [redacted]), unlocked 1, key <db985e283b6cc62989fd3f99dbe4a9ef8a75b5fe1ebd8af7cf82b16128b728dd>
2018-08-05 23:47:29.372	  0x7fffa8904380	ERROR	wallet.wallet2	src/wallet/wallet2.cpp:6317	!scanty_outs.empty(). THROW EXCEPTION: error::not_enough_outs_to_mix
2018-08-05 23:47:29.372	  0x7fffa8904380	WARN 	net.http	src/wallet/wallet_errors.h:794	/DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:6317:N5tools5error22not_enough_outs_to_mixE: not enough outputs to use, ring size = 7, scanty_outs:
3.000000000000 - 1
```

Monero Wallet CLI requests 11 outputs (based on the calculation of `requested_output_count`), however 10 of them are blackballed (which is a common problem with pre-RingCT outputs, since many used zero decoys), and it is unable to form a ring of size 7. This results in a recommendation to the user to use `sweep_unmixable`, even though it *should* be possible to find 6 decoys of that denomination.


# Discussion History
## moneromooo-monero | 2018-08-07T17:17:18+00:00
Ah, good catch. For these, the wallet should retry to get more candidates. I never ended up doing this since the probability of this being required was pretty small - until this.

## jamespic | 2018-08-14T22:34:29+00:00
The user who reported this also reports that `sweep_unmixable` fails, with "No unmixable outputs found". This makes sense, because it identifies unmixable outputs purely from the histogram.

These two things combined mean that users with blackballs can't send these pre-RingCT outputs.

## moneromooo-monero | 2018-08-14T23:25:25+00:00
That doesn't make sense to me. A level 2 log would be helpful there.

## jamespic | 2018-08-15T07:28:44+00:00
I got this from the user who made me aware of the issue. I can go back and ask for more detail if needed.

```

2018-08-06 19:15:51.438	  0x7fffa8904380	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:364	Read command: sweep_unmixable 46XXREDACTEDXX
2018-08-06 19:15:59.187	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-08-06 19:15:59.187	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:15:59.217	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 127
2018-08-06 19:15:59.333	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-08-06 19:15:59.333	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:15:59.360	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 277
2018-08-06 19:15:59.360	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v2 rules
2018-08-06 19:15:59.360	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v4 rules
2018-08-06 19:15:59.465	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-08-06 19:15:59.465	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:15:59.494	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 274
2018-08-06 19:15:59.494	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8117	Not using v7 rules
2018-08-06 19:15:59.683	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-08-06 19:15:59.683	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:15:59.706	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 277
2018-08-06 19:15:59.706	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v6 rules
2018-08-06 19:16:00.092	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 164
2018-08-06 19:16:00.092	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:16:00.093	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 1448
2018-08-06 19:16:00.094	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 2896
2018-08-06 19:16:00.094	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 4344
2018-08-06 19:16:00.095	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 4344
2018-08-06 19:16:00.163	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 1448
2018-08-06 19:16:00.193	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 2896
... lots of this ...
2018-08-06 19:16:00.839	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 1448
2018-08-06 19:16:00.840	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 2836
2018-08-06 19:16:00.878	  0x7fffa8904380	ERROR	msgwriter	src/common/scoped_message_writer.h:102	Error: No unmixable outputs found
2018-08-06 19:16:21.779	  0x7fffa8904380	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:364	Read command: set
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	seed = English
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	always-confirm-transfers = 0
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	print-ring-members = 1
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	store-tx-info = 1
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	default-ring-size = 0
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	auto-refresh = 1
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	refresh-type = optimize-coinbase
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	priority = 0
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	confirm-missing-payment-id = 1
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	ask-password = 1
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	unit = monero
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	min-outputs-count = 0
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	min-outputs-value = 0.000000000000
2018-08-06 19:16:21.779	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	merge-destinations = 0
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	confirm-backlog = 1
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	confirm-backlog-threshold = 0
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	confirm-export-overwrite = 1
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	refresh-from-block-height = 0
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	auto-low-priority = 1
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	segregate-pre-fork-outputs = 1
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	key-reuse-mitigation2 = 1
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	subaddress-lookahead = 50:200
2018-08-06 19:16:21.780	  0x7fffa8904380	INFO 	msgwriter	src/common/scoped_message_writer.h:102	segregation-height = 1546000
2018-08-06 19:16:21.846	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-08-06 19:16:21.846	  0x7fffa8904380	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-08-06 19:16:21.875	  0x7fffa8904380	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 951
2018-08-06 19:16:31.075	  0x7fffa8904380	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:364	Read command: exit
2018-08-06 19:16:31.075	  0x7fffa8904380	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:3927	trimming to [redacted], offset [redacted]
2018-08-06 19:16:31.157	  0x7fffa8904380	DEBUG	device.ledger	src/device/device_ledger.cpp:230	Device 0 Destroyed
```

## moneromooo-monero | 2018-08-15T09:56:23+00:00
Are there any unmixable outputs in that wallet ?
"incoming_transfers available" will list outputs.

## jamespic | 2018-08-16T09:45:44+00:00
I don't believe there are any truly unmixable outputs in that account, but there are outputs that failed to mix because of the original issue, and the standard message that is produced recommends to try `sweep_unmixable`.

## jamespic | 2018-08-23T20:40:54+00:00
```

[wallet [redacted]]: incoming_transfers available
amount spent unlocked ringct global index tx id addr index
0.000000100000 F unlocked - [redacted] <[redacted]> 0
0.003000000000 F unlocked - [redacted] <[redacted]> 0
3.000000000000 F unlocked - [redacted] <[redacted]> 0
0.141367865394 F unlocked RingCT [redacted] <[redacted]> 0
```

## moneromooo-monero | 2018-09-09T12:58:52+00:00
This should be fixed by https://github.com/monero-project/monero/pull/4260 (will need reimporting blackball list as the format changed).

## moneromooo-monero | 2018-09-14T11:03:45+00:00
Which is now merged.

## moneromooo-monero | 2018-09-21T18:54:31+00:00
Believed fixed (blackball list will need re-importing). Reopen if it still happens.

+resolved

# Action History
- Created by: jamespic | 2018-08-07T16:09:55+00:00
- Closed at: 2018-09-21T19:08:57+00:00
