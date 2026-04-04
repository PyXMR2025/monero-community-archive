---
title: 'Trezor: passphrase entry on computer crashes monero app on linux'
source_url: https://github.com/monero-project/monero/issues/7778
author: ph4r05
assignees: []
labels: []
created_at: '2021-07-09T10:37:40+00:00'
updated_at: '2021-08-12T07:44:08+00:00'
type: issue
status: closed
closed_at: '2021-08-12T07:44:08+00:00'
---

# Original Description
v0.17.2.2 fails when passphrase is entered on the computer (creating wallet from Trezor T wallet, with passphrase)
Crashes on linux, OSX is not affected, AFAIK.

monero-gui:
```
Thread 6 "Thread (pooled)" received signal SIGABRT, Aborted.
[Switching to Thread 0x7fffe7fff700 (LWP 3613)]
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7635859 in __GI_abort () at abort.c:79
#2  0x00007ffff76a03ee in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff77ca285 "%s\n")
    at ../sysdeps/posix/libc_fatal.c:155
#3  0x00007ffff76a847c in malloc_printerr (str=str@entry=0x7ffff77cc670 "double free or corruption (out)") at malloc.c:5347
#4  0x00007ffff76aa120 in _int_free (av=0x7ffff77fbb80 <main_arena>, p=0x7fffd80405f0, have_lock=<optimized out>) at malloc.c:4314
#5  0x00005555577758db in hw::trezor::messages::common::PassphraseAck::~PassphraseAck() ()
#6  0x00005555577d64c9 in hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, hw::trezor::messages::common::PassphraseRequest const*) ()
#7  0x00005555577d6f90 in hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&) ()
#8  0x000055555776e03b in std::shared_ptr<hw::trezor::messages::monero::MoneroAddress> hw::trezor::device_trezor_base::client_exchange<hw::trezor::messages::monero::MoneroAddress>(std::shared_ptr<google::protobuf::Message const> const&, boost::optional<hw::trezor::messages::MessageType> const&, boost::optional<std::vector<hw::trezor::messages::MessageType, std::allocator<hw::trezor::messages::MessageType> > > const&, boost::optional<hw::trezor::messages::MessageType*> const&, bool) ()
#9  0x000055555775cece in hw::trezor::device_trezor::get_address(boost::optional<cryptonote::subaddress_index> const&, boost::optional<crypto::hash8> const&, bool, boost::optional<std::vector<unsigned int, std::allocator<unsigned int> > > const&, boost::optional<cryptonote::network_type> const&) ()
#10 0x000055555775d4f2 in hw::trezor::device_trezor::get_public_address(cryptonote::account_public_address&) ()
#11 0x0000555557a85462 in cryptonote::account_base::create_from_device(hw::device&) ()
#12 0x0000555557607d32 in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) ()
#13 0x0000555555a7dd81 in Monero::WalletImpl::recoverFromDevice(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&) ()
#14 0x0000555555aa55c8 in Monero::WalletManagerImpl::createWalletFromDevice(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, Monero::NetworkType, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, unsigned long, Monero::WalletListener*) ()
#15 0x0000555555a0bbf8 in WalletManager::createWalletFromDevice(QString const&, QString const&, NetworkType::Type, QString const&, unsigned long long, QString const&, unsigned long long) ()
#16 0x0000555555a0c118 in std::_Function_handler<void (), WalletManager::createWalletFromDeviceAsync(QString const&, QString const&, NetworkType::Type, QString const&, unsigned long long, QString const&, unsigned long long)::{lambda()#1}>::_M_invoke(std::_Any_data const&) ()
#17 0x0000555555a2eb27 in QtConcurrent::RunFunctionTask<void>::run() ()
#18 0x0000555556cce58a in QThreadPoolThread::run() ()
#19 0x0000555556cc8ae8 in QThreadPrivate::start(void*) ()
#20 0x00007ffff7f92609 in start_thread (arg=<optimized out>) at pthread_create.c:477
#21 0x00007ffff7732293 in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:95
(gdb) 
```

On monero-wallet-cli:
```
Thread 1 "monero-wallet-c" received signal SIGABRT, Aborted.
__GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
50	../sysdeps/unix/sysv/linux/raise.c: No such file or directory.
(gdb) bt
#0  __GI_raise (sig=sig@entry=6) at ../sysdeps/unix/sysv/linux/raise.c:50
#1  0x00007ffff7c78859 in __GI_abort () at abort.c:79
#2  0x00007ffff7ce33ee in __libc_message (action=action@entry=do_abort, fmt=fmt@entry=0x7ffff7e0d285 "%s\n") at ../sysdeps/posix/libc_fatal.c:155
#3  0x00007ffff7ceb47c in malloc_printerr (str=str@entry=0x7ffff7e0f670 "double free or corruption (out)") at malloc.c:5347
#4  0x00007ffff7ced120 in _int_free (av=0x7ffff7e3eb80 <main_arena>, p=0x5555572b22f0, have_lock=<optimized out>) at malloc.c:4314
#5  0x000055555613581d in hw::trezor::messages::common::PassphraseAck::SharedDtor() ()
#6  0x0000555556135877 in hw::trezor::messages::common::PassphraseAck::~PassphraseAck() ()
#7  0x00005555561af392 in hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, hw::trezor::messages::common::PassphraseRequest const*) ()
#8  0x00005555561aff91 in hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&) ()
#9  0x000055555612ba23 in std::shared_ptr<hw::trezor::messages::monero::MoneroAddress> hw::trezor::device_trezor_base::client_exchange<hw::trezor::messages::monero::MoneroAddress>(std::shared_ptr<google::protobuf::Message const> const&, boost::optional<hw::trezor::messages::MessageType> const&, boost::optional<std::vector<hw::trezor::messages::MessageType, std::allocator<hw::trezor::messages::MessageType> > > const&, boost::optional<hw::trezor::messages::MessageType*> const&, bool) ()
#10 0x000055555611c8fe in hw::trezor::device_trezor::get_address(boost::optional<cryptonote::subaddress_index> const&, boost::optional<crypto::hash8> const&, bool, boost::optional<std::vector<unsigned int, std::allocator<unsigned int> > > const&, boost::optional<cryptonote::network_type> const&) ()
#11 0x000055555611cf34 in hw::trezor::device_trezor::get_public_address(cryptonote::account_public_address&) ()
#12 0x0000555556233d29 in cryptonote::account_base::create_from_device(hw::device&) ()
#13 0x0000555555e6e3ba in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) ()
#14 0x0000555555c9bcfd in cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&) ()
#15 0x0000555555cf5ff9 in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) ()
#16 0x0000555555c7c8ed in main ()
```

OSX works on current master 9c18f2767bc62796eacb0428ac50abf8fc5c14dd, trying to replicate on Linux.

The bug was found by @andrewkozlik in https://github.com/trezor/trezor-firmware/issues/1686 

# Discussion History
## ph4r05 | 2021-07-09T13:34:28+00:00
Ubuntu 20.04.1 - monero-wallet-cli crashes on passphrase entry on computer with (entry on Trezor works)

```
Enter device passphrase: 
=================================================================
==2537==ERROR: AddressSanitizer: attempting free on address which was not malloc()-ed: 0x6030000c7200 in thread T0
    #0 0x7efd5be058df in operator delete(void*) (/lib/x86_64-linux-gnu/libasan.so.5+0x1108df)
    #1 0x562644c8297a in hw::trezor::messages::common::PassphraseAck::SharedDtor() /usr/include/c++/9/ext/new_allocator.h:128
    #2 0x562644c82a24 in hw::trezor::messages::common::PassphraseAck::~PassphraseAck() /root/monero2/src/device_trezor/trezor/messages/messages-common.pb.cc:2327
    #3 0x562644ee0040 in hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, hw::trezor::messages::common::PassphraseRequest const*) /root/monero2/src/device_trezor/device_trezor_base.cpp:496
    #4 0x562644ee16e0 in hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&) /root/monero2/src/device_trezor/device_trezor_base.cpp:295
    #5 0x562644c5a6cc in std::shared_ptr<hw::trezor::messages::monero::MoneroAddress> hw::trezor::device_trezor_base::client_exchange<hw::trezor::messages::monero::MoneroAddress>(std::shared_ptr<google::protobuf::Message const> const&, boost::optional<hw::trezor::messages::MessageType> const&, boost::optional<std::vector<hw::trezor::messages::MessageType, std::allocator<hw::trezor::messages::MessageType> > > const&, boost::optional<hw::trezor::messages::MessageType*> const&, bool) /root/monero2/src/device_trezor/device_trezor_base.hpp:179
    #6 0x562644c0feff in hw::trezor::device_trezor::get_address(boost::optional<cryptonote::subaddress_index> const&, boost::optional<crypto::hash8> const&, bool, boost::optional<std::vector<unsigned int, std::allocator<unsigned int> > > const&, boost::optional<cryptonote::network_type> const&) /root/monero2/src/device_trezor/device_trezor.cpp:240
    #7 0x562644c10b01 in hw::trezor::device_trezor::get_public_address(cryptonote::account_public_address&) /root/monero2/src/device_trezor/device_trezor.cpp:165
    #8 0x5626451480ca in cryptonote::account_base::create_from_device(hw::device&) /root/monero2/src/cryptonote_basic/account.cpp:220
    #9 0x5626441a9602 in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) /root/monero2/src/wallet/wallet2.cpp:4923
    #10 0x562643b8e8bf in cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:5091
    #11 0x562643ca9ffe in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:4586
    #12 0x562643cb4366 in main /root/monero2/src/simplewallet/simplewallet.cpp:10646
    #13 0x7efd5b9850b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)
    #14 0x562643ace1ed in _start (/home/ph4r05/Desktop/monero-wallet-cli-linux+0x4c51ed)

0x6030000c7200 is located 6 bytes to the right of 26-byte region [0x6030000c71e0,0x6030000c71fa)
freed by thread T0 here:
    #0 0x7efd5be058df in operator delete(void*) (/lib/x86_64-linux-gnu/libasan.so.5+0x1108df)
    #1 0x562643d76b29 in cryptonote::simple_wallet::tr(char const*) (/home/ph4r05/Desktop/monero-wallet-cli-linux+0x76db29)
    #2 0x562643b3fa99 in cryptonote::simple_wallet::on_device_passphrase_request(bool&) /root/monero2/src/simplewallet/simplewallet.cpp:5849
    #3 0x562643f47d8e in tools::wallet2::on_device_passphrase_request(bool&) /root/monero2/src/wallet/wallet2.cpp:14069
    #4 0x562643f47e9a in tools::wallet_device_callback::on_passphrase_request(bool&) /root/monero2/src/wallet/wallet2.cpp:1124
    #5 0x562644edf613 in hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, hw::trezor::messages::common::PassphraseRequest const*) /root/monero2/src/device_trezor/device_trezor_base.cpp:494
    #6 0x562644ee16e0 in hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&) /root/monero2/src/device_trezor/device_trezor_base.cpp:295
    #7 0x562644c5a6cc in std::shared_ptr<hw::trezor::messages::monero::MoneroAddress> hw::trezor::device_trezor_base::client_exchange<hw::trezor::messages::monero::MoneroAddress>(std::shared_ptr<google::protobuf::Message const> const&, boost::optional<hw::trezor::messages::MessageType> const&, boost::optional<std::vector<hw::trezor::messages::MessageType, std::allocator<hw::trezor::messages::MessageType> > > const&, boost::optional<hw::trezor::messages::MessageType*> const&, bool) /root/monero2/src/device_trezor/device_trezor_base.hpp:179
    #8 0x562644c0feff in hw::trezor::device_trezor::get_address(boost::optional<cryptonote::subaddress_index> const&, boost::optional<crypto::hash8> const&, bool, boost::optional<std::vector<unsigned int, std::allocator<unsigned int> > > const&, boost::optional<cryptonote::network_type> const&) /root/monero2/src/device_trezor/device_trezor.cpp:240
    #9 0x562644c10b01 in hw::trezor::device_trezor::get_public_address(cryptonote::account_public_address&) /root/monero2/src/device_trezor/device_trezor.cpp:165
    #10 0x5626451480ca in cryptonote::account_base::create_from_device(hw::device&) /root/monero2/src/cryptonote_basic/account.cpp:220
    #11 0x5626441a9602 in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) /root/monero2/src/wallet/wallet2.cpp:4923
    #12 0x562643b8e8bf in cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:5091
    #13 0x562643ca9ffe in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:4586
    #14 0x562643cb4366 in main /root/monero2/src/simplewallet/simplewallet.cpp:10646
    #15 0x7efd5b9850b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)

previously allocated by thread T0 here:
    #0 0x7efd5be04947 in operator new(unsigned long) (/lib/x86_64-linux-gnu/libasan.so.5+0x10f947)
    #1 0x562643d7636a in void std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::_M_construct<char const*>(char const*, char const*, std::forward_iterator_tag) /usr/include/c++/9/bits/basic_string.tcc:219
    #2 0x562643d76ab1 in cryptonote::simple_wallet::tr(char const*) (/home/ph4r05/Desktop/monero-wallet-cli-linux+0x76dab1)
    #3 0x562643b3fa99 in cryptonote::simple_wallet::on_device_passphrase_request(bool&) /root/monero2/src/simplewallet/simplewallet.cpp:5849
    #4 0x562643f47d8e in tools::wallet2::on_device_passphrase_request(bool&) /root/monero2/src/wallet/wallet2.cpp:14069
    #5 0x562643f47e9a in tools::wallet_device_callback::on_passphrase_request(bool&) /root/monero2/src/wallet/wallet2.cpp:1124
    #6 0x562644edf613 in hw::trezor::device_trezor_base::on_passphrase_request(hw::trezor::GenericMessage&, hw::trezor::messages::common::PassphraseRequest const*) /root/monero2/src/device_trezor/device_trezor_base.cpp:494
    #7 0x562644ee16e0 in hw::trezor::device_trezor_base::message_handler(hw::trezor::GenericMessage&) /root/monero2/src/device_trezor/device_trezor_base.cpp:295
    #8 0x562644c5a6cc in std::shared_ptr<hw::trezor::messages::monero::MoneroAddress> hw::trezor::device_trezor_base::client_exchange<hw::trezor::messages::monero::MoneroAddress>(std::shared_ptr<google::protobuf::Message const> const&, boost::optional<hw::trezor::messages::MessageType> const&, boost::optional<std::vector<hw::trezor::messages::MessageType, std::allocator<hw::trezor::messages::MessageType> > > const&, boost::optional<hw::trezor::messages::MessageType*> const&, bool) /root/monero2/src/device_trezor/device_trezor_base.hpp:179
    #9 0x562644c0feff in hw::trezor::device_trezor::get_address(boost::optional<cryptonote::subaddress_index> const&, boost::optional<crypto::hash8> const&, bool, boost::optional<std::vector<unsigned int, std::allocator<unsigned int> > > const&, boost::optional<cryptonote::network_type> const&) /root/monero2/src/device_trezor/device_trezor.cpp:240
    #10 0x562644c10b01 in hw::trezor::device_trezor::get_public_address(cryptonote::account_public_address&) /root/monero2/src/device_trezor/device_trezor.cpp:165
    #11 0x5626451480ca in cryptonote::account_base::create_from_device(hw::device&) /root/monero2/src/cryptonote_basic/account.cpp:220
    #12 0x5626441a9602 in tools::wallet2::restore(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, epee::wipeable_string const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool) /root/monero2/src/wallet/wallet2.cpp:4923
    #13 0x562643b8e8bf in cryptonote::simple_wallet::new_wallet(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:5091
    #14 0x562643ca9ffe in cryptonote::simple_wallet::init(boost::program_options::variables_map const&) /root/monero2/src/simplewallet/simplewallet.cpp:4586
    #15 0x562643cb4366 in main /root/monero2/src/simplewallet/simplewallet.cpp:10646
    #16 0x7efd5b9850b2 in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x270b2)

SUMMARY: AddressSanitizer: bad-free (/lib/x86_64-linux-gnu/libasan.so.5+0x1108df) in operator delete(void*)
==2537==ABORTING
```

## ph4r05 | 2021-07-09T13:48:03+00:00
Interesting, reverting commit 34f942867f86ad3467cb168a19a0b38ad703f8df fixes the problem = no crash @selsta 

If I remove the wiping, also the current master works without crash
https://github.com/monero-project/monero/blob/34f942867f86ad3467cb168a19a0b38ad703f8df/src/device_trezor/device_trezor_base.cpp#L511-L514 Passphrase is correctly transferred to the Trezor (displayed on the screen).

Wiping also works if I assign newly allocated string to a local variable - no idea why.

```diff
-          m.set_allocated_passphrase(new std::string(passphrase->data(), passphrase->size()));
+          auto strr = new std::string(passphrase->data(), passphrase->size());
+          m.set_allocated_passphrase(strr);
```

Alternatively, if I change only one line - I add logging before wiping the string, it works as well 

```
MWARNING(std::string("wiping passphrase ") << &(m.mutable_passphrase())[0] << " size: " << m.mutable_passphrase()->size());
```

So it might be something with compiler optimizations and undefined behaviour of wiping strings buffer? No idea. 

UPDATE:
- passphrases `a{1,5}` crash the monero-wallet-cli
- passphrases `a{6,}` do not crash the wallet

Env:
- CMake version 3.16.3
- Found Boost Version: 107100
`gcc -v`
```
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/9/lto-wrapper
OFFLOAD_TARGET_NAMES=nvptx-none:hsa
OFFLOAD_TARGET_DEFAULT=1
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 9.3.0-10ubuntu2' --with-bugurl=file:///usr/share/doc/gcc-9/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++,gm2 --prefix=/usr --with-gcc-major-version-only --program-suffix=-9 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib=auto --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none,hsa --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2) 
```



## ph4r05 | 2021-07-09T15:35:44+00:00
@moneromooo-monero what do you think? Should be just drop wiping passphrase std::string to avoid crashes like this? Maybe disable passphrase entry on the computer altogether?


## dEBRUYNE-1 | 2021-07-09T20:51:03+00:00
Adding for visibility purposes, might be related.

https://www.reddit.com/r/monerosupport/comments/ogz1ao/trezor_macos_setup_gui_stuck_after_passphrase/

## selsta | 2021-07-09T20:53:04+00:00
@ph4r05 will take a look, we can also put out a new release once this is fixed

## perfect-daemon | 2021-07-10T23:54:41+00:00
```diff
 src/CMakeLists.txt                       | 10 ++++++++++
 src/device_trezor/device_trezor_base.cpp |  8 ++++++++
 src/test.cpp                             | 24 ++++++++++++++++++++++++
 3 files changed, 42 insertions(+)

diff --git a/src/CMakeLists.txt b/src/CMakeLists.txt
index 07d4d58c3..8f26607d3 100644
--- a/src/CMakeLists.txt
+++ b/src/CMakeLists.txt
@@ -143,3 +143,13 @@ endif()
 
 add_subdirectory(device)
 add_subdirectory(device_trezor)
+
+add_executable(
+  test_trezor
+  test.cpp
+)
+target_link_libraries(
+  test_trezor
+  device_trezor
+  device
+)
diff --git a/src/device_trezor/device_trezor_base.cpp b/src/device_trezor/device_trezor_base.cpp
index 70dc7f539..3125eb91a 100644
--- a/src/device_trezor/device_trezor_base.cpp
+++ b/src/device_trezor/device_trezor_base.cpp
@@ -460,7 +460,9 @@ namespace trezor {
           memwipe(&(*m.mutable_pin())[0], m.mutable_pin()->size());
       });
 
+      #if 0
       resp = call_raw(&m);
+      #endif
     }
 
     void device_trezor_base::on_passphrase_request(GenericMessage & resp, const messages::common::PassphraseRequest * msg)
@@ -494,6 +496,7 @@ namespace trezor {
 
       messages::common::PassphraseAck m;
       m.set_on_device(on_device);
+      #if 0
       if (!on_device) {
         if (!passphrase && m_passphrase) {
           passphrase = m_passphrase;
@@ -504,16 +507,21 @@ namespace trezor {
         }
 
         if (passphrase) {
+      #endif
           m.set_allocated_passphrase(new std::string(passphrase->data(), passphrase->size()));
+      #if 0
         }
       }
+      #endif
 
       const auto data_cleaner = epee::misc_utils::create_scope_leave_handler([&]() {
         if (m.has_passphrase())
           memwipe(&(m.mutable_passphrase())[0], m.mutable_passphrase()->size());
       });
 
+      #if 0
       resp = call_raw(&m);
+      #endif
     }
 
     void device_trezor_base::on_passphrase_state_request(GenericMessage & resp, const messages::common::Deprecated_PassphraseStateRequest * msg)
diff --git a/src/test.cpp b/src/test.cpp
new file mode 100644
index 000000000..17bf51b08
--- /dev/null
+++ b/src/test.cpp
@@ -0,0 +1,24 @@
+#include "device_trezor/device_trezor_base.hpp"
+#include "common/password.h"
+
+int main () {
+  struct callback_t: public hw::i_device_callback {
+    void on_button_request(uint64_t code=0) override {}
+    void on_button_pressed() override {}
+    boost::optional<epee::wipeable_string> on_pin_request() override {
+      return {epee::wipeable_string{"aaa"}};
+    }
+    boost::optional<epee::wipeable_string> on_passphrase_request(bool & on_device) override {
+      return {epee::wipeable_string{"aaa"}};
+    }
+    void on_progress(const hw::device_progress& event) override {}
+  };
+  mlog_set_log("*:TRACE");
+  hw::trezor::device_trezor_base device;
+  callback_t callback;
+  device.set_callback(&callback);
+  hw::trezor::messages::common::PassphraseRequest req;
+  hw::trezor::GenericMessage resp;
+  device.on_passphrase_request(resp, &req);
+  return 0;
+};

```
isolated test to reproduce problem

## perfect-daemon | 2021-07-10T23:55:01+00:00
Thanks for useful review
Thanks for issue without reproducible test

## selsta | 2021-07-10T23:58:50+00:00
#7781

## ph4r05 | 2021-07-11T00:07:32+00:00
> Thanks for issue without reproducible test

Sure

## selsta | 2021-07-11T00:22:09+00:00
Still don't know why it worked on Mac, maybe some undefined behavior. @ph4r05 if you can confirm that #7781 / 7782 fixes the issue then I'll prepare a new release :)

## ph4r05 | 2021-07-11T00:25:02+00:00
@selsta thanks! I will let you know as I get to it, in a day or two.

## ph4r05 | 2021-07-11T14:14:34+00:00
 @selsta I've tested it both on Linux and OSX, it works, thanks!

I've tested: passphrase entry both on Trezor and computer, same addresses. Passphrases: empty, "a", "aaaaaaaaaaaaaaa".
So, LGTM.

# Action History
- Created by: ph4r05 | 2021-07-09T10:37:40+00:00
- Closed at: 2021-08-12T07:44:08+00:00
