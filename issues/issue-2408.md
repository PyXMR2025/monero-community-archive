---
title: Cannot build master on OSX
source_url: https://github.com/monero-project/monero-gui/issues/2408
author: rotavele
assignees: []
labels:
- resolved
created_at: '2019-10-04T10:16:47+00:00'
updated_at: '2019-11-11T23:09:37+00:00'
type: issue
status: closed
closed_at: '2019-11-11T23:09:37+00:00'
---

# Original Description
I am trying to build the master branch from a fresh clone on OSX. 

This happens with both 
`./build.sh`
and
`./build.sh release-static`

The daemon build script appears to be building randomx submodule and the resulting binary is in the external dir as expected but I keep getting this error when the wallet tries to link/include it:

`ld: library not found for -lrandomx`

# Discussion History
## xiphon | 2019-10-04T11:20:09+00:00
Will be fixed via https://github.com/monero-project/monero/pull/5951

## rotavele | 2019-10-04T18:56:23+00:00
Awesome thank you. I will watch that issue and give feedback if I can.

## selsta | 2019-11-11T22:52:41+00:00
+resolved

# Action History
- Created by: rotavele | 2019-10-04T10:16:47+00:00
- Closed at: 2019-11-11T23:09:37+00:00
