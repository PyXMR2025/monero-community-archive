---
title: Invalid include line in patch
source_url: https://github.com/MrCyjaneK/monero_c/issues/184
author: Xcash-Labs
assignees: []
labels: []
created_at: '2026-03-19T18:11:44+00:00'
updated_at: '2026-03-20T10:06:27+00:00'
type: issue
status: closed
closed_at: '2026-03-20T10:06:27+00:00'
---

# Original Description
In patches/monero in 0019-fix-mingw-build-issues.patch this is a stray line that should probably be removed -

+#include <>

# Discussion History
## MrCyjaneK | 2026-03-20T10:06:27+00:00
It's not there https://github.com/MrCyjaneK/monero_c/blob/c157cb82973b05d1226b39b4d8de0bec4aa10000/patches/monero/0019-fix-mingw-build-issues.patch

# Action History
- Created by: Xcash-Labs | 2026-03-19T18:11:44+00:00
- Closed at: 2026-03-20T10:06:27+00:00
