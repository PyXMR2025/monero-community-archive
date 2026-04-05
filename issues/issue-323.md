---
title: Abort in debug windows
source_url: https://github.com/xmrig/xmrig/issues/323
author: aexhg
assignees: []
labels: []
created_at: '2018-01-05T23:30:19+00:00'
updated_at: '2018-11-05T07:08:32+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:08:32+00:00'
---

# Original Description
Caused by 
const rapidjson::Value &id = doc["id"];
in Client.cpp

I think only the first instruction set will have id. The rest won't. Works in Release

# Discussion History
# Action History
- Created by: aexhg | 2018-01-05T23:30:19+00:00
- Closed at: 2018-11-05T07:08:32+00:00
