---
title: start p2pool crashes local node
source_url: https://github.com/monero-project/monero-gui/issues/4248
author: rnrkrft
assignees: []
labels: []
created_at: '2023-11-26T15:15:09+00:00'
updated_at: '2023-11-26T15:26:17+00:00'
type: issue
status: closed
closed_at: '2023-11-26T15:26:17+00:00'
---

# Original Description
Starting pool mining stops the daemon. Log shows:

83.32.206.150:42180 287b37f0c45b9d5d normal 0 3026567 1 kB/s, 0 blocks / 0 MB queued
147.135.136.35:18080 0b67e337fa11e2bc normal 0 3026567 0 kB/s, 0 blocks / 0 MB queued
199.116.84.161:18080 0000000000000000 before_handshake 0 0 0 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB
[]
[26.11.23 14:18] 2023-11-26 13:18:05.283 I Monero 'Fluorine Fermi' (v0.18.3.1-release)
Stop signal sent
[26.11.23 14:18] 2023-11-26 13:18:11.580 I Monero 'Fluorine Fermi' (v0.18.3.1-release)
Error: Couldn't connect to daemon: 127.0.0.1:18081

Working on a MacPro with Sonoma. Haven't tested different machines or systems yet...


# Discussion History
# Action History
- Created by: rnrkrft | 2023-11-26T15:15:09+00:00
- Closed at: 2023-11-26T15:26:17+00:00
