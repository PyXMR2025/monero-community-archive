---
title: 'monerod RPC: limit limit_up limit_down invalid value'
source_url: https://github.com/monero-project/monero/issues/3051
author: jkasarherou
assignees: []
labels: []
created_at: '2018-01-03T10:35:37+00:00'
updated_at: '2018-02-18T19:32:36+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:32:36+00:00'
---

# Original Description
Hi!
when using `limit_up` I got this:
```
limit_up 99999999
Set limit-up to -663297 kB/s
```

Looks like a classic signed/unsigned mixup.

# Discussion History
## jkasarherou | 2018-01-03T10:38:25+00:00
```
$ monerod --version
Monero 'Helium Hydra' (v0.11.1.0-release)
$ monerod --os-version
OS: Darwin Darwin Kernel Version 17.2.0: Fri Sep 29 18:27:05 PDT 2017; root:xnu-4570.20.62~3/RELEASE_X86_64 17.2.0
```

## Sylvyrfysh | 2018-01-05T03:02:35+00:00
#3068 implements a fix

## moneromooo-monero | 2018-02-18T19:24:43+00:00
+resolved

# Action History
- Created by: jkasarherou | 2018-01-03T10:35:37+00:00
- Closed at: 2018-02-18T19:32:36+00:00
