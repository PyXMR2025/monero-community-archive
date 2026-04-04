---
title: Errors with static linking on CentOS
source_url: https://github.com/monero-project/monero/issues/6792
author: sn1f3rt
assignees: []
labels: []
created_at: '2020-09-01T08:43:54+00:00'
updated_at: '2021-10-06T03:12:25+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:12:25+00:00'
---

# Original Description
Hello. 

I'm using CentOS 8 at the moment, with all necessary dependencies installed. However, I'm not being able to create a static release (normal build or dynamic linking is working though). 

Here is the error:

```css
(.text._ZNK5boost6locale8impl_icu13number_formatIwE8do_parseIdEEmR
KNSt7__cxx1112basic_stringIwSt11char_traitsIwESaIwEEERT_[_ZNK5boos
t6locale8impl_icu13number_formatIwE8do_parseIdEEmRKNSt7__cxx1112ba
sic_stringIwSt11char_traitsIwESaIwEEERT_]+0x1ad): undefined refere
nce to `icu_60::UnicodeString::~UnicodeString()'                  
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libboost_loca
le.a(time_zone.o): In function `boost::locale::impl_icu::get_time_
zone(std::__cxx11::basic_string<char, std::char_traits<char>, std:
:allocator<char> > const&)':                                      
(.text+0x22): undefined reference to `icu_60::TimeZone::createDefa
ult()'                                                            
(.text+0x4c): undefined reference to `icu_60::UnicodeString::Unico
deString(char const*)'                                            
(.text+0x54): undefined reference to `icu_60::TimeZone::createTime
Zone(icu_60::UnicodeString const&)'                               
(.text+0x61): undefined reference to `icu_60::UnicodeString::~Unic
odeString()'                                                      
/usr/lib/gcc/x86_64-redhat-linux/8/../../../../lib64/libboost_loca
le.a(time_zone.o): In function `boost::locale::impl_icu::get_time_
zone(std::__cxx11::basic_string<char, std::char_traits<char>, std:
:allocator<char> > const&) [clone .cold.2]':                      
(.text.unlikely[.text.unlikely..group]+0x4): undefined reference t
o `icu_60::UnicodeString::~UnicodeString()'                       
collect2: error: ld returned 1 exit status                        
make[3]: *** [src/simplewallet/CMakeFiles/simplewallet.dir/build.m
ake:139: bin/monero-wallet-cli] Error 1                           
make[3]: Leaving directory '/root/monero/build/Linux/master/releas
e'                                                                
make[2]: *** [CMakeFiles/Makefile2:3625: src/simplewallet/CMakeFil
es/simplewallet.dir/all] Error 2                                  
make[2]: Leaving directory '/root/monero/build/Linux/master/releas
e'                                                                
make[1]: *** [Makefile:141: all] Error 2                          
make[1]: Leaving directory '/root/monero/build/Linux/master/releas
e'                                                                
make: *** [Makefile:107: release-static] Error 2
```
As a side note, this happens at 93% of the build, after `monero-wallet-cli` is built. Could anyone please assist me in this issue?

# Discussion History
## moneromooo-monero | 2020-09-01T14:35:59+00:00
Do you have more than one version of boost installed ?

## sn1f3rt | 2020-09-01T17:10:48+00:00
Well yeah I did have a conflicting version of boost. That is because a mixture of deps got pulled in from both PowerTools and Okay repos. But even after fixing the version-

```css
[root@ip147 xolentum]# dnf list installed | grep boost
boost.x86_64                                1.66.0-6.el8                               @okay
boost-atomic.x86_64                         1.66.0-6.el8                               @okay
boost-chrono.x86_64                         1.66.0-6.el8                               @okay
boost-container.x86_64                      1.66.0-6.el8                               @okay
boost-context.x86_64                        1.66.0-6.el8                               @okay
boost-coroutine.x86_64                      1.66.0-6.el8                               @okay
boost-date-time.x86_64                      1.66.0-6.el8                               @okay
boost-devel.x86_64                          1.66.0-6.el8                               @okay
boost-fiber.x86_64                          1.66.0-6.el8                               @okay
boost-filesystem.x86_64                     1.66.0-6.el8                               @okay
boost-graph.x86_64                          1.66.0-6.el8                               @okay
boost-iostreams.x86_64                      1.66.0-6.el8                               @okay
boost-locale.x86_64                         1.66.0-6.el8                               @okay
boost-log.x86_64                            1.66.0-6.el8                               @okay
boost-math.x86_64                           1.66.0-6.el8                               @okay
boost-program-options.x86_64                1.66.0-6.el8                               @okay
boost-random.x86_64                         1.66.0-6.el8                               @okay
boost-regex.x86_64                          1.66.0-6.el8                               @okay
boost-serialization.x86_64                  1.66.0-6.el8                               @okay
boost-signals.x86_64                        1.66.0-6.el8                               @okay
boost-stacktrace.x86_64                     1.66.0-6.el8                               @okay
boost-static.x86_64                         1.66.0-6.el8                               @okay
boost-system.x86_64                         1.66.0-6.el8                               @okay
boost-test.x86_64                           1.66.0-6.el8                               @okay
boost-thread.x86_64                         1.66.0-6.el8                               @okay
boost-timer.x86_64                          1.66.0-6.el8                               @okay
boost-type_erasure.x86_64                   1.66.0-6.el8                               @okay
boost-wave.x86_64                           1.66.0-6.el8                               @okay
```
- the same error is persisting. Any ideas?

## moneromooo-monero | 2020-09-01T20:23:05+00:00
make clean, and make sure you remove any cmake cache.


## sn1f3rt | 2020-09-02T07:24:08+00:00
No luck doing that. Even on a fresh clone, I'm getting the same error. I guess `libicu` installation shouldn't be the problem here.

```css
[root@ip147 monero]# dnf list installed | grep icu                              
libicu.x86_64                               60.3-2.el8_1                        
       @BaseOS                                                                  
libicu-devel.x86_64                         60.3-2.el8_1                        
       @BaseOS
```

## ghost | 2020-09-02T15:09:08+00:00
there isn't a libicu-static package which would include the libicu.a which you would need for a static link.

in this case libicu-devel does not provide libicu.a - from the 'icu.spec' file in the srpm:

* Sun Jul 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 3.4-0.2.d02
- 3.4-d02.
- Don't ship static libraries.

so it looks like we'd have to build our own static library in the centos 8/rhel 8 case


## sn1f3rt | 2020-09-02T16:33:49+00:00
Oh okay, I'll try that then.

# Action History
- Created by: sn1f3rt | 2020-09-01T08:43:54+00:00
- Closed at: 2021-10-06T03:12:25+00:00
