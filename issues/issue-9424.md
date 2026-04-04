---
title: Can't `liblmdb` be linked statically?
source_url: https://github.com/monero-project/monero/issues/9424
author: aperechnev
assignees: []
labels:
- more info needed
- build system
created_at: '2024-08-07T00:30:34+00:00'
updated_at: '2024-08-07T10:37:31+00:00'
type: issue
status: closed
closed_at: '2024-08-07T10:37:31+00:00'
---

# Original Description
I've taken a look at the FreeBSD [port](https://www.freshports.org/net-p2p/monero-cli/) of `monero-cli` and recognized that it replaces `/usr/local/lib/liblmdb.so` with it's own library during the process of installation. Then I went a bit deeper and found the next comment: https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/external/db_drivers/CMakeLists.txt#L29

The full text of that comment is:
```
# We aren't even going to check the system for an installed LMDB driver, as it is too
# critical a consensus component to rely on dynamically linked libraries
```

The problem is obvious, `monero-cli` just replaces the existing library silently.

If this library is too critical, why not to link it statically? If it isn't possible for some reason, why not to place it somewhere else?

Even more, `monero-cli` never knows if this library will be replaced in the future. So if `liblmdb.so` is too critical, maybe it's still better to link it statically?

If the problem is just the lack of free time, I can do it myself and send you a pull request.

# Discussion History
## selsta | 2024-08-07T00:41:28+00:00
Is this in regards to the FreeBSD port, or monero's own CMake file?

We don't have an install target and we do already statically link lmdb, but maybe I'm misunderstanding something.

If the issue is purely in regards to the FreeBSD port, it should be reported to the maintainer.

## aperechnev | 2024-08-07T01:10:27+00:00
Hi @selsta and many thanks for the quick reply. I didn't know you're already linking it statically.

I'm working on FreeBSD port of `monero-gui` and it works just perfectly. The only problem is the process of installation. As I mentioned before, it attempts to replace `/usr/local/lib/liblmdb.so`.

I still don't have a firm idea what's the reason and I would really appreciate any help. For now I see the next line: https://github.com/monero-project/monero/blob/caa62bc9ea1c5f2ffe3ffa440ad230e1de509bfd/external/db_drivers/liblmdb/Makefile#L53 which seems to be the reason. But I'm not sure.

Or, since you already link it statically, maybe I'm missing some CMake arguments and it still attempts to link it dynamically. At least for `monero-gui`.

Anyway thank you for the information. Since I know it must be linked statically, I'm able to do more research to solve the problem by myself.

# Action History
- Created by: aperechnev | 2024-08-07T00:30:34+00:00
- Closed at: 2024-08-07T10:37:31+00:00
