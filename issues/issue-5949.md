---
title: 'error: implicitly-declared‘hw::ledger::ABPkeys& hw::ledger::ABPkeys::operator='
source_url: https://github.com/monero-project/monero/issues/5949
author: moneroexamples
assignees: []
labels: []
created_at: '2019-10-01T12:12:00+00:00'
updated_at: '2019-10-01T13:19:43+00:00'
type: issue
status: closed
closed_at: '2019-10-01T13:19:43+00:00'
---

# Original Description
Getting the following error on Arch linux with gcc 9.1

```
c++: warning: switch ‘-mmitigate-rop’ is no longer supported
/home/mwo2/monero/src/device/device_ledger.cpp: In member function ‘bool hw::ledger::Keymap::find(const rct::key&, hw::ledger::ABPkeys&) const’:
/home/mwo2/monero/src/device/device_ledger.cpp:98:23: error: implicitly-declared ‘hw::ledger::ABPkeys& hw::ledger::ABPkeys::operator=(const hw::ledger::ABPkeys&)’ is deprecated [-Werror=deprecated-copy]
   98 |           keys = ABP[i];
      |                       ^
/home/mwo2/monero/src/device/device_ledger.cpp:83:5: note: because ‘hw::ledger::ABPkeys’ has user-provided ‘hw::ledger::ABPkeys::ABPkeys(const hw::ledger::ABPkeys&)’
   83 |     ABPkeys::ABPkeys(const ABPkeys& keys) {
      |     ^~~~~~~
```

# Discussion History
## moneromooo-monero | 2019-10-01T12:49:10+00:00
Are you sure you not testing old code ? That was supposed to be fixed a while ago.

## moneroexamples | 2019-10-01T13:19:43+00:00
You right!. Thank you.

# Action History
- Created by: moneroexamples | 2019-10-01T12:12:00+00:00
- Closed at: 2019-10-01T13:19:43+00:00
