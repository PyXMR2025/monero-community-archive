---
title: Build fails on Ubtunu 16.04 AMD64 - miniupnpc issue?
source_url: https://github.com/monero-project/monero/issues/3111
author: qskousen
assignees: []
labels: []
created_at: '2018-01-13T23:45:24+00:00'
updated_at: '2018-01-13T23:52:59+00:00'
type: issue
status: closed
closed_at: '2018-01-13T23:52:59+00:00'
---

# Original Description
When building from a clean version of master, make returns this error:

<code>
[ 48%] Linking CXX executable ../../bin/monerod
/usr/bin/ld: ../../external/miniupnpc/libminiupnpc.a(miniupnpc.c.o): relocation R_X86_64_32 against `.rodata.str1.1' can not be used when making a shared object; recompile with -fPIC
../../external/miniupnpc/libminiupnpc.a: error adding symbols: Bad value
collect2: error: ld returned 1 exit status
</code>



# Discussion History
## SpliffyMap | 2018-01-13T23:47:31+00:00
Here you go not merged yet fixes #3103 & #3099 :+1: 
I was having problems with server nodes, so added same code #3103 to /external/unbound/CMakeLists.txt 

## qskousen | 2018-01-13T23:52:59+00:00
that was fast. thank you!

# Action History
- Created by: qskousen | 2018-01-13T23:45:24+00:00
- Closed at: 2018-01-13T23:52:59+00:00
