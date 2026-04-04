---
title: recipe for target contrib/epee/src/libepee.a failed
source_url: https://github.com/monero-project/monero/issues/1704
author: ghost
assignees: []
labels: []
created_at: '2017-02-09T21:57:51+00:00'
updated_at: '2017-02-09T23:37:24+00:00'
type: issue
status: closed
closed_at: '2017-02-09T23:37:24+00:00'
---

# Original Description
Building from latest head (`99ee3fd`) with Ubuntu 16.04, GCC 5.4.1, ARMv8. Weirdness.

```
[  7%] Linking CXX static library libepee.a
Error running link command: No such file or directory
contrib/epee/src/CMakeFiles/epee.dir/build.make:120: recipe for target 'contrib/epee/src/libepee.a' failed
make[3]: *** [contrib/epee/src/libepee.a] Error 2
make[3]: Leaving directory '/home/nodey/monero/build/release'
CMakeFiles/Makefile2:281: recipe for target 'contrib/epee/src/CMakeFiles/epee.dir/all' failed
make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/monero/build/release'
Makefile:138: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/nodey/monero/build/release'
Makefile:51: recipe for target 'release' failed
make: *** [release] Error 2
```

# Discussion History
## ghost | 2017-02-09T22:10:33+00:00
Ok...I just fixed this with `sudo apt-get --reinstall install gcc-5` followed by the same for `g++-5`.

Why?

## moneromooo-monero | 2017-02-09T22:48:15+00:00
Parallel make with bad dependencies maybe ?

## ghost | 2017-02-09T23:37:24+00:00
Probably. I just wanted to log it in case it turned up for anyone else. Closing now.

# Action History
- Created by: ghost | 2017-02-09T21:57:51+00:00
- Closed at: 2017-02-09T23:37:24+00:00
