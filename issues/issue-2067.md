---
title: Better support for remote nodes
source_url: https://github.com/monero-project/monero/issues/2067
author: squilter
assignees: []
labels:
- proposal
created_at: '2017-06-02T15:24:02+00:00'
updated_at: '2018-01-08T16:51:53+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
As the blockchain becomes bigger, there will be more and more people who find it infeasible to run their own nodes. I'd be willing to put in some effort to try and improve support for remote nodes, and was hoping some people could give feedback on what features might be useful and how to implement them.

**Automatically Connect to a Remote Node**. Right now a person can check [here](https://moneroworld.com/#nodes) and choose a random node to connect to. It would be nice to have a flag built into the CLI and maybe also the GUI that will automatically choose a remote node and connect. Not sure how this would work.

**Connect to Multiple Remote Nodes**. Sending different queries (or maybe even overlapping queries) to different nodes might help improve privacy in certain scenarios. Not sure which scenarios those are.

# Discussion History
## dEBRUYNE-1 | 2018-01-08T12:37:42+00:00
+proposal

## SamsungGalaxyPlayer | 2018-01-08T16:49:34+00:00
Related to #2204.

## SamsungGalaxyPlayer | 2018-01-08T16:51:53+00:00
@squilter regarding the first point, this would have to be done with a mechanism similar to #2204. Specific remote nodes should not be included in the releases to avoid centralization.

Not sure how to address your second point. I don't know if this has been discussed anywhere in detail.

# Action History
- Created by: squilter | 2017-06-02T15:24:02+00:00
