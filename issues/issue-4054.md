---
title: Daemon not syncing
source_url: https://github.com/monero-project/monero-gui/issues/4054
author: Eumaios1212
assignees: []
labels: []
created_at: '2022-10-26T13:29:49+00:00'
updated_at: '2022-10-26T20:07:37+00:00'
type: issue
status: closed
closed_at: '2022-10-26T20:07:37+00:00'
---

# Original Description
When I start my GUI wallet in Ubuntu 22.04.1 LTS, the daemon fails to start. I can, however manually start it. The logs have the following:

Error: Couldn't connect to daemon: 127.0.0.1:18081

This repeats over and over until it gives up and I start it manually. Then I get this:
 
09:16
10/26/22 8:39 AM] 2022-10-26 12:39:27.997 I Monero 'Fluorine Fermi' (v0.18.1.2-release)
Height: 2736746, target: 2741934 (99.8108%)
Downloading at 72 kB/s
3 peers
Remote Host Peer_ID State Prune_Seed Height DL kB/s, Queued Blocks / MB
95.111.247.94:18080 ce9ec1bb6808e863 synchronizing 180 2741934 24 kB/s, 0 blocks / 0 MB queued
51.83.179.106:18080 b9fb97dbdd8bb699 synchronizing 0 2741934 24 kB/s, 0 blocks / 0 MB queued
46.28.204.223:18080 215c21bc8f3aa2b7 synchronizing 0 2741934 24 kB/s, 0 blocks / 0 MB queued
0 spans, 0 MB

# Discussion History
## selsta | 2022-10-26T17:56:20+00:00
How did you install the program?

## Eumaios1212 | 2022-10-26T18:34:23+00:00
Not sure what you are asking for--not at all tech-savy. What are my options?

If it helps: monero-wallet-gui, monero-wallet-gui.AppImage and monerod are all installed in my Applications folder.

## selsta | 2022-10-26T18:35:21+00:00
I mean did you download it from getmonero.org, or did you use flatpak / package manger?

## Eumaios1212 | 2022-10-26T18:37:12+00:00
OK, I see. I'm 90% sure through get.monero.org (I've had a lot of help from people making the move to Ubuntu from Windows, and some details are a blur). 

## selsta | 2022-10-26T18:48:22+00:00
When you start monerod from the GUI there should be an error message after 120s. What exact error shows up?

## selsta | 2022-10-26T20:07:37+00:00
Appears to be a permission issue.

# Action History
- Created by: Eumaios1212 | 2022-10-26T13:29:49+00:00
- Closed at: 2022-10-26T20:07:37+00:00
