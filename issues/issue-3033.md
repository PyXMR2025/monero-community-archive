---
title: Segmentation fault, fast_refresh, Index out of bounds of hashchain
source_url: https://github.com/monero-project/monero/issues/3033
author: zsilencer
assignees: []
labels: []
created_at: '2017-12-30T09:41:16+00:00'
updated_at: '2018-03-26T22:15:43+00:00'
type: issue
status: closed
closed_at: '2018-01-12T16:34:27+00:00'
---

# Original Description
Running latest master branch Monero 'Helium Hydra' (v0.11.1.0-master-a0a8706)

Tried running monero-wallet-rpc on testnet after creating new wallet, receive Segmentation Fault. 
```Thread 1 "monero-wallet-r" received signal SIGSEGV, Segmentation fault.
__memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1526
1526    ../sysdeps/x86_64/multiarch/memcmp-sse4.S: No such file or directory.
(gdb) bt
#0  __memcmp_sse4_1 () at ../sysdeps/x86_64/multiarch/memcmp-sse4.S:1526
#1  0x00000000007c1c95 in tools::wallet2::fast_refresh(unsigned long, unsigned long&, std::__cxx11::list<crypto::hash, std::allocator<crypto::hash> >&) ()
#2  0x00000000007da4f4 in tools::wallet2::refresh(unsigned long, unsigned long&, bool&) ()
#3  0x00000000007db6a3 in tools::wallet2::refresh() ()
#4  0x000000000067ab1b in main ()
```
Running the debug version still gives Segmentation fault but gdb will show this instead of crashing:
```ERROR wallet.wallet2  src/wallet/wallet2.cpp:1569     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
WARN    net.http        src/wallet/wallet_errors.h:773  /home/johnny/monero/src/wallet/wallet2.cpp:1569:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1569     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
WARN    net.http        src/wallet/wallet_errors.h:773  /home/johnny/monero/src/wallet/wallet2.cpp:1569:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1569     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
WARN    net.http        src/wallet/wallet_errors.h:773  /home/johnny/monero/src/wallet/wallet2.cpp:1569:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1569     !m_blockchain.is_in_bounds(current_index). THROW EXCEPTION: error::wallet_internal_error
WARN    net.http        src/wallet/wallet_errors.h:773  /home/johnny/monero/src/wallet/wallet2.cpp:1569:N5tools5error21wallet_internal_errorE: Index out of bounds of hashchain
ERROR   wallet.wallet2  src/wallet/wallet2.cpp:2150     pull_blocks failed, try_count=3
ERROR   wallet.rpc      src/wallet/wallet_rpc_server.cpp:3057   Wallet initialization failed: Index out of bounds of hashchain
```
System is Ubuntu 16.04.3 LTS x86_64

# Discussion History
## moneromooo-monero | 2017-12-30T10:55:50+00:00
The crash is fixed by https://github.com/monero-project/monero/pull/3002, but please give all relevant info how to recreate this. Exact commands you did, whether the daemon was running or not, whether synced or not, etc.

## zsilencer | 2018-01-01T02:42:58+00:00
Confirmed #3002 fixed crash, though monerod still crashed a few times during syncing when the db needed resized.

To reproduce, start monerod --testnet, then monero-wallet-rpc --testnet --rpc-bind-port=... etc. while not synced.

## moneromooo-monero | 2018-01-01T11:29:28+00:00
The crash on resize is fixed by https://github.com/monero-project/monero/pull/3019.

Can you please give ALL relevant info how to recreate this. Believe it or not, it's not crashing/breaking here when I run moenro-wallet-rpc on testnet with a monerod that's not synced, and this is why I asked "Exact commands you did, whether the daemon was running or not, whether synced or not, etc". Give versions, current daemon synced height, whether connected to the network or not, what height the wallet was synced in the first place, etc.

In fact, better: since this is testnet, could you share your wallet cache and keys somewhere I can download it (no javascript please) ?

One easy way is to base64 them and paste them on paste.debian.net.


## zsilencer | 2018-01-01T21:19:41+00:00
```
git clone https://github.com/monero-project/monero.git
cd monero
git reset --hard a0a8706946c0c7b9112678ffefa3354a04f7a020
git pull
make
cd build/release/bin
./monero-wallet-cli --testnet
<create wallet>
screen -dmS xmrd ./monerod --testnet
./monero-wallet-rpc --testnet --wallet-file=wallet --prompt-for-password --rpc-bind-port=12345
```
```
https://transfer.sh/EhOMO/wallet.tar.gz
password: 123
```
I'm not sure the exact height the daemon was at when I opened the wallet rpc (doesn't seem to matter) but it was connected and syncing, starting from 0.  Wallet was not synced.

## moneromooo-monero | 2018-01-03T10:31:54+00:00
Thanks for the files, I'll get to this soon, I'm a bit stuck in other stuff right now.

## moneromooo-monero | 2018-01-03T14:41:44+00:00
Are you sure the password is 123 ? I get an invalid password error here with this.

## zsilencer | 2018-01-03T20:55:20+00:00
Yeah I'm positive, I just downloaded the tar.gz from there and tried it myself again.

## moneromooo-monero | 2018-01-03T23:18:31+00:00
OK, this is using a chacha20 wallet cache, I was testing on a test VM without the latest code for this. I can get it now :)

## moneromooo-monero | 2018-01-04T12:36:34+00:00
That seems to be expected. The daemon is partly synced, so doesn't know the hashes the wallet claims near the top, so starts sending hashes from earlier, and the wallet has already dumped them. So you need to wait till the daemon's synced to at least where the wallet is before the wallet can sync some more.

## zsilencer | 2018-01-12T16:34:27+00:00
Closing. #3002 and #3019 fix these crashes.

## lunarthegrey | 2018-03-01T18:09:34+00:00
Doesn't look like a new binary has been released, thus anyone running the compiled binary is still going to run into this. Any word on when a binary with this fix in it will be released? Running on v0.11.1.0.

## arnuschky | 2018-03-26T22:15:43+00:00
Still seeing this on 0.12.0.0

# Action History
- Created by: zsilencer | 2017-12-30T09:41:16+00:00
- Closed at: 2018-01-12T16:34:27+00:00
