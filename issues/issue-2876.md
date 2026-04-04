---
title: Failed to compile on OpenBSD 6.2
source_url: https://github.com/monero-project/monero/issues/2876
author: exquisitus
assignees: []
labels: []
created_at: '2017-11-28T22:05:11+00:00'
updated_at: '2017-12-02T09:16:22+00:00'
type: issue
status: closed
closed_at: '2017-12-02T09:16:22+00:00'
---

# Original Description
I recently upgraded my OpenBSD from 6.1 to 6.2.
Building Boost failed on the last step with
```In file included from ./boost/archive/impl/basic_text_iprimitive.ipp:25:
In file included from ./boost/archive/iterators/remove_whitespace.hpp:21:
./boost/iterator/iterator_adaptor.hpp:311:20: error: type 'super_t' (aka 'int') cannot be used prior to '::' because it has no members
          typename super_t::iterator_category
                   ^
./boost/iterator/iterator_adaptor.hpp:317:29: error: type 'super_t' (aka 'int') cannot be used prior to '::' because it has no members
      void advance(typename super_t::difference_type n)
                            ^
./boost/iterator/iterator_adaptor.hpp:334:16: error: type 'super_t' (aka 'int') cannot be used prior to '::' because it has no members
      typename super_t::difference_type distance_to(
               ^
In file included from libs/serialization/src/basic_text_wiprimitive.cpp:26:
In file included from ./boost/archive/impl/basic_text_iprimitive.ipp:25:
In file included from ./boost/archive/iterators/remove_whitespace.hpp:21:
In file included from ./boost/iterator/iterator_adaptor.hpp:15:
In file included from ./boost/iterator/iterator_facade.hpp:13:
./boost/iterator/iterator_traits.hpp:22:64: error: no type named 'value_type' in 'std::__1::iterator_traits<boost::archive::iterators::binary_from_base64<boost::archive::iterators::remove_whitespace<boost::archive::iterators::istream_iterator<wchar_t> >, int> >'
    typedef typename boost::detail::iterator_traits<Iterator>::value_type type;
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
./boost/archive/iterators/transform_width.hpp:64:22: note: in instantiation of template class 'boost::iterators::iterator_value<boost::archive::iterators::binary_from_base64<boost::archive::iterators::remove_whitespace<boost::archive::iterators::istream_iterator<wchar_t> >, int> >' requested here
    typedef typename iterator_value<Base>::type base_value_type;
                     ^
./boost/archive/impl/basic_text_iprimitive.ipp:87:16: note: in instantiation of template class 'boost::archive::iterators::transform_width<boost::archive::iterators::binary_from_base64<boost::archive::iterators::remove_whitespace<boost::archive::iterators::istream_iterator<wchar_t> >, int>, 8, 6, wchar_t>' requested here
    binary i = binary(iterators::istream_iterator<CharType>(is));
               ^
libs/serialization/src/basic_text_wiprimitive.cpp:31:16: note: in instantiation of member function 'boost::archive::basic_text_iprimitive<std::__1::basic_istream<wchar_t> >::load_binary' requested here
template class basic_text_iprimitive<std::wistream> ;
               ^
13 errors generated.
...skipped <pbin.v2/libs/serialization/build/clang-linux-4.0.0/release/link-static/threading-multi>libboost_wserialization-mt.a(clean) for lack of <pbin.v2/libs/serialization/build/clang-linux-4.0.0/release/link-static/threading-multi>basic_text_wiprimitive.o...
...skipped <pbin.v2/libs/serialization/build/clang-linux-4.0.0/release/link-static/threading-multi>libboost_wserialization-mt.a for lack of <pbin.v2/libs/serialization/build/clang-linux-4.0.0/release/link-static/threading-multi>basic_text_wiprimitive.o...
...skipped <p/usr/local/lib>libboost_wserialization-mt.a for lack of <pbin.v2/libs/serialization/build/clang-linux-4.0.0/release/link-static/threading-multi>libboost_wserialization-mt.a...
...failed updating 1 target...
```

Cppzmq failed with
```
~/cppzmq/cppzmq-4.2.2/build# cmake ..
CMake Warning at CMakeLists.txt:4 (find_package):
  By not providing "FindZeroMQ.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "ZeroMQ", but
  CMake did not find one.

  Could not find a package configuration file provided by "ZeroMQ" with any
  of the following names:

    ZeroMQConfig.cmake
    zeromq-config.cmake

  Add the installation prefix of "ZeroMQ" to CMAKE_PREFIX_PATH or set
  "ZeroMQ_DIR" to a directory containing one of the above files.  If "ZeroMQ"
  provides a separate development package or SDK, be sure it has been
  installed.


CMake Error at CMakeLists.txt:12 (message):
  ZeroMQ was NOT found!

-- Configuring incomplete, errors occurred!
```

But I have installed zeromq with pkg_add according to the instructions
```#  pkg_info -e 'zeromq->=4'
inst:zeromq-4.1.4p0
```

# Discussion History
## ston1th | 2017-11-29T10:56:08+00:00
Hi

For cppzmq there is a PR with a fix: https://github.com/monero-project/monero/pull/2854
Simply this command: `doas ln -s /usr/local/lib/libzmq.so.4.1 /usr/local/lib/libzmq.so`

I built my boost version on a new plain install of OpenBSD 6.2.
I haven't testet an upgrade from 6.1 to 6.2, so maybe the upgrade is causing the problem.

## moneromooo-monero | 2017-12-02T09:12:54+00:00
+resolved

# Action History
- Created by: exquisitus | 2017-11-28T22:05:11+00:00
- Closed at: 2017-12-02T09:16:22+00:00
