---
title: 'zsh: segmentation fault macOS apple M1 silicon run CPU miner '
source_url: https://github.com/xmrig/xmrig/issues/3330
author: CassandraBala
assignees: []
labels:
- bug
- arm
- randomx
created_at: '2023-09-12T15:58:31+00:00'
updated_at: '2023-11-23T15:26:07+00:00'
type: issue
status: closed
closed_at: '2023-11-23T15:26:07+00:00'
---

# Original Description
zsh: segmentation fault sudo ./xmrig -o stratum+ssl://rx.unmineable.com:443 -a rx -k -u -p x

**Describe the bug**
A clear and concise description of what the bug is.
ABOUT XMRig/6.20.0 clang/14.0.3
LIBS libuv/1.46.0 OpenSSL/3.1.2 hwloc/2.9.2
HUGE PAGES unavailable
1GB PAGES unavailable
CPU Apple M1 (1) 64-bit AES
L2:16.0 MB L3:0.0 MB 8C/8T NUMA:1
MEMORY 8/16.0 GB (50%)
DONATE 1%
POOL https://github.com/xmrig/xmrig/issues/1 stratum+ssl://rx.unmineable.com:443 algo rx/0
COMMANDS hashrate, pause, resume, results, connection
OPENCL disabled
CUDA disabled
[2023-09-12 10:39:48.128] net use pool rx.unmineable.com:443 TLSv1.3 165.227.182.82
[2023-09-12 10:39:48.129] net fingerprint (SHA-256): "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
[2023-09-12 10:39:48.129] net new job from rx.unmineable.com:443 diff 100001 algo rx/0 height 2972661 (57 tx)
[2023-09-12 10:39:48.129] cpu use argon2 implementation default
[2023-09-12 10:39:48.130] randomx init dataset algo rx/0 (8 threads) seed 28ce4902cef60d2a...
[2023-09-12 10:39:48.130] randomx allocated 2336 MB (2080+256) huge pages 0% 0/1168 +JIT (0 ms)
[2023-09-12 10:39:56.230] randomx dataset ready (8100 ms)
[2023-09-12 10:39:56.231] cpu use profile rx (8 threads) scratchpad 2048 KB
zsh: segmentation fault sudo ./xmrig -o stratum+ssl://rx.unmineable.com:443 -a rx -k -u -p x

**To Reproduce**
Steps to reproduce the behavior.

run from terminal window in macOS:

sudo ./xmrig -o stratum+ssl://rx.unmineable.com:443 -a rx -k -u BTC:xxxxxxxxxxxxxxxxxxxxxx -p x

**Expected behavior**
A clear and concise description of what you expected to happen.
It supposed to run but its throwing an error "[
](zsh: segmentation fault sudo ./xmrig -o stratum+ssl://rx.unmineable.com:443 -a rx -k -u -p x)

**Required data**
 - Miner log as text or screenshot - attached above
 - Config file or command line (without wallets) -none
 - OS: MacOS ventura 13.5.2 (22G91) version, 
 - For GPU related issues: information about GPUs and driver version - N/A
 
Apple Silicon M1 CPU, MacOS ventura 13.5.2 (22G91) version, still having zsh: segmentation fault!. xmrig 6.20.0 version
what is/are the fix for this ? anyone help on this**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2023-09-12T16:43:54+00:00
It's a known issue with Apple silicon CPUs and newer SDKs: https://github.com/monero-project/monero/issues/8657#issuecomment-1331416941
You have to use older SDK to compile anything that has RandomX mining code.

## SChernykh | 2023-10-19T15:54:33+00:00
Fixed in #3346

# Action History
- Created by: CassandraBala | 2023-09-12T15:58:31+00:00
- Closed at: 2023-11-23T15:26:07+00:00
