---
title: '[performance] minor CPU overload initially.'
source_url: https://github.com/monero-project/monero-gui/issues/3240
author: ronohara
assignees: []
labels: []
created_at: '2020-11-16T09:15:39+00:00'
updated_at: '2022-11-16T00:07:35+00:00'
type: issue
status: open
closed_at: null
---

# Original Description

![image](https://user-images.githubusercontent.com/4027321/99233846-af7dff00-27eb-11eb-9c02-bb3288d6093d.png)

GUI v0.17.1.4

Actions:

- Start monero GUI
- sign in to wallet
- wait for sync to complete.

Then check 'top' ... in an Intel I7 (2 cores) top shows %190 CPU  (both CPU's at max), then drops back to 100% .. then about 2 minutes later, drops back to a trivial CPU load.

It looks like some CPU loop from initial actions (maybe some watchdog) that eventually is satisfied that startup is complete.



# Discussion History
## selsta | 2022-03-16T19:54:51+00:00
Are you sure this isn't just the sync process?

## mmortal03 | 2022-11-16T00:07:35+00:00
@ronohara , did you find a solution to this?

# Action History
- Created by: ronohara | 2020-11-16T09:15:39+00:00
