---
title: monero-wallet-cli --generate-from-json asks to restore from height when scan_from_height
  is set.
source_url: https://github.com/monero-project/monero/issues/3080
author: mikemhenry
assignees: []
labels:
- bug
created_at: '2018-01-08T01:54:35+00:00'
updated_at: '2018-02-16T13:19:32+00:00'
type: issue
status: closed
closed_at: '2018-02-16T13:19:32+00:00'
---

# Original Description
When using

`monero-wallet-cli --generate-from-json test_wallet.json `

with` test_wallet.json` containing:
```

{
        "version": 1,
        "filename": "test_wallet_json",
        "scan_from_height": 0,
        "password": "",
        "seed": "REDACTED"
}
```

I get
```

Monero 'Helium Hydra' (v0.11.1.0-release)
Logging to ./monero-wallet-cli.log
Restore from specific blockchain height (optional, default 0),
or alternatively from specific date (YYYY-MM-DD):
```
The behavior I expected was if `scan_from_height` is set, for that height to be used and not prompt the user to enter a height or date.


Thanks!


# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:32:35+00:00
+bug

## mikemhenry | 2018-01-08T23:43:17+00:00
To further help triage/diagnose this, I've noticed the same behavior when using the command line argument `--restore-height=0` that is to say, it ignores what I put for the height and asks me for a date or height interactively. 

# Action History
- Created by: mikemhenry | 2018-01-08T01:54:35+00:00
- Closed at: 2018-02-16T13:19:32+00:00
