---
title: '[Feature Request] Healthcheck Endpoints'
source_url: https://github.com/monero-project/monero/issues/8035
author: CryptoGrampy
assignees: []
labels: []
created_at: '2021-11-01T19:21:43+00:00'
updated_at: '2021-11-01T20:54:22+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
It would be great to have simple 'healthcheck' api endpoints added to Monerod and Wallet-Rpc, (others?) that could provide useful status information { "status": "available" } and could be possibly extended down the road.  An example of how this is used is Seth's Monerod Docker image that uses the get_info api for the healthcheck.  These things are useful for obviously checking service health and restarting things when necessary.  It would be great to have something a little more polished and defined.  

# Discussion History
## ndorf | 2021-11-01T19:49:39+00:00
What's wrong with `get_info`?

## CryptoGrampy | 2021-11-01T20:54:22+00:00
get_info seems fine unless anyone thinks it's too heavy handed for something that's pinged every 30 seconds/minute, but it would be great to see get_info also added to wallet-rpc for consistency's sake and perhaps adding documentation for monerod/wallet-rpc that it's a good endpoint to use for a healthcheck.

# Action History
- Created by: CryptoGrampy | 2021-11-01T19:21:43+00:00
