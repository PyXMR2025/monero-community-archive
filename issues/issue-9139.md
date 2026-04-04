---
title: Month-long reorgs in logs
source_url: https://github.com/monero-project/monero/issues/9139
author: quakemmo
assignees: []
labels:
- question
created_at: '2024-01-29T09:43:43+00:00'
updated_at: '2024-01-30T12:18:22+00:00'
type: issue
status: closed
closed_at: '2024-01-29T13:11:52+00:00'
---

# Original Description
What is going on here? The system is Linux running Monero 0.18.3.1 behind a firewall, mostly idling and keeping in sync.
I didn't remove anything from that log excerpt for completeness sake.

Look for the "months behind" log lines.
Note that the node keeps pretty much in sync.

```
2024-01-26 02:00:00.045 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 03:00:00.635 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 04:00:00.801 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 04:09:19.008 I [110.40.229.103:18080 OUT] Sync data returned a new top block candidate: 3070132 -> 3248526 [Your node is 178394 blocks (8.1 months) behind] 
2024-01-26 04:09:19.008 I SYNCHRONIZATION started
2024-01-26 05:00:03.595 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 06:00:04.594 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 07:00:04.800 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 08:00:04.903 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 09:00:04.959 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 10:00:05.922 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 11:00:06.985 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 12:00:07.608 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 13:00:08.554 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 14:00:09.100 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 15:00:10.016 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 16:00:10.575 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 17:00:11.433 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 18:00:11.573 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 19:00:12.441 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 20:00:13.127 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 21:00:13.993 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 22:00:14.536 W No incoming connections - check firewalls/routers allow port 38080
2024-01-26 23:00:15.099 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 00:00:15.443 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 01:00:15.524 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 01:37:09.748 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3070760
2024-01-27 01:37:09.748 I id:   <3b52982591dae10e8dacc38657580b7738e41fa4fd6e5aabab7a3e22ef4058a5>
2024-01-27 01:37:09.748 I PoW:  <93ba72bb057429fbaf604281b5947ae4c79ef792b180cf0cca85ca0000000000>
2024-01-27 01:37:09.748 I difficulty:   267289644361
2024-01-27 01:38:15.556 I ###### REORGANIZE on height: 3070760 of 3070760 with cum_difficulty 332767068739420609
2024-01-27 01:38:15.556 I  alternative blockchain size: 2 with cum_difficulty 332767338771822167
2024-01-27 01:38:16.198 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3070760
2024-01-27 01:38:16.198 I id:   <aba9d5bd935b6c3e0169daf410f46d536c6fe84a93b317314bac0060be53f128>
2024-01-27 01:38:16.198 I PoW:  <a0aeed5c6aa3e544aeed27285fa2ef448cba65299a9a40880924e40300000000>
2024-01-27 01:38:16.198 I difficulty:   267289644361
2024-01-27 01:38:17.296 I REORGANIZE SUCCESS! on height: 3070760, new blockchain size: 3070762
2024-01-27 02:00:15.538 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 03:00:16.414 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 04:00:17.836 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 05:00:18.450 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 06:00:18.686 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 07:00:19.221 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 08:00:19.322 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 09:00:20.016 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 09:43:44.995 I [110.40.229.103:18080 OUT] Sync data returned a new top block candidate: 3070995 -> 3281044 [Your node is 210049 blocks (9.6 months) behind] 
2024-01-27 09:43:44.995 I SYNCHRONIZATION started
2024-01-27 10:00:20.154 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 11:00:20.243 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 12:00:20.530 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 13:00:20.654 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 13:56:52.116 W There were 24 blocks in the last 20 minutes, there might be large hash rate changes, or we might be partitioned, cut off from the Monero network or under attack, or your computer's time is off. Or it could be just sheer bad luck.
2024-01-27 14:00:20.745 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 15:00:26.263 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 15:08:40.207 I [185.244.193.84:18080 OUT] Sync data returned a new top block candidate: 3071178 -> 3071179 [Your node is 1 blocks (2.0 minutes) behind] 
2024-01-27 15:08:40.207 I SYNCHRONIZATION started
2024-01-27 16:00:26.314 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 17:00:26.580 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 18:00:31.411 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 19:00:31.555 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 20:00:32.375 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 20:59:10.911 I [batch] DB resize needed
2024-01-27 20:59:11.047 I LMDB Mapsize increased.  Old: 199455MiB, New: 200479MiB
2024-01-27 21:00:32.402 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 22:00:32.695 W No incoming connections - check firewalls/routers allow port 38080
2024-01-27 23:00:32.790 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 00:00:33.667 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 01:00:33.984 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 02:00:43.554 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 03:00:44.347 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 04:00:44.965 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 04:57:00.266 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 3071594
2024-01-28 04:57:00.266 I id:   <c81b2a29b3e6eb05f506fcb3f292158bf7e911759173bef9679758a0aeca192c>
2024-01-28 04:57:00.266 I PoW:  <6d853d71f064f8e772fda893ea2e0b2a38f61bccbe09935132e93f0300000000>
2024-01-28 04:57:00.266 I difficulty:   283154836511
2024-01-28 05:00:45.064 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 06:00:45.607 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 07:00:45.856 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 08:00:46.448 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 09:00:46.453 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 10:00:46.550 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 11:00:47.211 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 12:00:47.696 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 13:00:48.096 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 14:00:49.086 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 15:00:49.754 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 16:01:46.804 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 16:39:00.308 W WARNING: no two valid DNS TXT records were received
2024-01-28 17:02:01.045 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 17:40:23.894 W WARNING: no two valid DNS TXT records were received
2024-01-28 18:02:20.467 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 19:03:16.158 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 20:03:19.522 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 20:42:36.210 W WARNING: no two valid DNS TXT records were received
2024-01-28 20:44:26.106 W WARNING: no two valid DNS TXT records were received
2024-01-28 21:03:44.704 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 21:08:29.513 I [110.40.220.181:18080 OUT] Sync data returned a new top block candidate: 3072086 -> 3319722 [Your node is 247636 blocks (11.3 months) behind] 
2024-01-28 21:08:29.513 I SYNCHRONIZATION started
2024-01-28 21:42:59.798 W WARNING: no two valid DNS TXT records were received
2024-01-28 22:03:47.182 W No incoming connections - check firewalls/routers allow port 38080
2024-01-28 22:43:19.148 W WARNING: no two valid DNS TXT records were received
2024-01-28 23:03:56.671 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 00:04:01.578 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 00:47:36.055 W WARNING: no two valid DNS TXT records were received
2024-01-29 01:04:02.339 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 01:48:06.126 W WARNING: no two valid DNS TXT records were received
2024-01-29 02:04:34.983 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 02:49:16.053 W WARNING: no two valid DNS TXT records were received
2024-01-29 03:04:47.596 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 03:49:55.955 W WARNING: no two valid DNS TXT records were received
2024-01-29 04:05:52.400 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 04:57:36.386 W WARNING: no two valid DNS TXT records were received
2024-01-29 05:05:53.296 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 05:27:04.828 I Synced 3072344/3072344
2024-01-29 06:03:41.883 W WARNING: no two valid DNS TXT records were received
2024-01-29 06:06:24.918 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 07:04:42.542 W WARNING: no two valid DNS TXT records were received
2024-01-29 07:06:36.908 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 08:05:37.340 W WARNING: no two valid DNS TXT records were received
2024-01-29 08:07:32.025 W No incoming connections - check firewalls/routers allow port 38080
2024-01-29 08:44:42.102 W WARNING: no two valid DNS TXT records were received
2024-01-29 08:52:53.282 W monerod is now disconnected from the network
2024-01-29 08:52:58.387 I [72.190.17.43:18080 OUT] Sync data returned a new top block candidate: 3072444 -> 3072446 [Your node is 2 blocks (4.0 minutes) behind] 
2024-01-29 08:52:58.387 I SYNCHRONIZATION started
2024-01-29 08:52:58.582 I Synced 3072446/3072446
2024-01-29 09:07:32.973 W No incoming connections - check firewalls/routers allow port 38080
```

# Discussion History
## selsta | 2024-01-29T13:11:52+00:00
It's just someone sending garbage data, either intentionally or they tried to fork the project and don't know what they are doing. You can ignore it or ban their IPs.

## Gingeropolous | 2024-01-30T12:18:20+00:00
38080 is the wownero port. 

# Action History
- Created by: quakemmo | 2024-01-29T09:43:43+00:00
- Closed at: 2024-01-29T13:11:52+00:00
