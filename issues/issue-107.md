---
title: 'enhancement request: option to disable upnp'
source_url: https://github.com/monero-project/monero/issues/107
author: iamsmooth
assignees: []
labels:
- enhancement
created_at: '2014-08-29T21:03:13+00:00'
updated_at: '2019-05-20T20:26:33+00:00'
type: issue
status: closed
closed_at: '2015-05-07T20:36:56+00:00'
---

# Original Description
No description

# Discussion History
## fluffypony | 2014-08-29T21:18:44+00:00
Just to clarify - at runtime or on compile?


## iamsmooth | 2014-08-29T21:24:28+00:00
Run time. Many coins have an option like "--no-upnp." I didn't see one here.


## fluffypony | 2014-08-29T21:25:44+00:00
Labels added


## rfree2monero | 2014-09-04T22:55:15+00:00
I implemented that (edit: already ago, was bugging me too), as --no-igd 
because that is called IGD here ( http://www.upnp-hacks.org/igd.html )

Not sure if that option was not lost during recent merges;
Try --no-igd on development, best on THIS VERSION from my development:

https://github.com/rfree2monero/bitmonero/commit/3a55e70576ca0cd70bd2e05260453d26141fac05

(it is most stable my version as of today)

If was lost I will readd it in matter of days


## rfree2monero | 2014-09-04T22:55:51+00:00
edit, that is option to the progra   bitmonerod --no-igd


## iamsmooth | 2015-02-03T23:28:08+00:00
seems to not be in master, so still needs to be merged


## fluffypony | 2015-02-04T06:43:36+00:00
@smooth this PR: https://github.com/monero-project/bitmonero/pull/217 is the hold up, that doesn't build on OS X or FreeBSD.


## rfree | 2015-04-07T09:41:35+00:00
It is merged now into master, option is --no-igd


## Geremia | 2019-05-20T20:26:32+00:00
@fluffypony How do I disable `miniupnp` and `libunbound` at compile-time?

# Action History
- Created by: iamsmooth | 2014-08-29T21:03:13+00:00
- Closed at: 2015-05-07T20:36:56+00:00
