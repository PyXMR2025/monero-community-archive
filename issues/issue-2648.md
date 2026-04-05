---
title: Ubuntu/Linux Xmrig not seeing all RAM (1792/2048)
source_url: https://github.com/xmrig/xmrig/issues/2648
author: nutsnox
assignees: []
labels: []
created_at: '2021-10-26T01:04:53+00:00'
updated_at: '2025-06-16T19:16:50+00:00'
type: issue
status: closed
closed_at: '2025-06-16T19:16:50+00:00'
---

# Original Description
Hello,

I've got older RX460 2GB GPU's. I run xmrig and for whatever reason all of their memory cannot be used (1792/2048). I run dmesg|grep VRAM and I see BAR=256M so it looks like 256M is being allocated. Is there a way to free up this last bit of RAM? These cards could use all that they can get! Any environment variable or via grub bootloader somehow? Thanks!

# Discussion History
## Spudz76 | 2021-10-26T02:32:28+00:00
If you haven't set the GPU environment vars, that might be part of it.

```
export GPU_USE_SYNC_OBJECTS=1
export GPU_MAX_HEAP_SIZE=100
export GPU_SINGLE_ALLOC_PERCENT=100
export GPU_FORCE_64BIT_PTR=1
export GPU_MAX_ALLOC_PERCENT=100
```

If you have X running that will eat about that much memory.

Depending what algo you're trying to use the memory might not matter?  It's not like having 4GB for a 2.5GB algo does anything but sit there.

## nutsnox | 2021-10-26T03:17:49+00:00
I appreciate the input.

I have set those environment vars - without them my available ram goes to 1.5GB. It seems like the ram is getting monopolized by BAR.... it doesn't do this in Windows so I'm not sure what it is that ubuntu does (or why) that allocates that RAM and it's not configurable that I can tell. Thank you for your help

## Spudz76 | 2021-10-26T03:44:22+00:00
BAR is not allocated, it's a location pointer that is accessed at address 256M (0x10000000)

[More info about BAR's](https://stackoverflow.com/questions/30190050/what-is-the-base-address-register-bar-in-pcie)

## nutsnox | 2021-10-26T05:49:52+00:00
Interesting - thank you for the link.

So I'm not sure why, but xmrig says that each of my 6 GPU's has exactly 1792MB/2048MB available and the only correlation to this, that I could find, was BAR reading 256MB on dmesg|grep VRAM output. This is Ubuntu Server, so no GUI to hog up RAM. If it were GUI or other application-related I'd expect varying degrees of free memory.... but for some reason it's like clockwork, 1792MB/2048MB which is why I looked to BAR.

Without environment vars set I get 1.5GB ram free instead of 1792MB so it's not that I don't think. I'm stumped.

## Spudz76 | 2021-10-26T07:26:16+00:00
Yeah I checked with this RX480-4GB and it says
```
 * OPENCL GPU   #0 01:00.0 AMD Radeon (TM) RX 480 Graphics (Ellesmere) 1303 MHz cu:36 mem:4031/4031 MB
```
Which is less than 4096, but is 1/1 ratio

What driver are you using, I wouldn't touch anything above amdgpu-pro 20.40 (but the rig above is running 20.30-1109583)

## Spudz76 | 2021-10-26T08:30:59+00:00
Also noticed I'm using amdgpu module args `audio=0 dc=0` which disable loading any audio or display-core.  It may init the display core and reserve some framebuffer space even without anything connected, and nobody needs HDMI audio anyway.

## nutsnox | 2021-10-26T13:49:46+00:00
thanks for recommendation on the driver - this is a fresh install and I'm on 21.30 so I'll drop back to 20.30 and see what that does.. The system is otherwise stable outside of this one issue (and heat - gotta fix the heat). I haven't heard of specifying module args so I'll have to look at how to apply those it sounds like a good idea.

## nutsnox | 2021-10-26T21:20:53+00:00
I could only get 20.50 amdgpu-pro to install. Are you running amdgpu-pro or amdgpu? I set those module parms via modprobe and that didn't seem to have any effect (though I think I'll keep them in there).

Perhaps I should try the amdgpu driver instead of amdgpu-pro?

## Spudz76 | 2021-10-26T22:00:57+00:00
Oh yeah, there is a patch for the 20.30/20.40 that makes it build correctly for newer kernels.  Here is how to make it work for 20.40-1147286... grab this patch txt: [patch_no_pci_platform_rom.diff.txt](https://github.com/xmrig/xmrig/files/7421747/patch_no_pci_platform_rom.diff.txt)

After the install of dkms explodes, do:
```
cd /usr/src/amdgpu-5.6.14.224-1147286/
cat /root/patch_no_pci_platform_rom.diff.txt | patch -p1
dkms remove -m amdgpu -v 5.6.14.224-1147286 --all
dkms install -m amdgpu -v 5.6.14.224-1147286 --all
```

Then it should build fine and install and work.

## Spudz76 | 2021-10-26T22:02:45+00:00
Note if you want 20.30-1109583 then the `5.6.14.224-1147286` above becomes `5.6.5.24-1109583` instead.  You can use tab completion to fill them in whatever version it is...

## Spudz76 | 2021-10-26T22:04:24+00:00
I also use a remote repo not the install-script but I think it works similarly with the install script (unless of course it fails to finish the install when dkms crashes)

## nutsnox | 2021-10-26T22:16:04+00:00
thanks for that - I get the same result. 1783/2028MB after environment vars you listed.

## nutsnox | 2021-10-26T22:22:27+00:00
If it helps, I'm on a Ryzen 3900x B450 motherboard btw.

## nutsnox | 2021-10-26T23:41:08+00:00
Here is a screencap of what I'm seeing:
![mem](https://user-images.githubusercontent.com/49820661/138976266-2e30af89-7158-4e14-8300-c73af56f44f8.png)




## nutsnox | 2021-10-26T23:53:57+00:00
could this be due to a lack of virtual memory allocated? I'm only running a 16GB SSD. But I have 16GB of RAM also.

## Spudz76 | 2021-10-27T01:10:12+00:00
What does `clinfo | grep -Ei '(global.memory.size|max.memory.allocation)'` say?

RX480-4GB says 1:1 also (this is where the numbers in xmrig come from anyway)
```
  Global memory size                              4288315392 (3.994GiB)
  Max memory allocation                           4288315392 (3.994GiB)
```

## Spudz76 | 2021-10-27T01:11:26+00:00
Sometimes things work with all the env vars as above except `GPU_FORCE_64BIT_PTR=0`

## nutsnox | 2021-10-27T01:11:59+00:00
I was LITERALLY just looking at this as you replied:

  Global memory size                              2132770816 (1.986GiB)
  Max memory allocation                           1589308620 (1.48GiB)
  Global memory size                              2127446016 (1.981GiB)
  Max memory allocation                           1589308620 (1.48GiB)

## nutsnox | 2021-10-27T01:37:13+00:00
when I run export GPU_SINGLE_ALLOC_PERCENT=100 && sudo -E clinfo | grep -Ei '(global.memory.size|max.memory.allocation)'

  Global memory size                              2132770816 (1.986GiB)
  Max memory allocation                           1869774848 (1.741GiB)
  Global memory size                              2127446016 (1.981GiB)
  Max memory allocation                           1869774848 (1.741GiB)


## Spudz76 | 2021-10-27T02:20:40+00:00
I am about out of ideas and don't much care to reboot a whole working rig without the `audio=0 dc=0` to find out if that's what it is.

If you put those in grub then you need `amdgpu.` prefixes so it knows which module to route it to.  I gave the raw settings, which would go in either `/etc/modprobe.d/amdgpu.conf`:
```
options amdgpu vm_fragment_size=9 audio=0 dc=0 aspm=0 ppfeaturemask=0xffffffff
```

Or in case it is loaded with initramfs then `/etc/initramfs-tools/modules`:
```
amdgpu vm_fragment_size=9 audio=0 dc=0  aspm=0 ppfeaturemask=0xffffffff
```

But the result in `/etc/default/grub` would be more like:
```
GRUB_CMDLINE_LINUX_DEFAULT="video=vesa:off panic=5 consoleblank=0 hugepagesz=1G hugepages=3 hugepagesz=2M hugepages=122 amdgpu.vm_fragment_size=9 amdgpu.audio=0 amdgpu.dc=0  amdgpu.aspm=0 amdgpu.ppfeaturemask=0xffffffff"
```

But I use the modprobe files.

Maybe some of those other settings do something (is vesa console driver making a "screen" on them? I have it shut completely off for example).

The fragment_size shouldn't be it but there is no downside to specifying it, some miners require it (not sure if xmrig needs it since I've had these args always since day one).

ASPM is power management and putting a link to sleep sounds like a vector for flakiness so I prefer it just leave them all on 24/7 since I'm generally using them 24/7.  Why have a sleep mode when you don't sleep.

ppfeaturemask just enables everything so that you can control clocks with sysfs.  no change if you boot and don't touch anything it will just be in the same bootup defaults

## Spudz76 | 2021-10-27T02:34:39+00:00
Also my `dmesg | grep -E '(amdgpu|drm)'`

```
[   10.492323] [drm] amdgpu kernel modesetting enabled.
[   10.531537] [drm] amdgpu version: 5.6.5.20.30
[   10.569220] [drm] OS DRM version: 5.4.0
[   10.605397] amdgpu: CRAT table not found
[   10.675630] amdgpu: Virtual CRAT table created for CPU
[   10.709098] amdgpu: Topology: Add CPU node
[   10.745916] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 0: 0x38ffe0000000 -> 0x38ffefffffff
[   10.815919] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 2: 0x38fff0000000 -> 0x38fff01fffff
[   10.890728] amdgpu 0000:01:00.0: remove_conflicting_pci_framebuffers: bar 5: 0xfbe00000 -> 0xfbe3ffff
[   10.967060] amdgpu 0000:01:00.0: enabling device (0000 -> 0003)
[   11.006105] [drm] initializing kernel modesetting (POLARIS10 0x1002:0x67DF 0x1462:0x3413 0xC7).
[   11.047301] amdgpu 0000:01:00.0: amdgpu: Trusted Memory Zone (TMZ) feature not supported
[   11.089805] [drm] register mmio base: 0xFBE00000
[   11.131728] [drm] register mmio size: 262144
[   11.172374] [drm] PCIE atomic ops is not supported
[   11.212719] [drm] add ip block number 0 <vi_common>
[   11.253614] [drm] add ip block number 1 <gmc_v8_0>
[   11.294629] [drm] add ip block number 2 <tonga_ih>
[   11.335120] [drm] add ip block number 3 <gfx_v8_0>
[   11.375014] [drm] add ip block number 4 <sdma_v3_0>
[   11.415020] [drm] add ip block number 5 <powerplay>
[   11.454019] [drm] add ip block number 6 <dce_v11_0>
[   11.492101] [drm] add ip block number 7 <uvd_v6_0>
[   11.529462] [drm] add ip block number 8 <vce_v3_0>
[   11.565766] kfd kfd: amdgpu: skipped device 1002:67df, PCI rejects atomics
[   11.837938] amdgpu: ATOM BIOS: 113-V34111-F1
[   11.874264] [drm] UVD is enabled in VM mode
[   11.910163] [drm] UVD ENC is enabled in VM mode
[   11.945622] [drm] VCE enabled in VM mode
[   11.979954] [drm] GPU posting now...
[   12.124505] [drm] vm size is 128 GB, 2 levels, block size is 10-bit, fragment size is 9-bit
[   12.159536] amdgpu 0000:01:00.0: BAR 2: releasing [mem 0x38fff0000000-0x38fff01fffff 64bit pref]
[   12.195039] amdgpu 0000:01:00.0: BAR 0: releasing [mem 0x38ffe0000000-0x38ffefffffff 64bit pref]
[   12.376573] amdgpu 0000:01:00.0: BAR 0: assigned [mem 0x380000000000-0x3800ffffffff 64bit pref]
[   12.416673] amdgpu 0000:01:00.0: BAR 2: assigned [mem 0x380100000000-0x3801001fffff 64bit pref]
[   12.605319] amdgpu 0000:01:00.0: amdgpu: VRAM: 4096M 0x000000F400000000 - 0x000000F4FFFFFFFF (4096M used)
[   12.675012] amdgpu 0000:01:00.0: amdgpu: GART: 256M 0x000000FF00000000 - 0x000000FF0FFFFFFF
[   12.711127] [drm] Detected VRAM RAM=4096M, BAR=4096M
[   12.746448] [drm] RAM width 256bits GDDR5
[   12.919099] [drm] amdgpu: 4096M of VRAM memory ready
[   12.953877] [drm] amdgpu: 32082M of GTT memory ready.
[   12.988778] [drm] GART: num cpu pages 65536, num gpu pages 65536
[   13.025423] [drm] PCIE GART of 256M enabled (table at 0x000000F400000000).
[   13.062423] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
[   13.100071] [drm] Driver supports precise vblank timestamp query.
[   13.138551] [drm] Chained IB support enabled!
[   13.179842] amdgpu: [powerplay] hwmgr_sw_init smu backed is polaris10_smu
[   13.220037] [drm] AMDGPU Display Connectors
[   13.259706] [drm] Connector 0:
[   13.298462] [drm]   DP-1
[   13.336695] [drm]   HPD6
[   13.374517] [drm]   DDC: 0x4868 0x4868 0x4869 0x4869 0x486a 0x486a 0x486b 0x486b
[   13.413929] [drm]   Encoders:
[   13.452888] [drm]     DFP1: INTERNAL_UNIPHY2
[   13.491354] [drm] Connector 1:
[   13.528483] [drm]   DP-2
[   13.565651] [drm]   HPD4
[   13.601531] [drm]   DDC: 0x4870 0x4870 0x4871 0x4871 0x4872 0x4872 0x4873 0x4873
[   13.637872] [drm]   Encoders:
[   13.672653] [drm]     DFP2: INTERNAL_UNIPHY2
[   13.706583] [drm] Connector 2:
[   13.739151] [drm]   HDMI-A-1
[   13.771844] [drm]   HPD1
[   13.803225] [drm]   DDC: 0x486c 0x486c 0x486d 0x486d 0x486e 0x486e 0x486f 0x486f
[   13.836043] [drm]   Encoders:
[   13.868489] [drm]     DFP3: INTERNAL_UNIPHY1
[   13.901093] [drm] Connector 3:
[   13.932575] [drm]   HDMI-A-2
[   13.962613] [drm]   HPD5
[   13.991115] [drm]   DDC: 0x4874 0x4874 0x4875 0x4875 0x4876 0x4876 0x4877 0x4877
[   14.020161] [drm]   Encoders:
[   14.048630] [drm]     DFP4: INTERNAL_UNIPHY1
[   14.076867] [drm] Connector 4:
[   14.104969] [drm]   DVI-D-1
[   14.132311] [drm]   HPD3
[   14.159396] [drm]   DDC: 0x487c 0x487c 0x487d 0x487d 0x487e 0x487e 0x487f 0x487f
[   14.187864] [drm]   Encoders:
[   14.216102] [drm]     DFP5: INTERNAL_UNIPHY
[   14.244423] [drm] Found UVD firmware Version: 1.130 Family ID: 16
[   14.289681] [drm] Found VCE firmware Version: 53.26 Binary ID: 3
[   14.405953] [drm] UVD and UVD ENC initialized successfully.
[   14.533911] [drm] VCE initialized successfully.
[   14.560902] amdgpu 0000:01:00.0: amdgpu: SE 4, SH per SE 1, CU per SH 9, active_cu_number 36
[   14.649359] [drm] Cannot find any crtc or sizes
[   14.714873] [drm] Initialized amdgpu 3.38.0 20150101 for 0000:01:00.0 on minor 0
```

Compare to yours, some things should be different like the CU count and such because this is an RX480-4GB, but many of the things should match up other than 2048GB where mine says 4096GB.

`Cannot find any crtc or sizes` may be key, I think that confirms there have been no screen buffers allocated for connected outputs (because that's why it would need to know "sizes").

This rig has 32GB but 26GB available so it should work within 6GB...  your 16GB should be fine.  This rig also has 3.7GB of swap where 0 is used (perpetually).

## Spudz76 | 2021-10-27T02:36:10+00:00
Oh plus that's the memory usage along with three other cards in the same rig also running.  So you should be perfectly fine with the mem and swap.  Swapfiles were more of a thing on Windows because of how it does virtual address mapping and co-mingles it with swap because they're silly.

## nutsnox | 2021-10-27T02:39:12+00:00
yeah - I used the grub approach with your exact parameters and no change.

I've dealt with something like this before a long time ago but I forgot the solution. I do vaguely remember something about a possible solution being group related. I can't run clinfo unless via sudo but I don't recall what group I had to assign the regular user to.

## Spudz76 | 2021-10-27T02:39:46+00:00
If it was that, probably `video`

I run everything as root because yolo

## nutsnox | 2021-10-27T02:41:45+00:00
for some reason I thought it might be render.... but I can try both

## nutsnox | 2021-10-27T02:55:12+00:00
nope, not it... I'm stumped :(

What OS distro/version etc are you running?

## nutsnox | 2021-10-27T04:46:06+00:00
so I think I was correct in thinking it had something to do with the BAR... I enabled resizable BAR in BIOS and disabled CSM. Reboot, reinstalled 21.30 and this is what comes up now....

  Global memory size                              2147483648 (2GiB)
  Max memory allocation                           2147483648 (2GiB)
  Global memory size                              2147483648 (2GiB)
  Max memory allocation                           1879048192 (1.75GiB)

The only problem is that not all cards share this so I have to figure out how to apply it across all cards if that's even possible.

## Spudz76 | 2021-10-27T09:39:22+00:00
Strange.  Ubuntu 20.04.3 LTS (focal) and with legacy bios.  Also risers so I have all sorts of PCIe BIOS options fiddled and each card is on an x1 link.  I definitely have the ["above 4GB option"](https://superuser.com/questions/1239231/what-is-above-4g-decoding) enabled, maybe it can't stuff the BARs up into 64-bit memory space without that.

## nutsnox | 2021-10-27T13:11:13+00:00
You're on the same OS as I am. I was booting into EFI so maybe legacy would be a better idea...

As to why, your guess is no doubt better than mine - my only question is how do I enable this for all of the GPU's in my box?

also, semi-related, but any time i write values to overclock I get permission denied. I updated grub with those params you posted. Is the overclock bit generally better done via modprobe?

edit: I'm going to try dropping back to legacy with 4g enabled, reinstall and see if that does it. I have a feeling it will...

## Spudz76 | 2021-10-27T15:15:32+00:00
You have to send `manual` (as opposed to the default, `auto`) into `power_dpm_force_performance_level` first, before changes are accepted in most of the others.

You should be able to ensure the args are working from grub by `cat /proc/cmdline` and ensure they made it there.  I only choose to do it through modprobe because the grub cmdline gets a bit ridiculous length otherwise, and I don't like the repeating `amdgpu.` over and over.  Then I do it both in `/etc/modprobe.d/amdgpu.conf` and `/etc/initramfs-tools/modules` just so they are definitely there whichever way the module gets loaded (some of my systems have amdgpu in the initramfs, some don't and will load it after boot).  Various half toasted cards used to lock up with it in initrd so then I'd block it from being included (customized module inclusion list) so it wouldn't crash until I had a second to get in to stop it from loading (or quick edit grub from the boot menu, to add `modprobe.blacklist=amdgpu` and then load it by hand for debugging).  This is also why I have `panic=5` so that it will reboot whenever the kernel panics for anything.  Mostly so 99.9% of things can be fixed or triaged from remote, since most of the rigs I manage are elsewhere.

## DeeDeeRanged | 2021-11-04T11:49:53+00:00
Haven't seen anything how the OpenCL driver was installed. For Polaris cards you only need amdgpu-pro-xx.xx to istall like amdgpu-install --opencl=legay --headless --no-dkms as that works with RX 480-580 cards.
The driver I am using amdgpu-pro-21.20 on ubuntu 20.4.3.

# Action History
- Created by: nutsnox | 2021-10-26T01:04:53+00:00
- Closed at: 2025-06-16T19:16:50+00:00
