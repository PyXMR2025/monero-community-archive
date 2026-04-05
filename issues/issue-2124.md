---
title: make command issues on ubuntu
source_url: https://github.com/xmrig/xmrig/issues/2124
author: fgsoftware1
assignees: []
labels: []
created_at: '2021-02-22T04:37:41+00:00'
updated_at: '2021-10-31T21:05:27+00:00'
type: issue
status: closed
closed_at: '2021-02-22T04:48:51+00:00'
---

# Original Description
Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:62: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o' failed
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
CMakeFiles/Makefile2:178: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/all' failed
make[1]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2

# Discussion History
## fgsoftware1 | 2021-02-22T04:48:44+00:00
> Building C object src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o
> cc: error: unrecognized command line option '-maes'; did you mean '-mapcs'?
> src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:62: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o' failed
> make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/ethash_internal.c.o] Error 1
> CMakeFiles/Makefile2:178: recipe for target 'src/3rdparty/libethash/CMakeFiles/ethash.dir/all' failed
> make[1]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
> Makefile:83: recipe for target 'all' failed
> make: *** [all] Error 2

I resolved this issue.
the issue is the flag -maes this flag need remove on arm devices

## Mertenrobson | 2021-10-31T21:05:27+00:00
Linking C static library libethash.a
Error running link command: No such file or directory
make[2]: *** [src/3rdparty/libethash/CMakeFiles/ethash.dir/build.make:114: src/3rdparty/libethash/libethash.a] Error 2
make[1]: *** [CMakeFiles/Makefile2:171: src/3rdparty/libethash/CMakeFiles/ethash.dir/all] Error 2
make: *** [Makefile:91: all] Error 2

# Action History
- Created by: fgsoftware1 | 2021-02-22T04:37:41+00:00
- Closed at: 2021-02-22T04:48:51+00:00
