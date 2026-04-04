---
title: Long wait for response
source_url: https://github.com/monero-project/monero/issues/5038
author: yura-sutnuk
assignees: []
labels: []
created_at: '2019-01-02T15:51:45+00:00'
updated_at: '2019-01-04T16:58:46+00:00'
type: issue
status: closed
closed_at: '2019-01-04T16:58:46+00:00'
---

# Original Description
Hi, i have my wallet-rpc and daemon on a different servers, in my application basically i need only create transaction method and generate new address but avarage time waiting for response is 10-15 seconds. On both servers i have HDD and i have few question:
1) wich one i should upgrade to SSD for speed up?
2) can i some how speed up without upgrade to SSD?

Also can monero proceed several request at one time or it put users in queue?

Monero 'Beryllium Bullet' (v0.13.0.2-release)

# Discussion History
## moneromooo-monero | 2019-01-02T18:10:06+00:00
The blockchain wants to be on a SSD for speed. The wallet file is irrelevant here. Use a recent monero for speedups. If you want to keep using a release, try 0.13.0.4, though I'm not sure how many such speedups it has.
RPC are processed sequentially.



## yura-sutnuk | 2019-01-04T08:32:25+00:00
so i need SSD only for server with daemon? ok thanks.

## yura-sutnuk | 2019-01-04T09:47:49+00:00
can you also say which server requirement have monero for stable work? on your site i see requirement for 2014 year, is they still actual?

## moneromooo-monero | 2019-01-04T13:28:55+00:00
If you're asking about disk space, the db will be about 60 GB to 70 GB, increasing at... half a GB per month I think (very roughly).

## yura-sutnuk | 2019-01-04T16:58:33+00:00
Ok, Thanks 

# Action History
- Created by: yura-sutnuk | 2019-01-02T15:51:45+00:00
- Closed at: 2019-01-04T16:58:46+00:00
