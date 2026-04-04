---
title: Fields have different fontsizes
source_url: https://github.com/monero-project/monero-gui/issues/531
author: ghost
assignees: []
labels:
- wontfix
created_at: '2017-03-03T17:34:50+00:00'
updated_at: '2018-03-30T02:45:19+00:00'
type: issue
status: closed
closed_at: '2018-03-30T02:45:19+00:00'
---

# Original Description
Some pages in the wallet (Send, Address Book, History, Settings) have fields with a larger fontsize. Other pages in the wallet (Receive, Check Payment, Sign/Verify) have fields with a smaller fontsize. Ideally these should look the same.

Address book:
![addressbook](https://cloud.githubusercontent.com/assets/21302237/23561751/9810769a-000d-11e7-924e-74669460dd0b.png)

Receive page:

![receive](https://cloud.githubusercontent.com/assets/21302237/23561758/9f8913b4-000d-11e7-9df8-21f4ee112ced.png)

The smaller fontsize looks best, but it may be slightly on the small size. So perhaps the ideal field fontsize for the entire wallet is one click up, perhaps 16px.

# Discussion History
## ghost | 2017-03-03T18:47:58+00:00
The only exception to this would be pages where a single field is the main focus. For example, it's probably ideal to keep the Password / Confirm password fields in the Wizard at 26px since they are the main focus of the entire page.

## sanderfoobar | 2018-03-30T01:59:16+00:00
Thanks for the report. Please note a new GUI theme is coming for next release. Closing this for now, as text has been reworked.

## sanderfoobar | 2018-03-30T01:59:22+00:00
+wontfix

# Action History
- Created by: ghost | 2017-03-03T17:34:50+00:00
- Closed at: 2018-03-30T02:45:19+00:00
