---
title: Some command fails on specific linux distro
source_url: https://github.com/xmrig/xmrig/issues/3688
author: lxl66566
assignees: []
labels: []
created_at: '2025-07-21T17:59:45+00:00'
updated_at: '2025-07-27T22:11:26+00:00'
type: issue
status: closed
closed_at: '2025-07-27T03:56:45+00:00'
---

# Original Description
**Describe the bug**
[The command in Msr_linux](https://github.com/xmrig/xmrig/blob/6e4a5a6d94b33d6ed93890126c699b62f9553f50/src/hw/msr/Msr_linux.cpp#L69) which calls `/sbin/modprobe` will always fail on nixos because there's no `/sbin` on it.

**Possable solution**
directly use `modprobe` instead.


# Discussion History
## Spudz76 | 2025-07-27T00:00:48+00:00
Unsafe since then it would run whatever is in `PATH`.

Correct workaround since this affects a single broken distro, is to mkdir /sbin and then symlink modprobe to wherever the proper binary exists on nixos.

## lxl66566 | 2025-07-27T03:56:45+00:00
ok, so nixpkgs should make a patch for it.

## Spudz76 | 2025-07-27T22:11:26+00:00
Yep that patch over there looks like an even better way to patch it for nixos.

# Action History
- Created by: lxl66566 | 2025-07-21T17:59:45+00:00
- Closed at: 2025-07-27T03:56:45+00:00
