---
title: './monero-blockchain-stats binary fails on pruned node '
source_url: https://github.com/monero-project/monero/issues/6073
author: SomaticFanatic
assignees: []
labels: []
created_at: '2019-11-01T01:07:13+00:00'
updated_at: '2019-11-04T18:07:03+00:00'
type: issue
status: closed
closed_at: '2019-11-04T18:07:03+00:00'
---

# Original Description
I simply ran the `./monero-blockchain-stats --testnet` command and it errored out without finishing.

I have no idea what this command does. I'm just testing stuff for the 0.15 release.

https://pastebin.com/FFQHz9Jw

# Discussion History
## SomaticFanatic | 2019-11-01T01:08:53+00:00
Be aware, I ran `./monero-blockchain-prune --testnet` and `./monero-blockchain-prune-known-spent-data --testnet` beforehand

## SomaticFanatic | 2019-11-01T01:16:32+00:00
I unpruned my node and ran it again and it worked fine. Maybe we need an error message like we have for ./monero-blockchain-export "Sorry we can't do this you have a pruned node"

Also interesting: Why is the first entry into monero-blockchain-stats for testnet from 1970? :)

## moneromooo-monero | 2019-11-01T15:45:01+00:00
I don't even remember what it's supposed to do now.

## hyc | 2019-11-01T17:21:16+00:00
What was pasted is what it did - it spits out counters of blockchain stats to stdout, in CSV format.

> Why is the first entry into monero-blockchain-stats for testnet from 1970? :)

The genesis block has a timestamp of 0.

## moneromooo-monero | 2019-11-04T15:18:28+00:00
https://github.com/monero-project/monero/pull/6094 should fix it.


# Action History
- Created by: SomaticFanatic | 2019-11-01T01:07:13+00:00
- Closed at: 2019-11-04T18:07:03+00:00
