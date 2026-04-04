---
title: 'Buildbot: filter non-build related files from building in PR''s/merges'
source_url: https://github.com/monero-project/meta/issues/30
author: anonimal
assignees: []
labels: []
created_at: '2016-12-20T19:53:53+00:00'
updated_at: '2020-03-09T21:44:59+00:00'
type: issue
status: closed
closed_at: '2020-03-09T21:44:59+00:00'
---

# Original Description
Is this possible? If this is implemented, then https://github.com/monero-project/kovri/pull/513 shows otherwise.  I think the filter works for .md/.asc/.conf files though. Can anyone confirm?

# Discussion History
## danrmiller | 2016-12-20T19:55:20+00:00
Yes its possible, I just need to find some time to implement and test

## anonimal | 2017-01-01T14:34:26+00:00
Resolved in #11 

## anonimal | 2017-01-24T01:22:48+00:00
https://github.com/monero-project/kovri/pull/535 is building markdown-only changes.

## anonimal | 2017-01-30T02:40:37+00:00
Can we also add Dockerfile? https://github.com/monero-project/kovri/pull/541

## anonimal | 2017-02-08T18:16:22+00:00
https://github.com/monero-project/kovri/pull/547 only changes README.md but the build kicked in.

## anonimal | 2017-02-11T03:26:19+00:00
There are more files that we should add to the filter, such as `.clang-format` and `.dockerignore`. Once the filter is fixed, I can just PR the additions which shouldn't trigger a build.

## anonimal | 2017-09-01T03:55:35+00:00
😢 

## anonimal | 2018-03-01T05:00:14+00:00
https://github.com/monero-project/kovri/pull/819 shows that `.asc` files are not filtered. AFAICT, the build also still kicks in for `.md` and `.conf` and basically anything that's PR'd.

@danrmiller is there anything I can do to help resolve this issue?

# Action History
- Created by: anonimal | 2016-12-20T19:53:53+00:00
- Closed at: 2020-03-09T21:44:59+00:00
