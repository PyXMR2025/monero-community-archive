---
title: macOS unable to connect to miner with workers.xmrig.info after 6.10.0 update
source_url: https://github.com/xmrig/xmrig/issues/2207
author: AntlerDM
assignees: []
labels:
- bug
created_at: '2021-03-25T04:48:38+00:00'
updated_at: '2021-04-12T13:20:25+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:20:25+00:00'
---

# Original Description
Since upgrading to 6.10.0, I am no longer able to connect via http via http://workers.xmrig.info/ or add the worker. With version 6.9.0 and prior, I simply needed to add the xmrig binary to my firewall exceptions to get it to work. Now, the only option is to disable the firewall.

I am using macOS (Big Sur) and I am using the following command to launch xmrig:
./xmrig --api-worker-id xmrig_V --http-host 0.0.0.0 --http-port 18888 -o 192.168.xx.xx:18089 -u <wallet> --coin monero --daemon

I have tried using different IPs (127.0.0.1, 192.168.xx.xx) and also tried leaving out --http-host entirely.

The release notes for 6.10.0 refer to a change with http parsing. Could this be related?

# Discussion History
## AntlerDM | 2021-03-28T20:08:45+00:00
It seems to be working now. No changes in configuration.

Maybe a change to workers.xmrig.info?

## xmrig | 2021-04-11T11:11:18+00:00
Fixed https://github.com/xmrig/xmrig/releases/tag/v6.11.2

There was a bug when migrating from http parser to llhttp: fragmented on TCP level HTTP requests was parsed incorrectly, only the first chunk of data was parsed.

# Action History
- Created by: AntlerDM | 2021-03-25T04:48:38+00:00
- Closed at: 2021-04-12T13:20:25+00:00
