---
title: Strip executable files before putting them in releases
source_url: https://github.com/monero-project/monero/issues/8558
author: duggavo
assignees: []
labels: []
created_at: '2022-09-08T15:21:21+00:00'
updated_at: '2022-09-08T15:32:21+00:00'
type: issue
status: closed
closed_at: '2022-09-08T15:32:21+00:00'
---

# Original Description
Using `strip ./monerod` reduces its size from 23.1 MB to 18.2 MB on the Linux x86-64 release. Is there any reason why the distributed binaries haven't been already stripped? 

# Discussion History
## hyc | 2022-09-08T15:32:21+00:00
Stripping would make backtraces useless.

# Action History
- Created by: duggavo | 2022-09-08T15:21:21+00:00
- Closed at: 2022-09-08T15:32:21+00:00
