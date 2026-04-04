---
title: Transactions Failing To Send On First Attempt After Update
source_url: https://github.com/monero-project/monero/issues/6952
author: downystreet
assignees: []
labels: []
created_at: '2020-10-30T22:27:55+00:00'
updated_at: '2022-02-19T01:05:21+00:00'
type: issue
status: closed
closed_at: '2022-02-19T01:05:20+00:00'
---

# Original Description
Since the last update I have noticed that every time I send a transaction it ends up failing and I have to resend it again. On the second attempt to send it works. I am using the GUI AppImage.

Version: monero-gui-v0.17.1.1

# Discussion History
## selsta | 2020-10-30T22:29:51+00:00
Simple mode or advanced mode?

If advanced mode, local node or remote node?

## downystreet | 2020-10-30T22:31:15+00:00
Simple Mode

## selsta | 2020-10-30T22:36:05+00:00
Can you go to Settings -> Log, enter "sync_info" and post the output here?

## downystreet | 2020-10-30T22:39:52+00:00
>>> sync_info
[10/30/20 6:37 PM] 2020-10-30 22:37:42.702 I Monero 'Oxygen Orion' (v0.17.1.1-release)
Height: 1, target: 2219881 (4.50475e-05%)
Downloading at 13 kB/s
Next needed pruning seed: 2
16 peers
142.44.144.199:18080 c230dc193bad94b8 normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
104.191.116.68:18080 b19a7f235e3b4c19 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
51.77.202.219:6213 418ca3fd30c8157a normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
173.249.20.78:18080 5c65d60a0de211b1 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
54.39.75.52:3434 43c6f9dbc6ce7a8e normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
82.38.144.132:18080 52b67c5142b6838e normal 0 2219881 1 kB/s, 0 blocks / 0 MB queued
116.203.189.184:18080 658b28ac3debc2a2 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
37.59.43.131:48080 2bf5e676689868b9 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
51.89.134.164:17611 fc0c293f947aba50 normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
51.77.202.219:18080 6a28b075ca3da93e normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
5.160.146.198:18080 848496e976f72b46 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
54.39.75.70:7597 e116ea4681130c08 normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
79.137.8.254:12668 6d07ac85b1ab35c9 normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
51.91.108.121:3807 81a13add4e30c4af normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
51.79.58.92:2117 0fa310a7cbae2fd0 normal 0 2219881 0 kB/s, 0 blocks / 0 MB queued
71.55.144.207:18080 02fc45445b22b802 normal 0 2219881 2 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]

## selsta | 2020-10-30T23:08:38+00:00
Interesting, thank you. This is a known issue, we are working on it. In the meantime please follow this comment: https://github.com/monero-project/monero-gui/issues/3140#issuecomment-706440354

## dEBRUYNE-1 | 2020-11-10T16:26:24+00:00
Please try the recently released v0.17.1.4:

https://www.reddit.com/r/Monero/comments/jrgtca/gui_v01714_oxygen_orion_released/

Additionally, see:

https://www.reddit.com/r/Monero/comments/jrh7mv/psa_informational_thread_on_the_recently_observed/

# Action History
- Created by: downystreet | 2020-10-30T22:27:55+00:00
- Closed at: 2022-02-19T01:05:20+00:00
