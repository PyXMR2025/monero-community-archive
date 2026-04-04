---
title: Buildbot fails kovri-all-win32
source_url: https://github.com/monero-project/meta/issues/135
author: anonimal
assignees: []
labels: []
created_at: '2017-11-07T21:09:10+00:00'
updated_at: '2017-11-15T20:15:23+00:00'
type: issue
status: closed
closed_at: '2017-11-15T20:15:22+00:00'
---

# Original Description
Apparently buildbot(?) is not running `ar` and `ranlib` for libcryptopp.a so, when the kovri cmake recipe is built, the cryptopp lib is not available: "Could not find Crypto++". Then build is successful when logging onto the same machine and building manually.

https://build.getmonero.org/builders/kovri-all-win32/builds/665

# Discussion History
## danrmiller | 2017-11-15T09:07:48+00:00
Sorry, I didn't see this until now. Here is some more info. 

https://build.getmonero.org/builders/kovri-all-win32/builds/685
I modified the job so it dies on the exit code 1 from cmake not finding Crypto++.  
I also set the VERBOSE environment variable so you can see how its building cryptopp.
And I made it highlight the CMakeOutput.log so we can see if a clue is in there:

https://build.getmonero.org/builders/kovri-all-win32/builds/685/steps/compile/logs/CMakeOutput.log

## danrmiller | 2017-11-15T16:58:43+00:00
That job was running via bash, I don't know why, I've switched it to just let buildbot exec make like all the other jobs and it seems to work

https://build.getmonero.org/builders/kovri-all-win32/builds/686


## anonimal | 2017-11-15T20:15:22+00:00
Thank you for figuring this out and resolving!

# Action History
- Created by: anonimal | 2017-11-07T21:09:10+00:00
- Closed at: 2017-11-15T20:15:22+00:00
