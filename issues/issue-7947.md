---
title: monero-wallet-cli didn't respect --do-not-relay flag
source_url: https://github.com/monero-project/monero/issues/7947
author: chaserene
assignees: []
labels: []
created_at: '2021-09-15T13:59:32+00:00'
updated_at: '2026-07-10T16:12:10+00:00'
type: issue
status: closed
closed_at: '2026-07-10T16:12:09+00:00'
---

# Original Description
0.17.2.3

invoked monero-wallet-cli with --do-not-relay and it still went into in broadcast mode.

my monero-wallet-cli.log contains no corresponding error.

update: I'm still experiencing this with 0.17.3.

# Discussion History
## selsta | 2026-07-10T16:12:10+00:00
There are not enough details to reproduce the issue but I assume this was fixed by https://github.com/monero-project/monero/pull/9977

# Action History
- Created by: chaserene | 2021-09-15T13:59:32+00:00
- Closed at: 2026-07-10T16:12:09+00:00
