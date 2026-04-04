---
title: 'guix: non-deterministic build failures'
source_url: https://github.com/monero-project/monero/issues/9900
author: tobtoht
assignees: []
labels:
- build system
created_at: '2025-04-08T23:01:59+00:00'
updated_at: '2025-10-25T09:57:36+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Tracking issue for non-deterministic build failures one may encounter when performing a full-source bootstrap of Monero.

Failures marked with 🔄 can be resolved by simply rerunning the build.

## Current

### vyyipkddjy8g1nz9fm4fx37vazs4rf5n-automake-1.16.5.drv 🔄

```
============================================================================
Testsuite summary for GNU Automake 1.16.5
============================================================================
# TOTAL: 2720
# PASS:  2396
# SKIP:  286
# XFAIL: 37
# FAIL:  1
# XPASS: 0
# ERROR: 0
```

Test failure: `FAIL: t/subobj.sh`

### zs4cr5zy4g514hwkfpx9qs4x9p46fvdk-clisp-2.49-92.drv 🔄

```
Internal error: statement in file "zthread.d", line 771 has been
      reached!!
      Please see <http://clisp.org/impnotes/faq.html#faq-bugs> for bug
      reporting instructions.
```

`Test suite failed, dumping logs.`

## After adding rust

### 6qfw5c8ynw77x1i3dg38nwg7c0xpn2c7-boost_1_83_0.tar.bz2

```
-sha256 hash mismatch for /gnu/store/6qfw5c8ynw77x1i3dg38nwg7c0xpn2c7-boost_1_83_0.tar.bz2:
  expected hash: 13iviiwk1srpw9dmiwabkxv56v0pl0zggjp8zxy1419k5zzfsy34
  actual hash:   0j4qqcb3lrcxhlh6sxldm95rdky1s7rdmk5ymy05lkj4hvwx7rkr
```

To fix this, manually download boost 1.83.0 from https://archives.boost.io/release/1.83.0/source/boost_1_83_0.tar.bz2

Then import it using `guix download boost_1_83_0.tar.bz2`.

### 8wwg41dh3kbbqmlkkb76varm7s59413x-rust-1.54.0.drv 🔄

```
ESC[31mUnable to run process '/tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_crc32fast-1_2_1_H2_run' - No such file or directoryESC[0m
Calling /tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_crc32fast-1_2_1_H2_run failed (see /tmp/guix-build-rust-1.54.0.drv-0/mrustc/output/cargo-build/build_crc32fast-1_2_1_H2.txt_failed.txt for stdout)
> /tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_typenum-1_12_0_run
ESC[31mUnable to run process '/tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_typenum-1_12_0_run' - No such file or directoryESC[0m
Calling /tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_typenum-1_12_0_run failed (see /tmp/guix-build-rust-1.54.0.drv-0/mrustc/output/cargo-build/build_typenum-1_12_0.txt_failed.txt for stdout)
> /tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_libc-0_2_95_H21_run
ESC[31mUnable to run process '/tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_libc-0_2_95_H21_run' - No such file or directoryESC[0m
Calling /tmp/guix-build-rust-1.54.0.drv-0/rustc-1.54.0-src/vendor/log/output/cargo-build/build_libc-0_2_95_H21_run failed (see /tmp/guix-build-rust-1.54.0.drv-0/mrustc/output/cargo-build/build_libc-0_2_95_H21.txt_failed.txt for stdout)
BUILD FAILED
make: *** [minicargo.mk:235: output/cargo] Error 1
```


# Discussion History
# Action History
- Created by: tobtoht | 2025-04-08T23:01:59+00:00
