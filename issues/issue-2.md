---
title: 'Kovri: fix environment for Win/MinGW builds'
source_url: https://github.com/monero-project/meta/issues/2
author: anonimal
assignees: []
labels: []
created_at: '2016-11-06T23:51:51+00:00'
updated_at: '2016-11-07T21:09:32+00:00'
type: issue
status: closed
closed_at: '2016-11-07T21:09:32+00:00'
---

# Original Description
Effects https://github.com/monero-project/kovri/pull/431, build logs [here](https://build.getmonero.org/builders/kovri-all-win64/builds/14/steps/compile/logs/stdio) and [here](https://build.getmonero.org/builders/kovri-all-win32/builds/4/steps/compile/logs/stdio). A fix is currently in-progress, ticketing for housekeeping.

# Discussion History
## danrmiller | 2016-11-07T20:48:15+00:00
I added env={'MSYSTEM': "MINGW32"} and env={'MSYSTEM': "MINGW64"} to the respective build factories and run the make command via the mingw bash shell. Mingw32 and mingw64 builds now compile but fail on tests. See 
https://build.getmonero.org/builders/kovri-all-win32/builds/12 and 
https://build.getmonero.org/builders/kovri-all-win64/builds/23

I opened issue #5 to enable tracking these build config changes.


## anonimal | 2016-11-07T21:09:32+00:00
I've pushed a [fix for tests](https://github.com/monero-project/kovri/pull/442/commits/e51e0b274ae5f89ca60c2d0cdf506ba189be3f2e) (not related to environment).  Everything looks great so far :+1: :beers: I'll reopen this issue if needed.


# Action History
- Created by: anonimal | 2016-11-06T23:51:51+00:00
- Closed at: 2016-11-07T21:09:32+00:00
