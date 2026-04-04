---
title: Taiga integrations localhost is funky
source_url: https://github.com/monero-project/meta/issues/131
author: michaesc
assignees: []
labels:
- resolved
created_at: '2017-10-26T16:03:55+00:00'
updated_at: '2017-11-05T16:40:04+00:00'
type: issue
status: closed
closed_at: '2017-11-05T16:40:04+00:00'
---

# Original Description
To reproduce:

Click 'Admin'
Click 'Integrations'
Click 'Github'
Find 'Payload URL'

Problem:

Payload URL shows 'localhost' but it should be taiga.getmonero.org or something public, shouldn't it?

In other words, how can this feature be used while the hostname states 'localhost'?

# Discussion History
## danrmiller | 2017-11-02T17:50:30+00:00
Thanks. Looks like it works now.  

I added ```SITES["api"]["domain"] = "taiga.getmonero.org"``` to settings/local.py.

## danrmiller | 2017-11-05T16:37:28+00:00
+resolved

# Action History
- Created by: michaesc | 2017-10-26T16:03:55+00:00
- Closed at: 2017-11-05T16:40:04+00:00
