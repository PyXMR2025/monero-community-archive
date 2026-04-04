---
title: 'Error: failed to load wallet: Wrong Device Status: 0x6f42 (UNKNOWN), EXPECTED
  0x9000 (SW_OK), MASK 0xffff'
source_url: https://github.com/monero-project/monero/issues/7498
author: paedeveloper
assignees: []
labels: []
created_at: '2021-03-10T06:22:21+00:00'
updated_at: '2021-03-10T06:32:48+00:00'
type: issue
status: closed
closed_at: '2021-03-10T06:32:48+00:00'
---

# Original Description
Hello, 

Paired with Ledger Nano S, today I cannot access my hardware wallet from GUI.

I switched to CLI. This is the error.

`Error: failed to load wallet: Wrong Device Status: 0x6f42 (UNKNOWN), EXPECTED 0x9000 (SW_OK), MASK 0xffff`

Can anyone help? :(

Ledger Nano S and CLI are latest version.

# Discussion History
## paedeveloper | 2021-03-10T06:24:26+00:00
now i'm getting this error.

`Error: failed to load wallet: invalid signature`

## paedeveloper | 2021-03-10T06:29:00+00:00
hello! in case anyone gets this, i've fixed the issue. 

`Error: failed to load wallet: invalid signature
Error: You may want to remove the file "<wallet file>" and try again`

this is the error from monero-cli. 

I moved the file to another folder and tried again, and it works! right now, its syncing the wallet blocks again. so I am currently checking if my monero is still there.

## paedeveloper | 2021-03-10T06:32:48+00:00
wallet balance is confirmed successfully. i guess now it's documentation for anyone who has the same issue!

closed.

# Action History
- Created by: paedeveloper | 2021-03-10T06:22:21+00:00
- Closed at: 2021-03-10T06:32:48+00:00
