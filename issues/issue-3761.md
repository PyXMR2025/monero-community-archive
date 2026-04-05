---
title: Not an issue but discussion about signifigant improvemment in Hs with Memory
  timings/clocks/voltages/stability.
source_url: https://github.com/xmrig/xmrig/issues/3761
author: jekv2
assignees: []
labels: []
created_at: '2026-01-20T00:53:05+00:00'
updated_at: '2026-01-20T00:58:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
So, I upgraded the FW of my Asus TUF B850 Gaming WIFI motherboard from 1079 to TUF-GAMING-B850-PLUS-WIFI-ASUS-1402, In the process of upgrading any MB FW, you must set defaults of the motherboard BIOS/UEFI settings as I've always known since 2002.

I have learned something very important about Monero mining with xmrig. This have sat in the back of my head to test but never had.

Memory Timings is very crucial to xmrig.

My RIG:
TUF-GAMING-B850-PLUS-WIFI-ASUS
AMD AM5 9950x
GSkill Trident Z5 f5-6800j3445g16gx2-tz5rk SK-Hynix A-Die
Nvidia Founders Edition RTX 3060-TIFE

 --------
Latest XMRig date of this post.
I loaded up my OS Linux Mint 22.3. All updated-n-upgraded, latest kernel previously.

Default UEFI settings: Default motherboard CPU overclock settings the board defaults to, @ 5.11Ghz on load. Default RAM settings.
Ran xmrig, 20,000 Kh/s.
--------
Custom RAM timings/Voltages and clocked under specs of this set of ram @ 6200 & FCLK@ 2200 w/tight timings that I made sure is stable with Memtest software months ago installed on mint.

Default motherboard CPU overclock settings the board defaults to, @ 5.11Ghz w/ the custom ram settings explained above, I ran XMRig and got 26,000Kh/s.
--------
That is a 6000 Kh/s improvement by enabling my stable Ram timings/voltages/clock settings.
--------
Now if I PBO set the CPU overclock, I get 27,000Kh/s but unstable I believe and drops down from 27 to 20/18/15/5 Kh/s over a matter of time.

So motherboard default overclock settings seems good for now, but on overclock.net there is a PBO tuning guide that I do not understand how to do but if someone has the same/near same setup, you could PBO tweaking and get the best out of your AM5 CPU for xmrig.

So, Ram timings are crucial for xmrig.

It took about two weeks for stability settings with finding on the net with similar setups as mine memory timings to start off with, tweaking/tuning stability benchmarking tests to the timings I have discovered works stably.

25,900 Kh/s because I am using the PC of time of screen shot.
<img width="1214" height="463" alt="Image" src="https://github.com/user-attachments/assets/c99d3e24-0508-4422-9ed0-bcf6304bcb51" />

# Discussion History
# Action History
- Created by: jekv2 | 2026-01-20T00:53:05+00:00
