---
title: Inbound and outbound i2p connections have the same peer ID
source_url: https://github.com/monero-project/monero/issues/7004
author: MoneroArbo
assignees: []
labels: []
created_at: '2020-11-10T20:36:53+00:00'
updated_at: '2021-01-09T01:40:55+00:00'
type: issue
status: closed
closed_at: '2021-01-09T01:40:55+00:00'
---

# Original Description
With the most recent version of monerod (0.17.1.3) I have been occasionally connected to INC and OUT i2p peers that have the same peer ID. As discussed in #6380, this is going to result in the ability to correlate transactions relayed over i2p with a particular i2p address.

[Output of print_cn](https://i.imgur.com/IMsoDr9.png)

[Output of sync_info](https://i.imgur.com/iTJRIDA.png)

@vtnerd I was suggested to ping you on this one

# Discussion History
## vtnerd | 2020-11-11T05:05:06+00:00
I closed the prior issue, and I will work on a fix for this shortly.

## moneromooo-monero | 2021-01-09T01:40:55+00:00
Patch merged.

# Action History
- Created by: MoneroArbo | 2020-11-10T20:36:53+00:00
- Closed at: 2021-01-09T01:40:55+00:00
