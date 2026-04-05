---
title: I need help setting up my XMR mining rig on my android phone. Getting stuck.
source_url: https://github.com/xmrig/xmrig/issues/3315
author: z3dzgam3r
assignees: []
labels: []
created_at: '2023-08-11T08:18:03+00:00'
updated_at: '2025-06-18T22:40:28+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:40:28+00:00'
---

# Original Description
i have downloaded the xmr rig it is in a folder somewhere called build

i got as far as trying to connect my monero wallet and trying to set up the mining pool, (which failed because it said connection cancelled.) I have switched DNS to try to resolve the issue.

i closed the terminal because it was stuck and tried reopening the rig to retry step two and got a CMake warning. (The picture is attached below.)



if any one can help I would greatly apreciate it.

![Screenshot_20230811-023820_Termux](https://github.com/xmrig/xmrig/assets/141998781/0f8cc1f0-e2cc-4e6b-85ea-b87e93dd6809)


# Discussion History
## bellos | 2023-08-11T23:00:36+00:00
cmake .. -DWITH_HWLOC=OFF
after 
make -j10     


# Action History
- Created by: z3dzgam3r | 2023-08-11T08:18:03+00:00
- Closed at: 2025-06-18T22:40:28+00:00
