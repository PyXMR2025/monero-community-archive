---
title: win64 cmake error
source_url: https://github.com/xmrig/xmrig/issues/815
author: passwordhhh
assignees: []
labels: []
created_at: '2018-10-19T02:22:12+00:00'
updated_at: '2018-11-05T15:05:04+00:00'
type: issue
status: closed
closed_at: '2018-11-05T15:05:04+00:00'
---

# Original Description
When I used cmake to generate vs projects, I made a mistake, and added - DWITH_ASM = OFF, the mistake disappeared, and I figured out how to fix it.
![e gb e9sj _gmuf 4sm9](https://user-images.githubusercontent.com/37529845/47194149-d3f71b00-d388-11e8-96a7-8bd743606c4f.png)


# Discussion History
## xmrig | 2018-10-19T02:26:03+00:00
What CMake and MSVC version do you use?
Thank you.

## passwordhhh | 2018-10-19T02:29:20+00:00
vs2015，cmake3.4.3

## xmrig | 2018-10-19T02:49:22+00:00
Update your cmake to recent version.
Thank you.

## passwordhhh | 2018-10-19T02:51:05+00:00
@xmrig ok，Thank you. I solved it.

# Action History
- Created by: passwordhhh | 2018-10-19T02:22:12+00:00
- Closed at: 2018-11-05T15:05:04+00:00
