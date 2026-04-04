---
title: can not be used when making a shared object;  recompile with -fPIC
source_url: https://github.com/monero-project/monero/issues/3140
author: danrmiller
assignees: []
labels: []
created_at: '2018-01-17T00:24:16+00:00'
updated_at: '2018-01-26T00:11:15+00:00'
type: issue
status: closed
closed_at: '2018-01-26T00:11:15+00:00'
---

# Original Description
Can someone confirm, does this mean for a static monero build I need to recompile my boost libs and we can't use distribution provided ones that aren't compiled with -fPIC? Or is something else going on?

```
/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): 
relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; 
recompile with -fPIC
```
I see someone has the same issue with gtest, but I think we offer that vendored, so it should be less of an issue: https://github.com/monero-project/monero/issues/3096#issuecomment-357510962


# Discussion History
## jtgrassie | 2018-01-17T00:44:00+00:00
I was seeing this recently too @danrmiller, just didn't have time to investigate. It's odd only boost showing this issue, but yes, looks like for _static_ builds, boost static libs need building now with -fPIC. Buildbots failing on this same issue.

## moneromooo-monero | 2018-01-17T00:44:30+00:00
That is correct, boost static archives aren't built with -fPIC, so they're unusable for PIE binaries.

## jtgrassie | 2018-01-17T00:47:12+00:00
@moneromooo-monero can we at least get the buildbots updated to have boost compiled with -fPIC for the static builds? 

_sorry not sure who manages the buildbots_

## danrmiller | 2018-01-17T00:51:01+00:00
@jtgrassie I manage the buildbots and will update.

## jtgrassie | 2018-01-17T00:51:54+00:00
Thanks @danrmiller 

## danrmiller | 2018-01-17T05:52:38+00:00
On the ubuntu amd64 box I've rebuilt boost with -fPIC, but now I need to do the same with ssl:

https://build.getmonero.org/builders/monero-static-ubuntu-amd64/builds/3296/steps/compile/logs/stdio

I don't know about other major distributions, but it looks intentional according to debian policy that the static libs are built without -fPIC: https://www.debian.org/doc/debian-policy/#libraries
```
As to the static libraries, the common case is not to have relocatable code, 
since there is no benefit, unless in specific cases; 
therefore the static version must not be compiled with the -fPIC flag.
```
I believe ubuntu has now changed policy recently to also build static libs with -fPIC for their upcoming releases (https://wiki.ubuntu.com/SecurityTeam/PIE).

I guess this isn't an issue because the benefits are worth it, and also because people can just build the regular shared build, but I'm going to leave this open another day or so for visibility that we've added a hurdle to many users easily building a static binary. 



## hippich | 2018-01-21T03:32:01+00:00
So for each OS and version we will have to build separate build? Like I compiled one on Ubuntu 16.04, copied over binary to Debian Wheezy and when running monerd i got missing libboost v1.58 error. Problem is - Debian has only v1.49 in repositories.. So now it means searching and installing libboost v1.58 somehow.. 

## moneromooo-monero | 2018-01-21T10:49:39+00:00
Just don't copy binaries, you need to build with whatever you'll be using.

## hippich | 2018-01-21T18:48:28+00:00
I am confused... Then how can we build static monero-gui for example? In fact, how one available on getmonero.com is built when if I try build one I am getting -fPIC errors mentioned above?

## moneromooo-monero | 2018-01-21T19:27:22+00:00
You can if you want to go to the trouble. It's just way easier to just compile what you run.

## danrmiller | 2018-01-26T00:11:15+00:00
I'll get the dependent libs recompiled for arm, bsd, etc. Thanks

# Action History
- Created by: danrmiller | 2018-01-17T00:24:16+00:00
- Closed at: 2018-01-26T00:11:15+00:00
