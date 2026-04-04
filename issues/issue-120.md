---
title: Build error on Odroid U3 / Arch
source_url: https://github.com/monero-project/monero/issues/120
author: levino
assignees: []
labels: []
created_at: '2014-09-06T19:19:36+00:00'
updated_at: '2015-02-03T18:16:02+00:00'
type: issue
status: closed
closed_at: '2015-02-03T18:16:02+00:00'
---

# Original Description
Hey Guys,

I tried to compile monerod on my Odroid U3 with Ubuntu 14.04. Did not work:

```
mkdir -p build/release
cd build/release && cmake -D CMAKE_BUILD_TYPE=Release ../..
-- Boost version: 1.55.0
-- Found the following Boost libraries:
--   system
--   filesystem
--   thread
--   date_time
--   chrono
--   regex
--   serialization
--   program_options
-- Found Git: /usr/bin/git
-- Configuring done
-- Generating done
-- Build files have been written to: /home/levin/coding/bitmonero/build/release
cd build/release && make
make[1]: Entering directory `/home/levin/coding/bitmonero/build/release'
make[2]: Entering directory `/home/levin/coding/bitmonero/build/release'
make[3]: Entering directory `/home/levin/coding/bitmonero/build/release'
make[3]: Leaving directory `/home/levin/coding/bitmonero/build/release'
make[3]: Entering directory `/home/levin/coding/bitmonero/build/release'
fatal: No names found, cannot describe anything.
CMake Warning at src/version.cmake:3 (message):
  Cannot determine current revision.  Make sure that you are building either
  from a Git working tree or from a source archive.


make[3]: Leaving directory `/home/levin/coding/bitmonero/build/release'
[  0%] Built target version
make[3]: Entering directory `/home/levin/coding/bitmonero/build/release'
make[3]: Leaving directory `/home/levin/coding/bitmonero/build/release'
make[3]: Entering directory `/home/levin/coding/bitmonero/build/release'
[  1%] Building C object external/miniupnpc/CMakeFiles/upnpc-static.dir/igd_desc_parse.c.o
cc: error: unrecognized command line option ‘-maes’
make[3]: *** [external/miniupnpc/CMakeFiles/upnpc-static.dir/igd_desc_parse.c.o] Error 1
make[3]: Leaving directory `/home/levin/coding/bitmonero/build/release'
make[2]: *** [external/miniupnpc/CMakeFiles/upnpc-static.dir/all] Error 2
make[2]: Leaving directory `/home/levin/coding/bitmonero/build/release'
make[1]: *** [all] Error 2
make[1]: Leaving directory `/home/levin/coding/bitmonero/build/release'
make: *** [build-release] Error 2
```

Is there anything I can do? Google did not spit out much for "maes".


# Discussion History
## fluffypony | 2015-02-03T18:16:02+00:00
Finally fixed!!

You may want to wait until we've merged in the blockchainDB work, but it now builds and runs on ARM.

LMDB needs a large MMAP for Monero (16gb, afair), so we are probably going to have BerkleyDB as the next DB implementation, as that will work much better on ARM.


# Action History
- Created by: levino | 2014-09-06T19:19:36+00:00
- Closed at: 2015-02-03T18:16:02+00:00
