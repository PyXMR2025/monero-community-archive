---
title: cannot compile 6.4.0 on centos 7
source_url: https://github.com/xmrig/xmrig/issues/1908
author: solpodein
assignees: []
labels:
- bug
created_at: '2020-10-22T09:24:42+00:00'
updated_at: '2020-11-13T19:19:23+00:00'
type: issue
status: closed
closed_at: '2020-11-13T19:19:23+00:00'
---

# Original Description
src/crypto/randomx/vm_compiled.hpp:41:8: error: converting to ‘const randomx::JitCompilerX86’ from initializer list would use explicit constructor ‘randomx::JitCompilerX86::JitCompilerX86(bool)’


# Discussion History
## ghost | 2020-10-22T09:37:08+00:00
https://gcc.gnu.org/bugzilla/show_bug.cgi?id=58930
That's due to bug in old version of GCC.

## ghost | 2020-10-22T10:37:24+00:00
@solpodein 
https://github.com/cohcho/xmrig/commit/b52feec2e048824b5ba9f03a17087e01f37d0307
Try this branch with 1 commit on top of v6.4.0 tag.

## xmrig | 2020-11-13T19:19:23+00:00
https://github.com/xmrig/xmrig/releases/tag/v6.5.2

# Action History
- Created by: solpodein | 2020-10-22T09:24:42+00:00
- Closed at: 2020-11-13T19:19:23+00:00
