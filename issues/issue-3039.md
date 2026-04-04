---
title: How does a process start with multiple threads
source_url: https://github.com/monero-project/monero-gui/issues/3039
author: Black52
assignees: []
labels: []
created_at: '2020-08-07T10:17:49+00:00'
updated_at: '2020-09-25T06:08:50+00:00'
type: issue
status: closed
closed_at: '2020-09-25T06:08:50+00:00'
---

# Original Description
watch_only_wallet  rpc Node startup occupies only a single core CPU，And use 100 percent。Nodes often die。
It takes five minutes to create the address。Is there any way to start with multithreading？
My server is 4-core 8GB。
Version used：monero-x86_64-linux-gnu-v0.16.0.1。

# Discussion History
## selsta | 2020-08-07T10:31:20+00:00
Is this GUI or CLI?

## Black52 | 2020-08-10T01:39:13+00:00
> Is this GUI or CLI?
The operating system is ubuntu.
monero-wallet-rpc/monero-wallet-cli Both are slow。

# Action History
- Created by: Black52 | 2020-08-07T10:17:49+00:00
- Closed at: 2020-09-25T06:08:50+00:00
