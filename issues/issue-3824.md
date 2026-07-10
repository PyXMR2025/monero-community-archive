---
title: 'CANNOT LINK EXECUTABLE "cmake": cannot locate symbol "_ZN4Json5ValueixENSt6__ndk117basic_string_viewIcNS1_11char_traitsIcEEEE"
  referenced by "/data/data/com.termux/files/usr/bin/cmake"...'
source_url: https://github.com/xmrig/xmrig/issues/3824
author: Khang70
assignees: []
labels: []
created_at: '2026-06-16T19:31:20+00:00'
updated_at: '2026-07-08T00:21:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Problem:
CANNOT LINK EXECUTABLE "cmake": cannot locate symbol "_ZN4Json5ValueixENSt6__ndk117basic_string_viewIcNS1_11char_traitsIcEEEE" referenced by "/data/data/com.termux/files/usr/bin/cmake"...**

**- What should I do?** I'm very bad at using Termux, so I've encountered this error. I've tried asking about GPT, YouTube, and GitHub, but nothing seems to work. Please, can someone explain it to me? If it's possible to fix, how do I do it?
**- Image of the problem above:**

<img width="1080" height="2400" alt="Image" src="https://github.com/user-attachments/assets/3d9a26df-cf57-4658-8efd-c141471067f0" />

_I'm using the latest Termux on F-Droid, Android 11, arm64._

# Discussion History
## Khang70 | 2026-06-16T19:35:17+00:00
I tried "apt update" and "apt upgrade" but it didn't work.

## lem-solutions | 2026-07-07T17:47:41+00:00
looks like a problem with termux or whereever you got your cmake from, I don't think your problem has anything to do with xmrig

## QXIoa | 2026-07-08T00:21:06+00:00
this is not an xmrig issue, it is likely misconfigured cmake

# Action History
- Created by: Khang70 | 2026-06-16T19:31:20+00:00
