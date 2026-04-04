---
title: 'German - index.html href error 404 '
source_url: https://github.com/monero-project/monero-site/issues/1939
author: nice42q
assignees: []
labels:
- bug
created_at: '2022-03-23T12:32:41+00:00'
updated_at: '2022-04-06T10:15:14+00:00'
type: issue
status: closed
closed_at: '2022-04-06T10:15:14+00:00'
---

# Original Description
https://www.getmonero.org/de/index.html
The Hyperlink "Arbeitsgruppen" in the footer is linked wrong (404)

# Discussion History
## erciccione | 2022-04-03T09:20:11+00:00
Thanks @nice42q :)

The i18n links are not being redirected. @binaryFate  we need a redirect for `https://www.getmonero.org/$LANG/community/team/` -> `https://www.getmonero.org/$LANG/community/workgroups/`. Right now it's working only for the English version.

## binaryFate | 2022-04-03T21:35:56+00:00
Ah yes, sorry that was on me.
I'll post here to confirm when done.

## binaryFate | 2022-04-04T17:12:59+00:00
Ok I fixed it and tested successfully. Can someone else check too?

## nice42q | 2022-04-04T17:19:30+00:00
> Ok I fixed it and tested successfully. Can someone else check too?

No more 404 error.
But it redirects to English instead of the selected language.

## binaryFate | 2022-04-05T12:48:59+00:00
@nice42q sorry, please check again

## erciccione | 2022-04-06T06:25:55+00:00
Seems to be working now. @nice42q if everything is ok now, please close the issue.

# Action History
- Created by: nice42q | 2022-03-23T12:32:41+00:00
- Closed at: 2022-04-06T10:15:14+00:00
