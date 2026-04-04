---
title: Cannot start local Monerod on Ubuntu 20
source_url: https://github.com/monero-project/monero-gui/issues/3355
author: vanthome
assignees: []
labels: []
created_at: '2021-03-14T09:38:23+00:00'
updated_at: '2022-04-26T18:37:10+00:00'
type: issue
status: closed
closed_at: '2022-04-26T18:37:10+00:00'
---

# Original Description
When I use the downloaded version, the daemon seems not to work:

```
2021-03-13 19:30:46.722 I Monero 'Oxygen Orion' (v0.17.1.9-release)
2021-03-13 19:30:46.722 I Initializing cryptonote protocol...
2021-03-13 19:30:46.722 I Cryptonote protocol initialized OK
2021-03-13 19:30:46.722 I Initializing core...
2021-03-13 19:30:46.722 I Loading blockchain from folder /home/xxxx/.bitmonero/lmdb ...
2021-03-13 19:30:46.722 I Stopping cryptonote protocol...
2021-03-13 19:30:46.722 I Cryptonote protocol stopped successfully
2021-03-13 19:30:46.723 E Exception in main! locale::facet::_S_create_c_locale name not valid
```

# Discussion History
## selsta | 2021-03-14T12:33:37+00:00
Does this happen if you start monerod manually? If yes, please report to monero repo as this is not GUI related.

## selsta | 2021-04-21T02:00:10+00:00
https://monero.stackexchange.com/a/12433 seems related

## selsta | 2022-04-26T18:37:10+00:00
No reply, closing.

# Action History
- Created by: vanthome | 2021-03-14T09:38:23+00:00
- Closed at: 2022-04-26T18:37:10+00:00
