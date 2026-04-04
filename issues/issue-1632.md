---
title: sweep_all causing freeze loop in cli and gui
source_url: https://github.com/monero-project/monero-gui/issues/1632
author: 5andr0
assignees: []
labels: []
created_at: '2018-10-10T15:38:00+00:00'
updated_at: '2018-10-11T14:14:43+00:00'
type: issue
status: closed
closed_at: '2018-10-11T14:14:42+00:00'
---

# Original Description
I tried to empty my wallet and always end up in a freeze loop.
cli log: 

```
2018-10-10 14:57:39.936	60896	DEBUG	wallet.wallet2	contrib/epee/include/console_handler.h:364	Read command: sweep_all unimportant 7 *OBFUSCATED*
2018-10-10 14:57:44.248	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-10-10 14:57:44.248	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:44.248	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 127
2018-10-10 14:57:47.195	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 159
2018-10-10 14:57:47.195	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.195	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 67
2018-10-10 14:57:47.195	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-10-10 14:57:47.195	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.195	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 277
2018-10-10 14:57:47.195	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v4 rules
2018-10-10 14:57:47.195	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7894	Spending from subaddress index 0
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-10-10 14:57:47.196	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 277
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v5 rules
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v4 rules
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-10-10 14:57:47.196	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 274
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8117	Not using v8 rules
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v4 rules
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 160
2018-10-10 14:57:47.196	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.196	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 127
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v5 rules
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7959	Starting with 4 non-dust outputs and 6 dust outputs
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 340, amount *obfuscated*
2018-10-10 14:57:47.196	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 1 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 1 with ring size 7 and 2: 13197 (544 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 205, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 2 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 2 with ring size 7 and 2: 13762 (1024 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 352, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 3 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 3 with ring size 7 and 2: 14327 (1504 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 213, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 4 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 4 with ring size 7 and 2: 14892 (1984 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 105, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 5 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 5 with ring size 7 and 2: 15457 (2464 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 174, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 6 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 6 with ring size 7 and 2: 16022 (2944 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 266, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 7 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 7 with ring size 7 and 2: 16587 (3424 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 191, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 8 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 8 with ring size 7 and 2: 17152 (3904 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 342, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 9 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 9 with ring size 7 and 2: 17717 (4384 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7982	Picking output 345, amount *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:7994	Considering whether to create a tx now, 10 inputs, tx limit 299400
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 10 with ring size 7 and 2: 18282 (4864 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:565	estimated rct tx size for 10 with ring size 7 and 1: 11972 (4832 saved)
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8008	Trying to create a tx now, with 1 destinations and 10 outputs
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:8115	Using v5 rules
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6501	transfer_selected_rct: starting with fee *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6502	selected transfers: 340 205 352 213 105 174 266 191 342 345
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6510	transfer: adding 0.000000000001, for a total of *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6550	wanted 0.001803240001, found *obfuscated*, fee *obfuscated*
2018-10-10 14:57:47.197	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5884	fake_outputs_count: 6
2018-10-10 14:57:47.620	60896	DEBUG	net.dns	src/common/dns_utils.cpp:481	DNSSEC not available for checkpoint update at URL: segheights.moneropulse.co, skipping.
2018-10-10 14:57:47.620	60896	DEBUG	net.dns	src/common/dns_utils.cpp:486	DNSSEC validation failed for checkpoint update at URL: segheights.moneropulse.co, skipping.
2018-10-10 14:57:47.620	60896	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:10521	Found segregation height via DNS: asicflood fork height at 1564000
2018-10-10 14:57:47.693	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 161
2018-10-10 14:57:47.693	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.693	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 1464
2018-10-10 14:57:47.718	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 163
2018-10-10 14:57:47.719	60896	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 10000
2018-10-10 14:57:47.719	60896	TRACE	net	contrib/epee/include/net/net_helper.h:403	READ ENDS: Success. bytes_tr: 5163
2018-10-10 14:57:47.720	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:5970	base_requested_outputs_count: 11
2018-10-10 14:57:47.720	60896	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6007	Found 0.000100000000: 79225 total, 79225 unlocked, 0 recent
2018-10-10 14:57:47.720	60896	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6041	79225 unlocked outputs of size 0.000100000000
2018-10-10 14:57:47.720	60896	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6063	Fake output makeup: 11 requested: 0 recent, 0 pre-fork, 3 post-fork, 8 full-chain
2018-10-10 14:57:47.720	60896	INFO 	wallet.wallet2	src/wallet/wallet2.cpp:6124	Selecting real output: 79224 for 0.000100000000
```

Probably caused by this endless loop here: https://github.com/monero-project/monero/blob/master/src/wallet/wallet2.cpp#L6971

It also stuck multiple times before when i tried to send higher amounts of coins from that wallet. (This was on GUI, so i don't have a debug log for that)

There are more people having issues with this: https://www.reddit.com/r/Monero/comments/8vcdhv/monero_gui_stuck_on_creating_transaction/

I'm on win64 and v0.12.3.0. Node is fully synced. Restart doesn't help.

I currently don't have the time to test this on linux or build it myself to debug it.
Any other idea how to pinpoint the bug?
Thanks

# Discussion History
## dEBRUYNE-1 | 2018-10-10T20:52:58+00:00
Have you tried performing a `sweep_all` with CLI v0.13? 

## 5andr0 | 2018-10-11T14:14:42+00:00
> Have you tried performing a `sweep_all` with CLI v0.13?

Thanks for the tip, i didn't realize there's v0.13. So after hours of compiling and migrating the db from v1 to v2 and then v3 it's not freezing anymore.
Issue closed =)

# Action History
- Created by: 5andr0 | 2018-10-10T15:38:00+00:00
- Closed at: 2018-10-11T14:14:42+00:00
