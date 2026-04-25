---
title: Potential Crash Due to Improper Memory Alignment in src/crypto/cn/sse2neon.h
source_url: https://github.com/xmrig/xmrig/issues/3804
author: MathysHerbomez
assignees: []
labels: []
created_at: '2026-04-22T12:24:01+00:00'
updated_at: '2026-04-24T04:56:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
In the file src/crypto/cn/sse2neon.h, several functions that load and store 128-bit data require the memory addresses to be aligned on a 16-byte boundary. The comments explicitly warn that if the memory is not properly aligned, a general-protection exception (crash) may be generated.

**To Reproduce**
Use functions like _mm_load_ps or _mm_store_ps with memory addresses that are not 16-byte aligned.

**Expected behavior**
The software should handle unaligned memory gracefully or ensure that memory is always properly aligned to prevent crashes.

**Required data**
 - XMRig version: v6.26.0
 - Miner log as text or screenshot: No miner log needed
 - Config file or command line (without wallets): Not dependent on the config
 - OS: Not OS specific, but architecture specific: ARM

**Additional context**
Potential impact:
- If memory alignment is not guaranteed, the software may crash due to general-protection exceptions.
- This affects stability and reliability.

Suggested actions:
- Audit codebase for 16-byte alignment of pointers passed to these functions.
- Add runtime checks or static assertions for misalignment.
- Consider safer alternatives or fallback paths for unaligned memory access.

This issue is critical for maintaining robustness and preventing crashes during operation.

Please let me know if you need additional details or assistance in reproducing this issue.


# Discussion History
## SChernykh | 2026-04-22T16:46:34+00:00
AI slop

## MathysHerbomez | 2026-04-23T22:48:47+00:00
??? @SChernykh 


## SChernykh | 2026-04-24T04:49:32+00:00
https://en.wikipedia.org/wiki/AI_slop
https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/

First, did you read the comments in that file for these functions? They literally say `mem_addr must be aligned on a 16-byte boundary` so yes we're well aware. Second, does it crash for you on your ARM device? If yes, then make a proper report - how did you compile XMRig, or did you use a release binary, what is your hardware, what is your software, what's the command line/config file.

AI slop = low effort, AI generated, and in 99.9% useless report that only wastes developers' time. Your AI didn't even understand that this "16-byte alignment warning" is originally meant for x86 CPUs, not ARM. And guess what, XMRig works perfectly fine on both AMD and Intel CPUs while using many of functions that require this alignment.

XMRig's code doesn't even use the functions mentioned in your report (it uses different ones, but they're properly aligned). And if it did use some function incorrectly, we would get loads of crash reports from ARM device owners. I tested XMRig on Raspberry Pi, several of my phones, and other people run it perfectly fine on their Macs.

# Action History
- Created by: MathysHerbomez | 2026-04-22T12:24:01+00:00
