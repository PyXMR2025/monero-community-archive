---
title: Monero Blockchain Downloading Very Slowly
source_url: https://github.com/monero-project/monero-gui/issues/3937
author: DavisRee
assignees: []
labels: []
created_at: '2022-06-02T01:20:22+00:00'
updated_at: '2022-06-02T01:24:25+00:00'
type: issue
status: closed
closed_at: '2022-06-02T01:24:16+00:00'
---

# Original Description
I've been synching the entire blockchain for days now.  Per speedtest.net, I have 500MBps download speed available so that is not the issue.  (Would take less than 4 minutes at that speed!)  When I started the synch, it looked like it should take a few hours based on the rate at which the blocks were synching.  I left it for the night and came back the next day with about 60%  of blocks synched, but rate was much slower.  Now a couple more days later, I checked the actual file size and it is at about 78GB and changing by less than 100KBps and making corresponding progress on blocks (maybe a few blocks per second with over 600,000 to go).

# Discussion History
## selsta | 2022-06-02T01:24:16+00:00
Syncing is not the same as just downloading a file. It also verifies all the cryptography which is the slow part.

To speed sync up try the following:

- Use an SSD instead of HDD
- Make sure to use the latest version v0.17.3.2

Closing as this is a question and not a bug report.

# Action History
- Created by: DavisRee | 2022-06-02T01:20:22+00:00
- Closed at: 2022-06-02T01:24:16+00:00
