---
title: randomly getting "failed to start WinRing0 driver, error 183"
source_url: https://github.com/xmrig/xmrig/issues/2844
author: lilputsis
assignees: []
labels: []
created_at: '2021-12-28T13:47:46+00:00'
updated_at: '2021-12-28T14:04:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've been using xmrig since the start of this year and never once had any issues. But now about 2-3 weeks ago I've been getting:

failed to start WinRing0 driver, error 183
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW

I've been googling for this issue and I can't find out what's causing it. I'm on Windows 10 21H1. Used to get over 9000 H/s, now I'm somewhere over 7000 H/s. I've tried disabling some software etc. tried to use safe mode, I'm still getting this error. Does anybody know what might be causing it? Should I uninstall monitoring software such as HWinfo, RivaTuner etc. though they've been installed on this computer before I started using xmrig and everything was fine then. And I always close monitoring programs when I leave xmrig on.
![Screenshot 2021-12-28 154705](https://user-images.githubusercontent.com/96780539/147572688-7db9a8e7-d58d-42c4-845f-24a7609cb35f.png)


# Discussion History
## SChernykh | 2021-12-28T13:52:29+00:00
Update to the latest version, it was fixed in v6.16.0

## lilputsis | 2021-12-28T14:04:26+00:00
I can't believe I didn't try to update before, this was too easy. Thank you! My hashrate is back at 9200 H/s.


# Action History
- Created by: lilputsis | 2021-12-28T13:47:46+00:00
