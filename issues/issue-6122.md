---
title: '[RELEASE] Failed to link librandomx.a on arm64 for ios'
source_url: https://github.com/monero-project/monero/issues/6122
author: naughtyfox
assignees: []
labels: []
created_at: '2019-11-11T13:34:01+00:00'
updated_at: '2019-11-12T11:47:00+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
We are trying to build exawallet with new release libraries. For x86-64 simulator it builds fine, but the linking problem occurs for arm64:
```
Undefined symbols for architecture arm64:
  "_randomx_program_aarch64_main_loop", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_vm_instructions", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_imul_rcp_literals_end", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_init_dataset_aarch64_end", referenced from:
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_init_dataset_aarch64", referenced from:
      randomx::JitCompilerA64::getDatasetInitFunc() in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_vm_instructions_end_light", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_light_cacheline_align_mask", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_calc_dataset_item_aarch64_store_result", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_calc_dataset_item_aarch64_prefetch", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_vm_instructions_end", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_cacheline_align_mask1", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_cacheline_align_mask2", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_calc_dataset_item_aarch64", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64", referenced from:
      randomx::JitCompilerA64::JitCompilerA64() in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::getDatasetInitFunc() in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_calc_dataset_item_aarch64_mix", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_update_spMix1", referenced from:
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_program_aarch64_light_dataset_offset", referenced from:
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
  "_randomx_calc_dataset_item_aarch64_end", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      __GLOBAL__sub_I_jit_compiler_a64.cpp in librandomx.a(jit_compiler_a64.cpp.o)
  "___clear_cache", referenced from:
      void randomx::JitCompilerA64::generateSuperscalarHash<8ul>(randomx::SuperscalarProgram (&) [8ul], std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long> >&) in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::generateProgram(randomx::Program&, randomx::ProgramConfiguration&) in librandomx.a(jit_compiler_a64.cpp.o)
      randomx::JitCompilerA64::generateProgramLight(randomx::Program&, randomx::ProgramConfiguration&, unsigned int) in librandomx.a(jit_compiler_a64.cpp.o)
ld: symbol(s) not found for architecture arm64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

Some debug info:
```
$ nm -C /tmp/librandomx-arm64.a | grep randomx_program_aarch
0000000000000000 T randomx_program_aarch64
0000000000003354 T randomx_program_aarch64_cacheline_align_mask1
0000000000003368 T randomx_program_aarch64_cacheline_align_mask2
000000000000324c T randomx_program_aarch64_imul_rcp_literals_end
000000000000344c T randomx_program_aarch64_light_cacheline_align_mask
0000000000003454 T randomx_program_aarch64_light_dataset_offset
0000000000000100 T randomx_program_aarch64_main_loop
00000000000033a0 T randomx_program_aarch64_update_spMix1
00000000000001e4 T randomx_program_aarch64_vm_instructions
000000000000334c T randomx_program_aarch64_vm_instructions_end
0000000000003430 T randomx_program_aarch64_vm_instructions_end_light
0000000000003370 t randomx_program_aarch64_xor_with_dataset_line
                 U _randomx_program_aarch64
                 U _randomx_program_aarch64_cacheline_align_mask1
                 U _randomx_program_aarch64_cacheline_align_mask2
                 U _randomx_program_aarch64_imul_rcp_literals_end
                 U _randomx_program_aarch64_light_cacheline_align_mask
                 U _randomx_program_aarch64_light_dataset_offset
                 U _randomx_program_aarch64_main_loop
                 U _randomx_program_aarch64_update_spMix1
                 U _randomx_program_aarch64_vm_instructions
                 U _randomx_program_aarch64_vm_instructions_end
                 U _randomx_program_aarch64_vm_instructions_end_light```
```

For x86-64 library:
```
$ nm -C x86_64/librandomx.a | grep randomx_program
00000000000004c0 T _randomx_program_end
0000000000000340 T _randomx_program_epilogue
0000000000000140 T _randomx_program_loop_begin
00000000000002a6 T _randomx_program_loop_end
0000000000000141 T _randomx_program_loop_load
0000000000000262 T _randomx_program_loop_store
0000000000000040 T _randomx_program_prologue
00000000000000ad T _randomx_program_prologue_first_load
00000000000001b2 T _randomx_program_read_dataset
0000000000000232 T _randomx_program_read_dataset_sshash_fin
00000000000001f0 T _randomx_program_read_dataset_sshash_init
00000000000001b1 T _randomx_program_start
                 U _randomx_program_end
                 U _randomx_program_epilogue
                 U _randomx_program_loop_begin
                 U _randomx_program_loop_end
                 U _randomx_program_loop_load
                 U _randomx_program_loop_store
                 U _randomx_program_prologue
                 U _randomx_program_prologue_first_load
                 U _randomx_program_read_dataset
                 U _randomx_program_read_dataset_sshash_fin
                 U _randomx_program_read_dataset_sshash_init
                 U _randomx_program_start
```

The same output for android arm64 library (which works):
```
$ nm -C librandomx.a | grep randomx_program
0000000000000000 T randomx_program_aarch64
0000000000003354 T randomx_program_aarch64_cacheline_align_mask1
0000000000003368 T randomx_program_aarch64_cacheline_align_mask2
000000000000324c T randomx_program_aarch64_imul_rcp_literals_end
000000000000344c T randomx_program_aarch64_light_cacheline_align_mask
0000000000003454 T randomx_program_aarch64_light_dataset_offset
0000000000000100 T randomx_program_aarch64_main_loop
00000000000033a0 T randomx_program_aarch64_update_spMix1
00000000000001e4 T randomx_program_aarch64_vm_instructions
000000000000334c T randomx_program_aarch64_vm_instructions_end
0000000000003430 T randomx_program_aarch64_vm_instructions_end_light
0000000000003370 t randomx_program_aarch64_xor_with_dataset_line
                 U randomx_program_aarch64
                 U randomx_program_aarch64_cacheline_align_mask1
                 U randomx_program_aarch64_cacheline_align_mask2
                 U randomx_program_aarch64_imul_rcp_literals_end
                 U randomx_program_aarch64_light_cacheline_align_mask
                 U randomx_program_aarch64_light_dataset_offset
                 U randomx_program_aarch64_main_loop
                 U randomx_program_aarch64_update_spMix1
                 U randomx_program_aarch64_vm_instructions
                 U randomx_program_aarch64_vm_instructions_end
                 U randomx_program_aarch64_vm_instructions_end_light
```

The problem is in the underscore clang adds to mangle C-symbol, I believe

# Discussion History
## naughtyfox | 2019-11-12T11:47:00+00:00
I filed a bug to randomx library - https://github.com/tevador/RandomX/issues/153. I think the module needs to be updated after fix.

# Action History
- Created by: naughtyfox | 2019-11-11T13:34:01+00:00
