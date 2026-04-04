---
title: Update GetKovri.org
source_url: https://github.com/monero-project/meta/issues/72
author: anonimal
assignees: []
labels: []
created_at: '2017-05-31T22:20:18+00:00'
updated_at: '2017-06-12T19:48:27+00:00'
type: issue
status: closed
closed_at: '2017-06-12T19:48:27+00:00'
---

# Original Description
I don't know what getkovri.org is pulling from but it should be https://github.com/anonimal/kovri-site until monero-project/kovri-site is online.

# Discussion History
## danrmiller | 2017-05-31T23:39:18+00:00
That is the repo deployed to getkovri.org, origin  https://github.com/anonimal/kovri-site.git (fetch)

We aren't auto-updating during the preview period, we are still at the 740f3d1f2ddd61807db2aca8a41c5de1793eb447 from when the preview setup was requested.



## anonimal | 2017-06-01T18:59:39+00:00
I wasn't sure if the backend was pulling from the old ajs repo or not. But yes, I would hope there would be some automation for pulling from HEAD on master; even if the site isn't "officially" online.

## danrmiller | 2017-06-01T19:05:13+00:00
As you requested in IRC, https://getkovri.org/ has been updated from 740f3d1f2ddd61807db2aca8a41c5de1793eb447 to 67dcff9c74ca83094e5dd9124e46b0030d266736.
New required gem jekyll-multiple-languages-plugin has been installed.

## anonimal | 2017-06-12T19:48:27+00:00
As agreed to in IRC, future updates will be done manually. Thanks @danrmiller. Closing.

# Action History
- Created by: anonimal | 2017-05-31T22:20:18+00:00
- Closed at: 2017-06-12T19:48:27+00:00
