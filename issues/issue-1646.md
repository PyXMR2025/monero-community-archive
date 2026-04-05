---
title: Astrobwt algorithm is not working correctly
source_url: https://github.com/xmrig/xmrig/issues/1646
author: paolosezart
assignees: []
labels:
- bug
created_at: '2020-04-13T18:53:04+00:00'
updated_at: '2021-09-26T10:24:09+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:58:40+00:00'
---

# Original Description
The astrobwt algorithm does work not correctly when config.json is auto-configured. Tested on the Win7 intel G2030 2 cores and Win10 intel core i7 8 cores, with the parameter "max-threads-hint": 50, in both cases the processor runs at 100% power, that is, all cores are involved. When launched from the command line with the parameter --cpu-max-threads-hint = 50 or with the parameter --threads = 1 / - threads = 4, the processor works as it should, at half the power.

# Discussion History
## backamblock | 2021-09-26T09:56:52+00:00
for me it works with none of these on windows 10 64 bit

i have 4 threads but astrobwt does NOT honour my max thread hint 50, no matter where I set it. all other things work with 2 threads as told, but not astrobwt. 

please tell me what to change to fix. thank you!

## SChernykh | 2021-09-26T10:24:09+00:00
https://github.com/xmrig/xmrig/pull/2606 should fix it

# Action History
- Created by: paolosezart | 2020-04-13T18:53:04+00:00
- Closed at: 2021-04-12T14:58:40+00:00
