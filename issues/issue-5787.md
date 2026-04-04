---
title: Remove unnecessary null pointer checks
source_url: https://github.com/monero-project/monero/issues/5787
author: elfring
assignees: []
labels:
- invalid
created_at: '2019-08-01T11:33:37+00:00'
updated_at: '2019-09-02T11:25:27+00:00'
type: issue
status: closed
closed_at: '2019-09-02T11:25:27+00:00'
---

# Original Description
[An extra null pointer check is not needed in functions](https://isocpp.org/wiki/faq/freestore-mgmt#delete-handles-null "Do I need to check for null before delete p?") like the following.
- [connection](https://github.com/monero-project/monero/blob/ff7dc087ae5f7de162131cea9dbcf8eac7c126a1/contrib/epee/include/net/abstract_tcp_server_cp.h#L131 "Destructor for connection")
- [DaemonHandler::handle](https://github.com/monero-project/monero/blob/fd0cf689ddb62c07fa9d86ca6e070860c51669cc/src/rpc/daemon_handler.cpp#L895 "DaemonHandler::handle function")
- [wallet_rpc_server](https://github.com/monero-project/monero/blob/8adde33e01e76ae929cba7f03ac06fc4eed1f896/src/wallet/wallet_rpc_server.cpp#L108 "Destructor for wallet_rpc_server")

# Discussion History
## iamamyth | 2019-08-05T04:12:03+00:00
They aren't unnecessary, you're linking to the later ISO C++ standards, the relevant parts of which don't take effect until C++14 (afaik, Monero is C++11 compatible):
> If expression evaluates to a null pointer value, no destructors are called, and the deallocation function may or may not be called (it's implementation-defined), but the default deallocation functions are guaranteed to do nothing when handed a null pointer. (until C++14)
> https://en.cppreference.com/w/cpp/language/delete

While it may be that specific situations use the default dellocation functions, it doesn't make sense to rely on that implementation detail, nor does it make sense to retroactively impose a rule that all non-default deallocation functions must check for a nullptr (patching existing code in this manner would likely introduce bugs, and, once C++14 becomes the minimum build standard, such checks would be repeated in the delete implementation as well as the deallocation function itself).

## elfring | 2019-08-05T06:28:55+00:00
I suggest to avoid redundant (null pointer) checks.

## jtgrassie | 2019-08-10T16:09:54+00:00
@elfring they are not "redundant" or "unnecessary", as @iamamyth has detailed.

## elfring | 2019-08-11T08:44:21+00:00
Would you like to clarify constraints for null pointer checks before a function like “`delete`” (or “`free`”) a bit more?

## jtgrassie | 2019-08-11T16:05:06+00:00
The checks are there to ensure a non-null value is passed to `delete`, because _until C++14_, if it were null:

> ... the deallocation function may or may not be called (it's implementation-defined) ... (until C++14)

The Monero codebase supports C++11, so these checks _are_ needed to avoid relying on an implementation detail. As @iamamyth has already answered.

For `free`, (which is new to this discussion - your examples all relate to `delete`), there are old implementations (pre C89) where calling `free(NULL)` would cause a crash. Therefore it's not uncommon to find instances of C code explicitly checking for null before calling free.



## elfring | 2019-08-11T16:32:10+00:00
* Do you find [advice which is given by the C++ FAQ questionable](https://isocpp.org/wiki/faq/freestore-mgmt#delete-handles-null "Do I need to check for null before delete p?") then?
* How do you think about to achieve a better common understanding for mentioned current programming language standards?

## jtgrassie | 2019-08-11T16:49:50+00:00
> Do you find advice which is given by the C++ FAQ questionable then?

No. I find advice a _guide_, not a _reference_ specification.

>> you're linking to the later ISO C++ standards, the relevant parts of which don't take effect until C++14 

so

> How do you think about to achieve a better common understanding for mentioned current programming language standards?

If you read the [c]makefile(s) for a project, you can find the relevant standard a project is building against. For Monero, this is [c++11](https://github.com/monero-project/monero/blob/1bb4ae3b5e9c6e9599fbefb2fd311d7c850ff06c/CMakeLists.txt#L720) and [c11](https://github.com/monero-project/monero/blob/1bb4ae3b5e9c6e9599fbefb2fd311d7c850ff06c/CMakeLists.txt#L719), not c++14.

## elfring | 2019-08-11T17:02:24+00:00
I find it not so relevant to distinguish for a null pointer if a deallocation function will be called by C++11. Such a function will need to tolerate also the passing of null pointers, won't it?

## jtgrassie | 2019-08-11T17:10:39+00:00
This has already been answered very clearly: https://github.com/monero-project/monero/issues/5787#issuecomment-518078772

## elfring | 2019-08-11T17:20:46+00:00
How do you think about to improve affected source code places by the usage of smart pointers instead?

## jtgrassie | 2019-08-11T17:36:50+00:00
> How do you think about to improve affected source code places by the usage of smart pointers instead?

Whether that would be an "improvement" is debatable, but more importantly, why risk introducing new bugs for things that aren't broken?

## elfring | 2019-08-11T17:41:15+00:00
Would you like to take [the C++ guideline “R.11: Avoid calling new and delete explicitly”](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#r11-avoid-calling-new-and-delete-explicitly "Recommendations around allocation and deallocation") into account?

## hyc | 2019-08-11T17:47:51+00:00
This all sounds like change for change's sake. Please stop, this is not a good use of developer time.

## elfring | 2019-08-11T17:49:06+00:00
I propose another bit of source code fine-tuning.

## vtnerd | 2019-08-11T19:27:37+00:00
I hate to do this but -

I read through the C++11 draft spec (actual releases cost money), and the `delete` operator can be passed `null` safely assuming the spec didn't change before and after the finalization of C++11. Also the page that @iamamyth referenced actually says this for "until C++14":

> If expression evaluates to a null pointer value, no destructors are called, and the deallocation function may or may not be called (it's implementation-defined), but the default deallocation functions are guaranteed to do nothing when handed a null pointer. 

The default `delete` can be altered, but we don't do this. Either way, as @jtgrassie @hyc mentioned, the gain is basically nothing so why bother.

As for smart pointers, I would advocate making the changes as actual problems are found. There are some dodgy pointer lifetimes that would be better as `shared_ptr` and might be some exception-safety issues that can be cleared up with `unique_ptr`. Pointers in a class that free in its destructor are generally less of a concern IMO.

## elfring | 2019-08-11T20:02:54+00:00
How do you think about to [use a development tool like “clang-tidy” for corresponding source code adjustments](https://clang.llvm.org/extra/clang-tidy/checks/readability-delete-null-pointer.html "Deletion of unnecessary null pointer checks")?

## hyc | 2019-08-11T20:10:40+00:00
@elfring No.

## iamamyth | 2019-08-12T00:21:52+00:00
@vtnerd Yes, we're quoting the exact same rules. Per my original reply, as the codebase probably doesn't use non-default (de)allocators, one could theoretically eliminate the nullptr checks now, however it would be counter-productive because, as seems to be the consensus, there's minimal benefit in clarity or performance, but lots of code to change. Additionally, classes can override the default allocator, so you'd be adding a constraint not just to the existing internal project code, but every referenced library; relying on chains of implementation details in this fashion seems unwise and dangerous, which is presumably part of the rationale for the change in delete behavior in C++14.

## moneromooo-monero | 2019-09-02T11:16:17+00:00
Mostly pointless, closing.

+invalid

# Action History
- Created by: elfring | 2019-08-01T11:33:37+00:00
- Closed at: 2019-09-02T11:25:27+00:00
