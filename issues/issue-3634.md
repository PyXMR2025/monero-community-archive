---
title: Hope the xmrig author requests to replace the BLAKE2 version with the BLAKE3
  version.
source_url: https://github.com/xmrig/xmrig/issues/3634
author: Agwl-team
assignees: []
labels: []
created_at: '2025-02-08T02:28:37+00:00'
updated_at: '2025-06-16T19:35:49+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:35:49+00:00'
---

# Original Description
Hope the xmrig author requests to replace the BLAKE2 version with the BLAKE3 version.

# Discussion History
## SChernykh | 2025-02-08T09:24:28+00:00
What? These are different hash algorithms.

## Agwl-team | 2025-02-08T10:34:58+00:00
In the future, upgrade BLAKE2 to BLAKE3 in RandomX and aim to support the maximum number of new instruction sets.

## Agwl-team | 2025-02-08T10:35:38+00:00
Instruction sets such as FMA3, FMA4, and AVX512.

## SChernykh | 2025-02-08T10:38:11+00:00
RandomX uses Blake2. Blake3 was released in 2020, and RandomX went live in 2019. Also, Blake2 is less than 0.1% of RandomX hash time, so it doesn't matter which hash is used.

## Agwl-team | 2025-02-08T10:42:38+00:00
When XMRig starts, the CPU frequency can reach 4.0GHz, and during operation, it stays at 3.0GHz, while the CPU's base frequency is 2.60GHz. Is optimization possible?

## Agwl-team | 2025-02-08T10:44:41+00:00
Can the RandomX algorithm consider supporting older CPUs?

## SChernykh | 2025-02-08T10:52:18+00:00
XMRig can run RandomX on any 64-bit (x86-64 or ARM64) CPU. This is basically any AMD and Intel CPU released since 2006.

## Agwl-team | 2025-02-11T05:28:37+00:00
When XMRig starts, the CPU frequency can reach 4.0GHz, and during operation, it stays at 3.0GHz, while the CPU's base frequency is 2.60GHz. Is optimization possible?

![Image](https://github.com/user-attachments/assets/f03d63e6-8fb6-4276-9a5c-e408069c61cf)

## Agwl-team | 2025-02-11T05:31:45+00:00
![Image](https://github.com/user-attachments/assets/555bbc3e-edf8-4533-8efd-6f2f67a9de20)

## SChernykh | 2025-02-11T09:06:56+00:00
This is how Intel CPUs work. It's not related to XMRig in any way.

# Action History
- Created by: Agwl-team | 2025-02-08T02:28:37+00:00
- Closed at: 2025-06-16T19:35:49+00:00
