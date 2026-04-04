---
title: mingw to build dll on windows breaks
source_url: https://github.com/monero-project/monero/issues/4002
author: ajaxwang2020
assignees: []
labels:
- invalid
created_at: '2018-06-15T08:07:05+00:00'
updated_at: '2018-09-14T11:56:59+00:00'
type: issue
status: closed
closed_at: '2018-09-14T11:56:59+00:00'
---

# Original Description
Anybody ever built dlls on windows successfully? It prompts multiple definitions error. After added -Wl,--allow-multiple-definition, I still got the message below:

[ 85%] Linking CXX shared library libp2p.dll
CMakeFiles/p2p.dir/objects.a(net_node.cpp.obj):net_node.cpp:(.data+0x30): undefined reference to `cryptonote::arg_testnet_on'
CMakeFiles/p2p.dir/objects.a(net_node.cpp.obj):net_node.cpp:(.data+0x38): undefined reference to `cryptonote::arg_stagenet_on'

It looks that the cryptonote_core.dll doesn't link correctly. I attached the dll export screenshot.

![dll](https://user-images.githubusercontent.com/18001163/41457413-208eed02-70b6-11e8-9173-7fb2180e8091.png)


# Discussion History
## stoffu | 2018-06-17T05:52:34+00:00
You seem to be trying to build Windows binaries that are dynamically linked which is not supported. Only statically linked build is supported for Windows, where libp2p.a etc are generated instead of libp2p.dll.

## moneromooo-monero | 2018-09-14T11:31:13+00:00
+invalid

# Action History
- Created by: ajaxwang2020 | 2018-06-15T08:07:05+00:00
- Closed at: 2018-09-14T11:56:59+00:00
