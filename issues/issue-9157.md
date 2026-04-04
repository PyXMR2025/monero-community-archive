---
title: I'm getting lots of stacktrace exceptions (running sethforprivacy's monero
  Docker)
source_url: https://github.com/monero-project/monero/issues/9157
author: FlavioB79
assignees: []
labels:
- low priority
- more info needed
created_at: '2024-02-08T19:01:42+00:00'
updated_at: '2024-02-13T19:18:28+00:00'
type: issue
status: closed
closed_at: '2024-02-13T19:18:28+00:00'
---

# Original Description
Hi all.
I'm getting a lot of these log entries:
2024-02-08 18:45:19.031	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:45:19.031	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:45:19.031	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:45:56.715	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:45:56.715	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:45:56.715	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:46:04.724	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:46:04.725	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:46:04.725	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:49:28.493	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:49:28.493	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:49:28.502	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:49:58.577	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:49:58.578	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:49:58.578	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:50:38.895	    7f8767648b38	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:50:38.895	    7f8767648b38	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:50:38.895	    7f8767648b38	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:53:35.191	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:53:35.191	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:53:35.191	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:53:44.125	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:53:44.125	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:53:44.125	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:54:43.679	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:54:43.679	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:54:43.679	[P2P1]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:55:13.763	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:55:13.763	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:55:13.763	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2024-02-08 18:57:29.171	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2024-02-08 18:57:29.171	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2024-02-08 18:57:29.171	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	

I'm running the latest monerod composed by sethforprivacy (Docker) on my Synology NAS.
Is the above relevant/critical?

BR,
F.

# Discussion History
## 0xFFFC0000 | 2024-02-13T12:19:08+00:00
Thanks for reporting this. Usually `std::bad_alloc` means a memory allocation issue. 

1. Do you have any other issue other than these outputs in the log? 
2. How much memory (RAM) does your system have?
3. I am not familiar with Synology NAS. Do you have SSH access to your NAS? I want to check the memory while running the `monerod`. 

## selsta | 2024-02-13T12:22:20+00:00
It might be this https://github.com/monero-project/monero/issues/8790#issuecomment-1498511918

It's harmless and you can ignore it if you don't have other issues.

## FlavioB79 | 2024-02-13T18:41:51+00:00
Hi.
1. I don't have any issues at all, just curious to know if the reported
logs are relevant or not.
2. 2 GB
3. See here:

top - 19:40:44 up 79 days, 23 min,  1 user,  load average: 1.64, 1.57, 1.35
[IO: 0.88, 1.14, 1.05 CPU:

Tasks: 405 total,   2 running, 403 sleeping,   0 stopped,   0 zombie

%Cpu(s):  7.4 us,  5.0 sy,  0.0 ni, 65.4 id, 22.1 wa,  0.0 hi,  0.0 si,  0.0
st

GiB Mem :    1.785 total,    0.105 free,    1.194 used,    0.485 buff/cache

GiB Swap:    3.072 total,    0.651 free,    2.421 used.    0.350 avail Mem


  PID USER      PR  NI    VIRT    RES  %CPU  %MEM     TIME+ S COMMAND


 9148 root      20   0  120.2m   7.8m 4.605 0.424 218:52.88 S
/var/packages/ActiveInsight/target/bin/+

  546 root       0 -20    0.0m   0.0m 2.632 0.000 901:41.15 D [kswapd0:0]


 8786 root      10 -10 1069.2m   9.5m 1.974 0.518 590:57.56 S /bin/python3
/var/packages/ActiveInsigh+

 8876 TM        20   0   94.8m  26.1m 1.974 1.430   0:24.84 S
***@***.***/SMBServic+

12537 root      20   0  642.1m   4.5m 1.316 0.245 270:10.36 S
/usr/syno/bin/scemd

15340 admin     20   0   33.4m   3.3m 1.316 0.181   0:02.12 R top


 1547 PlexMed+  20   0   55.6m   0.5m 0.658 0.029  22:19.35 S Plex Plug-in [
org.musicbrainz.agents.mu+

 1869 PlexMed+  20   0   62.6m   0.6m 0.658 0.032  22:15.14 S Plex Plug-in
[com.plexapp.agents.themov+

 5289 1000      20   0  0.192t 256.9m 0.658 14.06 215:26.02 S monerod
--non-interactive --rpc-restric+

 8172 root      20   0    0.0m   0.0m 0.658 0.000   3:08.50 S [md3_raid1]

BR,
F.

https://www.instagram.com/boniforti_music
https://soundcloud.com/boniforti_music
https://bonny-j.bandcamp.com


Am Di., 13. Feb. 2024 um 13:19 Uhr schrieb 0xFFFC0000 <
***@***.***>:

> Thanks for reporting this. Usually std::bad_alloc means a memory
> allocation issue.
>
>    1. Do you have any other issue other than these outputs in the log?
>    2. How much memory (RAM) does your system have?
>    3. I am not familiar with Synology NAS. Do you have SSH access to your
>    NAS? I want to check the memory while running the monerod.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/9157#issuecomment-1941390269>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AIEUZR2LXMBJQ5VVO4TBFCDYTNK4RAVCNFSM6AAAAABDAIRGN6VHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMYTSNBRGM4TAMRWHE>
> .
> You are receiving this because you authored the thread.Message ID:
> ***@***.***>
>


# Action History
- Created by: FlavioB79 | 2024-02-08T19:01:42+00:00
- Closed at: 2024-02-13T19:18:28+00:00
