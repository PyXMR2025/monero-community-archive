---
title: 'Discussion:  Deployment of Docs website '
source_url: https://github.com/monero-project/monero-docs/issues/18
author: dan-is-not-the-man
assignees: []
labels: []
created_at: '2024-08-13T07:28:41+00:00'
updated_at: '2025-06-29T20:45:33+00:00'
type: issue
status: closed
closed_at: '2025-06-29T20:45:33+00:00'
---

# Original Description
So currently for testing plowsof and i are using coolify with a dockerfile located in the repo. When a pr is made or pushed to a branch set in coolify, it updates the webpage with the changes. For coolify to work it requires github app setup between coolify and github

Options :

1. Run monero-docs  with coolify only and when a pr is made its creates a preview-deployment  webpage before its merges to main and website has to be manually git pulled and updated

2. Completely  deploy with coolfy in terms of preview-deployment and live website.

- [Preview deployment with coolify](https://coolify.io/docs/knowledge-base/applications#preview-deployments)
- [Github app setup with coolify](https://coolify.io/docs/knowledge-base/git/github/integration#with-github-app-recommended)

# Discussion History
## dan-is-not-the-man | 2024-08-24T22:33:25+00:00

looking options Issue https://github.com/monero-project/monero-docs/discussions/22

## nahuhh | 2025-06-29T20:45:16+00:00
Completed w/o github app by using [pr comment workflow](https://github.com/monero-project/monero-docs/blob/master/.github/workflows/comment_pr.yml)

# Action History
- Created by: dan-is-not-the-man | 2024-08-13T07:28:41+00:00
- Closed at: 2025-06-29T20:45:33+00:00
