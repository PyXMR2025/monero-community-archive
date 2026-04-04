---
title: send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000),
source_url: https://github.com/monero-project/monero/issues/661
author: Gingeropolous
assignees: []
labels: []
created_at: '2016-02-14T03:31:13+00:00'
updated_at: '2017-02-14T09:48:13+00:00'
type: issue
status: closed
closed_at: '2016-12-15T18:02:49+00:00'
---

# Original Description
0.9.1, set_log 2

`2016-Feb-13 22:27:51.657324 [P2P9]CHECKPOINT PASSED FOR HEIGHT 900000 <d9958d0e7dcf91a5a7b11de225927bf7efc6eb26240315ce12372be902cc1337>
2016-Feb-13 22:27:51.657495 [P2P9]CHECKPOINT PASSED FOR HEIGHT 913193 <5292d5d56f6ba4de33a58d9a34d263e2cb3c6fee0aed2286fd4ac7f36d53c85f>
2016-Feb-13 22:27:51.659772 [P2P9][104.156.227.151:18080 OUT]NOTIFY_NEW_BLOCK (hop 2)
2016-Feb-13 22:27:51.664224 [P2P9]tx <8f822dbae9cc0f78ea75b79732a079782099385c511f826bad4c636ffdb55477> already have transaction in blockchain
2016-Feb-13 22:27:51.665088 [P2P9]tx <ff488d521e932f9d796e93759b9bfd7b7f207063d2cc1cf93ff426e1e0710e0e> already have transaction in blockchain
2016-Feb-13 22:27:51.665973 [P2P9]tx <c39e9e3e7806093984bc1841326238327022617a01787293246571c92740f9ea> already have transaction in blockchain
2016-Feb-13 22:27:51.666536 [P2P9][104.156.227.151:18080 OUT]NOTIFY_NEW_TRANSACTIONS
2016-Feb-13 22:27:51.666713 [P2P9][104.156.227.151:18080 OUT]NOTIFY_NEW_BLOCK (hop 3)
ERROR   {8} {p1} 2016-02-13 22:27:53.591725 [abstract_tcp_server2.inl+494 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
2016-Feb-13 22:27:53.591852 [P2P5][95.49.242.65:49676 INC]Failed to do_send
2016-Feb-13 22:27:53.592045 [P2P5]Failed to invoke command 1002 return code -1
2016-Feb-13 22:27:53.592211 [P2P5][95.49.242.65:49676 INC]COMMAND_TIMED_SYNC invoke failed. (-1, LEVIN_ERROR_CONNECTION)
2016-Feb-13 22:27:53.592432 [P2P5]Failed to invoke command 1002 return code 0
2016-Feb-13 22:27:53.592594 [P2P5][95.49.242.65:49676 INC]COMMAND_TIMED_SYNC Failed
2016-Feb-13 22:27:53.596195 [P2P5]FINISHED PEERLIST IDLE HANDSHAKE
set_lo2016-Feb-13 22:27:56.342053 [P2P0][108.83.181.106:34606 INC]NOTIFY_NEW_TRANSACTIONS`


# Discussion History
## Gingeropolous | 2016-10-04T02:27:40+00:00
I also haven't seen this error in a while. I can close unless someone says otherwise. 


## assylias | 2017-02-14T09:44:35+00:00
@Gingeropolous I installed a full node on a new machine last night and got the error:

    2017-Feb-13 21:38:01.615331 [P2P9][xx.xx.xx.xx:18080 OUT] SYNCHRONIZED OK
    ERROR   {2} {p1} 2017-02-13 23:04:31.895879 [abstract_tcp_server2.inl+515 ::do_send_chunk] send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(1000), shutting down connection
    2017-Feb-13 23:29:57.773226 [P2P0][xx.xx.xx.xx:18080 OUT]Synced 1245516/1245516

I would suggest at least rewording the message: for a layman, it is quite unclear what this error means.

Version:

    ./monerod --version
    Creating the logger system
    Monero 'Wolfram Warptangent' (v0.10.1.0-release)

# Action History
- Created by: Gingeropolous | 2016-02-14T03:31:13+00:00
- Closed at: 2016-12-15T18:02:49+00:00
