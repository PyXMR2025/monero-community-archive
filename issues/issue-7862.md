---
title: 'cli: under Void & Mint Linux, the text remains bold after calling rpc --help'
source_url: https://github.com/monero-project/monero/issues/7862
author: mj-xmr
assignees: []
labels: []
created_at: '2021-08-15T12:08:00+00:00'
updated_at: '2021-09-09T19:20:52+00:00'
type: issue
status: closed
closed_at: '2021-09-09T19:20:52+00:00'
---

# Original Description
Reported by @sausagenoods .

Reproducible via the distributed Void package, [using tag: 0.17.2.0 ](https://github.com/void-linux/void-packages/blob/934ce39e13fd90021f43c2a5749e1252d73f8380/srcpkgs/monero/template) as well as on `master` at the time of writing (15.08.2021 82149bfe4) under Void Linux:

```bash
./monero-walled-rpc --help
ps # Font stays bold
ps # Font stays bold
ls # Font resets and is not bold anymore
ps # Font is not bold anymore
```

# Discussion History
## sausagenoods | 2021-08-15T14:03:48+00:00
Also reproducible via the precompiled binaries from getmonero.org (v0.17.2.0) under Linux Mint:
`./monero-wallet-rpc --help && ps`
The output from `ps` command will be in bold. When run as two seperate commands the font will only be restored if the PS1 contains the reset escape code.

Edit: typo.

# Action History
- Created by: mj-xmr | 2021-08-15T12:08:00+00:00
- Closed at: 2021-09-09T19:20:52+00:00
