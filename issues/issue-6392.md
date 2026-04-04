---
title: Regarding the "various improvements to the ZMQ JSON-RPC handling" commit
source_url: https://github.com/monero-project/monero/issues/6392
author: sumogr
assignees: []
labels: []
created_at: '2020-03-18T06:25:03+00:00'
updated_at: '2020-05-16T15:57:21+00:00'
type: issue
status: closed
closed_at: '2020-05-16T15:57:21+00:00'
---

# Original Description
I have a feeling that on this compile static assert https://github.com/monero-project/monero/blob/master/src/serialization/json_object.cpp#L204 this is not a valid-working comparison
`static_assert(std::numeric_limits<std::uint64_t>::min() <= std::numeric_limits<long long>::min(), "bad int64 conversion");`




# Discussion History
## vtnerd | 2020-03-18T18:05:47+00:00
You have a compiler that is failing here or think it might in some scenario not yet seen?

## xiphon | 2020-03-18T18:20:34+00:00
Guess is about `-Wsign-compare` warning GCC prints during the compilation. From [Ubuntu CI logs](https://github.com/monero-project/monero/commit/0f78b06e8c578819f831a513490278a5f70b01af/checks/491889236/logs):
```c++
/home/runner/work/monero/monero/src/serialization/json_object.cpp: In function â€˜void cryptonote::json::toJsonValue(rapidjson::Writer<rapidjson::GenericStringBuffer<rapidjson::UTF8<> > >&, long long int)â€™:
/home/runner/work/monero/monero/src/serialization/json_object.cpp:204:59: warning: comparison between signed and unsigned integer expressions [-Wsign-compare]
   static_assert(std::numeric_limits<std::uint64_t>::min() <= std::numeric_limits<long long>::min(), "bad int64 conversion");
                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

## sumogr | 2020-03-18T18:23:10+00:00
rethink of the logic behind it. does it seem right to you? the warning is a tell tale


## sumogr | 2020-03-18T18:25:58+00:00
the first part of the assertion is a boolean that must equal to true so as not to break compilation with the message of the second part. the max comparison doesnt throw this warning cause you compare max long long integer with unsigned long long integer. both maxes are positive. Now recheck what you check for minimum IMHO the comparison if it was working the way it is written it should be breaking compilation


## vtnerd | 2020-03-18T22:25:57+00:00
Yes, this was a typo on my part. It was supposed to be `int64_t` because `long long` was being converted to that type on the line below. I have no idea why I reverted from the existing `static_assert` check, I will just revert back to that. There shouldn't be any actual runtime issues, unless `long long` doesn't suddenly fit into a `std::int64_t` on some platform.

## moneromooo-monero | 2020-05-16T15:57:21+00:00
Fixed.

# Action History
- Created by: sumogr | 2020-03-18T06:25:03+00:00
- Closed at: 2020-05-16T15:57:21+00:00
