---
title: Versioning scheme
source_url: https://github.com/Cuprate/cuprate/issues/53
author: SyntheticBird45
assignees: []
labels:
- C-discussion
created_at: '2024-02-07T15:58:14+00:00'
updated_at: '2024-05-27T00:56:08+00:00'
type: issue
status: closed
closed_at: '2024-02-09T14:01:21+00:00'
---

# Original Description
What is the versioning scheme of Cuprate ? I see three options:
- Semantic Versioning: MAJOR.MINOR.PATCH with first release of Cuprate being 1.0.0
- Semantic Versioning: MAJOR.MINOR.PATCH but following monerod versioning. So Cuprate first version will likely be 18.3.1
- 0ver versioning: 0.MINOR.PATCH. I don't see any reason to use this.

Pros of following monerod versioning:
- Same version means it is compatible by network consensus.
- Easier for people to understand the latest version
Cons of following monerod versioning:
- Doesn't make a lot of sense to come out with an Alpha software at version 18.
- How do we name our fixes release ? We shouldn't be limited by monerod number of updates. Maybe MAJOR.MINOR.PATCH-N (eg. 18.3.1-5)

# Discussion History
## Boog900 | 2024-02-07T22:02:38+00:00
For the `cuprated` binary I would be for the first option. However I think the crates that make up Cuprate should follow their own versioning. 

For what I think the rules should be for the Cuprate binary should be, I think the MAJOR field should indicate a hf, so when we become stable the major field should only be incremented on hf before that I think versioning should have less defined rule.

## SyntheticBird45 | 2024-02-07T22:12:55+00:00
So following what you proposed first version of cuprated will be 18.0.1. The scheme is : HARDFORK.UPDATE.PATCH. 
with UPDATE being an API change, and PATCH being fixes.

## Boog900 | 2024-02-09T14:04:22+00:00
No just that the major version will only be increased on hf so first version will still be 1 but will only go to 2 when/ if there is a hardfork.

# Action History
- Created by: SyntheticBird45 | 2024-02-07T15:58:14+00:00
- Closed at: 2024-02-09T14:01:21+00:00
