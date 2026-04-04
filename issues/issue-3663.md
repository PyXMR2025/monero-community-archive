---
title: Does not build with boost 1.67.0
source_url: https://github.com/monero-project/monero/issues/3663
author: pected70
assignees: []
labels: []
created_at: '2018-04-18T21:50:44+00:00'
updated_at: '2018-04-28T15:01:44+00:00'
type: issue
status: closed
closed_at: '2018-04-28T15:01:44+00:00'
---

# Original Description
Monero does not build with boost 1.67.0.

---

[ 28%] Building CXX object contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o
In file included from monero/contrib/epee/src/connection_basic.cpp:35:
In file included from monero/contrib/epee/include/net/connection_basic.hpp:63:
monero/contrib/epee/include/syncobj.h:37:10: fatal error: 'boost/thread/v2/thread.hpp' file not
      found
#include <boost/thread/v2/thread.hpp>
         ^
1 error generated.
make[3]: *** [contrib/epee/src/CMakeFiles/epee.dir/connection_basic.cpp.o] Error 1
make[2]: *** [contrib/epee/src/CMakeFiles/epee.dir/all] Error 2
make[1]: *** [all] Error 2

---

$ ls /usr/local/Cellar/boost/1.67.0/include/boost/thread/v2/
shared_mutex.hpp

# Discussion History
## hashbender | 2018-04-19T04:23:19+00:00
I'm encountering this as well on OSX

## ilovezfs | 2018-04-19T06:11:51+00:00
Yup. Here is a full log https://gist.github.com/ilovezfs/c9c30a8fc935f50afef945202915eb01

## jbeich | 2018-04-19T07:15:04+00:00
Does #3667 help? Otherwise, same here:
- [FreeBSD 10.3 amd64](http://package22.nyi.freebsd.org/data/103amd64-default-PR227427/2018-04-17_15h33m37s/logs/errors/monero-cli-0.12.0.0.log)
- [FreeBSD 10.3 i386](http://package23.nyi.freebsd.org/data/103i386-default-PR227427/2018-04-17_05h28m01s/logs/errors/monero-cli-0.12.0.0.log)
- [FreeBSD 11.1 amd64](http://package22.nyi.freebsd.org/data/111amd64-default-PR227427/2018-04-17_05h28m08s/logs/errors/monero-cli-0.12.0.0.log])
- [FreeBSD 11.1 i386](http://package23.nyi.freebsd.org/data/111i386-default-PR227427/2018-04-17_17h22m58s/logs/errors/monero-cli-0.12.0.0.log)


## ilovezfs | 2018-04-19T07:29:36+00:00
@jbeich yes #3667 works https://gist.github.com/ilovezfs/129d57906c9e07fe704008de18843892

## pected70 | 2018-04-19T10:35:15+00:00
Why not fix upstream https://github.com/sabelnikov/epee?

## jbeich | 2018-04-19T11:07:21+00:00
https://github.com/sabelnikov/epee is not affected. epee bundled in monero is heavily modified but I don't know where to find commit history before 296ae46ed8f8.

# Action History
- Created by: pected70 | 2018-04-18T21:50:44+00:00
- Closed at: 2018-04-28T15:01:44+00:00
