---
title: monero-wallet-cli didn't respect --do-not-relay flag
source_url: https://github.com/monero-project/monero/issues/7947
author: chaserene
assignees: []
labels: []
created_at: '2021-09-15T13:59:32+00:00'
updated_at: '2022-05-29T15:38:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
0.17.2.3

invoked monero-wallet-cli with --do-not-relay and it still went into in broadcast mode.

my monero-wallet-cli.log contains no corresponding error.

update: I'm still experiencing this with 0.17.3.

# Discussion History
# Action History
- Created by: chaserene | 2021-09-15T13:59:32+00:00
