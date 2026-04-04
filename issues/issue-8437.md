---
title: monero-blockchain-stats crashes with IOT instruction error
source_url: https://github.com/monero-project/monero/issues/8437
author: Thor-x86
assignees: []
labels: []
created_at: '2022-07-15T15:06:51+00:00'
updated_at: '2022-07-17T17:16:34+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm currently using `Monero 'Oxygen Orion' (v0.17.3.2-release)` on Arch Linux x86-64 with Intel Atom D510 CPU. When I run `monero-blockchain-stats`, it throws these

```
2022-07-15 14:51:48.165 W Starting...
2022-07-15 14:51:48.166 W Initializing source blockchain (BlockchainDB)
/usr/include/c++/12.1.0/bits/unique_ptr.h:445: typename std::add_lvalue_reference<_Tp>::type std::unique_ptr<_Tp, _Dp>::operator*() const [with _Tp = cryptonote::Blockchain; _Dp = std::default_delete<cryptonote::Blockchain>; typename std::add_lvalue_reference<_Tp>::type = cryptonote::Blockchain&]: Assertion 'get() != pointer()' failed.
zsh: IOT instruction  sudo -u monero monero-blockchain-stats --data-dir=/srv/monero --log-level=4
```

The daemon already run since an hour ago. I think this is a problem from compiler's optimization. I'll tell you whether it's working or not after I build it on my server.

# Discussion History
## Thor-x86 | 2022-07-17T17:16:34+00:00
I did some experiments and turns out that's all because of `-Ofast` compiler flag. I already pull request [here](https://github.com/monero-project/monero/pull/8441). Here's what have I done:

```
Compiler at: AMD Ryzen 7-3700U
Executed at: AMD Ryzen 7-3700U
Result: Success
```

```
Compiler at: AMD Ryzen 7-3700U
Executed at: Intel Atom D510
Result: Failed - IOT illegal instruction
```

```
Compiler at: Intel Atom D510
Executed at: Intel Atom D510
Result: Success
```

```
Compiler at: AMD Ryzen 7-3700U
Executed at: Intel Atom D510
Extra: -Ofast changed to -O2
Result: Success
```

# Action History
- Created by: Thor-x86 | 2022-07-15T15:06:51+00:00
