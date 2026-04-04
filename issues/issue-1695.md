---
title: Inconsistencies between wallet-cli and wallet-rpc
source_url: https://github.com/monero-project/monero/issues/1695
author: amiuhle
assignees: []
labels: []
created_at: '2017-02-07T21:34:17+00:00'
updated_at: '2017-08-07T15:46:50+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I just looked into `monero-wallet-rpc` and discovered several inconsitencies to `monero-wallet-cli`.

For example, cli has `show_transfers` which can be used to get unconfirmed incoming transactions. In rpc, there's `get_transfers` which seems to do a different thing. There's no `show_transfers` in cli, and there's no `get_transfers` in rpc...  
Also, documentation about rpc is outdated

I think it would be desirable to have 1:1 consistency between naming of methods and params in cli and rpc.

I'd create a couple of PRs to fix this if you agree. Would the current rpc calls have to be deprecated first, or is monero still alpha / beta enough to just do this in the next version?

# Discussion History
## vtnerd | 2017-02-07T21:52:47+00:00
As mentioned in IRC, it should be possible to get incoming mempool transfers. `get_transfers` with the `pool` option set to true should do it. Please test against that.

## vtnerd | 2017-02-07T21:55:06+00:00
And my suggestion would be for not changing the name of existing RPC calls. Its tough to tell how many people this would impact.

## vtnerd | 2017-02-07T21:58:52+00:00
Changing the names of the cli options _might_ be more agreeable, but I don't if someone is attempting to strange things with piping commands into `stdin` or something. Some feedback from more in the community would help here.

## amiuhle | 2017-02-07T22:16:15+00:00
I think the main question is: Do we want consistency between CLI and RPC?

Personally, I do. During development, it'll help a lot to just do the same thing manually and in code. Also, there would basically only be one API to document.

If the consensus is YES, then sooner is way better than later. I also think that RPC should be adjusted because I'm guessing way more people are using CLI.

Best way to do it IMO is to migrate all methods in RPC to the CLI method signatures, aliasing the deprecated ones and logging a big, fat, red message in the logs. Leave both new and deprecated messages in RPC and then remove the deprecated stuff in the January 18 HF.

Shouldn't be a big problem if it's done now. There will be 6 months of deprecation warnings, and almost everyone is probably following GitHub issues or r/Monero anyways, so they will know.

Like I said, better now than tomorrow. This won't get any easier.

## moneromooo-monero | 2017-02-08T17:16:42+00:00
With this particular case, it's because simplewallet gets the transfer from RPC., then displays them. It doesn't attempt to exactly mimic the workings of the RPC (though in in this case it's pretty close). Some other wallet commands use more than one RPC too. Some use only part of what another RPC returns. While there might be things that could be named better, I don't think this is one of them.

# Action History
- Created by: amiuhle | 2017-02-07T21:34:17+00:00
