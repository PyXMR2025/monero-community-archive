---
title: When running simplewallet with --wallet-file flag, the check whether the file
  exists is done after asking user for the password
source_url: https://github.com/monero-project/monero-gui/issues/21
author: JollyMort
assignees: []
labels: []
created_at: '2016-09-12T18:55:11+00:00'
updated_at: '2016-09-13T04:11:29+00:00'
type: issue
status: closed
closed_at: '2016-09-13T04:11:29+00:00'
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
## mbg033 | 2016-09-12T21:28:55+00:00
Perhaps you want to submit issue here: https://github.com/monero-project/monero/issues


## JollyMort | 2016-09-13T04:11:29+00:00
You're right, I messed up - sorry


# Action History
- Created by: JollyMort | 2016-09-12T18:55:11+00:00
- Closed at: 2016-09-13T04:11:29+00:00
