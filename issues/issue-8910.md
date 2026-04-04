---
title: Alpine aarch64 doesn't recognize the aarch64 binary of Monero
source_url: https://github.com/monero-project/monero/issues/8910
author: and0x00
assignees: []
labels: []
created_at: '2023-06-18T01:21:33+00:00'
updated_at: '2023-06-18T19:39:36+00:00'
type: issue
status: closed
closed_at: '2023-06-18T19:39:36+00:00'
---

# Original Description
Hello Monero development team, I'm having an issue when trying to use monero-cli in the latest version of Alpine. Wasn't it supposed to work? (If there were support :)

Packages installed
```
bash
libgcc
libstdc++
libunwind
libunwind-dev
libssl1.1
libzmq
libsodium
openssl
zeromq
unbound
libsodium
libunwind
xz
readline
expat
gtest
ccache
doxygen
graphviz
qt5-qttools
hidapi
libusb
protobuf
```

```
  ~ # uname -m
  aarch64

  ~ # curl -L https://downloads.getmonero.org/cli/linuxarm8 -o monero.tar.bz2 \
  >     && tar -xvjf monero.tar.bz2 \
  >     && rm monero.tar.bz2
    % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                   Dload  Upload   Total   Spent    Left  Speed
  100   169    0   169    0     0    144      0 --:--:--  0:00:01 --:--:--   144
  100   145    0   145    0     0    121      0 --:--:--  0:00:01 --:--:--   121
  100 63.5M  100 63.5M    0     0  5111k      0  0:00:12  0:00:12 --:--:-- 5594k
  monero-aarch64-linux-gnu-v0.18.2.2/
  monero-aarch64-linux-gnu-v0.18.2.2/ANONYMITY_NETWORKS.md
  monero-aarch64-linux-gnu-v0.18.2.2/LICENSE
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-ancestry
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-depth
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-export
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-import
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-mark-spent-outputs
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-prune
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-prune-known-spent-data
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-stats
  monero-aarch64-linux-gnu-v0.18.2.2/monero-blockchain-usage
  monero-aarch64-linux-gnu-v0.18.2.2/monerod
  monero-aarch64-linux-gnu-v0.18.2.2/monero-gen-ssl-cert
  monero-aarch64-linux-gnu-v0.18.2.2/monero-gen-trusted-multisig
  monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli
  monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-rpc
  monero-aarch64-linux-gnu-v0.18.2.2/README.md

  ~ # ls
  monero-aarch64-linux-gnu-v0.18.2.2

  ~ # ./monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli 
  /bin/sh: ./monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli: not found

  ~ # chmod +x monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli

  ~ # ./monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli 
  /bin/sh: ./monero-aarch64-linux-gnu-v0.18.2.2/monero-wallet-cli: not found

  ~ # uname -a
  Linux f4d9a046a51e 5.15.49-linuxkit #1 SMP PREEMPT Tue Sep 13 07:51:32 UTC 2022 aarch64 Linux
```

# Discussion History
## MrCyjaneK | 2023-06-18T08:45:47+00:00
I have a weird feeling that it may be due to musl libc implementation, try doing `apk add gcompat` (or follow https://wiki.alpinelinux.org/wiki/Running_glibc_programs).

## and0x00 | 2023-06-18T12:18:35+00:00
> I have a weird feeling that it may be due to musl libc implementation, try doing `apk add gcompat` (or follow https://wiki.alpinelinux.org/wiki/Running_glibc_programs).

Thanks. Would you know all the necessary dependencies on Alpine Linux? It seems that Monero does not have support for Alpine, but I wanted to try to make it run on it in docker container.

```
/ # ./monero/monero-wallet-cli 
terminate called after throwing an instance of 'std::system_error'
  what():  No error information
Aborted
```

Updated error!

## MrCyjaneK | 2023-06-18T13:28:17+00:00
well I know that alpine is pretty much different on all levels - you may want to compile it from scratch on alpine, or use debian - which is also pretty lightweight (considering that you are working with something that weights more than 100GB when fully synced 30mb here or there doesn't really matter - and you will have much better and battle tested compatibility).

Or - you may want to try using the `scratch` image to just drop all binaries.

These are just blind guesses based on my previous work with monero in docker.

# Action History
- Created by: and0x00 | 2023-06-18T01:21:33+00:00
- Closed at: 2023-06-18T19:39:36+00:00
