---
title: mac, release build master, monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/3287
author: jtgrassie
assignees: []
labels: []
created_at: '2018-02-18T07:02:14+00:00'
updated_at: '2018-02-21T18:08:44+00:00'
type: issue
status: closed
closed_at: '2018-02-21T18:08:44+00:00'
---

# Original Description
When running monero-wallet-cli, program crashes with following error: 
```
Wallet and key files found, loading...
Error: memset_s failed
```
Unfortunately I couldn't debug further due to a separate issue #3286 

# Discussion History
## stoffu | 2018-02-18T07:24:37+00:00
I see the same problem also on Mac, which seems to have started after the merge of #3195. You can for now get around this by disabling the `#ifdef HAVE_MEMSET_S` section in epee/src/memwipe.c which is certainly not the real solution. I'm not sure why `memset_s` is failing for me...


## jtgrassie | 2018-02-18T07:31:04+00:00
@stoffu yes that gets around it. I'll debug once I can get that build working.

## moneromooo-monero | 2018-02-18T12:38:47+00:00
Print the return value, it seems to be an errno value. Also ptr and n.

## stoffu | 2018-02-18T13:23:45+00:00
With this patch:
```diff
diff --git a/contrib/epee/src/memwipe.c b/contrib/epee/src/memwipe.c
index e3a2f76c..d0ee71a9 100644
--- a/contrib/epee/src/memwipe.c
+++ b/contrib/epee/src/memwipe.c
@@ -50,7 +50,9 @@
 
 void *memwipe(void *ptr, size_t n)
 {
-  if (memset_s(ptr, n, 0, n))
+  errno_t r = memset_s(ptr, n, 0, n);
+  fprintf(stderr, "errno=%d, ptr=%p, n=%zu\n", r, ptr, n);
+  if (r)
   {
 #ifdef NDEBUG
     fprintf(stderr, "Error: memset_s failed\n");
```
I get the following when opening an existing wallet file:
```
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd60, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd70, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd70, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd70, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
errno=0, ptr=0x7fff5486bd50, n=32
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.

Monero 'Helium Hydra' (v0.11.1.0-master-4f80c507)
Logging to build/release/bin/monero-wallet-cli.log
errno=22, ptr=0x0, n=0
Error: memset_s failed

```

## moneromooo-monero | 2018-02-18T13:34:04+00:00
Add a crash if ptr==NULL, and look at the stack trace. Easy to fix, but I want to make sure this is not a bug in the first place.

## jtgrassie | 2018-02-18T13:36:34+00:00
```
(lldb) frame variable 
(void *) ptr = 0x0000000000000000
(size_t) n = 0
(lldb) p (int)memset_s(ptr, n, 0, n)
(int) $2 = 22
```

## jtgrassie | 2018-02-18T13:37:56+00:00
```
(lldb) bt
* thread #1: tid = 0x5651a1, 0x00007fff96ab4f06 libsystem_kernel.dylib`__pthread_kill + 10, queue = 'com.apple.main-thread', stop reason = signal SIGABRT
  * frame #0: 0x00007fff96ab4f06 libsystem_kernel.dylib`__pthread_kill + 10
    frame #1: 0x00007fff91dcf4ec libsystem_pthread.dylib`pthread_kill + 90
    frame #2: 0x00007fff90b9f6df libsystem_c.dylib`abort + 129
    frame #3: 0x00000001033c1781 libcommon.dylib`memwipe(ptr=0x0000000000000000, n=0) + 49 at memwipe.c:59
    frame #4: 0x00000001033bf11a libcommon.dylib`epee::wipeable_string::grow(this=0x00007fff5fbf3fb0, sz=0, reserved=1024) + 618 at wipeable_string.cpp:96
    frame #5: 0x00000001033c05d0 libcommon.dylib`epee::wipeable_string::reserve(this=0x00007fff5fbf3fb0, sz=1024) + 48 at wipeable_string.cpp:121
    frame #6: 0x00000001033624dc libcommon.dylib`(anonymous namespace)::read_from_tty(aPass=0x00007fff5fbf3fb0) + 28 at password.cpp:131
    frame #7: 0x0000000103361753 libcommon.dylib`(anonymous namespace)::read_from_tty(verify=true, message="Enter a new password for the wallet", pass1=0x00007fff5fbf3fb0, pass2=0x00007fff5fbf3f98) + 83 at password.cpp:168
    frame #8: 0x0000000103361455 libcommon.dylib`tools::password_container::prompt(verify=true, message="Enter a new password for the wallet") + 325 at password.cpp:237
    frame #9: 0x0000000100096340 monero-wallet-cli`(anonymous namespace)::password_prompter(prompt="Enter a new password for the wallet", verify=true) + 112 at simplewallet.cpp:151
    frame #10: 0x00000001001631d2 monero-wallet-cli`boost::optional<tools::password_container> std::__1::__invoke_void_return_wrapper<boost::optional<tools::password_container> >::__call<boost::optional<tools::password_container> (*&)(char const*, bool), char const*, bool>(boost::optional<tools::password_container> (*&&&)(char const*, bool), char const*&&, bool&&) [inlined] decltype(__f=0x00007fff5fbf60f8, __args=0x00007fff5fbf42a0, __args=0x00007fff5fbf429f)(char const*, bool)>(fp)(std::__1::forward<char const*, bool>(fp0))) std::__1::__invoke<boost::optional<tools::password_container> (*&)(char const*, bool), char const*, bool>(boost::optional<tools::password_container> (*&&&)(char const*, bool), char const*&&, bool&&) + 130 at __functional_base:416
    frame #11: 0x0000000100163197 monero-wallet-cli`boost::optional<tools::password_container> std::__1::__invoke_void_return_wrapper<boost::optional<tools::password_container> >::__call<boost::optional<tools::password_container> (__args=0x00007fff5fbf60f8, __args=0x00007fff5fbf42a0, __args=0x00007fff5fbf429f)(char const*, bool), char const*, bool>(boost::optional<tools::password_container> (*&&&)(char const*, bool), char const*&&, bool&&) + 71 at __functional_base:437
    frame #12: 0x0000000100163040 monero-wallet-cli`std::__1::__function::__func<boost::optional<tools::password_container> (*)(char const*, bool), std::__1::allocator<boost::optional<tools::password_container> (*)(char const*, bool)>, boost::optional<tools::password_container> (char const*, bool)>::operator(this=0x00007fff5fbf60f0, __arg=0x00007fff5fbf42a0, __arg=0x00007fff5fbf429f)(char const*&&, bool&&) + 80 at functional:1437
    frame #13: 0x0000000100e683aa libwallet.dylib`std::__1::function<boost::optional<tools::password_container> (char const*, bool)>::operator(this=0x00007fff5fbf60f0, __arg="Enter a new password for the wallet", __arg=true)(char const*, bool) const + 202 at functional:1817
    frame #14: 0x0000000100c9f5c7 libwallet.dylib`(anonymous namespace)::get_password(vm=0x00007fff5fbff470, opts=0x00007fff5fbf4be0, password_prompter=0x00007fff5fbf60f0, verify=true)::options const&, std::__1::function<boost::optional<tools::password_container> (char const*, bool)> const&, bool) + 2663 at wallet2.cpp:226
    frame #15: 0x0000000100ca5bd8 libwallet.dylib`tools::wallet2::make_new(vm=0x00007fff5fbff470, password_prompter=0x00007fff5fbf60f0)> const&) + 232 at wallet2.cpp:674
    frame #16: 0x0000000100093f98 monero-wallet-cli`cryptonote::simple_wallet::new_wallet(this=0x00007fff5fbfeae0, vm=0x00007fff5fbff470, recovery_key=0x00007fff5fbfebd8, recover=false, two_random=false, old_language="") + 184 at simplewallet.cpp:2710
    frame #17: 0x000000010008dbf0 monero-wallet-cli`cryptonote::simple_wallet::init(this=0x00007fff5fbfeae0, vm=0x00007fff5fbff470) + 36960 at simplewallet.cpp:2481
    frame #18: 0x00000001000c446c monero-wallet-cli`main(argc=1, argv=0x00007fff5fbff4f8) + 1276 at simplewallet.cpp:6802
    frame #19: 0x00007fff8fb415ad libdyld.dylib`start + 1
    frame #20: 0x00007fff8fb415ad libdyld.dylib`start + 1
```

## moneromooo-monero | 2018-02-18T13:47:48+00:00
Please try with https://github.com/monero-project/monero/pull/3289

## jtgrassie | 2018-02-18T14:14:20+00:00
#3289 now fixes.

# Action History
- Created by: jtgrassie | 2018-02-18T07:02:14+00:00
- Closed at: 2018-02-21T18:08:44+00:00
