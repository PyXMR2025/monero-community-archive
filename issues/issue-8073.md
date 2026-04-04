---
title: Add change output to wallet balance immediately
source_url: https://github.com/monero-project/monero/issues/8073
author: woodser
assignees: []
labels: []
created_at: '2021-11-20T16:33:22+00:00'
updated_at: '2022-03-18T21:28:31+00:00'
type: issue
status: closed
closed_at: '2022-03-18T21:28:31+00:00'
---

# Original Description
When a user spends XMR, their wallet spends outputs and creates a change output.

Currently, the wallet does not add the change output to the wallet's balance until confirmed.

As a result, the balance decreases by more than the amount spent, which is alarming to users.

This issue requests that the wallet adds the change output into its balance immediately so only the spend amount is deducted from the balance.

# Discussion History
## notmike-5 | 2021-12-16T21:31:56+00:00
@woodser but it wouldn't really be an accurate reflection of things would it? What if the transaction failed for some reason? Then there needs to be additional code to remove the amount that was incorrectly added to the balance. There are other reasons to prefer the way things are here, as well. A user should not be alarmed at the wallet working as intended. 

## woodser | 2021-12-17T00:46:55+00:00
@notmike-5  Currently the outgoing amount is deducted from the wallet balance immediately and re-added if the transaction fails. Unconfirmed payments are also credited to the balance immediately with this [PR](https://github.com/monero-project/monero/pull/6986) merged to master. This issue goes along the same line of thinking, requesting that the change output be treated equal to the other incoming and outgoing amounts. Otherwise, why treat it differently? Doing so creates an incorrect balance whether the transaction fails or not.

## woodser | 2021-12-17T00:56:34+00:00
Also, the user's balance reducing by more than they sent is an alarming part of the experience. Adding change at the same time as subtracting the withdraw fixes that.

## rottenwheel | 2022-01-22T12:29:50+00:00
@woodser So, is this merged and we're all good for it to be part of forthcoming v15 network upgrade, or?

See: https://github.com/monero-project/monero/pull/6986

## woodser | 2022-01-22T14:17:47+00:00
This issue doesn't have an associated PR to my knowledge.

#6986 is merged into master, but it's not part of the v0.17.3.x release yet. Perhaps I should open a PR to the release-v0.17 branch? (@selsta?)

## woodser | 2022-01-25T20:11:58+00:00
If I'm not mistaken, unconfirmed change is already credited to the balance immediately: https://github.com/woodser/monero/blob/67be0552e769a8322fc92afa5cbc187216f2b8f7/src/wallet/wallet2.cpp#L6045

I opened a PR to also credit unconfirmed transfers back to the same wallet immediately: https://github.com/monero-project/monero/pull/8158

When used with #6986, the unconfirmed balance should be correct with unconfirmed transfers and change.

## selsta | 2022-01-25T20:21:24+00:00
@woodser if you want something in the next release please also open it against release branch

# Action History
- Created by: woodser | 2021-11-20T16:33:22+00:00
- Closed at: 2022-03-18T21:28:31+00:00
