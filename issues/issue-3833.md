---
title: Compile error, please help.
source_url: https://github.com/xmrig/xmrig/issues/3833
author: wong-fi-hung
assignees: []
labels: []
created_at: '2026-07-21T11:46:41+00:00'
updated_at: '2026-07-21T20:31:00+00:00'
type: issue
status: closed
closed_at: '2026-07-21T20:31:00+00:00'
---

# Original Description
how to fix the following errors...?

/root/Project/xmrig/src/base/net/tls/TlsGen.cpp: In member function ‘bool xmrig::TlsGen::generate_x509(const char*)’:
/root/Project/xmrig/src/base/net/tls/TlsGen.cpp:118:32: error: invalid conversion from ‘const X509_name_st*’ to ‘X509_NAME*’ {aka ‘X509_name_st*’} [-fpermissive]
  118 |     X509_NAME_add_entry_by_txt(name, "CN", MBSTRING_ASC, reinterpret_cast<const uint8_t *>(commonName), -1, -1, 0);
      |                                ^~~~
      |                                |
      |                                const X509_name_st*
In file included from /usr/local/deps/include/openssl/ssl.h:34,
                 from /root/Project/xmrig/src/base/net/tls/TlsGen.cpp:22:
/usr/local/deps/include/openssl/x509.h:1072:43: note:   initializing argument 1 of ‘int X509_NAME_add_entry_by_txt(X509_NAME*, const char*, int, const unsigned char*, int, int, int)’
 1072 | int X509_NAME_add_entry_by_txt(X509_NAME *name, const char *field, int type.

# Discussion History
## SChernykh | 2026-07-21T17:37:22+00:00
This is fixed in https://github.com/xmrig/xmrig/pull/3808

## wong-fi-hung | 2026-07-21T20:31:00+00:00
Thanks bro...
The problem now has been solved.

# Action History
- Created by: wong-fi-hung | 2026-07-21T11:46:41+00:00
- Closed at: 2026-07-21T20:31:00+00:00
