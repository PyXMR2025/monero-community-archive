---
title: '3640.403148] traps: monero-wallet-c[69627] trap invalid opcode ip:560de6f1beee
  sp:7ffc15a953c0 error:0 in monero-wallet-cli[560de69dd000+85f000]'
source_url: https://github.com/monero-project/monero/issues/9962
author: flogbl
assignees: []
labels: []
created_at: '2025-06-19T19:43:26+00:00'
updated_at: '2025-06-20T18:00:55+00:00'
type: issue
status: closed
closed_at: '2025-06-20T18:00:55+00:00'
---

# Original Description
Hello,

I've got a problem when launching this  :
```
$ ./monero-wallet-cli 
Instruction non permise
```

in dmesg :
`[ 4043.300215] traps: monero-wallet-c[70036] trap invalid opcode ip:55614c29feee sp:7ffcbe46a560 error:0 in monero-wallet-cli[55614bd61000+85f000]`

strace (don't know if it can help) :
```
[...]
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x7f2221915000, 94683)           = 0
getrandom("\xf4\x5a\x5d\x5f\xac\x18\x67\x17", 8, GRND_NONBLOCK) = 8
brk(NULL)                               = 0x5595759e5000
brk(0x559575a06000)                     = 0x559575a06000
futex(0x7f2220a1773c, FUTEX_WAKE_PRIVATE, 2147483647) = 0
uname({sysname="Linux", nodename="debian", ...}) = 0
openat(AT_FDCWD, "/dev/urandom", O_RDONLY|O_NOCTTY|O_CLOEXEC) = 3
read(3, "\3070\2\34\341\252\26\25\5K\240\17( \202b2\5\241Xw\30\214\311UX\205\352z0;\367", 32) = 32
close(3)                                = 0
brk(0x559575a27000)                     = 0x559575a27000
mlock(0x5595526a8000, 4096)             = 0
openat(AT_FDCWD, "/sys/devices/system/cpu/online", O_RDONLY|O_CLOEXEC) = 3
read(3, "0-11\n", 1024)                 = 5
close(3)                                = 0
brk(0x559575a48000)                     = 0x559575a48000
mmap(NULL, 204800, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f222056c000
mmap(NULL, 155648, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f2220546000
brk(0x559575a74000)                     = 0x559575a74000
--- SIGILL {si_signo=SIGILL, si_code=ILL_ILLOPN, si_addr=0x559552003eee} ---
+++ killed by SIGILL +++
Instruction non permise
```

Doesn't someone have an idea of how to resolve this problem ?

# Discussion History
## vtnerd | 2025-06-19T21:55:31+00:00
What type of box are you running on, and what build of `monero-wallet-cli` are you using? Most likely it is something armv8 related.

## flogbl | 2025-06-20T18:00:55+00:00
It's a x64 (ryzen) from a self compiled version of the v0.18. 
After cleaning all and recompile , all is now OK.
With my apologies.

# Action History
- Created by: flogbl | 2025-06-19T19:43:26+00:00
- Closed at: 2025-06-20T18:00:55+00:00
