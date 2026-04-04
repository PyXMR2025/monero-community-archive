---
title: bitmonero-0.9.1 won't build due to dns_utils.cpp
source_url: https://github.com/monero-project/monero/issues/647
author: GioMac
assignees: []
labels: []
created_at: '2016-02-05T22:14:20+00:00'
updated_at: '2018-04-10T18:32:53+00:00'
type: issue
status: closed
closed_at: '2016-07-07T20:03:47+00:00'
---

# Original Description
I've got errors with building version 0.9.1, while 0.8.8.6 has successfully passed build. Centos 7 w/latest updates:

http://pastebin.com/yAVCqjke

> [ 20%] Building CXX object src/common/CMakeFiles/common.dir/dns_utils.cpp.o
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp: In constructor 'tools::DNSResolver::DNSResolver()':
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:204:57: error: invalid conversion from 'const char_' to 'char_' [-fpermissive]
>      ub_ctx_set_fwd(m_data->m_ub_context, dns_public_addr);
>                                                          ^
> In file included from /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:33:0:
> /usr/include/unbound.h:295:5: error:   initializing argument 2 of 'int ub_ctx_set_fwd(ub_ctx_, char_)' [-fpermissive]
>  int ub_ctx_set_fwd(struct ub_ctx\* ctx, char\* addr);
>      ^
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:205:60: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
>      ub_ctx_set_option(m_data->m_ub_context, "do-udp:", "no");
>                                                             ^
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:205:60: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:206:61: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
>      ub_ctx_set_option(m_data->m_ub_context, "do-tcp:", "yes");
>                                                              ^
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:206:61: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:229:58: error: invalid conversion from 'const char_' to 'char_' [-fpermissive]
>      ub_ctx_add_ta(m_data->m_ub_context, ::get_builtin_ds() );
>                                                           ^
> In file included from /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:33:0:
> /usr/include/unbound.h:337:5: error:   initializing argument 2 of 'int ub_ctx_add_ta(ub_ctx_, char_)' [-fpermissive]
>  int ub_ctx_add_ta(struct ub_ctx\* ctx, char\* ta);
>      ^
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp: In member function 'std::vectorstd::basic_string<char > tools::DNSResolver::get_record(const string&, int, std::string (_)(const char_, size_t), bool&, bool&)':
> /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:261:51: error: invalid conversion from 'const char_' to 'char_' [-fpermissive]
>    if (!ub_resolve(m_data->m_ub_context, url.c_str(), record_type, DNS_CLASS_IN, &result))
>                                                    ^
> In file included from /root/coin/bitmonero-0.9.1/src/common/dns_utils.cpp:33:0:
> /usr/include/unbound.h:445:5: error:   initializing argument 2 of 'int ub_resolve(ub_ctx_, char_, int, int, ub_result*_)' [-fpermissive]
>  int ub_resolve(struct ub_ctx_ ctx, char\* name, int rrtype,
>      ^
> cc1plus: all warnings being treated as errors
> make[3]: **\* [src/common/CMakeFiles/common.dir/dns_utils.cpp.o] Error 1
> make[3]: Leaving directory `/root/coin/bitmonero-0.9.1/build/release'
> make[2]: *** [src/common/CMakeFiles/common.dir/all] Error 2
> make[2]: Leaving directory`/root/coin/bitmonero-0.9.1/build/release'
> make[1]: **\* [all] Error 2
> make[1]: Leaving directory `/root/coin/bitmonero-0.9.1/build/release'
> make: **\* [release-all] Error 2
> [root@test bitmonero-0.9.1]#


# Discussion History
## moneromooo-monero | 2016-02-05T22:19:12+00:00
That seems like an older version of libunbound.
The one in the monero tree takes a const char\* as second parameter.


## GioMac | 2016-02-05T22:26:54+00:00
libunbound is newer than required version from README doc, ldns is also updated:
[root@test bitmonero-0.9.1]# rpm -q unbound-libs unbound-devel ldns ldns-devel
unbound-libs-1.4.20-26.el7.x86_64
unbound-devel-1.4.20-26.el7.x86_64
ldns-1.6.17-16.el7.centos.x86_64
ldns-devel-1.6.17-16.el7.centos.x86_64
[root@test bitmonero-0.9.1]#


## GioMac | 2016-02-05T22:32:26+00:00
Same with 0.9.0 too


## GioMac | 2016-02-05T23:41:37+00:00
Related change: https://github.com/monero-project/bitmonero/commit/0d40de48c2da9cd24fa656500034f64baf87fd89


## moneromooo-monero | 2016-02-21T14:24:58+00:00
1.4.20 still has the non const version indeed.
Fixed in https://github.com/monero-project/bitmonero/pull/684


## GioMac | 2016-02-21T19:53:55+00:00
Issue not completely solved after applying patch:
[ 34%] Building CXX object src/p2p/CMakeFiles/p2p.dir/data_logger.cpp.o
/root/bitmonero-0.9.1/src/common/dns_utils.cpp: In constructor 'tools::DNSResolver::DNSResolver()':
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:207:60: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
     ub_ctx_set_option(m_data->m_ub_context, "do-udp:", "no");
                                                            ^
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:207:60: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:208:61: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
     ub_ctx_set_option(m_data->m_ub_context, "do-tcp:", "yes");
                                                             ^
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:208:61: error: deprecated conversion from string constant to 'char_' [-Werror=write-strings]
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:231:58: error: invalid conversion from 'const char_' to 'char_' [-fpermissive]
     ub_ctx_add_ta(m_data->m_ub_context, ::get_builtin_ds() );
                                                          ^
In file included from /root/bitmonero-0.9.1/src/common/dns_utils.cpp:33:0:
/usr/include/unbound.h:337:5: error:   initializing argument 2 of 'int ub_ctx_add_ta(ub_ctx_, char_)' [-fpermissive]
 int ub_ctx_add_ta(struct ub_ctx\* ctx, char\* ta);
     ^
/root/bitmonero-0.9.1/src/common/dns_utils.cpp: In member function 'std::vectorstd::basic_string<char > tools::DNSResolver::get_record(const string&, int, std::string (_)(const char_, size_t), bool&, bool&)':
/root/bitmonero-0.9.1/src/common/dns_utils.cpp:263:51: error: invalid conversion from 'const char_' to 'char_' [-fpermissive]
   if (!ub_resolve(m_data->m_ub_context, url.c_str(), record_type, DNS_CLASS_IN, &result))
                                                   ^
In file included from /root/bitmonero-0.9.1/src/common/dns_utils.cpp:33:0:
/usr/include/unbound.h:445:5: error:   initializing argument 2 of 'int ub_resolve(ub_ctx_, char_, int, int, ub_result*_)' [-fpermissive]
 int ub_resolve(struct ub_ctx_ ctx, char\* name, int rrtype,
     ^
cc1plus: all warnings being treated as errors
make[3]: **\* [src/common/CMakeFiles/common.dir/dns_utils.cpp.o] Error 1


## moneromooo-monero | 2016-02-22T08:38:33+00:00
Oh, somehow I'd missed this was happening at more than one place, and only fixed one :)


## moneromooo-monero | 2016-02-23T19:04:18+00:00
I updated the branch (forced push), which should have the workaround for all the calls needed.


## GioMac | 2016-02-23T19:35:56+00:00
Good,
can you please refer the commit #?


## moneromooo-monero | 2016-02-24T11:48:40+00:00
https://github.com/moneromooo-monero/bitmonero/tree/ub-const


## fluffypony | 2016-07-07T20:03:47+00:00
Fixed


## vrobolab | 2018-04-10T18:30:41+00:00
Same problem with CentOS 7 and latest git pull.

```

[ 17%] Building CXX object src/common/CMakeFiles/obj_common.dir/dns_utils.cpp.o
/dev/shm/monero/src/common/dns_utils.cpp: In constructor ‘tools::DNSResolver::DNSResolver()’:
/dev/shm/monero/src/common/dns_utils.cpp:233:52: error: invalid conversion from ‘const char*’ to ‘char*’ [-fpermissive]
       ub_ctx_set_fwd(m_data->m_ub_context, ip.c_str());
                                            ~~~~~~~~^~
In file included from /dev/shm/monero/src/common/dns_utils.cpp:31:0:
/usr/include/unbound.h:295:5: note:   initializing argument 2 of ‘int ub_ctx_set_fwd(ub_ctx*, char*)’
 int ub_ctx_set_fwd(struct ub_ctx* ctx, char* addr);
     ^~~~~~~~~~~~~~
```

gcc (GCC) 7.2.1 20170829 (Red Hat 7.2.1-1)
cmake3 version 3.6.3
unbound-libs-1.4.20-34.el7.x86_64
unbound-devel-1.4.20-34.el7.x86_64
ldns-1.6.16-10.el7.x86_64
ldns-devel-1.6.16-10.el7.x86_64


# Action History
- Created by: GioMac | 2016-02-05T22:14:20+00:00
- Closed at: 2016-07-07T20:03:47+00:00
