---
title: 'Segmentation fault: 11 / MAC OS 12 Beta / Newest Version'
source_url: https://github.com/xmrig/xmrig/issues/2604
author: artdj007
assignees: []
labels: []
created_at: '2021-09-24T20:41:57+00:00'
updated_at: '2021-09-26T18:23:20+00:00'
type: issue
status: closed
closed_at: '2021-09-26T18:23:20+00:00'
---

# Original Description
Last login: Fri Sep 24 21:27:40 on ttys000

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
macbooks-MacBook-Pro-2:~ macbook$ /Users/macbook/Downloads/xmrig-6.15.1/xmrig ; exit;
 * ABOUT        XMRig/6.15.1 clang/12.0.5
 * LIBS         libuv/1.42.0 OpenSSL/1.1.1l hwloc/2.5.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Apple M1 (1) 64-bit AES
                L2:8.0 MB L3:0.0 MB 8C/8T NUMA:1
 * MEMORY       7.7/8.0 GB (97%)
 * DONATE       1%
 * POOL #1      stratum+ssl://rx.unmineable.com:443 algo rx/0
 * COMMANDS     hashrate, pause, resume, results, connection
 * OPENCL       disabled
 * CUDA         disabled
[2021-09-24 22:30:24.202]  net      use pool rx.unmineable.com:443 TLSv1.2 159.65.25.23
[2021-09-24 22:30:24.203]  net      fingerprint (SHA-256): "baf587d7fcd7dedd153e6f7b9a66ff8242f75dcc06e76a776e4a22c76ea469e7"
[2021-09-24 22:30:24.203]  net      new job from rx.unmineable.com:443 diff 100001 algo rx/0 height 2456595 (98 tx)
[2021-09-24 22:30:24.203]  cpu      use argon2 implementation default
[2021-09-24 22:30:24.203]  randomx  init dataset algo rx/0 (8 threads) seed 72e63d3dacd06059...
[2021-09-24 22:30:24.203]  randomx  allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2021-09-24 22:30:29.638]  randomx  dataset ready (5434 ms)
[2021-09-24 22:30:29.638]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2021-09-24 22:30:29.638]  cpu      READY threads 8/8 (8) huge pages 0% 0/8 memory 16384 KB (1 ms)
<img width="826" alt="Bildschirmfoto 2021-09-24 um 21 28 15" src="https://user-images.githubusercontent.com/91348381/134737220-89382c32-2c00-486c-baa1-e9408b277980.png">
logout
Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Prozess beendet]


# Discussion History
## Spudz76 | 2021-09-25T15:00:25+00:00
Beta6 broken, Beta7 allegedly works fine again

https://github.com/xmrig/xmrig/issues/2570#issuecomment-927108806

## artdj007 | 2021-09-26T18:23:10+00:00
love it.. haha ;)

# Action History
- Created by: artdj007 | 2021-09-24T20:41:57+00:00
- Closed at: 2021-09-26T18:23:20+00:00
