---
title: guix binaries sync faster than those from depends workflow
source_url: https://github.com/seraphis-migration/monero/issues/259
author: plowsof
assignees: []
labels: []
created_at: '2025-12-09T14:36:23+00:00'
updated_at: '2025-12-11T18:13:53+00:00'
type: issue
status: closed
closed_at: '2025-12-11T18:13:53+00:00'
---

# Original Description
with Monero 'FCMP++ / Carrot alpha stressnet' (v0.19.0.0-alpha.1.4-44531c467) from x86_64 Linux @ 
https://github.com/seraphis-migration/monero/actions/runs/19939827839 sync is very slow
```
2025-12-09 14:40:09.600 I Synced 2850836/2892867 (98%, 42031 left)
2025-12-09 14:40:52.902 I Synced 2850840/2892867 (98%, 42027 left)
2025-12-09 14:41:37.704 I Synced 2850844/2892867 (98%, 42023 left, 0% of total synced, estimated 6.1 days left)
2025-12-09 14:42:21.830 I Synced 2850848/2892867 (98%, 42019 left)
```
with Monero 'FCMP++ / Carrot alpha stressnet' (v0.19.0.0-alpha.1.4-69f7b4692) sync looks normal @ https://github.com/seraphis-migration/monero/commit/69f7b46926ce90adc5ff9cf92bfc322bc027ca6f
```
2025-12-09 14:36:53.834 I SYNCHRONIZATION started
2025-12-09 14:37:05.624 I Synced 2850768/2892866 (98%, 42098 left)
2025-12-09 14:37:12.255 I Synced 2850772/2892866 (98%, 42094 left)
2025-12-09 14:37:19.359 I Synced 2850776/2892866 (98%, 42090 left)
2025-12-09 14:37:26.204 I Synced 2850780/2892866 (98%, 42086 left)
2025-12-09 14:37:32.728 I Synced 2850784/2892866 (98%, 42082 left)
2025-12-09 14:37:39.129 I Synced 2850788/2892866 (98%, 42078 left)
2025-12-09 14:37:45.511 I Synced 2850792/2892866 (98%, 42074 left)
2025-12-09 14:37:52.200 I Synced 2850796/2892866 (98%, 42070 left)
2025-12-09 14:37:58.617 I Synced 2850800/2892866 (98%, 42066 left)
2025-12-09 14:38:05.748 I Synced 2850804/2892866 (98%, 42062 left)
2025-12-09 14:38:12.189 I Synced 2850808/2892866 (98%, 42058 left)
2025-12-09 14:38:18.617 I Synced 2850812/2892866 (98%, 42054 left)
```
1.4 release:

```
2025-12-09 14:53:46.070 I Synced 2851131/2892870 (98%, 41739 left)
2025-12-09 14:53:46.111 I Synced 2851135/2892870 (98%, 41735 left)
2025-12-09 14:53:46.160 I Synced 2851139/2892870 (98%, 41731 left)
2025-12-09 14:53:46.288 I Synced 2851143/2892870 (98%, 41727 left)
2025-12-09 14:53:46.421 I Synced 2851147/2892870 (98%, 41723 left)
2025-12-09 14:53:46.793 I Synced 2851151/2892870 (98%, 41719 left)
2025-12-09 14:53:48.785 I Synced 2851155/2892870 (98%, 41715 left)
2025-12-09 14:53:50.571 I Synced 2851159/2892870 (98%, 41711 left)
2025-12-09 14:53:52.463 I Synced 2851163/2892870 (98%, 41707 left)
2025-12-09 14:53:54.188 I Synced 2851167/2892870 (98%, 41703 left)
2025-12-09 14:53:55.691 I Synced 2851171/2892870 (98%, 41699 left)
2025-12-09 14:53:57.428 I Synced 2851175/2892870 (98%, 41695 left)
2025-12-09 14:53:59.049 I Synced 2851179/2892870 (98%, 41691 left)
2025-12-09 14:54:00.822 I Synced 2851183/2892870 (98%, 41687 left)
2025-12-09 14:54:02.752 I Synced 2851187/2892870 (98%, 41683 left)
2025-12-09 14:54:04.431 I Synced 2851191/2892870 (98%, 41679 left)
```

am i just seeing the already mentioned regression in sync found by ofrnxmr?

back to 4453:
```
2025-12-09 15:08:56.228 I Synced 2851693/2892877 (98%, 41184 left)
2025-12-09 15:09:44.359 I Synced 2851706/2892877 (98%, 41171 left)
2025-12-09 15:10:45.108 I Synced 2851719/2892877 (98%, 41158 left, 0% of total synced, estimated 2.1 days left)
```

# Discussion History
## plowsof | 2025-12-09T19:55:56+00:00
using https://github.com/j-berman/monero/actions/runs/19940678057
```
$ grep -a synced hello-world.log-release 
2025-12-09 19:14:46.667	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855091/2892967 (98%, 37876 left, 0% of total synced, estimated 4.7 days left) (21.726540 sec, 0.046027 blocks/sec), 225.727539 MB queued in 66 spans, stripe 2 -> 2
2025-12-09 19:16:56.198	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855102/2892967 (98%, 37865 left, 0% of total synced, estimated 4.9 days left) (17.338837 sec, 0.057674 blocks/sec), 319.543365 MB queued in 91 spans, stripe 2 -> 2
2025-12-09 19:19:04.683	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855120/2892968 (98%, 37848 left, 0% of total synced, estimated 4.1 days left) (10.759900 sec, 0.092938 blocks/sec), 561.632324 MB queued in 162 spans, stripe 2 -> 2
2025-12-09 19:21:21.370	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855130/2892968 (98%, 37838 left, 0% of total synced, estimated 4.5 days left) (17.214378 sec, 0.058091 blocks/sec), 671.080872 MB queued in 204 spans, stripe 2 -> 2
2025-12-09 19:23:24.004	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855140/2892969 (98%, 37829 left, 0% of total synced, estimated 4.6 days left) (18.944736 sec, 0.052785 blocks/sec), 764.482300 MB queued in 248 spans, stripe 2 -> 2
2025-12-09 19:25:24.261	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855149/2892969 (98%, 37820 left, 0% of total synced, estimated 4.8 days left) (17.251142 sec, 0.057967 blocks/sec), 818.847656 MB queued in 290 spans, stripe 2 -> 2
2025-12-09 19:27:30.696	[P2P7]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1659	Synced 2855158/2892970 (98%, 37812 left, 0% of total synced, estimated 4.9 days left) (12.943588 sec, 0.077258 blocks/sec), 851.288757 MB queued in 316 spans, stripe 2 -> 2
```
vs v0.19.0.0-alpha.1.4-69f7b4692
```
$ grep -a synced hello-world.log-faster 
2025-12-09 19:34:17.906	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1638	Synced 2855228/2892974 (98%, 37746 left, 0% of total synced, estimated 1.8 days left) (10.512771 sec, 0.095122 blocks/sec), 662.924133 MB queued in 272 spans, stripe 2 -> 2
2025-12-09 19:36:23.074	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1638	Synced 2855254/2892974 (98%, 37720 left, 0% of total synced, estimated 1.9 days left) (5.388925 sec, 0.185566 blocks/sec), 732.622009 MB queued in 635 spans, stripe 2 -> 2
2025-12-09 19:38:25.086	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1638	Synced 2855279/2892975 (98%, 37696 left, 0% of total synced, estimated 2.0 days left) (2.396799 sec, 0.417223 blocks/sec), 850.061646 MB queued in 933 spans, stripe 2 -> 2
2025-12-09 19:40:29.813	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1638	Synced 2855299/2892975 (98%, 37676 left, 0% of total synced, estimated 2.1 days left) (8.632071 sec, 0.115847 blocks/sec), 1072.655518 MB queued in 1108 spans, stripe 2 -> 2
2025-12-09 19:42:29.889	[P2P9]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1638	Synced 2855333/2892976 (98%, 37643 left, 0% of total synced, estimated 2.0 days left) (5.410640 sec, 0.184821 blocks/sec), 1769.330811 MB queued in 1269 spans, stripe 2 -> 2
```

## j-berman | 2025-12-09T20:01:59+00:00
Can you share log level 2 with the new build for 5-10 minutes plz?

Also, what OS / RAM / CPU thread count are you using? You can see the thread count with the command `nproc` in the terminal

## plowsof | 2025-12-09T20:28:35+00:00
Ubuntu 22.04.4 LTS
8 core 64 gig ram i7-6700 CPU
`--prep-blocks-threads 8 --log-level 2` for both 

[plowsof-release-log.zip](https://github.com/user-attachments/files/24063510/plowsof-release-log.zip)

[plowsof-faster-log.zip](https://github.com/user-attachments/files/24063561/plowsof-faster-log.zip)

## j-berman | 2025-12-09T20:43:36+00:00
Got it, thanks!

Looks like this is similar to/maybe the same as #246. It's taking the new release upwards of 15s to verify 128-in FCMP++ txs on your machine, and only 4-5s on the old release.

Helpful 

## nahuhh | 2025-12-09T21:40:30+00:00
Fwiw i synced the same 10 blocks (2892890-2892899) using 1.4 and 1.5 and got similar sync times. `--prep-blocks-threads=$(nproc) --block-sync-size=1` was set for both runs

1.4 = 4:37
1.5 = 5.04

very possible that there werent many/any 128in txs in this sample (i didnt check)



## j-berman | 2025-12-11T02:06:01+00:00
@plowsof for the sync that looks normal/fast, are you possibly using the GUIX build? The GUIX build is the one that's included here: https://github.com/seraphis-migration/monero/releases

## plowsof | 2025-12-11T03:52:35+00:00
I'm almost certain im using the binaries from `depends` GH workflows for both. tomorrow im going to go through the commits and see which one triggers my slowdown, binary search method :) ill be able to confirm where it happens, and compare guix too.

## plowsof | 2025-12-11T11:55:56+00:00
re-confirmed that GUIX binaries sync quicker than those found in the depends workflow, thanks for the tip! is this known and to be expected?

## j-berman | 2025-12-11T17:33:05+00:00
This is a known/expected thing, and I had forgotten.

The depends builds use Rust v1.69 ([to work around issues building on Ubuntu 20.04](https://github.com/seraphis-migration/monero/blob/498d90af139b20a60ed16bb2237a3c79e4592ed8/.github/workflows/depends.yml#L87-L89)), and the [GUIX builds use Rust v1.85.1](https://github.com/monero-project/monero/pull/9440).

Performance regressions using Rust v1.69 were noted [here](https://github.com/kayabaNerve/fcmp-plus-plus/issues/16)

# Action History
- Created by: plowsof | 2025-12-09T14:36:23+00:00
- Closed at: 2025-12-11T18:13:53+00:00
