---
title: Merge submit_multisig into submit_transfer?
source_url: https://github.com/monero-project/monero/issues/3133
author: emesik
assignees: []
labels:
- proposal
created_at: '2018-01-16T00:59:23+00:00'
updated_at: '2018-04-04T23:45:31+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I was wondering if we could have one command to submit all kinds of signed transactions, whether regular or multisig.

It would be even better to have `libwallet` API also have one entry point for such operations before next release, which would save us from backward compatibility issues.

Any reasons why we wouldn't want it?

+proposal

# Discussion History
## moneromooo-monero | 2018-01-16T10:29:24+00:00
It is possible of course. You just add the inputs and outputs of both to a merged call, then add code to determine what to do based on which outputs are present, and whether to error out when they both are.

## dEBRUYNE-1 | 2018-01-16T10:33:49+00:00
+proposal

## egonson | 2018-04-04T03:25:03+00:00
I am waiting for this feature :)

## emesik | 2018-04-04T23:45:31+00:00
Being the one who raised the issue, I feel responsible, but unfortunately I have too much personal stuff on my head right now to code it.

# Action History
- Created by: emesik | 2018-01-16T00:59:23+00:00
