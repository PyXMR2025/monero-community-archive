---
title: Moneropedia links are broken in dev guides
source_url: https://github.com/monero-project/monero-site/issues/1054
author: 00-matt
assignees: []
labels:
- bug
created_at: '2020-06-25T10:35:51+00:00'
updated_at: '2020-08-14T19:11:37+00:00'
type: issue
status: closed
closed_at: '2020-08-14T19:11:37+00:00'
---

# Original Description
Moneropedia links in the dev guides show up as `@entry-name` instead of a link.

![moneropedia-1](https://user-images.githubusercontent.com/48835712/85704154-f3a32280-b6d7-11ea-8034-6b38159de574.png)
![moneropedia-2](https://user-images.githubusercontent.com/48835712/85704158-f43bb900-b6d7-11ea-9fae-9cde8c775cfd.png)


# Discussion History
## erciccione | 2020-06-25T11:47:40+00:00
I think that's happening because we changed the location of the developer guides, which are now in `/resources/developer-guides` instead of `_i18n/LANG/resources/devloper-guides`. I guess the `moneropedia.rb` script in `_plugins` needs to be adapted to catch the files in `/resources/developer-guides` (i'm guessing because i'm not 100% sure those links were working before).

## erciccione | 2020-08-06T16:16:42+00:00
Fixed with #1122

# Action History
- Created by: 00-matt | 2020-06-25T10:35:51+00:00
- Closed at: 2020-08-14T19:11:37+00:00
