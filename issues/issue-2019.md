---
title: Dockerhub image is badly outdated
source_url: https://github.com/xmrig/xmrig/issues/2019
author: h8llama
assignees: []
labels: []
created_at: '2021-01-02T18:12:18+00:00'
updated_at: '2021-04-12T14:25:18+00:00'
type: issue
status: closed
closed_at: '2021-04-12T14:25:18+00:00'
---

# Original Description
https://hub.docker.com/r/xmrig/xmrig exists but was last updated 3years ago

I've submitted a PR with a Dockerfile that will allow configuring auto building docker images whenever master is pushed (after it gets merged to master obv.): https://github.com/xmrig/xmrig/pull/2018

a demobuild  using Dockerfile in PR and current master (v6.7.0) is available at https://hub.docker.com/repository/docker/h8llama/xmrig

Alternatively the stale image should be removed from Dockerhub

# Discussion History
## xmrig | 2021-01-02T20:16:04+00:00
This Dockerhub image is not official and was created by someone else.
Thank you.


## h8llama | 2021-01-02T23:12:06+00:00
Ah, understood. unfortunate it was posted as xmrig/xmrig ....

Still think the Dockerfile in the pr would be a good add and only ongoing maintenance would be verifying the Alpine package dependencies but ¯\_(ツ)_/¯

# Action History
- Created by: h8llama | 2021-01-02T18:12:18+00:00
- Closed at: 2021-04-12T14:25:18+00:00
