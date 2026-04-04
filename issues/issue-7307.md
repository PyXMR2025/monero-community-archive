---
title: --restore-height CLI option not honored by monero-wallet-cli
source_url: https://github.com/monero-project/monero/issues/7307
author: robby-d
assignees: []
labels: []
created_at: '2021-01-11T22:56:32+00:00'
updated_at: '2021-02-16T16:42:38+00:00'
type: issue
status: closed
closed_at: '2021-02-16T16:42:38+00:00'
---

# Original Description
had issues getting `--restore-height` to be honored with monero-wallet-cli. I tried a command like `./monero-wallet-cli --generate-from-device myledger --restore-height 0` and the wallet still prompts with "No restore height is specified." -- this is newest release, on OS X Big Sur.

@moneromooo-monero responded on IRC that it looked like a bug and posted this (potential) fix: https://paste.debian.net/hidden/938e4dd5/

I will attempt to test this later once I can get the time to recompile the source. Posting this here for documentation of the issue.

# Discussion History
## selsta | 2021-01-12T11:52:26+00:00
I noticed this bug too.

@robby-dermody please open a PR if your patch passes testing.

## hyc | 2021-01-12T11:58:05+00:00
I'd say restore-height=0 is meaningless since nobody owns any txns in block 0. Just use restore-height=1 instead.

## selsta | 2021-01-12T12:00:58+00:00
If the patch is small I don’t see why we shouldn’t change this. Specifying --restore-height 0 and then getting the "no restore height specified" is not good user experience, even if technically correct.

## robby-d | 2021-01-12T23:05:01+00:00
Agreed with @selsta as it removes the requirement of additional domain specific knowledge from the user. Also, the monero-wallet-cli command line help states: `--restore-height arg (=0)             Restore from specific blockchain height`, which made me think that specifying 0 was both the default and perfectly acceptable.

My opinion is that, if specifying 0 doesn't work or shouldn't be allowed/valid to start scanning at the first block, then the default in help should be changed to `=1` and one should get an error message if 0 is specified.

## robby-d | 2021-01-12T23:11:34+00:00
@selsta I would open a PR, but it seems the Debian paste snippet expired, and I have no familiarity with the Monero codebase. Perhaps you or @moneromooo-monero could PR a fix that takes the feedback above on better user feedback if 0 is specified in mind? Sorry about that.

# Action History
- Created by: robby-d | 2021-01-11T22:56:32+00:00
- Closed at: 2021-02-16T16:42:38+00:00
