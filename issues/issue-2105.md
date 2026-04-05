---
title: To Access MSR Registers Admin Rights Required From Where?
source_url: https://github.com/xmrig/xmrig/issues/2105
author: imshaniqbal
assignees: []
labels: []
created_at: '2021-02-14T17:37:56+00:00'
updated_at: '2023-12-18T04:40:26+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:13:50+00:00'
---

# Original Description
I'm using Hash Miner and I'm new to this.. I just simply want to increase the Hashrate so

I'm using Windows 10 64BIT Latest Version, 

CPU: Core i5 10400
Ram: 16GB 2666
MotherBoard: MSI B460 Mag Wifi
**GPU: not using I will add later just mining on cpu...** 

Now if anyone can tell me how to add MSR registers admin rights?

or should I start Quick Miner from Hash

# Discussion History
## ghost | 2021-02-14T19:04:22+00:00
Run it as administrator, reboot (this will enable HUGE PAGES) and then run every time as administrator: this will set MSR automatically.

## mcg0 | 2021-11-05T18:20:00+00:00
I've tried to run as administrator and even activated the administrator account to install and run on Win10 Home, but still getting: 
failed to start WinRing0 driver, error 183
FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
Is there something else I'm missing?

## SChernykh | 2021-11-05T18:31:46+00:00
Error 183 means you run some other software that uses WinRing0 driver - something like hardware monitor or RGB control software. Try to close it. If it doesn't help, uninstall it.

## CarveTechElect | 2023-12-18T04:40:25+00:00
...well for me, I closed the xmrig running process, then simply right click on the icon I placed on the desktop, then clicked on 'run as administrator'. xmrig process restarted and msr was granted successfully

# Action History
- Created by: imshaniqbal | 2021-02-14T17:37:56+00:00
- Closed at: 2021-04-12T14:13:50+00:00
