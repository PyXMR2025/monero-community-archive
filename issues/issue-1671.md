---
title: closing miner,
source_url: https://github.com/xmrig/xmrig/issues/1671
author: overunme
assignees: []
labels: []
created_at: '2020-05-08T03:16:37+00:00'
updated_at: '2020-08-19T01:24:05+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:24:05+00:00'
---

# Original Description
For the last few days I have been trying mine monero with CPU. Ive had the following issues: at first PC thought it was a virus, I deativated windows security. I was then able to download the file. Then I processed the changes to create JSON file using the wizazrd.  The rig opened for a few seconds then would close. I tried opening from CMD but it would close once again. The file would eventually disapear from where i had unziped it. I have tried everything.  I am on windows 10 running ryze 3600. 

# Discussion History
## Masterbob79 | 2020-05-08T17:03:36+00:00
Probably json file is missing a comma or something. Or its saved as a .txt instead of .json

## 2010phenix | 2020-05-09T12:13:11+00:00
add to exclusive in defender windows security miner (xmrg.exe)
start file and miner build config(JSON) for your hardware
if use CMD and want look on error... add PAUSE in last line to bat file

# Action History
- Created by: overunme | 2020-05-08T03:16:37+00:00
- Closed at: 2020-08-19T01:24:05+00:00
