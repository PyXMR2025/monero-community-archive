---
title: When running simplewallet with --wallet-file flag, the check whether the file
  exists is done after asking user for the password
source_url: https://github.com/monero-project/monero/issues/1071
author: JollyMort
assignees: []
labels:
- enhancement
created_at: '2016-09-13T04:12:59+00:00'
updated_at: '2018-12-07T15:01:19+00:00'
type: issue
status: closed
closed_at: '2018-12-07T15:01:19+00:00'
---

# Original Description
C&p of command prompt below. System: Windows 7 x64. Version: monero.win.x64.v0-9-4-0

I believe it would make sense to check for the file first, before asking the user for the password.

```
C:\monero.win.x64.v0-9-4-0>simplewallet --wallet-file test
Creating the logger system
Monero 'Hydrogen Helix' (v0.9.4.0-release)
Logging at log level 0 to C:\monero.win.x64.v0-9-4-0\simplewallet.log
password: ****
Error: failed to load wallet: file not found "test.keys"
```


# Discussion History
## moneromooo-monero | 2016-09-21T20:20:35+00:00
Is the problem just wasted work (inputting a password), or something else ?


## JollyMort | 2016-09-24T10:35:14+00:00
Yeah only that, just an user experience thing.


## dEBRUYNE-1 | 2018-01-08T12:43:29+00:00
+enhancement

## selsta | 2018-12-07T13:46:18+00:00
This is fixed in recent versions.

## dEBRUYNE-1 | 2018-12-07T14:56:16+00:00
+resolved

# Action History
- Created by: JollyMort | 2016-09-13T04:12:59+00:00
- Closed at: 2018-12-07T15:01:19+00:00
