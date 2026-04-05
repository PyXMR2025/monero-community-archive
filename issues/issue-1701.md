---
title: Issues with AMD OpenCL on MacOS 10.15.4
source_url: https://github.com/xmrig/xmrig/issues/1701
author: jcouzy
assignees: []
labels:
- opencl
created_at: '2020-05-28T22:51:15+00:00'
updated_at: '2021-04-12T14:55:57+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:55:57+00:00'
---

# Original Description
cmake and make instructions work fine on MacOS.

But, when starting xmrig with --opencl the following errors occur:

[2020-05-29 00:38:16.671]  ocl  error CL_BUILD_PROGRAM_FAILURE when calling clBuildProgram
BUILD LOG:
<program source>:815:6: warning: no previous prototype for function 'get_byte32'
uint get_byte32(uint a,uint start_bit) { return (a>>start_bit)&0xFF; }
     ^
<program source>:1067:7: warning: no previous prototype for function 'rotr64'
ulong rotr64(ulong a,ulong shift) { return rotate(a,64-shift); }
      ^
<program source>:1091:6: warning: no previous prototype for function 'blake2b_512_process_single_block'
void blake2b_512_process_single_block(ulong *h,const ulong* m,uint blockTemplateSize)
     ^
<program source>:1152:6: warning: no previous prototype for function 'blake2b_512_process_double_block_32'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1150:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_32
                                              ^
<program source>:1229:6: warning: no previous prototype for function 'blake2b_512_process_double_block_64'
void blake2b_512_process_double_block_name(ulong *out,ulong* m,__global const ulong* in)
     ^
<program source>:1227:47: note: expanded from macro 'blake2b_512_process_double_block_name'
#define blake2b_512_process_double_block_name blake2b_512_process_double_block_64
    
After a short while, the complete system freezes....

Any clues?!

# Discussion History
# Action History
- Created by: jcouzy | 2020-05-28T22:51:15+00:00
- Closed at: 2021-04-12T14:55:57+00:00
