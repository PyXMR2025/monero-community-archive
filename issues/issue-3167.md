---
title: Doesn't work with AMD RX 580 8GB Sapphire Card ( opencl issues )
source_url: https://github.com/xmrig/xmrig/issues/3167
author: djlaserman
assignees: []
labels: []
created_at: '2022-11-21T06:03:20+00:00'
updated_at: '2022-11-22T19:59:03+00:00'
type: issue
status: closed
closed_at: '2022-11-22T07:56:58+00:00'
---

# Original Description
**Describe the bug**
Has opencl errors with AMD RX580 8GB Sapphire card. It churns out errors from the onset and seems to just not work with AMD gpus in general. 

**To Reproduce**
Just run it on the exact graphics card (if possible) AMD RX 580 8GB Sapphire 

**Expected behavior**
It breaks immediately with errors that either end up automatically abandoning gpu mining and proceeding with cpu mining if enabled or go on in an endless loop of the same errors that can be seen on the output in the console.

**Required data**
 * ABOUT        XMRig/6.18.1-mo1 gcc/11.2.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          11th Gen Intel(R) Core(TM) i7-11700 @ 2.50GHz (1) 64-bit AES VM
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       13.0/31.7 GB (41%)
                Controller0-ChannelA-DIMM0: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelA-DIMM1: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelB-DIMM0: <empty>
                Controller0-ChannelB-DIMM1: <empty>
 * MOTHERBOARD  ASUS - System Product Name
 * DONATE       0%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
 * ADL          press e for health report
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3444.0)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * OPENCL GPU   #1 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * CUDA         disabled
[2022-11-21 07:52:14.807]  net      use pool gulf.moneroocean.stream:10128  199.247.0.216
[2022-11-21 07:52:14.808]  net      new job from gulf.moneroocean.stream:10128 diff 1247K algo rx/arq height 1084514 (1 tx)
[2022-11-21 07:52:14.809]  cpu      use argon2 implementation AVX-512F
[2022-11-21 07:52:14.809]  msr      service WinRing0_1_2_0 already exists, but with a different service name
[2022-11-21 07:52:15.062]  msr      register values for "intel" preset have been set successfully (253 ms)
[2022-11-21 07:52:15.062]  randomx  init dataset algo rx/arq (16 threads) seed b9d7c9529ff4dc2c...
[2022-11-21 07:52:15.332]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (270 ms)
[2022-11-21 07:52:18.289]  randomx  dataset ready (2956 ms)
[2022-11-21 07:52:18.289]  cpu      use profile  rx  (8 threads) scratchpad 256 KB
[2022-11-21 07:52:18.291]  opencl   use profile  rx  (4 threads) scratchpad 256 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |    144 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |    144 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 01:00.0 |       576 |     8 |    144 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 01:00.0 |       576 |     8 |    144 | Radeon RX 580 Series (Ellesmere)
[2022-11-21 07:52:18.321]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 2048 KB (31 ms)
[2022-11-21 07:52:19.085]  opencl   GPU #0 compiling...
[2022-11-21 07:52:19.263]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:865:48: error: use of undeclared identifier 'RANDOMX_SCRATCHPAD_L3'
__global uint4* p=((__global uint4*) out)+idx*(outputSize0/sizeof(uint4))+sub;
                                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:823:22: note: expanded from macro 'outputSize0'
#define outputSize0 (outputSize + 64)
                     ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:822:20: note: expanded from macro 'outputSize'
#define outputSize RANDOMX_SCRATCHPAD_L3
                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:871:18: error: use of undeclared identifier 'RANDOMX_SCRATCHPAD_L3'
for (uint i=0; i<outputSize/sizeof(uint4); i+=4,p+=4)
                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:822:20: note: expanded from macro 'outputSize'
#define outputSize RANDOMX_SCRATCHPAD_L3
                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:955:48: error: use of undeclared identifier 'ENTROPY_SIZE'
__global uint4* p=((__global uint4*) out)+idx*(outputSize0/sizeof(uint4))+sub;
                                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:913:21: note: expanded from macro 'outputSize0'
#define outputSize0 outputSize
                    ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:912:20: note: expanded from macro 'outputSize'
#define outputSize ENTROPY_SIZE
                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:961:18: error: use of undeclared identifier 'ENTROPY_SIZE'
for (uint i=0; i<outputSize/sizeof(uint4); i+=4,p+=4)
                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:912:20: note: expanded from macro 'outputSize'
#define outputSize ENTROPY_SIZE
                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1017:57: error: use of undeclared identifier 'RANDOMX_SCRATCHPAD_L3'
__global const uint4* p=((__global uint4*) input)+idx*((inputSize+64)/sizeof(uint4))+sub;
                                                        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1001:19: note: expanded from macro 'inputSize'
#define inputSize RANDOMX_SCRATCHPAD_L3
                  ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1023:18: error: use of undeclared identifier 'RANDOMX_SCRATCHPAD_L3'
for (uint i=0; i<inputSize/sizeof(uint4); i+=4,p+=4)
                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1001:19: note: expanded from macro 'inputSize'
#define inputSize RANDOMX_SCRATCHPAD_L3
                  ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1408:37: error: use of undeclared identifier 'RANDOMX_PROGRAM_SIZE'
__local uint32_t execution_plan_buf[RANDOMX_PROGRAM_SIZE*WORKERS_PER_HASH*(32/8)*sizeof(exec_t)/sizeof(uint32_t)];
                                    ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1414:89: error: use of undeclared identifier 'RANDOMX_PROGRAM_SIZE'
__local exec_t* execution_plan=(__local exec_t*)(execution_plan_buf+(get_local_id(0)/8)*RANDOMX_PROGRAM_SIZE*WORKERS_PER_HASH*sizeof(exec_t)/sizeof(uint32_t));
                                                                                        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1415:58: error: use of undeclared identifier 'VM_STATE_SIZE'
__global uint64_t* R=((__global uint64_t*)vm_states)+idx*VM_STATE_SIZE/sizeof(uint64_t);
                                                         ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1417:79: error: use of undeclared identifier 'ENTROPY_SIZE'
const __global uint64_t* entropy=((const __global uint64_t*)entropy_data)+idx*ENTROPY_SIZE/sizeof(uint64_t);
                                                                              ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1431:22: error: use of undeclared identifier 'RANDOMX_PROGRAM_SIZE'
for (uint32_t i=0; i<RANDOMX_PROGRAM_SIZE; ++i)
                     ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:11: error: use of undeclared identifier 'RANDOMX_FREQ_IADD_RS'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:32: error: use of undeclared identifier 'RANDOMX_FREQ_IADD_M'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:52: error: use of undeclared identifier 'RANDOMX_FREQ_ISUB_R'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:72: error: use of undeclared identifier 'RANDOMX_FREQ_ISUB_M'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                       ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:92: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_R'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                           ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:112: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_M'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:132: error: use of undeclared identifier 'RANDOMX_FREQ_IMULH_R'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                                                                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:153: error: use of undeclared identifier 'RANDOMX_FREQ_IMULH_M'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                                                                                        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:174: error: use of undeclared identifier 'RANDOMX_FREQ_ISMULH_R'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                                                                                                             ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1439:196: error: use of undeclared identifier 'RANDOMX_FREQ_ISMULH_M'
if(opcode<RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M)
                                                                                                                                                                                                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:9: error: use of undeclared identifier 'RANDOMX_FREQ_IADD_RS'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:30: error: use of undeclared identifier 'RANDOMX_FREQ_IADD_M'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                             ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:50: error: use of undeclared identifier 'RANDOMX_FREQ_ISUB_R'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:70: error: use of undeclared identifier 'RANDOMX_FREQ_ISUB_M'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                     ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:90: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_R'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                         ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:110: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_M'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                                             ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:130: error: use of undeclared identifier 'RANDOMX_FREQ_IMULH_R'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                                                                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:151: error: use of undeclared identifier 'RANDOMX_FREQ_IMULH_M'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                                                                                      ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:172: error: use of undeclared identifier 'RANDOMX_FREQ_ISMULH_R'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                                                                                                           ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1449:194: error: use of undeclared identifier 'RANDOMX_FREQ_ISMULH_M'
opcode-=RANDOMX_FREQ_IADD_RS+RANDOMX_FREQ_IADD_M+RANDOMX_FREQ_ISUB_R+RANDOMX_FREQ_ISUB_M+RANDOMX_FREQ_IMUL_R+RANDOMX_FREQ_IMUL_M+RANDOMX_FREQ_IMULH_R+RANDOMX_FREQ_IMULH_M+RANDOMX_FREQ_ISMULH_R+RANDOMX_FREQ_ISMULH_M;
                                                                                                                                                                                                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1450:11: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_RCP'
if(opcode<RANDOMX_FREQ_IMUL_RCP)
          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1463:9: error: use of undeclared identifier 'RANDOMX_FREQ_IMUL_RCP'
opcode-=RANDOMX_FREQ_IMUL_RCP;
        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1464:11: error: use of undeclared identifier 'RANDOMX_FREQ_INEG_R'
if(opcode<RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R)
          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1464:31: error: use of undeclared identifier 'RANDOMX_FREQ_IXOR_R'
if(opcode<RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R)
                              ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1464:51: error: use of undeclared identifier 'RANDOMX_FREQ_IXOR_M'
if(opcode<RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R)
                                                  ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1464:71: error: use of undeclared identifier 'RANDOMX_FREQ_IROR_R'
if(opcode<RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R)
                                                                      ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1464:91: error: use of undeclared identifier 'RANDOMX_FREQ_IROL_R'
if(opcode<RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R)
                                                                                          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1474:9: error: use of undeclared identifier 'RANDOMX_FREQ_INEG_R'
opcode-=RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R;
        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1474:29: error: use of undeclared identifier 'RANDOMX_FREQ_IXOR_R'
opcode-=RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R;
                            ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1474:49: error: use of undeclared identifier 'RANDOMX_FREQ_IXOR_M'
opcode-=RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R;
                                                ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1474:69: error: use of undeclared identifier 'RANDOMX_FREQ_IROR_R'
opcode-=RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R;
                                                                    ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1474:89: error: use of undeclared identifier 'RANDOMX_FREQ_IROL_R'
opcode-=RANDOMX_FREQ_INEG_R+RANDOMX_FREQ_IXOR_R+RANDOMX_FREQ_IXOR_M+RANDOMX_FREQ_IROR_R+RANDOMX_FREQ_IROL_R;
                                                                                        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1475:11: error: use of undeclared identifier 'RANDOMX_FREQ_ISWAP_R'
if(opcode<RANDOMX_FREQ_ISWAP_R)
          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1491:9: error: use of undeclared identifier 'RANDOMX_FREQ_ISWAP_R'
opcode-=RANDOMX_FREQ_ISWAP_R;
        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:11: error: use of undeclared identifier 'RANDOMX_FREQ_FSWAP_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
          ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:32: error: use of undeclared identifier 'RANDOMX_FREQ_FADD_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:52: error: use of undeclared identifier 'RANDOMX_FREQ_FADD_M'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                   ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:72: error: use of undeclared identifier 'RANDOMX_FREQ_FSUB_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                       ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:92: error: use of undeclared identifier 'RANDOMX_FREQ_FSUB_M'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                                           ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:112: error: use of undeclared identifier 'RANDOMX_FREQ_FSCAL_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                                                               ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:133: error: use of undeclared identifier 'RANDOMX_FREQ_FMUL_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                                                                                    ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:153: error: use of undeclared identifier 'RANDOMX_FREQ_FDIV_M'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                                                                                                        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1492:173: error: use of undeclared identifier 'RANDOMX_FREQ_FSQRT_R'
if(opcode<RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R)
                                                                                                                                                                            ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:9: error: use of undeclared identifier 'RANDOMX_FREQ_FSWAP_R'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
        ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:30: error: use of undeclared identifier 'RANDOMX_FREQ_FADD_R'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
                             ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:50: error: use of undeclared identifier 'RANDOMX_FREQ_FADD_M'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
                                                 ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:70: error: use of undeclared identifier 'RANDOMX_FREQ_FSUB_R'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
                                                                     ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:90: error: use of undeclared identifier 'RANDOMX_FREQ_FSUB_M'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
                                                                                         ^
C:\Users\redacted\AppData\Local\Temp\\OCL25128T1.cl:1497:110: error: use of undeclared identifier 'RANDOMX_FREQ_FSCAL_R'
opcode-=RANDOMX_FREQ_FSWAP_R+RANDOMX_FREQ_FADD_R+RANDOMX_FREQ_FADD_M+RANDOMX_FREQ_FSUB_R+RANDOMX_FREQ_FSUB_M+RANDOMX_FREQ_FSCAL_R+RANDOMX_FREQ_FMUL_R+RANDOMX_FREQ_FDIV_M+RANDOMX_FREQ_FSQRT_R;
                                                                                                             ^

------------------------- I stopped the execution at this point, set opencl to 'false' and proceeded mining with only cpu---------

**Additional context**
Add any other context about the problem here.


# Discussion History
## SChernykh | 2022-11-21T07:31:11+00:00
`XMRig/6.18.1-mo1`
This is not an official XMRig release. Can you reproduce it with the official release?

## djlaserman | 2022-11-21T10:14:49+00:00
> `XMRig/6.18.1-mo1` This is not an official XMRig release. Can you reproduce it with the official release?

Yes, the original error are in the official release and so also in other mods of this release. Below is the output from this latest official release:

 * ABOUT        XMRig/6.18.1 gcc/11.2.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          11th Gen Intel(R) Core(TM) i7-11700 @ 2.50GHz (1) 64-bit AES VM
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       9.6/31.7 GB (30%)
                Controller0-ChannelA-DIMM0: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelA-DIMM1: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelB-DIMM0: <empty>
                Controller0-ChannelB-DIMM1: <empty>
 * MOTHERBOARD  ASUS - System Product Name
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2022-11-21 12:13:18.307]  config   configuration saved to: "C:\Users\djlas\Desktop\xmrig-6.18.1\config.json"
 * ADL          press e for health report
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3444.0)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * OPENCL GPU   #1 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * CUDA         disabled
[2022-11-21 12:13:19.435]  net      use pool gulf.moneroocean.stream:10128  13.228.20.61
[2022-11-21 12:13:19.435]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2760546 (45 tx)
[2022-11-21 12:13:19.436]  cpu      use argon2 implementation AVX-512F
[2022-11-21 12:13:19.436]  msr      to access MSR registers Administrator privileges required.
[2022-11-21 12:13:19.436]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-11-21 12:13:19.436]  randomx  init dataset algo rx/0 (16 threads) seed 5282d00ee18f482e...
[2022-11-21 12:13:19.436]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2022-11-21 12:13:23.465]  randomx  dataset ready (4028 ms)
[2022-11-21 12:13:23.465]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-11-21 12:13:23.467]  opencl   use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
[2022-11-21 12:13:23.517]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (50 ms)
[2022-11-21 12:13:24.831]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:24.832]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:24.892]  opencl   thread #0 self-test failed
[2022-11-21 12:13:24.970]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:24.971]  opencl   thread #2 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.021]  opencl   thread #2 self-test failed
[2022-11-21 12:13:25.040]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:25.041]  opencl   thread #3 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.059]  opencl   thread #3 self-test failed
[2022-11-21 12:13:25.097]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:25.098]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.117]  opencl   thread #1 self-test failed
[2022-11-21 12:13:25.118]  opencl   disabled (failed to start threads)


## djlaserman | 2022-11-21T10:16:35+00:00
> `XMRig/6.18.1-mo1` This is not an official XMRig release. Can you reproduce it with the official release?

Here is the output again, showing the miner proceeding with only CPU and having 'disabled' the GPU:

 * ABOUT        XMRig/6.18.1 gcc/11.2.0
 * LIBS         libuv/1.44.1 OpenSSL/1.1.1o hwloc/2.7.1
 * HUGE PAGES   permission granted
 * 1GB PAGES    unavailable
 * CPU          11th Gen Intel(R) Core(TM) i7-11700 @ 2.50GHz (1) 64-bit AES VM
                L2:4.0 MB L3:16.0 MB 8C/16T NUMA:1
 * MEMORY       9.6/31.7 GB (30%)
                Controller0-ChannelA-DIMM0: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelA-DIMM1: 16 GB DDR4 @ 2133 MHz CMW32GX4M2A2666C16
                Controller0-ChannelB-DIMM0: <empty>
                Controller0-ChannelB-DIMM1: <empty>
 * MOTHERBOARD  ASUS - System Product Name
 * DONATE       1%
 * ASSEMBLY     auto:intel
 * POOL #1      gulf.moneroocean.stream:10128 algo auto
 * COMMANDS     hashrate, pause, resume, results, connection
[2022-11-21 12:13:18.307]  config   configuration saved to: "C:\Users\djlas\Desktop\xmrig-6.18.1\config.json"
 * ADL          press e for health report
 * OPENCL       #1 AMD Accelerated Parallel Processing/OpenCL 2.1 AMD-APP (3444.0)
 * OPENCL GPU   #0 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * OPENCL GPU   #1 01:00.0 Radeon RX 580 Series (Ellesmere) 1340 MHz cu:36 mem:6745/8192 MB
 * CUDA         disabled
[2022-11-21 12:13:19.435]  net      use pool gulf.moneroocean.stream:10128  13.228.20.61
[2022-11-21 12:13:19.435]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2760546 (45 tx)
[2022-11-21 12:13:19.436]  cpu      use argon2 implementation AVX-512F
[2022-11-21 12:13:19.436]  msr      to access MSR registers Administrator privileges required.
[2022-11-21 12:13:19.436]  msr      FAILED TO APPLY MSR MOD, HASHRATE WILL BE LOW
[2022-11-21 12:13:19.436]  randomx  init dataset algo rx/0 (16 threads) seed 5282d00ee18f482e...
[2022-11-21 12:13:19.436]  randomx  allocated 2336 MB (2080+256) huge pages 100% 1168/1168 +JIT (0 ms)
[2022-11-21 12:13:23.465]  randomx  dataset ready (4028 ms)
[2022-11-21 12:13:23.465]  cpu      use profile  rx  (8 threads) scratchpad 2048 KB
[2022-11-21 12:13:23.467]  opencl   use profile  rx  (4 threads) scratchpad 2048 KB
|  # | GPU |  BUS ID | INTENSITY | WSIZE | MEMORY | NAME
|  0 |   0 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  1 |   0 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  2 |   1 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
|  3 |   1 | 01:00.0 |       576 |     8 |   1152 | Radeon RX 580 Series (Ellesmere)
[2022-11-21 12:13:23.517]  cpu      READY threads 8/8 (8) huge pages 100% 8/8 memory 16384 KB (50 ms)
[2022-11-21 12:13:24.831]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:24.832]  opencl   thread #0 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:24.892]  opencl   thread #0 self-test failed
[2022-11-21 12:13:24.970]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:24.971]  opencl   thread #2 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.021]  opencl   thread #2 self-test failed
[2022-11-21 12:13:25.040]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:25.041]  opencl   thread #3 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.059]  opencl   thread #3 self-test failed
[2022-11-21 12:13:25.097]  opencl   error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
[2022-11-21 12:13:25.098]  opencl   thread #1 failed with error CL_INVALID_PROGRAM
[2022-11-21 12:13:25.117]  opencl   thread #1 self-test failed
[2022-11-21 12:13:25.118]  opencl   disabled (failed to start threads)
[2022-11-21 12:14:03.611]  net      new job from gulf.moneroocean.stream:10128 diff 128001 algo rx/0 height 2760547 (41 tx)
[2022-11-21 12:14:24.549]  opencl   #0 01:00.0  37W 46C    0RPM 300/2250MHz
[2022-11-21 12:14:24.552]  opencl   #1 01:00.0  37W 46C    0RPM 300/2250MHz
[2022-11-21 12:14:24.555]  miner    speed 10s/60s/15m 1024.4 953.8 n/a H/s max 1114.8 H/s
[2022-11-21 12:14:37.884]  cpu      accepted (1/0) diff 128001 (1210 ms)
[2022-11-21 12:15:25.694]  opencl   #0 01:00.0  37W 48C    0RPM 300/2250MHz
[2022-11-21 12:15:25.696]  opencl   #1 01:00.0  37W 48C    0RPM 300/2250MHz
[2022-11-21 12:15:25.699]  miner    speed 10s/60s/15m 1114.0 1043.3 n/a H/s max 1114.8 H/s
[2022-11-21 12:15:37.379]  net      new job from gulf.moneroocean.stream:10128 diff 27837 algo rx/0 height 2760547 (41 tx)


## SChernykh | 2022-11-21T13:02:50+00:00
This is a different error than what you have in the original post, here it just says `CL_INVALID_PROGRAM`. You can try older AMD drivers (from 2019 or 2020), they should work fine. But mining RandomX on GPU is very inefficient, it's better to try some other algorithm for your GPUs.

## Spudz76 | 2022-11-21T18:57:31+00:00
I never used any driver newer than `20.40-1147286` including Ellesmere RX480.  The newer drivers are broken and/or only focus on fixing newer cores (Vega and so on).  `21.30-1290604` might still work too.

## djlaserman | 2022-11-21T19:42:18+00:00
> This is a different error than what you have in the original post, here it just says `CL_INVALID_PROGRAM`. You can try older AMD drivers (from 2019 or 2020), they should work fine. But mining RandomX on GPU is very inefficient, it's better to try some other algorithm for your GPUs.

It's all one and the same thing, an issue with opencl... yes the error output looks different but the cause is the same. Ok I hear you about trying older drivers, I just thought to report the issue because I thought that bugs should be highlighted so that the underlying problems can be looked at and fixed. 

No worries, when I feel upto the task, I'll fork the repo and load it up in visual studio and see if I can fix it myself. Thanks.

## Spudz76 | 2022-11-21T19:47:01+00:00
Once you fix that, the next driver will break stuff again.  There is nothing useful about newer drivers, on older cards.  If anything they tried to sabotage mining usage in general.  Just use the driver that worked.  This is how AMD has always been.  Even TeamRedMiner needs the same maximum versions of drivers (they claim 21.x work, they might, I just never bothered since I also had even older Hawaii's and stuff which 21.x+ broke).

## djlaserman | 2022-11-22T07:55:32+00:00
> Once you fix that, the next driver will break stuff again. There is nothing useful about newer drivers, on older cards. If anything they tried to sabotage mining usage in general. Just use the driver that worked. This is how AMD has always been. Even TeamRedMiner needs the same maximum versions of drivers (they claim 21.x work, they might, I just never bothered since I also had even older Hawaii's and stuff which 21.x+ broke).

Point taken, it's strange though that there are nbminer, phoenix miner and lolminer all work fine with my GPU and I've never seen such issues at all with them. So while I hear and agree with what you're saying, I'll just take a bash and see if perhaps there can be a workaround opencl in general because even Intel GPUs can't be used either, yet mining is essentially computations or calculations which shouldn't be next to impossible to emulate on the GPUs. I guess I'll need to look at the implementations of what is working and bring that to xmrig, that should fix my curiosity. I know it's not going to be easy, but if I succeed, my branch will be uploaded for those who'd like to use it or take a look to do so.

## Spudz76 | 2022-11-22T19:59:02+00:00
Yeah I fixed some of the Apple OpenCL (OSX) stuff, and thought some of that helped Intel OpenCL but no idea what it does on newer and non-embedded Intels.  It would be useful to have a couple modes autodetected but also manually configurable.  The default is AMD (including proprietary tricks and shortcuts), which might only work on certain drivers, or don't like PAL or HSAIL depending which sort of stack.  If your OpenCL platform doesn't have the string "AMD" in it then it tries a more vanilla OpenCL approach, which is what (somewhat) worked on Intel and nVidia OpenCL, and then if it says "Apple" then it uses some even more generic code because their OpenCL stack is old like 1.1 and very picky.

Not sure I ever had much luck with the RandomX kernels but since that's only a proof-of-concept and will never be profitable to actually use I honestly didn't test it.  Most other useful GPU algos did work.  If you want XMR for mining with a GPU you should cross-mine, and probably some other algos do actually work on your driver.

# Action History
- Created by: djlaserman | 2022-11-21T06:03:20+00:00
- Closed at: 2022-11-22T07:56:58+00:00
