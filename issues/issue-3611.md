---
title: local area network (LAN) xmrig monitoring?
source_url: https://github.com/xmrig/xmrig/issues/3611
author: dchmelik
assignees: []
labels: []
created_at: '2024-12-31T10:00:52+00:00'
updated_at: '2024-12-31T10:14:17+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**describe the bug (feature request)**
One can't monitor xmrig (well) on local area network (LAN) (shows JSON, error 401); remote monitoring is less usable/secure: can't mass-configure (one .conf for all) with multiple workers/ports, and less secure than closed ports.

**expected behaviour**
Run a HTTPD regularly updating detailed plaintext/webpage status not requiring authentication (on LAN).  Consider optional/integrated [xmrig-monitor](http://github.com/bitlamas/xmrig-monitor) [fork](http://github.com/JaymZZZZ/xmrig-monitor) if still works/continues (GPL3).

**required data**
 - XMRig version: some from 2023 through [6.21.3](http://github.com/xmrig/xmrig/archive/v6.21.3/xmrig-6.21.3.tar.gz) ([SlackBuild](http://slackbuilds.org/repository/15.0/network/xmrig)), [6.22.2](http://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-linux-static-x64.tar.gz) ([2](http://github.com/xmrig/xmrig/releases/download/v6.22.2/xmrig-6.22.2-noble-x64.tar.gz)) (Debian-/Ubuntu-based)
 - OS: UNIX/GNU/Linux: Slackware (stable & current), FreeBSD (in past), Devuan (in past) & *ubuntu-based (KDE Neon, Mint XFCE, Xubuntu)

**additional context**
Older miner xmr-stak-rx (no longer compiles since 2023) has its own (or optional) HTTPD not requiring authentication (on LAN) so miners who used to use it consider the feature basic/essential/standard.

# Discussion History
# Action History
- Created by: dchmelik | 2024-12-31T10:00:52+00:00
