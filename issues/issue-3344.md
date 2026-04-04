---
title: Can't build master on Windows 10 with MSYS2 MINGW 64
source_url: https://github.com/monero-project/monero/issues/3344
author: limnique
assignees: []
labels: []
created_at: '2018-03-04T06:45:17+00:00'
updated_at: '2018-03-04T07:13:43+00:00'
type: issue
status: closed
closed_at: '2018-03-04T07:13:31+00:00'
---

# Original Description
Hello! I just clone repo https://github.com/monero-project/monero.git
Then I run MSYS2 MINGW 64 and going to modero folder and:

`make release-static-win64`

After few min later I have error:

```
[ 97%] Building CXX object src/daemon/CMakeFiles/daemon.dir/daemon.cpp.obj
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/main.cpp.obj
[ 98%] Building CXX object src/daemon/CMakeFiles/daemon.dir/rpc_command_executor.cpp.obj
In file included from D:/GitHub/monero/src/daemonizer/daemonizer.h:63:0,
                 from D:/GitHub/monero/src/daemon/main.cpp:40:
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl: In function 'boost::filesystem::path daemonizer::get_relative_path_base(const boost::program_options::variables_map&)':
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:114:0: error: no matching function for call to 'has_arg(const boost::program_options::variables_map&, const command_line::arg_descriptor<std::__cxx11::basic_string<char>, false, true>&)'
       if (command_line::has_arg(vm, cryptonote::arg_data_dir))

In file included from D:/GitHub/monero/src/daemon/main.cpp:31:0:
D:/GitHub/monero/src/common/command_line.h:218:8: note: candidate: template<class T, bool required> bool command_line::has_arg(const boost::program_options::variables_map&, const command_line::arg_descriptor<T, required>&)
   bool has_arg(const boost::program_options::variables_map& vm, const arg_descriptor<T, required>& arg)
        ^~~~~~~
D:/GitHub/monero/src/common/command_line.h:218:8: note:   template argument deduction/substitution failed:
In file included from D:/GitHub/monero/src/daemonizer/daemonizer.h:63:0,
                 from D:/GitHub/monero/src/daemon/main.cpp:40:
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:114:0: note:   template argument 'true' does not match 'false'
       if (command_line::has_arg(vm, cryptonote::arg_data_dir))

D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

In file included from D:/GitHub/monero/src/daemonizer/daemonizer.h:63:0,
                 from D:/GitHub/monero/src/daemon/command_line_args.h:34,
                 from D:/GitHub/monero/src/daemon/daemon.cpp:47:
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl: In function 'boost::filesystem::path daemonizer::get_relative_path_base(const boost::program_options::variables_map&)':
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:114:0: error: no matching function for call to 'has_arg(const boost::program_options::variables_map&, const command_line::arg_descriptor<std::__cxx11::basic_string<char>, false, true>&)'
       if (command_line::has_arg(vm, cryptonote::arg_data_dir))

In file included from D:/GitHub/monero/src/cryptonote_core/cryptonote_core.h:43:0,
                 from D:/GitHub/monero/src/rpc/daemon_handler.h:34,
                 from D:/GitHub/monero/src/daemon/daemon.cpp:36:
D:/GitHub/monero/src/common/command_line.h:218:8: note: candidate: template<class T, bool required> bool command_line::has_arg(const boost::program_options::variables_map&, const command_line::arg_descriptor<T, required>&)
   bool has_arg(const boost::program_options::variables_map& vm, const arg_descriptor<T, required>& arg)
        ^~~~~~~
D:/GitHub/monero/src/common/command_line.h:218:8: note:   template argument deduction/substitution failed:
In file included from D:/GitHub/monero/src/daemonizer/daemonizer.h:63:0,
                 from D:/GitHub/monero/src/daemon/command_line_args.h:34,
                 from D:/GitHub/monero/src/daemon/daemon.cpp:47:
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:114:0: note:   template argument 'true' does not match 'false'
       if (command_line::has_arg(vm, cryptonote::arg_data_dir))

D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl: In function 'bool daemonizer::daemonize(int, const char**, T_executor&&, const boost::program_options::variables_map&)':
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:182:0: note: -Wmisleading-indentation is disabled from this point onwards, since column-tracking was disabled due to the size of the code/headers
     return false;

make[3]: *** [src/daemon/CMakeFiles/daemon.dir/build.make:159: src/daemon/CMakeFiles/daemon.dir/main.cpp.obj] Ошибка 1
make[3]: *** Ожидание завершения заданий…
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl: At global scope:
D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:64:0: warning: 'std::__cxx11::string daemonizer::{anonymous}::get_argument_string(int, const char**)' defined but not used [-Wunused-function]
     std::string get_argument_string(int argc, char const * argv[])

In file included from D:/GitHub/monero/src/daemonizer/windows_daemonizer.inl:33:0,
                 from D:/GitHub/monero/src/daemonizer/daemonizer.h:63,
                 from D:/GitHub/monero/src/daemon/command_line_args.h:34,
                 from D:/GitHub/monero/src/daemon/daemon.cpp:47:
D:/GitHub/monero/src/daemonizer/windows_service_runner.h:45:23: warning: 'std::vector<char> windows::{anonymous}::vecstring(const string&)' defined but not used [-Wunused-function]
     std::vector<char> vecstring(std::string const & str)
                       ^~~~~~~~~
make[3]: *** [src/daemon/CMakeFiles/daemon.dir/build.make:111: src/daemon/CMakeFiles/daemon.dir/daemon.cpp.obj] Ошибка 1


make[3]: выход из каталога «/d/GitHub/monero/build/release»
make[2]: *** [CMakeFiles/Makefile2:2875: src/daemon/CMakeFiles/daemon.dir/all] Ошибка 2
make[2]: выход из каталога «/d/GitHub/monero/build/release»
make[1]: *** [Makefile:129: all] Ошибка 2
make[1]: выход из каталога «/d/GitHub/monero/build/release»
make: *** [Makefile:111: release-static-win64] Ошибка 2
```

How I can fix this? On Ubuntu it's making and building without problem but on Windows 10 getting error. Please Help!

# Discussion History
## stoffu | 2018-03-04T06:54:42+00:00
#3318 

## limnique | 2018-03-04T07:13:31+00:00
stoffu, thank you!

# Action History
- Created by: limnique | 2018-03-04T06:45:17+00:00
- Closed at: 2018-03-04T07:13:31+00:00
