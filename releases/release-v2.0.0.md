---
title: v2.0.0
type: release
source_url: https://github.com/xmrig/xmrig/releases/tag/v2.0.0
author: xmrig
tag_name: v2.0.0
published_at: '2017-07-03T03:34:17+00:00'
---

# Version: v2.0.0

# Release Notes
 - Option `--backup-url` removed, instead now possibility specify multiple pools for example: `-o example1.com:3333 -u user1 -p password1 -k -o example2.com:5555 -u user2 -o example3.com:4444 -u user3`
 - [#15](https://github.com/xmrig/xmrig/issues/15) Added option `-l, --log-file=FILE` to write log to file.
 - [#15](https://github.com/xmrig/xmrig/issues/15) Added option `-S, --syslog` to use syslog for logging, Linux only.
 - [#18](https://github.com/xmrig/xmrig/issues/18) Added nice messages for accepted/rejected shares with diff and network latency.
 - [#20](https://github.com/xmrig/xmrig/issues/20) Fixed `--cpu-affinity` for more than 32 threads.
 - Fixed Windows XP support.
 - Fixed regression, option `--no-color` was not fully disable colored output.
 - Show resolved pool IP address in miner output.