---
title: 'Idea: introduce an opt-in fee for the FFS'
source_url: https://github.com/monero-project/monero-gui/issues/1564
author: ghost
assignees: []
labels: []
created_at: '2018-09-18T13:42:32+00:00'
updated_at: '2021-05-24T23:45:02+00:00'
type: issue
status: closed
closed_at: '2021-05-24T23:45:02+00:00'
---

# Original Description
FFS is the hot topic lately, so I started thinking about how we could evolve the process and the idea.

I've already created another discussion (#1560) to display the projects that are in the FFS directly in the GUI. But my idea today is to discuss something that was probably already talked about somewhere (but I found no log), which would be the introduction of a voluntary donation directly into the transactions of Monero via GUI.

An extra option in the advanced menu, where you can add a % of the transaction (or fees) to be sent to a dedicated wallet to fund FFS-approved projects. Such a wallet would be controlled by one or more core team members. This is different from the general development wallet as far as I know.

**How would it work?**

The user can choose between different tiers. Examples would range from 0.01% to 0.1% of the transaction value. Or maybe the value of the fee.

User A makes a transaction of 20 XMR, in which he will pay a ~0.003 XMR fee to the miners. The new donation transaction could be 0.01% of 20 XMR (0.002 XMR) or 1% of the rate (0.00003 XMR).

I have no idea how much money could be generated, even more because it's only opt-in. But I imagine a decent part of the core community (reddit) would participate.

Now, surely, this idea has problems and it would be necessary to evaluate them in a critical way, especially with respect to privacy. Transactions with an "extra fee", even if it is not a flat fee, opens up a certain vector for blockchain analysis in which you can accurately estimate which percentage of daily transactions are participating in the donation opt-in system. I can not say exactly how dangerous the result of this analysis can be. I am inclined to imagine that it would be probably harmless for the majority of users.

Still, it would be interesting to create such a system, and put a small introductory text explaining what this opt-in means, the benefits it can bring and also the risks.

I would go even further and place a second confirmation popup when the user performs a transaction with the GUI, saying that the Y value in XMR will be donated to the FFS wallet. The user will have the option to cancel the transaction and remove the donation temporarily.

Unlike the other proposal (#1560), this idea does not require any kind of communication with external websites. Everything can be done directly through the protocol.

# Discussion History
## selsta | 2021-05-24T23:45:02+00:00
XWallet had a similar fee idea and it was rejected due to privacy concerns and blockchain bloat.

https://www.reddit.com/r/Monero/comments/7rdtd5/you_shouldnt_use_xwallet_if_you_care_about_your/

We do have a donate button in Settings now.

# Action History
- Created by: ghost | 2018-09-18T13:42:32+00:00
- Closed at: 2021-05-24T23:45:02+00:00
