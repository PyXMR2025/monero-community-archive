---
title: Hi it say "Connection refused" Solo mining
source_url: https://github.com/xmrig/xmrig/issues/2595
author: KeparYTbcc
assignees: []
labels: []
created_at: '2021-09-22T05:06:35+00:00'
updated_at: '2021-09-25T21:54:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`@echo off
xmrig.exe --cuda -o 127.0.0.1:18081 -u 441H6vTAJdQdtBUnFeazh5CeZtqsWrWsSbwezbpiTeTnBYsdrxYqd7uS6UfSeTqzteZ6sfC2Bqf6UXaL6DrNfNLxKad7mMP --coin monero --daemon
pause`
![unknown](https://user-images.githubusercontent.com/67996155/134286443-8be91e54-22e2-4b07-8fd3-48119d36ef7f.png)


# Discussion History
## toy1111 | 2021-09-25T21:54:52+00:00
For solo mining you also need to run your own local monero node at the port you are telling xmrig to connect to (in this case 18081). The xmrig is only the miner, it doesn't also run the coin's node that's sync'ing with the blockchain.

# Action History
- Created by: KeparYTbcc | 2021-09-22T05:06:35+00:00
