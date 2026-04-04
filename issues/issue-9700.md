---
title: tesnet typo
source_url: https://github.com/monero-project/monero/issues/9700
author: tankf33der
assignees: []
labels: []
created_at: '2025-01-14T08:50:28+00:00'
updated_at: '2025-02-20T20:59:20+00:00'
type: issue
status: closed
closed_at: '2025-01-25T04:47:23+00:00'
---

# Original Description
FYI
```
cd monero/src
find . -type f | xargs grep "tesnet"
./daemon/main.cpp:      std::cerr << "Can't specify more than one of --tesnet and --stagenet and --regtest" << ENDL;
```

# Discussion History
# Action History
- Created by: tankf33der | 2025-01-14T08:50:28+00:00
- Closed at: 2025-01-25T04:47:23+00:00
