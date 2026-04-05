---
title: 'zsh: segmentation fault on macOS 12 beta 6'
source_url: https://github.com/xmrig/xmrig/issues/2570
author: wwessex
assignees: []
labels: []
created_at: '2021-09-01T12:43:23+00:00'
updated_at: '2025-06-16T20:49:37+00:00'
type: issue
status: closed
closed_at: '2025-06-16T20:49:37+00:00'
---

# Original Description
Hi,
I know it is still a beta but thought I'd let you know that XMRig says zsh: segmentation fault in beta 6 of macOS 12, however it did not say that in the other betas and worked. 

# Discussion History
## kabutar111 | 2021-09-02T11:52:00+00:00
i have the same issue after update to beta 6

## wwessex | 2021-09-02T14:25:14+00:00
> i have the same issue after update to beta 6

I’ve reported it in the Apple Feedback Assistant you may want to do the same.

## wwessex | 2021-09-02T18:24:50+00:00
P.S. if you build from the beta XMRig branch that works. But oddly not in the Dev branch version. 

## ReturnRei | 2021-09-03T16:26:01+00:00
Same issue here with xmrig. Also getting segfaults in jetbrains suite since beta 6 upgrade

## Spudz76 | 2021-09-04T00:06:18+00:00
I think the beta branch is pretty old and hasn't been remerged to master in a while.  (beta branch is `v6.2.0-beta` vs master branch is `v6.15.0`) So that is equivalent to running an older version before quite a few major changes.  If you checkout by version/release tags in the master branch and narrow down which version still works it will help find the place where the problem was introduced.  You could probably jump several minors such as 6.5.0 or even 6.10.0 and if that's broken then step back to save time of testing every release.

It could be related to hugepages, does it still fault when all hugepage options are disabled?  Are you using the brew versions of the three deps (hwloc/openssl/libuv) or did you try building the ones included (with `./scripts/build-deps.sh`)?  It may be possible to figure out which feature is the problem that way.

And I'm assuming it does this immediately before any output, not later when it's initializing an algo.  Correct?

## Spudz76 | 2021-09-04T00:12:32+00:00
jetbrains also exploding alludes to actual Apple bug, though.  Maybe it will just work again in b7...

## kty0113 | 2021-09-11T11:47:38+00:00
i have the same issue. (mac os beta build 21A5506j)

## cstrouse | 2021-09-17T14:41:29+00:00
v6.10.0 built from source using native homebrew versions of deps seg faults on 21A5506j.

```
casey@Hopper build % ./xmrig
 * ABOUT        XMRig/6.10.0 clang/13.0.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       15.0/16.0 GB (94%)
 * DONATE       1%
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-09-17 07:38:53.083]  net      use pool rx.unmineable.com:3333  139.59.164.251
[2021-09-17 07:38:53.084]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2451407
[2021-09-17 07:38:53.084]  cpu      use argon2 implementation default
[2021-09-17 07:38:53.084]  randomx  init dataset algo rx/0 (8 threads) seed [...]
[2021-09-17 07:38:53.085]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2021-09-17 07:38:56.864]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2451407
[2021-09-17 07:38:58.169]  randomx  dataset ready (5084 ms)
[2021-09-17 07:38:58.169]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-09-17 07:38:58.170]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
zsh: segmentation fault  ./xmrig
```

Fails as well with huge pages disabled.
```
casey@Hopper build % ./xmrig --no-huge-pages
 * ABOUT        XMRig/6.10.0 clang/13.0.0
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       13.8/16.0 GB (86%)
 * DONATE       1%
 * POOL #1      rx.unmineable.com:3333 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-09-17 07:42:31.795]  net      use pool rx.unmineable.com:3333  138.68.148.132
[2021-09-17 07:42:31.796]  net      new job from rx.unmineable.com:3333 diff 100001 algo rx/0 height 2451409
[2021-09-17 07:42:31.796]  cpu      use argon2 implementation default
[2021-09-17 07:42:31.796]  randomx  init dataset algo rx/0 (8 threads) seed [...]
[2021-09-17 07:42:31.797]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (1 ms)
[2021-09-17 07:42:36.803]  randomx  dataset ready (5006 ms)
[2021-09-17 07:42:36.803]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-09-17 07:42:36.804]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
zsh: segmentation fault  ./xmrig --no-huge-pages
```

v6.5.0 doesn't segfault but bogs the system down immediately and makes the UI almost unusable. This happens regardless of whether huge pages are enabled or not.

## artdj007 | 2021-09-25T03:32:15+00:00
are someone fixed the problem? using zsh it doesn't work also without. I just get an issue.

 * ABOUT        XMRig/6.15.1 clang/12.0.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.9/8.0 GB (99%)
 * DONATE       1%
 * POOL #1      stratum+ssl://rx.unmineable.com:443 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-09-25 05:29:44.365]  net      use pool rx.unmineable.com:443 TLSv1.2 159.65.25.23
[2021-09-25 05:29:44.366]  net      fingerprint (SHA-256): "baf587d7fcd7dedd153e6f7b9a66ff8242f75dcc06e76a776e4a22c76ea469e7"
[2021-09-25 05:29:44.366]  net      new job from rx.unmineable.com:443 diff 100001 algo rx/0 height 2456846 (20 tx)
[2021-09-25 05:29:44.366]  cpu      use argon2 implementation default
[2021-09-25 05:29:44.366]  randomx  init dataset algo rx/0 (8 threads) seed 72e63d3dacd06059...
[2021-09-25 05:29:44.366]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2021-09-25 05:29:49.879]  randomx  dataset ready (5513 ms)
[2021-09-25 05:29:49.879]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-09-25 05:29:49.881]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (2 ms)
Segmentation fault: 11
logout
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

## wwessex | 2021-09-25T11:40:07+00:00
It is working fine now in beta 7

## cstrouse | 2021-09-26T18:30:13+00:00
I updated to beta 7 and this still exhibits the same behavior.

UPDATE: Actually, 6.15.0 works but 6.15.1 seg faults on beta 7.

## furic | 2023-03-21T04:20:44+00:00
I have the same issue on 6.19.0, and macOS 13.2.1.

I think it may be about notarization and code-signing.

# Action History
- Created by: wwessex | 2021-09-01T12:43:23+00:00
- Closed at: 2025-06-16T20:49:37+00:00
