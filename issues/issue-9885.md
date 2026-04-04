---
title: Use of external caches break guix build
source_url: https://github.com/monero-project/monero/issues/9885
author: lobster-kerouac
assignees: []
labels:
- build system
created_at: '2025-04-02T19:35:54+00:00'
updated_at: '2025-04-06T16:28:12+00:00'
type: issue
status: closed
closed_at: '2025-04-06T16:23:27+00:00'
---

# Original Description
Hello,

I'm trying out the guix build using the instructions [here](https://github.com/monero-project/monero/blob/master/contrib/guix/README.md), and the use of SOURCES_PATH and/or BASE_CACHE environmental variables seem to be causing builds to fail.

Some example output trying to build a single host after everything in the /gnu/store has been built:

```
$ env SOURCES_PATH="/path/to/sources-dir" BASE_CACHE="/path/to/base-dir" HOSTS='x86_64-linux-gnu' ./contrib/guix/guix-build
Checking that we can connect to the guix-daemon...

Hint: If this hangs, you may want to try turning your guix-daemon off and on
      again.

make: Entering directory '/home/guixuser/build/monero/contrib/depends'
make[1]: Entering directory '/home/guixuser/build/monero/contrib/depends'
make[1]: Leaving directory '/home/guixuser/build/monero/contrib/depends'
make: Leaving directory '/home/guixuser/build/monero/contrib/depends'
INFO: Building 977dedce2cf7 for platform triple x86_64-linux-gnu:
      ...using commit timestamp: 1742992626
      ...running at most 6 jobs
      ...from worktree directory: '/home/guixuser/build/monero'
          ...bind-mounted in container to: '/monero'
      ...in build directory: '/home/guixuser/build/monero/guix/guix-build-977dedce2cf7/build/distsrc-977dedce2cf7-x86_64-linux-gnu'
          ...bind-mounted in container to: '/distsrc-base/build/distsrc-977dedce2cf7-x86_64-linux-gnu'
      ...outputting in: '/home/guixuser/build/monero/guix/guix-build-977dedce2cf7/output/x86_64-linux-gnu'
          ...bind-mounted in container to: '/outdir-base/x86_64-linux-gnu'
x86_64-linux-gnu
Required environment variables as seen inside the container:
    DIST_ARCHIVE_BASE: /outdir-base/dist-archive
    VERSION: 977dedce2cf7
    HOST: x86_64-linux-gnu
    COMMIT_TIMESTAMP: 1742992626
    JOBS: 6
    DISTSRC: /distsrc-base/build/distsrc-977dedce2cf7-x86_64-linux-gnu
    OUTDIR: /outdir-base/x86_64-linux-gnu
    LOGDIR: /logdir-base/x86_64-linux-gnu
    OPTIONS: 
make: Entering directory '/monero/contrib/depends'
Fetching protobuf-cpp-3.21.12.tar.gz from https://github.com/protocolbuffers/protobuf/releases/download/v21.12/
/gnu/store/3jhfhxdf6v5ms10x5zmnl166dh3yhbr1-bash-minimal-5.1.16/bin/sh: line 1: curl: command not found
Fetching protobuf-cpp-3.21.12.tar.gz from https://downloads.getmonero.org/depends-sources
/gnu/store/3jhfhxdf6v5ms10x5zmnl166dh3yhbr1-bash-minimal-5.1.16/bin/sh: line 1: curl: command not found
make: *** [funcs.mk:300: /home/guixuser/build/guix_cache/sources_path/download-stamps/.stamp_fetched-native_protobuf-protobuf-cpp-3.21.12.tar.gz.hash] Error 127
make: Leaving directory '/monero/contrib/depends'
```

From the log it seems like neither the SOURCES_CACHE nor BASE_CACHE environmental variables are being passed to the container. Thus, I'm assuming `curl` can't be found because the container doesn't know to look somewhere else.

Any advice would be appreciated.

# Discussion History
## tobtoht | 2025-04-03T14:14:31+00:00
What is the output of `ls -la /path/to/sources-dir/**`?

## lobster-kerouac | 2025-04-03T14:50:11+00:00
Here's everything in the SOURCES_DIR:
```
total 157960
drwxrwxr-x 3 guixuser guixuser      4096 Apr  2 17:58 .
drwxr-xr-x 5 guixuser guixuser      4096 Apr  2 03:06 ..
-rw-rw-r-- 1 guixuser guixuser 123110547 Apr  2 17:58 boost_1_84_0.tar.bz2
drwxrwxr-x 2 guixuser guixuser      4096 Apr  2 17:58 download-stamps
-rw-rw-r-- 1 guixuser guixuser    348221 Apr  2 17:58 hidapi-0.14.0.tar.gz
-rw-rw-r-- 1 guixuser guixuser   1919817 Apr  2 17:58 libsodium-1.0.18.tar.gz
-rw-rw-r-- 1 guixuser guixuser    643680 Apr  2 17:58 libusb-1.0.27.tar.bz2
-rw-rw-r-- 1 guixuser guixuser   3365395 Apr  2 17:58 ncurses-6.1.tar.gz
-rw-rw-r-- 1 guixuser guixuser  15294843 Apr  2 17:58 openssl-3.0.13.tar.gz
-rw-rw-r-- 1 guixuser guixuser   4842303 Apr  2 17:58 protobuf-cpp-3.21.12.tar.gz
-rw-rw-r-- 1 guixuser guixuser   2975937 Apr  2 17:58 readline-8.0.tar.gz
-rw-rw-r-- 1 guixuser guixuser   6682466 Apr  2 17:58 unbound-1.22.0.tar.gz
-rw-rw-r-- 1 guixuser guixuser   2530237 Apr  2 17:58 zeromq-4.3.5.tar.gz
```

The BASE_CACHE directory is empty.

I'm not sure if this matters, but initially I had the SOURCES_PATH and BASE_CACHE on a separate file system (no symlinks, though). I just tried again with those dirs on the same filesystem as where the build is happening and got the same result.

For the record, this is on Ubuntu Server 24.04 LTS.

## tobtoht | 2025-04-05T11:10:21+00:00
What is the output of `/var/guix/profiles/per-user/root/current-guix/bin/guix-daemon --version`?

## lobster-kerouac | 2025-04-05T16:13:20+00:00
I get `guix-daemon (GNU Guix) 1.4.0`. I installed guix using the official install script.

I notice that that command is querying the root user's guix-daemon. Should the `guix-build` command be run as root?

## tobtoht | 2025-04-05T16:53:19+00:00
Reproduced. Looking for a fix.

>Should the guix-build command be run as root?

No.

## lobster-kerouac | 2025-04-06T16:28:11+00:00
Thanks, @tobtoht! Everything is working as expected.

# Action History
- Created by: lobster-kerouac | 2025-04-02T19:35:54+00:00
- Closed at: 2025-04-06T16:23:27+00:00
