---
title: xmrig does`t stop without devices opencl_R9280
source_url: https://github.com/xmrig/xmrig/issues/1554
author: qpuJlocoqp
assignees: []
labels:
- bug
- opencl
created_at: '2020-02-16T10:00:11+00:00'
updated_at: '2020-02-24T22:41:56+00:00'
type: issue
status: closed
closed_at: '2020-02-24T22:41:56+00:00'
---

# Original Description
 * ABOUT        XMRig/5.6.0 MSVC/2019
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   unavailable
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Pentium(R) CPU G3420 @ 3.20GHz (1) x64 -AES
                L2:0.5 MB L3:3.0 MB 2C/2T NUMA:1
 * MEMORY       3.8/7.9 GB (47%)
 * DONATE       5%
 * ASSEMBLY     auto:none
 * POOL #1      pool.supportxmr.com:443 algo auto
 * COMMANDS     hashrate, pause, resume
[2020-02-16 12:44:40.175] configuration saved to: "C:\Maining\xmrig-5.6.0\config
.json"
 * ADL          press e for health report
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (2906.
10)
 * OPENCL GPU   #0 01:00.0 AMD Radeon R9 200 Series (Tahiti) 1000 MHz cu:32 mem:
2816/3072 MB
 * CUDA         disabled
[2020-02-16 12:44:42.641]  net  use pool pool.supportxmr.com:443 TLSv1.2 95.216.
46.125
[2020-02-16 12:44:42.643]  net  fingerprint (SHA-256): "efe8e986720f4631571b0393
6da48deff25aad8d58168c3403c48150978db2e6"
[2020-02-16 12:44:42.644]  net  new job from pool.supportxmr.com:443 diff 50000
algo rx/0 height 2034772
[2020-02-16 12:44:42.645]  rx   init dataset algo rx/0 (2 threads) seed 2ad7b6b5
509b48e8...
[2020-02-16 12:44:42.646]  rx   allocated 2336 MB (2080+256) huge pages 0% 0/116
8 +JIT (0 ms)
[2020-02-16 12:44:47.908]  net  new job from pool.supportxmr.com:443 diff 85714
algo rx/0 height 2034772
[2020-02-16 12:44:56.619]  rx   dataset ready (13971 ms)
[2020-02-16 12:44:56.619]  cpu  use profile  rx  (2 threads) scratchpad 2048 KB
[2020-02-16 12:44:56.643]  cpu  READY threads 2/2 (2) huge pages 0% 0/2 memory 4
096 KB (22 ms)
[2020-02-16 12:44:56.662]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 01:00.0 |  192 |  8 |  0 |  - |  8 |  384 | AMD Radeon R9 200 Serie
s (Tahiti)
|  1 |   0 | 01:00.0 |  192 |  8 |  0 |  - |  8 |  384 | AMD Radeon R9 200 Serie
s (Tahiti)
[2020-02-16 12:44:56.734]  ocl  GPU #0 compiling...
[2020-02-16 12:44:56.890]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBu
ildProgram
BUILD LOG:
"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 1141: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);

                                                ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 1218: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);

                                                ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 1250: warning: OpenCL
          extension is now part of core
  #pragma OPENCL EXTENSION cl_khr_fp64 : enable
                           ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 2357: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_a)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 2358: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_b)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 2359: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_c)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 2580: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T1.cl", line 2659: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

3 errors detected in the compilation of "C:\Users\Ksu\AppData\Local\Temp\OCL7312
T1.cl".
Frontend phase failed compilation.

[2020-02-16 12:44:56.903]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2020-02-16 12:44:56.906]  ocl  GPU #0 compiling...
[2020-02-16 12:44:56.940]  ocl  thread #0 self-test failed
[2020-02-16 12:44:57.207]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBu
ildProgram
BUILD LOG:
"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 1141: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);

                                                ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 1218: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);

                                                ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 1250: warning: OpenCL
          extension is now part of core
  #pragma OPENCL EXTENSION cl_khr_fp64 : enable
                           ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 2357: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_a)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 2358: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_b)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 2359: error: expression
          must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_c)->y|=1U<<20;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 2580: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

"C:\Users\Ksu\AppData\Local\Temp\OCL7312T2.cl", line 2659: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

3 errors detected in the compilation of "C:\Users\Ksu\AppData\Local\Temp\OCL7312
T2.cl".
Frontend phase failed compilation.

[2020-02-16 12:44:57.220]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2020-02-16 12:44:57.243]  ocl  thread #1 self-test failed
[2020-02-16 12:44:57.244]  ocl  disabled (failed to start threads)


# Discussion History
## dedizones | 2020-02-16T12:07:30+00:00
Hi, i have same error with 280X

DRIVER: AMD 20.2.1

## SChernykh | 2020-02-16T12:16:05+00:00
@dedizones this error?
```
error: expression must have pointer-to-struct-or-union type
((uint2*)&mantissa_a)->y|=1U<<20;
```

## dedizones | 2020-02-16T12:21:19+00:00
> @dedizones this error?
> 
> ```
> error: expression must have pointer-to-struct-or-union type
> ((uint2*)&mantissa_a)->y|=1U<<20;
> ```
**My Log error** 

` * ABOUT        XMRig/5.6.0 MSVC/2019
 * LIBS         libuv/1.34.0 OpenSSL/1.1.1d hwloc/2.1.0
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          Intel(R) Core(TM) i7-3820 CPU @ 3.60GHz (1) x64 AES
                L2:1.0 MB L3:10.0 MB 4C/8T NUMA:1
 * MEMORY       2.7/23.9 GB (11%)
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      xmr-eu1.nanopool.org:14444 coin monero
 * COMMANDS     hashrate, pause, resume
 * ADL          press e for health report
 * OPENCL       #0 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3004.8)
 * OPENCL GPU   #0 02:00.0 AMD Radeon R9 200 Series (Tahiti) 1070 MHz cu:32 mem:2816/3072 MB
 * CUDA         disabled
[2020-02-16 13:20:27.257]  net  use pool xmr-eu1.nanopool.org:14444  217.182.169.148
[2020-02-16 13:20:27.257]  net  new job from xmr-eu1.nanopool.org:14444 diff 480045 algo rx/0 height 2034841
[2020-02-16 13:20:27.294]  msr  register values for "intel" preset has been set successfully (36 ms)
[2020-02-16 13:20:27.294]  rx   init dataset algo rx/0 (8 threads) seed 2ad7b6b5509b48e8...
[2020-02-16 13:20:27.304]  rx   allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (10 ms)
[2020-02-16 13:20:32.484]  rx   dataset ready (5179 ms)
[2020-02-16 13:20:32.485]  cpu  use profile  rx  (4 threads) scratchpad 2048 KB
[2020-02-16 13:20:32.550]  cpu  READY threads 4/4 (4) huge pages 100% 4/4 memory 8192 KB (65 ms)
[2020-02-16 13:20:32.569]  ocl  use profile  rx  (2 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID |    I |  W | SI | MC |  U |  MEM | NAME
|  0 |   0 | 02:00.0 |  192 |  8 |  0 |  - |  8 |  384 | AMD Radeon R9 200 Series (Tahiti)
|  1 |   0 | 02:00.0 |  192 |  8 |  0 |  - |  8 |  384 | AMD Radeon R9 200 Series (Tahiti)
[2020-02-16 13:20:32.634]  ocl  GPU #0 compiling...
[2020-02-16 13:20:32.831]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 1141: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);
                                                ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 1218: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);
                                                ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 1250: warning:
          OpenCL extension is now part of core
  #pragma OPENCL EXTENSION cl_khr_fp64 : enable
                           ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 2357: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_a)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 2358: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_b)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 2359: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_c)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 2580: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl", line 2659: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

3 errors detected in the compilation of "C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T1.cl".
Frontend phase failed compilation.

[2020-02-16 13:20:32.832]  ocl  thread #0 failed with error CL_INVALID_PROGRAM
[2020-02-16 13:20:32.834]  ocl  GPU #0 compiling...
[2020-02-16 13:20:32.837]  ocl  thread #0 self-test failed
[2020-02-16 13:20:33.027]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 1141: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);
                                                ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 1218: warning: shift
          count is too large
  m[(in_len-128)/sizeof(ulong)] &= (ulong)(-1)>>(64-(in_len % sizeof(ulong))*8);
                                                ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 1250: warning:
          OpenCL extension is now part of core
  #pragma OPENCL EXTENSION cl_khr_fp64 : enable
                           ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 2357: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_a)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 2358: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_b)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 2359: error:
          expression must have pointer-to-struct-or-union type
  ((uint2*)&mantissa_c)->y|=1U<<20;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 2580: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

"C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl", line 2659: warning: goto
          statement may cause irreducible control flow
  goto execution_end;
  ^

3 errors detected in the compilation of "C:\Users\WARSGA~1\AppData\Local\Temp\OCL5944T2.cl".
Frontend phase failed compilation.

[2020-02-16 13:20:33.029]  ocl  thread #1 failed with error CL_INVALID_PROGRAM
[2020-02-16 13:20:33.035]  ocl  thread #1 self-test failed
[2020-02-16 13:20:33.035]  ocl  disabled (failed to start threads)
`

## SChernykh | 2020-02-16T12:24:45+00:00
WTF, I hate AMD now. Same code that compiles successfully on Polaris/Vega/Navi, doesn't want to compile on earlier GPUs on **the same driver**. I'll try to come up with a workaround for this.

## ossimo | 2020-02-17T17:27:06+00:00
 Software ver. 19.12.3  error


## SChernykh | 2020-02-18T09:29:38+00:00
An update: I tried to rewrite the code in question in several different ways, but couldn't make it work on all my GPUs with the latest driver. Current code works on Polaris/Vega/Navi, but doesn't compile on older GPUs, so I'll keep looking for a solution.

## Spudz76 | 2020-02-24T22:39:44+00:00
Does it work on VI chips (like Hawaii)?
SI chips might have similar problems as the terascale where no driver newer than antique 15.x works

# Action History
- Created by: qpuJlocoqp | 2020-02-16T10:00:11+00:00
- Closed at: 2020-02-24T22:41:56+00:00
