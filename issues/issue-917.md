---
title: 'wallet-rpc.md: "restore_height" is defined as a a long integer, but it should
  be defined as an integer'
source_url: https://github.com/monero-project/monero-site/issues/917
author: erciccione
assignees: []
labels:
- '📚 docs: dev guides'
- easy
created_at: '2020-04-12T09:27:47+00:00'
updated_at: '2020-05-02T04:36:47+00:00'
type: issue
status: closed
closed_at: '2020-05-02T04:36:47+00:00'
---

# Original Description
*Issue originally created by @timetherewere*

*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/1068*

---
"restore_height" is labeled "long" but, but it is defined as a "uint64_t" in the wallet-rpc-server.cpp file. 

It should be labeled "integer" in wallet-rpc.md to keep the document self-consistent.

# Discussion History
# Action History
- Created by: erciccione | 2020-04-12T09:27:47+00:00
- Closed at: 2020-05-02T04:36:47+00:00
