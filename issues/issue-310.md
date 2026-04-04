---
title: testnet error
source_url: https://github.com/monero-project/monero/issues/310
author: Gingeropolous
assignees: []
labels: []
created_at: '2015-06-05T21:55:03+00:00'
updated_at: '2015-06-11T03:26:10+00:00'
type: issue
status: closed
closed_at: '2015-06-11T03:25:20+00:00'
---

# Original Description
id:     <252f2344fd8560c51b3d492d69b3deec92f9b4cfa69a562584b26559fda4a6f6>
PoW:    <d83033d52d5cd0c857a4d12720781f8c2433ef3d3545bac64c2723d0f19f3a00>
HEIGHT 380108, difficulty:      715
block reward: 12.243040181841(12.243040181841 + 0.000000000000), coinbase_blob_size: 239, cumulative size: 239, 83(3/79)ms
2015-Jun-05 17:52:55.918690 [miner 0]MINING RESUMED
2015-Jun-05 17:52:55.919000 [miner 0][0.0.0.0:0 OUT] post relay N10cryptonote16NOTIFY_NEW_BLOCKE -->
ERROR   {13} {p1} 2015-06-05 17:53:01.763661 [abstract_tcp_server2.inl+489 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
2015-Jun-05 17:53:01.763783 [miner 0][178.62.50.85:28080 OUT]Failed to do_send()
ERROR   {13} {p1} 2015-06-05 17:53:07.455565 [abstract_tcp_server2.inl+489 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
2015-Jun-05 17:53:07.455677 [miner 0][104.152.212.170:28080 OUT]Failed to do_send()
ERROR   {13} {p1} 2015-06-05 17:53:13.123122 [abstract_tcp_server2.inl+489 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
2015-Jun-05 17:53:13.123227 [miner 0][104.152.213.138:28080 OUT]Failed to do_send()
2015-Jun-05 17:53:32.862582 [miner 0]Found block for difficulty: 716
2015-Jun-05 17:53:32.862876 [miner 0]MINING PAUSED
2015-Jun-05 17:53:33.350637 [miner 0]+++++ BLOCK SUCCESSFULLY ADDED
id:     <e655c593947452d6dfa6b9d791b79bb70d8982a71a3b4e176f937af4c83bdcf3>
PoW:    <a5d1a51759eed788fc6f29631ff0ce60a9acd0522767a72be97b67cb88520000>
HEIGHT 380109, difficulty:      716


# Discussion History
## Gingeropolous | 2015-06-08T11:31:33+00:00
might be related to #309 


## Gingeropolous | 2015-06-11T03:25:20+00:00
fixed with make release-static-64. Actually, I didn't test if this hasn't popped up again, I just assume that its the same problem I had with my other issues. 


# Action History
- Created by: Gingeropolous | 2015-06-05T21:55:03+00:00
- Closed at: 2015-06-11T03:25:20+00:00
