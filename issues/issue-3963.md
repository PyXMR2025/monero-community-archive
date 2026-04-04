---
title: Failed to connect the aemon on Android
source_url: https://github.com/monero-project/monero-gui/issues/3963
author: hmsjy2017
assignees: []
labels: []
created_at: '2022-07-09T06:27:13+00:00'
updated_at: '2022-07-21T14:01:57+00:00'
type: issue
status: closed
closed_at: '2022-07-21T06:14:01+00:00'
---

# Original Description
I successfully built an Android APK of monero-gui, but there are some errors.
![Screenshot_20220709_141103_org qtproject example monero_wallet_gui](https://user-images.githubusercontent.com/42692274/178094137-5b47a5da-28f5-4efe-85f3-085d3643a9d9.jpg)

In addition, could you tell me how to customize the package name and icon?

# Discussion History
## selsta | 2022-07-20T18:10:04+00:00
Not sure if local monerod is supported yet on Android. You can set a custom remote node?

## hmsjy2017 | 2022-07-21T00:23:29+00:00
Even if I chose a simple mode, it still cannot work normally.

https://user-images.githubusercontent.com/42692274/180104190-b44647a2-d4a4-48d3-abfd-7dc20a60f8c2.mp4


## selsta | 2022-07-21T00:24:25+00:00
You have to manually connect to a remote node with advanced mode, not simple mode. Simple mode currently require the daemon.

## hmsjy2017 | 2022-07-21T06:14:01+00:00
It works. Thank you!

## selsta | 2022-07-21T14:01:57+00:00
Regarding package name and icon - I don't know and unfortunately don't have an Android phone so it's not something I will look into soon.

# Action History
- Created by: hmsjy2017 | 2022-07-09T06:27:13+00:00
- Closed at: 2022-07-21T06:14:01+00:00
