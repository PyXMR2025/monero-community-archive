---
title: Clarify Boost 1.54 dependency caveat in documentation
source_url: https://github.com/monero-project/monero/issues/906
author: anonimal
assignees: []
labels: []
created_at: '2016-07-12T19:39:07+00:00'
updated_at: '2016-09-14T22:00:59+00:00'
type: issue
status: closed
closed_at: '2016-09-14T22:00:37+00:00'
---

# Original Description
```
anonimal        Is the boost 1.54 caveat still applicable?
anonimal        I've built successfully with gcc 4.8.5 and 5.3.0 on ubuntu LTS with 1.54, and both nodes are syncing successfully.
anonimal        Does the error/issue come up later?
i2p-relay       {-fluffypony} anonimal: it's Windows-specific, I think
```

I'm writing up a Travi-CI yaml for bitmonero so a solid answer will help me build a more accurate recipe.


# Discussion History
## ghost | 2016-09-14T21:46:00+00:00
I think that according to #1015, we should now be using Boost 1.58


## anonimal | 2016-09-14T22:00:37+00:00
Resolved in #964 and #981 


# Action History
- Created by: anonimal | 2016-07-12T19:39:07+00:00
- Closed at: 2016-09-14T22:00:37+00:00
