---
title: mac, debug build error
source_url: https://github.com/monero-project/monero/issues/3286
author: jtgrassie
assignees: []
labels: []
created_at: '2018-02-18T06:57:10+00:00'
updated_at: '2018-02-21T18:08:58+00:00'
type: issue
status: closed
closed_at: '2018-02-21T18:08:58+00:00'
---

# Original Description
```
make debug
...
[ 81%] Linking CXX shared library libp2p.dylib
Undefined symbols for architecture x86_64:
  "cryptonote::arg_testnet_on", referenced from:
      ___cxx_global_var_init.29 in net_node.cpp.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[3]: *** [src/p2p/libp2p.dylib] Error 1
make[2]: *** [src/p2p/CMakeFiles/p2p.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [debug] Error 2
```

Appears #3170 is the culprit.

# Discussion History
## tewinget | 2018-02-18T07:02:13+00:00
@xmr_eric perhaps this is the cause of your recent testnet issue as well?

On Feb 18, 2018 1:57 AM, "Jethro Grassie" <notifications@github.com> wrote:

> make debug
> ...
> [ 81%] Linking CXX shared library libp2p.dylib
> Undefined symbols for architecture x86_64:
>   "cryptonote::arg_testnet_on", referenced from:
>       ___cxx_global_var_init.29 in net_node.cpp.o
> ld: symbol(s) not found for architecture x86_64
> clang: error: linker command failed with exit code 1 (use -v to see invocation)
> make[3]: *** [src/p2p/libp2p.dylib] Error 1
> make[2]: *** [src/p2p/CMakeFiles/p2p.dir/all] Error 2
> make[1]: *** [all] Error 2
> make: *** [debug] Error 2
>
> Appears #3170 <https://github.com/monero-project/monero/pull/3170> is the
> culprit.
>
> —
> You are receiving this because you are subscribed to this thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/3286>, or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5pHVhfele2DiL7W4RloIi3tLmzktks5tV8nKgaJpZM4SJl_0>
> .
>


## jtgrassie | 2018-02-18T07:14:35+00:00
@xmr-eric what was the issue you had?

## stoffu | 2018-02-18T07:42:24+00:00
#3288 

# Action History
- Created by: jtgrassie | 2018-02-18T06:57:10+00:00
- Closed at: 2018-02-21T18:08:58+00:00
