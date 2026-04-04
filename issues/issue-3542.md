---
title: Incompatability with libunbound 1.4.20 on centos 7
source_url: https://github.com/monero-project/monero/issues/3542
author: NmxMilk
assignees: []
labels: []
created_at: '2018-04-03T07:44:41+00:00'
updated_at: '2018-04-12T11:56:55+00:00'
type: issue
status: closed
closed_at: '2018-04-12T11:56:55+00:00'
---

# Original Description
Readme says libunbound 	1.4.16 or newer !
Compilation on centos7 with libunbound 1.4.20 gives compilation errors wrong prototypes : char * and const char *.
Cloned https://github.com/monero-project/unbound.git to make it compile.
This installed version 2.1.5 so maybe should update the readme.
Note :
The readme states to use :
cd monero && git submodule init && git submodule update
which should compile version 2.1.5 as well

BTW, can someone explain why monero forked libunbound instead of using original from https://www.unbound.net/download.html ?
And how come latest version from unbound.net is 1.7 and not 2.1 ?



# Discussion History
## anonimal | 2018-04-03T08:39:15+00:00
>BTW, can someone explain why monero forked libunbound instead of using original from 

**It is the original libunbound** along with necessary monero build patches. Please look closer at the repo before making accusations.

> And how come latest version from unbound.net is 1.7 and not 2.1 ?

From the link that you just posted:  [The latest version of unbound (currently 1.7.0)](https://www.unbound.net/download.html).

>Readme says libunbound 1.4.16 or newer !

Try removing on distro-installed unbound and do the following: `$ git clone --recursive https://github.com/monero-project/monero && cd monero && make` and see if builds. Paste a useful log message if it doesn't build.

## NmxMilk | 2018-04-03T12:15:53+00:00
@anonimal  no accusation just simple remarks and questions
I issued : yum install unbound-devel and this installed version 1.4.20 on my system
Monero won't compile with that version (as per title).
Googled for the most recent version of libunbound and found:
http://unbound.nlnetlabs.nl/download.html
which states version 1.7 as latest release.
At the same time i found the submodule in the monero project and decided to give it a try first.
This gave me /usr/local/lib/libunbound.so -> libunbound.so.2.5.8
I thought libunbound.so.2.5.8 meant version 2.5.8 ?
Since that confused me thus my last question.

If you read my comments carefully you can see i have it already compiled and running.


## vrobolab | 2018-04-10T19:04:48+00:00
It is an old issue from 2016: https://github.com/monero-project/monero/issues/647
I confirm that compiling Monero with the fork of Unbound (`git clone --recursive https://github.com/monero-project/monero`) works well on CentOS 7, gcc 7.2.1, cmake 3.6.3.
Also I confirm that Monero won't build with Unbound 1.4.20 from CentOS repos.


## moneromooo-monero | 2018-04-11T10:54:10+00:00
https://github.com/monero-project/monero/pull/3601

## moneromooo-monero | 2018-04-12T11:54:34+00:00
+resolved

# Action History
- Created by: NmxMilk | 2018-04-03T07:44:41+00:00
- Closed at: 2018-04-12T11:56:55+00:00
