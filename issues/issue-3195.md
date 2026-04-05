---
title: 'Enhancement: failed pool connections should show IP address '
source_url: https://github.com/xmrig/xmrig/issues/3195
author: koitsu
assignees: []
labels:
- enhancement
created_at: '2023-01-11T07:41:34+00:00'
updated_at: '2023-04-29T05:52:43+00:00'
type: issue
status: closed
closed_at: '2023-04-29T05:52:43+00:00'
---

# Original Description
**Describe the bug**
Currently when xmrig attempts to connect to a pool and the pool is down (e.g. daemon isn't running), it emits a log line like this:

```
[2023-01-10 23:27:03.889]  net      us-west.flockpool.com:5555 connect error: "connection refused"
```

It would be useful if xmrig would disclose what IP address it was trying to connect to on failures.  This is useful for cases where pools uses RR (round-robin) A records -- in this example, us-west.flockpool.com does -- when only one of the A records is unreachable.  Example:

```
$ dig a us-west.flockpool.com +short
154.53.60.5
154.53.62.186
154.53.59.252
$ nc -v 154.53.60.5 5555
Connection to 154.53.60.5 5555 port [tcp/*] succeeded!
^C
$ nc -v 154.53.62.186 5555
Connection to 154.53.62.186 5555 port [tcp/*] succeeded!
^C
$ nc -v 154.53.59.252 5555
nc: connect to 154.53.59.252 port 5555 (tcp) failed: Connection refused
```

In other words, this log line (or variation of sorts) would be more useful:

```
[2023-01-10 23:27:03.889]  net      us-west.flockpool.com:5555 154.53.59.252 connect error: "connection refused"
```


**Required data**
 - Miner log as text or screenshot: see above
 - Config file or command line (without wallets): irrelevant
 - OS: Windows x64, Linux (jammy and focal), etc.


# Discussion History
## SChernykh | 2023-01-11T08:31:12+00:00
Fixed in #3196 

## koitsu | 2023-04-29T05:52:43+00:00
Confirmed working in version 6.19.2 through a basic test (port # intentionally incorrect):
```
[2023-04-28 22:51:31.003]  net      us-west.flockpool.com:5559 85.239.233.157 connect error: "connection refused"
```
Thank you!

# Action History
- Created by: koitsu | 2023-01-11T07:41:34+00:00
- Closed at: 2023-04-29T05:52:43+00:00
