---
title: 'History :: Filter validation'
source_url: https://github.com/monero-project/monero-gui/issues/88
author: M5M400
assignees: []
labels: []
created_at: '2016-10-25T12:03:53+00:00'
updated_at: '2016-11-13T17:58:53+00:00'
type: issue
status: closed
closed_at: '2016-11-13T17:58:53+00:00'
---

# Original Description
values for Date and Amount filters can be set in unlogical way:

"Date from" can be bigger than "Date to" and vice versa
"Amount from" can be bigger than "Amount to" and vice versa

Input boxes for amounts also accept alphanumeric/special characters

![screenshot from 2016-10-25 14-03-04](https://cloud.githubusercontent.com/assets/22886679/19685233/db570926-9abb-11e6-830b-96499f9cbe55.png)


# Discussion History
## mbg033 | 2016-11-06T16:14:45+00:00
Fixed here: https://github.com/monero-project/monero-core/pull/120


## fluffypony | 2016-11-13T17:58:53+00:00
Closing as fixed


# Action History
- Created by: M5M400 | 2016-10-25T12:03:53+00:00
- Closed at: 2016-11-13T17:58:53+00:00
