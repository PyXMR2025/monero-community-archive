---
title: Exceptions in log
source_url: https://github.com/monero-project/monero/issues/8790
author: andrew-jman
assignees: []
labels: []
created_at: '2023-03-20T12:43:46+00:00'
updated_at: '2025-09-29T06:14:35+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:02:44+00:00'
---

# Original Description
A lot of std::bad_alloc exceptions in monerod log (stack trace is below). monerod is still working.

Running monerod version release-v0.18 on Debian x64 10.13.
Run command: /usr/local/bin/monerod --restricted-rpc --block-sync-size 3 --confirm-external-bind --config-file /home/satoshi/.bitmonero/monerod.conf --detach

monerod.conf content:
data-dir=/home/satoshi/.bitmonero data-dir=/home/satoshi/.bitmonero
log-file=/home/satoshi/.bitmonero/monero.log
log-level=0

Strace log:

2023-03-20 12:22:22.615	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-03-20 12:22:59.618	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-03-20 12:22:59.618	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0x11c) [0x558dd31ad740]:__cxa_throw+0x11c) [0x558dd31ad740]
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] /usr/local/bin/monerod(+0x710861) [0x558dd3819861] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] /usr/local/bin/monerod(+0x708322) [0x558dd3811322] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] /usr/local/bin/monerod(+0x7058e3) [0x558dd380e8e3] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] /usr/local/bin/monerod(+0x4e2e85) [0x558dd35ebe85] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] /usr/local/bin/monerod(+0x4e3df4) [0x558dd35ecdf4] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] /usr/local/bin/monerod(+0x4cd012) [0x558dd35d6012] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] /usr/local/bin/monerod(+0x4cd1ca) [0x558dd35d61ca] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] /usr/local/bin/monerod(+0x4cd263) [0x558dd35d6263] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] /usr/local/bin/monerod(+0x47ccd8) [0x558dd3585cd8] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] /usr/local/bin/monerod(+0x5240a8) [0x558dd362d0a8] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/local/bin/monerod(+0x524a4a) [0x558dd362da4a] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/local/bin/monerod(+0x4806ae) [0x558dd35896ae] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /usr/local/bin/monerod(+0x4a05df) [0x558dd35a95df] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] /usr/local/bin/monerod(+0x42cf0a) [0x558dd3535f0a] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /usr/local/bin/monerod(+0x17feb0) [0x558dd3288eb0] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /usr/local/bin/monerod(+0x1823cd) [0x558dd328b3cd] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] /usr/local/bin/monerod(+0x40baf9) [0x558dd3514af9] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] /usr/local/bin/monerod(+0x40da79) [0x558dd3516a79] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] /usr/local/bin/monerod(+0x124725) [0x558dd322d725] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21] /usr/local/bin/monerod(+0x125381) [0x558dd322e381] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/local/bin/monerod(+0x12b801) [0x558dd3234801] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/local/bin/monerod(+0x3d00fc) [0x558dd34d90fc] 
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24]  0x14615) [0x7fc103caf615]:_64-linux-gnu/libboost_thread.so.1.67.0(+0x14615) [0x7fc103caf615]
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [25]  0x7fa3) [0x7fc10391cfa3]:_64-linux-gnu/libpthread.so.0(+0x7fa3) [0x7fc10391cfa3]
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [26]  0x3f) [0x7fc10384e06f]:_64-linux-gnu/libc.so.6(clone+0x3f) [0x7fc10384e06f]
2023-03-20 12:22:59.619	[P2P2]	INFO	stacktrace	src/common/stack_trace.cpp:172	



# Discussion History
## Veeeetzzzz | 2023-03-31T20:13:22+00:00
It could just be a local system issue that's causing the memory errors - I would post your system/install specifications if you can, perhaps someone can attempt to replicate and fix. Would be curious to know how much RAM you have/is being used by any Monero processes. Is it all physical or hybrid w/ swap space, what split?

What do these values say in monerod settings?

block-sync-size
db-sync-mode

If there is a memory leak, it shouldn't be too hard to replicate.

## selsta | 2023-03-31T20:36:49+00:00
What kind of hardware do you have? Why did you set `block-sync-size 3` for example?

## salimathel | 2023-04-05T03:44:02+00:00
Hello. I'm posting here because I'm testing the occurrence of this issue, since it also affects me. It is important to note that this issue did **NOT** happen for me with the official binaries, but it did happen in all other scenarios I've tested. I know this sounds weird, but also note that OP here (@andrew-jman) wrote: "Running monerod version release-v0.18" - Although I can't be sure, this does suggests he isn't using the official binaries, but rather that he is using a version of Monero from the `release-v0.18` branch he compiled locally on his machine. OP, correct me if this is a wrong assumption, but in case this is true, this does match with my results.

Below is a more detailed explanation of the issue and how I tested it:

Issue: `bitmonero.log` gets flooded with `std::bad_alloc` exceptions (as OP mentioned), and for me `boost::wrapexcept<boost::bad_weak_ptr>` exceptions also appear. The `free` command showed I always had enough free memory (6 GB or more) during the generation of these logs to reasonably conclude this is not a lack of memory issue (and there was no data being written to the swap on disk). But there is a very important catch here, this issue does **NOT** seem to happen with the official binaries, but it did happen in every other scenario I've tested.

I always run monerod with the default arguments, except with a different `--data-dir` because I have the blockchain stored on another internal SSD. I also always have the P2P port (18080) open to incoming connections, but I don't know if this is relevant here.

I've tested on 2 different Linux distros (Arch Linux and Linux Mint 20.3 - based on Ubuntu 20.04), and compiled 4 different versions of Monero ( `v0.18.0.0` , `v0.18.1.2`, `v0.18.2.0` and `v0.18.2.2` ). I've also tested the pre-compiled binaries from the Arch Linux repositories (currently `v0.18.2.0`). In all these scenarios, the exceptions I mentioned earlier start showing up in the log file right after starting monerod. Here is what the log file looks like in all these scenarios:

```
2023-04-04 19:52:26.599	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:52:26.599	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x505168) [0x562b47654168] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x50b61b) [0x562b4765a61b] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e43c7) [0x562b473333c7] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [24] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:52:26.600	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:52:26.971	[P2P8]	INFO	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1686	Synced 2857120/2857120
2023-04-04 19:53:31.535	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:53:31.535	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:53:31.535	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:53:31.536	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:53:44.983	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:53:44.984	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:54:03.856	    7f47cb7fe6c0	INFO	msgwriter	src/common/scoped_message_writer.h:102	Height: 2857122/2857122 (100.0%) on mainnet, not mining, net hash 2.51 GH/s, v16, 12(out)+10(in) connections, uptime 0d 0h 2m 23s
2023-04-04 19:54:25.548	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:54:25.548	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:54:25.549	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:55:14.231	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:55:14.232	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x91edc) [0x562b471e0edc] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x45d817) [0x562b475ac817] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x48d2be) [0x562b475dc2be] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x47615f) [0x562b475c515f] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x4897ee) [0x562b475d87ee] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x49058f) [0x562b475df58f] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x4c88a6) [0x562b476178a6] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x4c8d3b) [0x562b47617d3b] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x12e9ea) [0x562b4727d9ea] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x45da32) [0x562b475aca32] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x4ac5d0) [0x562b475fb5d0] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:56:52.660	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 19:58:49.942	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 19:58:49.942	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 19:58:49.943	[P2P6]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:00:53.021	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:00:53.021	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:00:53.021	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:00:53.022	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:03:57.172	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:03:57.172	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:03:57.173	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:04:06.582	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:04:06.582	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:04:06.582	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:04:06.582	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:04:06.582	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:04:06.583	[P2P3]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:04:12.775	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:07:37.788	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-04-04 20:07:37.788	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x91edc) [0x562b471e0edc] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x45d817) [0x562b475ac817] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x48d2be) [0x562b475dc2be] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x4571f0) [0x562b475a61f0] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x459da7) [0x562b475a8da7] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x493a5e) [0x562b475e2a5e] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x4a58c9) [0x562b475f48c9] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:07:37.793	[P2P5]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:08:05.313	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:08:05.314	[P2P9]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:10:55.978	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:10:55.978	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:10:55.979	[P2P4]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:11:35.060	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:11:35.060	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:11:35.061	[P2P8]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:15:36.423	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>
2023-04-04 20:15:36.423	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x91edc) [0x562b471e0edc] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x45d817) [0x562b475ac817] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x479f01) [0x562b475c8f01] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x44c9c1) [0x562b4759b9c1] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x4f57f3) [0x562b476447f3] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x459fb7) [0x562b475a8fb7] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x49373e) [0x562b475e273e] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x4a50f9) [0x562b475f40f9] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:15:36.424	[P2P7]	INFO	stacktrace	src/common/stack_trace.cpp:172	
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: std::bad_alloc
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:134	Unwound call stack:
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [1]  0xaf) [0x562b47206cab]:__cxa_throw+0xaf) [0x562b47206cab]
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [2] ./monerod(+0x115b86) [0x562b47264b86] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [3] ./monerod(+0x871982) [0x562b479c0982] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [4] ./monerod(+0x86ec73) [0x562b479bdc73] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [5] ./monerod(+0x5c7755) [0x562b47716755] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [6] ./monerod(+0x5c930b) [0x562b4771830b] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [7] ./monerod(+0x5ade85) [0x562b476fce85] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [8] ./monerod(+0x544ecf) [0x562b47693ecf] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [9] ./monerod(+0x618430) [0x562b47767430] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [10] ./monerod(+0x6187ec) [0x562b477677ec] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [11] ./monerod(+0x54a2fa) [0x562b476992fa] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [12] ./monerod(+0x574922) [0x562b476c3922] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [13] ./monerod(+0x4e419d) [0x562b4763319d] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [14] ./monerod(+0x1e48b0) [0x562b473338b0] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [15] ./monerod(+0x1e6805) [0x562b47335805] 
2023-04-04 20:16:15.370	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [16] ./monerod(+0x4cc2ec) [0x562b4761b2ec] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [17] ./monerod(+0x4cdf17) [0x562b4761cf17] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [18] ./monerod(+0x164e75) [0x562b472b3e75] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [19] ./monerod(+0x440fd3) [0x562b4758ffd3] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [20] ./monerod(+0x47f372) [0x562b475ce372] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [21]  0xfcbb) [0x7f7284dfdcbb]:_thread.so.1.81.0(+0xfcbb) [0x7f7284dfdcbb]
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [22] /usr/lib/libc.so.6(+0x85bb5) [0x7f728429ebb5] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	    [23] /usr/lib/libc.so.6(+0x107d90) [0x7f7284320d90] 
2023-04-04 20:16:15.371	[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:172	
```

But the weird thing is that doesn't seem to happen with the official binaries. 

@selsta Any idea of what's going on? Can you or someone else please try to replicate this?

## selsta | 2023-04-05T11:08:36+00:00
@salimathel Release binaries don't have libunwind, which means they don't print a stack trace on uncaught exceptions.

## salimathel | 2023-04-05T13:45:29+00:00
@selsta That makes total sense.

Still, can anyone replicate this while running monerod compiled with libunwind? For me, it happens basically all the time non-stop.

And should we be concerned about this?

## selsta | 2023-04-05T14:06:41+00:00
`boost::wrapexcept<boost::bad_weak_ptr>` is known and can be ignored. I don't know about bad_alloc currently, are you mining? Do you have any issues apart from the log message?

## salimathel | 2023-04-05T18:27:41+00:00
@selsta No, I'm not mining to this node. And even if I reboot and run only monerod (mining disabled) and nothing more, same thing happens.

Good to know `boost::wrapexcept<boost::bad_weak_ptr>` can be ignored, but `std::bad_alloc` is even more common in the logs. Basically, there is at least one bad_alloc each 5 minutes monerod is running. 

If I had other issues? Well, yes, about a week ago monerod simply wouldn't sync at random times, it would display a ton of messages of "syncronization started" and "new top block candidate", but it would not sync blocks. Similar to issue #8814 , but monerod never crashed or "exited by itself". Restarting monerod did not solve the issue, but rebooting the machine usually did. Then I started to run monerod with `--db-salvage` sometimes, then monerod would simply start normally and work normally. I'm not sure if this is solved already, but it hasn't happen again during this short period of time. However, sometimes monerod still displays some weird error messages like:
```
2023-04-05 09:17:28.031	E Error retrieving blocks, missed 3 transactions for block with hash: <bda4f9865944e49a430d31b6cc1b3bf8e4d8d4f4d16847366d005c624dd40390>
2023-04-05 09:40:54.567	W DB error attempting to fetch tx from hashMDB_CORRUPTED: Located page was wrong type
2023-04-05 09:40:54.570	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.570	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.571	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.571	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.572	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.572	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.573	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.573	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.574	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.574	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.575	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:40:54.575	W DB error attempting to fetch tx from hashMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
2023-04-05 09:46:59.872	E Error retrieving blocks, missed 8 transactions for block with hash: <03f7b71c3b555a2daa3c3d858979154a89fa43b32afe356c8a07866b31f12bff>
2023-04-05 13:54:18.494	E Error retrieving blocks, missed 3 transactions for block with hash: <18659856dddc309e8d5df436ae0375d51b395aa09e1f668563ca67df480f63cd>
```
 Those error messages appear sometimes but not always (like once a day, or once every 6-20 hours, something like that), but monerod still syncs nonetheless. 

I guess I could try running monerod for longer, and try comparing running it with the P2P port (18080) closed to incoming connections, and see if that makes a difference. It's pretty normal for my node to get between 80 to 120 incoming connections, and my system tends to keep allocating memory as buff/cache as long as monerod is running (according to `free`, basically all this memory is marked as "available", but it isn't "free memory" anymore - I have no idea if this is relevant or not).

But then again, the `std::bad_alloc` exceptions always keep showing up all the time, even right after starting monerod after a reboot, with lots of free memory, not mining, and nothing else running on the system. So I really don't know.

## salimathel | 2023-04-05T19:13:49+00:00
@selsta update: closing the P2P port also changed nothing. Same thing, at least 1 `std::bad_alloc` each 5 minutes (in reality it's more frequent than that).

## moneromooo-monero | 2023-04-05T20:16:55+00:00
It's likely from randomx. Run with gdb, run "catch throw" in gdb, "bt" when it breaks, "cont" to continue till next break.

## salimathel | 2023-04-06T02:18:32+00:00
@moneromooo-monero Ok, so this was actually my first time using gdb. I did like you said, (using monerod from the Arch repos) and this was the result:
```
GNU gdb (GDB) 13.1
Copyright (C) 2023 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-pc-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<https://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from monerod...

This GDB supports auto-downloading debuginfo from the following URLs:
  <https://debuginfod.archlinux.org>
Enable debuginfod for this session? (y or [n]) y
Debuginfod has been enabled.
To make this setting permanent, add 'set debuginfod enabled on' to .gdbinit.
Reading symbols from /home/coder/.cache/debuginfod_client/c5a56f64d187384f1afa2947c031d9efcfd97178/debuginfo...
(gdb) catch throw 
Catchpoint 1 (throw)
(gdb) run
Starting program: /usr/bin/monerod 
Downloading separate debug info for system-supplied DSO at 0x7ffff7fc8000...
Downloading separate debug info for /usr/lib/libzmq.so.5...
Downloading separate debug info for /usr/lib/libsodium.so.23...
Downloading separate debug info for /usr/lib/libunbound.so.8...
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/usr/lib/libthread_db.so.1".
Downloading separate debug info for /usr/lib/libpgm-5.3.so.0...
Downloading separate debug info for /usr/lib/libprotobuf-c.so.1...
2023-04-06 01:58:49.948	I Monero 'Fluorine Fermi' (v0.18.2.0-release)
2023-04-06 01:58:49.948	I Initializing cryptonote protocol...
2023-04-06 01:58:49.948	I Cryptonote protocol initialized OK
2023-04-06 01:58:49.949	I Initializing core...
2023-04-06 01:58:49.949	I Loading blockchain from folder /media/coder/XrayDisk/Monero/blockchain/lmdb ...
[New Thread 0x7fd55e5ff6c0 (LWP 7789)]
[New Thread 0x7fd55ddfe6c0 (LWP 7790)]
[New Thread 0x7fd55d5fd6c0 (LWP 7791)]
[Switching to Thread 0x7fd55ddfe6c0 (LWP 7790)]

Thread 3 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd558009130, tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
Downloading source file /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc...
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd558009130, 
    tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd558009130, info=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x000055555564a49d in randomx::InterpretedLightVm<randomx::AlignedAllocator<64ul>, true>::operator new(unsigned long) [clone .part.0] [clone .lto_priv.0] (size=<optimized out>)
    at /usr/src/debug/monero/monero/external/randomx/src/vm_interpreted_light.hpp:44
#3  0x000055555564a4a2 in randomx::LargePageAllocator::allocMemory (count=268435456)
    at /usr/src/debug/monero/monero/external/randomx/src/randomx.cpp:110
#4  randomx_alloc_cache (flags=<optimized out>)
    at /usr/src/debug/monero/monero/external/randomx/src/randomx.cpp:103
#5  0x000055555592e094 in rx_alloc_cache (flags=flags@entry=106, 
    cache=cache@entry=0x555555e75d80 <main_cache>)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:232
#6  0x000055555593060d in rx_set_main_seedhash_thread (arg=0x555555fcc460)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:372
#7  0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#8  0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
[New Thread 0x7fd55d0fc6c0 (LWP 7812)]
[New Thread 0x7fd55cbfb6c0 (LWP 7813)]
2023-04-06 01:59:03.440	I Loading checkpoints
2023-04-06 01:59:03.441	I Core initialized OK
2023-04-06 01:59:03.441	I Initializing p2p server...
2023-04-06 01:59:03.462	I p2p server initialized OK
2023-04-06 01:59:03.463	I Initializing core RPC server...
2023-04-06 01:59:03.463	I Binding on 127.0.0.1 (IPv4):18081
2023-04-06 01:59:03.535	I core RPC server initialized OK on port: 18081
[New Thread 0x7fd547ffe6c0 (LWP 7814)]
[New Thread 0x7fd5477fd6c0 (LWP 7815)]
[New Thread 0x7fd546ffc6c0 (LWP 7816)]
2023-04-06 01:59:03.538	I Starting core RPC server...
[New Thread 0x7fd5467fb6c0 (LWP 7817)]
[New Thread 0x7fd545ffa6c0 (LWP 7818)]
2023-04-06 01:59:03.539	I core RPC server started ok
[New Thread 0x7fd5457f96c0 (LWP 7819)]
[New Thread 0x7fd544ff86c0 (LWP 7820)]
[New Thread 0x7fd52ffff6c0 (LWP 7821)]
2023-04-06 01:59:03.542	I Starting p2p net loop...
[New Thread 0x7fd52f7fe6c0 (LWP 7822)]
[New Thread 0x7fd5447f76c0 (LWP 7823)]
[New Thread 0x7fd52effd6c0 (LWP 7824)]
[New Thread 0x7fd52eafc6c0 (LWP 7825)]
[New Thread 0x7fd52e5fb6c0 (LWP 7826)]
[New Thread 0x7fd52e0fa6c0 (LWP 7827)]
[New Thread 0x7fd52dbf96c0 (LWP 7828)]
[New Thread 0x7fd52d6f86c0 (LWP 7829)]
[New Thread 0x7fd52d1f76c0 (LWP 7830)]
[New Thread 0x7fd52ccf66c0 (LWP 7831)]
[New Thread 0x7fd52c7f56c0 (LWP 7832)]
[Thread 0x7fd55ddfe6c0 (LWP 7790) exited]
2023-04-06 01:59:04.543	I 
2023-04-06 01:59:04.543	I **********************************************************************
2023-04-06 01:59:04.543	I The daemon will start synchronizing with the network. This may take a long time to complete.
2023-04-06 01:59:04.543	I 
2023-04-06 01:59:04.543	I You can set the level of process detailization through "set_log <level|categories>" command,
2023-04-06 01:59:04.543	I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
2023-04-06 01:59:04.543	I 
2023-04-06 01:59:04.543	I Use the "help" command to see the list of available commands.
2023-04-06 01:59:04.543	I Use "help <command>" to see a command's documentation.
2023-04-06 01:59:04.543	I **********************************************************************
2023-04-06 01:59:04.545	W Unable to send transaction(s), no available connections
[New Thread 0x7fd4f3fff6c0 (LWP 7833)]
[New Thread 0x7fd4f3afe6c0 (LWP 7834)]
[New Thread 0x7fd4f35fd6c0 (LWP 7835)]
[New Thread 0x7fd4f30fc6c0 (LWP 7836)]
[New Thread 0x7fd4f2bfb6c0 (LWP 7837)]
[New Thread 0x7fd4f26fa6c0 (LWP 7838)]
[New Thread 0x7fd4f21f96c0 (LWP 7839)]
2023-04-06 01:59:05.120	I [91.198.115.45:18280 OUT] Sync data returned a new top block candidate: 2858023 -> 2858024 [Your node is 1 blocks (2.0 minutes) behind] 
2023-04-06 01:59:05.120	I SYNCHRONIZATION started
[Switching to Thread 0x7fd52ccf66c0 (LWP 7831)]

Thread 24 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd4f400d160, tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
81	in /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd4f400d160, 
    tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd4f400d160, info=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x000055555564a49d in randomx::InterpretedLightVm<randomx::AlignedAllocator<64ul>, true>::operator new(unsigned long) [clone .part.0] [clone .lto_priv.0] (size=<optimized out>)
    at /usr/src/debug/monero/monero/external/randomx/src/vm_interpreted_light.hpp:44
#3  0x000055555564a60e in randomx::LargePageAllocator::allocMemory (count=2097152)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:108
#4  randomx::VmBase<randomx::LargePageAllocator, false>::allocate (this=0x7fd4f402e500)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:114
#5  0x0000555555a99c2b in randomx_create_vm (flags=<optimized out>, cache=0x7fd558000cb0, dataset=0x0)
    at /usr/src/debug/monero/monero/external/randomx/src/randomx.cpp:325
#6  0x000055555592e1c7 in rx_init_light_vm (cache=0x7fd558000cb0, vm=0x7fd52ccf6670, flags=122)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:277
#7  rx_init_light_vm (flags=<optimized out>, vm=0x7fd52ccf6670, cache=0x7fd558000cb0)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:264
#8  0x000055555592f09e in rx_slow_hash (seedhash=<optimized out>, data=0x7fd4f400c530, length=76, 
    result_hash=0x7fd52ccf3b00 "") at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:429
#9  0x0000555555b5d020 in cryptonote::get_block_longhash(cryptonote::Blockchain const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, crypto::hash&, unsigned long, int, crypto::hash const*, int) [clone .constprop.0] (pbc=pbc@entry=0x555555fafbf0, 
    bd="\020\020\253\315\270\241\006\305B\275\265\347\"\366\2578bJ\364\001\350\034\031E\335\005Z\245eQi\365\257\033[\026n\300\334~\016\0000\3536\267\215\r\027*\"- \251\317\334\337ɕ\220Tp\002H\231\263\342\363L\236_\347\3070\256\026", res=..., height=height@entry=2858023, major_version=<optimized out>, 
    seed_hash=seed_hash@entry=0x0, miners=<optimized out>)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:698
#10 0x000055555590256a in cryptonote::get_block_longhash (miners=<optimized out>, seed_hash=0x0, 
    height=2858023, res=..., b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:709
#11 cryptonote::get_block_longhash (seed_hash=0x0, miners=0, height=2858023, b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:715
#12 cryptonote::Blockchain::block_longhash_worker (this=0x555555fafbf0, height=2858024, blocks=..., 
    map=std::unordered_map with 0 elements)
    at /usr/src/debug/monero/monero/src/cryptonote_core/blockchain.cpp:4868
#13 0x0000555555956792 in std::function<void ()>::operator()() const (this=<optimized out>, 
    this=<optimized out>) at /usr/include/c++/12.2.1/bits/std_function.h:591
#14 tools::threadpool::run (this=0x555555e75ba0 <tools::threadpool::getInstanceForCompute()::instance>, 
    flush=true) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:169
#15 0x0000555555956c39 in tools::threadpool::waiter::wait (this=0x7fd52ccf4030)
    at /usr/src/debug/monero/monero/src/common/threadpool.cpp:132
#16 0x0000555555909ce7 in cryptonote::Blockchain::prepare_handle_incoming_blocks (this=0x555555fafbf0, 
    blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...})
    at /usr/src/debug/monero/monero/src/cryptonote_core/blockchain.cpp:5241
#17 0x0000555555b17a40 in cryptonote::core::prepare_handle_incoming_blocks(std::vector<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&, std::vector<cryptonote::block, std::allocator<cryptonote::block> >&) [clone .constprop.0] (this=0x555555fafa50, 
    blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...})
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_core.cpp:1623
#18 0x0000555555bfae4d in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) [clone .isra.0] (this=0x555555faf790, context=...)
    at /usr/src/debug/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1512
#19 0x0000555555883764 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects (this=0x555555faf790, command=<optimized out>, arg=..., context=...)
    at /usr/src/debug/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:1325
#20 0x0000555555ad9f13 in std::__invoke_impl<int, int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*&)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*&, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&> (__t=<optimized out>, __f=<optimized out>) at /usr/include/c++/12.2.1/bits/invoke.h:74
#21 std::__invoke<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*&)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*&, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&> (
    __fn=<optimized out>) at /usr/include/c++/12.2.1/bits/invoke.h:96
#22 std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>::__call<int, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&, 0ul, 1ul, 2ul, 3ul>(std::tuple<int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&>&&, std::_Index_tuple<0ul, 1ul, 2ul, 3ul>) (__args=..., this=<optimized out>)
    at /usr/include/c++/12.2.1/functional:495
#23 std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&)>::operator()<int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t> >&, cryptonote::cryptonote_connection_context&, int>(int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t> >&, cryptonote::cryptonote_connection_context&) (this=<optimized out>) at /usr/include/c++/12.2.1/functional:580
#24 epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>, cryptonote::cryptonote_connection_context, std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&)> >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, epee::span<unsigned char const>, std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&)>, cryptonote::cryptonote_connection_context&) (command=2004, powner=0x555555faf790, 
    context=..., cb=..., in_buff=...)
    at /usr/src/debug/monero/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:202
#25 cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context> (this=0x555555faf790, is_notify=is_notify@entry=true, command=command@entry=2004, 
    in_buff=..., context=..., handled=@0x7fd52ccf53df: true, buff_out=...)
    at /usr/src/debug/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.h:92
#26 0x0000555555adbd7c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, epee::byte_stream&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.0] (this=0x555555fb0cd0, is_notify=is_notify@entry=true, 
    command=2004, in_buff=..., buff_out=..., context=..., handled=@0x7fd52ccf53df: true)
    at /usr/src/debug/monero/monero/src/p2p/net_node.h:323
#27 0x000055555576eee9 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify (this=<optimized out>, command=<optimized out>, in_buff=..., context=...)
    at /usr/src/debug/monero/monero/src/p2p/net_node.h:313
#28 0x00005555558b4348 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv (this=0x7fd5140040f8, ptr=<optimized out>, cb=<optimized out>)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/levin_protocol_handler_async.h:557
#29 0x00005555558c19a2 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}::operator()() const (__closure=0x7fd52ccf5720)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:406
#30 boost::asio::asio_handler_invoke<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, ...) (
    function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:88
#31 boost_asio_handler_invoke_helpers::invoke<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&) (context=..., function=...)
    at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#32 boost::asio::detail::handler_work<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul>, void>::complete<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&) (handler=..., function=..., this=<synthetic pointer>)
    at /usr/include/boost/asio/detail/handler_work.hpp:520
#33 boost::asio::detail::completion_handler<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) (
    owner=0x555556023f80, base=0x7fd500000f20) at /usr/include/boost/asio/detail/completion_handler.hpp:74
#34 0x00005555556de985 in boost::asio::detail::scheduler_operation::complete (
    bytes_transferred=<optimized out>, ec=..., owner=<optimized out>, this=<optimized out>, 
    this=<optimized out>, owner=<optimized out>, ec=..., bytes_transferred=<optimized out>)
    at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#35 boost::asio::detail::strand_service::do_complete (owner=0x555556023f80, base=0x7fd514004720, ec=...)
    at /usr/include/boost/asio/detail/impl/strand_service.ipp:193
#36 0x0000555555b45237 in boost::asio::detail::scheduler_operation::complete (
    bytes_transferred=<optimized out>, ec=..., owner=<optimized out>, this=<optimized out>, 
    this=<optimized out>, owner=<optimized out>, ec=..., bytes_transferred=<optimized out>)
    at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#37 boost::asio::detail::scheduler::do_run_one (ec=..., this_thread=..., lock=..., this=0x555556023f80)
    at /usr/include/boost/asio/detail/impl/scheduler.ipp:492
#38 boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .constprop.0] (
    this=0x555556023f80, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#39 0x00005555558a192f in boost::asio::io_context::run (this=<optimized out>)
    at /usr/include/boost/asio/impl/io_context.ipp:63
#40 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555555fe2d60)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#41 0x00007ffff7bfdcbb in boost::(anonymous namespace)::thread_proxy (param=<optimized out>)
    at libs/thread/src/pthread/thread.cpp:179
#42 0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#43 0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
[Switching to Thread 0x7fd5447f76c0 (LWP 7823)]

Thread 16 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd51401a1c0, tinfo=0x555555e61490 <typeinfo for boost::wrapexcept<boost::bad_weak_ptr>>, 
    dest=0x5555556ba100 <boost::wrapexcept<boost::bad_weak_ptr>::~wrapexcept()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
81	in /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd51401a1c0, 
    tinfo=0x555555e61490 <typeinfo for boost::wrapexcept<boost::bad_weak_ptr>>, 
    dest=0x5555556ba100 <boost::wrapexcept<boost::bad_weak_ptr>::~wrapexcept()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd51401a1c0, 
    info=0x555555e61490 <typeinfo for boost::wrapexcept<boost::bad_weak_ptr>>, 
    dest=0x5555556ba100 <boost::wrapexcept<boost::bad_weak_ptr>::~wrapexcept()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x000055555567214f in boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&) [clone .constprop.0] (e=...) at /usr/include/boost/throw_exception.hpp:165
#3  0x0000555555605cb9 in boost::detail::shared_count::shared_count (r=..., this=<synthetic pointer>)
    at /usr/include/boost/smart_ptr/detail/shared_count.hpp:670
#4  boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >
    (r=..., this=<optimized out>, this=<optimized out>, r=...)
    at /usr/include/boost/smart_ptr/shared_ptr.hpp:465
#5  boost::enable_shared_from_this<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::shared_from_this (
    this=<optimized out>, this=<optimized out>)
    at /usr/include/boost/smart_ptr/enable_shared_from_this.hpp:50
#6  epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::add_ref (this=<optimized out>)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1103
#7  0x000055555586b4b1 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::start_outer_call (this=0x7fd51401cc78)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/levin_protocol_handler_async.h:349
#8  epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::foreach_connection<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_peer_used(nodetool::peerlist_entry_base<epee::net_utils::network_address> const&)::{lambda(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&)#1}>(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_peer_used(nodetool::peerlist_entry_base<epee::net_utils::network_address> const&)::{lambda(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&)#1} const&) (cb=..., this=0x555555fe3388)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/levin_protocol_handler_async.h:859
#9  nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_peer_used (
    this=this@entry=0x555555fb0cd0, peer=...) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1283
#10 0x000055555586cfaa in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_new_connection_from_peerlist (this=this@entry=0x555555fb0cd0, zone=..., 
    use_white_list=use_white_list@entry=true) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1691
#11 0x0000555555870e4e in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::make_expected_connections_count (this=0x555555fb0cd0, zone=..., peer_type=<optimized out>, 
    expected_connections=12) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1889
#12 0x0000555555861c51 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker (this=this@entry=0x555555fb0cd0) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1826
#13 0x000055555586171a in boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >::operator() (p=0x555555fb0cd0, this=<synthetic pointer>)
    at /usr/include/boost/bind/mem_fn_template.hpp:49
#14 boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> >::operator()<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list0> (a=<synthetic pointer>..., f=<synthetic pointer>..., 
    this=<synthetic pointer>) at /usr/include/boost/bind/bind.hpp:228
#15 boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > >::operator() (this=<synthetic pointer>)
    at /usr/include/boost/bind/bind.hpp:1273
#16 epee::math_helper::once_a_time<epee::math_helper::get_constant_interval<1000000ul>, true>::do_call<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > (functr=..., this=0x555555fb0db8)
    at /usr/src/debug/monero/monero/contrib/epee/include/math_helper.h:281
#17 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker (
    this=0x555555fb0cd0) at /usr/src/debug/monero/monero/src/p2p/net_node.inl:1999
#18 0x000055555589c831 in boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >::operator() (p=<optimized out>, this=<optimized out>)
    at /usr/include/boost/bind/mem_fn_template.hpp:49
#19 boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> >::operator()<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list0> (a=<synthetic pointer>..., f=..., 
    this=<optimized out>) at /usr/include/boost/bind/bind.hpp:228
#20 boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > >::operator() (this=<optimized out>)
    at /usr/include/boost/bind/bind.hpp:1273
#21 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >::call_handler (this=<optimized out>)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.h:437
#22 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > (this=0x555555fe2d60, ptr=...)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.h:456
#23 0x00005555558b824c in boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >::operator() (this=0x7fd5447f6700, a1=..., p=<optimized out>)
    at /usr/include/boost/bind/mem_fn_template.hpp:165
#24 boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > >::operator()<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::rrlist1<boost::system::error_code const&> > (a=<synthetic pointer>..., f=..., 
    this=0x7fd5447f6710) at /usr/include/boost/bind/bind.hpp:288
#25 boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >::operator()<boost::system::error_code const&> (a1=..., this=0x7fd5447f6700)
    at /usr/include/boost/bind/bind.hpp:1285
#26 boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>::operator() (
    this=0x7fd5447f6700) at /usr/include/boost/asio/detail/bind_handler.hpp:171
#27 boost::asio::asio_handler_invoke<boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code> > (function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:88
#28 boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>, boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > > > (context=..., function=...)
    at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#29 boost::asio::detail::handler_work<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::asio::any_io_executor, void>::complete<boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code> > (handler=..., function=..., 
    this=0x7fd5447f66c0) at /usr/include/boost/asio/detail/handler_work.hpp:520
#30 boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::asio::any_io_executor>::do_complete (
    owner=0x555556023f80, base=<optimized out>) at /usr/include/boost/asio/detail/wait_handler.hpp:76
#31 0x0000555555b45237 in boost::asio::detail::scheduler_operation::complete (
    bytes_transferred=<optimized out>, ec=..., owner=<optimized out>, this=<optimized out>, 
    this=<optimized out>, owner=<optimized out>, ec=..., bytes_transferred=<optimized out>)
    at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#32 boost::asio::detail::scheduler::do_run_one (ec=..., this_thread=..., lock=..., this=0x555556023f80)
    at /usr/include/boost/asio/detail/impl/scheduler.ipp:492
#33 boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .constprop.0] (
    this=0x555556023f80, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#34 0x00005555558a192f in boost::asio::io_context::run (this=<optimized out>)
    at /usr/include/boost/asio/impl/io_context.ipp:63
#35 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555555fe2d60)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#36 0x00007ffff7bfdcbb in boost::(anonymous namespace)::thread_proxy (param=<optimized out>)
    at libs/thread/src/pthread/thread.cpp:179
#37 0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#38 0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
2023-04-06 01:59:45.972	I Synced 2858024/2858024
2023-04-06 01:59:45.972	I 
2023-04-06 01:59:45.972	I **********************************************************************
2023-04-06 01:59:45.972	I You are now synchronized with the network. You may now start monero-wallet-cli.
2023-04-06 01:59:45.972	I 
2023-04-06 01:59:45.972	I Use the "help" command to see the list of available commands.
2023-04-06 01:59:45.972	I **********************************************************************
[New Thread 0x7fd55c6fa6c0 (LWP 7963)]
[New Thread 0x7fd55c1ff6c0 (LWP 7964)]
[New Thread 0x7fd5442f66c0 (LWP 7965)]
[New Thread 0x7fd5441f56c0 (LWP 7966)]
[Thread 0x7fd5442f66c0 (LWP 7965) exited]
[Thread 0x7fd5441f56c0 (LWP 7966) exited]
[Thread 0x7fd55c6fa6c0 (LWP 7963) exited]
[Thread 0x7fd55c1ff6c0 (LWP 7964) exited]
[Switching to Thread 0x7fd52d1f76c0 (LWP 7830)]

Thread 23 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd5000c8a80, tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
81	in /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd5000c8a80, 
    tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd5000c8a80, info=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x000055555564a49d in randomx::InterpretedLightVm<randomx::AlignedAllocator<64ul>, true>::operator new(unsigned long) [clone .part.0] [clone .lto_priv.0] (size=<optimized out>)
    at /usr/src/debug/monero/monero/external/randomx/src/vm_interpreted_light.hpp:44
#3  0x000055555564a60e in randomx::LargePageAllocator::allocMemory (count=2097152)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:108
#4  randomx::VmBase<randomx::LargePageAllocator, false>::allocate (this=0x7fd50000f7c0)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:114
#5  0x0000555555a99c2b in randomx_create_vm (flags=<optimized out>, cache=0x7fd558000cb0, dataset=0x0)
    at /usr/src/debug/monero/monero/external/randomx/src/randomx.cpp:325
#6  0x000055555592e1c7 in rx_init_light_vm (cache=0x7fd558000cb0, vm=0x7fd52d1f7670, flags=122)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:277
#7  rx_init_light_vm (flags=<optimized out>, vm=0x7fd52d1f7670, cache=0x7fd558000cb0)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:264
#8  0x000055555592f09e in rx_slow_hash (seedhash=<optimized out>, data=0x7fd5100bbab0, length=76, 
    result_hash=0x7fd52d1f4c00 "") at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:429
#9  0x0000555555b5d020 in cryptonote::get_block_longhash(cryptonote::Blockchain const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, crypto::hash&, unsigned long, int, crypto::hash const*, int) [clone .constprop.0] (pbc=pbc@entry=0x555555fafbf0, 
    bd="\020\020\350ϸ\241\006_\363\350\271\033\326\001\020\305\367\256f\261\320\346\333ke\241\316HM1\025\024\341[,\r\327:h\337\317*\020%\211w\244<:\336\364ia\364\224\n\331ޙ\037\241\350\306\006a\254\205\343\2607\v\002\3776\340$", res=..., height=height@entry=2858024, major_version=<optimized out>, 
    seed_hash=seed_hash@entry=0x0, miners=<optimized out>)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:698
#10 0x000055555590256a in cryptonote::get_block_longhash (miners=<optimized out>, seed_hash=0x0, 
    height=2858024, res=..., b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:709
#11 cryptonote::get_block_longhash (seed_hash=0x0, miners=0, height=2858024, b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:715
#12 cryptonote::Blockchain::block_longhash_worker (this=0x555555fafbf0, height=2858025, blocks=..., 
    map=std::unordered_map with 0 elements)
    at /usr/src/debug/monero/monero/src/cryptonote_core/blockchain.cpp:4868
#13 0x0000555555956792 in std::function<void ()>::operator()() const (this=<optimized out>, 
    this=<optimized out>) at /usr/include/c++/12.2.1/bits/std_function.h:591
#14 tools::threadpool::run (this=0x555555e75ba0 <tools::threadpool::getInstanceForCompute()::instance>, 
    flush=true) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:169
#15 0x0000555555956c39 in tools::threadpool::waiter::wait (this=0x7fd52d1f5130)
    at /usr/src/debug/monero/monero/src/common/threadpool.cpp:132
#16 0x0000555555909ce7 in cryptonote::Blockchain::prepare_handle_incoming_blocks (this=0x555555fafbf0, 
    blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...})
    at /usr/src/debug/monero/monero/src/cryptonote_core/blockchain.cpp:5241
#17 0x0000555555b17a40 in cryptonote::core::prepare_handle_incoming_blocks(std::vector<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> > const&, std::vector<cryptonote::block, std::allocator<cryptonote::block> >&) [clone .constprop.0] (this=0x555555fafa50, 
    blocks_entry=std::vector of length 1, capacity 1 = {...}, 
    blocks=std::vector of length 1, capacity 1 = {...})
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_core.cpp:1623
#18 0x000055555588adbc in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block (this=0x555555faf790, command=<optimized out>, arg=..., context=...)
    at /usr/src/debug/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.inl:780
#19 0x0000555555ad9352 in std::__invoke_impl<int, int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*&)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*&, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&> (__t=@0x7fd52d1f5e10: 0x555555faf790, 
    __f=@0x7fd52d1f5e00: (int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*)(cryptonote::t_cryptonote_protocol_handler<cryptonote::core> * const, int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> &, cryptonote::cryptonote_connection_context &)) 0x555555888cb0 <cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>)
    at /usr/include/c++/12.2.1/bits/invoke.h:74
#20 std::__invoke<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*&)(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&), cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*&, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&> (
    __fn=@0x7fd52d1f5e00: (int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*)(cryptonote::t_cryptonote_protocol_handler<cryptonote::core> * const, int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> &, cryptonote::cryptonote_connection_context &)) 0x555555888cb0 <cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_notify_new_fluffy_block(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>)
    at /usr/include/c++/12.2.1/bits/invoke.h:96
#21 std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>::__call<int, int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&, 0ul, 1ul, 2ul, 3ul>(std::tuple<int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&>&&, std::_Index_tuple<0ul, 1ul, 2ul, 3ul>) (__args=..., this=0x7fd52d1f5e00)
    at /usr/include/c++/12.2.1/functional:495
#22 std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>::operator()<int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&, int>(int&, boost::value_initialized<epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t> >&, cryptonote::cryptonote_connection_context&) (this=0x7fd52d1f5e00) at /usr/include/c++/12.2.1/functional:580
#23 epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>, cryptonote::cryptonote_connection_context, std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)> >(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, int, epee::span<unsigned char const>, std::_Bind<int (cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::*(cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*, std::_Placeholder<1>, std::_Placeholder<2>, std::_Placeholder<3>))(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request_t>&, cryptonote::cryptonote_connection_context&)>, cryptonote::cryptonote_connection_context&) (in_buff=..., cb=..., context=..., 
    powner=0x555555faf790, command=2008)
    at /usr/src/debug/monero/monero/contrib/epee/include/storages/levin_abstract_invoke2.h:202
#24 0x0000555555ada72c in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context> (this=0x555555faf790, is_notify=is_notify@entry=true, 
    command=command@entry=2008, in_buff=..., context=..., handled=@0x7fd52d1f63df: true, buff_out=...)
    at /usr/src/debug/monero/monero/src/cryptonote_protocol/cryptonote_protocol_handler.h:95
#25 0x0000555555adbd7c in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, epee::byte_stream&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .constprop.0] (this=0x555555fb0cd0, is_notify=is_notify@entry=true, 
    command=2008, in_buff=..., buff_out=..., context=..., handled=@0x7fd52d1f63df: true)
    at /usr/src/debug/monero/monero/src/p2p/net_node.h:323
#26 0x000055555576eee9 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify (this=<optimized out>, command=<optimized out>, in_buff=..., context=...)
    at /usr/src/debug/monero/monero/src/p2p/net_node.h:313
#27 0x00005555558b4348 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv (this=0x7fd514106e88, ptr=<optimized out>, cb=<optimized out>)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/levin_protocol_handler_async.h:557
#28 0x00005555558c19a2 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}::operator()() const (__closure=0x7fd52d1f6720)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:406
#29 boost::asio::asio_handler_invoke<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, ...) (
    function=...) at /usr/include/boost/asio/handler_invoke_hook.hpp:88
#30 boost_asio_handler_invoke_helpers::invoke<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&) (context=..., function=...)
    at /usr/include/boost/asio/detail/handler_invoke_helpers.hpp:54
#31 boost::asio::detail::handler_work<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul>, void>::complete<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}>(epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}&) (handler=..., function=..., this=<synthetic pointer>)
    at /usr/include/boost/asio/detail/handler_work.hpp:520
#32 boost::asio::detail::completion_handler<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::start_read()::{lambda(boost::system::error_code const&, unsigned long)#3}::operator()(boost::system::error_code const&, unsigned long) const::{lambda()#1}, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0ul> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) (
    owner=0x555556023f80, base=0x7fd5000c4990) at /usr/include/boost/asio/detail/completion_handler.hpp:74
#33 0x00005555556de985 in boost::asio::detail::scheduler_operation::complete (
    bytes_transferred=<optimized out>, ec=..., owner=<optimized out>, this=<optimized out>, 
    this=<optimized out>, owner=<optimized out>, ec=..., bytes_transferred=<optimized out>)
    at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#34 boost::asio::detail::strand_service::do_complete (owner=0x555556023f80, base=0x7fd5140d9c10, ec=...)
    at /usr/include/boost/asio/detail/impl/strand_service.ipp:193
#35 0x0000555555b45237 in boost::asio::detail::scheduler_operation::complete (
    bytes_transferred=<optimized out>, ec=..., owner=<optimized out>, this=<optimized out>, 
    this=<optimized out>, owner=<optimized out>, ec=..., bytes_transferred=<optimized out>)
    at /usr/include/boost/asio/detail/scheduler_operation.hpp:40
#36 boost::asio::detail::scheduler::do_run_one (ec=..., this_thread=..., lock=..., this=0x555556023f80)
    at /usr/include/boost/asio/detail/impl/scheduler.ipp:492
#37 boost::asio::detail::scheduler::run(boost::system::error_code&) [clone .constprop.0] (
    this=0x555556023f80, ec=...) at /usr/include/boost/asio/detail/impl/scheduler.ipp:210
#38 0x00005555558a192f in boost::asio::io_context::run (this=<optimized out>)
    at /usr/include/boost/asio/impl/io_context.ipp:63
#39 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread (this=0x555555fe2d60)
    at /usr/src/debug/monero/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1320
#40 0x00007ffff7bfdcbb in boost::(anonymous namespace)::thread_proxy (param=<optimized out>)
    at libs/thread/src/pthread/thread.cpp:179
#41 0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#42 0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
[Switching to Thread 0x7fd55d5fd6c0 (LWP 7791)]

Thread 4 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd5400031d0, tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
81	in /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd5400031d0, 
    tinfo=0x7ffff7428db8 <typeinfo for std::bad_alloc>, dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd5400031d0, info=0x7ffff7428db8 <typeinfo for std::bad_alloc>, 
    dest=0x7ffff72a52b0 <std::bad_alloc::~bad_alloc()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x000055555564a49d in randomx::InterpretedLightVm<randomx::AlignedAllocator<64ul>, true>::operator new(unsigned long) [clone .part.0] [clone .lto_priv.0] (size=<optimized out>)
    at /usr/src/debug/monero/monero/external/randomx/src/vm_interpreted_light.hpp:44
#3  0x000055555564a60e in randomx::LargePageAllocator::allocMemory (count=2097152)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:108
#4  randomx::VmBase<randomx::LargePageAllocator, false>::allocate (this=0x7fd540203940)
    at /usr/src/debug/monero/monero/external/randomx/src/virtual_machine.cpp:114
#5  0x0000555555a99c2b in randomx_create_vm (flags=<optimized out>, cache=0x7fd558000cb0, dataset=0x0)
    at /usr/src/debug/monero/monero/external/randomx/src/randomx.cpp:325
#6  0x000055555592e1c7 in rx_init_light_vm (cache=0x7fd558000cb0, vm=0x7fd55d5fd670, flags=122)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:277
#7  rx_init_light_vm (flags=<optimized out>, vm=0x7fd55d5fd670, cache=0x7fd558000cb0)
    at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:264
#8  0x000055555592f09e in rx_slow_hash (seedhash=<optimized out>, data=0x7fd5400023d0, length=76, 
    result_hash=0x7fd55d5fc9c0 "") at /usr/src/debug/monero/monero/src/crypto/rx-slow-hash.c:429
#9  0x0000555555b5d020 in cryptonote::get_block_longhash(cryptonote::Blockchain const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, crypto::hash&, unsigned long, int, crypto::hash const*, int) [clone .constprop.0] (pbc=pbc@entry=0x555555fafbf0, 
    bd="\020\020\366ϸ\241\006N\356C\302\"\ts緓\nt\031\366\267\375\024\236SFW\304B9h\361%\312\325\0363x\322\3653P%\264\003\016j\250\305KG\312\353\363\rC\357\032K\3520P\307\320\030P\355\221b\230l~T\306\001", res=..., 
    height=height@entry=2858025, major_version=<optimized out>, seed_hash=seed_hash@entry=0x0, 
    miners=<optimized out>) at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:698
#10 0x000055555590256a in cryptonote::get_block_longhash (miners=<optimized out>, seed_hash=0x0, 
    height=2858025, res=..., b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:709
#11 cryptonote::get_block_longhash (seed_hash=0x0, miners=0, height=2858025, b=..., pbc=0x555555fafbf0)
    at /usr/src/debug/monero/monero/src/cryptonote_core/cryptonote_tx_utils.cpp:715
#12 cryptonote::Blockchain::block_longhash_worker (this=0x555555fafbf0, height=2858026, blocks=..., 
    map=std::unordered_map with 0 elements)
    at /usr/src/debug/monero/monero/src/cryptonote_core/blockchain.cpp:4868
#13 0x0000555555956792 in std::function<void ()>::operator()() const (this=<optimized out>, 
    this=<optimized out>) at /usr/include/c++/12.2.1/bits/std_function.h:591
#14 tools::threadpool::run (this=0x555555e75ba0 <tools::threadpool::getInstanceForCompute()::instance>, 
    flush=false) at /usr/src/debug/monero/monero/src/common/threadpool.cpp:169
#15 0x00007ffff7bfdcbb in boost::(anonymous namespace)::thread_proxy (param=<optimized out>)
    at libs/thread/src/pthread/thread.cpp:179
#16 0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#17 0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
save
Blockchain saved
exit
[Thread 0x7fd52e5fb6c0 (LWP 7826) exited]
[Thread 0x7fd52d1f76c0 (LWP 7830) exited]
[Thread 0x7fd52e0fa6c0 (LWP 7827) exited]
[Thread 0x7fd52eafc6c0 (LWP 7825) exited]
[Thread 0x7fd5447f76c0 (LWP 7823) exited]
Stop signal sent
[Thread 0x7fd52effd6c0 (LWP 7824) exited]
[Thread 0x7fd52dbf96c0 (LWP 7828) exited]
[Thread 0x7fd52c7f56c0 (LWP 7832) exited]
[Thread 0x7fd52ccf66c0 (LWP 7831) exited]
[Thread 0x7fd52d6f86c0 (LWP 7829) exited]
2023-04-06 02:01:56.577	I p2p net loop stopped
[Thread 0x7fd544ff86c0 (LWP 7820) exited]
[Thread 0x7fd5457f96c0 (LWP 7819) exited]
[Switching to Thread 0x7fd52ffff6c0 (LWP 7821)]

Thread 14 "monerod" hit Catchpoint 1 (exception thrown), 0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (
    obj=0x7fd51c000c20, tinfo=0x7ffff742b470 <typeinfo for std::system_error>, 
    dest=0x7ffff72d6fa0 <std::system_error::~system_error()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
81	in /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc
(gdb) bt
#0  0x00007ffff72a6fa1 in __cxxabiv1::__cxa_throw (obj=0x7fd51c000c20, 
    tinfo=0x7ffff742b470 <typeinfo for std::system_error>, 
    dest=0x7ffff72d6fa0 <std::system_error::~system_error()>)
    at /usr/src/debug/gcc/gcc/libstdc++-v3/libsupc++/eh_throw.cc:81
#1  0x0000555555613de7 in __cxa_throw (ex=0x7fd51c000c20, 
    info=0x7ffff742b470 <typeinfo for std::system_error>, 
    dest=0x7ffff72d6fa0 <std::system_error::~system_error()>)
    at /usr/src/debug/monero/monero/src/common/stack_trace.cpp:104
#2  0x0000555555614013 in detail::expect::throw_ (ec=..., msg=<optimized out>, file=<optimized out>, 
    line=<optimized out>) at /usr/include/c++/12.2.1/bits/allocator.h:174
#3  0x00005555559932d4 in detail::expect::unwrap<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > (error_msg=0x0, 
    file=0x555555c36e20 "/usr/src/debug/monero/monero/src/rpc/zmq_server.cpp", line=161, result=...)
    at /usr/src/debug/monero/monero/src/common/expect.h:89
#4  cryptonote::rpc::ZmqServer::serve (this=<optimized out>)
    at /usr/src/debug/monero/monero/src/rpc/zmq_server.cpp:161
#5  0x00007ffff7bfdcbb in boost::(anonymous namespace)::thread_proxy (param=<optimized out>)
    at libs/thread/src/pthread/thread.cpp:179
#6  0x00007ffff709ebb5 in start_thread (arg=<optimized out>) at pthread_create.c:444
#7  0x00007ffff7120d90 in clone3 () at ../sysdeps/unix/sysv/linux/x86_64/clone3.S:81
(gdb) c
Continuing.
[Thread 0x7fd52f7fe6c0 (LWP 7822) exited]
[Thread 0x7fd52ffff6c0 (LWP 7821) exited]
[Thread 0x7fd5477fd6c0 (LWP 7815) exited]
[Thread 0x7fd547ffe6c0 (LWP 7814) exited]
2023-04-06 02:02:07.956	I Stopping core RPC server...
2023-04-06 02:02:07.957	I Node stopped.
[Thread 0x7fd545ffa6c0 (LWP 7818) exited]
[Thread 0x7fd5467fb6c0 (LWP 7817) exited]
2023-04-06 02:02:08.054	I Deinitializing core RPC server...
[Thread 0x7fd546ffc6c0 (LWP 7816) exited]
2023-04-06 02:02:08.056	I Deinitializing p2p...
2023-04-06 02:02:08.080	I Deinitializing core...
[Thread 0x7fd55e5ff6c0 (LWP 7789) exited]
2023-04-06 02:02:08.132	I Stopping cryptonote protocol...
2023-04-06 02:02:08.132	I Cryptonote protocol stopped successfully
[Thread 0x7fd4f30fc6c0 (LWP 7836) exited]
[Thread 0x7fd4f21f96c0 (LWP 7839) exited]
[Thread 0x7fd4f26fa6c0 (LWP 7838) exited]
[Thread 0x7fd4f2bfb6c0 (LWP 7837) exited]
[Thread 0x7fd4f35fd6c0 (LWP 7835) exited]
[Thread 0x7fd4f3afe6c0 (LWP 7834) exited]
[Thread 0x7fd4f3fff6c0 (LWP 7833) exited]
[Thread 0x7fd55cbfb6c0 (LWP 7813) exited]
[Thread 0x7fd55d0fc6c0 (LWP 7812) exited]
[Thread 0x7fd55d5fd6c0 (LWP 7791) exited]
[Inferior 1 (process 7769) exited normally]
(gdb) exit
```

Is this what you were expecting? Does it mean these bad_allocs are not a big deal? And why? 

## SChernykh | 2023-04-06T05:28:42+00:00
It's LargePageAllocator failing, so maybe you just don't have huge pages enabled in your system.

## moneromooo-monero | 2023-04-06T09:43:43+00:00
Yes, it is what I was expecting. As SChernykh said, it's trying to use huge pages, failing, and falling back to normal allocation. It's unfortunate it uses exceptions for this, bit it's harmless, you're just not getting some speed boost to your hash rate. Which, if you're not mining, you don't really care about anyway.


## salimathel | 2023-04-06T19:52:25+00:00
@SChernykh 
@moneromooo-monero 
Thanks for the info. Yes, you guys are right indeed. After enabling huge pages, there are no more bad allocs. Solved. Thanks.

## selsta | 2023-06-06T01:02:44+00:00
No reply from issue creator.

## drzraf | 2024-01-26T00:42:30+00:00
Still an actual issue which clutters the logs (a least on 0.18.2.2)

## ndorf | 2025-09-29T06:14:35+00:00
IMHO, it is not really reasonable to just ignore these. The RandomX hugepages request alone dumps the stack every 5 minutes. That's enough to make the log file unreadable. The icing on the cake is that when build type is `Release` (the default), there are no debug symbols, so these stack traces are not even intelligible.

I propose that libunwind simply be disabled when build type is `Release`. The official binary releases already ship without it, so this would be consistent with those. 


# Action History
- Created by: andrew-jman | 2023-03-20T12:43:46+00:00
- Closed at: 2023-06-06T01:02:44+00:00
