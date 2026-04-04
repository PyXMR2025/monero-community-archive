---
title: Fail to compile v0.11.0
source_url: https://github.com/monero-project/monero/issues/2444
author: cslashm
assignees: []
labels: []
created_at: '2017-09-13T13:21:10+00:00'
updated_at: '2017-09-25T20:30:23+00:00'
type: issue
status: closed
closed_at: '2017-09-25T20:30:23+00:00'
---

# Original Description
0.10.3 compile correctly but 0.11.0 fails. Can Someone help me? 
I attached make ouput log and my config is is:

[make.log.zip](https://github.com/monero-project/monero/files/1299517/make.log.zip)

gcc version

    gcc (Ubuntu 6.2.0-5ubuntu12) 6.2.0 20161005

platform     

    Linux Lulu 4.8.0-59-generic #64-Ubuntu SMP Thu Jun 29 19:38:34 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux

Packages:

    Name                   Version                Description
    ======================-======================-==================================================================
    build-essential        12.1ubuntu2            Informational list of build-essential packages
    cmake                  3.5.2-2ubuntu1         cross-platform, open-source make system
    doxygen                1.8.11-3               Documentation system for C, C++, Java, Python and other languages
    graphviz               2.38.0-15ubuntu1.1     rich set of graph drawing tools
    libboost-all-dev       1.61.0.2               Boost C++ Libraries development files (ALL) (default version)
    libexpat1-dev:amd64    2.2.0-1ubuntu0.1       XML parsing C library - development kit
    libgtest-dev:amd64     1.7.0-4ubuntu1         Google's framework for writing C++ tests - header files
    libldns-dev:amd64      1.6.17-9               ldns library for DNS programming
    liblzma-dev:amd64      5.1.1alpha+20120614-2  XZ-format compression library - development files
    libssl-dev:amd64       1.0.2g-1ubuntu9.3      Secure Sockets Layer toolkit - development files
    libunbound-dev:amd64   1.5.8-1ubuntu1         static library, header files, and docs for libunbound
    libunwind8-dev         1.1-4.1ubuntu2         library to determine the call-chain of a program - development

    libminiupnpc-dev  vendored




# Discussion History
## moneromooo-monero | 2017-09-13T15:00:29+00:00
Do you have another build tree of boost accessible to cmake ?

If not, you might want to try an older version of boost.


## cslashm | 2017-09-13T16:13:09+00:00
I have only this one installed. I 'll try 1.58 as said in readme.
boost is definitively a nightmare! 


## AJIekceu4 | 2017-09-14T08:25:30+00:00
Same problem with libboost-all-dev 1.61.0.2 and Ubuntu, after installing libboost1.60-all-dev (1.60.0+dfsg-6) another error:

> [ 63%] Linking CXX executable coretests
> ../../src/common/libcommon.a(download.cpp.o): In function `__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > boost::re_detail_106000::re_is_set_member<__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, char, boost::regex_traits<char, boost::cpp_regex_traits<char> >, unsigned int>(__gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, __gnu_cxx::__normal_iterator<char const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, boost::re_detail_106000::re_set_long<unsigned int> const*, boost::re_detail_106000::regex_data<char, boost::regex_traits<char, boost::cpp_regex_traits<char> > > const&, bool)':
> download.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x17a): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform_primary[abi:cxx11](char const*, char const*) const'
> download.cpp:(.text._ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb[_ZN5boost16re_detail_10600016re_is_set_memberIN9__gnu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEEcNS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEjEET_SH_SH_PKNS0_11re_set_longIT2_EERKNS0_10regex_dataIT0_T1_EEb]+0x354): undefined reference to `boost::re_detail_106000::cpp_regex_traits_implementation<char>::transform[abi:cxx11](char const*, char const*) const'
> collect2: error: ld returned 1 exit status
> tests/core_tests/CMakeFiles/coretests.dir/build.make:458: recipe for target 'tests/core_tests/coretests' failed
> make[3]: *** [tests/core_tests/coretests] Error 1
> make[3]: Leaving directory '/monero/monero/build/release'
> CMakeFiles/Makefile2:2264: recipe for target 'tests/core_tests/CMakeFiles/coretests.dir/all' failed
> make[2]: *** [tests/core_tests/CMakeFiles/coretests.dir/all] Error 2
> make[2]: Leaving directory '/monero/monero/build/release'
> Makefile:138: recipe for target 'all' failed
> make[1]: *** [all] Error 2
> make[1]: Leaving directory '/monero/monero/build/release'
> Makefile:62: recipe for target 'release-all' failed
> make: *** [release-all] Error 2

After this i download and compile boost_1_58_0 manually and monero compiled without error from src.

## cslashm | 2017-09-14T09:54:16+00:00
I succeeded to compile it.

1. I removed all system boost package with apt-get

2. I downloaded boost 1.58 (the version listed in Readme.md)
https://sourceforge.net/projects/boost/files/boost/1.58.0/
and install it:

        ./bootstrap.sh --prefix=/opt/boost/boost1.58
        ./b2
         sudo ./b2 install

3. I setup those variables. Some of them may not needed, this setup is the incremental result....:

        declare -x Boost_NO_SYSTEM_PATHS="1"
        declare -x BOOST_ROOT="/opt/boost/boost1.58"
        declare -x DT_RUNPATH="/opt/boost/boost1.58/lib"
        declare -x LD_LIBRARY_PATH="/opt/boost/boost1.58/lib"
        declare -x LIBRARY_PATH="/opt/boost/boost1.58/lib"

4. in monero dir, just run 

        make clean
        make  

If something still goes wrong, add "set(CMAKE_VERBOSE_MAKEFILE ON)" in root CMakeLists.txt to get executed command lines.


## moneromooo-monero | 2017-09-18T10:29:58+00:00
https://github.com/monero-project/monero/pull/2466

## moneromooo-monero | 2017-09-22T17:31:36+00:00
> Same problem with libboost-all-dev 1.61.0.2 and Ubuntu, after installing libboost1.60-all-dev (1.60.0+dfsg-6) another error:

FWIW, I am using boost 1.60.0 on one of my VMs, and it builds fine.


## diederikdehaas | 2017-09-24T01:00:39+00:00
Also FWIW, I have successfully compiled v0.11.0.0 on a 64-bit Debian Stretch system with boost 1.62.0.1

## moneromooo-monero | 2017-09-25T20:25:20+00:00
+resolved

# Action History
- Created by: cslashm | 2017-09-13T13:21:10+00:00
- Closed at: 2017-09-25T20:30:23+00:00
