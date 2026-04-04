---
title: compiling Dependencies as Static
source_url: https://github.com/monero-project/monero/issues/4046
author: ghost
assignees: []
labels:
- invalid
created_at: '2018-06-23T22:42:25+00:00'
updated_at: '2019-04-21T19:43:41+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:48:59+00:00'
---

# Original Description
I have an issue of trying to compile the Monero wallet on older i5 Ubuntu 16.04
Server edition machine. I was able to compile xmr on my I5 ubuntu version 18 after installing all of the Dependencies. However upon repeating the same on this process on the Server machine, it complains "**/usr/bin/ld: /usr/lib/gcc/x86_64-linux-gnu/5/../../../x86_64-linux-gnu/libboost_chrono.a(chrono.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC**" Reading the docs, it stated the Dependencies need to compiled static using the gcc -fPIC flag. any suggestions on how to do this or resolve this problem?

Thank you.

# Discussion History
## moneromooo-monero | 2018-06-24T08:13:43+00:00
To build boost with -fPIC, read boost docs.
Typically, for most software, you set custom CFLAGS when configuring.

## moneromooo-monero | 2018-08-15T11:16:24+00:00
+invalid

## blackrangersoftware | 2019-04-21T19:38:14+00:00
https://github.com/monero-project/monero/issues/4019

This is a duplicate of the issue in 4019 and 3099, and yet the code I pulled again last night still produces this error.

Why then, isn't the code set to always look for the built-in version of gtest with the suggested switch -fPIC??

None has ever answered the gentleman's question about where to place that switch. Just a few remarks about it being "normal" to add switches does not help.

Folks are looking for details and should be able to rely on the community for straight answer and solutions not simply sent on their way to go figure out what some "techie" meant.

# Action History
- Created by: ghost | 2018-06-23T22:42:25+00:00
- Closed at: 2018-08-15T11:48:59+00:00
