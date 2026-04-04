---
title: MIssing brackets around IPv6 address in logfile when using --rpc-bind-ipv6-address
  [::]
source_url: https://github.com/monero-project/monero/issues/7966
author: li5lo
assignees: []
labels: []
created_at: '2021-09-22T11:27:49+00:00'
updated_at: '2023-10-27T05:33:21+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
IPv6 addresses are supposed to be specified in brackets (although i don't know if it's a requirement).

Run monerod with this command:
`./monerod --testnet --log-level 1 --data-dir /[your directory]/ --rpc-bind-ip 0.0.0.0 --rpc-bind-port 28081 --rpc-use-ipv6 --rpc-bind-ipv6-address [::] --confirm-external-bind`

Logmessage will be:
`2021-09-22 10:13:23.339	I Binding on :: (IPv6):28081`

Monerod should put brackets around the IPv6 address so it should be:
`2021-09-22 10:13:23.339	I Binding on [::] (IPv6):28081`

# Discussion History
## ianebeckett | 2023-10-27T05:33:20+00:00
source: [RFC 5952](https://datatracker.ietf.org/doc/html/rfc5952#section-6)

# Action History
- Created by: li5lo | 2021-09-22T11:27:49+00:00
