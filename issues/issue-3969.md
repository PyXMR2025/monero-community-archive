---
title: SIGABRT on Ubuntu 17.10 when attempting to create Ledger wallet
source_url: https://github.com/monero-project/monero/issues/3969
author: jamespic
assignees: []
labels: []
created_at: '2018-06-09T10:39:45+00:00'
updated_at: '2018-06-09T22:30:50+00:00'
type: issue
status: closed
closed_at: '2018-06-09T20:00:45+00:00'
---

# Original Description
When running `monero-wallet-cli --generate-from-device ~/Monero/wallets/ledger`, the wallet cli process crashes with SIGABRT. The symptoms are the same whether using the official builds or debug builds. `gdb` gives the following stack trace for debug builds:

```
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:51
#1  0x00007fd5d637df5d in __GI_abort () at abort.c:90
#2  0x00007fd5d63c628d in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7fd5d64ed528 "*** Error in `%s': %s: 0x%s ***\n") at ../sysdeps/posix/libc_fatal.c:181
#3  0x00007fd5d63cd64a in malloc_printerr (action=<optimised out>, str=0x7fd5d64e9e7c "free(): invalid size", ptr=<optimised out>, ar_ptr=<optimised out>) at malloc.c:5426
#4  0x00007fd5d63cf73e in _int_free (av=0x7fd5d671fc20 <main_arena>, p=<optimised out>, have_lock=0) at malloc.c:4175
#5  0x00007fd5d63d444e in __GI___libc_free (mem=mem@entry=0x7ffc608b6dd0) at malloc.c:3145
#6  0x00007fd5d39fb4da in SCardFreeMemory (hContext=<optimised out>, pvMem=0x7ffc608b6dd0) at winscard_clnt.c:2959
#7  0x00007fd5d5352716 in hw::ledger::device_ledger::connect (this=0x55c78d1a6a00) at /home/james/temp-source/monero/src/device/device_ledger.cpp:410
#8  0x00007fd5d85064c4 in cryptonote::account_base::create_from_device (this=this@entry=0x55c78d1a54e8, device_name="Ledger")
    at /home/james/temp-source/monero/src/cryptonote_basic/account.cpp:140
#9  0x00007fd5d9adc1b8 in tools::wallet2::restore (this=0x55c78d1a54e0, wallet_="/home/james/Monero/wallets/ledger", password=..., device_name="Ledger")
    at /home/james/temp-source/monero/src/wallet/wallet2.cpp:3246
#10 0x000055c78b433585 in cryptonote::simple_wallet::new_wallet (this=0x7ffc608b7f60, vm=..., device_name="Ledger")
    at /home/james/temp-source/monero/src/simplewallet/simplewallet.cpp:3420
#11 0x000055c78b4454ec in cryptonote::simple_wallet::init (this=0x7ffc608b7f60, vm=...) at /home/james/temp-source/monero/src/simplewallet/simplewallet.cpp:2989
#12 0x000055c78b4478e8 in main (argc=3, argv=0x7ffc608b8508) at /home/james/temp-source/monero/src/simplewallet/simplewallet.cpp:7524
```

I've got version 1.8.22-1ubuntu1 of libpcsclite1 and libpcsclite-dev installed, and `pcscd` is active. Happy to provide core dumps or other debugging data.

# Discussion History
## moneromooo-monero | 2018-06-09T10:46:10+00:00
Can you give the exact commit you're running ?

Also, please build with this patch and tell me which message it's printing when building:

```
diff --git a/src/device/device_ledger.cpp b/src/device/device_ledger.cpp
index 3b9ab67..d917a31 100644
--- a/src/device/device_ledger.cpp
+++ b/src/device/device_ledger.cpp
@@ -357,9 +357,11 @@ namespace hw {
 
       this->disconnect();
 #ifdef SCARD_AUTOALLOCATE
+#warning SCARD_AUTOALLOCATE defined
       dwReaders = SCARD_AUTOALLOCATE;
       rv = SCardListReaders(this->hContext, NULL, (LPSTR)&mszReaders, &dwReaders);
 #else
+#warning SCARD_AUTOALLOCATE undefined
       dwReaders = 0;
       rv = SCardListReaders(this->hContext, NULL, NULL, &dwReaders);
       if (rv != SCARD_S_SUCCESS)

```

## jamespic | 2018-06-09T10:48:45+00:00
I'm using e2c39f6b59fcf5c623c814dfefc518ab0b7eca32 - the `v0.12.2.0` tag. I'll patch that in and get back to you.

## moneromooo-monero | 2018-06-09T10:52:42+00:00
Also, can you see if you can work out the value of SCARD_AUTOALLOCATE in the pcsc headers, if it's defined ?

## jamespic | 2018-06-09T10:57:56+00:00
I'm getting `#warning SCARD_AUTOALLOCATE defined` on build, and I found `#define SCARD_AUTOALLOCATE (DWORD)(-1)` in `/usr/include/PCSC/pcsclite.h`

## moneromooo-monero | 2018-06-09T11:05:55+00:00
Can you run with valgrind (just add "valgrind " in front of the command line), and add --log-level 1,device\*:DEBUG to the end of the command line.

## stoffu | 2018-06-09T11:10:31+00:00
Isn’t it necessary to add :DEBUG to the end? --log-lovel 1,device*:DEBUG

## moneromooo-monero | 2018-06-09T11:11:53+00:00
Yes.

## jamespic | 2018-06-09T19:41:10+00:00
Here's the output from Valgrind:

```
==12019== Memcheck, a memory error detector
==12019== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==12019== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==12019== Command: build/debug/bin/monero-wallet-cli --generate-from-device /home/james/Monero/wallets/ledger --log-level 1,device*:DEBUG
==12019== 
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on an another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

Monero 'Lithium Luna' (v0.12.2.0-release)
Logging to build/debug/bin/monero-wallet-cli.log
Enter a new password for the wallet: 
Confirm password: 
==12019== Warning: set address range perms: large range [0xeeb5000, 0x4e7b5000) (defined)
==12019== Conditional jump or move depends on uninitialised value(s)
==12019==    at 0x98D1708: hw::ledger::device_ledger::connect() (device_ledger.cpp:408)
==12019==    by 0x66CB4C3: cryptonote::account_base::create_from_device(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (account.cpp:140)
==12019==    by 0x519D1B7: tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (wallet2.cpp:3246)
==12019==    by 0x285584: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (simplewallet.cpp:3420)
==12019==    by 0x2974EB: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:2989)
==12019==    by 0x2998E7: main (simplewallet.cpp:7524)
==12019== 
==12019== Conditional jump or move depends on uninitialised value(s)
==12019==    at 0x4C30CF1: free (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==12019==    by 0xB21A4D9: SCardFreeMemory (winscard_clnt.c:2959)
==12019==    by 0x98D1715: hw::ledger::device_ledger::connect() (device_ledger.cpp:410)
==12019==    by 0x66CB4C3: cryptonote::account_base::create_from_device(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (account.cpp:140)
==12019==    by 0x519D1B7: tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (wallet2.cpp:3246)
==12019==    by 0x285584: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (simplewallet.cpp:3420)
==12019==    by 0x2974EB: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:2989)
==12019==    by 0x2998E7: main (simplewallet.cpp:7524)
==12019== 
==12019== Invalid free() / delete / delete[] / realloc()
==12019==    at 0x4C30D3B: free (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==12019==    by 0xB21A4D9: SCardFreeMemory (winscard_clnt.c:2959)
==12019==    by 0x98D1715: hw::ledger::device_ledger::connect() (device_ledger.cpp:410)
==12019==    by 0x66CB4C3: cryptonote::account_base::create_from_device(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (account.cpp:140)
==12019==    by 0x519D1B7: tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (wallet2.cpp:3246)
==12019==    by 0x285584: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (simplewallet.cpp:3420)
==12019==    by 0x2974EB: cryptonote::simple_wallet::init(boost::program_options::variables_map const&) (simplewallet.cpp:2989)
==12019==    by 0x2998E7: main (simplewallet.cpp:7524)
==12019==  Address 0xda78660 is 224 bytes inside a block of size 712 alloc'd
==12019==    at 0x4C3017F: operator new(unsigned long) (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==12019==    by 0x7CECDEB: el::base::RegisteredLoggers::get(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) (easylogging++.cc:1845)
==12019==    by 0x7CF157C: el::base::Writer::initializeLogger(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, bool) (easylogging++.cc:2550)
==12019==    by 0x7CF1425: el::base::Writer::construct(int, char const*, ...) (easylogging++.cc:2542)
==12019==    by 0x98D2E1B: hw::ledger::device_ledger::device_ledger() (device_ledger.cpp:223)
==12019==    by 0x98D3074: hw::ledger::register_all(std::map<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::unique_ptr<hw::device, std::default_delete<hw::device> >, std::less<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::pair<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const, std::unique_ptr<hw::device, std::default_delete<hw::device> > > > >&) (device_ledger.cpp:1987)
==12019==    by 0x98C3259: s_devices (device.cpp:50)
==12019==    by 0x98C3259: hw::get_device(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >) (device.cpp:55)
==12019==    by 0x66CB852: account_keys (account.h:46)
==12019==    by 0x66CB852: cryptonote::account_base::account_base() (account.cpp:65)
==12019==    by 0x51478DB: tools::wallet2::wallet2(cryptonote::network_type, bool) (wallet2.cpp:682)
==12019==    by 0x51499B8: (anonymous namespace)::make_basic(boost::program_options::variables_map const&, (anonymous namespace)::options const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&) (wallet2.cpp:229)
==12019==    by 0x514AA35: tools::wallet2::make_new(boost::program_options::variables_map const&, std::function<boost::optional<tools::password_container> (char const*, bool)> const&) (wallet2.cpp:746)
==12019==    by 0x2854F2: cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) (simplewallet.cpp:3401)
==12019== 
Error: failed to generate new wallet: Fail SCard API : (2148532270) Cannot find a smart card reader. Device=0, hCard=0, hContext=568453152
==12019== Warning: set address range perms: large range [0xeeb5000, 0x4e7b5000) (noaccess)
==12019== 
==12019== HEAP SUMMARY:
==12019==     in use at exit: 2,227,429 bytes in 196 blocks
==12019==   total heap usage: 12,840 allocs, 12,645 frees, 7,569,036 bytes allocated
==12019== 
==12019== LEAK SUMMARY:
==12019==    definitely lost: 0 bytes in 0 blocks
==12019==    indirectly lost: 0 bytes in 0 blocks
==12019==      possibly lost: 0 bytes in 0 blocks
==12019==    still reachable: 2,227,429 bytes in 196 blocks
==12019==         suppressed: 0 bytes in 0 blocks
==12019== Rerun with --leak-check=full to see details of leaked memory
==12019== 
==12019== For counts of detected and suppressed errors, rerun with: -v
==12019== Use --track-origins=yes to see where uninitialised values come from
==12019== ERROR SUMMARY: 3 errors from 3 contexts (suppressed: 0 from 0)
```

Weirdly, whilst it seems to have spotted the illegal free, it nonetheless continued, and failed because it couldn't find the device, but that's probably another issue.

EDIT: The issue with not finding the device is probably due to the version of `libccid` in 17.10 - it's 1.4.27, and Ledger Nano S support wasn't added until 1.4.28.

## moneromooo-monero | 2018-06-09T19:51:56+00:00
https://github.com/monero-project/monero/pull/3976 should fix it.


## moneromooo-monero | 2018-06-09T19:57:47+00:00
Perfect, please keep that old version till we're sure it works fine with it :D

## jamespic | 2018-06-09T20:00:45+00:00
Yep, the fix works. It now fails with `Error: failed to generate new wallet: Fail SCard API : (2148532270) Cannot find a smart card reader. Device=0, hCard=0, hContext=87565787` - which is what we expect with that version of `libccid`.

## iDunk5400 | 2018-06-09T20:31:30+00:00
[User manual](https://github.com/LedgerHQ/blue-app-monero/blob/master/doc/user/bolos-app-monero.pdf), section 3.2.1. I haven't tried it on 17.10, but it works fine on 16.04.

## jamespic | 2018-06-09T22:30:50+00:00
@iDunk5400 Man, that really needs to be in the readme, not buried in a PDF in the repo

# Action History
- Created by: jamespic | 2018-06-09T10:39:45+00:00
- Closed at: 2018-06-09T20:00:45+00:00
