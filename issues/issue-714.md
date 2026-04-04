---
title: 'GUI daemon on OSx can''t sync the last blocks '
source_url: https://github.com/monero-project/monero-gui/issues/714
author: kamushki
assignees: []
labels:
- resolved
created_at: '2017-05-05T13:40:59+00:00'
updated_at: '2017-12-13T16:43:46+00:00'
type: issue
status: closed
closed_at: '2017-12-13T11:09:12+00:00'
---

# Original Description


Problem started after "friend" messed with daemon trying to speed up the synchronization, which was almost finished after 3 days of working(Indian inet), the network status went "Disconnected" (while the internet connection is fine)and in "send" it's failing to connect the wallet to daemon,and the sync process stuck on the same block,since 3days ago it shows the same :
2017-05-04 23:36:33.157	INFO global contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1223958 (100.0%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 1(out)+0(in) connections, uptime 0d 0h 0m 11s

2017-05-04 23:38:49.640	INFO global contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1302929 (93.9%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 6(out)+0(in) connections, uptime 0d 0h 2m 27s

2017-05-04 23:50:38.437	INFO global contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1223958/1302938 (93.9%) on mainnet, not mining, net hash 49.96 MH/s, v4, up to date, 8(out)+0(in) connections, uptime 0d 0h 14m 16s

Just after creating the wallet I've sent some xmr to it, the transaction appears on the blockchain ,but not in the wallet , will it appear when sync is done?
how to solve this daemon issue?

# Discussion History
## rserranon | 2017-05-09T00:43:35+00:00
Similar problem on Mac OsX 10.11.6 with Monero wallet 
2017-05-08 19:41:19.306		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
Height: 1305991/1305991 (100.0%) on mainnet, not mining, net hash 67.23 MH/s, v5, up to date, 8(out)+0(in) connections, uptime 0d 0h 3m 26s

but on terminal:

ro@MacBook-Prot-5:~/monero$ ./monerod
2017-05-08 19:37:45.093		INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO
2017-05-08 19:37:45.094		INFO 	global	src/daemon/main.cpp:282	Monero 'Wolfram Warptangent' (v0.10.3.1-release)
2017-05-08 19:37:45.094		INFO 	global	src/daemon/protocol.h:55	Initializing cryptonote protocol...
2017-05-08 19:37:45.094		INFO 	global	src/daemon/protocol.h:60	Cryptonote protocol initialized OK
2017-05-08 19:37:45.096		INFO 	global	src/daemon/p2p.h:63	Initializing p2p server...
2017-05-08 19:37:53.609		INFO 	global	src/daemon/p2p.h:68	P2p server initialized OK
2017-05-08 19:37:53.609		INFO 	global	src/daemon/rpc.h:58	Initializing core rpc server...
2017-05-08 19:37:53.609		INFO 	global	contrib/epee/include/net/http_server_impl_base.h:70	Binding on 127.0.0.1:18081
2017-05-08 19:37:53.612		INFO 	global	src/daemon/rpc.h:63	Core rpc server initialized OK on port: 18081
2017-05-08 19:37:53.612		INFO 	global	src/daemon/core.h:73	Initializing core...
2017-05-08 19:37:53.629		INFO 	global	src/cryptonote_core/cryptonote_core.cpp:326	Loading blockchain from folder /Users/robert/.bitmonero/lmdb ...
2017-05-08 19:38:44.990		WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received
2017-05-08 19:38:45.002		INFO 	global	src/daemon/core.h:78	Core initialized OK
2017-05-08 19:38:45.003		INFO 	global	src/daemon/rpc.h:68	Starting core rpc server...
2017-05-08 19:38:45.004	[RPC1]	INFO 	global	src/daemon/rpc.h:73	Core rpc server started ok
2017-05-08 19:38:45.006	[RPC1]	INFO 	global	src/daemon/p2p.h:78	Starting p2p net loop...
2017-05-08 19:38:46.010	[P2P9]	INFO 	global	src/cryptonote_core/cryptonote_core.cpp:1098	
**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************

2017-05-08 19:38:46.544	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:293	[98.151.16.60:18080 OUT] Sync data returned a new top block candidate: 1305984 -> 1305991 [Your node is 7 blocks (0 days) behind] 
SYNCHRONIZATION started
2017-05-08 19:38:48.865	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1004	[216.117.145.37:18080 OUT]  Synced 1305991/1305991
2017-05-08 19:38:48.866	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099	SYNCHRONIZED OK
2017-05-08 19:38:48.866	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099	SYNCHRONIZED OK
2017-05-08 19:38:48.866	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1115	
**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************
2017-05-08 19:38:49.102	[P2P9]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1099	SYNCHRONIZED OK
2017-05-08 19:39:39.027	[P2P9]	WARN 	net.dns	src/common/dns_utils.cpp:531	WARNING: no two valid MoneroPulse DNS checkpoint records were received

## dEBRUYNE-1 | 2017-08-07T18:09:48+00:00
Try adding `--block-sync-size 20` as startup flag on the `Settings` page.

## kamushki | 2017-09-07T12:28:23+00:00
Hi
Thanx this partially helps , but i fail to figure out why this tx is not showing received in my wallet ???
https://xmrchain.net/tx/cf4304b37a3cd1325e720cf0c9e796f9f1a4fd13628045a1b20c0ef74e9786c1

On Mon, Aug 7, 2017 at 21:09, dEBRUYNE-1 <notifications@github.com> wrote:

> Try adding --block-sync-size 20 as startup flag on the Settings page.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-core/issues/714#issuecomment-320738101), or [mute the thread](https://github.com/notifications/unsubscribe-auth/AbFR_9_3WrJHA7c8MIFOt_LO5tk3VFmIks5sV1LugaJpZM4NR7nH).
>
> {"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/monero-project/monero-core","title":"monero-project/monero-core","subtitle":"GitHub repository","main_image_url":"https://cloud.githubusercontent.com/assets/143418/17495839/a5054eac-5d88-11e6-95fc-7290892c7bb5.png","avatar_image_url":"https://cloud.githubusercontent.com/assets/143418/15842166/7c72db34-2c0b-11e6-9aed-b52498112777.png","action":{"name":"Open in GitHub","url":"https://github.com/monero-project/monero-core"}},"updates":{"snippets":[{"icon":"PERSON","message":"@dEBRUYNE-1 in #714: Try adding `--block-sync-size 20` as startup flag on the `Settings` page."}],"action":{"name":"View Issue","url":"https://github.com/monero-project/monero-core/issues/714#issuecomment-320738101"}}}

## dEBRUYNE-1 | 2017-12-13T11:05:18+00:00
@kamushki I didn't see this until now. You can use this guide:

https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

## dEBRUYNE-1 | 2017-12-13T11:06:48+00:00
If the issue is strictly related to the daemon, please open an issue on monero-project/monero. 

+resolved

## kamushki | 2017-12-13T16:43:45+00:00
Dear Debruyn)
You’ve helped me with this issue long time ago, maybe I’ve doubled the request due to my impatience, excuse me pls for taking your time)
Thanx

Sent from ProtonMail Mobile

On Wed, Dec 13, 2017 at 16:39, issue-helper <notifications@github.com> wrote:

> Closed [#714](https://github.com/monero-project/monero-gui/issues/714).
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, [view it on GitHub](https://github.com/monero-project/monero-gui/issues/714#event-1385400086), or [mute the thread](https://github.com/notifications/unsubscribe-auth/AbFR_8mZfBiAuwbMQMkpdSc--B5qM7qaks5s_7BagaJpZM4NR7nH).
>
> {"api_version":"1.0","publisher":{"api_key":"05dde50f1d1a384dd78767c55493e4bb","name":"GitHub"},"entity":{"external_key":"github/monero-project/monero-gui","title":"monero-project/monero-gui","subtitle":"GitHub repository","main_image_url":"https://cloud.githubusercontent.com/assets/143418/17495839/a5054eac-5d88-11e6-95fc-7290892c7bb5.png","avatar_image_url":"https://cloud.githubusercontent.com/assets/143418/15842166/7c72db34-2c0b-11e6-9aed-b52498112777.png","action":{"name":"Open in GitHub","url":"https://github.com/monero-project/monero-gui"}},"updates":{"snippets":[{"icon":"DESCRIPTION","message":"Closed #714."}],"action":{"name":"View Issue","url":"https://github.com/monero-project/monero-gui/issues/714#event-1385400086"}}}

# Action History
- Created by: kamushki | 2017-05-05T13:40:59+00:00
- Closed at: 2017-12-13T11:09:12+00:00
