---
title: LibGL driver errors
source_url: https://github.com/monero-project/monero-gui/issues/347
author: abelboldu
assignees: []
labels:
- resolved
created_at: '2016-12-22T23:28:24+00:00'
updated_at: '2017-08-07T18:50:12+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:50:12+00:00'
---

# Original Description
The LibGL library reports errors:
```
% ./start-gui.sh 
app startd
libGL error: unable to load driver: i965_dri.so
libGL error: driver pointer missing
libGL error: failed to load driver: i965
libGL error: unable to load driver: i965_dri.so
libGL error: driver pointer missing
libGL error: failed to load driver: i965
libGL error: unable to load driver: swrast_dri.so
libGL error: failed to load driver: swrast
Unrecognized OpenGL version
Unrecognized OpenGL version
```
so the GUI can't load.

Workaround: Removing the libs/libGL.so.1 file fixes the problem.

OS : Void Linux
Linux tdn 4.9.0_3 #1 SMP PREEMPT Wed Dec 21 16:16:39 UTC 2016 x86_64 GNU/Linux


# Discussion History
## Fornax96 | 2017-04-05T12:25:17+00:00
Having the same problem on Ubuntu 16.10. Deleting libGL.so.1 fixed it.

## Jaqueeee | 2017-04-06T15:19:03+00:00
@Fornax96 You had this issue with Beta2?

## Jaqueeee | 2017-04-06T15:20:43+00:00
I guess not, since that file isn't included in Beta2. 

## Fornax96 | 2017-04-07T08:05:29+00:00
I'll check. I got this version from the monero website, I guess it's outdated?

## Fornax96 | 2017-04-07T08:07:56+00:00
Beta 2 starts without deleting any files :) 

## medusadigital | 2017-04-18T09:35:15+00:00
can be closed

## dEBRUYNE-1 | 2017-08-07T17:45:32+00:00
+resolved

# Action History
- Created by: abelboldu | 2016-12-22T23:28:24+00:00
- Closed at: 2017-08-07T18:50:12+00:00
