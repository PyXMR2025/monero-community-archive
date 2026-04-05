---
title: can't manage to apply MSR mode because winring already exist on another path
  and a different service name
source_url: https://github.com/xmrig/xmrig/issues/3370
author: Psyprism
assignees: []
labels: []
created_at: '2023-12-02T15:43:33+00:00'
updated_at: '2025-06-18T22:32:05+00:00'
type: issue
status: closed
closed_at: '2025-06-18T22:32:05+00:00'
---

# Original Description
Heya! i was trying to run XMRig with MSR tweaks but it tells me that winring0_1_2_0 file does already exist but with a different service name (check pic).
I indeed have installed cooler master (master plus) in order to manage my RGB and it uses the same file called winring0x64.sys. is there a way to manually insert the correct path for the correct file? or is there another way to let XMRig run the MSR tweaks? 
Thanks in advance!

![immagine](https://github.com/xmrig/xmrig/assets/122061030/01fad628-74b6-4bc1-8c98-693aa45585c2)


# Discussion History
## MarcusNewman | 2023-12-02T16:23:13+00:00
Can you start XMRig before starting cooler master?

## Psyprism | 2023-12-02T16:34:02+00:00
> Can you start XMRig before starting cooler master?

unfortunately even if i don't start coolermaster at all the error displays the same :(

## MarcusNewman | 2023-12-02T18:07:14+00:00
> > Can you start XMRig before starting cooler master?
> 
> unfortunately even if i don't start coolermaster at all the error displays the same :(

Strange. I would try uninstalling cooler master completely. But I’ve never used it and don’t know the ramifications of doing that. Hopefully someone more knowledgeable can chime in. 

## SChernykh | 2023-12-02T19:03:07+00:00
Your problem is not the Cooler Master software, but the VM (see red "VM" in the first few lines in the window). Do the usual drill - turn off virtualization in BIOS, turn off core isolation and memory integrity in Windows.

## Psyprism | 2023-12-03T23:23:37+00:00
> Your problem is not the Cooler Master software, but the VM (see red "VM" in the first few lines in the window). Do the usual drill - turn off virtualization in BIOS, turn off core isolation and memory integrity in Windows.

THANKS A LOT! this worked!


# Action History
- Created by: Psyprism | 2023-12-02T15:43:33+00:00
- Closed at: 2025-06-18T22:32:05+00:00
