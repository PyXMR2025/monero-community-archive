---
title: FreeBSD "Listen queue overflow" issues
source_url: https://github.com/monero-project/monero/issues/8210
author: camberkenpas
assignees: []
labels: []
created_at: '2022-03-07T18:02:07+00:00'
updated_at: '2022-05-29T15:33:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After running monerod (through the FreeBSD port), I get these messages:
sonewconn: pcb 0xfffff804083a3d58 (0.0.0.0:18080 (proto 6)): Listen queue overflow: 193 already in queue awaiting acceptance (34 occurrences)
sonewconn: pcb 0xfffff804083a3d58 (0.0.0.0:18080 (proto 6)): Listen queue overflow: 193 already in queue awaiting acceptance (21 occurrences)
sonewconn: pcb 0xfffff804083a3d58 (0.0.0.0:18080 (proto 6)): Listen queue overflow: 193 already in queue awaiting acceptance (23 occurrences)
sonewconn: pcb 0xfffff804083a3d58 (0.0.0.0:18080 (proto 6)): Listen queue overflow: 193 already in queue awaiting acceptance (25 occurrences)
sonewconn: pcb 0xfffff804083a3d58 (0.0.0.0:18080 (proto 6)): Listen queue overflow: 193 already in queue awaiting acceptance (24 occurrences)

I set kern.ipc.soacceptqueue=16384 set in /etc/sysctl.conf (and applied the change) and this still happens.

Any idea what's wrong?

This could potentially be due to running monerod in a jail. Currently, I can't run monerod directly on the machine as I *need* libressl and monerod currently isn't compatible with libressl.

monerod --version
Monero 'Oxygen Orion' (v0.17.3.0-release)


# Discussion History
## camberkenpas | 2022-03-07T18:03:58+00:00
After restarting monerod, it doesn't seem like this issue starts immediately, but it seems it also doesn't take too long. I restarted the daemon this morning and received another such message around 20-30 minutes later.

When this happens, monero-wallet-cli stalls when trying to connect to the daemon.

# Action History
- Created by: camberkenpas | 2022-03-07T18:02:07+00:00
