---
title: compiling on raspbian buster -> failed to create symbolic link 'libminiupnpc.so
source_url: https://github.com/monero-project/monero/issues/8043
author: frnandu
assignees: []
labels: []
created_at: '2021-11-05T10:11:05+00:00'
updated_at: '2021-12-21T05:09:51+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
[  2%] Linking C shared library libminiupnpc.so
CMake Error: failed to create symbolic link 'libminiupnpc.so.17': function not implemented
CMake Error: cmake_symlink_library: System Error: Function not implemented
CMake Error: failed to create symbolic link 'libminiupnpc.so': function not implemented
CMake Error: cmake_symlink_library: System Error: Function not implemented
make[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/build.make:295: external/miniupnp/miniupnpc/libminiupnpc.so.2.2.1] Error 1
make[3]: *** Deleting file 'external/miniupnp/miniupnpc/libminiupnpc.so.2.2.1'
make[3]: Leaving directory '/mnt/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1088: external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/all] Error 2
make[2]: Leaving directory '/mnt/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/mnt/monero/build/release'
make: *** [Makefile:95: release] Error 2
```

```
libminiupnpc-dev is already the newest version (2.1-1+b1).
```
any ideas?

# Discussion History
## selsta | 2021-11-05T18:17:10+00:00
Which branch are you trying to build?

> libminiupnpc-dev is already the newest version (2.1-1+b1).

miniupnp is a submodule so it's not necessary to install it with a package manager.

## frnandu | 2021-11-07T12:25:41+00:00
> Which branch are you trying to build?

release-v0.17
 
> > libminiupnpc-dev is already the newest version (2.1-1+b1).
> 
> miniupnp is a submodule so it's not necessary to install it with a package manager.

I tried building after removing package libminiupnpc-dev:

```
[ 43%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/cpu.cpp.o
[ 43%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/dataset.cpp.o
In file included from /usr/include/c++/8/vector:69,
                 from /media/pi/rootfs/monero/external/randomx/src/dataset.hpp:32,
                 from /media/pi/rootfs/monero/external/randomx/src/dataset.cpp:44:
/usr/include/c++/8/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {const long long unsigned int&}; _Tp = long long unsigned int; _Alloc = std::allocator<long long unsigned int>]’:
/usr/include/c++/8/bits/vector.tcc:413:7: note: parameter passing for argument of type ‘std::vector<long long unsigned int>::iterator’ {aka ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’} changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/8/vector:64,
                 from /media/pi/rootfs/monero/external/randomx/src/dataset.hpp:32,
                 from /media/pi/rootfs/monero/external/randomx/src/dataset.cpp:44:
/usr/include/c++/8/bits/stl_vector.h: In function ‘void randomx::initCache(randomx_cache*, const void*, size_t)’:
/usr/include/c++/8/bits/stl_vector.h:1085:4: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long unsigned int*, std::vector<long long unsigned int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), __x);
    ^~~~~~~~~~~~~~~~~
[ 43%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/soft_aes.cpp.o
[ 43%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/virtual_memory.cpp.o
[ 44%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted.cpp.o
[ 44%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/allocator.cpp.o
[ 44%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/assembly_generator_x86.cpp.o
[ 44%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instruction.cpp.o
[ 44%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/randomx.cpp.o
/media/pi/rootfs/monero/external/randomx/src/randomx.cpp: In function ‘void randomx_calculate_hash(randomx_vm*, const void*, size_t, void*)’:
/media/pi/rootfs/monero/external/randomx/src/randomx.cpp:355:34: warning: requested alignment 16 is larger than 8 [-Wattributes]
   alignas(16) uint64_t tempHash[8];
                                  ^
[ 45%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/superscalar.cpp.o
[ 45%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_compiled.cpp.o
[ 45%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_interpreted_light.cpp.o
[ 45%] Building C object external/randomx/CMakeFiles/randomx.dir/src/argon2_core.c.o
[ 46%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/blake2_generator.cpp.o
[ 46%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/instructions_portable.cpp.o
[ 46%] Building C object external/randomx/CMakeFiles/randomx.dir/src/reciprocal.c.o
[ 46%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/virtual_machine.cpp.o
[ 48%] Building CXX object external/randomx/CMakeFiles/randomx.dir/src/vm_compiled_light.cpp.o
[ 48%] Building C object external/randomx/CMakeFiles/randomx.dir/src/blake2/blake2b.c.o
[ 48%] Building C object external/randomx/CMakeFiles/randomx.dir/src/jit_compiler_a64_static.S.o
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S: Assembler messages:
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:112: Error: shift expression expected -- `sub sp,sp,192'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:113: Error: bad instruction `stp x16,x17,[sp]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:114: Error: bad instruction `stp x18,x19,[sp,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:115: Error: bad instruction `stp x20,x21,[sp,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:116: Error: bad instruction `stp x22,x23,[sp,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:117: Error: bad instruction `stp x24,x25,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:118: Error: bad instruction `stp x26,x27,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:119: Error: bad instruction `stp x28,x29,[sp,96]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:120: Error: bad instruction `stp x8,x30,[sp,112]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:121: Error: bad instruction `stp d8,d9,[sp,128]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:122: Error: bad instruction `stp d10,d11,[sp,144]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:123: Error: bad instruction `stp d12,d13,[sp,160]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:124: Error: bad instruction `stp d14,d15,[sp,176]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:127: Error: ARM register expected -- `mov x4,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:128: Error: ARM register expected -- `mov x5,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:129: Error: ARM register expected -- `mov x6,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:130: Error: ARM register expected -- `mov x7,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:131: Error: ARM register expected -- `mov x12,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:132: Error: ARM register expected -- `mov x13,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:133: Error: ARM register expected -- `mov x14,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:134: Error: ARM register expected -- `mov x15,xzr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:137: Error: bad instruction `ldp x9,x1,[x1]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:140: Error: ARM register expected -- `mov x10,x9'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:143: Error: bad instruction `ldp q24,q25,[x0,192]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:144: Error: bad instruction `ldp q26,q27,[x0,224]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:147: Error: ARM register expected -- `mov x16,0x00FFFFFFFFFFFFFF'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:148: Error: bad instruction `ins v29.d[0],x16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:149: Error: bad instruction `ins v29.d[1],x16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:152: Error: ARM register expected -- `ldr q30,[x0,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:155: Error: ARM register expected -- `mov x16,0x80f0000000000000'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:156: Error: bad instruction `ins v31.d[0],x16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:157: Error: bad instruction `ins v31.d[1],x16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:160: Error: ARM register expected -- `mrs x8,fpcr'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:161: Error: ARM register expected -- `rbit x8,x8'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:164: Error: ARM register expected -- `str x0,[sp,-16]!'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:167: Error: ARM register expected -- `ldr x0,literal_x0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:168: Error: ARM register expected -- `ldr x11,literal_x11'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:169: Error: ARM register expected -- `ldr x20,literal_x20'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:170: Error: ARM register expected -- `ldr x21,literal_x21'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:171: Error: ARM register expected -- `ldr x22,literal_x22'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:172: Error: ARM register expected -- `ldr x23,literal_x23'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:173: Error: ARM register expected -- `ldr x24,literal_x24'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:174: Error: ARM register expected -- `ldr x25,literal_x25'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:175: Error: ARM register expected -- `ldr x26,literal_x26'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:176: Error: ARM register expected -- `ldr x27,literal_x27'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:177: Error: ARM register expected -- `ldr x28,literal_x28'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:178: Error: ARM register expected -- `ldr x29,literal_x29'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:179: Error: ARM register expected -- `ldr x30,literal_x30'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:181: Error: ARM register expected -- `ldr q0,literal_v0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:182: Error: ARM register expected -- `ldr q1,literal_v1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:183: Error: ARM register expected -- `ldr q2,literal_v2'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:184: Error: ARM register expected -- `ldr q3,literal_v3'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:185: Error: ARM register expected -- `ldr q4,literal_v4'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:186: Error: ARM register expected -- `ldr q5,literal_v5'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:187: Error: ARM register expected -- `ldr q6,literal_v6'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:188: Error: ARM register expected -- `ldr q7,literal_v7'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:189: Error: ARM register expected -- `ldr q8,literal_v8'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:190: Error: ARM register expected -- `ldr q9,literal_v9'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:191: Error: ARM register expected -- `ldr q10,literal_v10'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:192: Error: ARM register expected -- `ldr q11,literal_v11'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:193: Error: ARM register expected -- `ldr q12,literal_v12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:194: Error: ARM register expected -- `ldr q13,literal_v13'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:195: Error: ARM register expected -- `ldr q14,literal_v14'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:196: Error: ARM register expected -- `ldr q15,literal_v15'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:201: Error: ARM register expected -- `lsr x18,x10,32'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:204: Error: ARM register expected -- `and w16,w10,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:205: Error: ARM register expected -- `and w17,w18,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:209: Error: ARM register expected -- `add x16,x16,x2'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:210: Error: ARM register expected -- `add x17,x17,x2'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:213: Error: bad instruction `ldp x18,x19,[x16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:214: Error: ARM register expected -- `eor x4,x4,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:215: Error: ARM register expected -- `eor x5,x5,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:216: Error: bad instruction `ldp x18,x19,[x16,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:217: Error: ARM register expected -- `eor x6,x6,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:218: Error: ARM register expected -- `eor x7,x7,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:219: Error: bad instruction `ldp x18,x19,[x16,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:220: Error: ARM register expected -- `eor x12,x12,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:221: Error: ARM register expected -- `eor x13,x13,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:222: Error: bad instruction `ldp x18,x19,[x16,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:223: Error: ARM register expected -- `eor x14,x14,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:224: Error: ARM register expected -- `eor x15,x15,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:227: Error: bad instruction `ldpsw x18,x19,[x17]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:228: Error: bad instruction `ins v16.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:229: Error: bad instruction `ins v16.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:230: Error: bad instruction `ldpsw x18,x19,[x17,8]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:231: Error: bad instruction `ins v17.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:232: Error: bad instruction `ins v17.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:233: Error: bad instruction `ldpsw x18,x19,[x17,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:234: Error: bad instruction `ins v18.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:235: Error: bad instruction `ins v18.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:236: Error: bad instruction `ldpsw x18,x19,[x17,24]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:237: Error: bad instruction `ins v19.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:238: Error: bad instruction `ins v19.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:239: Error: bad instruction `scvtf v16.2d,v16.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:240: Error: bad instruction `scvtf v17.2d,v17.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:241: Error: bad instruction `scvtf v18.2d,v18.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:242: Error: bad instruction `scvtf v19.2d,v19.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:245: Error: bad instruction `ldpsw x18,x19,[x17,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:246: Error: bad instruction `ins v20.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:247: Error: bad instruction `ins v20.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:248: Error: bad instruction `ldpsw x18,x19,[x17,40]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:249: Error: bad instruction `ins v21.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:250: Error: bad instruction `ins v21.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:251: Error: bad instruction `ldpsw x18,x19,[x17,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:252: Error: bad instruction `ins v22.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:253: Error: bad instruction `ins v22.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:254: Error: bad instruction `ldpsw x18,x19,[x17,56]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:255: Error: bad instruction `ins v23.d[0],x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:256: Error: bad instruction `ins v23.d[1],x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:257: Error: bad instruction `scvtf v20.2d,v20.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:258: Error: bad instruction `scvtf v21.2d,v21.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:259: Error: bad instruction `scvtf v22.2d,v22.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:260: Error: bad instruction `scvtf v23.2d,v23.2d'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:261: Error: ARM register expected -- `and v20.16b,v20.16b,v29.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:262: Error: ARM register expected -- `and v21.16b,v21.16b,v29.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:263: Error: ARM register expected -- `and v22.16b,v22.16b,v29.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:264: Error: ARM register expected -- `and v23.16b,v23.16b,v29.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:265: Error: ARM register expected -- `orr v20.16b,v20.16b,v30.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:266: Error: ARM register expected -- `orr v21.16b,v21.16b,v30.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:267: Error: ARM register expected -- `orr v22.16b,v22.16b,v30.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:268: Error: ARM register expected -- `orr v23.16b,v23.16b,v30.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:312: Error: ARM register expected -- `lsr x10,x9,32'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:315: Error: ARM register expected -- `eor x9,x9,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:318: Error: ARM register expected -- `mov w18,w9'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:321: Error: ARM register expected -- `and x18,x18,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:322: Error: ARM register expected -- `add x18,x18,x1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:325: Error: bad instruction `prfm pldl2strm,[x18]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:328: Error: ARM register expected -- `ror x9,x9,32'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:332: Error: ARM register expected -- `and x10,x10,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:333: Error: ARM register expected -- `add x10,x10,x1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:337: Error: bad instruction `ldp x18,x19,[x10]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:338: Error: ARM register expected -- `eor x4,x4,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:339: Error: ARM register expected -- `eor x5,x5,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:340: Error: bad instruction `ldp x18,x19,[x10,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:341: Error: ARM register expected -- `eor x6,x6,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:342: Error: ARM register expected -- `eor x7,x7,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:343: Error: bad instruction `ldp x18,x19,[x10,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:344: Error: ARM register expected -- `eor x12,x12,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:345: Error: ARM register expected -- `eor x13,x13,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:346: Error: bad instruction `ldp x18,x19,[x10,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:347: Error: ARM register expected -- `eor x14,x14,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:348: Error: ARM register expected -- `eor x15,x15,x19'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:352: Error: ARM register expected -- `eor x10,x0,x0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:355: Error: bad instruction `stp x4,x5,[x17,0]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:356: Error: bad instruction `stp x6,x7,[x17,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:357: Error: bad instruction `stp x12,x13,[x17,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:358: Error: bad instruction `stp x14,x15,[x17,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:361: Error: ARM register expected -- `eor v16.16b,v16.16b,v20.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:362: Error: ARM register expected -- `eor v17.16b,v17.16b,v21.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:363: Error: ARM register expected -- `eor v18.16b,v18.16b,v22.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:364: Error: ARM register expected -- `eor v19.16b,v19.16b,v23.16b'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:367: Error: bad instruction `stp q16,q17,[x16,0]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:368: Error: bad instruction `stp q18,q19,[x16,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:370: Error: ARM register expected -- `subs x3,x3,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:374: Error: ARM register expected -- `ldr x0,[sp],16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:377: Error: bad instruction `stp x4,x5,[x0,0]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:378: Error: bad instruction `stp x6,x7,[x0,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:379: Error: bad instruction `stp x12,x13,[x0,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:380: Error: bad instruction `stp x14,x15,[x0,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:383: Error: bad instruction `stp q16,q17,[x0,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:384: Error: bad instruction `stp q18,q19,[x0,96]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:385: Error: bad instruction `stp q20,q21,[x0,128]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:386: Error: bad instruction `stp q22,q23,[x0,160]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:389: Error: bad instruction `ldp x16,x17,[sp]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:390: Error: bad instruction `ldp x18,x19,[sp,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:391: Error: bad instruction `ldp x20,x21,[sp,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:392: Error: bad instruction `ldp x22,x23,[sp,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:393: Error: bad instruction `ldp x24,x25,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:394: Error: bad instruction `ldp x26,x27,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:395: Error: bad instruction `ldp x28,x29,[sp,96]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:396: Error: bad instruction `ldp x8,x30,[sp,112]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:397: Error: bad instruction `ldp d8,d9,[sp,128]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:398: Error: bad instruction `ldp d10,d11,[sp,144]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:399: Error: bad instruction `ldp d12,d13,[sp,160]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:400: Error: bad instruction `ldp d14,d15,[sp,176]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:401: Error: shift expression expected -- `add sp,sp,192'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:403: Error: bad instruction `ret'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:406: Error: shift expression expected -- `sub sp,sp,96'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:407: Error: bad instruction `stp x0,x1,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:408: Error: bad instruction `stp x2,x30,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:411: Error: ARM register expected -- `eor x9,x9,x18'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:414: Error: ARM register expected -- `ror x9,x9,32'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:417: Error: ARM register expected -- `mov x0,x1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:420: Error: ARM register expected -- `mov x1,sp'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:424: Error: ARM register expected -- `and w2,w9,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:427: Error: ARM register expected -- `lsr x2,x2,6'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:431: Error: ARM register expected -- `add x2,x2,0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:432: Error: ARM register expected -- `add x2,x2,0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:436: Error: ARM register expected -- `mov x10,sp'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:437: Error: bad instruction `ldp x0,x1,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:438: Error: bad instruction `ldp x2,x30,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:439: Error: shift expression expected -- `add sp,sp,96'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:454: Error: ARM register expected -- `str x30,[sp,-16]!'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:457: Error: ARM register expected -- `ldr x0,[x0]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:461: Error: ARM register expected -- `add x1,x1,64'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:462: Error: ARM register expected -- `add x2,x2,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:463: Error: ARM register expected -- `cmp x2,x3'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:467: Error: ARM register expected -- `ldr x30,[sp],16'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:469: Error: bad instruction `ret'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:490: Error: shift expression expected -- `sub sp,sp,112'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:491: Error: bad instruction `stp x0,x1,[sp]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:492: Error: bad instruction `stp x2,x3,[sp,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:493: Error: bad instruction `stp x4,x5,[sp,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:494: Error: bad instruction `stp x6,x7,[sp,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:495: Error: bad instruction `stp x8,x9,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:496: Error: bad instruction `stp x10,x11,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:497: Error: bad instruction `stp x12,x13,[sp,96]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:499: Error: ARM register expected -- `ldr x12,superscalarMul0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:501: Error: ARM register expected -- `mov x8,x0'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:502: Error: ARM register expected -- `mov x9,x1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:503: Error: ARM register expected -- `mov x10,x2'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:506: Error: bad instruction `madd x0,x2,x12,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:509: Error: ARM register expected -- `ldr x12,superscalarAdd1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:510: Error: ARM register expected -- `eor x1,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:513: Error: ARM register expected -- `ldr x12,superscalarAdd2'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:514: Error: ARM register expected -- `eor x2,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:517: Error: ARM register expected -- `ldr x12,superscalarAdd3'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:518: Error: ARM register expected -- `eor x3,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:521: Error: ARM register expected -- `ldr x12,superscalarAdd4'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:522: Error: ARM register expected -- `eor x4,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:525: Error: ARM register expected -- `ldr x12,superscalarAdd5'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:526: Error: ARM register expected -- `eor x5,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:529: Error: ARM register expected -- `ldr x12,superscalarAdd6'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:530: Error: ARM register expected -- `eor x6,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:533: Error: ARM register expected -- `ldr x12,superscalarAdd7'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:534: Error: ARM register expected -- `eor x7,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:551: Error: ARM register expected -- `and x11,x10,1'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:552: Error: ARM register expected -- `add x11,x8,x11,lsl 6'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:553: Error: bad instruction `prfm pldl2strm,[x11]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:558: Error: bad instruction `ldp x12,x13,[x11]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:559: Error: ARM register expected -- `eor x0,x0,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:560: Error: ARM register expected -- `eor x1,x1,x13'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:561: Error: bad instruction `ldp x12,x13,[x11,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:562: Error: ARM register expected -- `eor x2,x2,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:563: Error: ARM register expected -- `eor x3,x3,x13'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:564: Error: bad instruction `ldp x12,x13,[x11,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:565: Error: ARM register expected -- `eor x4,x4,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:566: Error: ARM register expected -- `eor x5,x5,x13'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:567: Error: bad instruction `ldp x12,x13,[x11,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:568: Error: ARM register expected -- `eor x6,x6,x12'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:569: Error: ARM register expected -- `eor x7,x7,x13'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:572: Error: bad instruction `stp x0,x1,[x9]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:573: Error: bad instruction `stp x2,x3,[x9,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:574: Error: bad instruction `stp x4,x5,[x9,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:575: Error: bad instruction `stp x6,x7,[x9,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:577: Error: bad instruction `ldp x0,x1,[sp]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:578: Error: bad instruction `ldp x2,x3,[sp,16]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:579: Error: bad instruction `ldp x4,x5,[sp,32]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:580: Error: bad instruction `ldp x6,x7,[sp,48]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:581: Error: bad instruction `ldp x8,x9,[sp,64]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:582: Error: bad instruction `ldp x10,x11,[sp,80]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:583: Error: bad instruction `ldp x12,x13,[sp,96]'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:584: Error: shift expression expected -- `add sp,sp,112'
/media/pi/rootfs/monero/external/randomx/src/jit_compiler_a64_static.S:586: Error: bad instruction `ret'
make[3]: *** [external/randomx/CMakeFiles/randomx.dir/build.make:375: external/randomx/CMakeFiles/randomx.dir/src/jit_compiler_a64_static.S.o] Error 1
make[3]: Leaving directory '/media/pi/rootfs/monero/build/release'
make[2]: *** [CMakeFiles/Makefile2:1547: external/randomx/CMakeFiles/randomx.dir/all] Error 2
make[2]: Leaving directory '/media/pi/rootfs/monero/build/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/media/pi/rootfs/monero/build/release'
make: *** [Makefile:95: release] Error 2
```


## ttmcmurry | 2021-11-26T03:28:21+00:00
"Me too"  .. this is exact behavior happening on a fully up to date Ubuntu 20.04 on Odroid XU4.  Followed the exact same steps and process as frnandu from https://github.com/monero-project/monero.

[ 10%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/portlistingparse.c.o 
[ 10%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/receivedata.c.o
[ 10%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/listdevices.c.o
[ 10%] Building C object external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/addr_is_reserved.c.o
[ 10%] Linking C shared library libminiupnpc.so
CMake Error: failed to create symbolic link 'libminiupnpc.so.17': operation not supported on socket
CMake Error: cmake_symlink_library: System Error: Operation not supported
CMake Error: failed to create symbolic link 'libminiupnpc.so': operation not supported on socket
CMake Error: cmake_symlink_library: System Error: Operation not supported
make[3]: *** [external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/build.make:295:                                                                                                 external/miniupnp/miniupnpc/libminiupnpc.so.2.2.1] Error 1
make[3]: *** Deleting file 'external/miniupnp/miniupnpc/libminiupnpc.so.2.2.1'
make[3]: Leaving directory '/mnt/Miner1/monero/build/Linux/release-v0.17/release'
make[2]: *** [CMakeFiles/Makefile2:1484: external/miniupnp/miniupnpc/CMakeFiles/libminiupnpc-shared.dir/all] Error 2
make[2]: Leaving directory '/mnt/Miner1/monero/build/Linux/release-v0.17/release'
make[1]: *** [Makefile:141: all] Error 2
make[1]: Leaving directory '/mnt/Miner1/monero/build/Linux/release-v0.17/release'
make: *** [Makefile:103: release-all] Error 2


## shermand100 | 2021-11-27T12:53:32+00:00
@selsta Same as above on RPi4 and Odroid XU4 but I've noticed that when building with release-v0.17 I've ended up with a Monerod version shown as 0.17.3 Which is odd because it hasn't been tagged yet. Just adding it here in case it's related to the above.


## selsta | 2021-11-27T16:23:28+00:00
@shermand100 getting v0.17.3.0 is normal, we have to bump the version in source code before tagging.

## hvalev | 2021-12-20T17:32:18+00:00
I'm getting the same error as @frnandu when trying to build from source. Is there an update or a resolution to this? I've so far tried the v0.17.2.3 and v0.17.3.0 branches and it happens on both. I'm building it within a docker container with a debian:buster-20211201 image.

## selsta | 2021-12-21T00:07:03+00:00
@hvalev which docker file are you using?

## hvalev | 2021-12-21T05:09:50+00:00
The dockerfile I'm using is based on the instructions of this repo. 

```
FROM debian:buster-20211201

ENV MONERO_V=release-v0.17

RUN apt-get update && apt-get install -y build-essential cmake pkg-config \
    libzmq3-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev \
    liblzma-dev libreadline6-dev libldns-dev libexpat1-dev libpgm-dev \
    qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev \
    protobuf-compiler libudev-dev libboost-chrono-dev libboost-date-time-dev \
    libboost-filesystem-dev libboost-locale-dev libboost-program-options-dev \
    libboost-regex-dev libboost-serialization-dev libboost-system-dev \
    libboost-thread-dev ccache doxygen graphviz

RUN apt-get install libgtest-dev -y && \
    cd /usr/src/gtest && \
    cmake . && \
    make && \
    mv libg* /usr/lib/

RUN apt-get install git -y && \
    git clone -b ${MONERO_V} --recursive https://github.com/monero-project/monero && \
    cd monero && git submodule init && git submodule update && \
    make && \
    mv build/build/Linux/${MONERO_V}/release/bin/* /

RUN mkdir /data && \
    mkdir /log 

COPY monerod.conf /monerod.conf

CMD [ "/monerod", "--config-file", "/monerod.conf", "--non-interactive" ]
```

For context, I am using GitHub actions to build images for armv7/arm64 and amd64 on a self-hosted runner running arm64 raspiOS. The build actually works for arm64 and amd64 (currently I can confirm this only for the release-v0.17 version), when I removed armv7 as a target. However, for armv7, the build fails with the same error message as in @frnandu when compiling `jit_compiler_a64_static.S.o`. 

# Action History
- Created by: frnandu | 2021-11-05T10:11:05+00:00
