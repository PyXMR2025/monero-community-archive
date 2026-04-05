---
title: XMR + Docker + Gvisor = crash
source_url: https://github.com/xmrig/xmrig/issues/2854
author: Supernaut90
assignees: []
labels: []
created_at: '2022-01-02T19:24:14+00:00'
updated_at: '2022-01-05T00:40:30+00:00'
type: issue
status: closed
closed_at: '2022-01-05T00:40:30+00:00'
---

# Original Description

this image runs fine locally using docker, but when opened in a container using gvisor it crashes.

install docker, run `docker run -it cryptoandcoffee/cpu-moneroocean` everything should work fine
install gvisor/runsc , then `docker run --runtime=runsc -it cryptoandcoffee/cpu-moneroocean` it should give you an error looking something like `/root/moneroocean/miner.sh: line 7:  4755 Aborted                 nice /root/moneroocean/xmrig $*` on one of the benchmarks



# Discussion History
# Action History
- Created by: Supernaut90 | 2022-01-02T19:24:14+00:00
- Closed at: 2022-01-05T00:40:30+00:00
