---
title: Problem linking with libicu when building on Arch
source_url: https://github.com/monero-project/monero/issues/9140
author: Thomas-995
assignees: []
labels:
- question
- low priority
- reproduction needed
- more info needed
created_at: '2024-01-29T19:45:53+00:00'
updated_at: '2024-02-03T19:07:05+00:00'
type: issue
status: closed
closed_at: '2024-02-03T19:07:05+00:00'
---

# Original Description
I am trying to statically build the project with `make release-static -j8` I have icu and all the other listed dependencies installed but I get the following errors when doing a clean build:
[output.txt](https://github.com/monero-project/monero/files/14088880/output.txt)

6.6.10-arch1-1

# Discussion History
## 0xFFFC0000 | 2024-01-29T20:21:00+00:00
I think error messages tell me this is an issue with your setup. Well before hitting any error related to `icu` you have this error: 

```
Run Build Command(s): /usr/bin/cmake -E env VERBOSE=1 /usr/bin/make -f Makefile cmTC_c8c45/fast
make[1]: Entering directory '/home/thomas/monero/build/Linux/release-v0.18/release/CMakeFiles/CMakeTmp'
/usr/bin/make  -f CMakeFiles/cmTC_c8c45.dir/build.make CMakeFiles/cmTC_c8c45.dir/build
make[2]: Entering directory '/home/thomas/monero/build/Linux/release-v0.18/release/CMakeFiles/CMakeTmp'
Building CXX object CMakeFiles/cmTC_c8c45.dir/test-protobuf.pb.cc.o
/usr/bin/c++  -I/home/thomas/monero/build/Linux/release-v0.18/release -DZMQ_STATIC -pthread  -std=gnu++11 -o CMakeFiles/cmTC_c8c45.dir/test-protobuf.pb.cc.o -c /home/thomas/monero/build/Linux/release-v0.18/release/test-protobuf.pb.cc
In file included from /usr/include/absl/base/config.h:86,
                 from /usr/include/absl/base/attributes.h:37,
                 from /usr/include/google/protobuf/port_def.inc:33,
                 from /home/thomas/monero/build/Linux/release-v0.18/release/test-protobuf.pb.h:13,
                 from /home/thomas/monero/build/Linux/release-v0.18/release/test-protobuf.pb.cc:4:
/usr/include/absl/base/policy_checks.h:79:2: error: #error "C++ versions less than C++14 are not supported."
   79 | #error "C++ versions less than C++14 are not supported."
      |  ^~~~~
/usr/include/google/protobuf/port_def.inc:159:15: error: static assertion failed: Protobuf only supports C++14 and newer.
  159 | static_assert(PROTOBUF_CPLUSPLUS_MIN(201402L), "Protobuf only supports C++14 and newer.");
      |               ^~~~~~~~~~~~~~~~~~~~~~
```



## Thomas-995 | 2024-01-29T21:01:15+00:00
Hey, thanks for getting back so quick. You are right, so I looked into it and protobuf indeed does not support C++ versions less than 14. But I have C++17 so that was weird, so I looked at the cmake log and the c++ binary is being called with:
`/usr/bin/c++  -I/home/thomas/monero/build/Linux/release-v0.18/release -DZMQ_STATIC -pthread  -std=gnu++11 -o CMakeFiles/cm...
` so std=gnu++11 is being passed, which of course results in C++11 being used. I'm probably misunderstanding something but I wonder what the reason for this is and why no one else has this issue. Since gnu++11 being passed directly changes __cplusplus to be less than C++14 which is what protobuf checks for on the line where the error occurs, line 79 of policy_checks.h. 

## selsta | 2024-01-29T21:08:10+00:00
The protobuf error message isn't an issue unless you need Trezor hardware wallet support. It should just skip it, as it says in the CMake log 

```
-- Trezor support disabled
```

Regarding your boost issue, did you custom compile static boost? If yes, did you try to add the `--without-icu` flag, similar to how we do it in release builds?

https://github.com/monero-project/monero/blob/master/contrib/depends/packages/boost.mk#L38C18-L38C31



## Thomas-995 | 2024-01-30T13:33:42+00:00
I did not custom build static boost, should I try doing that?

## 0xFFFC0000 | 2024-01-30T18:45:57+00:00
For some reason you don't link to `icu` :

``` 
/usr/bin/ld: (.text+0x8df): undefined reference to `icu_74::UnicodeString::UnicodeString(char const*)'
```

Can you put the command you are using for cloning, installing dependencies, running the cmake and building here. 

## selsta | 2024-01-30T18:47:30+00:00
I don't know if it's possible to compile static monero with boost installed from the package manager.

I'd recommend to custom compile static boost with the --without-icu flag since we don't need libicu for boost.

## Thomas-995 | 2024-01-31T11:10:41+00:00
Ah I understand, I compiled static boost with --without-icu succesfully. It works with other boost projects but gets a bunch of errors on monero probably indicating I did not compile it right. Is there any documentation on how to compile static boost in a way that would work with the monero project. Thank you.

## selsta | 2024-01-31T11:44:23+00:00
Can you share the errors?

## Thomas-995 | 2024-01-31T11:55:19+00:00
[output.txt](https://github.com/monero-project/monero/files/14111208/output.txt)

I built boost with:
```
./bootstrap.sh --without-icu
./b2 clean
./b2 headers
./b2 -j7 --disable-icu --ignore-site-config variant=release threading=multi install link=static
```


## selsta | 2024-01-31T12:28:06+00:00
Can you try to build boost 1.64 for testing purposes instead of 1.85? 1.85 is still in development.

## Thomas-995 | 2024-01-31T12:36:09+00:00
Get the same errors. Got it from https://www.boost.org/users/history/version_1_64_0.html

## selsta | 2024-01-31T14:15:33+00:00
Just to confirm, did you do a clean build?

## Thomas-995 | 2024-01-31T15:02:40+00:00
Yes, both when I compiled the latest and the 1.64 boost.

## 0xFFFC0000 | 2024-02-01T07:12:19+00:00
I started an arch VM to debug this issue to make sure we are not missing any issues. I was able to compile it without any issues. 

I used boost 1.64.0 from https://www.boost.org/users/history/version_1_64_0.html as you mentioned.

Installed boost with exactly your commands
```
./bootstrap.sh --without-icu -without-libraries=python
./b2 clean
./b2 headers
sudo ./b2 -j7 --disable-icu --ignore-site-config variant=release threading=multi install link=static --disable-python
```

Here is the result of `make release-static -j24` : 

![image](https://github.com/monero-project/monero/assets/136067098/69bdeeb5-260a-4334-8d8e-c021e7e1caad)


P.S. Don't worry about the `dev_0xfffc_add_issue-template`, that is just my personal fork of the master branch. Which doesn't have any code changes in comparison to `master`.

## Thomas-995 | 2024-02-01T16:17:46+00:00
Huh that is odd, I tried it with your commands as well (with -without-libraries=python etc) and I still get the exact same errors. The only difference is that I have to run all the commands with sudo as it doesn't have the permissions to write to the log files otherwise. Besides that I have no idea what could be causing this, maybe some environment variable I set? I also get a bunch of warnings when running the last b2 command, idk if that's normal.

## Thomas-995 | 2024-02-02T20:30:52+00:00
I just `sudo chmod 777 -R *` and built bootstrap without sudo except for the last command. I still get the exact same error when compiling monero project. In what file does net_peerlist.cpp get compiled, so I can play around with it to try and fix the `‘boost::filesystem::copy_option’ has not been declared` error.

## moneromooo-monero | 2024-02-03T09:52:46+00:00
Try https://git.townforge.net/townforge/townforge/commit/05aed8c1e74e6503ac5127ede9def28c3d0ee8d7

## Thomas-995 | 2024-02-03T13:59:30+00:00
There is no such file as "boost_serialization_helper.h" in the latest version of monero as far as I could find. I tried it in another version (in monero-java since compiling that is my end goal) and then I get the error:

```
[ 86%] Linking CXX executable ../../bin/monero-gen-ssl-cert
/usr/bin/ld: ../../contrib/epee/src/libepee.a(mlog.cpp.o): in function `mlog_configure(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, unsigned long, unsigned long)::{lambda(char const*, unsigned long)#1}::operator()(char const*, unsigned long) const [clone .isra.0]':
mlog.cpp:(.text+0x5140): undefined reference to `boost::filesystem::detail::directory_iterator_construct(boost::filesystem::directory_iterator&, boost::filesystem::path const&, boost::filesystem::directory_options, boost::filesystem::detail::directory_iterator_params*, boost::system::error_code*)'
collect2: error: ld returned 1 exit status
make[3]: *** [src/gen_ssl_cert/CMakeFiles/gen_ssl_cert.dir/build.make:121: bin/monero-gen-ssl-cert] Error 1
make[2]: *** [CMakeFiles/Makefile2:3437: src/gen_ssl_cert/CMakeFiles/gen_ssl_cert.dir/all] Error 2
make[2]: *** Waiting for unfinished jobs....
```


## Thomas-995 | 2024-02-03T14:05:55+00:00
And replacing all the listed occurences of if_exists with existing in the given files except for boost_serialization_helper.h in the latest monero src (not in monero-java) I get the following output:
[output.txt](https://github.com/monero-project/monero/files/14151657/output.txt)


## 0xFFFC0000 | 2024-02-03T14:08:30+00:00
> There is no such file as "boost_serialization_helper.h" in the latest version of monero as far as I could find. I tried it in another version (in monero-java since compiling that is my end goal) and then I get the error:
> 
> ```
> [ 86%] Linking CXX executable ../../bin/monero-gen-ssl-cert
> /usr/bin/ld: ../../contrib/epee/src/libepee.a(mlog.cpp.o): in function `mlog_configure(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&, bool, unsigned long, unsigned long)::{lambda(char const*, unsigned long)#1}::operator()(char const*, unsigned long) const [clone .isra.0]':
> mlog.cpp:(.text+0x5140): undefined reference to `boost::filesystem::detail::directory_iterator_construct(boost::filesystem::directory_iterator&, boost::filesystem::path const&, boost::filesystem::directory_options, boost::filesystem::detail::directory_iterator_params*, boost::system::error_code*)'
> collect2: error: ld returned 1 exit status
> make[3]: *** [src/gen_ssl_cert/CMakeFiles/gen_ssl_cert.dir/build.make:121: bin/monero-gen-ssl-cert] Error 1
> make[2]: *** [CMakeFiles/Makefile2:3437: src/gen_ssl_cert/CMakeFiles/gen_ssl_cert.dir/all] Error 2
> make[2]: *** Waiting for unfinished jobs....
> ```

Do you have a Matrix account (or IRC)? I will try to diagnose and fix this issue in live chat [1].  PM me at matrix: `0xfffc`

1. https://www.getmonero.org/community/hangouts/


## Thomas-995 | 2024-02-03T14:10:15+00:00
Even when I try building in a kali vm I get errors such as this one: https://bbs.archlinux.org/viewtopic.php?id=285729. Which I fixed with adding ```#include <cstdint>``` but then I just got libunbound linking errors. I really don't know why I just can't seem to compile it anywhere I try.

## Thomas-995 | 2024-02-03T14:23:06+00:00
Hello, I have joined the monero matrix group, thank you.

## Thomas-995 | 2024-02-03T19:05:21+00:00
Turns out it was a problem with the original (non statically compiled) boost not being entirely removed. Removed all of the leftover boost files and recompiled boost and monero project is successfully compiling now. Thank you to @0xFFFC0000 for walking me through it step by step and resolving the issue.

# Action History
- Created by: Thomas-995 | 2024-01-29T19:45:53+00:00
- Closed at: 2024-02-03T19:07:05+00:00
