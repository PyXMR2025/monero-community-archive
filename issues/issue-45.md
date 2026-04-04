---
title: Provide X-I2P header response on check.kovri.i2p
source_url: https://github.com/monero-project/meta/issues/45
author: anonimal
assignees: []
labels: []
created_at: '2017-02-07T21:19:39+00:00'
updated_at: '2017-06-16T02:16:45+00:00'
type: issue
status: closed
closed_at: '2017-06-16T02:16:45+00:00'
---

# Original Description
From https://github.com/monero-project/kovri/issues/540:
>HTTP client tunnel output to file will also ease sharing of whitelisted addresses for server tunnels

Instead of a file, we can implement on check.kovri.i2p to provide a header response for HTTP client tunnels *without* persistent keys, similar to what stats.i2p/cgi-bin/mydest is doing (see tunnels config documentation for details).

This is trivial to implement with PHP. Ticketing for housekeeping.

# Discussion History
## anonimal | 2017-06-16T02:16:45+00:00
Moved to https://github.com/monero-project/kovri-site/issues/4.

# Action History
- Created by: anonimal | 2017-02-07T21:19:39+00:00
- Closed at: 2017-06-16T02:16:45+00:00
