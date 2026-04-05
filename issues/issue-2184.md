---
title: Environment Variable like "rid-id" =  ${Random} not working
source_url: https://github.com/xmrig/xmrig/issues/2184
author: hirdeshsaxena
assignees: []
labels: []
created_at: '2021-03-16T04:36:38+00:00'
updated_at: '2021-04-12T13:56:38+00:00'
type: issue
status: closed
closed_at: '2021-04-12T13:56:38+00:00'
---

# Original Description
Hello Dev,

I want to change  these two   "pass": "${Random}",    "rig-id": "${Random}",

My cmakelists.txt has option which is already enable
option(WITH_ENV_VARS        "Enable environment variables support in config file" ON)

I want in both file config file as well as in config.default.h

but system considering as a string / word how can i get random

Thankyou

# Discussion History
# Action History
- Created by: hirdeshsaxena | 2021-03-16T04:36:38+00:00
- Closed at: 2021-04-12T13:56:38+00:00
