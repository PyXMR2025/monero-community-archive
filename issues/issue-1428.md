---
title: Errors when compiling Monero on openSUSE
source_url: https://github.com/monero-project/monero/issues/1428
author: good-guy-greg
assignees: []
labels:
- invalid
created_at: '2016-12-10T20:25:19+00:00'
updated_at: '2018-01-08T13:00:33+00:00'
type: issue
status: closed
closed_at: '2018-01-08T13:00:33+00:00'
---

# Original Description
I'm trying to compile latest version of Monero On openSUSE Leap, but it throws an error. Here is the log: 
http://paste.opensuse.org/view/raw/79b78294


# Discussion History
## good-guy-greg | 2016-12-10T21:43:40+00:00
I just tried and was able to successfully build the stable version 0.10.0 from the source. But I'm unable to build the latest version.

## iDunk5400 | 2016-12-11T11:59:15+00:00
I tried to build master at 2d0fbaf with gcc/g++ 4.8.5 and got the same error, while it built just fine with 4.9.4, 5.4.1 and 6.2.0. I guess the implementation of thread groups moved the minimum required gcc version to 4.9. Not sure if any particular minor version is required.

## moneromooo-monero | 2016-12-11T13:57:36+00:00
See https://github.com/monero-project/monero/issues/1373 for discussion and trivial fix. It had been forgot I think, I'll make the change now.

## moneromooo-monero | 2016-12-11T14:01:50+00:00
https://github.com/monero-project/monero/pull/1431

Can you try and see if that works for you ?

## iDunk5400 | 2016-12-11T14:14:08+00:00
I can confirm that master builds successfully with gcc 4.8.5 after applying #1431.

## good-guy-greg | 2016-12-11T14:40:41+00:00
It passed the previous point of failure. But now there is a new error. Please let me know if I should start a new issue. Here is the log:
http://paste.opensuse.org/view/raw/3086f0af

## good-guy-greg | 2016-12-12T22:50:31+00:00
If I use gcc 5.3.1, the errors change. Here is the log:
http://paste.opensuse.org/view/raw/3789434b

## peronero | 2016-12-13T15:53:33+00:00
Compiles fine on Tumbleweed FWIW...

## ghost | 2016-12-13T21:54:54+00:00
@good-guy-greg Has this now been resolved with the latest changes in 0.10.1.0?

## good-guy-greg | 2016-12-13T23:24:03+00:00
@NanoAkron Yes, there are errors. Please see the log: http://paste.opensuse.org/view/raw/41eaf24e

## ghost | 2016-12-14T23:02:31+00:00
@vtnerd Have you seen this issue before?

@good-guy-greg Would you try with GCC >=4.9 and report back?

@fluffypony Should we bump the min GCC version?

## good-guy-greg | 2016-12-15T00:34:27+00:00
@NanoAkron, Just tried with gcc 4.9.2 with no success. Log: http://paste.opensuse.org/5b803b8a

## vtnerd | 2016-12-15T02:18:02+00:00
@iDunk5400 gcc 4.8.5 should have been able to compile the master branch without that patch.

@good-guy-greg can you post a log with an environment variable `VERBOSE=1`. This shows the exact command be given. I think somehow multiple compiler versions are being mixed.

## good-guy-greg | 2016-12-15T09:34:38+00:00
@vtnerd Done, using gcc 4.9: http://paste.opensuse.org/789e9dcf

## vtnerd | 2016-12-16T02:38:20+00:00
I think this is compiling against headers from the C++ libs of the newer compiler, while trying to link against the library of the older compiler. Although I am not sure about those other errors. Does `find /usr/lib64/gcc/x86_64-suse-linux/4.9/ -name "libstdc++*"` return a second C++ lib? There should be a shared object in that folder, and see if the top level `/usr/lib64/libstdc++.so` is an alias. The latter is what is being linked against.

## moneromooo-monero | 2017-08-08T11:52:43+00:00
ping

## dEBRUYNE-1 | 2018-01-08T12:59:44+00:00
+invalid

# Action History
- Created by: good-guy-greg | 2016-12-10T20:25:19+00:00
- Closed at: 2018-01-08T13:00:33+00:00
