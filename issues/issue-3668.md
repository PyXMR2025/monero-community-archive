---
title: Windows ARM64 support
source_url: https://github.com/xmrig/xmrig/issues/3668
author: xmrig
assignees: []
labels:
- enhancement
- arm
created_at: '2025-06-16T13:40:02+00:00'
updated_at: '2025-06-26T17:17:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Release 6.23.0 brings support for Windows ARM64, including official binaries for this OS. ARM64 support isn't new; it has been available for other operating systems for a while.

Only MSYS2 is currently supported; there are no plans to add support for Visual Studio for ARM64, as it requires a huge effort.

Additionally, significant changes have been made to the official binary downloads:
MSYS2 builds now use [`ucrt`](https://www.msys2.org/docs/environments/) instead of the legacy `msvcrt`. If you build from the source, please download the new dependencies and follow the [updated manual](https://xmrig.com/docs/miner/build/windows) for a complete rebuild.
MSVC builds now use Visual Studio 2022; builds with earlier versions continue to work, but they are no longer supported.

Filename changes:
`xmrig-6.xx.x-gcc-win64.zip` -> `xmrig-6.xx.x-windows-gcc-x64.zip`
`xmrig-6.xx.x-msvc-win64.zip` -> `xmrig-6.xx.x-windows-x64.zip`
New file: `xmrig-6.xx.x-windows-arm64.zip` 

# Discussion History
## HumbleDeer | 2025-06-22T17:01:42+00:00
Would it be possible for us / the userbase to provide crowdsourced edits to the documentation? Are the docs available in a repository for sourcing and suggesting? 

## xmrig | 2025-06-22T17:38:49+00:00
@HumbleDeer Still no #1733
It would be helpful if you had an idea of how to make it. Anything that can generate static pages and not limited to plain markdown will be nice.
Thank you.

## PPPDUD | 2025-06-26T17:16:57+00:00
The first step to getting more powerful ARM computers is finding a use-case for more powerful ARM computers.

@xmrig, thanks so much for finding that use-case and making software for it!

# Action History
- Created by: xmrig | 2025-06-16T13:40:02+00:00
