---
title: '[dev] TLS changes break libssl 1.0.x'
source_url: https://github.com/xmrig/xmrig/issues/1601
author: Spudz76
assignees: []
labels:
- bug
created_at: '2020-03-21T20:52:19+00:00'
updated_at: '2020-03-22T01:55:08+00:00'
type: issue
status: closed
closed_at: '2020-03-22T01:55:08+00:00'
---

# Original Description
**Describe the bug**
Compilation fails to locate function `DH_set0_pqg` @ [this line](https://github.com/xmrig/xmrig/commit/5b610e4dfe9ee022c57c94924b89ef5f20284881#diff-dce132ce071d432681108966c4ed9a46R82)

**To Reproduce**
Compile on old system with `libssl 1.0.2g`

**Expected behavior**
Compile and work even with libssl 1.0.x, as before this change

**Additional context**
Workarounds (polyfill) documented here (search for `DH_set0_pqg`):
https://wiki.openssl.org/index.php/OpenSSL_1.1.0_Changes#Compatibility_Layer

Compilation works `WITH_TLS=OFF` but that disables Pool TLS along with API TLS.

# Discussion History
## xmrig | 2020-03-21T22:59:40+00:00
Fixed. Thank you.

## Spudz76 | 2020-03-22T01:50:32+00:00
Testing now on affected ancient Gentoo system

## Spudz76 | 2020-03-22T01:55:03+00:00
Works great, API TLS untested though.

# Action History
- Created by: Spudz76 | 2020-03-21T20:52:19+00:00
- Closed at: 2020-03-22T01:55:08+00:00
