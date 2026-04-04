---
title: 'error: suggest braces around initialization of subobject'
source_url: https://github.com/monero-project/monero/issues/2544
author: danrmiller
assignees: []
labels: []
created_at: '2017-09-27T22:36:32+00:00'
updated_at: '2017-10-03T14:58:36+00:00'
type: issue
status: closed
closed_at: '2017-10-03T14:58:35+00:00'
---

# Original Description
I started getting this error on debian linux aarch64 "stretch" using boost 1.62:

https://build.getmonero.org/builders/monero-static-debian-armv8/builds/1977/steps/compile/logs/stdio

Building CXX object src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o
/mnt/buildbot/buildbot/slave/monero-static-debian-armv8/build/src/cryptonote_protocol/block_queue.cpp:208:44: error: suggest braces around initialization of subobject [-Werror,-Wmissing-braces]
  static const boost::uuids::uuid uuid0 = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

I think it started with #2434, but I'm not sure because I also had unrelated openssl errors building at that time.


# Discussion History
## radfish | 2017-09-28T04:27:34+00:00
From IRC:
2017-09-26 18:47:32     +moneromooo      = boost::uuids::nil_uuid
2017-09-26 18:47:41     +moneromooo     Possibly with () at the end, can't recall.

Perhaps PR that please?

## danrmiller | 2017-09-28T13:26:00+00:00
thanks, OK will test that and then PR

## danrmiller | 2017-10-03T03:54:53+00:00
error: no type named 'nil_uuid' in namespace 'boost::uuids'

## radfish | 2017-10-03T04:00:07+00:00

boost::uuids::uuid u = boost::uuids::nil_uuid();

## moneromooo-monero | 2017-10-03T10:57:02+00:00
https://github.com/monero-project/monero/pull/2571 does this one work ? It works here, so if it doens't work for you it might be a boost version thing.

## danrmiller | 2017-10-03T14:58:35+00:00
Thanks, #2571 works.

# Action History
- Created by: danrmiller | 2017-09-27T22:36:32+00:00
- Closed at: 2017-10-03T14:58:35+00:00
