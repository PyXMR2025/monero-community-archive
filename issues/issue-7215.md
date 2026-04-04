---
title: monero-wallet-rpc stuck at "Starting wallet RPC server"
source_url: https://github.com/monero-project/monero/issues/7215
author: vceylan
assignees: []
labels: []
created_at: '2020-12-28T14:18:38+00:00'
updated_at: '2020-12-28T19:34:29+00:00'
type: issue
status: closed
closed_at: '2020-12-28T19:34:29+00:00'
---

# Original Description
I upgraded monero node successfully and can get latest block etc. info. When i try start wallet rpc it is showing info below and not continue:

![image](https://user-images.githubusercontent.com/4114128/103220028-47fdb800-4930-11eb-8fe3-676f90a8e7d7.png)

This is my config file:

![image](https://user-images.githubusercontent.com/4114128/103220087-724f7580-4930-11eb-8d84-6250f4adfeef.png)

Please help!

# Discussion History
## moneromooo-monero | 2020-12-28T17:05:45+00:00
Post the JSON you're sending as well as the response you get (or whether it times out without a response).

## vceylan | 2020-12-28T19:34:28+00:00
Thanks for your reply. My problem was on connection to wallet. i didn't open wallet from my integration and couldn't connect.
My installation was correct.

# Action History
- Created by: vceylan | 2020-12-28T14:18:38+00:00
- Closed at: 2020-12-28T19:34:29+00:00
