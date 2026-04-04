---
title: Request to add MoneroVision.com as a resource
source_url: https://github.com/monero-project/monero-site/issues/777
author: jspence425
assignees: []
labels: []
created_at: '2018-06-24T21:32:50+00:00'
updated_at: '2018-06-28T02:33:24+00:00'
type: issue
status: closed
closed_at: '2018-06-28T02:33:24+00:00'
---

# Original Description
MoneroVision.com is a recently-launched open-source Monero explorer. It's the first of its kind in that it has a modern design & branding, has estimated transaction timers, and more detailed here: https://medium.com/mycrypto/introducing-monerovision-com-ee0c9656dd3a

I'm submitting this request to get MoneroVision added to the site where appropriate.

Any consideration is appreciated. :) 

# Discussion History
## UkoeHB | 2018-06-24T22:27:06+00:00
monerovision.com loads an empty page on my browser

## jspence425 | 2018-06-24T22:56:45+00:00
Mmm, that’s odd and definitely shouldn’t be happening. Have you tried in a different browser or with a clear cache?

## UkoeHB | 2018-06-25T04:10:18+00:00
Firefox, Safari, and Opera don't work. It may be my outdated OSX- mountain lion.

## erciccione | 2018-06-25T07:49:02+00:00
Yes, monerovision not working. No reason to add it until it's fixed

## erciccione | 2018-06-25T09:17:45+00:00
+merchant

## wtzb | 2018-06-25T09:26:23+00:00
@UkoeHB @erciccione Could you take a look at what your browser console (F12) returns? We are unable to reproduce the issue, perhaps it gives back some useful error we could take a closer look at. Thanks!

## erciccione | 2018-06-25T09:32:28+00:00
Actually now it's working properly. Adding it right now

## erciccione | 2018-06-25T09:36:48+00:00
Added in #779 
Thanks :)

+in progress

## jspence425 | 2018-06-25T17:13:13+00:00
Thank you @erciccione! Much appreciated.

## UkoeHB | 2018-06-25T20:59:55+00:00
Browser console:
SyntaxError: missing = in const declaration main.bundle.js:13:7724

## wbobeirne | 2018-06-25T21:24:37+00:00
`for(const t of M.entries())`

is the relevant line. This looks like something isn't being properly transpiled to ES5, though this is valid Javascript. In the short term, you should probably update your browser, but we can open a relevant issue on MoneroVision.

# Action History
- Created by: jspence425 | 2018-06-24T21:32:50+00:00
- Closed at: 2018-06-28T02:33:24+00:00
