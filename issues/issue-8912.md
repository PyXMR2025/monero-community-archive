---
title: unit_tests fails to compile using gcc 13 and C++14
source_url: https://github.com/monero-project/monero/issues/8912
author: observantraven1018
assignees: []
labels: []
created_at: '2023-06-20T01:19:33+00:00'
updated_at: '2023-09-22T00:06:53+00:00'
type: issue
status: closed
closed_at: '2023-09-21T17:11:55+00:00'
---

# Original Description
This might be more suited to be a gcc bug report (?), but I figured I'd leave a note here anyway.

The `unit_tests` target is failing to compile with gcc 13.1.1, while using the default Monero CXX standard of C++14. If I set `set(CMAKE_CXX_STANDARD 17)` in `CMakeLists.txt`, `unit_tests` compiles without issue on gcc 13.1.1. `unit_tests` also compiles without issue if I use gcc 12.3.0 with CXX standard C++14. This issue occurs on both `master` and `release-v0.18` branches.

OS: Arch Linux
Kernel: Linux 6.3.8
gcc: 13.1.1 20230429
boost: 1.81.0-6

Compilation error:
```
[ 80%] Building CXX object tests/unit_tests/CMakeFiles/unit_tests.dir/epee_boosted_tcp_server.cpp.o
In file included from /home/observantraven1018/temp/monero/contrib/epee/include/net/abstract_tcp_server2.h:529,
                 from /home/observantraven1018/temp/monero/tests/unit_tests/epee_boosted_tcp_server.cpp:41:
/home/observantraven1018/temp/monero/contrib/epee/include/net/abstract_tcp_server2.inl: In instantiation of ‘epee::net_utils::connection<t_protocol_handler>::connection(socket_t&&, std::shared_ptr<shared_state>, epee::net_utils::t_connection_type, ssl_support_t) [with t_protocol_handler = epee::levin::async_protocol_handler<test_epee_connection_ssl_shutdown_Test::TestBody()::context_t>; socket_t = boost::asio::basic_stream_socket<boost::asio::ip::tcp>; ssl_support_t = epee::net_utils::ssl_support_t]’:
/home/observantraven1018/temp/monero/contrib/epee/include/net/abstract_tcp_server2.inl:948:5:   required from ‘epee::net_utils::connection<t_protocol_handler>::connection(io_context_t&, std::shared_ptr<shared_state>, epee::net_utils::t_connection_type, ssl_support_t) [with t_protocol_handler = epee::levin::async_protocol_handler<test_epee_connection_ssl_shutdown_Test::TestBody()::context_t>; io_context_t = boost::asio::io_context; ssl_support_t = epee::net_utils::ssl_support_t]’
/home/observantraven1018/temp/monero/contrib/epee/include/net/abstract_tcp_server2.inl:1216:29:   required from ‘bool epee::net_utils::boosted_tcp_server<t_protocol_handler>::init_server(uint32_t, const std::string&, uint32_t, const std::string&, bool, bool, epee::net_utils::ssl_options_t) [with t_protocol_handler = epee::levin::async_protocol_handler<test_epee_connection_ssl_shutdown_Test::TestBody()::context_t>; uint32_t = unsigned int; std::string = std::__cxx11::basic_string<char>]’
/home/observantraven1018/temp/monero/tests/unit_tests/epee_boosted_tcp_server.cpp:510:21:   required from here
/home/observantraven1018/temp/monero/contrib/epee/include/net/abstract_tcp_server2.inl:964:26: internal compiler error: Segmentation fault
  964 |     m_timers{m_io_context}
      |                          ^
0x1ad0868 internal_error(char const*, ...)
	???:0
0x78b326 emit_mem_initializers(tree_node*)
	???:0
0x85521d instantiate_decl(tree_node*, bool, bool)
	???:0
0x879a43 instantiate_pending_templates(int)
	???:0
0x76ff06 c_parse_final_cleanups()
	???:0
0x9430e4 c_common_parse_file()
	???:0
Please submit a full bug report, with preprocessed source (by using -freport-bug).
Please include the complete backtrace with any bug report.
See <https://bugs.archlinux.org/> for instructions.
make[3]: *** [tests/unit_tests/CMakeFiles/unit_tests.dir/build.make:342: tests/unit_tests/CMakeFiles/unit_tests.dir/epee_boosted_tcp_server.cpp.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:5374: tests/unit_tests/CMakeFiles/unit_tests.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:5381: tests/unit_tests/CMakeFiles/unit_tests.dir/rule] Error 2
make: *** [Makefile:1804: unit_tests] Error 2
```

Actual compilation command:
```
/usr/bin/g++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION -DDEFAULT_DB_TYPE=\\\"lmdb\\\" -DDEVICE_TREZOR_READY=1 -DGTEST_LINKED_AS_SHARED_LIBRARY=1 -DHAVE_EXPLICIT_BZERO -DHAVE_HIDAPI -DHAVE_READLINE -DHAVE_STRPTIME -DHAVE_TREZOR_LIBUSB=1 -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -DPROTOBUF_INLINE_NOT_IN_HEADERS=0 -I/home/observantraven1018/temp/monero/external/rapidjson/include -I/home/observantraven1018/temp/monero/external/easylogging++ -I/home/observantraven1018/temp/monero/src -I/home/observantraven1018/temp/monero/contrib/epee/include -I/home/observantraven1018/temp/monero/external -I/home/observantraven1018/temp/monero/external/supercop/include -I/home/observantraven1018/temp/monero/build/Linux/master/release/generated_include -I/home/observantraven1018/temp/monero/build/Linux/master/release/translations -I/home/observantraven1018/temp/monero/external/db_drivers/liblmdb -I/usr/include/hidapi -I/usr/include/libusb-1.0 -I/home/observantraven1018/temp/monero/contrib/epee/src/../include  -pthread -maes -march=native -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -fPIC  -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=1 -Wformat -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type -fno-strict-aliasing -ftemplate-depth=900 -DNDEBUG -Ofast  -std=c++14  -Wno-undef -Wno-sign-compare -o CMakeFiles/unit_tests.dir/epee_boosted_tcp_server.cpp.o -c /home/observantraven1018/temp/monero/tests/unit_tests/epee_boosted_tcp_server.cpp
```

# Discussion History
## SChernykh | 2023-06-20T14:27:49+00:00
`internal compiler error: Segmentation fault` means that it's a problem with compiler, not with Monero code.

## selsta | 2023-08-09T00:01:32+00:00
Can you reproduce this with 13.2.1?

## 0xFFFC0000 | 2023-09-11T18:07:52+00:00
Can you run the compilation command with `-save-temps ` flag and upload the results here? It should create a few new files `.i` and `.s` files. 

If it fails without generating those, just run the command with `-E` flag to generate the preprocessed file (`.i`).

## selsta | 2023-09-21T17:11:56+00:00
Closing as this isn't a bug in our code.

## 0xFFFC0000 | 2023-09-22T00:03:10+00:00
I'm just commenting on this here in case anyone is curious. 

First of all, I hate parsers and parsers are the part that I have worked least in compilers. When debugging this bug I realized that `current_function_decl` is nullptr while it should not be nullptr. If I remember correctly, `current_function_decl` can be null only before compilation starts or the compilation of current function is finished, so when you are compiling a function, it cannot be null. Anyway, long story short, something was setting the `current_function_decl` to null, while compiling that function. Which is not allowed.

This bug started with this [1]. As you can see it assigned `current_function_decl` without any checks.

But the good news it has been fixed and currently fix is available in the releases/gcc-13 branch and working [2, 3].

This is the simplest case I can find that bug happens https://godbolt.org/z/cq8ThqEf6

1. https://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=041a164ec9b467f9ac2f15980f83f17e3f8ea150;hp=0963cb5fde158cce986523a90fa9edc51c881f31
2. https://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=0d7e5f90597167c36c7816f5bcf689472e8b1940;hp=b16f123ccbb3bb16a6569256bb6500c554d4c333
3. https://gcc.gnu.org/bugzilla//show_bug.cgi?id=109666

# Action History
- Created by: observantraven1018 | 2023-06-20T01:19:33+00:00
- Closed at: 2023-09-21T17:11:55+00:00
