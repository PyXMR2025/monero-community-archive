---
title: boost library functions undefined reference
source_url: https://github.com/monero-project/monero-gui/issues/870
author: Cherisher
assignees: []
labels:
- resolved
created_at: '2017-09-11T02:47:01+00:00'
updated_at: '2018-07-17T14:00:30+00:00'
type: issue
status: closed
closed_at: '2018-07-17T14:00:30+00:00'
---

# Original Description
I try to built this project many times on Windows 7,  but it is always failed. The error messages is boost library functions undefined reference.  such as:

C:/msys64/home/admin/monero-core/monero/lib/libwallet_merged.a(wallet_manager.cp                                                                                                    p.obj):wallet_manager.cpp:(.text$_ZN5boost16re_detail_10620012perl_matcherIN9__g                                                                                                    nu_cxx17__normal_iteratorIPKcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE                                                                                                    EEESaINS_9sub_matchISC_EEENS_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_i                                                                                                    mpEv[__ZN5boost16re_detail_10620012perl_matcherIN9__gnu_cxx17__normal_iteratorIP                                                                                                    KcNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEEEESaINS_9sub_matchISC_EEEN                                                                                                    S_12regex_traitsIcNS_16cpp_regex_traitsIcEEEEE8find_impEv]+0x293): undefined ref                                                                                                    erence to `boost::re_detail_106200::put_mem_block(void*)'


# Discussion History
## MaxXor | 2017-09-11T11:00:02+00:00
See #828 

## sanderfoobar | 2018-07-17T13:58:06+00:00
+resolved

# Action History
- Created by: Cherisher | 2017-09-11T02:47:01+00:00
- Closed at: 2018-07-17T14:00:30+00:00
