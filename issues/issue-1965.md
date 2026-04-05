---
title: Hashrate Loss
source_url: https://github.com/xmrig/xmrig/issues/1965
author: septuig
assignees: []
labels: []
created_at: '2020-12-06T12:36:11+00:00'
updated_at: '2021-04-12T14:33:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:33:26+00:00'
---

# Original Description
While xmrig is started, the Hashrate is about 8.5k, but after about 0.5hr, it drops to 4k. and then restarts again to 8.5k, after 0.5hr it drops again to 4k. the issue occurs on multiple PCs. 

CPU miners 2xE2680v2, 16G memory. 
Pool: SupportXMR:3333/5555. 

Thank you.

# Discussion History
## xmrig | 2020-12-06T12:57:55+00:00
Please check it first https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide
Thank you.

## SChernykh | 2020-12-06T15:29:57+00:00
If on Windows, disable all tasks in Task Scheduler -> Microsoft -> Windows -> MemoryDiagnostic section. You can open task scheduler by pressing Win+R, typing `taskschd.msc` and pressing Enter.

# Action History
- Created by: septuig | 2020-12-06T12:36:11+00:00
- Closed at: 2021-04-12T14:33:26+00:00
