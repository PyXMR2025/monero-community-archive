---
title: GCC 6.1 compilation errors
source_url: https://github.com/monero-project/monero/issues/834
author: moneroexamples
assignees: []
labels: []
created_at: '2016-05-08T04:56:48+00:00'
updated_at: '2021-12-28T14:19:54+00:00'
type: issue
status: closed
closed_at: '2016-06-20T06:47:55+00:00'
---

# Original Description
Arch Linux just upgrade GCC 5.3 to 6.1. With this change, Monero no longer compiles. Compilation fails for the following errors:
#### 1. error: value-initialization of incomplete type

```
/home/mwo/bitmonero/src/crypto/crypto.cpp:275:58: error: value-initialization of incomplete type ‘crypto::rs_comm::<anonymous struct> []’
     return sizeof(rs_comm) + pubs_count * sizeof(rs_comm().ab[0]);
```

This can be fixed by changing

```
return sizeof(rs_comm) + pubs_count * sizeof(rs_comm().ab[0]);
```

into equivalent expression of

```
return sizeof(rs_comm) + pubs_count * 2 * sizeof(ec_point);
```
#### 2. error: throw will always call terminate()

```
 /home/mwo/bitmonero/contrib/epee/include/misc_log_ex.h:1430:130: error: throw will always call terminate() [-Werror=terminate]
 e) {LOG_ERROR(message); std::stringstream ss; ss << message; throw std::runtime_error(ss.str());}
```

This can be fixed by compiling as follows:

```
make CXXFLAGS='-Wno-error=terminate'
```
#### 3. undefined reference to boost::re_detail

```
[ 40%] Linking CXX executable ../../bin/simpleminer
/tmp/cc2gv4GN.ltrans18.ltrans.o: In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106000::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106000::re_set_long<unsigned int> const*, boost::re_detail_106000::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
<artificial>:(.text+0xc4a): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
<artificial>:(.text+0xe5d): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
collect2: error: ld returned 1 exit status
src/miner/CMakeFiles/simpleminer.dir/build.make:121: recipe for target 'bin/simpleminer' failed
```

This I dont know how to fix. `boost_regex` is correctly installed for sure. Maybe there are some ABI differences with gcc 6 as compared to 5.3, but did not manage to pin them down and go past this error.

Maybe someone else will have more luck?


# Discussion History
## moneroexamples | 2016-05-15T07:29:28+00:00
Arch updated boost libraries, so there is no problem: 3. undefined reference to boost::re_detail

Problem 1 remains. 

Problem 2 is extended and can be fixed by compiling as follow

```
make CXXFLAGS='-Wno-error=terminate -Wno-error=misleading-indentation'
```


## daniellockyer | 2016-06-19T23:12:55+00:00
This should be closed now :) cc @fluffypony 


## sarp07 | 2021-12-28T14:18:25+00:00
Hello guys,


-- Configuring done
-- Generating done
-- Build files have been written to: /home/bitrabit/cryptonote/build/release
cd build/release && make
make[1]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[2]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
fatal: No names found, cannot describe anything.
CMake Warning at src/version.cmake:3 (message):
  Cannot determine current revision.  Make sure that you are building either
  from a Git working tree or from a source archive.


make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[  0%] Built target version
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[  5%] Built target upnpc-static
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[  6%] Built target gtest
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[  6%] Built target gtest_main
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 10%] Built target P2P
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 11%] Built target NodeRpcProxy
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 12%] Built target InProcessNode
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 15%] Built target Logging
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 18%] Built target Serialization
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 25%] Built target Common
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 31%] Built target Crypto
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 33%] Built target Http
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 34%] Built target BlockchainExplorer
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 43%] Built target CryptoNoteCore
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 48%] Built target System
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 50%] Built target Rpc
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 51%] Built target Daemon
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 53%] Built target Transfers
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 58%] Built target Wallet
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 59%] Built target SimpleWallet
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 61%] Built target PaymentGate
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 62%] Built target JsonRpcServer
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 62%] Built target ConnectivityTool
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 64%] Built target PaymentGateService
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 66%] Built target Miner
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 66%] Built target HashTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 66%] Built target DifficultyTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 68%] Built target CryptoTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 69%] Built target PerformanceTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 71%] Built target IntegrationTestLibrary
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 73%] Built target IntegrationTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 74%] Built target TestGenerator
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 88%] Built target UnitTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 93%] Built target CoreTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 93%] Built target NodeRpcProxyTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 98%] Built target SystemTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[ 99%] Built target HashTargetTests
make[3]: Entering directory '/home/bitrabit/cryptonote/build/release'
make[3]: Leaving directory '/home/bitrabit/cryptonote/build/release'
[100%] Built target TransfersTests
make[2]: Leaving directory '/home/bitrabit/cryptonote/build/release'
make[1]: Leaving directory '/home/bitrabit/cryptonote/build/release'

I saw these errors.

## selsta | 2021-12-28T14:19:54+00:00
@sarp07 make sure to correctly clone the repository with git

# Action History
- Created by: moneroexamples | 2016-05-08T04:56:48+00:00
- Closed at: 2016-06-20T06:47:55+00:00
