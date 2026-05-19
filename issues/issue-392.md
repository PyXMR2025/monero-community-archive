---
title: monero-wallet-gui can't get blocks
source_url: https://github.com/seraphis-migration/monero/issues/392
author: ComputeryPony
assignees: []
labels: []
created_at: '2026-05-16T16:25:07+00:00'
updated_at: '2026-05-17T06:11:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I imagine I'm not the only one to encounter this but I don't see an open issue for it so opening one.

After restoring a wallet from seed pointed at my daemon that's marked as trusted the GUI fails to refresh with an error of:
```
2026-05-16 16:10:51.364 E Too many object fields
2026-05-16 16:10:51.372 E Exception at [portable_storage::load_from_binary], what=Too many object fields
2026-05-16 16:10:51.372 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
```

Larger log:
```
2026-05-16 16:10:34.543 W SSL peer has not been verified
2026-05-16 16:10:34.543 W SSL peer has not been verified
2026-05-16 16:10:34.543 W SSL peer has not been verified
2026-05-16 16:10:34.633 D SSL handshake success
2026-05-16 16:10:34.634 T READ ENDS: Success. bytes_tr: 1433
2026-05-16 16:10:34.634 T http_stream_filter::parse_cached_header(*)
2026-05-16 16:10:34.634 D Newest wallet status: Wallet::ConnectionStatus_Connected
2026-05-16 16:10:34.634 D Starting refresh
2026-05-16 16:10:34.636 D Wallet connection status changed 1
2026-05-16 16:10:34.659 T doRefresh: doRefresh, rescan = 0
2026-05-16 16:10:34.659 D Refresh will ignore low start_height 0 and proceed to scan contiguously on top of already synced blocks
2026-05-16 16:10:34.659 I Refresh starting from block 2840000
2026-05-16 16:10:34.659 D Requesting blocks starting on top of block hash <78fcbc6428e2876ec39db9bb3eb0d63d92e5656421ccba5f82fa201f45702277>, n blocks synced: 2840000, init_tree_sync: 1
2026-05-16 16:10:43.888 T refreshThreadFunc: refresh lock acquired...
2026-05-16 16:10:43.888 T refreshThreadFunc: m_refreshEnabled: 0
2026-05-16 16:10:43.888 T refreshThreadFunc: m_status: 0
2026-05-16 16:10:43.888 T refreshThreadFunc: m_refreshShouldRescan: 0
2026-05-16 16:10:43.888 T refreshThreadFunc: waiting for refresh...
2026-05-16 16:10:51.299 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.299 T http_stream_filter::parse_cached_header(*)
2026-05-16 16:10:51.299 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.299 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.300 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.300 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.300 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.300 T READ ENDS: Success. bytes_tr: 16384
...
2026-05-16 16:10:51.327 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.327 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.327 T READ ENDS: Success. bytes_tr: 16384
2026-05-16 16:10:51.327 T READ ENDS: Success. bytes_tr: 13834
2026-05-16 16:10:51.364 E Too many object fields
2026-05-16 16:10:51.372 E Exception at [portable_storage::load_from_binary], what=Too many object fields
2026-05-16 16:10:51.372 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2026-05-16 16:10:51.372 W /monero-gui/monero/src/wallet/wallet_errors.h:1070:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = getblocks.bin
2026-05-16 16:10:51.372 I Another try pull_blocks (try_count=0)...
2026-05-16 16:10:51.372 D Refresh will ignore low start_height 0 and proceed to scan contiguously on top of already synced blocks
2026-05-16 16:10:51.372 I Refresh starting from block 2840000
2026-05-16 16:10:51.372 D Requesting blocks starting on top of block hash <78fcbc6428e2876ec39db9bb3eb0d63d92e5656421ccba5f82fa201f45702277>, n blocks synced: 2840000, init_tree_sync: 1
2026-05-16 16:10:53.888 T refreshThreadFunc: refresh lock acquired...
2026-05-16 16:10:53.888 T refreshThreadFunc: m_refreshEnabled: 0
2026-05-16 16:10:53.888 T refreshThreadFunc: m_status: 0
2026-05-16 16:10:53.888 T refreshThreadFunc: m_refreshShouldRescan: 0
2026-05-16 16:10:53.888 T refreshThreadFunc: waiting for refresh...
2026-05-16 16:11:03.888 T refreshThreadFunc: refresh lock acquired...
2026-05-16 16:11:03.888 T refreshThreadFunc: m_refreshEnabled: 0
2026-05-16 16:11:03.888 T refreshThreadFunc: m_status: 0
2026-05-16 16:11:03.888 T refreshThreadFunc: m_refreshShouldRescan: 0
2026-05-16 16:11:03.888 T refreshThreadFunc: waiting for refresh...
2026-05-16 16:11:06.127 D blocking close event
2026-05-16 16:11:06.127 D close accepted
2026-05-16 16:11:06.127 D DaemonManager: exit()
2026-05-16 16:11:06.127 D P2PoolManager: exit()
2026-05-16 16:11:06.128 D Displaying processing splash
2026-05-16 16:11:06.129 D ~Wallet: Closing wallet
2026-05-16 16:11:06.129 D Pausing refresh
```

# Discussion History
## j-berman | 2026-05-16T20:28:03+00:00
Is this windows perchance? I *think* this was also the issue for windows in #376 (and possibly resolved by #371) but I don't recall

## ComputeryPony | 2026-05-16T20:28:16+00:00
Linux

## j-berman | 2026-05-16T20:35:23+00:00
Ack, it may still be resolved by #371. Looks like a very similar isssue.

## ComputeryPony | 2026-05-16T20:36:24+00:00
I already have #371 applied. :/
I'm on d1adfbba21cdde7cec4b732ae4682ac44ee79167.
EDIT:
I also have applied #391 as I was experiencing that.

## j-berman | 2026-05-16T20:41:15+00:00
You're certain that both your GUI and daemon are using all that latest code?

## ComputeryPony | 2026-05-16T20:41:45+00:00
Yes, I've rebuilt them to apply #391.

## nahuhh | 2026-05-16T21:43:37+00:00
probably need to use restricted rpc

## ComputeryPony | 2026-05-16T23:27:29+00:00
Yup, that allows the wallet to sync, leaving this issue open though till normal rpc is fixed.

## nahuhh | 2026-05-17T06:11:06+00:00
You can cherry-pick #360

this should fix the unrestricted rpc

# Action History
- Created by: ComputeryPony | 2026-05-16T16:25:07+00:00
