---
title: Dockerfile fails to build in 0.12.2.0
source_url: https://github.com/monero-project/monero/issues/3988
author: tannerdsilva
assignees: []
labels: []
created_at: '2018-06-11T19:14:35+00:00'
updated_at: '2018-06-12T18:02:10+00:00'
type: issue
status: closed
closed_at: '2018-06-12T18:02:10+00:00'
---

# Original Description
It appears as though the variable `MONERO_HASH` is incorrect in Dockerfile 0.12.2.0, resulting in a container that will not build.

When I download the 0.12.2.0 source and run `docker build`, step 28 exits `1` as a result of the following comparison

``test `git rev-parse HEAD` = ${MONERO_HASH} || exit 1``
``test e2c39f6b59fcf5c623c814dfefc518ab0b7eca32 = c29890c2c03f7f24aa4970b3ebbfe2dbb95b24eb``

When I change MONERO_HASH to reflect the hash returned from `git rev-parse HEAD`, the container successfully builds. I posted about this issue on the [monero subreddit](https://www.reddit.com/r/Monero/comments/8qahgc/is_it_just_me_or_is_the_01220_dockerfile_broken/), and at the time of writing, didn't have any evidence from users that the 0.12.2.0 container has been successfully built from source. 

# Discussion History
## tannerdsilva | 2018-06-11T19:17:49+00:00
I realize that the very act of releasing a fix for this bug will fix the problem, as a new HEAD hash would be generated. Just wanted to point out the problem, for whatever its worth.

## homdx | 2018-06-11T21:27:36+00:00
My commit is can help and run Docker?
https://github.com/monero-project/monero/pull/3879

# Action History
- Created by: tannerdsilva | 2018-06-11T19:14:35+00:00
- Closed at: 2018-06-12T18:02:10+00:00
