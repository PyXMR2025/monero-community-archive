---
title: ipv6 bind address doesn't support network mask
source_url: https://github.com/monero-project/monero/issues/7406
author: nick4fake
assignees: []
labels: []
created_at: '2021-02-26T15:25:11+00:00'
updated_at: '2021-03-11T15:36:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
````
p2p-bind-ipv6-address=::1/128
rpc-bind-ipv6-address=::1/128
````

Error:
````
Invalid IP address given for --rpc-bind-ipv6-address
````

# Discussion History
## vdero133 | 2021-03-01T03:29:17+00:00
this error comes from `boost::asio::ip::address::from_string()`. Does asio support subnet masks?

On another note `from_string()` should be changed to `make_address()` as the former is deprecated.

## vtnerd | 2021-03-06T03:22:12+00:00
What is the expected behavior here? To bind every address in the range?

# Action History
- Created by: nick4fake | 2021-02-26T15:25:11+00:00
