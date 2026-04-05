---
title: XMRig 6.19.1 for Raspberry Pi / Compilation advice for mining RandomX ?
source_url: https://github.com/xmrig/xmrig/issues/3234
author: FSOL-XDAG
assignees: []
labels: []
created_at: '2023-03-27T12:41:16+00:00'
updated_at: '2023-03-27T13:53:35+00:00'
type: issue
status: closed
closed_at: '2023-03-27T13:53:35+00:00'
---

# Original Description
Hi ! 

I've follow [theses instructions](https://forums.raspberrypi.com/viewtopic.php?t=305983) to compile XMRig 6.19.1 on an old Raspberry Pi 2b (1Gb RAM). Despite, I get some "issue" : 

```
[2023-03-27 14:32:59.518]  randomx  not enough memory for RandomX dataset
[2023-03-27 14:32:59.518]  randomx  failed to allocate RandomX dataset, switching to slow mode (1 ms)
```

Do you have any compilation recommendations to get a light version of XMRig able to mine with RandomX?

# Discussion History
## SChernykh | 2023-03-27T13:00:01+00:00
`--randomx-mode=light` in XMRig command line, or `"mode":"light"` in config.json ("randomx" section).

## FSOL-XDAG | 2023-03-27T13:53:30+00:00
Thanks a lot ! 🤗

# Action History
- Created by: FSOL-XDAG | 2023-03-27T12:41:16+00:00
- Closed at: 2023-03-27T13:53:35+00:00
