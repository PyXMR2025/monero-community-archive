---
title: Sent transaction is not visible in the "Transactions" section until first confirmation
source_url: https://github.com/monero-project/monero-gui/issues/3967
author: Akira45-0
assignees: []
labels: []
created_at: '2022-07-10T04:56:28+00:00'
updated_at: '2022-07-13T05:41:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hello. I am using Monero Gui 0.17.3.2-release (Qt 5.15.3) running on Linux in Advanced mode (Local node).

When I send XMR the transaction is not visible in the "Transactions" section until first confirmation. I think it should be visible with "Pending" status, like it used to be. This is not only annoying, but confusing.

How to make pending sent transactions visible again?

# Discussion History
## selsta | 2022-07-11T17:44:53+00:00
When did this start happening to you? I don't think anything was changed in this regard. Did you change the sorting on the transactions page?

## Akira45-0 | 2022-07-11T18:07:26+00:00
I didn't change anything. It's hard to say when it did start happening, because I used previous Monero Gui versions on Windows and haven't had this problem. I have this problem since I moved to Linux and 0.17.3-2

## selsta | 2022-07-12T02:06:39+00:00
Do you have failed transactions in your transaction history?

## Akira45-0 | 2022-07-12T07:31:15+00:00
No, it doesn't look like this. Everything looks ordinary.

## Akira45-0 | 2022-07-13T05:39:10+00:00
There's a lot of warnings like this (censored for privacy)
[log.txt](https://github.com/monero-project/monero-gui/files/9099226/log.txt)


# Action History
- Created by: Akira45-0 | 2022-07-10T04:56:28+00:00
