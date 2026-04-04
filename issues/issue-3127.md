---
title: Log origin IP in HTTP parsing error messages.
source_url: https://github.com/monero-project/monero/issues/3127
author: ghost
assignees: []
labels:
- easy
created_at: '2018-01-15T16:15:17+00:00'
updated_at: '2018-06-18T15:25:13+00:00'
type: issue
status: closed
closed_at: '2018-06-18T15:25:13+00:00'
---

# Original Description
@hyc encountered the following error after a possible telnet:
```
[RPC1]  ERROR   net.http        contrib/epee/include/net/http_protocol_handler.inl:365  simple_http_connection_handler<t_connection_context>::handle_invoke_query_line(): Failed to match first line: ^V^C
[RPC1]  ERROR   net.http        contrib/epee/include/net/http_protocol_handler.inl:303  simple_http_connection_handler::handle_char_out: Error state!!!
```

The error should at least state the originating IP. We might consider to auto-blacklist these kind of connections after certain amount of attempts.

# Discussion History
## moneromooo-monero | 2018-01-15T16:35:42+00:00
+easy

Can you rename this to something sensible please :) Like, log origin IP in HTTP parsing error messages or somesuch.

## garwahl | 2018-03-21T11:30:48+00:00
I'd like to make an attempt at this if no one has had a shot. Where would I begin?

## moneromooo-monero | 2018-03-22T15:16:34+00:00
Find those messages (git grep). See if you can access the connection context, which holds the IP. Change the log message (there are log macros which automatically use the context to display source).

## moneromooo-monero | 2018-06-18T15:06:51+00:00
+resolved

# Action History
- Created by: ghost | 2018-01-15T16:15:17+00:00
- Closed at: 2018-06-18T15:25:13+00:00
