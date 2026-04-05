---
title: SSL/TLS support
source_url: https://github.com/xmrig/xmrig/issues/758
author: xmrig
assignees: []
labels:
- enhancement
- META
created_at: '2018-09-22T05:54:03+00:00'
updated_at: '2018-10-10T22:22:23+00:00'
type: issue
status: closed
closed_at: '2018-10-10T22:22:23+00:00'
---

# Original Description
In version 2.8 added SSL/TLS support for connections between miner/proxy and pool using OpenSSL library.

### 2 new options added:
* `"tls"` or `--tls` to enable SSL/TLS support.
* `"tls-fingerprint"` or `--tls-fingerprint` to optionally verify pool certificate fingerprint, for advanced usage only.

### Compile from source
OpenSSL support enabled by default if you like compile miner/proxy without TLS support you should use `-DWITH_TLS=OFF` CMake option.

### Known issues
xmrig-proxy still require external solution like haproxy for incoming connections TLS support.

# Discussion History
## k0ste | 2018-10-03T07:51:23+00:00
Actually `tls` options is not listed in `help`:

```
[k0ste@WorkStation bin]$ ./xmrig --version ; ./xmrig --help | grep -i tls
XMRig 2.8.0-rc
 built on Oct  3 2018 with GCC 8.2.1
 features: 64-bit AES

libuv/1.23.1
microhttpd/0.9.59
OpenSSL/1.1.1
[k0ste@WorkStation bin]$ 
```

# Action History
- Created by: xmrig | 2018-09-22T05:54:03+00:00
- Closed at: 2018-10-10T22:22:23+00:00
