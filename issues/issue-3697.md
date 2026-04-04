---
title: Linking shared library broken on OSX
source_url: https://github.com/monero-project/monero/issues/3697
author: hashbender
assignees: []
labels:
- invalid
created_at: '2018-04-24T17:44:42+00:00'
updated_at: '2018-10-27T12:24:58+00:00'
type: issue
status: closed
closed_at: '2018-10-27T12:24:58+00:00'
---

# Original Description
I'm trying to link to the hash function using cgo in a Go project, and am failing with the following error: 

Seems that the CMakeLists might need updating.  
```
 20%] Linking CXX shared library libcnutil.dylib
Undefined symbols for architecture x86_64:
  "hw::get_device(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >)", referenced from:
      cryptonote::account_base::create_from_device(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&) in libcryptonote_basic.a(account.cpp.o)
      cryptonote::account_keys::account_keys() in libcryptonote_basic.a(account.cpp.o)
  "_ub_ctx_add_ta", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_create", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_delete", referenced from:
      tools::DNSResolver::~DNSResolver() in libcommon.a(dns_utils.cpp.o)
      tools::DNSResolver::~DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_hosts", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_resolvconf", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_set_fwd", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_ctx_set_option", referenced from:
      tools::DNSResolver::DNSResolver() in libcommon.a(dns_utils.cpp.o)
  "_ub_resolve", referenced from:
      tools::DNSResolver::get_record(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, int, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) in libcommon.a(dns_utils.cpp.o)
  "_ub_resolve_free", referenced from:
      tools::DNSResolver::get_record(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, int, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > (*)(char const*, unsigned long), bool&, bool&) in libcommon.a(dns_utils.cpp.o)
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
make[2]: *** [cnutil/libcnutil.dylib] Error 1
make[1]: *** [cnutil/CMakeFiles/cnutil.dir/all] Error 2
```

# Discussion History
## hyc | 2018-04-24T21:24:57+00:00
Looks like you need to link libunbound.

## quantumproducer | 2018-04-25T02:37:18+00:00
Possibly related? https://github.com/monero-project/monero/issues/3698

## jtgrassie | 2018-04-25T10:10:19+00:00
@quantumproducer not related.

## moneromooo-monero | 2018-10-27T12:16:11+00:00
I've just re-read and noticed it's not monero but another codebase, so I'll close. And what hyc said.

+invalid

# Action History
- Created by: hashbender | 2018-04-24T17:44:42+00:00
- Closed at: 2018-10-27T12:24:58+00:00
