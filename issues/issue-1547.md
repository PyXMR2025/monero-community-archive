---
title: 'OSX: CMake error related to liblzma/libunbound'
source_url: https://github.com/monero-project/monero/issues/1547
author: kenshi84
assignees: []
labels: []
created_at: '2017-01-09T04:13:37+00:00'
updated_at: '2017-01-16T16:18:39+00:00'
type: issue
status: closed
closed_at: '2017-01-16T16:18:39+00:00'
---

# Original Description
CMake gives me an error with the recent master, probably related to PR #1494:

Before (dd580d7bc751018017e61f4852f68896f6edf620):

     -- Using LMDB as default DB type
     -- Could not find libunwind (missing:  LIBUNWIND_LIBRARIES) 
     -- Stack trace on exception disabled
     -- Found the miniupnpc libraries at /usr/local/lib/libminiupnpc.a

After (c6ec93962689393291df0ac89267139f5665a44e):

    -- Using LMDB as default DB type
    -- looking for liblzma
    -- liblzma found
    -- Found Libunwind: /usr/include  
    -- Stack trace on exception enabled
    -- Found the miniupnpc libraries at /usr/local/lib/libminiupnpc.a
    ...
    CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
    Please set them or make sure they are set and tested correctly in the CMake files:
    LIBUNWIND_LIBRARIES (ADVANCED)
        linked by target "common" in directory /Users/kenshi/dev/github/monero-project/monero/src/common
    
    -- Configuring incomplete, errors occurred!

@moneromooo-monero 

# Discussion History
## danrmiller | 2017-01-09T04:27:25+00:00
#1494 at least builds on some osx boxes:
https://build.getmonero.org/builders/monero-static-osx-10.10/builds/492
https://build.getmonero.org/builders/monero-static-osx-10.11/builds/485
https://build.getmonero.org/builders/monero-static-osx-10.12/builds/366

Wouldn't c6ec939 be #1542 ?
That seems ok on some osx too:

https://build.getmonero.org/builders/monero-static-osx-10.10/builds/557
https://build.getmonero.org/builders/monero-static-osx-10.11/builds/550
https://build.getmonero.org/builders/monero-static-osx-10.12/builds/431


## kenshi84 | 2017-01-09T04:37:58+00:00
@danrmiller I noticed that too and I got confused. With the recent master, my Mac somehow started to show `Stack trace on exception enabled`. But libunbound is supposed to not be available for Mac, isn't it? Is this happening only to me?

## kenshi84 | 2017-01-09T05:27:45+00:00
Now I figured out: I needed to use `make release-static` instead of just `make`. Decision to do stack trace or not is made at [L279 of CMakeLists.txt](https://github.com/monero-project/monero/blob/c6ec93962689393291df0ac89267139f5665a44e/CMakeLists.txt#L279) and after PR #1494 `LIBUNWIND_FOUND` somehow evaluates to true. (Isn't it weird, since it's not supposed to be available for OSX?)

Perhaps the build instruction should be changed if non-static build is not supported anymore.

## ghost | 2017-01-09T13:26:36+00:00
I think the answer might be to nest the logic on L279  i.e. 'if not (apple or arm) ... if libunwind found' etc. and put L276 inside as well.

## ghost | 2017-01-09T14:01:57+00:00
@kenshi84 would you care to test #1548?

## kenshi84 | 2017-01-09T15:17:27+00:00
@NanoAkron Yes, it works!

## ghost | 2017-01-09T16:30:20+00:00
OK, let me do a bit of extra tweaking to sort out the dynamic compile

## ghost | 2017-01-09T16:47:16+00:00
@kenshi84 @NanoAkron This fixed my breaking OSX build as well. Thanks.

## ghost | 2017-01-16T15:43:59+00:00
Hi @kenshi84, would you mind closing this issue now it's been addressed? Thanks!

## kenshi84 | 2017-01-16T16:18:39+00:00
Forgot to close. Thanks ;)

# Action History
- Created by: kenshi84 | 2017-01-09T04:13:37+00:00
- Closed at: 2017-01-16T16:18:39+00:00
