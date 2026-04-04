---
title: 'Feature request: Delayed transfers'
source_url: https://github.com/monero-project/monero/issues/9019
author: phytohydra
assignees: []
labels:
- feature
- low priority
- proposal
created_at: '2023-10-14T20:27:25+00:00'
updated_at: '2023-12-07T20:19:27+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
For when a transfer is not time-critical, it would be nice to have an easy way to submit it to the network at a random time within a specified time period.

It would help avoid leaking information about the timezone or activity cycle of the creator of a set of outputs, and help avoid probabilistic linking of outputs by their being created near to each other (ie, you had the wallet open and performed several transactions) or by their having been created near in time to each other on different days.

It could be added to the transfer and sweep commands as a `[delay=<interval>]` argument.  e.g. `transfer delay=1d <address> <amount>` would schedule it to be sent at a random time within the next 24 hours.

The wallet would resolve that into a specific time and let you know when it was scheduled to be sent, then tack that scheduled time onto the transfer.  Your trusted monero daemon would hold the transfer, and not broadcast it until the scheduled time.

I am thinking specifically of defeating Eve-Alice-Eve attacks.  You have some outputs which are KYCed to you or otherwise linked to one of your identities, and you want to break that link as efficiently as possible.  For a chain of several sweep_single transfers to be maximally effective, they should not occur around the same time each day, or in the same 8 hour window each day.

# Discussion History
# Action History
- Created by: phytohydra | 2023-10-14T20:27:25+00:00
