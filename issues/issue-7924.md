---
title: Public Nodes Firewall rules
source_url: https://github.com/monero-project/monero/issues/7924
author: AAH20
assignees: []
labels: []
created_at: '2021-09-08T11:14:26+00:00'
updated_at: '2022-02-18T23:56:29+00:00'
type: issue
status: closed
closed_at: '2022-02-18T23:56:29+00:00'
---

# Original Description
The Monero.fail lists and the public_nodes command of the cli wallet , generates an ultimate attack surface for adversaries with a bunch of vulnerable machines with a lot of open ports from different ISPs ,how was the monero community handling this in the past years ? , and where is the roadmap ? , its very hard for open source communities to maintain a long term roadmap or plan unless they are backed with whales , i think that was the case when RandomX was Launched , finally why is the security policy section of the github is neglected even in the most active projects out there ?

# Discussion History
## cirocosta | 2021-09-08T12:07:56+00:00
> _finally why is the security policy section of the github is neglected even in the most active projects out there ?_

https://github.com/monero-project/meta/blob/master/VULNERABILITY_RESPONSE_PROCESS.md  (which, btw, is right there in the README of this repository)

yes, might be worth pointing to that entry from `.github/SECURITY.md`, although I'd say it makes more sense to do so from a `.github` repository so it applies to all of them (see [Creating a repository for default files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file#creating-a-repository-for-default-files))

## AAH20 | 2021-09-08T12:49:41+00:00
then @moneromooo and @luigi1111 are needed here , there are only few hackativity reports on hackerone and the ones less than 1 year ago aren't accessible , why #7830 isn't submitted to hackerone i think that is as critical issue as this one https://hackerone.com/reports/501585

## UkoeHB | 2021-09-13T20:05:33+00:00
> why #7830 isn't submitted to hackerone

1. The issue is publicly known already.
2. It takes a lot of work and expertise to make a PoC exploit.
3. A hackerone report isn't going to get it solved faster.

## erciccione | 2021-09-14T17:44:01+00:00
> why #7830 isn't submitted to hackerone i think that is as critical issue

We asked to the core team how to proceed. After looking into it they were ok with opening a public issue. See @UkoeHB's comment for the reasons.

## selsta | 2022-02-18T23:56:29+00:00
> how was the monero community handling this in the past years ?

This wasn't a problem in the last years. If someone has a vulnerable machine there isn't much we can do. `monerod` isn't a firewall. Closing this as the other questions were also answered.

# Action History
- Created by: AAH20 | 2021-09-08T11:14:26+00:00
- Closed at: 2022-02-18T23:56:29+00:00
