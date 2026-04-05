---
title: 'msr: Write to unrecognized MSR 0xc0011020 by xmrig (AMD Ryzen 5 - 4600H)'
source_url: https://github.com/xmrig/xmrig/issues/2098
author: Bogdan107
assignees: []
labels: []
created_at: '2021-02-12T10:57:27+00:00'
updated_at: '2021-04-12T14:15:40+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:15:40+00:00'
---

# Original Description
This is message in my syslog:
```msr: Write to unrecognized MSR 0xc0011020 by xmrig (pid: 68425). Please report to x86@kernel.org.```

$ uname -p
```AMD Ryzen 5 4600H with Radeon Graphics```
$ uname -r
```5.10.15-gentoo-x86_64```

Some messages from xmrig:
```
* ABOUT        XMRig/6.8.1 gcc/10.2.0
* LIBS         libuv/1.40.0 OpenSSL/1.1.1i hwloc/2.4.0
* CPU          AMD Ryzen 5 4600H with Radeon Graphics (1) 64-bit AES
               L2:3.0 MB L3:8.0 MB 6C/12T NUMA:1
* MOTHERBOARD  HP - 87B1
* ASSEMBLY     auto:ryzen
cpu      use argon2 implementation AVX2
msr      register values for "ryzen_17h" preset have been set successfully (21 ms)
 ```

May be this report will help.

# Discussion History
## coolhaircut | 2021-03-05T22:34:04+00:00
The linux kernel is disabling userspace writes to MSR in version 5.9 :(

For now, you should be able to fix this by adding `msr.allow_writes=on` to the kernel cmdline (`GRUB_CMDLINE_LINUX` variable in `/etc/default/grub')

# Action History
- Created by: Bogdan107 | 2021-02-12T10:57:27+00:00
- Closed at: 2021-04-12T14:15:40+00:00
