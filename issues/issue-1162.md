---
title: Duplicate link URL in feed.xml
source_url: https://github.com/monero-project/monero-site/issues/1162
author: azuchi
assignees:
- erciccione
labels:
- bug
created_at: '2020-08-28T09:08:06+00:00'
updated_at: '2020-09-23T18:45:00+00:00'
type: issue
status: closed
closed_at: '2020-09-23T18:45:00+00:00'
---

# Original Description
URL in feed.xml is duplicated as below.

```
<link href="https://www.getmonero.org/https://www.getmonero.org/2020/08/22/triptych.html" rel="alternate" type="text/html" title=" Triptych accepted for publication"/>
```

https://web.getmonero.org/feed.xml

Maybe you need to modify the `baseurl` setting in `_config.xml`?

# Discussion History
## erciccione | 2020-08-28T17:09:13+00:00
Looks like the plugin for the feed is using both `url` and `baseurl`(#1119 fixed the same problem, but with autodetection. I guess the two problems are related). Will check.

## erciccione | 2020-08-29T09:35:52+00:00
This was actually symptom of a deeper problem: we enforce a baseurl with a wrong structure and that conflicts with jekyll's structure and consequently, most of the plugins, like `jekyll-feed`, which we use to generate the feed.xml file. We are looking into solutions. This caused other issues, like the problem with autodetection that i mentioned in the comment above.

## erciccione | 2020-08-30T12:31:40+00:00
#1164

# Action History
- Created by: azuchi | 2020-08-28T09:08:06+00:00
- Closed at: 2020-09-23T18:45:00+00:00
