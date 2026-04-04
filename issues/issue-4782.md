---
title: Cannot compile monero - problem with boost
source_url: https://github.com/monero-project/monero/issues/4782
author: rg687
assignees: []
labels:
- invalid
created_at: '2018-11-02T10:28:05+00:00'
updated_at: '2018-11-03T16:40:58+00:00'
type: issue
status: closed
closed_at: '2018-11-03T16:40:58+00:00'
---

# Original Description
Hello, 

When i try to compile monero, i've got this issue

> -- Found Boost Version: 105800
> 
> CMake Error at CMakeLists.txt:874 (message):
> 
>  Boost older than 1.62 is too old to link with OpenSSL 1.1 or newer. Update
> 
>  Boost or install OpenSSL 1.0 and set path to it when running cmake: cmake
> 
>  -DOPENSSL_ROOT_DIR='/usr/include/openssl-1.0;/usr/lib/openssl-1.0'
> 
> 
> -- Configuring incomplete, errors occurred!
> 
> See also "/home/user/Documents/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release/CMakeFiles/CMakeOutput.log".
> 
> See also "/home/user/Documents/monero/build/Linux/_HEAD_detached_at_v0.13.0.4_/release/CMakeFiles/CMakeError.log".
> 
> Makefile:85: recipe for target 'release-all' failed
> 
> make: *** [release-all] Error 1
> 
> user@host:~/Documents/monero$ sudo apt-get install libboost-all-dev
> 
> Reading package lists... Done
> 
> Building dependency tree      
> 
> Reading state information... Done
> 
> libboost-all-dev is already the newest version (1.62.0.1).
> 
> 0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.

it looks like it doesnt find boot older than 1.62 but it seems I have 1.62.0.1 version?

Should i install boost from the source? but what about the one with apt?

thanks

# Discussion History
## moneromooo-monero | 2018-11-02T11:41:50+00:00
You have 1.58 installed where it finds it. Fix that first.

## moneromooo-monero | 2018-11-03T16:27:51+00:00
Not a bug, closing.

+invalid

# Action History
- Created by: rg687 | 2018-11-02T10:28:05+00:00
- Closed at: 2018-11-03T16:40:58+00:00
