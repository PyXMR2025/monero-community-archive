---
title: 'Compiler warnings: writing 1 byte into a region of size 0'
source_url: https://github.com/monero-project/monero/issues/8320
author: jeffro256
assignees: []
labels: []
created_at: '2022-05-09T19:28:47+00:00'
updated_at: '2024-03-12T20:06:22+00:00'
type: issue
status: closed
closed_at: '2022-05-27T02:25:45+00:00'
---

# Original Description
After I upgraded my Ubuntu distro to Ubuntu 22, I got the following warnings when compiling:

```
In file included from /home/jeff/forks/monero/external/boost/archive/portable_binary_oarchive.hpp:32,
                 from /home/jeff/forks/monero/src/p2p/net_peerlist.cpp:37:
In function ‘void boost::archive::reverse_bytes(signed char, char*)’,
    inlined from ‘void boost::archive::portable_binary_oarchive::save_impl(intmax_t, char)’ at /home/jeff/forks/monero/external/boost/archive/portable_binary_oarchive.hpp:267:26:
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;

```


Here's my system info:

```
OS: Ubuntu 22
g++: (Ubuntu 11.2.0-19ubuntu1) 11.2.0
CPU: Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz
```

# Discussion History
## jeffro256 | 2022-05-09T20:15:30+00:00
Here is another trace:

```
In function ‘void boost::archive::reverse_bytes(signed char, char*)’,
    inlined from ‘void boost::archive::portable_binary_iarchive::load_impl(intmax_t&, char)’ at /home/jeff/forks/monero/external/boost/archive/portable_binary_iarchive.hpp:265:18,
    inlined from ‘void boost::archive::portable_binary_iarchive::load(T&) [with T = boost::serialization::collection_size_type]’ at /home/jeff/forks/monero/external/boost/archive/portable_binary_iarchive.hpp:108:18,
    inlined from ‘static void boost::archive::load_access::load_primitive(Archive&, T&) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::collection_size_type]’ at /usr/include/boost/archive/detail/iserializer.hpp:108:16,
    inlined from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::load_primitive::invoke(Archive&, T&) [with T = boost::serialization::collection_size_type; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/iserializer.hpp:384:40,
    inlined from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::invoke(Archive&, T&) [with T = boost::serialization::collection_size_type; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/iserializer.hpp:461:22,
    inlined from ‘void boost::archive::load(Archive&, T&) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::collection_size_type]’ at /usr/include/boost/archive/detail/iserializer.hpp:624:18,
    inlined from ‘void boost::archive::detail::common_iarchive<Archive>::load_override(T&) [with T = boost::serialization::collection_size_type; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/common_iarchive.hpp:67:22,
    inlined from ‘void boost::archive::portable_binary_iarchive::load_override(T&) [with T = boost::serialization::collection_size_type]’ at /home/jeff/forks/monero/external/boost/archive/portable_binary_iarchive.hpp:160:52,
    inlined from ‘Archive& boost::archive::detail::interface_iarchive<Archive>::operator>>(T&) [with T = boost::serialization::collection_size_type; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/interface_iarchive.hpp:68:36,
    inlined from ‘void boost::serialization::load(Archive&, boost::serialization::nvp<T>&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::collection_size_type]’ at /usr/include/boost/serialization/nvp.hpp:56:8,
    inlined from ‘static void boost::serialization::free_loader<Archive, T>::invoke(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::nvp<boost::serialization::collection_size_type>]’ at /usr/include/boost/serialization/split_free.hpp:58:13,
    inlined from ‘void boost::serialization::split_free(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::nvp<boost::serialization::collection_size_type>]’ at /usr/include/boost/serialization/split_free.hpp:74:18,
    inlined from ‘void boost::serialization::serialize(Archive&, boost::serialization::nvp<T>&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::collection_size_type]’ at /usr/include/boost/serialization/nvp.hpp:65:15,
    inlined from ‘void boost::serialization::serialize_adl(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = boost::serialization::nvp<boost::serialization::collection_size_type>]’ at /usr/include/boost/serialization/serialization.hpp:118:14,
    inlined from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::load_only::invoke(Archive&, const T&) [with T = boost::serialization::nvp<boost::serialization::collection_size_type>; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/iserializer.hpp:395:48,
    inlined from ‘static void boost::archive::detail::load_non_pointer_type<Archive>::invoke(Archive&, T&) [with T = const boost::serialization::nvp<boost::serialization::collection_size_type>; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/iserializer.hpp:461:22,
    inlined from ‘void boost::archive::load(Archive&, T&) [with Archive = boost::archive::portable_binary_iarchive; T = const boost::serialization::nvp<boost::serialization::collection_size_type>]’ at /usr/include/boost/archive/detail/iserializer.hpp:624:18,
    inlined from ‘void boost::archive::detail::common_iarchive<Archive>::load_override(T&) [with T = const boost::serialization::nvp<boost::serialization::collection_size_type>; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/common_iarchive.hpp:67:22,
    inlined from ‘void boost::archive::portable_binary_iarchive::load_override(T&) [with T = const boost::serialization::nvp<boost::serialization::collection_size_type>]’ at /home/jeff/forks/monero/external/boost/archive/portable_binary_iarchive.hpp:160:52,
    inlined from ‘Archive& boost::archive::detail::interface_iarchive<Archive>::operator>>(T&) [with T = const boost::serialization::nvp<boost::serialization::collection_size_type>; Archive = boost::archive::portable_binary_iarchive]’ at /usr/include/boost/archive/detail/interface_iarchive.hpp:68:36,
    inlined from ‘void boost::serialization::load(Archive&, std::vector<U, Allocator>&, unsigned int, mpl_::false_) [with Archive = boost::archive::portable_binary_iarchive; U = crypto::public_key; Allocator = std::allocator<crypto::public_key>]’ at /usr/include/boost/serialization/vector.hpp:84:8,
    inlined from ‘void boost::serialization::load(Archive&, std::vector<U, Allocator>&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; U = crypto::public_key; Allocator = std::allocator<crypto::public_key>]’ at /usr/include/boost/serialization/vector.hpp:165:9,
    inlined from ‘static void boost::serialization::free_loader<Archive, T>::invoke(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = std::vector<crypto::public_key>]’ at /usr/include/boost/serialization/split_free.hpp:58:13,
    inlined from ‘void boost::serialization::split_free(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = std::vector<crypto::public_key>]’ at /usr/include/boost/serialization/split_free.hpp:74:18,
    inlined from ‘void boost::serialization::serialize(Archive&, std::vector<U, Allocator>&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; U = crypto::public_key; Allocator = std::allocator<crypto::public_key>]’ at /usr/include/boost/serialization/vector.hpp:176:37,
    inlined from ‘void boost::serialization::serialize_adl(Archive&, T&, unsigned int) [with Archive = boost::archive::portable_binary_iarchive; T = std::vector<crypto::public_key>]’ at /usr/include/boost/serialization/serialization.hpp:118:14,
    inlined from ‘void boost::archive::detail::iserializer<Archive, T>::load_object_data(boost::archive::detail::basic_iarchive&, void*, unsigned int) const [with Archive = boost::archive::portable_binary_iarchive; T = std::vector<crypto::public_key>]’ at /usr/include/boost/archive/detail/iserializer.hpp:187:40:
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:48:15: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   48 |         *last = *first;
      |         ~~~~~~^~~~~~~~
/home/jeff/forks/monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~

```

## moneromooo-monero | 2022-05-09T20:21:21+00:00
AFAICT it's fine and ASAN doesn't complain on:
```
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

inline void
reverse_bytes(signed char size, char *address){
    if (size <= 0)
        printf("BEEP\n");
    char * first = address;
    char * last = first + size - 1;
    for(;first < last;++first, --last){
        char x = *last;
        *last = *first;
        *first = x;
    }
}

int main()
{
  for (int i = 1; i <= 127; ++i)
  {
    char *str = (char*)malloc(i);
    reverse_bytes(i, str);
    free(str);
  }
  return 9;
}

```


## Xeverous | 2024-03-12T20:06:20+00:00
I know it's late but FYI I got the same weird warning on my own project which uses high-level C++ (no memcpy / byte stuff), it points to random types and totally sane operations like ctor member init list (which can not cause undefined behavior).

[Searching GCC bugzilla](https://gcc.gnu.org/bugzilla/buglist.cgi?bug_status=UNCONFIRMED&bug_status=NEW&bug_status=ASSIGNED&bug_status=SUSPENDED&bug_status=WAITING&bug_status=REOPENED&cf_known_to_fail_type=allwords&cf_known_to_work_type=allwords&f0=OP&f1=OP&f10=OP&f11=OP&f12=product&f13=component&f14=alias&f15=short_desc&f17=content&f18=CP&f19=CP&f2=product&f20=OP&f21=OP&f22=alias&f23=short_desc&f25=content&f26=CP&f27=CP&f28=OP&f29=OP&f3=component&f30=product&f31=component&f32=alias&f33=short_desc&f35=content&f36=CP&f37=CP&f38=OP&f39=OP&f4=alias&f40=alias&f41=short_desc&f43=content&f44=CP&f45=CP&f46=OP&f47=OP&f48=product&f49=component&f5=short_desc&f50=alias&f51=short_desc&f53=content&f54=CP&f55=CP&f56=OP&f57=OP&f58=alias&f59=short_desc&f61=content&f62=CP&f63=CP&f7=content&f8=CP&f9=CP&j1=OR&j11=OR&j21=OR&j29=OR&j39=OR&j47=OR&j57=OR&o12=substring&o13=substring&o14=substring&o15=substring&o16=substring&o17=matches&o2=substring&o22=substring&o23=substring&o24=substring&o25=matches&o3=substring&o30=substring&o31=substring&o32=substring&o33=substring&o34=substring&o35=matches&o4=substring&o40=substring&o41=substring&o42=substring&o43=matches&o48=substring&o49=substring&o5=substring&o50=substring&o51=substring&o52=substring&o53=matches&o58=substring&o59=substring&o6=substring&o60=substring&o61=matches&o7=matches&product=gcc&query_format=advanced&short_desc=byte%20into%20a%20region%20of%20size%200&short_desc_type=allwordssubstr&v12=into&v13=into&v14=into&v15=into&v16=into&v17="into"&v2=byte&v22=a&v23=a&v24=a&v25="a"&v3=byte&v30=region&v31=region&v32=region&v33=region&v34=region&v35="region"&v4=byte&v40=of&v41=of&v42=of&v43="of"&v48=size&v49=size&v5=byte&v50=size&v51=size&v52=size&v53="size"&v58=0&v59=0&v6=byte&v60=0&v61="0"&v7="byte") with this warning gives me 8 results, many on totally bug-free code. Fixes generally include tweaking optimization options.

# Action History
- Created by: jeffro256 | 2022-05-09T19:28:47+00:00
- Closed at: 2022-05-27T02:25:45+00:00
