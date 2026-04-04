---
title: Taiga fails to notify via email
source_url: https://github.com/monero-project/meta/issues/227
author: michaesc
assignees: []
labels: []
created_at: '2018-05-29T11:07:39+00:00'
updated_at: '2020-06-05T15:39:38+00:00'
type: issue
status: closed
closed_at: '2020-06-05T15:39:38+00:00'
---

# Original Description
There is no documentation informing of what should happen when _Contact the project_ HTML form button is pressed on Taiga project pages, however common sense indicates that an email should reach the intended recipients who are most likely the project administrators.

If this is the case, then the current Taiga implementation or configuration is flawed.

### Reproduction

To reproduce an error resulting from this flaw:

1) Navigate to the [Vegas Events project](https://taiga.getmonero.org/project/michael-vegas-august-2018/)
2) Click **Contact the project team**
3) Enter a suitable test message (versioned please)
4) Ask any project administrator if they were notified by email

### Assistance

We (the Vegas team) can assist anyone repairing this flaw by making them a project member and raising them to administrator role. Please request this on #monero-community. There are **four** (!) administrators who can assist with testing.

### Related

It's possible that this flaw relates to [the problem](https://github.com/monero-project/meta/issues/131/) we had before regarding a host ACL.

# Discussion History
## scottAnselmo | 2018-06-04T16:26:36+00:00
FYI for whoever will work/is working this... I am one of said people and can be reached via saying 'xmrscott' on #monero-community. Other three are msvb-lab, rehrar, and sean

## anonimal | 2018-06-28T23:22:32+00:00
Has this issue been resolved?

## erciccione | 2018-06-29T11:00:58+00:00
I currently receive emails from people clicking the "contact the project button" with no issues (for the monero localizations workgroup), but i also never had this problem in past so....

# Action History
- Created by: michaesc | 2018-05-29T11:07:39+00:00
- Closed at: 2020-06-05T15:39:38+00:00
