---
title: 27k drops to 21 or less k screenshot
source_url: https://github.com/xmrig/xmrig/issues/3706
author: jekv2
assignees: []
labels: []
created_at: '2025-09-09T17:20:58+00:00'
updated_at: '2026-01-20T12:50:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
edit2:
Solution:
https://github.com/xmrig/xmrig/issues/3706#issuecomment-3352953903
end edit:

Edit:
Jump to 
https://github.com/xmrig/xmrig/issues/3706#issuecomment-3343830801
end edit:

I have done all the optimizations in the reddit guide for xmrig for win10x64 https://www.reddit.com/r/MoneroMining/comments/f18825/windows_10_tuning_guide_for_randomx_mining/ and that it keeps dropping down to 21 or less k hs from 27 and above, sometimes it can run 12 hours then drop, other times 5 minutes, longest I seen it run 27k is i think 12 hours or less.

9950x.

I disabled virtualization as well in uefi.

I'm drove mad to the point of not mining monero no more. I have no idea why this keeps happening, also it kept doing this on linux mint so I jumped to win10 and seen a big increase in HS over linux mint on win10 so stuck with win10, now i am combating this irritating significant hash rate drop that does not go back up until reboot. No events happen in event logger of win10.

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/5e806066-dfd6-4543-ab47-13bc8909c36a" />

# Discussion History
## SChernykh | 2025-09-09T18:22:28+00:00
You have two XMRigs running in your screenshot, maybe this is the reason. If not, my only advice is to start the task manager and check what else is using CPU when you get hashrate drops. Also, check CPU core speeds and temperatures in HWInfo monitor.

## jekv2 | 2025-09-10T03:16:36+00:00
> You have two XMRigs running in your screenshot, maybe this is the reason. If not, my only advice is to start the task manager and check what else is using CPU when you get hashrate drops. Also, check CPU core speeds and temperatures in HWInfo monitor.

Second xmrig was for nvidia rtx 3060TI FE, I stopped it, and been trying to mine all day with 27 drops to 22-21 like as if CPU goes to stock clocks, cuz at stock thats what it mines at 21k. PBO overclock of pbo/advanced 10x 200 85c temp, ccd0 negative 20 ccd1 negative 30. I read somewhere maybe here a day ago or so, someone had same problem and found out it was PBO percision boost overdrive. They disabled it. But if I do that, I will only get 21k :(. Asus TUF B850-Plus & 9950x. If unstable memory timings and overclock, could that cause it to crash down to 21k? Because the other day it was running fine at a strong 27.5k for good while, I left the room and came back and it was at 21k hs. No screen saver, all power set to performance. 

27707 right now nice and strong. Temps are great. Also, say like I used mspaint, it dropped but it goes back up when I leave the win10 GUI alone, mouse, not opening apps etc..

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/5b0b0394-91ba-4afd-b541-6ec35e10d919" />

## jekv2 | 2025-09-10T12:34:36+00:00
Worst I've ever seen, it dropped down to 18k over night. Something with the OS, I just know it.

Temps are fine.

<img width="1544" height="679" alt="Image" src="https://github.com/user-attachments/assets/8169cf8e-09b7-4448-a3dc-3054ecbe9ae9" />

## jekv2 | 2025-09-10T16:09:10+00:00
I found out, someone has been breaking in and accessing my computer. I put up a camera on my PC n keyboard and left and came back, And it is solid, also I ran a memtest and passed. And prime benchmark passed.

Also on the camera and sound when I was gone, there are sounds as if someone was in here when I was gone.

So, it's someone commanding something in powershell or cmd as admin to make it drop. I knew my system is stable.

Here is proof. Also I can upload the the video with the sounds if possible.

![Image](https://github.com/user-attachments/assets/5a852fe9-81ce-4921-bd31-b730bf840e22)
![Image](https://github.com/user-attachments/assets/ba70f5c9-c12a-4ff4-8dcf-1eb0bc260a2a)
![Image](https://github.com/user-attachments/assets/d885e82b-3659-464f-b9d6-4821a24bdac2)
![Image](https://github.com/user-attachments/assets/30d52339-287e-410c-b91f-b96960db2b6e)
<img width="1200" height="805" alt="Image" src="https://github.com/user-attachments/assets/db44fec6-9ec8-4339-bb4f-8b461e4ce9ea" />

## jekv2 | 2025-09-10T17:01:23+00:00
I am going to install a desktop screen recorder.

## jekv2 | 2025-09-28T16:02:15+00:00
I believe someone is using a screen recorder on my Linux Mint machine. and as well previously my win10 os same machine but I have Mint on it now.

I jumped to linux mint see if it would solve the problem.

I'd leave the house come back and hash would be dropped bad.

So I decided to install simple screen recorder for linux. 

https://github.com/MaartenBaert/ssr

My hash rate drops from 27k and to 22k-18k-17khs/s.

I started simple screen recorder, my hash went from 27k to 25k to 18k. Stop recording and xmrig does not recover back to 27k until a restart. Even with closing xmrig and reopening it, also my 9950x temp should be around 82c and drops to 70c obviously showing that xmrig is not recovering back to 27k hs/s.

Screenshots.

<img width="1214" height="667" alt="Image" src="https://github.com/user-attachments/assets/75b03e7c-c524-4049-9c6d-6889554ca150" />
<img width="371" height="313" alt="Image" src="https://github.com/user-attachments/assets/2eb721d1-c802-4087-9759-1119133b8913" />

## jekv2 | 2025-09-30T16:26:44+00:00
I am not sure but I believe I found the problem.

Will see after 24 hours. It's been 10minutes and no hash rate crashes.

I removed 

hugepagesz=1GB default_hugepagesz=1GB hugepages=6 

on LM 22.2.

from /etc/default/grub/

Usually it would crash using Waterfox or Firefox.

I am sitting at a steady 82.c @ 
27648.4 27649.1 n/a H/s max 27778.2 H/s

Time will tell.

<img width="1214" height="463" alt="Image" src="https://github.com/user-attachments/assets/43acc311-3b01-4146-bcb5-d036e58f9a49" />

## jekv2 | 2025-10-01T01:01:23+00:00
https://github.com/xmrig/xmrig/issues/3706#issuecomment-3352953903

## jekv2 | 2025-10-01T12:31:45+00:00
Nope it's back.

Happened at 6:35 am this morning.

06:35:55.838]  miner    speed 10s/60s/15m 27483.8 27476.0 27415.1 H/s max 27747.8 H/s
[2025-10-01 06:35:55.850]  cpu      accepted (13971/7) diff 97857 (39 ms)
[2025-10-01 06:35:56.042]  cpu      accepted (13972/7) diff 97857 (40 ms)
[2025-10-01 06:36:03.927]  cpu      accepted (13973/7) diff 97857 (51 ms)
[2025-10-01 06:36:08.781]  cpu      accepted (13974/7) diff 97857 (38 ms)
[2025-10-01 06:36:14.415]  cpu      accepted (13975/7) diff 97857 (38 ms)
[2025-10-01 06:36:24.218]  cpu      accepted (13976/7) diff 97857 (38 ms)
[2025-10-01 06:36:25.268]  cpu      accepted (13977/7) diff 97857 (45 ms)
[2025-10-01 06:36:28.745]  cpu      accepted (13978/7) diff 97857 (38 ms)
[2025-10-01 06:36:39.124]  cpu      accepted (13979/7) diff 97857 (53 ms)
[2025-10-01 06:36:43.682]  cpu      accepted (13980/7) diff 97857 (77 ms)
[2025-10-01 06:36:48.778]  cpu      accepted (13981/7) diff 97857 (43 ms)
[2025-10-01 06:36:53.988]  cpu      accepted (13982/7) diff 97857 (38 ms)
[2025-10-01 06:36:55.023]  cpu      accepted (13983/7) diff 97857 (68 ms)
[2025-10-01 06:36:55.872]  miner    speed 10s/60s/15m 20406.3 22711.4 27099.1 H/s max 27747.8 H/s

## geekwilliams | 2025-10-01T16:44:29+00:00
I see you haven't posted the full output of xmrig at start, or your config.json.  Can you do both of those things?  

In one of your screenshots you are using "americas.mining-dutch.nl" as a pool, and that pool supports automatic algorithm switching.  I suspect that may be part of the issue you're experiencing.  

## jekv2 | 2026-01-20T11:49:04+00:00
> I see you haven't posted the full output of xmrig at start, or your config.json. Can you do both of those things?
> 
> In one of your screenshots you are using "americas.mining-dutch.nl" as a pool, and that pool supports automatic algorithm switching. I suspect that may be part of the issue you're experiencing.


Here is the config. I took off the aggressive cpu overclock and left the UEFI default settings for the CPU. Instead 27,000 H/s, it was @ 25,855 kH/s but after 11.5 hours of mining about 8 minutes before I woke, it dropped to 20,000 kH/s. Oddly, 8 minutes or so, give or take a min.

All temps are great.

You may find more information here I created last night.
https://github.com/xmrig/xmrig/issues/3761

My mint machine has been mining xmr for 11.5 hours from last night, about 8 minutes prior to waking up and checking the hash rate, my hash rate went from 25,855 down to 20 Kh/s and will not recover.

Also, I have set in my dutch-mining account to strictly mine only xmr, no coin switching.

Also I have tried a different pool a few days ago with Hash rate drop as the same as dutch-mining.

--------
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
        "1gb-pages": true,
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
        "asm": "ryzen",
        "argon2-impl": null,
        "argon2": [0, 12, 1, 13, 2, 14, 3, 15, 4, 16, 5, 17, 6, 18, 7, 19, 8, 20, 9, 21, 10, 22],
        "cn": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 3],
            [1, 4],
            [1, 5],
            [1, 6],
            [1, 7],
            [1, 8],
            [1, 9],
            [1, 10],
            [1, 11]
        ],
        "cn-heavy": [
            [1, 0],
            [1, 1],
            [1, 2],
            [1, 6],
            [1, 7],
            [1, 8]
        ],
        "cn-lite": [
            [1, 0],
            [1, 12],
            [1, 1],
            [1, 13],
            [1, 2],
            [1, 14],
            [1, 3],
            [1, 15],
            [1, 4],
            [1, 16],
            [1, 5],
            [1, 17],
            [1, 6],
            [1, 18],
            [1, 7],
            [1, 19],
            [1, 8],
            [1, 20],
            [1, 9],
            [1, 21],
            [1, 10],
            [1, 22],
            [1, 11],
            [1, 23]
        ],
        "cn-pico": [
            [2, 0],
            [2, 12],
            [2, 1],
            [2, 13],
            [2, 2],
            [2, 14],
            [2, 3],
            [2, 15],
            [2, 4],
            [2, 16],
            [2, 5],
            [2, 17],
            [2, 6],
            [2, 18],
            [2, 7],
            [2, 19],
            [2, 8],
            [2, 20],
            [2, 9],
            [2, 21],
            [2, 10],
            [2, 22],
            [2, 11],
            [2, 23]
        ],
        "cn/upx2": [
            [2, 0],
            [2, 12],
            [2, 1],
            [2, 13],
            [2, 2],
            [2, 14],
            [2, 3],
            [2, 15],
            [2, 4],
            [2, 16],
            [2, 5],
            [2, 17],
            [2, 6],
            [2, 18],
            [2, 7],
            [2, 19],
            [2, 8],
            [2, 20],
            [2, 9],
            [2, 21],
            [2, 10],
            [2, 22],
            [2, 11],
            [2, 23]
        ],
        "ghostrider": [
            [8, 0],
            [8, 1],
            [8, 2],
            [8, 3],
            [8, 4],
            [8, 5],
            [8, 6],
            [8, 7],
            [8, 8],
            [8, 9],
            [8, 10],
            [8, 11]
        ],
        "rx": [0, 16, 1, 17, 2, 18, 3, 19, 4, 20, 5, 21, 6, 22, 7, 23, 8, 24, 9, 25, 10, 26, 11, 27, 12, 28, 13, 29, 14, 30, 15, 31],
        "rx/wow": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 25, 26, 27, 28, 29, 30, 31],
        "cn-lite/0": false,
        "cn/0": false,
        "rx/arq": "rx/wow"
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
        "nvml": true,
        "cn": [
            {
                "index": 0,
                "threads": 34,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-heavy": [
            {
                "index": 0,
                "threads": 18,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-lite": [
            {
                "index": 0,
                "threads": 70,
                "blocks": 24,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn-pico": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "cn/upx2": [
            {
                "index": 0,
                "threads": 4,
                "blocks": 64,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "kawpow": [
            {
                "index": 0,
                "threads": 256,
                "blocks": 16384,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": false
            }
        ],
        "rx": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "rx/arq": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "rx/wow": [
            {
                "index": 0,
                "threads": 32,
                "blocks": 16,
                "bfactor": 0,
                "bsleep": 0,
                "affinity": -1,
                "dataset_host": true
            }
        ],
        "cn-lite/0": false,
        "cn/0": false
    },
    "log-file": null,
    "donate-level": 1,
    "donate-over-proxy": 0,
    "pools": [
        {
            "algo": "rx/0",
            "coin": "XMR",
            "url": "stratum+tcp://americas.mining-dutch.nl:3340",
            "user": "VisuallausiV.worker1-cpu",
            "pass": "d=1450000",
            "rig-id": null,
            "nicehash": false,
            "keepalive": true,
            "enabled": true,
            "tls": true,
            "sni": false,
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
    "dns": {
        "ip_version": 0,
        "ttl": 30
    },
    "user-agent": null,
    "verbose": 0,
    "watch": true,
    "pause-on-battery": false,
    "pause-on-active": false
}
----------

<img width="1214" height="922" alt="Image" src="https://github.com/user-attachments/assets/035ae8e8-0f93-4eac-a967-c600d33c5060" />
<img width="1214" height="922" alt="Image" src="https://github.com/user-attachments/assets/32b3716e-b820-40cd-8da3-7d6056686d9b" />

## jekv2 | 2026-01-20T12:13:29+00:00
Also for a note:

Couple months ago, I tried a different mining software, I forget which miner software, same results.

I have also tried to seek support at linux mint forums and got no where with support and was criticized from stating someone is accessing my mint machine physically and then being accessed remotely.

As stated, screen recording that I have tested results in the same behavior finding on accident, and does not recover.

Something is being activated on my mint machine that I am not aware of what by intruders/invaders. Obviously by showing evidence above.

Edit:
Also, I have everything updated, upgraded, and cleaned by using:
sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt clean -y && sudo apt autoclean -y

Edit2:
After a reboot, attached.

Edit3:
I wonder by the intruders, something is being activated and resulting in a memory allocation problem?
Similar problem:
https://www.reddit.com/r/MoneroMining/comments/h7kjgj/xmrig_with_half_the_hashrate_if_i_open_after_a/

<img width="1214" height="463" alt="Image" src="https://github.com/user-attachments/assets/05ed5fb1-b2ce-4745-9453-833744bed7f6" />

# Action History
- Created by: jekv2 | 2025-09-09T17:20:58+00:00
