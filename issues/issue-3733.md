---
title: If a tx spending an output is constructed (but not broadcast), selected decoys
  never change
source_url: https://github.com/monero-project/monero-gui/issues/3733
author: salamipusher
assignees: []
labels: []
created_at: '2021-11-13T20:56:10+00:00'
updated_at: '2025-05-06T19:28:15+00:00'
type: issue
status: closed
closed_at: '2025-05-06T19:28:15+00:00'
---

# Original Description
I reported this issue in the Monero dev channel, but it needs to be tracked properly here.

Steps to reproduce:
----
1. Construct a transaction spending some output(s). For example, try to sweep the outputs from an account. Click 'Send' but *do not* confirm the spend, ensuring the transaction is not broadcast.
2. Note the selected decoys for the outputs in the log.
3. Wait some time
4. Construct a new transaction spending the output(s) above. Try different amounts and different recipient addresses. Note that the selected decoys are identical to those in step 2.

Expected behavior:
----
New decoys will be selected.

Actual behavior:
----
The same decoys are selected. This leaks bits. Because decoy selection is highly time-dependent (recent outputs comprise the majority of the decoys selected), broadcasting a transaction with decoys selected more than hour or so in the past will look very unusual. Nobody else will be broadcasting transactions with so many decoys from that time period.


Discussion:
----
I understand that this might be somewhat-intentional behavior, as if a transaction has been broadcast but held back by a malicious peer, spending the same output(s) with new decoys will uniquely identify the real output.

The problem is that there seems to be no difference between "tx has left this machine: keep the same decoys" and "tx hasn't left this machine: select new decoys".

Finally, there may be some other bug here. When I load the wallet with `monero-cli` and `unset_ring` the key image(s) for the outputs, nothing happens, and I do not get any L2 log messages indicating the entry was actually removed from the shared ringdb. Yet when I launch `monero-gui` again, those same decoys are selected.

This actually opens the door to a workaround: spending those outputs with `monero-cli` chooses new decoys.

# Discussion History
## salamipusher | 2021-11-17T03:50:58+00:00
I have placed a 0.2XMR bounty on this issue: https://bounties.monero.social/posts/33/fix-monero-gui-decoy-selection-bug-monero-gui-issue-3733

## selsta | 2021-11-22T19:55:11+00:00
From IRC

```
19:53 <+selsta> moneromoooo: not sure how available you are, but is this expected behaviour with ringdb? https://github.com/monero-project/monero-gui/issues/3733
20:20 <moneromoooo> Yes.
20:21 <moneromoooo> That's the whole point of the ringdb.
20:21 <moneromoooo> Whether the tx is sent to the txpool or not is not relevant, unless I'm shown why it is.
20:22 <moneromoooo> If it were to select new fake outs if the tx was not sent to the txpool, it'd open a trivial attack if the dameon is not yours: fail once, but not twice. Then you know which outputs are the real ones.
20:22 <moneromoooo> The ringdb could be disabled with --trusted-daemon though.
20:23 <moneromoooo> Though I'm sure some poeple would add --trusted-daemon with untrusted dameons so...
```

Did you test behaviour with `--trusted-daemon`? You can also set it in GUI node settings.

## jeffro256 | 2023-03-22T23:35:30+00:00
Sorry, I know this is old, but I'm interested in what the OP was trying to achieve here since I suspect that this might be an instance of an XY problem. Why would one want to sign a transaction, store it, wait some time, and then regenerate it with different decoys?

## plowsof | 2024-02-03T22:13:14+00:00
would a PR implementing this ever be accepted? if not then close this issue and presumably refund @salamipusher s 0.2 xmr from his bounty after closing that also

## jeffro256 | 2025-05-06T14:12:41+00:00
@plowsof yes please close 

# Action History
- Created by: salamipusher | 2021-11-13T20:56:10+00:00
- Closed at: 2025-05-06T19:28:15+00:00
