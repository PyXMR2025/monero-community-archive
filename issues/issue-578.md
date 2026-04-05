---
title: 'Doesn''t compile on raspberry pi zero. '
source_url: https://github.com/xmrig/xmrig/issues/578
author: dcherrera
assignees: []
labels:
- wontfix
created_at: '2018-04-23T00:19:00+00:00'
updated_at: '2018-11-05T07:14:56+00:00'
type: issue
status: closed
closed_at: '2018-11-05T07:14:56+00:00'
---

# Original Description
I believe its ARMv6 but I'm not sure I'm a shade tree programmer. I have spend 8+ hours trying. can anyone either make the changes necessary to the source or create a binary? raspberry pi zero runs rasbian which is a ubuntu port running gcc 6.3

Error code it gives is
[  2%] Building CXX object CMakeFiles/xmrig.dir/src/api/Api.cpp.o
c++: error: unrecognized command line option ‘-maes’; did you mean ‘-mapcs’?
CMakeFiles/xmrig.dir/build.make:62: recipe for target 'CMakeFiles/xmrig.dir/src/api/Api.cpp.o' failed
make[2]: *** [CMakeFiles/xmrig.dir/src/api/Api.cpp.o] Error 1
CMakeFiles/Makefile2:67: recipe for target 'CMakeFiles/xmrig.dir/all' failed
make[1]: *** [CMakeFiles/xmrig.dir/all] Error 2
Makefile:83: recipe for target 'all' failed
make: *** [all] Error 2


I added armv61 to cmake/cpu.make. I'm kinda at a loss for what to do next

similar to issue 216 but nothing there gives the answer since they did a bug fix and it was for ARMv7

# Discussion History
## dcherrera | 2018-04-23T00:22:00+00:00
Or build instructions for raspian would be great because porting to a new platform is above my pay grade.

## DrStein99 | 2018-04-23T03:20:53+00:00
Is it like 5 or 10 h/s on rasperri?  How many bookshelves full of rasperri pi 3 does it take to get enough hash rate, combined into a proxy to connect to a pool?

## ghost | 2018-04-27T12:53:48+00:00
@DrStein99 The Pi's (Pi-zero, Pi-2, and Pi-3) total hashrate is low, but hashes per watt is actually not terrible, ~10h/s per watt I think, with some configuration tuning.

## dcherrera | 2018-04-27T20:55:15+00:00
Thats why im trying to get xmrig on  the zero. I live off grid and solar is my only option and even low h/s add up when you put up multiples. I want to set miners to run 24/7 because where I live its next to impossible to make a living. I already have a set of laptops running over 1kh/s and iff i add pi0's to each usb and then start adding them to the array i could start seeing some returns. right now i make ~-$3 a day meaning im loosing money. so once i get solar set up i should make $2 a day and the solar will be payed off in a year or less because I'm building the arrays myself for ~$.20 per watt. I already own and use the batteries needed and they payed for themselfs long ago. so at about $600 invested I will shortly have a 2.5kw setup and i want to push as many hashes as possible to get it payed for and be in the clear :) Any help would be appreciated to get this running on the pi0.

## ghost | 2018-04-28T19:05:19+00:00
I have not had success with xmrig on the Pi-zero. Previously, I've had cpuminer-multi running on the zero, but I'm not sure if it's been updated for the new xmr pow. Support for ARMv6 would be nice, but might run into issues similar to some older devices since the new proof of work: https://github.com/xmrig/xmrig/issues/446

I'll be excited if ARMv6 support comes for my fleet of Pi-zeros (https://github.com/xmrig/xmrig/issues/437), but I think there are probably higher priority items for the devs at the moment.

# Action History
- Created by: dcherrera | 2018-04-23T00:19:00+00:00
- Closed at: 2018-11-05T07:14:56+00:00
