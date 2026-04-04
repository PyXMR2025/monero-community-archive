---
title: ASAP undefined reference to `boost::this_thread::hidden::sleep_until(timespec
  const&)'
source_url: https://github.com/monero-project/monero/issues/4963
author: yolihavim
assignees: []
labels:
- invalid
created_at: '2018-12-09T15:10:41+00:00'
updated_at: '2019-03-21T13:41:47+00:00'
type: issue
status: closed
closed_at: '2019-03-21T13:41:47+00:00'
---

# Original Description
The same error as in #4051, but I couldn't make it work.

After running make it returns me the following error

```
[ 80%] Built target obj_daemonizer
[ 81%] Linking CXX static library libdaemonizer.a
[ 81%] Built target daemonizer
[ 82%] Building CXX object src/wallet/CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o
warning: unknown warning option '-Wlogical-op'; did you mean '-Wliblto'? [-Wunknown-warning-option]
warning: unknown warning option '-Werror=maybe-uninitialized'; did you mean '-Werror=uninitialized'? [-Wunknown-warning-option]
warning: unknown warning option '-Werror=cpp' [-Wunknown-warning-option]
3 warnings generated.
[ 83%] Linking CXX executable ../../bin/monero-wallet-rpc
CMakeFiles/wallet_rpc_server.dir/wallet_rpc_server.cpp.o: In function `boost::re_detail_106400::perl_matcher<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > >, boost::regex_traits<char, boost::cpp_regex_traits<char> > >::perl_matcher(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::match_results<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<boost::sub_match<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > > > >&, boost::basic_regex<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, boost::regex_constants::_match_flags, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >)':
....
....
...

../cryptonote_basic/libcryptonote_basic.a(miner.cpp.o): In function `cryptonote::miner::worker_thread()':
/home/monero/src/cryptonote_basic/miner.cpp:(.text+0x3857): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
/home/monero/src/cryptonote_basic/miner.cpp:(.text+0x38c5): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
/home/monero/src/cryptonote_basic/miner.cpp:(.text+0x3f38): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
../../contrib/epee/src/libepee.a(connection_basic.cpp.o): In function `epee::net_utils::connection_basic::sleep_before_packet(unsigned long, int, int)':
/home/monero/contrib/epee/src/connection_basic.cpp:(.text+0x17b4): undefined reference to `boost::this_thread::hidden::sleep_until(timespec const&)'
clang: error: linker command failed with exit code 1 (use -v to see invocation)
src/wallet/CMakeFiles/wallet_rpc_server.dir/build.make:125: recipe for target 'bin/monero-wallet-rpc' failed
make[2]: *** [bin/monero-wallet-rpc] Error 1
CMakeFiles/Makefile2:2301: recipe for target 'src/wallet/CMakeFiles/wallet_rpc_server.dir/all' failed
make[1]: *** [src/wallet/CMakeFiles/wallet_rpc_server.dir/all] Error 2

```

I downloaded boot_1_66_0 
```
cd /usr/local/boost_1_66_0
./bootstrap.sh
./b2 
export BOOST_ROOT=/usr/local/boost_1_66_0

```
`echo $BOOST_ROOT`
`/usr/local/boost_1_66_0`

but still, it returns me the same error.

Any idea? I need help ASAP



# Discussion History
## moneromooo-monero | 2018-12-09T15:33:39+00:00
> echo $BOOST_ROOT
> /usr/loca/boost_1_66_0


You want local, not loca.


## yolihavim | 2018-12-09T16:08:58+00:00
> > echo $BOOST_ROOT
> > /usr/loca/boost_1_66_0
> 
> You want local, not loca.

sorry, it was a typo in my github comment. It still doesn't work

## moneromooo-monero | 2018-12-09T16:45:09+00:00
Are you sure you're not using two boost libs ?

## yolihavim | 2018-12-09T16:46:32+00:00
there is a chance i have two boost libs. But I don't uninstall it. 

## moneromooo-monero | 2018-12-09T16:49:29+00:00
just to make sure: make clean

Then check boost paths in build/release/CMakeCache.txt

If they don't all point to your new version, fix that first.


## yolihavim | 2018-12-09T17:00:40+00:00
Thanks so much for your help. I did run everytime make clean, and then make and still have the same error.
I couldn't find the path or anything related to boost in build/release/CMakeCache.txt



## ghost | 2018-12-09T19:40:05+00:00
Did you follow all the instructions under https://github.com/monero-project/monero#note-for-raspbian-jessie-users ? (Change 1.64 for 1.66 obviously)

This includes removing your previous version of boost, building from source, and installing the new version.

## moneromooo-monero | 2019-03-21T13:27:13+00:00
No further comments, and I'm pretty sure it's a user configuration problem, so closing.

+invalid

# Action History
- Created by: yolihavim | 2018-12-09T15:10:41+00:00
- Closed at: 2019-03-21T13:41:47+00:00
