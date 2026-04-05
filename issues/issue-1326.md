---
title: rx dataset uses cpu thread count instead of config thread count
source_url: https://github.com/xmrig/xmrig/issues/1326
author: YetAnotherRussian
assignees: []
labels:
- question
created_at: '2019-11-28T14:20:56+00:00'
updated_at: '2019-12-22T19:39:36+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:39:36+00:00'
---

# Original Description
Cpu thread count: 24
Config file params:
"rx": [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

Code:
int m_threads   = -1;

return m_threads < 1 ? static_cast<uint32_t>(Cpu::info()->threads()) : static_cast<uint32_t>(m_threads);

Miner output (cut-off):
[2019-11-28 17:18:17.268]  rx   init dataset algo rx/0 (24 threads) 
[2019-11-28 17:18:19.674]  cpu  use profile  rx  (12 threads) scratchpad 2048 KB
[2019-11-28 17:18:19.676]  cpu  READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (1 ms)

This makes a slow CPU or VM dead for some time. Maybe a better solution is to use thread count from config or make a separate config param.

# Discussion History
## SChernykh | 2019-11-28T14:58:37+00:00
Dataset initialization doesn't need 2 MB memory, so it can be parallelized across all available cores. CPU/VM shouldn't die or freeze when all cores are used, so it's some misconfiguration on your side.

## xmrig | 2019-11-29T02:43:10+00:00
https://github.com/xmrig/xmrig/blob/master/src/config.json#L18 you can change `"init": -1,` (auto = all threads) to another thread count.
Thank you.

# Action History
- Created by: YetAnotherRussian | 2019-11-28T14:20:56+00:00
- Closed at: 2019-12-22T19:39:36+00:00
