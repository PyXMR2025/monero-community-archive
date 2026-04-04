---
title: Support database pruning
source_url: https://github.com/monero-project/monero-gui/issues/2087
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-04-16T14:36:01+00:00'
updated_at: '2021-04-13T23:44:25+00:00'
type: issue
status: closed
closed_at: '2021-04-13T23:44:25+00:00'
---

# Original Description
Refer *existing* users (those with a non-pruned blockchain) to the `prune-blockchain` tool. Add some information inside the GUI on how to use this tool. New users would prune their blockchain by default, which means: add `--prune-blockchain` to the daemon startup flags.

To get pruned status a RPC call is required: `prune_blockchain` with `check` argument set to `true` will return a bool `pruned`.

# Discussion History
## SamsungGalaxyPlayer | 2019-04-16T21:36:22+00:00
I support automatically pruning the blockchain by default. It's the usability tradeoff that is appropriate for most people.

## dEBRUYNE-1 | 2019-04-17T06:15:05+00:00
Automatic pruning by default would only be enabled on `Simple mode (bootstrap mode)` as far as I know. 

## ITwrx | 2020-08-06T02:27:07+00:00
While i agree that most people would choose pruning, i don't prefer it were enabled by default. What i would like to see, is the option given during the setup "wizard", and it would be nice if one could get info about all available flags (in the gui where the daemon flag input is). The fact that i had to do a github issues search, after a failing web search, and not finding it in the pdf manual included with the download, is an aggravating user experience. Advanced mode shouldn't mean the info is not available in the GUI at all, IMO. It should be that it's just more low level stuff most people won't want to deal with, at least at first.

## erciccione | 2020-08-06T09:23:10+00:00
@ITwrx 

> What i would like to see, is the option given during the setup "wizard"

That sounds like a good option. We could make the user check "pruned" or "normal", maybe leaving "pruned" checked by default.

> would be nice if one could get info about all available flags

I guess the best way to do it would be to redirect to existing documentation with these info. I wouldn't put a long list of flags on that page.

> not finding it in the pdf manual included with the download

FWIW, there is an old open issue about adding that: https://github.com/monero-ecosystem/monero-GUI-guide/issues/149

## ITwrx | 2020-08-06T12:36:28+00:00
> I guess the best way to do it would be to redirect to existing documentation with these info. I wouldn't put a long list of flags on that page.

yes, i like tooltips and/or links


## selsta | 2021-04-13T23:44:25+00:00
Simple mode (bootstrap) now pruned automatically.

It is also possible to select pruning during wizard if a new chain is setup.

# Action History
- Created by: sanderfoobar | 2019-04-16T14:36:01+00:00
- Closed at: 2021-04-13T23:44:25+00:00
