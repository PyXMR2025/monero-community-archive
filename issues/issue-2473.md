---
title: Lastest GIT FTBFS on ppc64el
source_url: https://github.com/monero-project/monero/issues/2473
author: madscientist159
assignees: []
labels:
- duplicate
created_at: '2017-09-18T22:30:28+00:00'
updated_at: '2017-09-19T02:24:21+00:00'
type: issue
status: closed
closed_at: '2017-09-19T02:24:21+00:00'
---

# Original Description
Trying to build latest GIT on ppc64el, got assertion error and FTBFS:

`/home/test/monero/src/serialization/json_object.cpp: In instantiation of ‘void cryptonote::json::{anonymous}::convert_numeric(Source, Type&) [with Source = int; Type = char]’:
/home/test/monero/src/serialization/json_object.cpp:76:20:   required from ‘void cryptonote::json::{anonymous}::to_int(const Value&, Type&) [with Type = char; rapidjson::Value = rapidjson::GenericValue<rapidjson::UTF8<> >]’
/home/test/monero/src/serialization/json_object.cpp:144:16:   required from here
/home/test/monero/src/serialization/json_object.cpp:54:5: error: static assertion failed: source and destination signs do not match
     static_assert(
     ^
src/serialization/CMakeFiles/obj_serialization.dir/build.make:62: recipe for target 'src/serialization/CMakeFiles/obj_serialization.dir/json_object.cpp.o' failed`

# Discussion History
## hyc | 2017-09-19T00:12:32+00:00
+duplicate
#2471 

## danrmiller | 2017-09-19T02:23:41+00:00
@hyc the label bot didn't take action because you aren't in the access list. I added you (https://github.com/monero-project/meta/issues/100#issuecomment-330407739). 

Its already marked this comment as seen in its db, and I think it would be easiest if I just tell it to label this instead of messing with the database, but from now on this should work for you in the monero repo.

+duplicate


# Action History
- Created by: madscientist159 | 2017-09-18T22:30:28+00:00
- Closed at: 2017-09-19T02:24:21+00:00
