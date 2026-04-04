---
title: new rpc payments flags not working with --restricted-rpc-port
source_url: https://github.com/monero-project/monero/issues/6196
author: Gingeropolous
assignees: []
labels: []
created_at: '2019-11-29T17:33:43+00:00'
updated_at: '2020-05-16T16:12:22+00:00'
type: issue
status: closed
closed_at: '2020-05-16T16:12:22+00:00'
---

# Original Description
there's 2 ways to have restricted rpc.... one with --restricted-rpc whcih restricts all ports, and one with --restricted-rpc-port VALUE that allows you to confine restrictions to one port.

i just tried launching with the new payments flags on a conf file that had the port one, and it exited out saying that it needed a restricted rpc. 

# Discussion History
## moneromooo-monero | 2019-11-29T20:13:46+00:00
https://github.com/monero-project/monero/pull/6198

## moneromooo-monero | 2020-05-16T16:12:22+00:00
Fixed

# Action History
- Created by: Gingeropolous | 2019-11-29T17:33:43+00:00
- Closed at: 2020-05-16T16:12:22+00:00
