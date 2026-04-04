---
title: 'Compile monerod for SunOS (SmartOS) - warnings - relocation warning: R_AMD64_PC32'
source_url: https://github.com/monero-project/monero/issues/5804
author: kayront
assignees: []
labels: []
created_at: '2019-08-10T19:02:36+00:00'
updated_at: '2022-04-08T16:29:49+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
No idea what these mean, and they are only warnings, but they seem fishy.

Any idea what is happening here?

There are many, many lines with stuff similiar to:

```
[ 74%] Linking CXX executable block_fuzz_tests                                                                                                                                                                                                
ld: warning: relocation warning: R_AMD64_PC32: file CMakeFiles/block_fuzz_tests.dir/fuzzer.cpp.o: section [2].rela.text: symbol .LC5: relocation against discarded COMDAT section [52].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                                        
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/cryptonote_basic/libcryptonote_basic.a(account.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [94].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.1: symbol not found, relocation ignored                                                                                                                                                                                     
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/device/libdevice.a(device_default.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [113].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc
.str1.1: symbol not found, relocation ignored                                                                                                                                                                                                 
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/device/libdevice.a(device_default.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [113].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc
.str1.1: symbol not found, relocation ignored                                                                                                                                                                                                 
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/device/libdevice.a(device_default.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [113].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc
.str1.1: symbol not found, relocation ignored                                                                                                                               
```

A bit further down..

```
tr1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/ringct/libringct_basic.a(rctOps.cpp.o): section [2].rela.text: symbol .LC9: relocation against discarded COMDAT section [100].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.s
tr1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/ringct/libringct_basic.a(rctOps.cpp.o): section [2].rela.text: symbol .LC9: relocation against discarded COMDAT section [100].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.s
tr1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/ringct/libringct_basic.a(rctOps.cpp.o): section [2].rela.text: symbol .LC9: relocation against discarded COMDAT section [100].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.s
tr1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/ringct/libringct_basic.a(rctOps.cpp.o): section [2].rela.text: symbol .LC9: relocation against discarded COMDAT section [100].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.s
tr1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/common/libcommon.a(util.cpp.o): section [2].rela.text: symbol .LC11: relocation against discarded COMDAT section [141].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.str
1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/common/libcommon.a(util.cpp.o): section [2].rela.text: symbol .LC11: relocation against discarded COMDAT section [141].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.str
1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../src/common/libcommon.a(util.cpp.o): section [2].rela.text: symbol .LC11: relocation against discarded COMDAT section [141].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.str
1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../contrib/epee/src/libepee.a(mlog.cpp.o): section [2].rela.text: symbol .LC4: relocation against discarded COMDAT section [105].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.
str1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../contrib/epee/src/libepee.a(mlog.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [116].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.
1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../contrib/epee/src/libepee.a(mlog.cpp.o): section [2].rela.text: symbol .LC5: relocation against discarded COMDAT section [105].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.
str1.1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../contrib/epee/src/libepee.a(mlog.cpp.o): section [2].rela.text: symbol .LC8: relocation against discarded COMDAT section [116].gnu.linkonce.r._ZN2el4base14MessageBuilderlsEPKc.str1.
1: symbol not found, relocation ignored
ld: warning: relocation warning: R_AMD64_PC32: file ../../contrib/epee/src/libepee.a(mlog.cpp.o): section [2].rela.text: symbol .LC5: relocation against discarded COMDAT section [105].gnu.linkonce.r._ZNK5boost6system12system_error4whatEv.
str1.1: symbol not found, relocation ignored
```

.. and so on.

I can produce a full log these snippets are not enough of a clue.

# Discussion History
## notmike-5 | 2019-08-14T20:02:05+00:00
Did you download GNU ld and make after linking to your copy of GNU ld?

That is,

mkdir -p build/release
cd build/release
cmake -DCMAKE_LINKER=/path/to/ld -D CMAKE_BUILD_TYPE=Release ../..
cd ../..

(see: https://everycity.co.uk/alasdair/2011/03/using-the-gnu-ld-linker-on-solaris/) 

## selsta | 2022-04-08T16:29:40+00:00
@kayront did you see @notmike-5 reply?  Did it help?

# Action History
- Created by: kayront | 2019-08-10T19:02:36+00:00
