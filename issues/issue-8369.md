---
title: Mining error on testnet
source_url: https://github.com/monero-project/monero/issues/8369
author: ghost
assignees: []
labels: []
created_at: '2022-05-31T21:02:44+00:00'
updated_at: '2022-07-20T00:42:58+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
`start_mining 9wog1AwLTJRKCMgs7ZbCZGVJa26eve3ZU4hpxTBYxpp8LGUMiioB1shjS5aibER2AvY8bpDRiNRw929FMpxmeeuy9vQnRH6 1
2022-05-31 21:01:23.717 D Read command: start_mining 9wog1AwLTJRKCMgs7ZbCZGVJa26eve3ZU4hpxTBYxpp8LGUMiioB1shjS5aibER2AvY8bpDRiNRw929FMpxmeeuy9vQnRH6 1
2022-05-31 21:01:23.717 I Wrong address prefix: 53, expected 18 or 19 or 42
Mining to a testnet address, make sure this is intentional!`

Says wrong address prefix, even though everything is correct. I launched the daemon with --testnet and am mining to a testnet address.

# Discussion History
## selsta | 2022-05-31T22:53:09+00:00
Does it start mining even though it displays this `Wrong address prefix` message?

I tried 

```
start_mining 9wog1AwLTJRKCMgs7ZbCZGVJa26eve3ZU4hpxTBYxpp8LGUMiioB1shjS5aibER2AvY8bpDRiNRw929FMpxmeeuy9vQnRH6 1
```

and it worked as expected. Where do you see this warning message? Did you increase log level?

## ghost | 2022-06-01T01:33:03+00:00
Yes this is with log level 2. Error message is in the daemon log. And yes it mines correctly. But the error message is still strange. 

## Cactii1 | 2022-07-20T00:33:41+00:00
It does say, "make sure this is intentional!" which should give you the indication that it's going to mine to that address anyways.

## selsta | 2022-07-20T00:39:15+00:00
I debugged the issue and it's a harmless side effect of how the code is implemented. Not sure if it's worth fixing.

## Cactii1 | 2022-07-20T00:42:46+00:00
It's testnet, it should be allowed. If it was stagenet or mainnet I'd say there's a need for concern - but on testnet no.

# Action History
- Created by: ghost | 2022-05-31T21:02:44+00:00
