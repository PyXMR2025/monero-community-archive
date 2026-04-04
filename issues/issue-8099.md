---
title: stringop-overflow warning in GCC, when optimization set to '02' or greater
source_url: https://github.com/monero-project/monero/issues/8099
author: who-biz
assignees: []
labels: []
created_at: '2021-11-30T20:26:40+00:00'
updated_at: '2021-12-03T18:24:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When compiling monero, I receive the following warning (along with a range of others for the same `reverse_bytes` function in `portable_binary_archive.hpp`):

```
monero/external/boost/archive/portable_binary_archive.hpp:49:16: warning: writing 1 byte into a region of size 0 [-Wstringop-overflow=]
   49 |         *first = x;
      |         ~~~~~~~^~~
```

Interestingly, this can be fixed by setting in CMake build flags: `set(OPT_FLAGS_RELEASE "-O1")`.. Instead of `-Ofast`, as is the case for my linux build environment.

I am unsure if current implementation of boost's portable archives results in overflow behavior, in practice.

# Discussion History
## moneromooo-monero | 2021-12-03T12:58:03+00:00
I'm reasonably confident your compiler is wrong. My compiler doesn't complain either (GCC 10.3.1). Admittedly the signed char for a size is an interesting choice, but the code looks ok and asan/valgrind don't complain either.

## who-biz | 2021-12-03T18:24:33+00:00
I am using GCC 11.2.  Attempt with a newer version and you'll find the warning to be easily reproduced.

I tried briefly tooling around with code modifications, as I also thought signed/unsigned conversions could be the issue.  Warnings persisted.  Did not spend a lot of time on it, however, so maybe worth a look with a finer comb.

Porting EOS's archives into XMR's codebase did resolve the warnings, but obviously broke backward compatibility with existing archive format.

These files are not included in boost's compiled libraries, and as a result have *not been extensively tested*, according to their historical dev discussions. Since lowering optimization resolves compiler yelling, I am doubtful there is a serious issue here... but I'm really not sure what changes the compiler is making to generate the warning under different O levels.

# Action History
- Created by: who-biz | 2021-11-30T20:26:40+00:00
