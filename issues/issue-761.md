---
title: Windows 64 issues GUI Beta 2  Black screen/crashing.
source_url: https://github.com/monero-project/monero-gui/issues/761
author: Throwaway674422
assignees: []
labels: []
created_at: '2017-06-08T03:01:12+00:00'
updated_at: '2017-07-03T09:54:12+00:00'
type: issue
status: closed
closed_at: '2017-07-03T09:54:12+00:00'
---

# Original Description
I am having an issue with the beta gui.  When trying to run the exe it just opens a black screen, hangs, then crashes. I have also tried to run the low-graphics batch file, with no luck. When I double click it, cmd window pops up, then closes immediately, that is it.

Running Windows 7 Ultimate
Intel I7 12gb

Log
https://paste.fedoraproject.org/paste/m7LZhp6te8ExH6WXO3mq6V5M1UNdIGYhyRLivL9gydE=



# Discussion History
## muusbolla | 2017-06-08T18:10:20+00:00
I had this issue today on Windows 7 64bit as well. The logfile didn't seem to show anything meaningful for me either. Restarting my PC fixed it... sigh, Windows.

## Throwaway674422 | 2017-06-08T19:50:26+00:00
I have restarted multiple times with no avail.   

## eth125754 | 2017-06-12T09:08:05+00:00
I'm having a very similar issue. Exact same log.

The process monero-wallet-gui runs but no screen shows. 

Windows 10 64bit

## Jaqueeee | 2017-06-13T06:40:51+00:00
@eth125754 Have you tried the low graphic bat file?

## eth125754 | 2017-06-13T17:23:18+00:00
Yeah, that starts a command line but nothing is displayed on it. It starts a process as well but nothing else happens as far as I can tell.

## medusadigital | 2017-06-20T09:59:14+00:00
@eth125754  can you tell us what computer you have ? 

## Pecral | 2017-06-20T13:23:05+00:00
I've experienced the same problem as you and it was reproducable as soon as I've used Google's DNS servers (8.8.8.8 and 8.8.4.4) - The problem didn't occur while using my ISP's DNS server. Unfortunately your log-file isn't available anymore so I can't compare whether I had the same log-file, but you can increase your log-level to see where the process hangs.

## medusadigital | 2017-06-21T09:32:51+00:00
thanks a lot @Pecral, your feedback helps a lot

## MaxXor | 2017-06-21T13:10:54+00:00
@Pecral Never had issues with the Monero Wallet GUI on Windows 7 Enterprise 64 bit and I'm also using Google's DNS servers. 😕 Don't think it has anything to do with DNS.

## eth125754 | 2017-06-21T18:06:44+00:00
@medusadigital Sure, it's a Windows 10 Home edition 64 Bit. i5-6600K with 16GB RAM. The Moneorod runs fine, just not the gui exe. The text file reads out this:

2017-06-21 19:03:55.492	3732	INFO 	global	contrib/epee/src/mlog.cpp:145	New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,net.cn:FATAL,global:INFO,verify:FATAL,stacktrace:INFO


# Action History
- Created by: Throwaway674422 | 2017-06-08T03:01:12+00:00
- Closed at: 2017-07-03T09:54:12+00:00
