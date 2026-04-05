---
title: config.json
source_url: https://github.com/xmrig/xmrig/issues/472
author: liminalsoundscapes
assignees: []
labels:
- enhancement
created_at: '2018-03-23T09:37:17+00:00'
updated_at: '2019-08-02T13:56:04+00:00'
type: issue
status: closed
closed_at: '2019-08-02T13:56:04+00:00'
---

# Original Description
would love a nice solution on how to set a static config filename to the build setup so there is no need to modify the platform.cpp file on every new release. im keeping two miners in the same folder and config.json for both makes a conflict for cpu and gpu mining together

# Discussion History
## xmrig | 2018-03-24T05:26:35+00:00
Why just not use `--config` option?
Thank you.

## liminalsoundscapes | 2018-03-24T21:01:44+00:00
I can, but some settings i would like to keep as few parameters as possible, i think config.json can still be a default, but an alternative default would be nice as well which could be hardcoded in the cmake option part :)

## calvintam236 | 2018-03-30T09:15:44+00:00
A suggestion: run the docker image of xmrig.

# Action History
- Created by: liminalsoundscapes | 2018-03-23T09:37:17+00:00
- Closed at: 2019-08-02T13:56:04+00:00
