---
title: '''Wagner attack'' in Monero multisig'
source_url: https://github.com/monero-project/monero/issues/7830
author: erciccione
assignees: []
labels: []
created_at: '2021-08-04T15:33:13+00:00'
updated_at: '2022-11-24T22:39:25+00:00'
type: issue
status: closed
closed_at: '2022-11-24T22:39:25+00:00'
---

# Original Description
Monero's multisignature implementation is vulnerable to a Wagner attack: if multiple signatures are constructed for a given address, and the wagner attack is executed, then the attacker can learn the private key shares of other participants.

We (Haveno) had talks with @luigi1111, @SarangNoether, @moneromooo-monero and @UkoeHB about it. Looks like the change needed to fix the vulnerability would be quite invasive so a deeper look into the problem is needed.

@SarangNoether suggests to implement [MRL-0009](https://www.getmonero.org/resources/research-lab/pubs/MRL-0009.pdf). @moneromooo-monero gave his availability for the coding part if somebody provide him with python code to refactor into C++. We need a cryptographer willing to look into the issue and provide mooo with the info he needs.

Haveno is happy to provide resources to fix the vulnerability and we already opened an issue to keep track of progresses: https://github.com/haveno-dex/haveno/issues/103. As you can see, the issue has a bounty, but we could provide more resources if necessary.

# Discussion History
## AAH20 | 2021-08-27T21:07:46+00:00
Still no one solved it ?
Here is the solution :

Digital Envelopes , signatures implementation along with MRL-009 , check the internet engineering task force latest rfc9101 to have a sufficient knowledge of how a secure communication channel should be specially in form of secure implementation of apis.

## UkoeHB | 2021-08-27T21:12:18+00:00
@AAH20 We already have a solution (MRL-0009), it just requires someone to implement it.

Transmitting data between multisig participants securely is out-of-scope for this issue.

## AAH20 | 2021-08-27T21:31:47+00:00
@UkoeHB okay lets see who can implement that and also take a look at my new issue #7896 and feel free to share your opinion.

## selsta | 2022-03-16T15:55:16+00:00
https://github.com/monero-project/monero/pull/8113

## johnnyluo | 2022-11-24T22:38:24+00:00
given https://github.com/monero-project/monero/pull/8149 has been merged , believe this one has been fixed, correct? 

# Action History
- Created by: erciccione | 2021-08-04T15:33:13+00:00
- Closed at: 2022-11-24T22:39:25+00:00
