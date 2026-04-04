---
title: Build failure with Boost 1.85.0
source_url: https://github.com/monero-project/monero/issues/9304
author: cho-m
assignees: []
labels:
- low priority
- easy
created_at: '2024-04-25T21:17:28+00:00'
updated_at: '2024-05-21T04:43:45+00:00'
type: issue
status: closed
closed_at: '2024-05-21T04:43:45+00:00'
---

# Original Description
Building with Boost 1.85.0 results in errors like:
```
/tmp/wownero-20240425-95926-qcyyf2/src/common/boost_serialization_helper.h:113:93: error: no member named 'copy_option' in namespace 'boost::filesystem'; did you mean 'copy_options'?
      boost::filesystem::copy_file(file_path, file_path + ".unportable", boost::filesystem::copy_option::overwrite_if_exists);
                                                                         ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~
                                                                                            copy_options
```
```
/tmp/wownero-20240425-95926-qcyyf2/contrib/epee/include/storages/portable_storage_val_converters.h:63:49: error: no member named 'numeric' in namespace 'boost'
      CHECK_AND_ASSERT_THROW_MES(from >= boost::numeric::bounds<to_type>::lowest(), "int value overhead: try to set value " << from << " to type " << typeid(to_type).name() << " with lowest possible value = " << boost::numeric::bounds<to_type>::lowest());
                                         ~~~~~~~^
```

The first is due to removal of `boost::filesystem::copy_option` (https://github.com/boostorg/filesystem/commit/5df060e95ca844fe91b29001b4ae22bdb65635c6). Previous attempt to fix in #8751 back when only deprecated.

Second looks like some indirect headers need to be directly included.

---

EDIT: Also, on master branch, there are some other incompatibilities like:
https://github.com/monero-project/monero/blob/c8214782fb2a769c57382a999eaf099691c836e7/src/simplewallet/simplewallet.cpp#L4777

---

Seen when updating Boost in Homebrew - https://github.com/Homebrew/homebrew-core/pull/169237

# Discussion History
## 0xFFFC0000 | 2024-04-27T05:49:37+00:00
Thanks for reporting this. I am looking into this. For the first error, this should fix it I believe [1]. Trying to replicate second one.


1. https://github.com/monero-project/monero/pull/9305

## cho-m | 2024-04-27T13:55:13+00:00
> Trying to replicate second one.

I didn't see it on stable release, but was building fork Wownero when I saw the failure. Then I checked that this was part of Monero code.

https://www.boost.org/doc/libs/1_85_0/libs/filesystem/doc/deprecated.html mentions `complete` was removed and replacement is `absolute`. For previous 1.84.0, the implementation was essentially an alias https://github.com/boostorg/filesystem/blob/boost-1.84.0/include/boost/filesystem/operations.hpp#L408-L412


## 0xFFFC0000 | 2024-05-02T05:32:06+00:00
This series of simple patches does fix this issue: #9313 #9307 #9305

I am closing this issue. Feel free to let me know if you had encountered issues. 

## selsta | 2024-05-02T09:38:53+00:00
Keeping this open until the PRs are merged, in case others run into this issue.

# Action History
- Created by: cho-m | 2024-04-25T21:17:28+00:00
- Closed at: 2024-05-21T04:43:45+00:00
