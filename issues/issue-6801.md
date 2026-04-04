---
title: '[Feature Request] Allow automatic churning of incoming transactions to "flagged"
  subaddresses'
source_url: https://github.com/monero-project/monero/issues/6801
author: sethforprivacy
assignees: []
labels: []
created_at: '2020-09-05T19:44:31+00:00'
updated_at: '2020-09-06T23:38:52+00:00'
type: issue
status: closed
closed_at: '2020-09-06T23:38:52+00:00'
---

# Original Description
This is a formalization of the idea I have been mentioning over the last several days, and comes out of research being put forth by knaccc on IRC around the efficacy of churning to avoid merge analysis, EABE, and poisoned output analysis.

The goal of this proposal is to seek feedback on creating the tools in both CLI and GUI wallets to make churning of incoming transactions to "flagged" subaddresses to be automatically churned using some (TBD) timing to mimic normal user spend behavior and aid in normalizing decoy selections for churn transactions.

# Proposed UX:

Whenever a user creates a new subaddress, in either the GUI or CLI wallet, they will be prompted with the following (or similar, open to feedback on phrasing!):

`Will this subaddress in any way be linked to your real-world ID? (eg. exchange withdrawals, tip addresses, etc) [Yes|No]`

If the user answers "Yes", that subaddress is flagged for automatic churning whenever transactions are received to it. These outputs are not made available to spend until a given amount of churns (early research indicates 3+) are completed, although a hidden/advanced option to allow spending could be exposed, but difficult to access.

If the user answers "No", that subaddess is handled as all are today, and no churning is done by default.

I also would propose allowing users to right click (or have a unique button) to allow previously created subaddresses to be flagged for automatic churning, or a CLI command for the `monero-wallet-cli` users.

# Goals of the proposal:

- Improve users privacy against targeted attacks where their address is known and linked to their ID in any way (EABE, KYC exchange withdrawals, poisoned outputs, merge analysis)
- Avoid unnecessary chain bloat by not forcing all inputs to be churned, but only those being received to a subaddress linked to the users ID in any way
- Allow automatic churns that enable transactions to mimic normal user behavior, timing, and decoy selection, instead of relying on `sweep_single`

# Current gaps:

- Ideal churn counts are still being researched
- Ideal churn timing is still being researched

# Current potential issues:

- The user's wallet would have to remain open and "hot" in order to churn multiple times, as each transaction cannot be signed until the last is broadcast and confirmed
- Hardware wallets would be incredibly tricky to churn with, as users would have to unlock and sign each transaction over a multi-hour period

# Discussion History
## sethforprivacy | 2020-09-05T19:52:15+00:00
Some old (but related) feedback on churning in general can be found in:

#4305 

## jtgrassie | 2020-09-05T22:52:27+00:00
Given the answer to:

>Will this subaddress in any way be linked to your real-world ID? (eg. exchange withdrawals, tip addresses, etc) [Yes|No]

would almost always be "Yes", it seems redundant and thus a UX mistake IMO.

I'd always imagined that once there was some research on how best to handle any automatic single output churns, it would either become a default enabled setting or a global setting. From a UX perspective, they should not have to think about this stuff and we should just enable sane defaults.

Side note: we should probably remove `sweep_all` functionality (or at least warn if it's attempted), because one thing we do already know is that this kind of churn, in almost all cases, actually weakens privacy. Unfortunately there was a period where there were *some* vocal people recommending "churning" and so even of recent, this results in some users unwittingly making common mistake (which harms their privacy).

Until there is research / agreement on *how* we can do automatic sweep single churning, any discussion on how it may be presented to users seems premature.


## sethforprivacy | 2020-09-06T16:24:51+00:00
My main purpose for putting forward this issue is that if we enable churning for all transactions, we essentially triple (as current research is pointing towards 3+ churns being most effective) the burden every transaction places on the network, so any kind of default that doesn't discriminate based on source of funds in some way would put undue stress on the network.

The goal here is to see if we can find some way to avoid at least _some_ of that burden, while still enabling an easy (for the user) defense to common attacks from adversarial sources.

Maybe a better wording for the prompt (as a prompt is required in some way unless we do this for all transactions) would be `Will this address be exposed to potential attackers (KYC exchanges, government agencies, etc) with access to other data about you?` or something similar?

> Side note: we should probably remove sweep_all functionality (or at least warn if it's attempted), because one thing we do already know is that this kind of churn, in almost all cases, actually weakens privacy. 

Fully agree here, would love this to _at least_ be hidden from users or give some sort of bold and clear warning before being used, as this is almost never necessary, and can easily be harmful to the user.

> Until there is research / agreement on how we can do automatic sweep single churning, any discussion on how it may be presented to users seems premature.

I agree that we need a clearer idea of how the actual churning process should work, but if we implement it as a manual step we will never see it used properly by most people, and if we do it by-default for all transactions, we'd put a massive burden on the network. I wanted to get this idea down on paper so it could be thought about and discussed in tandem with the current churning research, rather than only be thought about after that, as the UX implementation is somewhat independent of the actual churning method.

## knaccc | 2020-09-06T22:09:59+00:00
I agree with @jtgrassie, I think it's premature to comment on churn implementation details prior to first detailing the nature and extent of specific threats we wish to address (outputs-spent-directly-together heuristics, iterated-EABE, etc). After we have been specific enough about the problem, and after we've come to strong conclusions about the best way to address the problem, only then would it make sense to figure out the UX of any proposed solution.

## sethforprivacy | 2020-09-06T23:38:48+00:00
Ok, thanks for the quick comments! 

I'll just close this out for now then, and we can circle back at a later date once we have a more clear picture of the churning landscape.

# Action History
- Created by: sethforprivacy | 2020-09-05T19:44:31+00:00
- Closed at: 2020-09-06T23:38:52+00:00
