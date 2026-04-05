---
title: XMrig not allocating/using full amount of huge-pages
source_url: https://github.com/xmrig/xmrig/issues/1252
author: kio3i0j9024vkoenio
assignees: []
labels:
- question
created_at: '2019-10-25T21:23:36+00:00'
updated_at: '2019-10-26T11:42:34+00:00'
type: issue
status: closed
closed_at: '2019-10-26T11:42:34+00:00'
---

# Original Description
System is Dell T5500 Workstation: Windows 7 64-bit. 48GB memory (24GB on each Xeon X5670 processor). NUMA mode enabled.

Using latest version v4.4.0-beta (but earlier versions also have this issue)

Running XMrig with admin privilege. Each run shows red/yellow status on huge-pages. These used to be green and 100%. Red/Yellow is not optimal and the result is massive hash rate loss.

What is interesting is that each run of XMrig produces different huge-page usage.

Note in the screen shots the huge-pages "4/12 33%" on one run and "5/12 42%" on another. I have seen 1/12 and 8/12 also.

![Screen Shot 2019-10-25 @ 16-11-42](https://user-images.githubusercontent.com/35711866/67605338-bc910180-f743-11e9-86b7-6f0d2703f95a.JPG)
![Screen Shot 2019-10-25 @ 16-12-18](https://user-images.githubusercontent.com/35711866/67605348-c3b80f80-f743-11e9-8737-b53e8bd61072.JPG)





# Discussion History
## xmrig | 2019-10-26T05:48:56+00:00
Only reboot helps, on Windows huge-pages allocation is not guaranteed if other applications heavy use memory there is no longer free huge-pages available, miner can't do anything with it.
Thank you.

## kio3i0j9024vkoenio | 2019-10-26T11:41:58+00:00
Rebooting fixed the issue. Thanks.

Looks like a Windows Update was the problem and even though it didn't demand a reboot a reboot was still needed.

![Screen Shot 2019-10-26 @ 06-37-21](https://user-images.githubusercontent.com/35711866/67618969-af175e00-f7bb-11e9-9968-f3ef528214c9.JPG)



# Action History
- Created by: kio3i0j9024vkoenio | 2019-10-25T21:23:36+00:00
- Closed at: 2019-10-26T11:42:34+00:00
