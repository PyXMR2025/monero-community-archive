---
title: Windows AMD services update issue possibly?
source_url: https://github.com/xmrig/xmrig/issues/2324
author: ERRA-Augment
assignees: []
labels: []
created_at: '2021-04-28T17:06:30+00:00'
updated_at: '2021-04-29T00:59:20+00:00'
type: issue
status: closed
closed_at: '2021-04-29T00:59:20+00:00'
---

# Original Description
Not sure why this is doing this now, but a couple days ago when mining kevacoin or wownero, there was an AMD services update and my ryzens on both PC's one has a 3900x and one has a 2700x throttle down to half speed, and then after being left long enough they go down to 100kh, the core voltages dont change, ive disabled antivirus and realtime protection, ive tried totally different pools with the same result, ive freshly formatted both computers, i even set lower voltage in the bios instead of ryzen master and still same issues, the voltage does not change when the mining application begins to run at half speed or less, ontop of that the computers start running sluggish until i hit pause and resume on the miner, then the hashrates go back up for 5 mins and everything is fine, ive been mining for a long time and im surprised i cant figure out this issue, not sure if anyone else has reported anything like this yet but id like to know if anyone knows why this is all of a sudden happening, i even tried older versions of xmrig and no changes so im feeling like it might be a windows issue with the update after everything i did


# Discussion History
## SChernykh | 2021-04-28T18:08:36+00:00
Turn off memory compression and RunFullMemoryDiagnostic task: https://xmrig.com/docs/miner/randomx-stability-troubleshooting-guide

## ERRA-Augment | 2021-04-28T22:19:59+00:00
That was it, you rock, much appreciated., been trying to figure that out for a day

# Action History
- Created by: ERRA-Augment | 2021-04-28T17:06:30+00:00
- Closed at: 2021-04-29T00:59:20+00:00
