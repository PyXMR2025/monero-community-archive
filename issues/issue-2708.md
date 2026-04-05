---
title: Bus Error
source_url: https://github.com/xmrig/xmrig/issues/2708
author: Netricko
assignees: []
labels: []
created_at: '2021-11-19T15:14:39+00:00'
updated_at: '2021-11-20T13:06:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Describe the bug**
when i'm trying to start a miner with a command ./xmrig with parameters -o -u -p i get a problem, after
 
>[2021-11-19 14:41:02.029]  randomx  dataset ready (4637 ms)
[2021-11-19 14:41:02.030]  cpu      use profile  rx  (4 threads) scratchpad 2048 KB
Bus error

I get a "Bus error". I'm running old asus tinkerboard S 32bit with DietPi os, i cannot use any proposed solution from bug #446 as command 
>set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -Wall -fno-exceptions -fno-rtti -Wno-missing-braces")

returns 

> -bash: syntax error near unexpected token `CMAKE_CXX_FLAGS'

 and i can't seem to find a syntax error, i copied this command proposed in mentioned thread.

"gdb ./xmrig" returns this:

> GNU gdb (Debian 10.1-1.7) 10.1.90.20210103-git
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "arm-linux-gnueabihf".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

>For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./xmrig...
(No debugging symbols found in ./xmrig)

as well as "r" command returns this:
>Starting program: /root/xmrig/build/xmrig
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/arm-linux-gnueabihf/libthread_db.so.1".
[2021-11-19 15:04:40.498] unable to open "/root/xmrig/build/config.json".
[2021-11-19 15:04:40.498] unable to open "/root/.xmrig.json".
[2021-11-19 15:04:40.498] unable to open "/root/.config/xmrig.json".
[2021-11-19 15:04:40.498] no valid configuration found, try https://xmrig.com/wizard
[Inferior 1 (process 6778) exited with code 02]

tried xmrig wizard as well

send help please :(


# Discussion History
## Spudz76 | 2021-11-20T06:12:26+00:00
RandomX requires 2.1GB minimum to even launch

Tinkerboard S has 2GB total.

## Killer-Software | 2021-11-20T13:06:49+00:00
Hi Everyone,
I'm facing the same issues once I start the miner with a command ./xmrig with parameters -o -u -k it gives an error: "bus error (core dumped)". I have been searching for a solution and have tried a lot of things but no solution found yet. my system is Intel(R) Xeon(R) CPU @ 2.20GHz with 8GB ram run Linux. If you find any solution do let me know plz as I'm new to mining as well as Linux.

# Action History
- Created by: Netricko | 2021-11-19T15:14:39+00:00
