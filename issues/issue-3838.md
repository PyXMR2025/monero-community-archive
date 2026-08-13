---
title: CUDA version too new?
source_url: https://github.com/xmrig/xmrig/issues/3838
author: grahamreeds
assignees: []
labels: []
created_at: '2026-08-10T11:35:39+00:00'
updated_at: '2026-08-10T11:40:16+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Windows 10, Intel Xeon 2.8ghz 48GB, M2200 4gb

NVidia-smi reports CUDA version to be 13.0

I can run local ollama models (though they are slow and/or crap) so I know CUDA can work.

However even with the settings in config.json and the dll being in the same folder as the executable I still get CUDA disabled message.

Is the CUDA driver too new?  Does it specifically need 12.9?

# Discussion History
## SChernykh | 2026-08-10T11:39:51+00:00
CUDA 13 support was added in https://github.com/xmrig/xmrig-cuda/pull/216 but it's not the released version of the xmrig-cuda plugin yet. You'll have to build it from source (dev branch), or use CUDA 12.

# Action History
- Created by: grahamreeds | 2026-08-10T11:35:39+00:00
