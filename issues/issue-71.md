---
title: Usage of filter data structures over sets
source_url: https://github.com/Cuprate/cuprate/issues/71
author: hinto-janai
assignees: []
labels:
- C-discussion
- C-optimization
created_at: '2024-02-23T16:14:10+00:00'
updated_at: '2024-05-27T00:52:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What
Filter data structures are smaller & faster than traditional sets.

Cuprate could use these over traditional sets (`HashSet`, `BTreeSet`) in cases where all we need to know is:
- Does the set _not_ contain `x`?

Off the top of my head, key image & peerlist checks could benefit from this.

These could also be used for a filter layer above the database to avoid disk access.

Filter usage in other projects:
- https://github.com/search?q=repo%3Abitcoin%2Fbitcoin%20bloom&type=code
- https://github.com/search?q=repo%3Aparadigmxyz%2Freth+bloom&type=code
- https://github.com/search?q=repo%3AZcashFoundation%2Fzebra%20bloom&type=code

These are essentially optimizations (which also come with negative side-effects, e.g. removal of a set member is more complicated in filters), so it isn't necessary right now, although we should eventually get around to it.

## Filters
Some possible filters we could use. Starting from the most known with the longest history.

| Filter | Description |
|--------|-------------|
| Bloom  | https://en.wikipedia.org/wiki/Bloom_filter
| Cuckoo | https://en.wikipedia.org/wiki/Cuckoo_filter
| Xor    | https://arxiv.org/abs/1912.08258
| Ribbon | https://arxiv.org/abs/2103.02515

# Discussion History
## SyntheticBird45 | 2024-03-25T14:27:12+00:00
Saving this one for when the time comes: https://github.com/tomtomwombat/fastbloom/

# Action History
- Created by: hinto-janai | 2024-02-23T16:14:10+00:00
