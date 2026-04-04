---
title: Problem with 0MQ RPC
source_url: https://github.com/monero-project/monero/issues/2471
author: ghost
assignees: []
labels: []
created_at: '2017-09-18T16:44:54+00:00'
updated_at: '2017-09-25T10:49:46+00:00'
type: issue
status: closed
closed_at: '2017-09-23T01:35:10+00:00'
---

# Original Description
```
[ 66%] Building CXX object src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o
/home/nodey/monero/src/serialization/json_object.cpp: In instantiation of ‘void cryptonote::json::{anonymous}::convert_numeric(Source, Type&) [with Source = int; Type = char]’:
/home/nodey/monero/src/serialization/json_object.cpp:76:20:   required from ‘void cryptonote::json::{anonymous}::to_int(const Value&, Type&) [with Type = char; rapidjson::Value = rapidjson::GenericValue<rapidjson::UTF8<> >]’
/home/nodey/monero/src/serialization/json_object.cpp:144:16:   required from here
/home/nodey/monero/src/serialization/json_object.cpp:54:5: error: static assertion failed: source and destination signs do not match
     static_assert(
     ^~~~~~~~~~~~~
src/serialization/CMakeFiles/obj_serialization.dir/build.make:62: recipe for target 'src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o' failed
make[3]: *** [src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o] Error 1
make[3]: Leaving directory '/home/nodey/monero/build/release'
CMakeFiles/Makefile2:1441: recipe for target 'src/serialization/CMakeFiles/obj_serialization.dir/all' failed
make[2]: *** [src/serialization/CMakeFiles/obj_serialization.dir/all] Error 2
make[2]: Leaving directory '/home/nodey/monero/build/release'
Makefile:140: recipe for target 'all' failed
make[1]: *** [all] Error 2
make[1]: Leaving directory '/home/nodey/monero/build/release'
Makefile:55: recipe for target 'release' failed
make: *** [release] Error 2
```
Ping @tewinget 

# Discussion History
## hyc | 2017-09-18T16:58:29+00:00
This trivial patch gets past it. Not sure what the point of these functions is though.
````
diff --git a/src/serialization/json_object.cpp b/src/serialization/json_object.cpp
index ead3fdd5..e183b469 100644
--- a/src/serialization/json_object.cpp
+++ b/src/serialization/json_object.cpp
@@ -141,7 +141,8 @@ void fromJsonValue(const rapidjson::Value& val, unsigned char& i)
 
 void fromJsonValue(const rapidjson::Value& val, char& i)
 {
-  to_int(val, i);
+  signed char j=(signed)i;
+  to_int(val, j);
 }
 
 void fromJsonValue(const rapidjson::Value& val, signed char& i)
````

## ghost | 2017-09-18T17:18:35+00:00
Is there some 0MQ package weirdness with libzmq-dev vs libzmq3-dev, or maybe should we package our own 0MQ headers/library?

## moneromooo-monero | 2017-09-18T17:53:41+00:00
Since there's an override for signed char just below, I guess the override you changed is intended for unsigned char. If 128 is passed, casting to unsigned (from effective signed char) will get you -127. So I think it should be cast to unsigned, not signed ?

## hyc | 2017-09-18T18:10:08+00:00
@moneromooo-monero No. Then the function would use to_uint() instead. See the explicit handler for unsigned char 5 lines above.

to_int() is clearly for signed integers, and this code clearly assumed char was also signed by default.

## hyc | 2017-09-18T18:11:42+00:00
The patch I pasted here is probably wrong of course. Since `i` is being passed in by reference, presumably the resulting value in `j` needs to be assigned back to `i` before returning.

## moneromooo-monero | 2017-09-18T18:14:45+00:00
Hmm, OK, I just looked at the patch, so nevermind.

## ghost | 2017-09-18T18:19:28+00:00
This why I don't understand why people aren't happier to use explicit type definitions like uint_8 and int_8 instead of unsigned char and char

## tewinget | 2017-09-19T06:51:27+00:00
libzmq-dev is zmq 2 iirc, want to use libzmq3-dev on *buntu.  As for
including zmq in our build instead, that seems reasonable.

On Sep 18, 2017 1:18 PM, "Nano Akron" <notifications@github.com> wrote:

> Is there some 0MQ package weirdness with libzmq-dev vs libzmq3-dev, or
> maybe should we package our own 0MQ headers/library?
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2471#issuecomment-330291944>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5gTzHkmj6yTFWyF1mgtyXggZfv9yks5sjqXugaJpZM4PbMy0>
> .
>


## ghost | 2017-09-19T09:35:26+00:00
@tewinget I'm using libzmq3-dev on Ubuntu 16.04 but unfortunately it's still refusing to build. Can you see how to fix the signedness issue?

## tewinget | 2017-09-19T11:37:13+00:00
@NanoAkron I just did a fresh build on my Ubuntu 17.04 box with no issue.  Can you give me more specifics on your build environment?

## hyc | 2017-09-19T13:02:16+00:00
tewinget: builds fail on ARM and ppc64 because their chars are not signed.

## vtnerd | 2017-09-19T14:48:26+00:00
@NanoAkron I was responsible for removing the `uint8_t` etc., variations that @tewinget initially wrote. I removed them because some data structure uses `std::size_t` (which is irritating obviously). `std::size_t` on some platforms is **not** the same type as `std::uint32_t` or `std::uint64_t` so it wasn't possible to catch all scenarios with _just_ those aliases (this was from the caller side). I convinced @tewinget  to go with the "actual" types to catch all scenarios.

The purpose of this function is to convert from a rapidjson object which only provides `IsInt()`, `IsUint()`,  is `IsInt64()`, and `IsUint64()` into a potentially smaller destination. This particular static_assert was to prevent undefined behavior when signed integers can be converted to unsigned integers in comparison operations. It shouldn't happen in this scenario since `char` is always going to be converted to an `int` regardless of its sign.

IMO the easiest fix is to update the static assert:
```c++
static_assert(
      std::is_same<Type, char>() ||
      std::numeric_limits<Source>::is_signed == std::numeric_limits<Type>::is_signed,
      "source may have undefined behavior in comparisons below"
    );
```
EDIT: Wrong template argument, sorry! See corrected version if you got this by email.

## tewinget | 2017-09-19T17:12:13+00:00
Thanks @vtnerd.

On Sep 19, 2017 10:48 AM, "Lee Clagett" <notifications@github.com> wrote:

> @NanoAkron <https://github.com/nanoakron> I was responsible for removing
> the uint8_t etc., variations that @tewinget <https://github.com/tewinget>
> initially wrote. I removed them because some data structure uses
> std::size_t (which is irritating obviously). std::size_t on some
> platforms is *not* the same type as std::uint32_t or std::uint64_t so it
> wasn't possible to catch all scenarios with *just* those aliases (this
> was from the caller side). I convinced @tewinget
> <https://github.com/tewinget> to go with the "actual" types to catch all
> scenarios.
>
> The purpose of this function is to convert from a rapidjson object which
> only provides IsInt(), IsUint(), is IsInt64(), and IsUint64() into a
> potentially smaller destination. This particular static_assert was to
> prevent undefined behavior when signed integers can be converted to
> unsigned integers in comparison operations. It shouldn't happen in this
> scenario since char is always going to be converted to an int regardless
> of its sign.
>
> IMO the easiest fix is to update the static assert:
>
> static_assert(
>       std::is_same<Source, char>() ||
>       std::numeric_limits<Source>::is_signed == std::numeric_limits<Type>::is_signed,
>       "source may have undefined behavior in comparisons below"
>     );
>
> —
> You are receiving this because you were mentioned.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2471#issuecomment-330564118>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AE3k5qJ2zBFK9UVnXqz3O4wMX1XWeiVwks5sj9REgaJpZM4PbMy0>
> .
>


## ghost | 2017-09-23T01:35:10+00:00
Closing in favour of @vtnerd’s fix

## bitkevin | 2017-09-25T10:49:46+00:00
Docker build with zmq issue link: https://github.com/monero-project/monero/issues/2520

# Action History
- Created by: ghost | 2017-09-18T16:44:54+00:00
- Closed at: 2017-09-23T01:35:10+00:00
