---
title: Refresh from Height Issue
source_url: https://github.com/monero-project/monero/issues/105
author: fluffypony
assignees: []
labels: []
created_at: '2014-08-26T17:09:11+00:00'
updated_at: '2015-11-24T14:41:47+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:41:47+00:00'
---

# Original Description
@jakoblind - not sure if you played with this much, but just tested it on a newly restored wallet that has 1 XMR in it, and it gets stuck in an infinite loop:)

We're currently on block 190558, and this tx is in 190551 -

```
[wallet ----]: refresh 190500
Height 190551, transaction <4084a075e06899d34e271bbf00c509143b448fd5ebf576f7d3a11a45a06bccc3>, received 1.000000000000
Height 190551, transaction <4084a075e06899d34e271bbf00c509143b448fd5ebf576f7d3a11a45a06bccc3>, received 1.000000000000
```

and so on until you ctrl-c:

```
Height 190551, transaction <4084a075e06899d34e271bbf00c509143b448fd5ebf576f7d3a11a45a06bccc3>, received 1.000000000000
Refresh done, blocks received: 13224
balance: 232.000000000000, unlocked balance: 0.000000000000
```

That balance is supposed to be 1:)


# Discussion History
## fluffypony | 2015-11-24T14:41:47+00:00
Feature shelved for the moment


# Action History
- Created by: fluffypony | 2014-08-26T17:09:11+00:00
- Closed at: 2015-11-24T14:41:47+00:00
