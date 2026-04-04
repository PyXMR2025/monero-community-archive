---
title: Easylogging looks for execinfo on android again
source_url: https://github.com/monero-project/monero/issues/3058
author: danrmiller
assignees: []
labels: []
created_at: '2018-01-03T20:39:33+00:00'
updated_at: '2018-01-18T23:40:30+00:00'
type: issue
status: closed
closed_at: '2018-01-18T23:40:30+00:00'
---

# Original Description
@moneromooo-monero I believe this broke from #2940.
https://build.getmonero.org/builders/monero-android-armv7/builds/1213/steps/compile/logs/stdio
```
[ 43%] Building CXX object external/easylogging++/CMakeFiles/easylogging.dir/easylogging++.cc.o
In file included from /home/vagrant/slave/monero-android-armv7/build/external/easylogging++/easylogging++.cc:18:
/home/vagrant/slave/monero-android-armv7/build/external/easylogging++/easylogging++.h:362:13: fatal error: 'execinfo.h' file not found
#   include <execinfo.h>
            ^~~~~~~~~~~~
1 error generated.
```

# Discussion History
## moneromooo-monero | 2018-01-04T12:51:58+00:00
https://github.com/monero-project/monero/pull/3063 should fix it.

## moneromooo-monero | 2018-01-18T23:33:40+00:00
+resolved

# Action History
- Created by: danrmiller | 2018-01-03T20:39:33+00:00
- Closed at: 2018-01-18T23:40:30+00:00
