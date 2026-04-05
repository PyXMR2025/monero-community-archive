---
title: 'MSYS2 64 bit: and 32: cannot run the new self build 2.8-rc'
source_url: https://github.com/xmrig/xmrig/issues/774
author: huffery
assignees: []
labels: []
created_at: '2018-10-04T01:31:08+00:00'
updated_at: '2018-10-04T01:53:15+00:00'
type: issue
status: closed
closed_at: '2018-10-04T01:53:15+00:00'
---

# Original Description
Ubuntu 17.10 x64 build and run 2.8-rc OK.

MSYS2 64 bit: and 32:
can build the exe file. Not able to run:
   1: win 64: the application was unable to start correctly. 0xc00007b.
   2: win 32: can not start becasue libstdc++-6.dll is missing.
 
But I can build and run 2.6.4 in windows without any problem.
  


# Discussion History
## huffery | 2018-10-04T01:52:37+00:00
I resolved the problem by upgrading the xmrig-deps.


# Action History
- Created by: huffery | 2018-10-04T01:31:08+00:00
- Closed at: 2018-10-04T01:53:15+00:00
