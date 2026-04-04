---
title: aarch64/arm64-darwin stack overflow
source_url: https://github.com/monero-project/monero-gui/issues/3801
author: jla3378
assignees: []
labels: []
created_at: '2021-12-13T13:23:17+00:00'
updated_at: '2021-12-13T20:33:04+00:00'
type: issue
status: closed
closed_at: '2021-12-13T20:33:04+00:00'
---

# Original Description
Building on arm64 macOS works fine by setting `ARCH=default` or `ARCH=arm64` but running the program will result in an `EXC_BAD_ACCESS` crash. The crash notes are attached. 

Since my Apple Developer account is just about to renew, I decided to open a Technical Support Incident with apple on this and this is what I got back:


```
Exception Type:        EXC_BAD_ACCESS (SIGBUS)
Exception Codes:       KERN_PROTECTION_FAILURE at 0x000000016fa03ff8

This shows that the process died with a memory access exception trying to access the address 0x000000016fa03ff8.

VM Region Info: 0x16fa03ff8 is in 0x16fa00000-0x16fa04000; …
     …
--->  STACK GUARD 16fa00000-16fa04000 [ 16K] ---/rwx SM=NUL … for thread 7
     Stack       16fa04000-16fa8c000 [544K] rw-/rwx SM=PRV thread 7

This suggests that the thread ran out of stack space, in that the crashing address is in the guard page that’s placed immediately below the thread’s stack start

Thread 7 Crashed:: Thread (pooled)
0  libsystem_pthread.dylib … ___chkstk_darwin + 60
1  monero-wallet-gui       … cn_slow_hash + 48
2  monero-wallet-gui       … cryptonote::get_block_longhash(cryptonote::Bl…
3  monero-wallet-gui       … std::__1::__function::__func<cryptonote::gene…
4  monero-wallet-gui       … cryptonote::miner::find_nonce_for_given_block…
5  monero-wallet-gui       … cryptonote::generate_genesis_block(cryptonote…
6  monero-wallet-gui       … tools::wallet2::set_ring_database(std::__1::b…
7  monero-wallet-gui       … Monero::WalletImpl::open(std::__1::basic_stri…
8  monero-wallet-gui       … Monero::WalletManagerImpl::openWallet(std::__…
9  monero-wallet-gui       … WalletManager::openWallet(QString const&, QSt…
10 monero-wallet-gui       … std::__1::__function::__func<WalletManager::o…
11 monero-wallet-gui       … QtConcurrent::StoredFunctorCall0<void, Future…
12 monero-wallet-gui       … QtConcurrent::RunFunctionTask<void>::run() + …
13 QtCore                  … 0x104718000 + 152200
14 QtCore                  … 0x104718000 + 134800
15 libsystem_pthread.dylib … _pthread_start + 148
16 libsystem_pthread.dylib … thread_start + 8

And the backtrace of the crashed thread looks just like normal code.  There’s nothing here to suggest that it’s doing anything that would be impacted by code signing.

Moreover, frame 0 is `___chkstk_darwin`, which is a system routine that checks whether we’ve run out of stack space. You can see this code in the Darwin open source [1] [2].

<https://opensource.apple.com/source/libpthread/libpthread-454.40.3/src/pthread_asm.s.auto.html>

IMPORTANT: This file contains various flavours of assembly language.  Skip down to the Apple silicon variant denoted by `#elif defined(__arm64__)`.

If you look at the `Lcrash` label, you’ll see this comment:

	// POSIX mandates that stack overflow crashes with SIGSEGV
	// so load an address in the guard page and dereference it

which is exactly what we’re seeing here.

Share and Enjoy
--
Quinn “The Eskimo!”
Apple Developer Relations, Developer Technical Support, Core OS/Hardware

[1] The Darwin open source that corresponds to macOS 12 hasn’t been released yet, but this stuff hasn’t changed much since macOS 11.

[2] Sorry about the formatting.  If you download the file and change the extension to `.html`, it’ll render nicely.  Or download the pthread tarball from this page.

<https://opensource.apple.com/release/macos-1101.html>
```

# Discussion History
## jla3378 | 2021-12-13T13:24:13+00:00
[crash.log](https://github.com/monero-project/monero-gui/files/7704176/crash.log)


## selsta | 2021-12-13T19:59:40+00:00
Which exact commit are you compiling? What is your monero submodule set to?

When does the program crash? When opening the GUI or when opening a wallet?

## jla3378 | 2021-12-13T20:03:48+00:00
I compiled commit bddb9b0 today but it's been the same issue for the past couple months of commits.

Monero(d) on its own builds fine and has been built native for months now but the submodule is set to ab18fea.

## jla3378 | 2021-12-13T20:05:47+00:00
I have a wallet already set up so when I launch the app bundle it displays the box to input my password. Upon hitting enter is when it crashes.

## selsta | 2021-12-13T20:10:27+00:00
This fixed this issue for me so not sure why it's still broken on your system: https://github.com/monero-project/monero/commit/187633c0ca9e563129bd942488e8b6e2d16f0a3f

## jla3378 | 2021-12-13T20:32:57+00:00
Forgot to clean to build from scratch. Doh.

# Action History
- Created by: jla3378 | 2021-12-13T13:23:17+00:00
- Closed at: 2021-12-13T20:33:04+00:00
