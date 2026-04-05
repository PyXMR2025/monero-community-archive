---
title: Get build warning under Bookworm but not Bullseye with Rapberry Pi
source_url: https://github.com/xmrig/xmrig/issues/3557
author: raymate
assignees: []
labels:
- question
- arm
created_at: '2024-09-30T21:34:42+00:00'
updated_at: '2025-06-16T19:36:57+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:36:57+00:00'
---

# Original Description
Been setting up some Pi4 4GB and PI5 4GB with xmrig. All are fresh installs of the latest PiOS as of today.

With the Pi4 and under a fresh "Bullseye" install, xmrig builds with the make command fine. Completes with no warnings.

If I build and make xmrig under fresh "Bookworm" I start to get lots of warning at around 81% until 83%, it completes and it does seem to run OK, just wondering why the warning and are they anything to worry about.


[xmrig-warnings.txt](https://github.com/user-attachments/files/17196648/xmrig-warnings.txt)



# Discussion History
## SChernykh | 2024-09-30T23:26:03+00:00
No, it's all false positives. It should be running just fine.

# Action History
- Created by: raymate | 2024-09-30T21:34:42+00:00
- Closed at: 2025-06-16T19:36:57+00:00
