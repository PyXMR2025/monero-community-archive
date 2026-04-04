---
title: Multidistributed input selection for large ring sizes
source_url: https://github.com/monero-project/monero/issues/3112
author: DistinctiveMultiple
assignees: []
labels:
- proposal
created_at: '2018-01-13T23:51:12+00:00'
updated_at: '2018-01-25T21:00:57+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Increases in ring size and the introduction of a fixed ring sized are already discussed in various places (e.g. #3069). If we get RTRS RingCT higher ring sizes become viable, although they will likely still be limited (I remember reading a "likely below 100"). Once we have the ability to reasonably standardize on the use of ring sizes between e.g. 16-80, it should become possible to use a multidistributed input selection process which would solves issues such as "the use of very recent transactions sticks out" as well as "the use of very old transactions sticks out". In this post, I would like to propose such a process.

A multidistributed input selection scheme could look like this. For a ring size of n:

1. Pick n/4 inputs from the blocks 10-25 at the top of the chain, i.e. the newest blocks that that could contain freshly unlocked balances.
2. Pick n/4 inputs biased towards recent inputs, similar to the current input selection.
3. Pick n/4 inputs biased towards old inputs, with older ones being more likely.
4. Pick n/4 inputs uniformly across all possible choices.
5. From all the chosen inputs, replace the input that is closest to the real one with the real input.

Finding one single distribution that covers all common and less common use cases to a reasonable degree seems difficult. This approach should cover all types of transactions reasonably well.

# Discussion History
## dEBRUYNE-1 | 2018-01-15T16:49:51+00:00
+proposal

## SamsungGalaxyPlayer | 2018-01-25T21:00:44+00:00
@DistinctiveMultiple there would have to be sufficient, quantifiable evidence that this method works well against different attacks. The ringsize and the selection algorithm are topics of continued discussion.

# Action History
- Created by: DistinctiveMultiple | 2018-01-13T23:51:12+00:00
