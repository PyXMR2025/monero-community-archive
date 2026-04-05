---
title: '"FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW"'
source_url: https://github.com/xmrig/xmrig/issues/3078
author: swaggerooni
assignees: []
labels: []
created_at: '2022-06-27T17:04:48+00:00'
updated_at: '2022-06-27T22:16:15+00:00'
type: issue
status: closed
closed_at: '2022-06-27T22:16:15+00:00'
---

# Original Description
Opened latest version of XMRig in admin mode and this error still pops up

"failed to start WinRing0 driver, error 87"
"FAILED TO APPLY MSR MOD,HASHRATE WILL BE LOW"

Tried Reinstalling but still happens

I'm on windows 11 and huge pages is on btw

![Screenshot 2022-06-27 180409](https://user-images.githubusercontent.com/42319486/175996429-a4f0993f-e7b5-4fbe-a0dc-6698acc8b023.png)



# Discussion History
## SChernykh | 2022-06-27T20:19:41+00:00
XMRig shows red `VM` text, so you're running in a virtual machine which doesn't allow MSR. Windows does this when core isolation/memory integrity is enabled, try to turn it off: https://www.thewindowsclub.com/core-isolation-and-memory-integrity-in-windows-10
You can also try to disable any virtualization options in BIOS.

# Action History
- Created by: swaggerooni | 2022-06-27T17:04:48+00:00
- Closed at: 2022-06-27T22:16:15+00:00
