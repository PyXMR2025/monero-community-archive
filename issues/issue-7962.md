---
title: 'Windows10, precompiled bins, running local pruned node, monerod exits it self
  quietly at log : D do_send() will SPLIT into small chunks, from packet=72712 B for
  ptr='
source_url: https://github.com/monero-project/monero/issues/7962
author: MXS2514
assignees: []
labels: []
created_at: '2021-09-21T07:25:26+00:00'
updated_at: '2021-10-01T03:15:50+00:00'
type: issue
status: closed
closed_at: '2021-10-01T03:15:49+00:00'
---

# Original Description
My ip is p2p friendly, from latest 2-3 of version, monerod often exits it self, hard to trace.
Setting log level to 3 or 4 indecates:

> 2021-09-20 11:43:47.454 D do_send() will SPLIT into small chunks, from packet=72712 B for ptr=?!??????鐩?

this line before crash

Tried cmd line:
`monerod.exe --data-dir=.\ --block-sync-size 10 --limit-rate=400 --max-concurrency=1 --enable-dns-blocklist --rpc-bind-port 38380 --restricted-rpc --db-sync-mode safe:sync `
seemed have no effect.

_BUT_ on my another net location machine, it worked quite steady, **NAT under router**.
Any clues?
[log1.txt](https://github.com/monero-project/monero/files/7201130/log1.txt)
[log2.txt](https://github.com/monero-project/monero/files/7201133/log2.txt)
[log3.txt](https://github.com/monero-project/monero/files/7201134/log3.txt)



# Discussion History
## selsta | 2021-09-22T20:15:19+00:00
Can you compile master binary and redo this test?

## MXS2514 | 2021-09-24T06:31:13+00:00
> Can you compile master binary and redo this test?

Compiled from master monerod.exe v0.17.0.0-a39b1d56c
Already keep running over 24hrs, will continue keeping on eye.

## MXS2514 | 2021-10-01T03:15:49+00:00
Tested 10 days, no issue anymore, haven't clues, closed.

# Action History
- Created by: MXS2514 | 2021-09-21T07:25:26+00:00
- Closed at: 2021-10-01T03:15:49+00:00
