---
title: Daemon synchronization is taking too long
source_url: https://github.com/monero-project/monero-gui/issues/4464
author: ghost
assignees: []
labels: []
created_at: '2025-06-27T11:25:07+00:00'
updated_at: '2025-06-29T09:37:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Synchronizing daemon with monero gui is taking too long. Many of the times, not happening at all. At some times, the synchronization timed out.

# Discussion History
## HoaxParagon | 2025-06-27T15:33:05+00:00
Try adding --out-peers 128 or some value higher than default.

## PyXMR2025 | 2025-06-28T14:32:01+00:00
You can try specifying a boot node (a trusted node)

## selsta | 2025-06-28T16:36:35+00:00
I don't know what "timed out" means, there is no time out during sync as far as I remember.

Can you specify how long you are waiting? And are you syncing to a HDD or SSD?

## ghost | 2025-06-29T08:33:34+00:00
After 120 seconds, the GUI said that it timed out.
The GUI dosen't always say that the daemon is synchronizing or not. Sometimes it doesn't synchronize. Sometimes it does.
I was syncing it to a HDD.

## ghost | 2025-06-29T08:34:54+00:00
```
[29/06/25 2:04 PM] 2025-06-29 08:33:58.939 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:13.629 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:16.409 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:19.324 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:21.638 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:24.091 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:26.868 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:29.475 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:32.055 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:34.547 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:36.989 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:39.598 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:42.542 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:44.889 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:47.846 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:50.910 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:54.518 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:57.183 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:59.655 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:02.115 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:04.591 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:07.579 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:09.887 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:12.340 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:14.854 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:17.308 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:19.755 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:22.727 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:25.135 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:27.763 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:31.585 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:33.898 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:36.647 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:39.654 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:42.908 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:05 PM] 2025-06-29 08:35:46.361 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:06 PM] 2025-06-29 08:35:50.092 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Height: 2474104, target: 2474104 (100%)
Downloading at 0 kB/s
Next needed pruning seed: 5
0 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
0 spans, 0 MB
[]
```

## PyXMR2025 | 2025-06-29T09:37:34+00:00
Open the task manager, close all programs related to Monero, then reopen the GUI and wait for Monerode to start (usually automatically).



At 2025-06-29 16:35:15, "Kallam Tarun Kumar Reddy" ***@***.***> wrote:

tarunkumar-collab left a comment (monero-project/monero-gui#4464)
[29/06/25 2:04 PM] 2025-06-29 08:33:58.939 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:13.629 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:16.409 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:19.324 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:21.638 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:24.091 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:26.868 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081
[29/06/25 2:04 PM] 2025-06-29 08:34:29.475 I Monero 'Fluorine Fermi' (v0.18.4.0-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081


—
Reply to this email directly, view it on GitHub, or unsubscribe.
You are receiving this because you commented.Message ID: ***@***.***>

# Action History
- Created by: ghost | 2025-06-27T11:25:07+00:00
