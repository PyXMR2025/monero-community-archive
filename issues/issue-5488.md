---
title: Creating Unsigned Transaction taking ~200 seconds in <net_utils::invoke_http_json_rpc>
source_url: https://github.com/monero-project/monero/issues/5488
author: zhongqiuwood
assignees: []
labels: []
created_at: '2019-04-24T09:33:54+00:00'
updated_at: '2019-09-02T12:01:38+00:00'
type: issue
status: closed
closed_at: '2019-09-02T12:01:38+00:00'
---

# Original Description
I'm using v0.14.0.2 monero-wallet-cli to generate an unsigned tx which always took me ~200 seconds. And finally I found it stucked in method <net_utils::invoke_http_json_rpc> in <wallet2::get_rct_distribution>.

```
2019-04-24 08:55:36.862	    7f0cd13ca780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:6669	fake_outputs_count: 10
2019-04-24 08:55:36.902	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 160
2019-04-24 08:55:36.903	    7f0cd13ca780	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2019-04-24 08:55:36.942	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 128
2019-04-24 08:55:36.942	    7f0cd13ca780	DEBUG	wallet.wallet2	src/wallet/wallet2.cpp:2828	Daemon is recent enough, requesting rct distribution
```
200 seconds pause

```
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 164
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net.http	contrib/epee/include/net/http_client.h:758	http_stream_filter::parse_cached_header(*)
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.752	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
2019-04-24 08:59:06.753	    7f0cd13ca780	TRACE	net	contrib/epee/include/net/net_helper.h:404	READ ENDS: Success. bytes_tr: 10000
```

# Discussion History
## moneromooo-monero | 2019-04-24T10:37:32+00:00
Is the daemon just started, and running on a HDD ? This call is a heavy one, but gets cached.


## moneromooo-monero | 2019-04-24T10:40:24+00:00
Also, there are speedups for this in master, if you want to try it and compare.

## zhongqiuwood | 2019-04-24T14:12:43+00:00
The monerod is running on a separated cloud vm(HDD) from the one where monero-wallet-cli run on, but the 2 cloud vms are in a same data center. The monerod is not just started, but running for a couple of days.

## zhongqiuwood | 2019-04-24T14:16:20+00:00
@moneromooo-monero will the next release ship the speedups?

## moneromooo-monero | 2019-04-24T14:24:49+00:00
The next release will have the speedups.

## moneromooo-monero | 2019-04-24T14:27:16+00:00
You seem to have kinda the worst case. Please let us know once you run the coming release, what the new time is.

## zhongqiuwood | 2019-04-25T01:10:30+00:00
@moneromooo-monero Thanks. Will keep you updated.

## apufvqsp | 2019-04-25T07:05:49+00:00
> Is the daemon just started, and running on a HDD ? This call is a heavy one, but gets cached.

@moneromooo-monero how long the<net_utils::invoke_http_json_rpc> call result cache expire in monero-wallet-cli？the<net_utils::invoke_http_json_rpc> call cache always valid if i repeat invoke it？

## moneromooo-monero | 2019-04-25T09:15:35+00:00
Until a new block arrives, but most of the cache is still valid then. There's a bug with reorgs though, which will get fixed soon.

## apufvqsp | 2019-04-25T12:28:28+00:00
OK， thank you

## moneromooo-monero | 2019-04-25T16:51:50+00:00
#5496 further improves this, but I'm not sure it'll be in next release.

## moneromooo-monero | 2019-06-15T10:38:59+00:00
It is in 0.14.1.0, please try with that.

## moneromooo-monero | 2019-09-02T11:20:48+00:00
Since no more info for a while, I'll close it since the speedups have been in for a while.

+resolved

# Action History
- Created by: zhongqiuwood | 2019-04-24T09:33:54+00:00
- Closed at: 2019-09-02T12:01:38+00:00
