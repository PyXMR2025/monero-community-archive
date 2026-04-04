---
title: static build produces dynamic-linked file(monero-wallet-cli)
source_url: https://github.com/monero-project/monero/issues/9563
author: dtcomp
assignees: []
labels:
- question
created_at: '2024-11-11T09:21:22+00:00'
updated_at: '2024-12-13T23:35:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I wanted to build a static monero-wallet-cli.
The compile finished, but apparently products are not static:

```
make -j6 release-static-linux-x86_64
cd build/Linux/_HEAD_detached_at_v0.18.3.4_/release/bin/
file monero-wallet-cli 
monero-wallet-cli: ELF 64-bit LSB pie executable, x86-64, version 1 (GNU/Linux), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0c9d04df7b181472cef6d098b03b97d745192356, for GNU/Linux 3.2.0, with debug_info, not stripped
```
Linux bookworm 6.1.0-27-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.115-1 (2024-11-01) x86_64 GNU/Linux

# Discussion History
## 0xFFFC0000 | 2024-11-11T09:25:00+00:00
Can you run `ldd` on your binary and put the results here. 

E.g. 

![image](https://github.com/user-attachments/assets/650c3794-b05f-4a56-a16d-30f7f7ec89bc)

## dtcomp | 2024-11-11T09:30:47+00:00
ldd monero-wallet-cli 
	linux-vdso.so.1 (0x00007ffc1435a000)
	libudev.so.1 => /lib/x86_64-linux-gnu/libudev.so.1 (0x00007f9e6624f000)
	libm.so.6 => /lib/x86_64-linux-gnu/libm.so.6 (0x00007f9e64b21000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f9e64940000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f9e66289000)
Debian Bookworm

## dtcomp | 2024-11-12T03:56:24+00:00
It looks like 2 libs prevent static link - libudev and libgssapi_krb5.
It was simple to get a static libudev, but still working on libgssapi_krb5.
update: mebbe not worth the bother: the above-mentioned libs define the same function (memdup) - so link-time errors...

## selsta | 2024-12-13T23:35:02+00:00
Easiest way to get static binaries would be to use `make depends`.

https://github.com/monero-project/monero?tab=readme-ov-file#cross-compiling

# Action History
- Created by: dtcomp | 2024-11-11T09:21:22+00:00
