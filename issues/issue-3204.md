---
title: wallet-cli crash in debug build
source_url: https://github.com/monero-project/monero/issues/3204
author: ph4r05
assignees: []
labels: []
created_at: '2018-01-29T18:50:18+00:00'
updated_at: '2018-01-31T12:59:24+00:00'
type: issue
status: closed
closed_at: '2018-01-31T12:59:24+00:00'
---

# Original Description
Hi,

`make debug` builds the project with shared libraries (`BUILD_SHARED_LIBS=ON`). This causes `monero-wallet-cli` to crash with the following error:

```
# the seed is made up
./build/debug/bin/monero-wallet-cli --testnet --generate-new-wallet ~/testnet/wallet_01.bin  --restore-deterministic-wallet --electrum-seed="sequence atlas unveil summon pebbles tuesday beer rudely snake rockets different fuselage woven tagged bested dented vegan hover rapid fawns obvious muppet randomly seasons randomly" --password "" --log-file ~/testnet/wallet_01.log;

2018-01-29 18:31:23.357	  0x7fffb0acb340	ERROR	default	contrib/epee/src/wipeable_string.cpp:81	wipefunc is not set
libc++abi.dylib: terminating with uncaught exception of type std::runtime_error: wipefunc is not set
Abort trap: 6
```

The code throwing the exception is the following: 

```cpp
void wipeable_string::wipe()
{
  CHECK_AND_ASSERT_THROW_MES(wipefunc, "wipefunc is not set");
  wipefunc(buffer.data(), buffer.size() * sizeof(char));
}
```

The problem is the static member `wipefunc` of the `wipeable_string` is not shared between `libcommon.dylib` dynamically loaded lib and the `monero-wallet-cli`. Both have custom, separate copies. Also `&memwipe` is different in those two.

Wallet correctly initializes `wipeable_string` with `tools::on_startup() -> wipeable_string::set_wipe(&memwipe);` 

This works fine with static linking. The problem is `tools::on_startup()` is "inside" `libcommon.dylib` library so the common version copy of the `wipeable_string` is initialized only. The copy in the `monero-wallet-cli` is separate, still null. As a consequence, destruction of 

```cpp
epee::wipeable_string seed_pass = pwd_container->password();
``` 

from `simplewallet.cpp` causes the crash as the `wipefunc` is still null from this perspective.

I tried to fix this problem with `-fvisibility`, `__attribute__ ((visibility ("default")))`, `-rdynamic` but without success (it would require more clean & build experiments I have time to play with it). 

For now, I am using static linkage also in the debug mode, which works fine. 

```bash
mkdir -p build/debug && cd build/debug
cmake -D CMAKE_BUILD_TYPE=Debug -D BUILD_SHARED_LIBS=OFF ../..
make
```

Env: Mac 10.13.3
Master at: ed67e5c001d50a2eea5fa24dfc58eba0921d525b

Related resources:
- https://stackoverflow.com/questions/8623657/multiple-instances-of-singleton-across-shared-libraries-on-linux
- http://thinkingeek.com/2012/08/08/common-linking-issues-c/



# Discussion History
## moneromooo-monero | 2018-01-30T09:22:08+00:00
Sounds like a linker bug, no ?

## moneromooo-monero | 2018-01-31T12:25:00+00:00
In fact, the reason for the function pointer (memwipe being in src, wipeable_string in contrib) has now gone, so I'll remove it and call memwipe directly.

## moneromooo-monero | 2018-01-31T12:27:33+00:00
https://github.com/monero-project/monero/pull/3217

## ph4r05 | 2018-01-31T12:59:05+00:00
Ok great! Thanks!

# Action History
- Created by: ph4r05 | 2018-01-29T18:50:18+00:00
- Closed at: 2018-01-31T12:59:24+00:00
