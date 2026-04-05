---
title: How to stop my xmrig from running on VM (there's no VM on my PC)?
source_url: https://github.com/xmrig/xmrig/issues/3135
author: Jeswin-123
assignees: []
labels: []
created_at: '2022-10-10T16:12:16+00:00'
updated_at: '2022-10-11T17:43:20+00:00'
type: issue
status: closed
closed_at: '2022-10-11T17:43:20+00:00'
---

# Original Description
No description

# Discussion History
## Spudz76 | 2022-10-10T16:44:26+00:00
Windows uses VM mode as a safety sandbox, shut that junk off.

https://github.com/xmrig/xmrig/issues/1891#issuecomment-776180629

## Jeswin-123 | 2022-10-10T16:47:38+00:00
How to shut that off?


## Spudz76 | 2022-10-10T18:23:59+00:00
It says how, in the post I linked to?

## Jeswin-123 | 2022-10-10T18:26:57+00:00
Oh yeah I found it thanks :))
But it still shows the error failed to apply mod msr, is there any way to fix it too??  I thought it might be coz of the VM, but I guess there's more to it

## mkhuber1 | 2022-10-10T18:29:36+00:00
config.json
Under RandomX

        "rdmsr": false,
        "wrmsr": false,

## Spudz76 | 2022-10-11T02:04:21+00:00
that only gets rid of the message by disabling the whole thing

run as Administrator...

## Jeswin-123 | 2022-10-11T07:48:54+00:00
I am running it as admin, even turned it on through properties > compatibility. But to still not working!


## SChernykh | 2022-10-11T09:31:34+00:00
Turn **off** Core Isolation and Memory Integrity in Windows settings: https://www.howtogeek.com/357757/what-are-core-isolation-and-memory-integrity-in-windows-10/
If it doesn't help, turn off any virtualization settings in BIOS.

## Jeswin-123 | 2022-10-11T10:04:29+00:00
Done everything, but the msr error still persists......Btw is it worth mining on my Celeron N4020 processor?


## SChernykh | 2022-10-11T11:23:04+00:00
Did you try to disable Secure Boot and all other virtualization settings in BIOS? But it will probably not work for you because all benchmarks of this CPU have MSR disabled for some reason https://xmrig.com/benchmark?cpu=Intel%28R%29+Celeron%28R%29+N4020+CPU+%40+1.10GHz

## Jeswin-123 | 2022-10-11T12:53:16+00:00
Yeah I did disable all visualisation settings. Ohh is it that's too bad anyways :(

## Spudz76 | 2022-10-11T16:21:24+00:00
Celerons don't have the MSRs so disable it to get rid of the message

## Jeswin-123 | 2022-10-11T17:43:00+00:00
Ohhh yeah I've done that, the issue is fixed now. Thanks everyone for the valuable inputs :)

# Action History
- Created by: Jeswin-123 | 2022-10-10T16:12:16+00:00
- Closed at: 2022-10-11T17:43:20+00:00
