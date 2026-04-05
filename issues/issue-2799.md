---
title: '[6.16.2, Ghostrider] 0.1% of rejected shares'
source_url: https://github.com/xmrig/xmrig/issues/2799
author: electroape
assignees: []
labels: []
created_at: '2021-12-07T11:26:21+00:00'
updated_at: '2021-12-07T15:35:42+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
XMRig 6.16.2 GCC, Raptoreum / Ghostrider, Flockpool.com

About 100 different machines (ranging from low-end Pentiums and i3s 6-7 gen to high-end i7s, i9s and Ryzens and a few Xeon and EPYC servers), mostly on Windows. Consistent 0.1% of 'high-hash' rejected shares (120 out of 95k) regardless of hardware or software config. There were no rejected shares when i was using cpuminer-gr. Minuscule amount so it's not really an issue, just reporting in.

# Discussion History
## SChernykh | 2021-12-07T12:45:40+00:00
Can you check in logs which rotations (combinations of Cryptonight algorithms) cause rejected shares the most?

## Lonnegan | 2021-12-07T13:49:26+00:00
6.12.2 has no Ghostrider support, yet. You mean 6.1**6**.2?

We've had this discussion about rejected shares already here:
https://github.com/xmrig/xmrig/issues/2730#issuecomment-980719349

## electroape | 2021-12-07T14:49:00+00:00
> 6.12.2 has no Ghostrider support, yet. You mean 6.1**6**.2?

Correct.

> Can you check in logs which rotations (combinations of Cryptonight algorithms) cause rejected shares the most?

No obvious offenders.

```
[2021-12-06 18:45:38.562]  cpu      GhostRider algo 1: cn/fast (2 MB)
[2021-12-06 18:45:38.562]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2021-12-06 18:45:38.562]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)

[2021-12-06 23:56:12.081]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2021-12-06 23:56:12.081]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2021-12-06 23:56:12.081]  cpu      GhostRider algo 3: cn/lite (1 MB)

[2021-12-07 07:50:03.768]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 07:50:03.768]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-07 07:50:03.768]  cpu      GhostRider algo 3: cn/dark (512 KB)

[2021-12-07 10:31:28.821]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 10:31:28.821]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-07 10:31:28.837]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)

[2021-12-07 10:31:28.821]  cpu      GhostRider algo 1: cn/lite (1 MB)           -
[2021-12-07 10:31:28.821]  cpu      GhostRider algo 2: cn/fast (2 MB)           x2
[2021-12-07 10:31:28.837]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)    -

[2021-12-07 10:53:14.545]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2021-12-07 10:53:14.545]  cpu      GhostRider algo 2: cn/dark (512 KB)
[2021-12-07 10:53:14.545]  cpu      GhostRider algo 3: cn/fast (2 MB)

[2021-12-07 14:53:13.607]  cpu      GhostRider algo 1: cn/dark (512 KB)
[2021-12-07 14:53:13.607]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-07 14:53:13.607]  cpu      GhostRider algo 3: cn/dark-lite (256 KB)

[2021-12-06 19:01:32.143]  cpu      GhostRider algo 1: cn/dark-lite (256 KB)
[2021-12-06 19:01:32.143]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-06 19:01:32.143]  cpu      GhostRider algo 3: cn/turtle (256 KB)

[2021-12-06 19:15:01.722]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-06 19:15:01.722]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2021-12-06 19:15:01.722]  cpu      GhostRider algo 3: cn/fast (2 MB)

[2021-12-06 22:46:14.522]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2021-12-06 22:46:14.538]  cpu      GhostRider algo 2: cn/fast (2 MB)
[2021-12-06 22:46:14.538]  cpu      GhostRider algo 3: cn/dark (512 KB)

[2021-12-07 01:02:54.274]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 01:02:54.274]  cpu      GhostRider algo 2: cn/dark-lite (256 KB)
[2021-12-07 01:02:54.274]  cpu      GhostRider algo 3: cn/fast (2 MB)

[2021-12-07 03:01:46.664]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 03:01:46.664]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-12-07 03:01:46.664]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)

[2021-12-07 10:07:10.248]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2021-12-07 10:07:10.248]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2021-12-07 10:07:10.248]  cpu      GhostRider algo 3: cn/turtle-lite (128 KB)

[2021-12-07 12:02:07.372]  cpu      GhostRider algo 1: cn/lite (1 MB)
[2021-12-07 12:02:07.372]  cpu      GhostRider algo 2: cn/turtle (256 KB)
[2021-12-07 12:02:07.372]  cpu      GhostRider algo 3: cn/fast (2 MB)

[2021-12-07 14:32:21.469]  cpu      GhostRider algo 1: cn/turtle (256 KB)
[2021-12-07 14:32:21.734]  cpu      GhostRider algo 2: cn/lite (1 MB)
[2021-12-07 14:32:21.734]  cpu      GhostRider algo 3: cn/fast (2 MB)
```

# Action History
- Created by: electroape | 2021-12-07T11:26:21+00:00
