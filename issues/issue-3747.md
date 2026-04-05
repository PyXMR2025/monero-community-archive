---
title: End of file :(
source_url: https://github.com/xmrig/xmrig/issues/3747
author: fazbis
assignees: []
labels: []
created_at: '2025-12-26T21:20:24+00:00'
updated_at: '2026-01-21T21:31:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
[2025-12-26 21:03:07.808]  net      pool-at.supportxmr.com:80 read error: "end of file"
[2025-12-26 21:03:07.812]  net      0000 no active pools, stop
[2025-12-26 21:16:33.894]  net      pool-at.supportxmr.com:5555 read error: "end of file"
[2025-12-26 21:16:33.894]  net      0000 no active pools, stop

I tried many ports and doesnt work for me

# Discussion History
## geekwilliams | 2025-12-26T21:23:48+00:00
Please post the full xmrig output, the command you used to start it, and the config.json if you're using the config file.  (Please censor wallet address)

We cannot help without more information from you. 

## fazbis | 2025-12-26T21:26:44+00:00
<img width="907" height="534" alt="Image" src="https://github.com/user-attachments/assets/21847b3e-a323-4cf6-91a7-468f1c74cb03" />

<img width="788" height="28" alt="Image" src="https://github.com/user-attachments/assets/bd714ce8-acae-4381-a1ca-f7fc204e0b40" />

<img width="921" height="44" alt="Image" src="https://github.com/user-attachments/assets/27308ff2-d670-4de8-8953-11018d79851b" />

<img width="1159" height="300" alt="Image" src="https://github.com/user-attachments/assets/f4290d65-c891-4464-8f26-8619c7c550bd" />

## SChernykh | 2025-12-26T21:39:14+00:00
Try another pool then. It's a pool-side error - they disconnect from you.

## fazbis | 2025-12-26T21:49:44+00:00
> Try another pool then. It's a pool-side error - they disconnect from you.

i wait for fix, maybe fix

## MENISH-5119 | 2025-12-27T05:33:53+00:00
And no help for me....

## jekv2 | 2026-01-21T21:31:01+00:00
I have the same for [2026-01-21 15:30:31.012]  net      americas.mining-dutch.nl:3340 read error: "end of file"


I have to use supportxmx.com now.

# Action History
- Created by: fazbis | 2025-12-26T21:20:24+00:00
