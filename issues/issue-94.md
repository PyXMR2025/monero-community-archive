---
title: 'Build: add doxygen build step for Kovri'
source_url: https://github.com/monero-project/meta/issues/94
author: anonimal
assignees: []
labels:
- resolved
created_at: '2017-07-18T03:10:15+00:00'
updated_at: '2017-07-22T15:35:04+00:00'
type: issue
status: closed
closed_at: '2017-07-22T15:35:04+00:00'
---

# Original Description
So issues like https://github.com/monero-project/kovri/pull/677 are caught sooner and https://github.com/monero-project/kovri-site/issues/5 runs smoothly. The buildbot step would run our Doxygen build option with a simple `make doxygen`.

# Discussion History
## anonimal | 2017-07-18T03:11:55+00:00
Note: if resources are a concern, we could simply apply this step to the Linux x86-64 builder.

## danrmiller | 2017-07-18T18:25:10+00:00
Ready to go on the static nightly builds once https://github.com/monero-project/kovri/pull/677 is merged. I'll wait to PR the buildbot config until after @luigi1111 merges #93 

## anonimal | 2017-07-18T18:34:32+00:00
https://github.com/monero-project/kovri/pull/677 has been merged. Thank you so much @danrmiller.

>I'll wait to PR the buildbot config until after @luigi1111 merges #93

Just a git FYI if it helps, if you approve of #93, there's also the option of basing a topic branch off of my remote and then PR'ing your changes before @luigi1111 merges #93 (the PR would include my commits but that's ok since they will be merged anyway, assuming @luigi1111 approves).

## danrmiller | 2017-07-22T15:34:01+00:00
+resolved

# Action History
- Created by: anonimal | 2017-07-18T03:10:15+00:00
- Closed at: 2017-07-22T15:35:04+00:00
