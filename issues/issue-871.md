---
title: compilation fails on OSX
source_url: https://github.com/monero-project/monero/issues/871
author: antanst
assignees: []
labels: []
created_at: '2016-06-21T08:31:02+00:00'
updated_at: '2016-07-11T02:28:21+00:00'
type: issue
status: closed
closed_at: '2016-07-06T16:13:43+00:00'
---

# Original Description
Commit #de91bb7

`make release-static` fails with the following error:

https://paste.fedoraproject.org/382447/64978311/


# Discussion History
## radfish | 2016-06-21T23:41:11+00:00
Please try with the commit from #876.


## antanst | 2016-06-22T08:35:46+00:00
I've tried your `pr--missing-noexcept-spec` branch. It doesn't compile and I get the following error:

https://paste.fedoraproject.org/383058/65845411/


## radfish | 2016-06-22T13:08:55+00:00
Sorry, I submitted PR on a different working copy from which I tested, which was based on an old master. I rebased it, please try again. 


## antanst | 2016-06-22T14:39:59+00:00
Still getting an error in branch `pr--missing-noexcept-spec`:

https://paste.fedoraproject.org/383271/06377146/


## radfish | 2016-06-22T19:54:10+00:00
Ok, earlier error went away, now you get an error that's completely unrelated to #876.
Try:

```
  mkdir build
  cd build
  cmake STATIC=ON ..
  make
```

Also, check whether you have libunwind installed, to help diagnose this. During running 'cmake' (as above, with or without STATIC=ON), check output  for "Stack traces disabled" or "Using libunwind to provide stack traces"


## antanst | 2016-06-22T20:03:39+00:00
I installed `libunwind-headers` from homebrew (the only libunwind-related package there is) and tried your instructions.

https://paste.fedoraproject.org/383478/25696146/


## radfish | 2016-06-22T20:13:04+00:00
Ok, the code in stack_trace.cpp that is under STATICLIB is written to be built `-Wl,--wrap=__cxa_throw`, but in CMakeLists, that option is explicitly not passed for APPLE:

```
  if(STATIC AND NOT APPLE AND NOT FREEBSD AND NOT OPENBSD)
    set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -static-libgcc -static-libstdc++")
   set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--wrap=__cxa_throw")
 endif()
```

So, I'm not sure but, but "APPLE" (OSX) seems to be incompatible with STATIC, _but_ from your earlier report, STATICLIB appears to be set (even without STATIC=ON), but it should be not set by default except for MINGW and MSVC (Windows, afaik).

What happens with explicit STATIC=OFF?

Also, check that 'APPLE' variable is actually getting set in cmake (you can do this by inserting into CMakeLists: `message(STATUS "APPLE = ${APPLE}")`. I am not sure how it is supposed to get set. If it doesn't get set, then try `cmake APPLE=1 ..`.

~~Check with and without libunwind-headers installed (theoretically, it should build either way).~~ (No, this is most liklely NOT related to libunwind.)


## antanst | 2016-06-23T09:19:28+00:00
~~With just `STATIC=OFF` it finally compiled successfully. I didn't need to change anything regarding the 'APPLE' variable.~~

Edit - oops. wrong branch. Still getting an error with `STATIC=OFF`. Gonna try fiddling with the APPLE variable.

Thanks for the help.


## radfish | 2016-06-23T21:19:30+00:00
Which error with `STATIC=OFF`? Paste please.


## antanst | 2016-06-24T08:15:34+00:00
Same error as before. https://paste.fedoraproject.org/384017/66756078/


## antanst | 2016-06-27T15:20:46+00:00
Commit e97d96ccfbb639f621cc4f4336c54cc02fa43485 breaks the tree. Right before that bitmonerod compiles fine.

`make release-static` spews the following:

`[ 62%] Building CXX object src/common/CMakeFiles/common.dir/stack_trace.cpp.o
/Users/antonis/cryptos/bitmonero-master/src/common/stack_trace.cpp:116:2: error: libunwind disabled, no stack traces [-Werror,-W#warnings]
#warning libunwind disabled, no stack traces`

while `make release` spews this one.

`[ 63%] Building CXX object src/common/CMakeFiles/common.dir/stack_trace.cpp.o
/Users/antonis/cryptos/bitmonero-master/src/common/stack_trace.cpp:44:17: error: conflicting types for '__cxa_throw'
extern "C" void CXA_THROW(void *ex, void *info, void (*dest)(void*))
                ^
/Users/antonis/cryptos/bitmonero-master/src/common/stack_trace.cpp:41:19: note: expanded from macro 'CXA_THROW'
#define CXA_THROW __cxa_throw
                  ^
/usr/include/cxxabi.h:40:32: note: previous declaration is here
extern LIBCXXABI_NORETURN void __cxa_throw(void * thrown_exception,
                               ^
/Users/antonis/cryptos/bitmonero-master/src/common/stack_trace.cpp:55:23: error: cannot initialize a variable of type 'void (*const)(void *, void *, void (*)(void *))
      __attribute__((noreturn))' with an rvalue of type 'void (*)(void *, void *, void (*)(void *))'
  static void (*const rethrow)(void*, void*, void(*)(void*)) __attribute__((noreturn)) = (void(*)(void*, void*, void(*)(void*)))dlsym(RTLD_NEXT, "__cxa_throw");
                      ^                                                                  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/antonis/cryptos/bitmonero-master/src/common/stack_trace.cpp:116:2: error: libunwind disabled, no stack traces [-Werror,-W#warnings]
#warning libunwind disabled, no stack traces
 ^
3 errors generated.
make[3]: *** [src/common/CMakeFiles/common.dir/stack_trace.cpp.o] Error 1
make[2]: *** [src/common/CMakeFiles/common.dir/all] Error 2
make[1]: *** [all] Error 2
make: *** [release] Error 2`


## radfish | 2016-06-28T04:14:09+00:00
A potential fix for the latter was discussed on IRC. It's an LLVM/Clang-only issue. Edit stack_trace.cpp to match the prototype for CXA_THROW/__cxa_throw to the one found in /usr/include/cxxabi.h (the type of second argument should not be void *). Also, might have to remove 'const' in the assignmnet on line 55. There may or may not be other errors, I don't have Clang handy to test.

Re the former: that's not latest master, is it? I don't have an '#error' statement on line 116 in de91bb7.


## antanst | 2016-06-28T07:37:18+00:00
Thanks for the tip.

Re the former: No it's not master, it's the offending commit e97d96ccfbb639f621cc4f4336c54cc02fa43485.


## antanst | 2016-07-10T16:00:38+00:00
The `error: conflicting types for '__cxa_throw'` problem persists as of 18dd50702407ece54a98563921fa744c6b7c15b2.


## radfish | 2016-07-10T17:31:30+00:00
Nobody fixed anything. Did you try the patch I described above?


## antanst | 2016-07-10T18:46:07+00:00
I didn't, I admit fiddling with C++ code isn't my strong suit. I just mentioned that this issue still exists, since the bug has been closed but not fixed.


## radfish | 2016-07-10T19:27:45+00:00
Oh, you're right. There were two isues with OSX compilation. #876 fixed one of them, but the other one remains. We should either re-open this issue (preferred) or track it in its new duplicate #901.


## radfish | 2016-07-11T02:28:21+00:00
@antanst Could you please try the PR #904 on OSX?


# Action History
- Created by: antanst | 2016-06-21T08:31:02+00:00
- Closed at: 2016-07-06T16:13:43+00:00
