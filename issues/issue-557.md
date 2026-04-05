---
title: Linker error on FreeBSD
source_url: https://github.com/Cuprate/cuprate/issues/557
author: hiddener
assignees: []
labels: []
created_at: '2025-10-13T02:14:21+00:00'
updated_at: '2026-02-26T21:50:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Building from source on FreeBSD 14.3, the following error is returned:

   ```
error: linking with `cc` failed: exit status: 1
  |
  = note:  "cc" "-Wl,--version-script=/tmp/rustczgp3ta/list" "-Wl,--no-undefined-version" "-m64" "/tmp/rustczgp3ta/symbols.o" "<2 object files omitted>" "-Wl,--as-needed" "-Wl,-Bstatic" "-lrandomx" "-Wl,-Bdynamic" "-lstdc++" "-Wl,-Bstatic" "/home/test/cuprate/target/release/deps/{libthiserror-2fd21edc27463045.rlib,libbitflags-746ed2b054c4e266.rlib,liblibc-4d42eeaa18ea7c4a.rlib}.rlib" "<sysroot>/lib/rustlib/x86_64-unknown-freebsd/lib/{libstd-*,libpanic_abort-*,libobject-*,libmemchr-*,libaddr2line-*,libgimli-*,librustc_demangle-*,libstd_detect-*,libhashbrown-*,librustc_std_workspace_alloc-*,libminiz_oxide-*,libadler2-*,libunwind-*,libcfg_if-*,liblibc-*,librustc_std_workspace_core-*,liballoc-*,libcore-*,libcompiler_builtins-*}.rlib" "-Wl,-Bdynamic" "-lrt" "-lutil" "-lexecinfo" "-lkvm" "-lmemstat" "-lkvm" "-lutil" "-lprocstat" "-lrt" "-ldevstat" "-lexecinfo" "-lpthread" "-lgcc_s" "-lc" "-lm" "-lrt" "-lpthread" "-lrt" "-lutil" "-lexecinfo" "-lkvm" "-lmemstat" "-lkvm" "-lutil" "-lprocstat" "-lrt" "-ldevstat" "-L" "/tmp/rustczgp3ta/raw-dylibs" "-Wl,--eh-frame-hdr" "-Wl,-z,noexecstack" "-L" "/home/test/cuprate/target/release/build/randomx-rs-7390d8927567bce5/out/lib64" "-L" "/home/test/cuprate/target/release/build/randomx-rs-7390d8927567bce5/out/lib" "-o" "/home/test/cuprate/target/release/deps/librandomx_rs-be1292aca6b8e747.so" "-Wl,--gc-sections" "-shared" "-Wl,-z,relro,-z,now" "-Wl,-O1" "-nodefaultlibs"
  = note: some arguments are omitted. use `--verbose` to show all linker arguments
  = note: ld: error: unable to find library -lstdc++
          cc: error: linker command failed with exit code 1 (use -v to see invocation)


error: could not compile `randomx-rs` (lib) due to 1 previous error
```

I assume it should link with "lc++"

# Discussion History
## smiquee | 2026-02-26T21:50:58+00:00
@hinto-janai The original project made an update to support Freebsd, since tag 1.4.1. I just checked your repo and it seems you can directly merge the modifications from their version. Would be great to do so ;) 

# Action History
- Created by: hiddener | 2025-10-13T02:14:21+00:00
