---
title: Large page allocation may fail on Windows booted with non-PAE kernel
source_url: https://github.com/xmrig/xmrig/issues/272
author: yuhong
assignees: []
labels:
- bug
created_at: '2017-12-18T01:31:14+00:00'
updated_at: '2020-08-19T01:26:27+00:00'
type: issue
status: closed
closed_at: '2020-08-19T01:26:27+00:00'
---

# Original Description
On non-PAE, the large page size is 4MB instead of 2MB, and it does seem that allocations fail if it is not a multiple. You can use GetLargePageMinimum to determine. The default is that NX is enabled which means that the PAE kernel is used.
You can test on 32-bit Windows Vista or Windows 7 by using:
bcdedit /set pae ForceDisable
bcdedit /set nx AlwaysOff
then rebooting.

# Discussion History
## sergneo | 2017-12-20T07:20:03+00:00
And on Windows XP 32 bit may how to enable huge pages ? My miner says that is available but disabled

## yuhong | 2017-12-20T07:48:35+00:00
AFAIK it is not supported in XP, you have to have Server 2003 or later to support them.

# Action History
- Created by: yuhong | 2017-12-18T01:31:14+00:00
- Closed at: 2020-08-19T01:26:27+00:00
