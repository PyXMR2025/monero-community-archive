---
title: rpc timeout and take too much memory
source_url: https://github.com/monero-project/monero/issues/2786
author: bitkevin
assignees: []
labels: []
created_at: '2017-11-09T16:51:42+00:00'
updated_at: '2017-11-13T17:56:26+00:00'
type: issue
status: closed
closed_at: '2017-11-13T17:56:26+00:00'
---

# Original Description
I use monerod for mining pool but it's NOT stable at all, always get rpc timeout every few hours.

* monerod version: `Monero 'Helium Hydra' (v0.11.1.0-release)`
* docker OS version: `Ubuntu 16.04 LTS`
* `Linux bbfc38982c34 4.4.0-62-generic #83-Ubuntu SMP Wed Jan 18 14:10:15 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux`

And it took TOO much memory, over than 18GB, see below:

```
top - 00:49:29 up 86 days,  9:45,  1 user,  load average: 0.94, 1.12, 1.14
Tasks: 570 total,   1 running, 569 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.7 us,  0.9 sy,  0.2 ni, 96.9 id,  0.0 wa,  0.0 hi,  0.3 si,  0.0 st
KiB Mem:  13203644+total, 12692653+used,  5109912 free,   739732 buffers
KiB Swap:        0 total,        0 used,        0 free. 10933664+cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
23744 root      20   0 57.867g 0.018t 0.018t S   2.0 14.9 507:04.66 monerod
31556 root      20   0 3464.5m 1.361g  12.9m S   3.0  1.1   4291:21 bitcoind
21020 root      20   0 2989.3m 1.089g  11.4m S   0.3  0.9 239:14.35 litecoind
```

# Discussion History
## moneromooo-monero | 2017-11-09T17:41:46+00:00
https://github.com/monero-project/monero/pull/2737 might help for the RPC timeouts. Please report. If it doesn't tell us which RPC call(s) fail(s).

About the RAM, it's fine, most of it is cache and the OS is free to take it back.


## bitkevin | 2017-11-10T08:45:51+00:00
@moneromooo-monero I use rpc call `getblocktemplate` for mining. Just patched monerod with #2737, will report again tmr.

## moneromooo-monero | 2017-11-10T09:54:07+00:00
getblocktemplate can be a heavy call. There's a caching branch at https://github.com/moneromooo-monero/bitmonero/tree/cache-block-template (which might need rebasing).

## bitkevin | 2017-11-10T13:04:18+00:00
After apply the #2737 patch, RPC call timeout still the same. Usually when it happen, will hang for 5~15 minutes, nothing could get from monerod.

## moneromooo-monero | 2017-11-10T13:29:20+00:00
OK, that's way too long. When this happens, please get an all thread stack trace please. You can do that either with:
```
pstack `pidof monerod`
```
or:
```
gdb /path/to/monerod `pidof monerod`
bt
```
(replace /path/to/monerod with the actual path)


## bitkevin | 2017-11-13T17:05:49+00:00
After I switched my dns server to `8.8.8.8`, this problem seems fixed. So I think it's checkpoints cause this issue.

https://github.com/monero-project/monero/issues/1535#issuecomment-343519511 

# Action History
- Created by: bitkevin | 2017-11-09T16:51:42+00:00
- Closed at: 2017-11-13T17:56:26+00:00
