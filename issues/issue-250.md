---
title: Seed nodes are down
source_url: https://github.com/monero-project/monero/issues/250
author: u38
assignees: []
labels: []
created_at: '2015-04-02T09:04:06+00:00'
updated_at: '2015-04-02T14:50:09+00:00'
type: issue
status: closed
closed_at: '2015-04-02T14:50:09+00:00'
---

# Original Description
Looks like all seed nodes aren't wokring. Can't synchronize from scratch.


# Discussion History
## fluffypony | 2015-04-02T09:43:27+00:00
Seed nodes aren't the problem - there's something else is head that is breaking startup, and it isn't related to the seed nodes (the blockchainDB branch syncs up, for eg.)


## u38 | 2015-04-02T09:45:30+00:00
Do you mean there are some bugs introduced into the code recently?


## fluffypony | 2015-04-02T09:47:08+00:00
Yes, if you're compiling against head. Per the README -

> As with many development projects, the repository on Github is considered to be the "staging" area for the latest changes. Before changes are merged into that branch on the main repository, they are tested by individual developers, committed to the "development" branch, and then subsequently tested by contributors who focus on thorough testing and code reviews. That having been said, the repository should be carefully considered before using it in a production environment, unless there is a patch in the repository for a particular show-stopping issue you are experiencing. It is generally a better idea to use a tagged release for stability.

The most recent tagged release is 0.8.8.6, which is here: https://github.com/monero-project/bitmonero/releases/tag/v0.8.8.6


## u38 | 2015-04-02T10:18:56+00:00
v0.8.8.6 works. With seed nodes taken from v0.8.8.6 master branch also works. Looks like seed nodes list in master contains only dead nodes.


## fluffypony | 2015-04-02T10:27:14+00:00
The hardcoded seed list isn't used unless DNS seed nodes fail, which doesn't seem to be the case.


# Action History
- Created by: u38 | 2015-04-02T09:04:06+00:00
- Closed at: 2015-04-02T14:50:09+00:00
