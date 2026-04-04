---
title: memory corruption at the end of unit_tests in readline code
source_url: https://github.com/monero-project/monero/issues/2298
author: moneromooo-monero
assignees: []
labels: []
created_at: '2017-08-16T07:41:18+00:00'
updated_at: '2017-08-17T19:36:43+00:00'
type: issue
status: closed
closed_at: '2017-08-17T19:36:43+00:00'
---

# Original Description
Run readline without any tests enabled (for speed):

valgrind ./build/debug/tests/unit_tests/unit_tests --gtest_filter=lkjn

We get corruption (and also a deadlock in readline, though I don't get it without valgrind, so this is a race, though probably the same as the one that's already filed):

```
==8580== Memcheck, a memory error detector
==8580== Copyright (C) 2002-2015, and GNU GPL'd, by Julian Seward et al.
==8580== Using Valgrind-3.12.0 and LibVEX; rerun with -h for copyright info
==8580== Command: ./build/debug/tests/unit_tests/unit_tests --gtest_filter=lkjn
==8580== 
Note: Google Test filter = lkjn
[==========] Running 0 tests from 0 test cases.
[==========] 0 tests from 0 test cases ran. (28 ms total)
[  PASSED  ] 0 tests.
==8580== Invalid read of size 8
==8580==    at 0xA9D80F3: std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >::~basic_string() (in /usr/lib64/libstdc++.so.6.0.22)
==8580==    by 0xA98F66: void std::_Destroy<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*) (stl_construct.h:93)
==8580==    by 0xA98942: void std::_Destroy_aux<false>::__destroy<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*) (stl_construct.h:103)
==8580==    by 0xA97D7F: void std::_Destroy<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*) (stl_construct.h:126)
==8580==    by 0xA9682E: void std::_Destroy<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&) (stl_construct.h:151)
==8580==    by 0xA954F0: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~vector() (stl_vector.h:426)
==8580==    by 0xB3B4749: __cxa_finalize (in /usr/lib64/libc-2.24.so)
==8580==    by 0x8E06332: ??? (in /home/user/src/bitmonero/build/debug/src/common/libcommon.so)
==8580==    by 0x40114E9: _dl_fini (in /usr/lib64/ld-2.24.so)
==8580==    by 0xB3B43CF: __run_exit_handlers (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB3B4429: exit (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB39A407: (below main) (in /usr/lib64/libc-2.24.so)
==8580==  Address 0x10405ef0 is 0 bytes inside a block of size 32 free'd
==8580==    at 0x4C2F21A: operator delete(void*) (vg_replace_malloc.c:576)
==8580==    by 0xA98F3D: __gnu_cxx::new_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (new_allocator.h:110)
==8580==    by 0xA98911: std::allocator_traits<std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::deallocate(std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (alloc_traits.h:442)
==8580==    by 0xA97D59: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (stl_vector.h:178)
==8580==    by 0xA967EA: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~_Vector_base() (stl_vector.h:160)
==8580==    by 0xA954FC: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~vector() (stl_vector.h:427)
==8580==    by 0xB3B43CF: __run_exit_handlers (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB3B4429: exit (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB39A407: (below main) (in /usr/lib64/libc-2.24.so)
==8580==  Block was alloc'd at
==8580==    at 0x4C2E1FC: operator new(unsigned long) (vg_replace_malloc.c:334)
==8580==    by 0xAE3E83: __gnu_cxx::new_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::allocate(unsigned long, void const*) (new_allocator.h:104)
==8580==    by 0xADA013: std::allocator_traits<std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::allocate(std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, unsigned long) (alloc_traits.h:416)
==8580==    by 0xAD1EA3: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_allocate(unsigned long) (stl_vector.h:170)
==8580==    by 0xAD02FB: void std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_range_initialize<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*, std::forward_iterator_tag) (stl_vector.h:1285)
==8580==    by 0xAC728A: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::vector(std::initializer_list<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&) (stl_vector.h:379)
==8580==    by 0xF2BAA3: __static_initialization_and_destruction_0(int, int) (readline_buffer.cpp:20)
==8580==    by 0xF2BB6A: _GLOBAL__sub_I_readline_buffer.cpp (readline_buffer.cpp:260)
==8580==    by 0xF5C18C: __libc_csu_init (in /home/user/src/bitmonero/build/debug/tests/unit_tests/unit_tests)
==8580==    by 0xB39A38F: (below main) (in /usr/lib64/libc-2.24.so)
==8580== 
==8580== Invalid free() / delete / delete[] / realloc()
==8580==    at 0x4C2F21A: operator delete(void*) (vg_replace_malloc.c:576)
==8580==    by 0xA98F3D: __gnu_cxx::new_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (new_allocator.h:110)
==8580==    by 0xA98911: std::allocator_traits<std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::deallocate(std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (alloc_traits.h:442)
==8580==    by 0xA97D59: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (stl_vector.h:178)
==8580==    by 0xA967EA: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~_Vector_base() (stl_vector.h:160)
==8580==    by 0xA954FC: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~vector() (stl_vector.h:427)
==8580==    by 0xB3B4749: __cxa_finalize (in /usr/lib64/libc-2.24.so)
==8580==    by 0x8E06332: ??? (in /home/user/src/bitmonero/build/debug/src/common/libcommon.so)
==8580==    by 0x40114E9: _dl_fini (in /usr/lib64/ld-2.24.so)
==8580==    by 0xB3B43CF: __run_exit_handlers (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB3B4429: exit (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB39A407: (below main) (in /usr/lib64/libc-2.24.so)
==8580==  Address 0x10405ef0 is 0 bytes inside a block of size 32 free'd
==8580==    at 0x4C2F21A: operator delete(void*) (vg_replace_malloc.c:576)
==8580==    by 0xA98F3D: __gnu_cxx::new_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (new_allocator.h:110)
==8580==    by 0xA98911: std::allocator_traits<std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::deallocate(std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (alloc_traits.h:442)
==8580==    by 0xA97D59: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_deallocate(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >*, unsigned long) (stl_vector.h:178)
==8580==    by 0xA967EA: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~_Vector_base() (stl_vector.h:160)
==8580==    by 0xA954FC: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::~vector() (stl_vector.h:427)
==8580==    by 0xB3B43CF: __run_exit_handlers (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB3B4429: exit (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB39A407: (below main) (in /usr/lib64/libc-2.24.so)
==8580==  Block was alloc'd at
==8580==    at 0x4C2E1FC: operator new(unsigned long) (vg_replace_malloc.c:334)
==8580==    by 0xAE3E83: __gnu_cxx::new_allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >::allocate(unsigned long, void const*) (new_allocator.h:104)
==8580==    by 0xADA013: std::allocator_traits<std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::allocate(std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >&, unsigned long) (alloc_traits.h:416)
==8580==    by 0xAD1EA3: std::_Vector_base<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_allocate(unsigned long) (stl_vector.h:170)
==8580==    by 0xAD02FB: void std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::_M_range_initialize<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*>(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const*, std::forward_iterator_tag) (stl_vector.h:1285)
==8580==    by 0xAC728A: std::vector<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > >::vector(std::initializer_list<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > >, std::allocator<std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > > const&) (stl_vector.h:379)
==8580==    by 0xF2BAA3: __static_initialization_and_destruction_0(int, int) (readline_buffer.cpp:20)
==8580==    by 0xF2BB6A: _GLOBAL__sub_I_readline_buffer.cpp (readline_buffer.cpp:260)
==8580==    by 0xF5C18C: __libc_csu_init (in /home/user/src/bitmonero/build/debug/tests/unit_tests/unit_tests)
==8580==    by 0xB39A38F: (below main) (in /usr/lib64/libc-2.24.so)
==8580== 
^C^C==8580== 
==8580== Process terminating with default action of signal 2 (SIGINT)
==8580==    at 0xB16C37D: __lll_lock_wait (in /usr/lib64/libpthread-2.24.so)
==8580==    by 0xB169288: pthread_cond_destroy@@GLIBC_2.3.2 (in /usr/lib64/libpthread-2.24.so)
==8580==    by 0xB3B4749: __cxa_finalize (in /usr/lib64/libc-2.24.so)
==8580==    by 0x8E06332: ??? (in /home/user/src/bitmonero/build/debug/src/common/libcommon.so)
==8580==    by 0x40114E9: _dl_fini (in /usr/lib64/ld-2.24.so)
==8580==    by 0xB3B43CF: __run_exit_handlers (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB3B4429: exit (in /usr/lib64/libc-2.24.so)
==8580==    by 0xB39A407: (below main) (in /usr/lib64/libc-2.24.so)
==8580== 
==8580== HEAP SUMMARY:
==8580==     in use at exit: 73,738 bytes in 707 blocks
==8580==   total heap usage: 12,477 allocs, 11,771 frees, 859,043 bytes allocated
==8580== 
==8580== LEAK SUMMARY:
==8580==    definitely lost: 32 bytes in 1 blocks
==8580==    indirectly lost: 0 bytes in 0 blocks
==8580==      possibly lost: 0 bytes in 0 blocks
==8580==    still reachable: 73,706 bytes in 706 blocks
==8580==         suppressed: 0 bytes in 0 blocks
==8580== Rerun with --leak-check=full to see details of leaked memory
==8580== 
==8580== For counts of detected and suppressed errors, rerun with: -v
==8580== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 0 from 0)
```

# Discussion History
# Action History
- Created by: moneromooo-monero | 2017-08-16T07:41:18+00:00
- Closed at: 2017-08-17T19:36:43+00:00
