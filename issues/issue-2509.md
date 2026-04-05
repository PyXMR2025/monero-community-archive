---
title: Threads were only used half.
source_url: https://github.com/xmrig/xmrig/issues/2509
author: danuonuo
assignees: []
labels: []
created_at: '2021-08-04T05:50:06+00:00'
updated_at: '2021-08-06T06:26:55+00:00'
type: issue
status: closed
closed_at: '2021-08-06T06:26:55+00:00'
---

# Original Description
Hey,when I was mining,I found that only half of the threads were used.Is that a bug?
![image](https://user-images.githubusercontent.com/40296672/128128731-27c97cc1-1479-4142-9e50-77ad68f6a9fa.png)
![image](https://user-images.githubusercontent.com/40296672/128128790-cb236ce1-e0b5-4b2c-8017-f4b9772f1d56.png)


# Discussion History
## SChernykh | 2021-08-04T07:31:56+00:00
What CPU? Number of threads is limited by how much L2 and L3 cache you have (256 KB L2 per thread and 2 MB L3 per thread is required).

## danuonuo | 2021-08-04T07:41:25+00:00
L2 cache:            256K
L3 cache:            25600K
So it can only afford 18 threads?
(I think you have a typing errer about L2,because in your case,it can only run 1 threads.)

> What CPU? Number of threads is limited by how much L2 and L3 cache you have (256 KB L2 per thread and 2 MB L3 per thread is required).



## Lonnegan | 2021-08-04T17:44:17+00:00
No typing error. The size of the L2 cache is per core, the size of the L3 cache is per CPU.

Besides it depends of what algo you are mining. Moneros rx algo uses 2 MB scratchpad size per thread. Havens cn/xhv algo uses 4 MB per thread, rx/arq only 256 KB per thread, cn/upx2 only 128 KB per thread. So if you want want to use all your compute ressources without flooding the last level cache, you have to choose an algo (coin) which fits better to your CPU.

Edit: but which Intel cpu has 25 MB L3 cache and 256 KB L2 cache? Sure that your cpu doesn't have 1 MB L2 cache per core?

## danuonuo | 2021-08-05T00:36:36+00:00
> No typing error. The size of the L2 cache is per core, the size of the L3 cache is per CPU.
> 
> Besides it depends of what algo you are mining. Moneros rx algo uses 2 MB scratchpad size per thread. Havens cn/xhv algo uses 4 MB per thread, rx/arq only 256 KB per thread, cn/upx2 only 128 KB per thread. So if you want want to use all your compute ressources without flooding the last level cache, you have to choose an algo (coin) which fits better to your CPU.
> 
> Edit: but which Intel cpu has 25 MB L3 cache and 256 KB L2 cache? Sure that your cpu doesn't have 1 MB L2 cache per core?

That is an aws server,L2 is 1024K,however,it still uses half.
 * ABOUT        XMRig/6.13.1 gcc/8.3.0
 * LIBS         libuv/1.41.0 OpenSSL/1.1.1k hwloc/2.4.1
 * HUGE PAGES   supported
 * 1GB PAGES    supported
 * CPU          Intel(R) Xeon(R) Platinum 8252C CPU @ 3.80GHz (1) 64-bit AES VM
                L2:12.0 MB L3:24.8 MB 12C/24T NUMA:1
 * MEMORY       5.8/92.3 GB (6%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr.f2pool.com:13531 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * HTTP API     0.0.0.0:9500 
 * OPENCL       disabled
 * CUDA         disabled
[2021-08-05 00:33:41.557]  net      use pool xmr.f2pool.com:13531  47.100.95.105
[2021-08-05 00:33:41.557]  net      new job from xmr.f2pool.com:13531 diff 65537 algo rx/0 height 2420039
[2021-08-05 00:33:41.557]  cpu      use argon2 implementation AVX-512F
[2021-08-05 00:33:41.558]  msr      register values for "intel" preset have been set successfully (2 ms)
[2021-08-05 00:33:41.558]  randomx  init dataset algo rx/0 (24 threads) seed db14407ad84a4016...
[2021-08-05 00:33:42.153]  randomx  allocated 3072 MB (2080+256) huge pages 100% 3/3 +JIT (595 ms)
[2021-08-05 00:33:43.456]  randomx  dataset ready (1302 ms)
[2021-08-05 00:33:43.456]  cpu      use profile  rx  (12 threads) scratchpad 2048 KB
[2021-08-05 00:33:43.466]  cpu      READY threads 12/12 (12) huge pages 100% 12/12 memory 24576 KB (10 ms)


## SChernykh | 2021-08-05T19:59:24+00:00
> however,it still uses half.

It shows 24.8 MB L3 cache which is enough for only 12 threads. Everything is correct there.

## danuonuo | 2021-08-06T06:26:51+00:00
> > however,it still uses half.
> 
> It shows 24.8 MB L3 cache which is enough for only 12 threads. Everything is correct there.

OK.
Thank you.

# Action History
- Created by: danuonuo | 2021-08-04T05:50:06+00:00
- Closed at: 2021-08-06T06:26:55+00:00
