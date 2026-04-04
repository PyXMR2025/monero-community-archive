---
title: Monero Multisig for HF
source_url: https://github.com/monero-project/monero/issues/8237
author: UkoeHB
assignees: []
labels: []
created_at: '2022-04-04T00:50:29+00:00'
updated_at: '2022-10-18T21:15:51+00:00'
type: issue
status: closed
closed_at: '2022-09-29T17:40:20+00:00'
---

# Original Description
There are currently several multisig PRs in the air. Ideally all of them would be merged before the upcoming [hard fork](https://github.com/monero-project/meta/issues/680).

### Mandatory PRs

| PR |  Author | (Review) / Approved / Merged | Status |
|----|---------|------------------------------|--------|
[Signature fixes #8149](https://github.com/monero-project/monero/pull/8149) | | | merged |
[Post-kex verification round #8220](https://github.com/monero-project/monero/pull/8220) | | | merged |
[Force-update option #8329](https://github.com/monero-project/monero/pull/8329) | | | merged |
[Mitigate fund burning #8432](https://github.com/monero-project/monero/pull/8432) | | | merged |

### Good-to-have PRs

| PR |  Author | (Review) / Approved / Merged | Status |
|----|---------|------------------------------|--------|
[Kex round boosting #8203](https://github.com/monero-project/monero/pull/8203) | @UkoeHB | none | Needs to rebase onto the force-update flag PR and get reviewed. |
| [Code quality #7852](https://github.com/monero-project/monero/pull/7852) | @UkoeHB | @rbrunner7  | Either review+merge or reject it.


# Discussion History
## arnuschky | 2022-04-04T08:59:13+00:00
Thanks for the summary @UkoeHB - I was a bit lost after the dev meeting. 

One question: You said above that the status of #8220 is "Needs a review of multisig kex changes." To what changes are you referring exactly? Are there additional, un-approved changes in the PR that you are referring to, or do you mean #8203?




## UkoeHB | 2022-04-04T12:56:13+00:00
@arnuschky #8220 adds a key exchange round, this is a change to the key exchange protocol that's in master. The reviews on that PR did not validate the kex changes.

# Action History
- Created by: UkoeHB | 2022-04-04T00:50:29+00:00
- Closed at: 2022-09-29T17:40:20+00:00
