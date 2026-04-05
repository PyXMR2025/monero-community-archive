---
title: changes in evo (09cddd) break ios build
source_url: https://github.com/xmrig/xmrig/issues/1027
author: resistor4u
assignees: []
labels: []
created_at: '2019-06-04T18:22:40+00:00'
updated_at: '2019-06-04T18:42:47+00:00'
type: issue
status: closed
closed_at: '2019-06-04T18:42:47+00:00'
---

# Original Description
Sorry to report, but the changes in 09cdddc7f6d751ce273e7a8a33edf379a7122eaf break the ios build.

I'm able to generate an executable binary, but it fails the hash self-test each time regardless of the configuration.

Advice?

Edit
------
You must specify `-DWITH_CN_GPU=OFF` in the cmake. I neglected to do this; sorry for false alarm.

# Discussion History
# Action History
- Created by: resistor4u | 2019-06-04T18:22:40+00:00
- Closed at: 2019-06-04T18:42:47+00:00
