---
title: 'Silly compiler error: ‘payment_id_seen’ set but not used'
source_url: https://github.com/monero-project/monero/issues/1226
author: ghost
assignees: []
labels: []
created_at: '2016-10-15T22:32:35+00:00'
updated_at: '2016-10-16T10:29:39+00:00'
type: issue
status: closed
closed_at: '2016-10-16T10:29:39+00:00'
---

# Original Description
`monero/src/simplewallet/simplewallet.cpp: In member function ‘bool cryptonote::simple_wallet::locked_transfer(const std::vector<std::__cxx11::basic_string<char> >&)’:`

`monero/src/simplewallet/simplewallet.cpp:2660:8: warning: variable ‘payment_id_seen’ set but not used [-Wunused-but-set-variable]  bool payment_id_seen = false;`

But it is used! Stupid compiler...


# Discussion History
## moneromooo-monero | 2016-10-16T08:56:40+00:00
It's not an error, and the compiler means "not used beyond setting". The reason is in my 1179 comments, but this got merged before I could comment. Hopefully the author might fix, or I'll do it at some point.


## ghost | 2016-10-16T10:29:39+00:00
Hope so too after reviewing your comments.


# Action History
- Created by: ghost | 2016-10-15T22:32:35+00:00
- Closed at: 2016-10-16T10:29:39+00:00
