---
title: Travis build timeout for Win64
source_url: https://github.com/monero-project/monero/issues/4978
author: ph4r05
assignees: []
labels: []
created_at: '2018-12-14T12:23:52+00:00'
updated_at: '2018-12-27T20:35:20+00:00'
type: issue
status: closed
closed_at: '2018-12-27T20:35:20+00:00'
---

# Original Description
I am currently struggling with getting Win64 Travis job done under the hard limit, 50 minutes.
E.g., https://travis-ci.org/monero-project/monero/builds/467242133

@TheCharlatan any ideas how we might address this? Do we need to build `qt` in this case? It takes quite a long time and I don't recall seeing it used somewhere in the code.

If we do need it, maybe we can just compile it in docker outside the Travis and cache precompiled versions, in the similar way they are stored in `contrib/depends/built`.

We could store the cached archives on github, download matching versions or recompile from source if there is none. This could also speed up the overall Travis job times. However, I think the Travis is caching built stuff if job finishes in time - which is not the case for Win64. 

Could we maybe Travis-cache `contrib/depends/built` incrementally so the next build can start where the previous finished?



# Discussion History
## sedited | 2018-12-14T17:32:30+00:00
I have a branch containing a travis CI script that should address this, but my Travis account was flagged for illegal activity, so I cannot test it that moment.

## ph4r05 | 2018-12-14T17:34:09+00:00
OK great! btw I had the same problem with the Travis. I dropped them an email and it got resolved in a day or so.

## sedited | 2018-12-23T15:52:12+00:00
Fixed in #5010 

# Action History
- Created by: ph4r05 | 2018-12-14T12:23:52+00:00
- Closed at: 2018-12-27T20:35:20+00:00
