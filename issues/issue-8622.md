---
title: '''make debug'' fails'
source_url: https://github.com/monero-project/monero/issues/8622
author: gus4rs
assignees: []
labels:
- bug
created_at: '2022-10-23T14:05:56+00:00'
updated_at: '2024-01-18T23:07:23+00:00'
type: issue
status: closed
closed_at: '2024-01-18T23:07:23+00:00'
---

# Original Description

```make debug``` in ```tag: v0.18.1.1```, same for ```tag: v0.18.1.2```

```
[ 31%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee.dir/int-util.cpp.o
[ 31%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee.dir/portable_storage.cpp.o
In file included from /home/monero/contrib/epee/src/portable_storage.cpp:35:
/home/monero/contrib/epee/include/storages/portable_storage_from_bin.h: In member function ‘epee::serialization::storage_entry epee::serialization::throwable_buffer_reader::load_storage_entry()’:
/home/monero/contrib/epee/include/storages/portable_storage_from_bin.h:322:5: error: control reaches end of non-void function [-Werror=return-type]
  322 |     }
      |     ^
/home/monero/contrib/epee/include/storages/portable_storage_from_bin.h: In member function ‘epee::serialization::storage_entry epee::serialization::throwable_buffer_reader::load_storage_array_entry(uint8_t)’:
/home/monero/contrib/epee/include/storages/portable_storage_from_bin.h:231:5: error: control reaches end of non-void function [-Werror=return-type]
  231 |     }
      |     ^
cc1plus: some warnings being treated as errors
make[3]: *** [contrib/epee/src/CMakeFiles/obj_epee.dir/build.make:356: contrib/epee/src/CMakeFiles/obj_epee.dir/portable_storage.cpp.o] Error 1
make[3]: Leaving directory '/home/monero/build/Linux/_HEAD_detached_at_v0.18.1.1_/debug'
make[2]: *** [CMakeFiles/Makefile2:1496: contrib/epee/src/CMakeFiles/obj_epee.dir/all] Error 2
make[2]: Leaving directory '/home/monero/build/Linux/_HEAD_detached_at_v0.18.1.1_/debug'
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/monero/build/Linux/_HEAD_detached_at_v0.18.1.1_/debug'
make: *** [Makefile:58: debug] Error 2
```


# Discussion History
## selsta | 2022-10-24T14:57:02+00:00
Which compiler version are you using?

## hyc | 2022-10-24T15:08:35+00:00
Technically the compiler is correct, the functions in question end without a "return blah" value. But that's because there's just a switch() statement in the body, and all valid cases return a value, and the default case does an assert/throw, so execution will never reach the end of the functions. But maybe could add in a dummy return statement just to shut the compiler up.

## gus4rs | 2022-10-24T17:37:30+00:00
gcc (GCC) 12.2.1 20220819 (Red Hat 12.2.1-2)

## gus4rs | 2022-10-24T17:46:45+00:00
This error was explicitly enabled about 2 years ago in https://github.com/monero-project/monero/blame/master/CMakeLists.txt#L898-L899


I wonder why I am the only one catching this since I am not doing anything special, only a ```make debug```



## One-horse-wagon | 2022-10-24T21:33:05+00:00
I used Arch Linux with the latest dependencies and Boost.  If you run just "make", the program works fine and monero is successfully built.  If you run "make debug", it hangs with the same type errors in that some warnings are treated as errors.   I did this twice to confirm.

cc1plus: some warnings being treated as errors
make[3]: *** [contrib/epee/src/CMakeFiles/obj_epee.dir/build.make:356: contrib/epee/src/CMakeFiles/obj_epee.dir/portable_storage.cpp.o] Error 1
make[3]: Leaving directory '/home/one-horse-wagon/monero/build/Linux/release-v0.18/debug'
make[2]: *** [CMakeFiles/Makefile2:1496: contrib/epee/src/CMakeFiles/obj_epee.dir/all] Error 2
make[2]: Leaving directory '/home/one-horse-wagon/monero/build/Linux/release-v0.18/debug'
make[1]: *** [Makefile:146: all] Error 2
make[1]: Leaving directory '/home/one-horse-wagon/monero/build/Linux/release-v0.18/debug'
make: *** [Makefile:58: debug] Error 2


# Action History
- Created by: gus4rs | 2022-10-23T14:05:56+00:00
- Closed at: 2024-01-18T23:07:23+00:00
