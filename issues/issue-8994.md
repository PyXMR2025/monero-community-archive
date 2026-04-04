---
title: Error when building on Fedora 38
source_url: https://github.com/monero-project/monero/issues/8994
author: gus4rs
assignees: []
labels: []
created_at: '2023-09-18T12:14:44+00:00'
updated_at: '2023-09-18T12:31:59+00:00'
type: issue
status: closed
closed_at: '2023-09-18T12:26:43+00:00'
---

# Original Description
Environment:

```
Fedora Linux 38 on aarch64
gcc (GCC) 13.2.1 20230728 (Red Hat 13.2.1-1)
tag: v0.18.2.2
```


```
[ 18%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee.dir/string_tools.cpp.o
[ 19%] Building CXX object contrib/epee/src/CMakeFiles/obj_epee.dir/parserse_base_utils.cpp.o
In file included from /home/user/monero/contrib/epee/src/parserse_base_utils.cpp:27:
/home/user/monero/contrib/epee/include/storages/parserse_base_utils.h:46:28: error: ‘uint8_t’ does not name a type
   46 |     static const constexpr uint8_t lut[256]={
      |                            ^~~~~~~
/home/user/monero/contrib/epee/include/storages/parserse_base_utils.h:32:1: note: ‘uint8_t’ is defined in header ‘<cstdint>’; did you forget to ‘#include <cstdint>’?
   31 | #include <boost/utility/string_ref_fwd.hpp>
  +++ |+#include <cstdint>
   32 | #include <string>
/home/user/monero/contrib/epee/include/storages/parserse_base_utils.h: In function ‘bool epee::misc_utils::parse::isspace(char)’:
/home/user/monero/contrib/epee/include/storages/parserse_base_utils.h:87:14: error: ‘lut’ was not declared in this scope
   87 |       return lut[(uint8_t)c] & 8;
```





# Discussion History
## selsta | 2023-09-18T12:16:44+00:00
Does adding `#include <cstdint>` to `contrib/epee/include/storages/parserse_base_utils.h` solve the issue?

## 0xFFFC0000 | 2023-09-18T12:19:06+00:00
I had this issue first time building few weeks ago. As @selsta mentioned adding the include is going to fix it. 

## gus4rs | 2023-09-18T12:21:39+00:00
It fixes that particular error, but it fails further down with similar messages of missng includes. What is the reason for this? Is this a compiler issue?

## selsta | 2023-09-18T12:23:31+00:00
Can you post the next error? I think your compiler version has different default includes and that's why it fails.

## SChernykh | 2023-09-18T12:24:03+00:00
It's an issue with C++ library that comes with your compiler. It doesn't include <cstdint> where other libraries do.

## tobtoht | 2023-09-18T12:24:04+00:00
git cherry-pick c32befe4f8385f5f893c0db611060bc7c7b425f3

## 0xFFFC0000 | 2023-09-18T12:25:00+00:00
Just double checking, are you sure it is exactly similar error? Can you post it here? 

Regarding why this happens, I am not sure about the exact reason, but each distro and compiler does have its own internal customization and paths. Tomorrow I will take a deep look at where does it get those types in Ubuntu. 

## selsta | 2023-09-18T12:26:43+00:00
It's fixed already by @tobtoht in master and release branch, but it's not included in the v0.18.2.2 tag.

`git checkout release-v0.18` would solve it or the cherry-pick command posted above. 

## gus4rs | 2023-09-18T12:31:48+00:00
> 
> `git checkout release-v0.18` would solve it or the cherry-pick command posted above.

yes, I will be using this branch, thanks all


# Action History
- Created by: gus4rs | 2023-09-18T12:14:44+00:00
- Closed at: 2023-09-18T12:26:43+00:00
