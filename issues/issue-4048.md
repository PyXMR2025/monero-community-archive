---
title: Improper wiping of certain structures with memset
source_url: https://github.com/monero-project/monero/issues/4048
author: c---
assignees: []
labels: []
created_at: '2018-06-24T17:27:12+00:00'
updated_at: '2018-06-24T18:07:33+00:00'
type: issue
status: closed
closed_at: '2018-06-24T18:07:33+00:00'
---

# Original Description
There are several places in the code that try to wipe out an object by using memset(&obj, 0, sizeof(obj)). This is fine for simple structures but in some cases it's wiping objects within the structure like std::string, std::vector, etc. This is very bad practice and can lead to memory leaks (eg. internal allocated pointers may be wiped and lost). GCC 8.1 detects these issues and will give an error (ie. monero will not compile successfully when using GCC 8.1).

Looks like two places in the v0.12.2.0 code:
src/cryptonote_basic/account.cpp line line 160
Looks like the wipe isn't needed because when the object is created it does a scrub()

src/daemon/rpc_command_executor.cpp line 976
This one is more complicated. There are buried std::* object(s) that will already be "wiped" on initialization and should not be memset. However, there are a bunch of values that are not set to anything when the object is created.

# Discussion History
## moneromooo-monero | 2018-06-24T17:56:16+00:00
Those are fixed already AFAICT. Did you check current code ?

## c--- | 2018-06-24T18:07:33+00:00
Yep, sorry, it looks fixed in the latest code. I forgot to look.

FIxed in 9a3bd88b9f65f4245b6b20ef0c33b75c39779b80


# Action History
- Created by: c--- | 2018-06-24T17:27:12+00:00
- Closed at: 2018-06-24T18:07:33+00:00
