---
title: Streamline pull request review process
source_url: https://github.com/monero-project/monero/issues/4421
author: leonklingele
assignees: []
labels: []
created_at: '2018-09-22T22:46:06+00:00'
updated_at: '2022-07-20T19:51:52+00:00'
type: issue
status: closed
closed_at: '2022-07-20T19:51:52+00:00'
---

# Original Description
A bunch of pull requests were merged by @fluffypony which did not receive a single mark of approval (except of fluffy's). This "review process" needs to be improved.
Monero is a community project and it is unacceptable to merge obviously broken changes such as this one: https://github.com/monero-project/monero/pull/4401/files#diff-04c6e90faac2675aa89e2176d2eec7d8R119

# Discussion History
## moneromooo-monero | 2018-09-22T22:55:02+00:00
Review it then ?

## leonklingele | 2018-09-22T23:14:52+00:00
The PR I've linked to was open for a mere 3 days. It wasn't critical to merge that early.
Why not add a bot which pings various GitHub accounts if a pull request didn't receive any reviews within 7 days or so. Something similar to [this](https://github.com/facebookarchive/mention-bot) maybe? I can help in creating a custom one too.

## sedited | 2018-09-22T23:21:33+00:00
Part of it is also a CI problem. Build Bot is red far too often. This makes it hard for developers to submit pr's that compile on all platforms, do not contain conflict markers (can be avoided with a simple linter) and do not break existing tests, but also for reviewers, because they need to go through half baked pr's . 

## plavirudar | 2018-09-23T01:17:15+00:00
What's wrong with the PR you linked? I don't see anything "obviously broken" with it. 

## sedited | 2018-09-23T08:29:26+00:00
@plavirudar conflict markers were left inside the commit for example. 

## moneromooo-monero | 2018-09-23T08:44:55+00:00
The reason it was merged early is that we need to release asap now. Otherwise PRs stay open for ~10 days at least. But even then, some PRs stay unreviewed for weeks. The people who review more than the occasional PR are myself, stoffu, and sometimes vtnerd. It will only become better if more people (with the skills to do do obviously) start reviewing. You don't even have to review everything, just PRs that didn't get reviewed yet. It adds up.

## Gingeropolous | 2018-09-24T03:47:38+00:00
@leonklingele , yes make the bot! just do it. don't ask permission, seek approval, confer with the spirits, throw the I ching... just do it. 

unofficial monero dev slogan, hacked from nike: just code it

## sedited | 2018-09-24T05:03:26+00:00
 I suggest that labels are added to the pull requests. I could then easily sort through them and look for changes to the build system for example. This is something maintainers would have to do though. 

## leonklingele | 2018-09-30T19:37:45+00:00
While examining various GitHub bots, I found the following which might be of interest:

1. https://github.com/probot/stale Auto-replies to Pull Requests after a period of inactivity
2. https://github.com/facebookarchive/mention-bot @-mentions potential reviewers (based on their previous contributions and reviews)
3. https://probot.github.io/apps/minimum-reviews/ Prevents merging of unreviewed Pull Requests

Who can set them up?

## selsta | 2022-07-20T19:51:52+00:00
Our CI setup is way better these days. I'm closing this as I don't think there will be much more discussion here. Personally I'm not a fan of bots that just add noise.

# Action History
- Created by: leonklingele | 2018-09-22T22:46:06+00:00
- Closed at: 2022-07-20T19:51:52+00:00
