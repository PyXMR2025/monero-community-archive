---
title: Enforcing commit message conventions for post-github apocalyptic era
source_url: https://github.com/Cuprate/cuprate/issues/621
author: SyntheticBird45
assignees: []
labels:
- C-proposal
created_at: '2026-05-28T11:28:18+00:00'
updated_at: '2026-05-28T21:32:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What

I come to realize recently that most of the explanations about commits are in the commit title and PR description. while PR can be cloned and backup on alternative platform, I believe the git repository should be sufficient to have all the information needed about the intent of a commit. Some IDE do integrate commit <-> PR relation but that require privacy invasive calls to Github.

I made a comment on https://github.com/Cuprate/cuprate/pull/618 because NO_COLOR was added as an environment variable but not listed in the PR description nor is it described in the commit message.
Most of our big PRs are actually squashed branch with concat titles from all the smaller commits.

Take a look at:

https://github.com/Cuprate/cuprate/commit/467a168677a5725b2f7133a396b643320095cc26
https://github.com/Cuprate/cuprate/commit/c5976055cfb7ef0e21b12955cb7f7eaa58031e29

## Where

I'm proposing that merged commits (obviously squashed so we just talk about a single commit) have this format:
```
TITLE

<General description that we often write in the PR description>
<Short reasoning and why>
<Changelog as compact as possible>
Optional: <List of squashed commits titles if found relevant>
```

Yes that make commit messages much longer but that is not idiosyncratic behavior when you consider that this is standard in mailing list based development (notably LKML comes to my mind).


# Discussion History
## redsh4de | 2026-05-28T21:32:43+00:00
+1 would be a big plus for platform-agnostic/offline auditability

I reckon would also come in handy if ever a codebase migration need be to a different platform, all the informational data would be available in the commit itself instead of scattered across Github specific metadata buckets

# Action History
- Created by: SyntheticBird45 | 2026-05-28T11:28:18+00:00
