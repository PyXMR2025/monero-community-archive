---
title: 'failed to load wallet: std::bad_alloc'
source_url: https://github.com/monero-project/monero/issues/4855
author: REal0day
assignees: []
labels: []
created_at: '2018-11-15T18:06:58+00:00'
updated_at: '2019-05-02T00:38:02+00:00'
type: issue
status: closed
closed_at: '2018-11-20T09:25:11+00:00'
---

# Original Description
monero-wallet-cli(18265,0x7fffae48f380) malloc: *** mach_vm_map(size=6604946474546995200) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
monero-wallet-cli(18265,0x7fffae48f380) malloc: *** mach_vm_map(size=2581599401600528384) failed (error code=3)
*** error: can't allocate region
*** set a breakpoint in malloc_error_break to debug
Error: failed to load wallet: std::bad_alloc

# Discussion History
## moneromooo-monero | 2018-11-15T21:10:17+00:00
Probably corrupt, or loading on a different arch, or built with incompatible boost.

## dEBRUYNE-1 | 2018-11-16T15:10:05+00:00
Please see:

https://monero.stackexchange.com/questions/6611/cant-load-wallet-in-cli-v0-13-0-2-or-gui-v0-13-0-3-error-stdbad-alloc-err

## dEBRUYNE-1 | 2018-11-18T11:06:52+00:00
Ping @REal0day - Did you manage to resolve your issue? 

## dEBRUYNE-1 | 2018-11-20T09:21:50+00:00
+resolved

## REal0day | 2019-05-02T00:38:02+00:00
Yes. Thank yoU!

# Action History
- Created by: REal0day | 2018-11-15T18:06:58+00:00
- Closed at: 2018-11-20T09:25:11+00:00
