---
title: 'Looking for inputs regarding the message: WARNING: You may not have a high
  enough lockable memory limit, , see ulimit -l'
source_url: https://github.com/monero-project/monero/issues/8718
author: blackmennewstyle
assignees: []
labels: []
created_at: '2023-01-22T12:59:51+00:00'
updated_at: '2023-02-22T19:11:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Every-time i launch the `monero-wallet-rpc` daemon, i got that message`WARNING: You may not have a high enough lockable memory limit, , see ulimit -l`. Where can we found more information about it? According to my operating system, `GNU/Linux Debian 11`, my limits are currently:
```
ulimit -H -a
real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) unlimited
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 125768
max locked memory           (kbytes, -l) 4036874
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1048576
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) unlimited
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 125768
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```
So i imagine `4036874 kilobytes` is not enough? What is the recommendation?

# Discussion History
## moneromooo-monero | 2023-01-22T16:00:59+00:00
Maybe the soft limit is lower ?

## blackmennewstyle | 2023-01-23T00:08:33+00:00
Well, apparently no :/
```
ulimit -S -a
real-time non-blocking time  (microseconds, -R) unlimited
core file size              (blocks, -c) 0
data seg size               (kbytes, -d) unlimited
scheduling priority                 (-e) 0
file size                   (blocks, -f) unlimited
pending signals                     (-i) 125768
max locked memory           (kbytes, -l) 4036874
max memory size             (kbytes, -m) unlimited
open files                          (-n) 1024
pipe size                (512 bytes, -p) 8
POSIX message queues         (bytes, -q) 819200
real-time priority                  (-r) 0
stack size                  (kbytes, -s) 8192
cpu time                   (seconds, -t) unlimited
max user processes                  (-u) 125768
virtual memory              (kbytes, -v) unlimited
file locks                          (-x) unlimited
```
They are both the same apparently.

## moneromooo-monero | 2023-01-23T14:22:34+00:00
That should be much more than enough.

What is the output of this ?

```
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/resource.h>
#include <unistd.h>
#include <stdio.h>

  ssize_t get_lockable_memory()
  {
#ifdef __GLIBC__
    struct rlimit rlim;
    if (getrlimit(RLIMIT_MEMLOCK, &rlim) < 0)
    {
      printf("Failed to determine the lockable memory limit\n");
      return -1;
    }
    return rlim.rlim_cur;
#else
    return -1;
#endif
  }


int main()
{
  ssize_t S = get_lockable_memory();
  printf("%zd\n", S);
  return 0;
}
```

## blackmennewstyle | 2023-01-24T06:41:07+00:00
The suggested code outputs:
```
./monero 
963691520
```

## moneromooo-monero | 2023-01-30T14:11:11+00:00
Are you sure both are run in a similar context ?

## blackmennewstyle | 2023-02-20T14:07:07+00:00
Sorry for the late reply.

I executed your previous code on the wrong computer. When i executed on the right one, i got
```
./monero
4133803008
```

## moneromooo-monero | 2023-02-22T19:11:41+00:00
Both cases output well more than needed. But the error happens when that same code, when run from the monero code, returns a small value...

This patch will print it from the monero source.
Save it as  /tmp/wallet_patch.diff then run:

patch -p1 < /tmp/wallet_patch.diff

```
diff --git a/src/wallet/wallet_args.cpp b/src/wallet/wallet_args.cpp
index 6f95f546d..62d37941a 100644
--- a/src/wallet/wallet_args.cpp
+++ b/src/wallet/wallet_args.cpp
@@ -226,6 +226,7 @@ namespace wallet_args
     Print(print) << boost::format(wallet_args::tr("Logging to %s")) % log_path;
 
     const ssize_t lockable_memory = tools::get_lockable_memory();
+    printf("lockable_memory: %zd\n", lockable_memory);
     if (lockable_memory >= 0 && lockable_memory < 256 * 4096) // 256 pages -> at least 256 secret keys and other such small/medium objects
       Print(print) << tr("WARNING: You may not have a high enough lockable memory limit")
 #ifdef ELPP_OS_UNIX
```
Then make again, run, and see what it reports. It ought to be the same as the test program above since I copied that code, but if not it may be some SELinux configuration, etc, etc. Or something unexpected I can't guess right now.



# Action History
- Created by: blackmennewstyle | 2023-01-22T12:59:51+00:00
