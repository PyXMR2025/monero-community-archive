---
title: ToDo list for migration from gitlab
source_url: https://github.com/monero-project/monero-site/issues/894
author: erciccione
assignees: []
labels:
- 🔔 Priority 🔔
created_at: '2020-04-07T09:27:04+00:00'
updated_at: '2020-05-13T15:28:47+00:00'
type: issue
status: closed
closed_at: '2020-04-19T11:39:57+00:00'
---

# Original Description
We are migrating the monero-site repository from [Gitlab](https://repo.getmonero.org/monero-project/monero-site) to this repository. See discussion in https://github.com/monero-project/meta/issues/236.


This is a todo list of what needs to be done to complete the migration:

- [x] Clean old issues from this repo
- [x] Import issue labels
- [x] import commits from Gitlab
- [x] Import issues
- [x] import pull requests
- [ ] Add contributors with triage powers

~~**Please do not use this repository until the migration is completed.**~~  
Everything has been migrated. Feel free to use the repo, this issue will be closed when the announcement of the migration (#929) is published.

# Discussion History
## erciccione | 2020-04-12T10:26:06+00:00
Issues imported and labelled.

Waiting for the repository to be syncronized with the master on gitlab before asking people to migrate their merge requests (https://repo.getmonero.org/monero-project/monero-site/-/merge_requests) to avoid accidental rebases against an outdated master.

## erciccione | 2020-04-19T11:39:57+00:00
Everything was migrated, except some merge requests where the input of the original opener is needed. So, i think we can consider the migration completed and this issue resolved. I also [posted an update on Reddit](https://www.reddit.com/r/Monero/comments/g463jj/getmoneroorg_updated_migration_to_github_new_faq/).

I asked for people interested in having triage permissions on this repo, but got no answer yet. Those permissions can be edited anytime, so it's definitely not a stopper.

# Action History
- Created by: erciccione | 2020-04-07T09:27:04+00:00
- Closed at: 2020-04-19T11:39:57+00:00
