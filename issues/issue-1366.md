---
title: '[Request] Add schedule to enable/disable mode of work'
source_url: https://github.com/xmrig/xmrig/issues/1366
author: shehi
assignees: []
labels:
- question
created_at: '2019-12-02T14:14:59+00:00'
updated_at: '2019-12-22T19:42:17+00:00'
type: issue
status: closed
closed_at: '2019-12-22T19:42:17+00:00'
---

# Original Description
If possible, it'd be great to have some kind of scheduler in config.json, which would enable us to schedule the hours of the day when CPU/OpenCL/CUDA gets enabled or disabled. At work, I'd like to get my machine into Cuda mining when I am afk during evenings/nights, and off of it when I am back in the office during daytime. Thanks.

# Discussion History
## xmrig | 2019-12-02T14:19:25+00:00
It can be done by using external tools via HTTP API, `GET /1/config` and `POST /1/config`, or by replacing config file.

# Action History
- Created by: shehi | 2019-12-02T14:14:59+00:00
- Closed at: 2019-12-22T19:42:17+00:00
