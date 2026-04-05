---
title: Huge page support fails for "SYSTEM" account privileges
source_url: https://github.com/xmrig/xmrig/issues/609
author: 0xhesch
assignees: []
labels:
- review later
created_at: '2018-05-06T18:05:10+00:00'
updated_at: '2019-08-02T12:57:15+00:00'
type: issue
status: closed
closed_at: '2019-08-02T12:57:15+00:00'
---

# Original Description
If you run xmrig without a user domain eg. previous login or from a service it will correctly add the **SYSTEM** account to  `lock pages in memory` policy for the next reboot, but will always fail to use it. It just keeps readding it.

Why does this happen?

# Discussion History
# Action History
- Created by: 0xhesch | 2018-05-06T18:05:10+00:00
- Closed at: 2019-08-02T12:57:15+00:00
