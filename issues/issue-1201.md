---
title: 'feed: invalid links'
source_url: https://github.com/monero-project/monero-site/issues/1201
author: leonklingele
assignees: []
labels:
- duplicate
created_at: '2020-09-18T20:47:16+00:00'
updated_at: '2020-09-19T13:46:53+00:00'
type: issue
status: closed
closed_at: '2020-09-19T13:46:53+00:00'
---

# Original Description
Every link in the [feed](https://www.getmonero.org/feed.xml) is prefixed with `https://www.getmonero.org/`, resulting in invalid URLs. Example:

```atom
<link href="https://www.getmonero.org/https://www.getmonero.org/feed.xml" rel="self" type="application/atom+xml"/>

[..]

<content type="html" xml:base="https://www.getmonero.org/https://www.getmonero.org/2020/09/17/monero-0.17-released.html">
```

# Discussion History
## erciccione | 2020-09-19T13:46:50+00:00
This is a duplicate of #1162. The problem is fixed with #1164, which will be merged soon.

# Action History
- Created by: leonklingele | 2020-09-18T20:47:16+00:00
- Closed at: 2020-09-19T13:46:53+00:00
