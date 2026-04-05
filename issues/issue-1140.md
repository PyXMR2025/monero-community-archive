---
title: macOS / ElCap / Clang8 --> Missing symbols.
source_url: https://github.com/xmrig/xmrig/issues/1140
author: djfinch
assignees: []
labels:
- bug
- review later
created_at: '2019-08-26T10:33:55+00:00'
updated_at: '2019-09-02T12:54:44+00:00'
type: issue
status: closed
closed_at: '2019-09-02T12:54:43+00:00'
---

# Original Description
@xmrig Missing symbols @ 3.x, any idea? extern C? ElCap/Clang 8. Also, AVX2 looks detected but I'm sure that this old CPU is not supported - this is probably argon issue. Thx!

[CMake](https://pastebin.com/SnnNw0cJ) / [Make](https://pastebin.com/2rNUdG97)

# Discussion History
## xmrig | 2019-08-26T11:40:32+00:00
Thank you, but right now I have no idea how fix it, if compiler not support constexpr arrays, whole CnAlgo need be rewritten, I will take look to it later.

AVX2 right it for argon, this check means compiler support AVX2 code, if CPU or OS not support it, AVX2 code will never selected anyway. 

## djfinch | 2019-08-26T11:54:02+00:00
Thank you for your support & reply. Has this behavior been changed between 2.x and 3.x? 'Un-evolved' miners are OK as usual. AFAIK constexpr should work on C++17 with Clang5 and newer (as per implementation status list). Are those symbols in C? Should we avoid compiler mangling?

Thanks for pointing this out. I mean AVX. Thought it's CPU extension check, not compiler check. ;)

## djfinch | 2019-09-02T12:54:43+00:00
... So, the solution is use GCC instead of Clang ... Thanks!

# Action History
- Created by: djfinch | 2019-08-26T10:33:55+00:00
- Closed at: 2019-09-02T12:54:43+00:00
