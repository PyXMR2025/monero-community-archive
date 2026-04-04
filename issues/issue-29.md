---
title: 'Buildbot: upload step prevents other builds from starting'
source_url: https://github.com/monero-project/meta/issues/29
author: anonimal
assignees: []
labels: []
created_at: '2016-12-20T19:49:03+00:00'
updated_at: '2020-03-09T21:45:06+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:45:06+00:00'
---

# Original Description
Other builds wait in the queue during the upload step when (I'm assuming) resources are available for the next build. When the upload step is reached, is it possible to queue that [the step] instead of entire builds?

# Discussion History
# Action History
- Created by: anonimal | 2016-12-20T19:49:03+00:00
- Closed at: 2020-03-09T21:45:06+00:00
