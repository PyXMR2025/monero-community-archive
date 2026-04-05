---
title: Gcc 11 warning
source_url: https://github.com/xmrig/xmrig/issues/3130
author: predators46
assignees: []
labels: []
created_at: '2022-09-22T16:33:14+00:00'
updated_at: '2025-06-18T22:52:12+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:52:12+00:00'
---

# Original Description
@Spudz76 

I'm using gcc 11 and get a warning

warning: 'xmrig::kLastError' defined but not used [-Wunused-variable]                                                                                  69 | static const char* kLastError               = "lasterror";                           
      |                    ^~~~~~~~~~

can you add this fix in the next release

https://github.com/xmrig/xmrig/pull/3082/files

# Discussion History
# Action History
- Created by: predators46 | 2022-09-22T16:33:14+00:00
- Closed at: 2025-06-18T22:52:12+00:00
