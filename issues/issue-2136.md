---
title: Really low hash rate on Xeon with 2 processors?
source_url: https://github.com/xmrig/xmrig/issues/2136
author: MantisRay
assignees: []
labels:
- question
created_at: '2021-02-27T04:49:07+00:00'
updated_at: '2021-04-12T14:09:55+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:09:55+00:00'
---

# Original Description
I have a dual processor Xeon on Windows 7 with 64GB of memory running XMRig 6.9 with no other processes running on the system except for those that are part of the O/S.  I believe I'm getting a really low hash rate based on what I've read on this issues forum and the web.  I am running in administrator mode to get huge page support and during initialization the console window showed messages saying that huge page support had been enabled.

I have not used any of the processor or thread affinity settings and my config.json file is pretty basic, as you can see below:
```
{
    "autosave": true,
    "donate-level": 15,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "xmr.pool.gntl.co.uk:20009",
            "user": "not shown",
            "pass": "main",
            "keepalive": true,
            "tls": true
        }
    ]
}
```

The Win7 Performance window shows consistently a CPU consumption of 53 to 56 percent.  Below is a snapshot of my XMR mining history.  Why are my figures so low and how can I improve them?  I thought that a multi-core box with 16 cores and 64GB of memory with huge page support enabled would do well with the ASIC-resistant RandomX algo.  Or has the game gone back to the GPU and ASIC rigs again?

Also, I thought you only had to run XMRig in admin mode once to get the huge pages flag set.  I tried running XMRig in user mode after first launching it admin mode and the console window showed messages saying huge pages could not be enabled.  I went back to admin mode but I'd prefer to run in user mode if I can.

Here is a snapshot of my mining history:

![grafik](https://user-images.githubusercontent.com/79736102/109375689-c32a0e80-788c-11eb-9bdb-3aad3e24d413.png)


# Discussion History
## xmrig | 2021-02-27T06:50:54+00:00
You didn't mention which Xeons exactly, so nothing I can say about hashrate.
You can't use hugepages on Windows 7 without admin privileges unlike Windows 10.
Thank you.

## MantisRay | 2021-02-27T15:01:54+00:00
> 
> 
> You didn't mention which Xeons exactly, so nothing I can say about hashrate.
> You can't use hugepages on Windows 7 without admin privileges unlike Windows 10.
> Thank you.

Intel(R) Xeon(R) CPU-E5-2670 0 @2.60 GHz (2 processors)

## SChernykh | 2021-02-27T15:13:33+00:00
It should be 6700 h/s: https://xmrig.com/benchmark/4LZmaA
Check that huge pages and MSR mod are enabled, also check that each CPU has 4x RAM sticks installed for it in appropriate slots (check your motherboard mannual).

## MantisRay | 2021-02-27T15:23:20+00:00
> 
> 
> It should be 6700 h/s: https://xmrig.com/benchmark/4LZmaA
> Check that huge pages and MSR mod are enabled, also check that each CPU has 4x RAM sticks installed for it in appropriate slots (check your motherboard mannual).

What is my current hash rate?  I'm not sure how to read the hash reports shown in my screenshot above.  How do I interpret the 10s/60s/15m line in the report and convert it to a total hash rate based on the fact XMRig is using ~50% CPU?

The RAM slots appear to be filled properly.  As far as huge pages, I rechecked config.json and it appears that XMRig has updated the values to that shown below from the initial values I used from the wizard and I see field values that shows "true" for "huge-pages" but "false" for "huge-pages-jit", "1gb-pages" and "memory-pool":
```
{
    "api": {
        "id": null,
        "worker-id": null
    },
    "http": {
        "enabled": false,
        "host": "127.0.0.1",
        "port": 0,
        "access-token": null,
        "restricted": true
    },
    "autosave": true,
    "background": false,
    "colors": true,
    "title": true,
    "randomx": {
        "init": -1,
        "init-avx2": -1,
        "mode": "auto",
        "1gb-pages": false,
        "rdmsr": true,
        "wrmsr": true,
        "cache_qos": false,
        "numa": true,
        "scratchpad_prefetch_mode": 1
    },
    "cpu": {
        "enabled": true,
        "huge-pages": true,
        "huge-pages-jit": false,
        "hw-aes": null,
        "priority": null,
        "memory-pool": false,
        "yield": true,
        "asm": true,
        "argon2-impl": null,
        "astrobwt-max-size": 550,
        "astrobwt-avx2": false,
        "argon2": [not shown],
        "cn-heavy": [
not shown],
        "cn-pico": [
not shown],
        "rx": [not shown],
        "rx/wow": [not shown],
        "cn/0": false,
        "cn-lite/0": false,
        "rx/arq": "rx/wow",
        "rx/keva": "rx/wow"
    },
    "opencl": {
        "enabled": false,
        "cache": true,
        "loader": null,
        "platform": "AMD",
        "adl": true
    },
    "cuda": {
        "enabled": false,
        "loader": null,
        "nvml": true
    },
    "log-file": null,
    "donate-level": 15,
    "donate-over-proxy": 15,
    "pools": [
        {
            "algo": null,
            "coin": null,
            "url": "xmr.pool.gntl.co.uk:20009",
            "user": "not shown",
            "pass": "first-test",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "tls-fingerprint": null,
            "daemon": false,
            "socks5": null,
            "self-select": null,
            "submit-to-origin": false
        }
    ],
    "retries": 5,
    "retry-pause": 5,
    "print-time": 60,
    "health-print-time": 60,
    "dmi": true,
    "syslog": false,
    "tls": {
        "enabled": false,
        "protocols": null,
        "cert": null,
        "cert_key": null,
        "ciphers": null,
        "ciphersuites": null,
        "dhparam": null
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
```

## MantisRay | 2021-02-27T15:23:53+00:00
> MSR mod

How do I check to see if "MSR mod" is enabled?

## SChernykh | 2021-02-27T16:42:33+00:00
You just start XMRig and check all the messages it prints at startup, make sure there's nothing in red or yellow in these messages.

## MantisRay | 2021-02-27T17:04:04+00:00
> 
> 
> You just start XMRig and check all the messages it prints at startup, make sure there's nothing in red or yellow in these messages.

Here is my startup screenshot.  I do see a message about MSR being successfully enabled but it looks like that despite running in admin mode, huge pages are not being enabled.  Is there a doc that gives steps on how to diagnose and fix this issue?

![grafik](https://user-images.githubusercontent.com/79736102/109394177-a1b03d80-78f3-11eb-9984-d65f1ff60d63.png)


## SChernykh | 2021-02-27T17:26:34+00:00
It says `Huge pages unavailable` on your screentshot. I don't know why, but you probably need to manually enable them. 
- From the Start menu, open Local Security Policy (under Administrative Tools).
- Under Local Policies\User Rights Assignment, double click the Lock Pages in Memory setting.
- Click Add User or Group and type your Windows user name.
- Either log off and then log back in or restart your computer

## MantisRay | 2021-02-27T18:57:20+00:00
> 
> 
> It says `Huge pages unavailable` on your screentshot. I don't know why, but you probably need to manually enable them.
> 
>     * From the Start menu, open Local Security Policy (under Administrative Tools).
> 
>     * Under Local Policies\User Rights Assignment, double click the Lock Pages in Memory setting.
> 
>     * Click Add User or Group and type your Windows user name.
> 
>     * Either log off and then log back in or restart your computer

There was a bit of an anomaly.  When I went into Local Security Policy for the "Lock Pages in Memory" setting, I already saw my user account name (admin), so that wasn't working.   As a test I tried:

- Removed "admin" from the group
- Re-added it
- Clicked on "Check names"
- The system offered me a drop-down box with "admin" and "MAIN-PC\admin". 
- I selected "MAIN-PC\admin" and added it
- Restarted my system

After rebooting I tried running XMRig again and huge pages worked.  It appears that, at least on Windows 7, you have add the admin user with the PC name prefixing it to grant that user the ability to lock/unlock pages.  The user name alone won't work.

Thank you for all your help.  I see this now when I mine:

![grafik](https://user-images.githubusercontent.com/79736102/109397137-32dae080-7903-11eb-82ec-0345b650fd26.png)

Does this mean my hash rate is now ~6560 H/s?  If so, is that about right for my particular PC?

If so, how long should I wait to see a credit to my wallet from xmr.pool.gntl.co.uk:20009 at that hash rate before thinking something is wrong?



## MantisRay | 2021-02-27T19:02:29+00:00
Is there any real point to increasing the CPU percentage from 50% to higher values?  For example, would 75% give me better hashing without doing any signifant harm to the life of my PC, or is not worth it?  

Or is XMRig cycling between different cores to give them a chance to cool down and not suffer thermal damage so higher CPU percentage values would defeat that protection?

Would any of the process or thread affinity settings make a real difference?  By real difference I mean something more than a 10% improvement in hash rate without noticeably decreasing the life span of the PC.  As I said before, currently about 1/2 the cores are in use at any point in time and CPU consumption hovers between around 53 and 56%.


## SChernykh | 2021-02-27T19:02:32+00:00
Yes, hashrate is correct now for your CPU. You need to wait until this pool finds a block and then ~2 hours (for 60 network confirmations) and then you should see a balance on the pool. That pool finds blocks not very often so you'll have to wait.

Increasing number of threads will not improve hashrate because you're limited by L3 cache in your CPUs. XMRig chooses affinity automatically in the most optimal way.

## MantisRay | 2021-02-27T21:51:32+00:00
Can you give me a gross figure such as, a week, month, etc?  This way, if I don't see a credit in my wallet in a week for example I know not to bother mining anymore because it isn't working for me.  

Also how would a rig of 4 1060ti's compare against a box like mine?  I'm wondering if a GPU rig is still a superior choice for XMR.

Thank you plenty for all your help.

## coolhaircut | 2021-03-05T22:35:23+00:00
Make sure you only count _physical_ cores, not threads. With 2x E5-2670's, you only have 16 cores, not 32.

## Spudz76 | 2021-03-11T17:01:25+00:00
GPUs are horrible for all RandomX based algos, by design.  So no, 4x1060ti would not be any better mostly just wasting watts.

Your rig is doing very good rate.  Threadrippers blow Xeons out of the water though, which might be why you are losing to others on your pool (probably AMD with huge caches and huge number of cores).

# Action History
- Created by: MantisRay | 2021-02-27T04:49:07+00:00
- Closed at: 2021-04-12T14:09:55+00:00
