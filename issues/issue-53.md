---
title: Bitmonerod send ERROR
source_url: https://github.com/monero-project/monero/issues/53
author: spr0cker
assignees: []
labels: []
created_at: '2014-06-25T16:15:59+00:00'
updated_at: '2014-08-02T09:20:25+00:00'
type: issue
status: closed
closed_at: '2014-08-02T09:20:25+00:00'
---

# Original Description
[P2P0]ERROR /bitmonero/contrib/epee/include/net/abstract_tcp_server2.inl:307 send que size is more than ABSTRACT_SERVER_SEND_QUE_MAX_COUNT(100), shutting down connection
 [P2P0]ERROR /bitmonero/contrib/epee/include/net/levin_protocol_handler_async.h:638 [174.3.102.122:18080 OUT]Failed to do_send()

How can fix this? 


# Discussion History
## fluffypony | 2014-08-02T09:20:25+00:00
This isn't failing to send a transaction, it's failing to send data to a peer. We are changing the logging levels and changing the p2p queueing so that this won't occur often and won't be visible if it does occur. More specifically, this isn't an error, it's a notice, so even the wording is incorrect on the message:)


# Action History
- Created by: spr0cker | 2014-06-25T16:15:59+00:00
- Closed at: 2014-08-02T09:20:25+00:00
