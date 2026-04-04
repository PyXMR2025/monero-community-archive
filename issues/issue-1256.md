---
title: GUI glitch in progress bars
source_url: https://github.com/monero-project/monero-gui/issues/1256
author: rex4539
assignees: []
labels:
- enhancement
created_at: '2018-04-04T10:15:34+00:00'
updated_at: '2018-04-08T22:42:57+00:00'
type: issue
status: closed
closed_at: '2018-04-08T22:42:57+00:00'
---

# Original Description
GUI version: v0.12.0.0
macOS 10.13.4 (17E199)

Reproducibility: always

Steps:
Check the progress bars on the lower left.

What happened:
The color inside the bars is not fully drawn until the very right, implying there is still progress, although the wallet and daemon are both 100% synced.

![screen shot 2018-04-04 at 13 10 00](https://user-images.githubusercontent.com/227442/38302067-1fc8e574-380a-11e8-87ab-9a614fba4227.png)

Expected result:
No glitch.

# Discussion History
## tficharmers | 2018-04-04T11:44:05+00:00
Perhaps make the bar go green when 100% filled too?

## sanderfoobar | 2018-04-04T12:08:17+00:00
+enhancement

# Action History
- Created by: rex4539 | 2018-04-04T10:15:34+00:00
- Closed at: 2018-04-08T22:42:57+00:00
