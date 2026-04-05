---
title: nothing happening
source_url: https://github.com/seraphis-migration/monero/issues/116
author: brainchainz
assignees: []
labels: []
created_at: '2025-09-28T19:49:16+00:00'
updated_at: '2025-09-30T15:43:50+00:00'
type: issue
status: closed
closed_at: '2025-09-30T15:43:50+00:00'
---

# Original Description
when double clicking on stressnet 'monerod' I just get this:

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.

[Process completed]



# Discussion History
## nahuhh | 2025-09-28T19:59:34+00:00
Explain properly plz

- where did you get the binaries
- what os are you on
- exact steps you took to produce that output

## brainchainz | 2025-09-28T20:09:12+00:00
downloaded apple-sillicon, extracted, double clicked the monerod,
MacOS Sonoma 14.4.1

## j-berman | 2025-09-29T16:28:45+00:00
To run monerod, you have to open [terminal](https://support.apple.com/guide/terminal/get-started-pht23b129fed/2.14/mac/14.0), locate the monerod file in terminal, then run it via the command `./monerod --testnet`. If you're not familiar with the command line, the alpha stressnet might be a bit of a challenge to get going with. Can work on having a GUI you can download easily in future testing rounds.

## j-berman | 2025-09-30T15:43:50+00:00
Closing as I don't think this is an issue with the software

# Action History
- Created by: brainchainz | 2025-09-28T19:49:16+00:00
- Closed at: 2025-09-30T15:43:50+00:00
