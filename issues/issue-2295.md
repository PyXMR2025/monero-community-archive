---
title: Manually applying MSR not working
source_url: https://github.com/xmrig/xmrig/issues/2295
author: Mushoz
assignees: []
labels:
- question
created_at: '2021-04-21T11:18:35+00:00'
updated_at: '2022-04-03T14:40:43+00:00'
type: issue
status: closed
closed_at: '2022-04-03T14:40:43+00:00'
---

# Original Description
Running the miner via sudo gives me the correct hashrate (13.7k h/s) on my 5900x. However, I am not a big fan of running processes under root if they don´t have to. So I tried to apply the MSR boost manually by running the following script under root: https://github.com/xmrig/xmrig/blob/dev/scripts/randomx_boost.sh

However, after doing that, my hashrate is still in the 9.7k h/s range instead of the expected 13-14 range. Clearly, applying the boost manually  is not working correctly. Is this a bug, or am I doing something wrong? I´d love to run the miner process itself under an ordinary user, and run the script (which is much easier to audit!) under root once.

# Discussion History
## DeeDeeRanged | 2021-04-25T10:30:11+00:00
msr only gets applied when running xmrig as root/sudo plus you have to add the following to your /etc/default/grub GRUB_CMDLINE_LINUX="msr.allow_writes=on" take it you using Ubuntu/Debian?

## Spudz76 | 2021-04-25T12:59:10+00:00
The boost script should (but doesn't) have `allow_writes=on` with its `modprobe msr` line.  But `wrmsr` should complain if that were the problem.  Having the option in the kernel command line forces it regardless when or how the module loads (even if built-in).  But, if the miner as root hits the MSRs fine then the boost script should work (modprobe is no-op when module already there).

Are the hugepages also still working non-root?  You will also have to set those manually pre-launch.  Also if you use the cpu-priority setting, likely non-root can't do that either (use renice by pid after threads are launched). Cache-QoS probably also doesn't work.

## Mushoz | 2021-04-27T08:51:37+00:00
@DeeDeeRanged I am uing Arch Linux. I think you misunderstood me though. MSR mod seems to work fine when I use xmrig under root as expected. However, I am trying to NOT run the program under root, and use the MSR script manually: https://github.com/xmrig/xmrig/blob/dev/scripts/randomx_boost.sh

This should give me the same speed (since I would still be applying the MSR mod), but without having to run the program under root. However, this isn't the case at the moment. I run the MSR script (under root), and then start the miner (under my regular user), but then my speed is sub 10kh/s, which is way below what I get when I run the application itself under root.

@Spudz76 Huge pages are working fine under non-root as far as I can tell. "Huge pages" still comes back as "supported".

## xmrig | 2021-04-27T10:06:30+00:00
Huge pages are always supported on Linux, but you need sure it 100% allocated https://xmrig.com/docs/miner/hugepages so if you do not run as root you must reserve huge pages. Next time better provide miner log from startup as text or screenshot.
Thank you.


## DeeDeeRanged | 2021-04-30T10:34:44+00:00
If I am not mistaken, I can easily be, msr optioncan only be applied under root/sudo as the kernel devs implemented it that way. AFAIK it is a fairly recent change to the recent kernels.

## Spudz76 | 2021-04-30T18:45:54+00:00
Yes that is true however OP is saying they apply the MSRs as root (in another shell) and then launch xmrig (not as root) and the MSRs don't appear to be already set like they should be.  MSRs are singularly in the CPU and not subject to sessions or shells or users or sandboxes, so root setting them in one shell should persist everywhere globally until reboot.

Unlike hugepages there is no access needed by the non-root xmrig if the MSRs are already what it would have set them to...

## Spudz76 | 2021-04-30T18:48:19+00:00
I suppose another question is, when you apply MSR with the script, what does `rdmsr` say about the same locations?

If it doesn't read back what you wrote then something else is at play (it's ignoring your write, without blocking it).

You also have to have Secure Boot disabled for MSR stuff to work.  Linux can have all the write access it likes but it will just be ignored silently by BIOS.

## DeeDeeRanged | 2021-04-30T21:36:34+00:00
I have secure boot disabled (nvidia) and not having to jump through hoops to get it to work on Debian.

I wille try tomorrow with the msr script and see what results I get. To late for me to experiment ;)

## DeeDeeRanged | 2021-04-30T21:57:51+00:00
Actually I was to curious so I tried it on my notebook.
Ran the msr boost script  with sudo got 

Detected Intel CPU
./randomx_boost.sh: line 32: wrmsr: command not found
MSR register values for Intel applied

Started xmrig as user 
* ABOUT        XMRig/6.10.0 gcc/5.4.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1j hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    disabled
 * CPU          Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz (1) 64-bit AES
                L2:1.0 MB L3:6.0 MB 4C/8T NUMA:1
 * MEMORY       3.2/15.5 GB (20%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmrpool.eu:9999 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:10060 
 * OPENCL       disabled
 * CUDA         11.2/11.2/6.5.0
 * NVML         11.460.73.01/460.73.01 press e for health report
 * CUDA GPU     #0 01:00.0 GeForce GTX 1050 1493/3504 MHz smx:5 arch:61 mem:3927/4042 MB

[2021-04-30 23:48:48.945]  msr      cannot read MSR 0x000001a4
[2021-04-30 23:48:48.945]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW


## DeeDeeRanged | 2021-04-30T22:16:45+00:00
Had to install msr-tools for the wrmsr
sudo ./randomx_boost.sh works now but xmrig as user still barfs at
[2021-05-01 00:01:32.204]  msr      cannot read MSR 0x000001a4
[2021-05-01 00:01:32.204]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
I have a sneaky feeling  you can only read msr register as root

## Spudz76 | 2021-05-01T06:12:01+00:00
Yes but if you set xmrig as user config for `rdmsr:false, wrmsr:false` then it should not complain (and the overall idea is the hashrate should be the same as when run as root with those enabled and it saying it worked, etc - and it doesn't much matter if xmrig "thinks" it will be slow it couldn't look... so it can't know... but the ultimate proof is the hashrate)  Some cpus have larger difference with msrs, others may be difficult to see the difference.

Also, after the boost script does `rdmsr 0x1a4` say `0x0f`?

## DeeDeeRanged | 2021-05-01T13:46:05+00:00
After running sudo randox_boost.sh, sudo rdmsr 0x1a4 shows f.
Ran sudo xmrig and as user xmrig no real change in hashrate.
Did as you suggeted rdmsr:false, wrmsr:false in config.json and it doesn't complain anymore abt  msr. :+1:  it works, now have to make a systemd file out of it so msr gets set with every reboot.

# Action History
- Created by: Mushoz | 2021-04-21T11:18:35+00:00
- Closed at: 2022-04-03T14:40:43+00:00
