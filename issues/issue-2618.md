---
title: Feature request.
source_url: https://github.com/xmrig/xmrig/issues/2618
author: toxicroadkill
assignees: []
labels: []
created_at: '2021-10-06T23:50:39+00:00'
updated_at: '2021-10-16T19:19:09+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
would it be possible to add more stats to the web api, the stats that apear when xmrig first starts, memory.

 ABOUT        XMRig/6.15.1 gcc/9.3.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   supported
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-3770S CPU @ 3.10GHz (1) 64-bit AES
                L2:1.0 MB L3:8.0 MB 4C/8T NUMA:1
 * MEMORY       3.7/3.7 GB (98%)
                DIMM_A0: 2 GB DDR3 @ 1600 MHz M378B5773DH0-CK0  
                DIMM_B0: 2 GB DDR3 @ 1600 MHz M378B5773DH0-CK0  
 * MOTHERBOARD  Dell Inc. - 0V8WGR
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      192.168.1.134:10201 algo auto
 * POOL #2      192.168.1.135:10201 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     192.168.2.101:10000 

(just add the stats that are not there at the moment)

i have a rather large monero farm, and having the info at a glance would make it much easier to manage what works and what doens't and compare machine's performance

should be a pretty simple thing to add, it would be very handy to have those stats at a glance


# Discussion History
## Spudz76 | 2021-10-07T01:51:31+00:00
Memory and motherboard info is in `/2/dmi`

CPU info and other junk is in `/2/backends` and `/2/summary`

## toxicroadkill | 2021-10-07T02:17:41+00:00
cool, just what i was seeking...thanks for getting it added so soon ;)



> On Oct 6, 2021, at 8:51 PM, Tony Butler ***@***.***> wrote:
> 
> 
> Memory and motherboard info is in /2/dmi
> 
> CPU info and other junk is in /2/backends
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2618#issuecomment-937379736>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O3YIJHCLHVT7U435ZF3UFT4K3ANCNFSM5FQAJ5LQ>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> 



## Spudz76 | 2021-10-07T16:42:06+00:00
What's not added is good API docs for the newer API. :)

I grep the source for `/1/` or `/2/` to figure out what endpoints exist lol.

## toxicroadkill | 2021-10-07T16:52:52+00:00
docs would be a great thing

:)



> On Oct 7, 2021, at 11:42 AM, Tony Butler ***@***.***> wrote:
> 
> 
> What's not added is good API docs for the newer API. :)
> 
> I grep the source for /1/ or /2/ to figure out what endpoints exist lol.
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub <https://github.com/xmrig/xmrig/issues/2618#issuecomment-937970171>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ASD5O35I6Z66TUMFLMFTR2TUFXEWRANCNFSM5FQAJ5LQ>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> 



## OreoCupcakes | 2021-10-10T23:24:20+00:00
I don't know if this is done, since I can't find any documentation on it, but is there a way via command line to auto exit (Ctrl+C) XMRig after it completes a benchmark? I'm trying to have a script run the benchmark X times and log it, without my input, but the Ctrl+C command to exit XMRig is preventing me from doing it.

## Spudz76 | 2021-10-11T02:25:48+00:00
No that isn't wired into the API.  Only read-only information and status, or writable but all you can do is send a new configfile, there are no other control knobs.

You can send a signal with kill, `SIGHUP` (1) or `SIGTERM` (15) or `SIGINT` (2) and it will exit.  Technically CTRL-C sends a `SIGINT` anyway so it doesn't matter which way the app hears "signal 2".  So `kill -2 $pid` or `kill -INT $pid` should work quite the same as sending a CTRL-C into its stdin (which is tougher to grab than stdout).

## OreoCupcakes | 2021-10-11T02:43:07+00:00
Is there a way to do it in Windows command line/Powershell? When I try to do it with taskkill, XMRig still requires me to send the Ctrl-C command and then the script would send my taskkill command which wouldn't do anything since XMRig already exited. 

## toy1111 | 2021-10-16T19:19:09+00:00
This is what I use in Powershell - get xmrig process info and if exists kill the process.

function kill-miner {
    $xmr = Get-Process "xmrig" -ea SilentlyContinue
    if ($xmr) {
       Stop-Process -InputObject $xmr -Force
    }
}

# Action History
- Created by: toxicroadkill | 2021-10-06T23:50:39+00:00
