---
title: Mining occasionaly causes monerod to quietly crash
source_url: https://github.com/seraphis-migration/monero/issues/277
author: redsh4de
assignees: []
labels: []
created_at: '2025-12-29T21:56:23+00:00'
updated_at: '2026-01-11T01:32:01+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When starting mining with monerod, sometimes the node quietly crashes without any explicit error logs. Before the crash happened, the memory usage dropped down to 0.1MB, stayed there for 5-10 seconds, after which the node exited.

Below are logs of 5 runs of `v0.19.0.0-alpha.1.4-12d485e84` that ended with a crash a while after running the `start_mining` command.

[mining-level2-0.log](https://github.com/user-attachments/files/24374795/mining-level2-0.log)
[mining-level2-1.log](https://github.com/user-attachments/files/24374799/mining-level2-1.log)
[mining-level2-2.log](https://github.com/user-attachments/files/24374794/mining-level2-2.log)
[mining-level2-3.log](https://github.com/user-attachments/files/24374816/mining-level2-3.log)
[mining-level2-4.log](https://github.com/user-attachments/files/24374817/mining-level2-4.log)

On `v0.19.0.0-alpha.1.4-a3f5c7a28`, the same crash occured, but this time with an error dialog.
<img width="410" height="185" alt="Image" src="https://github.com/user-attachments/assets/b6ad65cc-4018-4971-971d-e30608264365" />

### Specs
OS: Windows 11
CPU: Ryzen 9950X3D
RAM:  64 GB DDR5

# Discussion History
## j-berman | 2025-12-29T22:12:35+00:00
Thank you! Can you link where you got `v0.19.0.0-alpha.1.4-12d485e84` from?

## redsh4de | 2025-12-29T22:15:42+00:00
Here's the action run @j-berman: https://github.com/seraphis-migration/monero/actions/runs/20469720792

## vtnerd | 2026-01-11T01:32:01+00:00
Address sanitizer in clang-21 is reporting an issue with RandomX in `master` and `fcmp++-alpha-stressnet`. The `release-v0.18` branch seems fine. Now I just have to find what changed between these branches.

Output from asan on `master` branch:
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==23293==ERROR: AddressSanitizer: SEGV on unknown address 0x7b2127001ff8 (pc 0x5597c57506c2 bp 0x7b2127731610 sp 0x7b2127731560 T29)
==23293==The signal is caused by a READ memory access.
    #0 0x5597c57506c2 in randomx::CompiledVm<randomx::LargePageAllocator, false, true>::execute() (/home/monero/clang-21-asan/bin/monerod+0x1ce66c2)
    #1 0x5597c574baba in randomx_calculate_hash (/home/monero/clang-21-asan/bin/monerod+0x1ce1aba)
    #2 0x5597c50e9dd1 in rx_slow_hash (/home/monero/clang-21-asan/bin/monerod+0x167fdd1)
    #3 0x5597c508db59 in cryptonote::get_block_longhash(cryptonote::Blockchain const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char>> const&, crypto::hash&, unsigned long, int, crypto::hash const*, int) (/home/monero/clang-21-asan/bin/monerod+0x1623b59)
    #4 0x5597c508e168 in cryptonote::get_block_longhash(cryptonote::Blockchain const*, cryptonote::block const&, unsigned long, crypto::hash const*, int) (/home/monero/clang-21-asan/bin/monerod+0x1624168)
    #5 0x5597c4f77246 in cryptonote::Blockchain::block_longhash_worker(unsigned long, epee::span<cryptonote::block const> const&, std::unordered_map<crypto::hash, crypto::hash, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, crypto::hash>>>&) const (/home/monero/clang-21-asan/bin/monerod+0x150d246)
    #6 0x5597c52409b5 in tools::threadpool::run(bool) (/home/monero/clang-21-asan/bin/monerod+0x17d69b5)
    #7 0x7f264dc8839f  (/usr/lib64/libboost_thread.so.1.88.0+0xa39f)
    #8 0x5597c4335e4a in asan_thread_start(void*) asan_interceptors.cpp.o
    #9 0x7f264d166f90  (/lib64/libc.so.6+0x93f90)
    #10 0x7f264d1d838b  (/lib64/libc.so.6+0x10538b)

==23293==Register values:
rax = 0x00007d064c08f728  rbx = 0x00007b2127731580  rcx = 0x00000fa0c9811ee5  rdx = 0x0000000000000005  
rdi = 0x00007d064c08ec80  rsi = 0x0000000000013000  rbp = 0x00007b2127731610  rsp = 0x00007b2127731560  
 r8 = 0x00007b2127002000   r9 = 0x00007b2127002cd9  r10 = 0x00000f64a4df8598  r11 = 0x0000000000000202  
r12 = 0x00000fa0c9811d90  r13 = 0x00007b20eb58f530  r14 = 0x00007d064c08ec80  r15 = 0x00007d064c08f540  
AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV (/home/monero/clang-21-asan/bin/monerod+0x1ce66c2) in randomx::CompiledVm<randomx::LargePageAllocator, false, true>::execute()
Thread T29 created by T16 here:
    #0 0x5597c431ccd1 in pthread_create (/home/monero/clang-21-asan/bin/monerod+0x8b2cd1)
    #1 0x7f264dc87082 in boost::thread::start_thread_noexcept(boost::thread_attributes const&) (/usr/lib64/libboost_thread.so.1.88.0+0x9082)

Thread T16 created by T0 here:
    #0 0x5597c431ccd1 in pthread_create (/home/monero/clang-21-asan/bin/monerod+0x8b2cd1)
    #1 0x7f264dc87082 in boost::thread::start_thread_noexcept(boost::thread_attributes const&) (/usr/lib64/libboost_thread.so.1.88.0+0x9082)

==23293==ABORTING
```

# Action History
- Created by: redsh4de | 2025-12-29T21:56:23+00:00
