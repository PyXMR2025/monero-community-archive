---
title: Regarding the two security vulnerabilities disclosed by the Monroe project
source_url: https://github.com/monero-project/monero/issues/6390
author: GongSuiLi
assignees: []
labels: []
created_at: '2020-03-15T02:40:38+00:00'
updated_at: '2020-05-16T18:47:10+00:00'
type: issue
status: closed
closed_at: '2020-05-16T18:47:10+00:00'
---

# Original Description
Regarding the two security vulnerabilities disclosed by the Monroe project:
1. https: //hackerone.com/reports/766963
The Monero node running on my server is v0.15.0.0. Do I have to upgrade to v0.15.0.5? I follow your discussion here: https://github.com/monero-project/monero/issues/6380, should be about this vulnerability. But I am not sure if it will affect our nodes. How do I know if I need to upgrade?
2. https: //hackerone.com/reports/803028
This vulnerability should be related to the GUI of Monero Wallet. If you don't use Monroe Wallet, you don't need to upgrade, right?

# Discussion History
## trasherdk | 2020-03-15T07:03:24+00:00
> How do I know if I need to upgrade?

If your running version is older than latest version, upgrade.

## dEBRUYNE-1 | 2020-03-15T09:49:08+00:00
1. To err on the side of caution, I'd advise to upgrade to v0.15.0.5 (the tag has already been set), as it contains the security fix.

2. Correct. 

## GongSuiLi | 2020-03-15T12:11:07+00:00
> 1. To err on the side of caution, I'd advise to upgrade to v0.15.0.5 (the tag has already been set), as it contains the security fix.

I have read your discussion on this issue. If it is a common Monero node, shall we need to force upgrade to v0.15.0.5? Including monero nodes and monero-cli? The upgrade process may take several days. Should our old monero nodes be discontinued during the entire upgrade period?

## moneromooo-monero | 2020-05-16T18:47:10+00:00
By now you might as well wait for 0.16, which should be in the next couple weeks.

Anyway, no bug here, so closing.

# Action History
- Created by: GongSuiLi | 2020-03-15T02:40:38+00:00
- Closed at: 2020-05-16T18:47:10+00:00
