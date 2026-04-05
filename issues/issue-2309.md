---
title: Linking CXX executable xmrig fails on Ubuntu 20.10
source_url: https://github.com/xmrig/xmrig/issues/2309
author: sascha08-15
assignees: []
labels: []
created_at: '2021-04-24T11:26:38+00:00'
updated_at: '2021-04-25T01:56:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Nothing to special about my setup, running Ubuntu 20.10 here, latest updates are in.

Running as described in `make -j$(nproc)` I end up with 1) a successful compilation but 2) with a failing linking:


```[100%] Linking CXX executable xmrig
/usr/bin/ld: CMakeFiles/xmrig.dir/src/3rdparty/fmt/format.cc.o: in function `fmt::v7::system_error::init(int, fmt::v7::basic_string_view<char>, fmt::v7::format_args)':
format.cc:(.text+0x1df8): undefined reference to `std::runtime_error::operator=(std::runtime_error&&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/io/Env.cpp.o: in function `std::_Sp_counted_ptr_inplace<std::__detail::_NFA<std::__cxx11::regex_traits<char> >, std::allocator<std::__detail::_NFA<std::__cxx11::regex_traits<char> > >, (__gnu_cxx::_Lock_policy)2>::_M_get_deleter(std::type_info const&)':
Env.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceINSt8__detail4_NFAINSt7__cxx1112regex_traitsIcEEEESaIS5_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceINSt8__detail4_NFAINSt7__cxx1112regex_traitsIcEEEESaIS5_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): undefined reference to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/dns/Dns.cpp.o: in function `std::_Sp_counted_ptr_inplace<xmrig::DnsUvBackend, std::allocator<xmrig::DnsUvBackend>, (__gnu_cxx::_Lock_policy)2>::_M_get_deleter(std::type_info const&)':
Dns.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceIN5xmrig12DnsUvBackendESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceIN5xmrig12DnsUvBackendESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): undefined reference to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o: in function `std::_Sp_counted_ptr_inplace<xmrig::DnsRequest, std::allocator<xmrig::DnsRequest>, (__gnu_cxx::_Lock_policy)2>::_M_get_deleter(std::type_info const&)':
DnsUvBackend.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceIN5xmrig10DnsRequestESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceIN5xmrig10DnsRequestESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): undefined reference to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/dns/DnsUvBackend.cpp.o: in function `std::_Sp_counted_ptr_inplace<uv_getaddrinfo_s, std::allocator<uv_getaddrinfo_s>, (__gnu_cxx::_Lock_policy)2>::_M_get_deleter(std::type_info const&)':
DnsUvBackend.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceI16uv_getaddrinfo_sSaIS0_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceI16uv_getaddrinfo_sSaIS0_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): undefined reference to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/stratum/benchmark/BenchClient.cpp.o: in function `std::_Sp_counted_ptr_inplace<xmrig::HttpListener, std::allocator<xmrig::HttpListener>, (__gnu_cxx::_Lock_policy)2>::_M_get_deleter(std::type_info const&)':
BenchClient.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceIN5xmrig12HttpListenerESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceIN5xmrig12HttpListenerESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): undefined reference to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)'
/usr/bin/ld: CMakeFiles/xmrig.dir/src/base/net/http/HttpClient.cpp.o:HttpClient.cpp:(.text._ZNSt23_Sp_counted_ptr_inplaceIN5xmrig5TimerESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info[_ZNSt23_Sp_counted_ptr_inplaceIN5xmrig5TimerESaIS1_ELN9__gnu_cxx12_Lock_policyE2EE14_M_get_deleterERKSt9type_info]+0x1a): more undefined references to `std::_Sp_make_shared_tag::_S_eq(std::type_info const&)' follow
collect2: error: ld returned 1 exit status
```

# Discussion History
## Spudz76 | 2021-04-25T01:56:59+00:00
Need `CMakeCache.txt` to see what it thinks of your toolchain.

64-bit everything right?  Do you have both `gcc` and `g++` installed?  Unsure what else to probe although it seems like a `libstdc++` problem.

# Action History
- Created by: sascha08-15 | 2021-04-24T11:26:38+00:00
