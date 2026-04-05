---
title: How to add command information to source code
source_url: https://github.com/xmrig/xmrig/issues/3530
author: YY-8885
assignees: []
labels: []
created_at: '2024-08-13T16:55:31+00:00'
updated_at: '2025-06-18T22:06:53+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:06:53+00:00'
---

# Original Description
I want to add the configuration to the source code, and start it after compiling and running, without the need for separate configuration

# Discussion History
## geekwilliams | 2024-08-13T18:42:42+00:00
In src/core/config are a lot of files of interest, in particular: Config_default.h.  

There is a compile time parameter 
-DWITH_EMBEDDED_CONFIG=ON that can be used with this 

# Action History
- Created by: YY-8885 | 2024-08-13T16:55:31+00:00
- Closed at: 2025-06-18T22:06:53+00:00
