---
title: 'Buildbot: use appropriate clang binary name on armv7 machine'
source_url: https://github.com/monero-project/meta/issues/216
author: anonimal
assignees: []
labels: []
created_at: '2018-05-01T03:31:01+00:00'
updated_at: '2018-05-07T21:03:54+00:00'
type: issue
status: closed
closed_at: '2018-05-07T21:03:53+00:00'
---

# Original Description
>`/bin/sh: 1: clang++: not found`

https://build.getmonero.org/builders/kovri-static-ubuntu-arm7/builds/403/steps/compile/logs/stdio


# Discussion History
## anonimal | 2018-05-01T03:32:20+00:00
>make[1]: clang++: Command not found
>make[1]: *** [cryptlib.o] Error 127
>make: *** [release-static-deps] Error 2

Prevents the static build from completing.

## danrmiller | 2018-05-01T16:47:29+00:00
Is it alright with you if we use gcc as we do for the shared lib build instead of clang for this job? I believe one reason we switched to clang on this platform was that the build was a little faster. I'd like to use ccache, and while clang is supposed to be able to work with ccache, I've been reading of several issues, and you can see the failed attempt here:

https://build.getmonero.org/builders/kovri-static-ubuntu-arm7/builds/405

Here is the successful ccache/gcc build:

https://build.getmonero.org/builders/kovri-static-ubuntu-arm7/builds/406

## anonimal | 2018-05-07T21:03:53+00:00
Ok, looks fine to me.

# Action History
- Created by: anonimal | 2018-05-01T03:31:01+00:00
- Closed at: 2018-05-07T21:03:53+00:00
