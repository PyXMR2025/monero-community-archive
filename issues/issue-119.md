---
title: 'monerod: MONERO_RANDOMX_FULL_MEM'
source_url: https://github.com/monero-project/monero-docs/issues/119
author: plowsof
assignees: []
labels: []
created_at: '2025-01-01T13:14:01+00:00'
updated_at: '2025-04-22T02:19:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
<sech1> neromonero1024 yes, you can make your Monero node to verify RandomX hashes in fast mode
<sech1> see https://github.com/monero-project/monero/pull/8677
<sech1> set MONERO_RANDOMX_FULL_MEM environment variable to 1 before running monerod
<sech1> or run it like "MONERO_RANDOMX_FULL_MEM=1 ./monerod ..."
<sech1> ofrnxmr ^
...
<sech1> It just increases memory requirements by 2 GB
```

Environment variable added to systemd:
```
[Service]
Environment=MONERO_RANDOMX_FULL_MEM=1
```
https://libera.monerologs.net/monero-dev/20240922#c432858


# Discussion History
## nahuhh | 2025-04-22T02:19:44+00:00
fwiw, I tested this on a few runs and had the sync crash a few times, and didn't notice any difference in performance

# Action History
- Created by: plowsof | 2025-01-01T13:14:01+00:00
