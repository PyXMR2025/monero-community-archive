---
title: '[Ledger] Account/Receive page load slow'
source_url: https://github.com/monero-project/monero-gui/issues/2009
author: selsta
assignees: []
labels: []
created_at: '2019-03-11T18:55:43+00:00'
updated_at: '2021-07-02T01:19:16+00:00'
type: issue
status: closed
closed_at: '2021-07-02T01:19:16+00:00'
---

# Original Description
Clicking on these pages has a delay, results in a bad experience.

Probably subaddress related.

# Discussion History
## mmbyday | 2019-03-13T02:09:54+00:00
Same experience here. I think it's the wallet communications with the ledger. Also creating a new account and creating a new address is an order of magnitude slower.  GUI becomes unresponsive :(

## sanderfoobar | 2019-04-10T02:38:48+00:00
This lag is most likely also present in CLI, best to open issue in monero. Re-open if it's accurately GUI related.

+invalid

## selsta | 2019-04-10T02:39:58+00:00
It is a GUI issue though :P The UI loading gets blocked by something subaddress related. Solution would e.g. be load the page first and load the subaddresses afterwards.

## sanderfoobar | 2019-04-10T14:15:35+00:00
oki

+open

## selsta | 2021-07-02T01:19:16+00:00
Will be solved by https://github.com/monero-project/monero/pull/7744 in the future.

# Action History
- Created by: selsta | 2019-03-11T18:55:43+00:00
- Closed at: 2021-07-02T01:19:16+00:00
