---
title: monero-wallet-cli's generate-from-json with password is broken
source_url: https://github.com/monero-project/monero/issues/4480
author: xnum
assignees: []
labels: []
created_at: '2018-10-01T08:20:53+00:00'
updated_at: '2018-10-02T20:57:01+00:00'
type: issue
status: closed
closed_at: '2018-10-02T20:57:01+00:00'
---

# Original Description
version: `release-v0.13`

execute `monero-wallet-cli --testnet --generate-from-json data.json` with following content in `data.json`

```
{"version":1,"filename":"/tmp/xmr.keys","scan_from_height":0,"password":"xxxxxxxx","viewkey":"...","spendkey":"...","address":"9x...."}
```
after the keys file was generated, open wallet with this file. 

`monero-wallet-cli --testnet --wallet-file xmr.keys`. 

I typed the password which is same as json specifics. then It always shows `Error: failed to load wallet: invalid password`

and demo here https://asciinema.org/a/IQYG6DKnjwLqvzP4vowzZCSiO

# Discussion History
## moneromooo-monero | 2018-10-01T11:21:09+00:00
https://github.com/monero-project/monero/pull/4482

## moneromooo-monero | 2018-10-02T20:50:11+00:00
+resolved

# Action History
- Created by: xnum | 2018-10-01T08:20:53+00:00
- Closed at: 2018-10-02T20:57:01+00:00
