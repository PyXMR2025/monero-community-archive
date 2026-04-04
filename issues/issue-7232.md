---
title: Fuzz test memory exhaustion
source_url: https://github.com/monero-project/monero/issues/7232
author: unseddd
assignees: []
labels: []
created_at: '2020-12-30T02:47:16+00:00'
updated_at: '2021-01-16T04:51:34+00:00'
type: issue
status: closed
closed_at: '2021-01-16T04:51:34+00:00'
---

# Original Description
During fuzz testing, I ran into a problem of all available RAM and swap space being exhausted by the build.

The problem seems to come from the [chaingen_main](https://github.com/monero-project/monero/blob/master/tests/core_tests/chaingen_main.cpp) core tests.

Maybe related to #7186 and #7225

The kind of hacky workaround I used was to disable all builds of non-fuzz tests in the `tests/CMakeLists.txt` build file.

Something like:

```
if (FUZZ || OSS_FUZZ)
  add_subdirectory(fuzz)
else()
  add_subdirectory(core_tests)
  add_subdirectory(crypto)
  add_subdirectory(functional_tests)
  add_subdirectory(performance_tests)
  add_subdirectory(core_proxy)
  add_subdirectory(unit_tests)
  add_subdirectory(difficulty)
  add_subdirectory(block_weight)
  add_subdirectory(hash)
  add_subdirectory(net_load_tests)
endif()
```

Only including fuzz tests in a fuzz build is likely a good idea anyway, since it will decrease overall build time, and none of the other tests need to be instrumented by `AFL`/`libFuzzer` anyways.

# Discussion History
## moneromooo-monero | 2020-12-30T15:02:23+00:00
make -C build/..../fuzz  fuzz_tests

## unseddd | 2020-12-30T23:01:02+00:00
> make -C build/..../fuzz fuzz_tests

I don't understand how that solves the problem, the memory exhaustion occurs during first build. Before there is even a `build/...` dir to change into. 

## moneromooo-monero | 2020-12-30T23:31:20+00:00
That builds just the fuzz tests, not core_tests, which is one of the memory hungry things.

Or did I misunderstand and It somehow OOMs during the preliminary cmake pass ?


## unseddd | 2020-12-30T23:55:10+00:00
> That builds just the fuzz tests, not core_tests, which is one of the memory hungry things.

Ah, ok. I'll try it out, and close the issue if changing dir works.

## unseddd | 2020-12-31T00:15:00+00:00
So, `make -C build/..../fuzz fuzz_tests` will only work with an existing build directory. Users would need a prior build, or manually make the full build path (e.g. build/Windows/master) and cmake.

The conditional build change to `tests/CMakeLists.txt` I suggested allows users to just run `make fuzz`, without having to do all the manual stuff, or have a prior build (which is the problem to begin with).

## moneromooo-monero | 2020-12-31T00:47:40+00:00
You just need the initial cmake step, then make -C to build whatever you want. Building tests with ASAN is definitely useful, I do it from tme to time.

## unseddd | 2020-12-31T09:02:23+00:00
> You just need the initial cmake step, then make -C to build whatever you want.

I was hoping to avoid the extra manual step, since it would also require manually tracking any cmake changes in the fuzz build, adds complexity, is annoying, etc.

> Building tests with ASAN is definitely useful, I do it from tme to time.

Definitely agree. I think that's more a case for a `test-asan` make option or similar. Using the fuzz build for that purpose adds a lot of extra instrumentation from the `afl-*` compiler tools.

## moneromooo-monero | 2020-12-31T17:27:40+00:00
Ah, in that case then splitting and restricting to fuzz tests seems like a good idea indeed.

# Action History
- Created by: unseddd | 2020-12-30T02:47:16+00:00
- Closed at: 2021-01-16T04:51:34+00:00
