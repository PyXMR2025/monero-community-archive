---
title: PRs remaining unmerged in the main /Monero repo
source_url: https://github.com/monero-project/meta/issues/675
author: ghost
assignees: []
labels: []
created_at: '2022-03-16T14:36:47+00:00'
updated_at: '2022-07-20T14:57:41+00:00'
type: issue
status: closed
closed_at: '2022-07-20T14:57:41+00:00'
---

# Original Description
Monero is the most interesting, useful, and legitimate cryptocurrency in the world right now. I understand that repo merge privileges are massive to give away (partially responsible for splitting BTC) but IMHO constant merges are what gave the Monero project a ton of energy back in 2017-2018. To have slow unconsistent merges makes the project itself lose energy. 

There are (currently) 140 unmerged PRs in the queue of the main /Monero/ repo. I understand they need review, ~~but there are a lot that have passed review, and they still have not been merged~~. Is Luigi1111 too busy to maintain the main repo (which is totally fine)? If so we need to come together as a community and find or fund someone to do this important work. Does anyone have any ideas for who could take on this responsibility? 

Is anyone willing to volunteer? Naturally they will have to be vetted by main devs and/or core team. 

Edit: removed comment saying PRs have passed review. There are actually zero fully reviewed PRs waiting. So this is both a review and a maintainer problem.

# Discussion History
## reemuru | 2022-03-16T14:43:24+00:00
Is it possible to setup a workflow where there is a bucket of vetted approvers and when a threshold is reached (e.g. 3/5) for approvals it gets automatically merged?

## selsta | 2022-03-16T14:44:22+00:00
It's not a maintainer issue, it's a review issue.

We just had merges two weeks ago and we currently have some more PRs in the merge queue. The majority of open PRs simply miss a review, or are unmerged for other reasons.

> but there are a lot that have passed review

Would you mind linking them? It's possible that there were some that were overlooked.

## selsta | 2022-03-16T14:46:54+00:00
@reemuru Seeing that we have struggles with getting one review, having 3/5 will be even more complicated :D

But like I wrote in my previous comment, the merging isn't the problem, though an additional maintainer would still be helpful to reduce luigi's workload.

## ghost | 2022-03-16T14:56:10+00:00
@selsta You’re right about the review issue. But really the issue is both a reviewer and a maintainer problem. Back in the day Fluffypony would often review and then immediately merge simple PRs that were waiting without review. Concurrently he would not merge contentious or complicated PRs if he was the only reviewer. This is what a good maintainer would do. So what we need is a new maintainer who can take over from him in this way.

But maybe wise community-vetted devs like @vtnerd might be willing to review more PRs so that @luigi1111 can merge them without review. Either works. We just need these PRs reviewed and merged in whatever fashion.

## rottenwheel | 2022-03-16T15:06:51+00:00
May I suggest having a discussion about bringing @Snipa22 back? He took on lead maintainer role once for not too long. Unfortunately, he was demoted for some off-topic reasons. If he was chosen once, why shouldn't it be at the very least considered at this point in time?

## selsta | 2022-03-16T15:09:33+00:00
> Back in the day Fluffypony would often review and then immediately merge simple PRs that were waiting without review. 

The majority of these 140 open PRs are exactly open because they aren't simple PRs that can be quickly merged.

Reasons for a PR being open can be:

- Too fresh (normally we wait 10 days at least until a PR gets merged)
- Missing review
- No consensus if change should be done
- Reviewed, but waiting on a different PR to get merged first
- Questionable if PR is an overall improvement
- PR author stopped responding
- Waiting in merge queue
- Reviewed, needs to be put into merge queue (I would appreciate a ping if someone sees one)

vtnerd has been working on reviews for the larger PRs (multisig, BP+, ...) but they take up a lot of time so ideally we would need more skilled devs who are familiar with the monero code base to help get things reviewed more efficiently.

# Action History
- Created by: ghost | 2022-03-16T14:36:47+00:00
- Closed at: 2022-07-20T14:57:41+00:00
