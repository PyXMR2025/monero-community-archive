---
title: 'Buildbot: debian-armv8 machine is offline'
source_url: https://github.com/monero-project/meta/issues/177
author: anonimal
assignees: []
labels: []
created_at: '2018-02-16T01:45:26+00:00'
updated_at: '2020-03-09T21:50:03+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:50:03+00:00'
---

# Original Description
and has been for a while now. Ticketing for housekeeping.

# Discussion History
## danrmiller | 2018-02-23T01:19:51+00:00
we had a hardware failure and its now been replaced

## anonimal | 2018-02-23T04:36:12+00:00
I see that it's back online https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/599/steps/compile/logs/stdio but needs more configuring. I also can't connect to the onion, I don't know if that's related.

## danrmiller | 2018-02-23T04:46:55+00:00
Yes that log is from before everything was installed yes. I thought you told me on irc you could get to the new onion. If you still can't, talk to me there.

## anonimal | 2018-02-25T01:16:57+00:00
You gave me a new onion that I was assuming was for the very out of date rpi3 (that was the context of conversation). The new armv8 onion works, I'll rewrite my aliases.

Thanks for fixing.

## anonimal | 2018-05-01T00:06:42+00:00
Last build was Feb 24th https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/601

## danrmiller | 2018-08-06T00:25:24+00:00
The static build works https://build.getmonero.org/builders/kovri-static-debian-arm8/builds/350

The dynamic build works for me from a bash shell, but from buildbot we get this error:

```
g++ -march=native -DCRYPTOPP_NO_CPU_FEATURE_PROBES=1 -march=armv8.4-a+crypto -c sm4-simd.cpp
Assembler messages:
Error: unknown architecture `armv8.4-a+crypto'

Error: unrecognized option -march=armv8.4-a+crypto
GNUmakefile:1153: recipe for target 'sm4-simd.o' failed
```
https://build.getmonero.org/builders/kovri-all-debian-arm8/builds/605/steps/compile/logs/stdio

The difference is buildbot is running make via execv not a shell. Is there an environment variable we need to set or do you have any other ideas?

# Action History
- Created by: anonimal | 2018-02-16T01:45:26+00:00
- Closed at: 2020-03-09T21:50:03+00:00
