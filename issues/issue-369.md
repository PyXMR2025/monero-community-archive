---
title: GUI does not launch in Tails nor in Whonix.
source_url: https://github.com/monero-project/monero-gui/issues/369
author: moneroexamples
assignees: []
labels: []
created_at: '2016-12-29T03:06:40+00:00'
updated_at: '2017-04-04T23:05:47+00:00'
type: issue
status: closed
closed_at: '2017-04-04T23:05:47+00:00'
---

# Original Description
Ability to run GUI in Tails or Whonix (Tor base Linux distros) is important from privacy point of view. In both distros, GUI wont start, since GUI relays on newer C++ stds that are available in those distros. 

Specifically, the error msg is:

```
ser@host:~/monero-wallet-gui$ ./start-gui.sh 
./monero-wallet-gui: /usr/lib/i386-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by ./monero-wallet-gui)
./monero-wallet-gui: /usr/lib/i386-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.21' not found (required by /home/user/monero-wallet-gui/libs/libproxy.so.1)
```

GUI uses `GLIBCXX_3.4.21`, whereas in both Tails and Whonix, there is `GLIBCXX_3.4.20`. 

I tried to compile GUI from source. On Tails there are dependencies problems. Did not look more into this. But on whonix all dependencies do install without problems. However, compilation fails, as monero depends on boost 1.58. However Whonix has 1.55. Manually changing in CMakeLists.txt to 1.55, leads later on to compilation errors:

```
/home/user/monero-core/monero/src/common/thread_group.cpp: In constructor ‘tools::thread_group::thread_group(std::size_t)’:
/home/user/monero-core/monero/src/common/thread_group.cpp:54:14: error: ‘class boost::optional<tools::thread_group::data>’ has no member named ‘emplace’
     internal.emplace(count);
              ^
src/common/CMakeFiles/obj_common.dir/build.make:215: recipe for target 'src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o' failed
make[3]: *** [src/common/CMakeFiles/obj_common.dir/thread_group.cpp.o] Error 1
make[3]: Leaving directory '/home/user/monero-core/monero/build/release'
CMakeFiles/Makefile2:502: recipe for target 'src/common/CMakeFiles/obj_common.dir/all' failed
make[2]: *** [src/common/CMakeFiles/obj_common.dir/all] Error 2
make[2]: Leaving directory '/home/user/monero-core/monero/build/release'
Makefile:127: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/user/monero-core/monero/build/release'
Makefile:58: recipe for target 'release-all' failed
make: *** [release-all] Error 2
```

So at the moment, I dont know how to compile nor run monero command line and gui on Whonix and Tails.




# Discussion History
## Jaqueeee | 2016-12-29T15:40:49+00:00
Unfortunately boost 1.58 is required so you will need to build or upgrade boost before building Monero and GUI on those platforms. 

I built boost 1.60 with following options
```
./b2 --layout=tagged --build-type=minimal --prefix=/usr/local --with-chrono --with-date_time --with-filesystem --with-program_options --with-regex --with-serialization --with-system --with-thread --with-locale 
sudo ./b2 install
```



## vtnerd | 2016-12-29T17:38:17+00:00
Is the GUI being built on a different platform and then copied into Tails?

## moneroexamples | 2016-12-30T01:37:05+00:00
> Is the GUI being built on a different platform and then copied into Tails?

I used the official 32 bit release of gui binaries. They dont work as in the first comment. Also test compiling from source, but compilation on Tails and Whonix  fails, as Monero uses newer boost than is available for Tails and Whonix.

## anonimal | 2017-01-20T10:21:20+00:00
@moneroexamples if you can do apt pinning, you won't need to build boost manually. They are both based on Debian so satisfying dependencies shouldn't be an issue if you know how to get around a Debian system.

## moneroexamples | 2017-01-21T01:36:34+00:00
Thanks. I'm not worrying about myself, but many privacy oriented users may want to run it in tails, whonix or qubes, and it would be good if it could run out of box on those OSes. Anyway, later I will check beta 2 and see if there is any change in this area.

## anonimal | 2017-01-24T21:05:25+00:00
@moneroexamples in the meantime, have you tried snapcraft yet? There's a yaml recipe in the monero repo (not monero-core), recently updated (I haven't tried it myself though).

https://github.com/monero-project/monero/pull/1068
https://github.com/monero-project/monero/pull/1601

## moneroexamples | 2017-01-24T21:11:54+00:00
Isnt snap ubuntu thing only? Will it be avaliable in tails or whonix?

## anonimal | 2017-01-24T21:39:42+00:00
http://snapcraft.io/
>Package any app for every Linux desktop, server, cloud or device, and deliver updates directly.

Like I said, they are based on Debian.

## ghost | 2017-03-29T03:46:06+00:00
@moneroexamples Can this issue be closed?

## moneroexamples | 2017-03-29T03:52:52+00:00
Yes, I can close it. But is gui working in tails and whonix? 

## moneroexamples | 2017-04-04T23:05:47+00:00
I will close it now. Havent been able to check if its working in tails or whonix, but I think someone said on reddit they using beta 2 on tails, so I guess its working already.

# Action History
- Created by: moneroexamples | 2016-12-29T03:06:40+00:00
- Closed at: 2017-04-04T23:05:47+00:00
