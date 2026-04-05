---
title: Question regarding multiple linux miners
source_url: https://github.com/xmrig/xmrig/issues/3077
author: Kryptoknife
assignees: []
labels: []
created_at: '2022-06-22T11:47:24+00:00'
updated_at: '2022-06-22T12:58:41+00:00'
type: issue
status: closed
closed_at: '2022-06-22T12:58:40+00:00'
---

# Original Description
Hey guys I recently decided to try and use my extra servers to mine, I did the stratum strategy, everything seemed to work well and the worker showed up in my nicehash account as -UNMANAGED, when I check active workers I only see 1 even though I have more running off the same command and the same pool 

./xmrig -o stratum+tcp://randomxmonero.auto.nicehash.com:9200 -u (WALLET) -p x -k --nicehash -a rx/0

The first one showed up and started mining left all of them overnight and the hash didnt change from 1 server to the additional 4 i added as a test.. 

What would be a better way to add more workers under -UNMANAGED ? 
Side question is there a way to see when transactions are being made from the linux server side?

# Discussion History
## SChernykh | 2022-06-22T12:47:02+00:00
If you use the same `-u WALLET` for all servers, they'll appear as a single worker with combined hashrate. Use `-u WALLET.server1`, `-u WALLET.server2` and so on to see each server separately.

## Kryptoknife | 2022-06-22T12:58:40+00:00
Thank you thank you! That did exactly what I needed! <3 <3 :+1: :1st_place_medal: 

# Action History
- Created by: Kryptoknife | 2022-06-22T11:47:24+00:00
- Closed at: 2022-06-22T12:58:40+00:00
