---
title: Automatic fallback to softwarecontext renderer
source_url: https://github.com/monero-project/monero-gui/issues/2878
author: selsta
assignees: []
labels: []
created_at: '2020-05-01T18:09:58+00:00'
updated_at: '2025-03-22T10:08:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
This wasn't fixed. Please re-open.

I also have 100% CPU using monero GUI `v0.15.0.4` in a VirtualBox VM (Whonix-Workstation). It's just the first screen (language selection screen). No monero installed ever in that VM before.

`QMLSCENE_DEVICE=softwarecontext ./monero-wallet-gui` helps as a workaround but it's not a solution. Users shouldn't be required to figure that out the hard way. Should be the default or some other fix.

Also my CPU use is now down to 30% which still seems to much for just an idle language selection screen.

_Originally posted by @adrelanos in https://github.com/monero-project/monero-gui/issues/2238#issuecomment-622497250_

# Discussion History
## selsta | 2020-05-01T18:21:09+00:00
The best solution would be automatic fallback to softwarecontext in systems which have trouble with OpenGL. If this is not possible then I guess this will be a wontfix.

> Should be the default

Setting the softwarecontext renderer as default will result in a worse experience for the majority of users. The renderer has worse quality, supports less features AFAIK also uses more CPU. See https://doc.qt.io/QtQuick2DRenderer/qtquick2drenderer-performance.html

## adrelanos | 2020-05-02T09:17:11+00:00
Btw as for Whonix integration (which runs mostly in VMs), I guess would be best if some script [1] checked if hardware rending is enabled. And if not, set `QMLSCENE_DEVICE=softwarecontext` as global environment variable by default.

How to test from command line if hardware acceleration is available?

selsta:
>> Should be the default
> 
> Setting the softwarecontext renderer as default will result in a worse experience for the majority of users. The renderer has worse quality, supports less features AFAIK also uses more CPU. See https://doc.qt.io/QtQuick2DRenderer/qtquick2drenderer-performance.html

I agree. softwarecontext renderer should if anything only be default when needed. Not for everyone that doesn't need it.

----

[1] Has nothing to do with monero. The name of package is [vm-config-dist](https://github.com/Whonix/vm-config-dist). I don't suggest to implement such a script in monero that changes environment variables globally. Just wondering for a good solution for Whonix / VMs.

## adrelanos | 2020-05-02T11:59:08+00:00
[Test command from inside VM to detect if VirtualBox 3D acceleration is enabled or disabled?](https://forums.virtualbox.org/viewtopic.php?f=3&t=97983)

## adrelanos | 2020-05-02T13:42:09+00:00
I guess this needs a separate ticket.
30% CPU in Debian buster based VirtualBox VM
https://github.com/monero-project/monero-gui/issues/2880


## selsta | 2020-05-04T18:01:14+00:00
Forget my comment, glxinfo is what you wrote above already.

Anyway, I think this is VirtualBox related as I never had any issues with VMWare Fusion.

Maybe you can add the info to only use softwarecontext if the GUI has high CPU usage: https://github.com/Whonix/monero-gui#vm-users


## adrelanos | 2020-05-04T18:09:47+00:00
Sure. Writing now:

> Due to this [VM specific Monero GUI upstream bug](https://github.com/monero-project/monero-gui/issues/2878) setting envrionment variable `QMLSCENE_DEVICE=softwarecontext` is required inside some virtual machines (VMs). Known affected are to VirtualBox and KVM based VMs on Debian buster. [Reported unaffected is VMWare Fusion](https://github.com/monero-project/monero-gui/issues/2878#issuecomment-623615401), in that case setting `QMLSCENE_DEVICE=softwarecontext` can be omitted.

Pull requests against VM (or anything) are also welcome.

## mmortal03 | 2022-11-16T00:05:43+00:00
Is this only supposed to be an issue with virtual machines? I'm currently seeing constant high CPU usage on a Windows laptop with AMD graphics switching on monero-wallet-gui.exe v0.18.1.2, even after it has synced. 72%+ constant CPU usage at the password entry screen, and 12%+ constant CPU usage after entering the wallet password. I am using a Trezor and a remote node. I tried adding monero-wallet-gui.exe to the AMD switchable graphics application settings, but doing that doesn't seem to affect the CPU usage, whether I'm configuring it to use the graphics card or the CPU graphics, I get the same high CPU usage. Lowering the affinity of CPUs or the process priority also doesn't seem to make a difference.

## selsta | 2022-11-16T00:08:14+00:00
@mmortal03 does starting "low-graphics-mode.bat" make a difference?

## mmortal03 | 2022-11-16T00:13:36+00:00
> @mmortal03 does starting "low-graphics-mode.bat" make a difference?

Oh, wow, yes, that solves it. I wonder what the cause is, though?

## selsta | 2022-11-16T16:40:42+00:00
It seems so GPU driver related issue. low-graphics-mode.bat uses CPU software rendering, in regular mode OpenGL is used.

## everoddandeven | 2025-03-20T19:22:41+00:00
Hey @adrelanos I saw your post on virtualbox forum:

`The output of glxinfo is exactly the same with and without 3D acceleration`

I have tried it on my pc, and I got 2 different results:

3D Acceleration **disabled**

```
[workstation user ~]% glxinfo | grep "OpenGL renderer"
OpenGL renderer string: llvmpipe (LLVM 15.0.6, 256 bits)

```

3D Acceleration **enabled**
```
[workstation user ~]% glxinfo | grep "OpenGL renderer"
OpenGL renderer string: SVGA3D; build: RELEASE;  LLVM;

```


## adrelanos | 2025-03-21T08:24:13+00:00
Based on that Monero may be able to choose correct renderer?

## everoddandeven | 2025-03-22T10:08:22+00:00
> Based on that Monero may be able to choose correct renderer?

I think so, in case 3D acceleration is enabled, the wallet can set the renderer to OpenGL. This way we avoid going blind as I had wrongly proposed at the beginning.

# Action History
- Created by: selsta | 2020-05-01T18:09:58+00:00
