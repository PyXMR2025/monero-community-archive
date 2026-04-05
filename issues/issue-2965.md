---
title: Quick question about MSR and running xmrig without superuser
source_url: https://github.com/xmrig/xmrig/issues/2965
author: ghost
assignees: []
labels: []
created_at: '2022-03-13T05:06:45+00:00'
updated_at: '2022-07-06T02:55:04+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I use xmrig on my personal computer (Intel i7-6500U), and I'd rather not run it as root because I also need to give it access to networking in order to pool mine.

Apparently the MSR optimization is auto-configured when xmrig is run as root. That does work for me. I just wanted to confirm that xmrig doesn't need su for `rdmsr` access, and that doing `wrmsr -a 0x1a4 0xf` myself will also activate the MSR optimization, because xmrig will still print scary `cannot read MSR 0x000001a4` and `FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW` messages because it can't read the MSR itself.

If so, perhaps the error message specifically for `rdmsr()` failures should be changed to something different like "cannot check MSR mod, your hashrate may be low" and "confirm that the MSR mod is activated by running 'rdmsr $address' : it should return $value".

# Discussion History
## Phoenix-Starlight | 2022-07-06T02:47:14+00:00
If you use wrmsr yourself by hand it should work since xmrig doesn't have perms to even touch MSR then. Also the reason I think for not allowing reading of MSRs unless root is to stop side channel attacks.

## Spudz76 | 2022-07-06T02:55:04+00:00
The assumption is if you are power-user enough to set the MSRs yourself, you will also be power-user enough to know the error message is lying.

# Action History
- Created by: ghost | 2022-03-13T05:06:45+00:00
