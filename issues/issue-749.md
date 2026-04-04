---
title: Can not compile in debug mode
source_url: https://github.com/monero-project/monero-gui/issues/749
author: MaxXor
assignees: []
labels: []
created_at: '2017-05-27T11:46:58+00:00'
updated_at: '2017-05-30T19:04:51+00:00'
type: issue
status: closed
closed_at: '2017-05-30T19:04:51+00:00'
---

# Original Description
Hello,
I'm trying to track down issue #524, but I'm stuck at trying to compile the project in debug mode. I get the following errors when I try to build with command `./build.sh debug`:
> /usr/bin/ld: cannot find -lwallet_merged
> /usr/bin/ld: cannot find -lepee
> /usr/bin/ld: cannot find -leasylogging

# Discussion History
## Jaqueeee | 2017-05-29T12:04:44+00:00
There's most likely a previous error in get_libwallet_api.sh where those libs are built. 
Try running that script explicitly before running build.sh and see if you get any errors. 
`./get_libwallet_api.sh debug`

## MaxXor | 2017-05-30T16:02:40+00:00
I'm getting many errors like the one below when executing that script.
>CMake Error at external/easylogging++/CMakeLists.txt:53 (install):
>install TARGETS given no LIBRARY DESTINATION for shared library target
>"easylogging".

## Jaqueeee | 2017-05-30T16:32:01+00:00
the one liner in #751 fixes the issue for me on osx. It makes the debug build static. You need to delete monero/build folder before trying again. 

## MaxXor | 2017-05-30T19:04:50+00:00
Thanks, that fixed it.

# Action History
- Created by: MaxXor | 2017-05-27T11:46:58+00:00
- Closed at: 2017-05-30T19:04:51+00:00
