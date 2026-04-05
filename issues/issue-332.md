---
title: Cycling through multiple Pools
source_url: https://github.com/xmrig/xmrig/issues/332
author: korishan
assignees: []
labels: []
created_at: '2018-01-11T00:52:31+00:00'
updated_at: '2018-11-05T07:09:18+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:09:18+00:00'
---

# Original Description
I'm new to the crypto world. Not sure of the search criteria to find this answer, or narrow down the results I'm looking for.

I've started using xmrig yesterday. I started using it in standalone mode from NiceHash as NH seems to keep disconnecting, rejecting, resetting connection, etc. 
But, I've managed to get this running in standalone using the NH pool addresses (for when I can mine for a period of time) and I've also included Nanopool and DwarfPool for Monero mining.
My question is, I have a list of pools in the config.json, but I only ever see it connect to the first one, and DwarfPool. After some time, NH will start denying my connection (for some unknown reason, I haven't gotten an answer from them about it) and xmrig will, I assume, go down the list until it gets a connection, which ends up being DwarfPool. 
But, during the retries, I never see any messages that it's trying the other pool addresses, only the first one, which is failing connection.
Is it actually cycling through the list of pools, and only showing the first one as failing?

Thanks,
Kori



# Discussion History
# Action History
- Created by: korishan | 2018-01-11T00:52:31+00:00
- Closed at: 2018-11-05T07:09:18+00:00
