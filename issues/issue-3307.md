---
title: Request for Windows debug builds on buildbot
source_url: https://github.com/xmrig/xmrig/issues/3307
author: koitsu
assignees: []
labels: []
created_at: '2023-07-22T18:40:20+00:00'
updated_at: '2023-11-19T00:48:08+00:00'
type: issue
status: closed
closed_at: '2023-11-19T00:48:07+00:00'
---

# Original Description
Hi SChe, I was wondering if you could add to your buildbot configuration debug version for Windows (MSVC or GCC is fine), specifically with `-DWITH_DEBUG_LOG=ON` ?

I'm helping Zergpool debug a problem that happens intermittently only on some of their GPU pool TLS/SSL endpoints.  I've done packet captures on the client side, and can see that there is some application payload returned to the client before the server sends FIN+ACK to close the socket.  But because of encrypted payload, I can't use Wireshark to see what's going on.

I'd build a binary myself under MSYS2 except there's no documentation that I could find on what the required versions of XMRig's dependencies are (i.e. CMake, GCC, libuv, hwloc, etc.).

If adding this to buildbot long-term isn't an option, that's fine too -- in which case, could you do me a favour and do a one-off debug build of 6.20.1-dev for MSVC onto https://download.xmrig.com/ ?  That would make my life a lot easier.  Otherwise I have to end up writing my own JSON-RPC client and try to mimic what I see on plaintext.

Thanks!


# Discussion History
## koitsu | 2023-11-19T00:48:07+00:00
No longer have need for this, although I do emphasise that having clear docs on what prereqs/versions are needed would be best.

# Action History
- Created by: koitsu | 2023-07-22T18:40:20+00:00
- Closed at: 2023-11-19T00:48:07+00:00
