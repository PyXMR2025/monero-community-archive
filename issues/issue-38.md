---
title: Monero blockchain visualization and analysis library
source_url: https://github.com/monero-project/research-lab/issues/38
author: b-g-goodell
assignees: []
labels: []
created_at: '2018-10-02T03:26:36+00:00'
updated_at: '2018-10-02T03:28:07+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
There are at least two ways to visualize the transactions on the Monero blockchain: (1) as a forest of trees whose vertices are transaction output keys ("notes") and whose edges are defined by ring membership (allowing us to ask questions about vertex-induced subtrees with some given root) or (2) as a bipartite graph where in the first nodeset we see ring (signatures) and in the second nodeset we see transaction notes, and whose edgeset is defined by ring membership.

It would be nice to have some sort of library that visualizes these graphs and provides some analysis of statistics for these graphs. For example, for (1) above, what is the mean and median depth of the trees in the forest? What about the mean and median total number of transaction notes in the sub-trees? Etc. 

# Discussion History
# Action History
- Created by: b-g-goodell | 2018-10-02T03:26:36+00:00
