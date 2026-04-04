---
title: Algorithmically determine max sizes of white and grey peer lists?
source_url: https://github.com/monero-project/monero/issues/1815
author: ghost
assignees: []
labels: []
created_at: '2017-02-27T10:20:41+00:00'
updated_at: '2025-12-19T15:30:07+00:00'
type: issue
status: closed
closed_at: '2025-12-19T15:30:07+00:00'
---

# Original Description
@IPGlider Could we use a biological 'capture-tag-release-recapture' methodology to sample the max population size of each peer group and thus algorithmically determine the max size of the grey and white peer lists, rather than having them hard-coded?

We could still rely on the existing values as soft or minimum limits.

# Discussion History
## IPGlider | 2017-02-28T19:27:45+00:00
Quite interesting concept, it could be applied but would need to be studied to know if the added complexity is worth it.

New components:
- One temporal connection that does not count towards total out connections.
- Two new data structures that store peers.

Algorithm:
1. Connect to X random nodes and get their peer list, add those to structure A.
2. After a span of Y hours connect to X random nodes and get their peer list, add those to structure B.
3. Apply the formula to get the total population.
4. Empty A.
5. Swap A and B.
6. Resize gray and white lists.
7. Go to 2.

Then the gray list could be resized taking the population into account and white list resized to keep it at 1/5 of the gray to keep the actual ratio.

## ghost | 2017-02-28T21:10:11+00:00
Would certainly be an interesting thing to simulate/study.

Now...the problem is that we want to avoid fingerprinting nodes, so putting in the work to implement this now may just become entirely useless in a future where all nodes are invisible behind TOR/I2P and any node IDs have been obfuscated.

Which raises another point - how do we make sure we don't just have a node list full of duplicates under such circumstances. Hmm...are these two mutually exclusive - non-fingerprintable nodes, yet provably unique occurrences on a peer list?

## iamsmooth | 2017-03-05T17:32:56+00:00
> any node IDs have been obfuscated

There don't really need to be node IDs at all. That mechanism is kind of stupid.

As far as capture-tag-release-recapture, I wonder about whether that is resistant to attack.The problem space is different from nature where (one assumes) no one is trying to fool you about the population.


## selsta | 2025-12-19T15:30:00+00:00
Closing this, if someone is interested in the idea and wants to study it, please open an issue in the research-lab repo.

# Action History
- Created by: ghost | 2017-02-27T10:20:41+00:00
- Closed at: 2025-12-19T15:30:07+00:00
