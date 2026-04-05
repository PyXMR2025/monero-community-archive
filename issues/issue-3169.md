---
title: '/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:220:18: error: ‘kMinimumDonateLevel’
  was not declared in this scope; did you mean ‘kDonateLevel’?'
source_url: https://github.com/xmrig/xmrig/issues/3169
author: gtxg16
assignees: []
labels:
- invalid
created_at: '2022-11-23T18:13:55+00:00'
updated_at: '2022-12-13T14:13:13+00:00'
type: issue
status: closed
closed_at: '2022-12-13T14:13:13+00:00'
---

# Original Description
**Describe the bug**
Not building
**To Reproduce**
Build latest version of xmrig on ubuntu & set donation level to zero
**Expected behavior**
The build to complete
**Required data**
In file included from /home/dodo/xmrig/src/base/net/stratum/Pools.cpp:32:
/home/dodo/xmrig/src/donate.h:41:1: error: expected ‘,’ or ‘;’ before ‘constexpr’
   41 | constexpr const int kMinimumDonateLevel = 0
      | ^~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp: In member function ‘int xmrig::Pools::donateLevel() const’:
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:76:55: error: invalid use of incomplete type ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
   76 |     return benchSize() || (m_benchmark && !m_benchmark->id().isEmpty()) ? 0 : m_donateLevel;
      |                                                       ^~
In file included from /home/dodo/xmrig/src/base/net/stratum/Pools.h:32,
                 from /home/dodo/xmrig/src/base/net/stratum/Pools.cpp:26:
/home/dodo/xmrig/src/base/net/stratum/Pool.h:37:7: note: forward declaration of ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
   37 | class BenchConfig;
      |       ^~~~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp: In member function ‘void xmrig::Pools::load(const xmrig::IJsonReader&)’:
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:137:61: error: incomplete type ‘xmrig::BenchConfig’ used in nested name specifier
  137 |     m_benchmark = std::shared_ptr<BenchConfig>(BenchConfig::create(reader.getObject(BenchConfig::kBenchmark), reader.getBool("dmi", true)));
      |                                                             ^~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:137:98: error: incomplete type ‘xmrig::BenchConfig’ used in nested name specifier
  137 |     m_benchmark = std::shared_ptr<BenchConfig>(BenchConfig::create(reader.getObject(BenchConfig::kBenchmark), reader.getBool("dmi", true)));
      |                                                                                                  ^~~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp: In member function ‘uint32_t xmrig::Pools::benchSize() const’:
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:171:37: error: invalid use of incomplete type ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
  171 |     return m_benchmark ? m_benchmark->size() : 0;
      |                                     ^~
In file included from /home/dodo/xmrig/src/base/net/stratum/Pools.h:32,
                 from /home/dodo/xmrig/src/base/net/stratum/Pools.cpp:26:
/home/dodo/xmrig/src/base/net/stratum/Pool.h:37:7: note: forward declaration of ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
   37 | class BenchConfig;
      |       ^~~~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp: In member function ‘void xmrig::Pools::toJSON(rapidjson::Value&, rapidjson::Document&) const’:
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:204:46: error: incomplete type ‘xmrig::BenchConfig’ used in nested name specifier
  204 |         out.AddMember(StringRef(BenchConfig::kBenchmark), m_benchmark->toJSON(doc), allocator);
      |                                              ^~~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:204:70: error: invalid use of incomplete type ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
  204 |         out.AddMember(StringRef(BenchConfig::kBenchmark), m_benchmark->toJSON(doc), allocator);
      |                                                                      ^~
In file included from /home/dodo/xmrig/src/base/net/stratum/Pools.h:32,
                 from /home/dodo/xmrig/src/base/net/stratum/Pools.cpp:26:
/home/dodo/xmrig/src/base/net/stratum/Pool.h:37:7: note: forward declaration of ‘using element_type = class xmrig::BenchConfig’ {aka ‘class xmrig::BenchConfig’}
   37 | class BenchConfig;
      |       ^~~~~~~~~~~
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp: In member function ‘void xmrig::Pools::setDonateLevel(int)’:
/home/dodo/xmrig/src/base/net/stratum/Pools.cpp:220:18: error: ‘kMinimumDonateLevel’ was not declared in this scope; did you mean ‘kDonateLevel’?
  220 |     if (level >= kMinimumDonateLevel && level <= 99) {
      |                  ^~~~~~~~~~~~~~~~~~~
      |                  kDonateLevel
make[2]: *** [CMakeFiles/xmrig.dir/build.make:557: CMakeFiles/xmrig.dir/src/base/net/stratum/Pools.cpp.o] Error 1
make[2]: *** Waiting for unfinished jobs....
make[1]: *** [CMakeFiles/Makefile2:158: CMakeFiles/xmrig.dir/all] Error 2
make: *** [Makefile:84: all] Error 2


# Discussion History
## sanderfoobar | 2022-11-23T20:48:23+00:00
Have you tried restarting your computer?

## gtxg16 | 2022-11-23T21:00:52+00:00
It's a variable declaration issue?

## theaog | 2022-11-23T21:58:03+00:00
are you aware that you're asking the developers that work hard on this project to help you remove the reward for their work from their work?

I don't understand if you're stupid or an idiot, maybe both.

props for the audacity though. GG

## gtxg16 | 2022-11-23T22:03:47+00:00
I mean like I could have made a donation to them for making it but you assume I didn't?

I mean I respect that they made it but 1% of everything I ever make is just too much for me 

## gtxg16 | 2022-11-23T22:04:17+00:00
Also it's not uncommon for that to happen

## theaog | 2022-11-23T22:07:14+00:00
this is what you should do: send 1XMR to https://github.com/xmrig/xmrig#donations
then contact @SChernykh, and maybe he'll help you compile.

## gtxg16 | 2022-11-24T16:20:37+00:00
can you just help me please?

## Spudz76 | 2022-11-25T01:32:47+00:00
It literally is telling you what's missing.

`error: expected ‘,’ or ‘;’ before ‘constexpr’`

## theaog | 2022-11-25T12:40:50+00:00
> can you just help me please?

no

# Action History
- Created by: gtxg16 | 2022-11-23T18:13:55+00:00
- Closed at: 2022-12-13T14:13:13+00:00
