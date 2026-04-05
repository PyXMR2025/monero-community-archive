---
title: Mac OSX - unknown type name 'uint64_t'
source_url: https://github.com/xmrig/xmrig/issues/918
author: emha
assignees: []
labels: []
created_at: '2019-01-21T08:44:46+00:00'
updated_at: '2019-01-29T20:16:51+00:00'
type: issue
status: closed
closed_at: '2019-01-29T20:16:51+00:00'
---

# Original Description
Hi,

I try to install xmrig on my macbook pro. When I run the `make` statement I get the following error as output:

**macOS Mojave (10.14.12)
Xcode-Build-Version: 10.1**

```
[ 15%] Building CXX object CMakeFiles/xmrig.dir/src/api/NetworkState.cpp.o
In file included from /Users/malteheyenga1/.xmrig/xmrig/src/api/NetworkState.cpp:25:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/algorithm:641:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/cstring:61:
In file included from /usr/local/include/string.h:25:
In file included from /usr/local/include/plist/Node.h:25:
/usr/local/include/plist/plist.h:161:28: error: unknown type name 'uint64_t'
    plist_t plist_new_uint(uint64_t val);
                           ^
/usr/local/include/plist/plist.h:180:45: error: unknown type name 'uint64_t'
    plist_t plist_new_data(const char *val, uint64_t length);
                                            ^
/usr/local/include/plist/plist.h:199:27: error: unknown type name 'uint64_t'
    plist_t plist_new_uid(uint64_t val);
                          ^
/usr/local/include/plist/plist.h:437:43: error: unknown type name 'uint64_t'
    void plist_get_uint_val(plist_t node, uint64_t * val);
                                          ^
/usr/local/include/plist/plist.h:457:55: error: unknown type name 'uint64_t'
    void plist_get_data_val(plist_t node, char **val, uint64_t * length);
                                                      ^
/usr/local/include/plist/plist.h:476:42: error: unknown type name 'uint64_t'
    void plist_get_uid_val(plist_t node, uint64_t * val);
                                         ^
/usr/local/include/plist/plist.h:520:43: error: unknown type name 'uint64_t'
    void plist_set_uint_val(plist_t node, uint64_t val);
                                          ^
/usr/local/include/plist/plist.h:540:60: error: unknown type name 'uint64_t'
    void plist_set_data_val(plist_t node, const char *val, uint64_t length);
                                                           ^
/usr/local/include/plist/plist.h:559:42: error: unknown type name 'uint64_t'
    void plist_set_uid_val(plist_t node, uint64_t val);
                                         ^
In file included from /Users/malteheyenga1/.xmrig/xmrig/src/api/NetworkState.cpp:25:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/algorithm:641:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/cstring:61:
In file included from /usr/local/include/string.h:26:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/string:477:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/string_view:176:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/__string:58:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/memory:653:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/typeinfo:61:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/exception:82:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/cstdlib:86:
In file included from /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1/stdlib.h:94:
In file included from /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/stdlib.h:66:
In file included from /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/wait.h:110:
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:197:2: error: unknown type name 'uint64_t'
        uint64_t ri_user_time;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:198:2: error: unknown type name 'uint64_t'
        uint64_t ri_system_time;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:199:2: error: unknown type name 'uint64_t'
        uint64_t ri_pkg_idle_wkups;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:200:2: error: unknown type name 'uint64_t'
        uint64_t ri_interrupt_wkups;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:201:2: error: unknown type name 'uint64_t'
        uint64_t ri_pageins;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:202:2: error: unknown type name 'uint64_t'
        uint64_t ri_wired_size;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:203:2: error: unknown type name 'uint64_t'
        uint64_t ri_resident_size;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:204:2: error: unknown type name 'uint64_t'
        uint64_t ri_phys_footprint;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:205:2: error: unknown type name 'uint64_t'
        uint64_t ri_proc_start_abstime;
        ^
/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk/usr/include/sys/resource.h:206:2: error: unknown type name 'uint64_t'
        uint64_t ri_proc_exit_abstime;
```

Any suggestions why this happens and how to fix it? Updated all dependencies etc. but that didn't help.

# Discussion History
## xmrig | 2019-01-21T11:01:11+00:00
Strange, try add `#include <stdint.h>` on top of `src/api/NetworkState.cpp` file.
Thank you.

## emha | 2019-01-21T11:04:37+00:00
Changed as described but the error is still the same. The include area now looks like this

```
#include <stdint.h>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <uv.h>
```

## emha | 2019-01-23T21:52:00+00:00
Any ideas on this?

## tttony | 2019-01-28T12:42:01+00:00
I don't have mac os x but I found this: https://stackoverflow.com/a/47401866, try it and let us know if it worked

## emha | 2019-01-29T20:16:51+00:00
That worked, thank you very much!

# Action History
- Created by: emha | 2019-01-21T08:44:46+00:00
- Closed at: 2019-01-29T20:16:51+00:00
