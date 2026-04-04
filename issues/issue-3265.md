---
title: '[Fork Attack Mitigation] add sweep_all_fork that accepts two destination addresses'
source_url: https://github.com/monero-project/monero/issues/3265
author: nasaWelder
assignees: []
labels: []
created_at: '2018-02-14T15:56:35+00:00'
updated_at: '2022-04-08T14:47:25+00:00'
type: issue
status: closed
closed_at: '2022-04-08T14:47:25+00:00'
---

# Original Description
The following idea assumes that the same ring members would be able to be used for both transactions, and that the fork cli would accept the signed tx as is. If not, I'll delete this issue.  

    sweep_all_fork <fee> <ringsize> moneroaddress forkaddress

The monero cli would submit the monero tx instantly, and save the fork transaction to file as signed_monerofork_tx.
The user could then use fork CLI to submit_transfer (after renaming it to whatever it needs to be).

Heavy use of explicit confirmation dialogs is suggested.

This is a "give them clean needles" approach.

# Discussion History
## moneromooo-monero | 2018-03-02T18:29:13+00:00
https://github.com/monero-project/monero/pull/3322 uses a ring database instead, so one may reuse tings. This more generic and is automatic (assuming the attackers merge this, which they might not if their goal is attacking, but then you can manually use set_ring in monero-wallet-cli once you spent on the fork).

## nasaWelder | 2018-03-02T18:37:27+00:00
I figure "we" wouldn't need to rely on attackers forking this feature because monero cli would be making the transaction for submission to fork network. I guess they could find a way to prevent that. I yeild, and I'll close.

## moneromooo-monero | 2018-03-02T18:50:48+00:00
If they actively try to prevent this, our fallback method is: spend in the fork, use set_ring in monero's monero-wallet-cli to record the ring that got used, spend in monero.

## moneromooo-monero | 2018-03-07T14:07:17+00:00
I kinda like this approach though because it also uses the same inputs for both txes. It would need knowing their address format, and is ultimately not scalable, so both pros and cons.

## selsta | 2022-04-08T14:47:25+00:00
Closing, as this issue is kinda irrelevant now. If it becomes relevant again we will have to search for new mitigations. Using the forkaddress doesn't seem scalable, as moneromooo wrote.

# Action History
- Created by: nasaWelder | 2018-02-14T15:56:35+00:00
- Closed at: 2022-04-08T14:47:25+00:00
