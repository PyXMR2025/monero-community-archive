---
title: 'computer reboots after 5 minutes of xmrig working '
source_url: https://github.com/xmrig/xmrig/issues/1802
author: chamuridis
assignees: []
labels:
- stability
created_at: '2020-08-06T14:57:10+00:00'
updated_at: '2020-08-31T05:46:24+00:00'
type: issue
status: closed
closed_at: '2020-08-31T05:46:24+00:00'
---

# Original Description
I use Linux s 5.4.34-1-pve with 3900x ryzen 
Im getting this error and after my pc reboots 


Message from syslogd@s at Aug  6 17:29:02 ...
 kernel:[  316.593422] [Hardware Error]: Corrected error, no action required.

Message from syslogd@s at Aug  6 17:29:02 ...
 kernel:[  316.593426] [Hardware Error]: CPU:0 (17:71:0) MC27_STATUS[-|CE|MiscV|-|-|-|SyndV|-|-|-]: 0x982000000002080b

Message from syslogd@s at Aug  6 17:29:02 ...
 kernel:[  316.593430] [Hardware Error]: IPID: 0x0001002e00000500, Syndrome: 0x000000005a020005

Message from syslogd@s at Aug  6 17:29:02 ...
 kernel:[  316.593432] [Hardware Error]: Power, Interrupts, etc. Ext. Error Code: 2, Link Error.

Message from syslogd@s at Aug  6 17:29:02 ...
 kernel:[  316.593435] [Hardware Error]: cache level: L3/GEN, mem/io: IO, mem-tx: GEN, part-proc: SRC (no timeout)


# Discussion History
## Lonnegan | 2020-08-07T12:00:09+00:00
Seems to be a hardware issue, because the system detected a CRC error, which it firstly could fix, but then led to a kernel panic. Do stability test-tools like Prime95 or memtest run smoothly without errors for hours?
https://www.mersenne.org/download/#stresstest
https://www.memtest86.com/
Please try first.

## xmrig | 2020-08-31T05:46:24+00:00
https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

# Action History
- Created by: chamuridis | 2020-08-06T14:57:10+00:00
- Closed at: 2020-08-31T05:46:24+00:00
