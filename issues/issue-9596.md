---
title: Add support for upcoming Boost 1.87.0 (Boost.Asio removals)
source_url: https://github.com/monero-project/monero/issues/9596
author: cho-m
assignees: []
labels:
- build system
created_at: '2024-11-28T16:08:40+00:00'
updated_at: '2025-02-15T14:21:06+00:00'
type: issue
status: closed
closed_at: '2025-02-15T14:21:06+00:00'
---

# Original Description
Advance notice that Monero does not compile with upcoming Boost 1.87.0 (based on beta1) as Boost.Asio has removed the deprecated io_service https://github.com/boostorg/asio/commit/ec0908c562102915423d8bd7aefd3079efbb6c86

This causes errors like:
```
contrib/epee/include/net/net_utils_base.h:33:10: fatal error: 'boost/asio/io_service.hpp' file not found
   33 | #include <boost/asio/io_service.hpp>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~
```

And impacts all usage of `boost::asio::io_service` (along with various other removed functions/methods)

io_service was deprecated in favor of io_context back in 1.66.0 (https://github.com/boostorg/asio/commit/b60e92b13ef68dfbb9af180d76eae41d22e19356). Easiest approach is to require a minimum of Boost 1.66.0 and use newer APIs. Otherwise, would need to create many `#if BOOST_VERSION ...` conditions for compatibility.

Related: https://www.boost.org/doc/libs/1_86_0/doc/html/boost_asio/net_ts.html

# Discussion History
## tobtoht | 2024-12-13T15:52:21+00:00
Boost 1.87.0 was released a few days ago, so this will start breaking development builds and CI soon.

I'm not very familiar with this part of the codebase. @vtnerd maybe?

## 0xFFFC0000 | 2024-12-13T15:57:10+00:00
that `io_service` to `io_context` for boost is going to be a huge PR. We are using `io_service` in 381 different place, and as asio dev are saying the change is not backward compatible. https://github.com/boostorg/asio/issues/110

## vtnerd | 2024-12-13T16:03:15+00:00
There's more than just the `io_service` removal in this version of boost, so it's going to be rough change. As someone mentioned, we should probably bump the minmum boost version, some of the changes are going to be a tough to workaround otherwise.

## tobtoht | 2024-12-13T16:05:03+00:00
We can bump the minimum to 1.66.0 per #9446 and a PR to bump boost in release builds from 1.64.0 to 1.84.0 is ready.

## vtnerd | 2024-12-17T16:41:31+00:00
I'm working on a patch using Boost 1.66-1.87 as the target. Lots of changes being made, so it may take a while to test them.

## vtnerd | 2024-12-18T02:57:35+00:00
See #9628 

# Action History
- Created by: cho-m | 2024-11-28T16:08:40+00:00
- Closed at: 2025-02-15T14:21:06+00:00
