---
title: 'Proposal: New CCS Wallet Setup with Collateral'
source_url: https://github.com/monero-project/meta/issues/926
author: MajesticBank
assignees: []
labels:
- proposal
created_at: '2023-11-08T19:03:25+00:00'
updated_at: '2024-02-22T14:51:24+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Starting any related write-up without considering how much Monero Core did for this project makes no sense.

Not just stewards, but role-models, crypto heroes and people who devoted their time, expertise and nerves to make Monero what is it now.

And for free so thank you !


1. 

New CCS Wallet Design need to allow CCS Coordinator (plowsof) with approval from luigi to make payments to devs in easy way.

Since at present monero-multisignature wallet tech is not 100% ready to be used as such wallet and would probably make things more complicated and not easier.

Using direct donation payments to devs is not an option for couple of reasons since there will be no oversight on their work / spend hours.

It's best to keep most of current CCS structure AS-IS.

2. 

There comes the Collateral, Collateral is given by the person who will be called Custodian.

Custodian will be in sole control of private keys of CCS wallet.

Custodian will provide Collateral in matching value as value of CCS wallet.

Considering CCS wallet balance is going up and down, the Custodian should on week / monthly basis deposit additional funds to Collateral wallet.

Collateral wallet is 2-3 multi-signature wallet, where singers are Custodian, plowsof and luigi.

Beside Custodian, any two other persons can be co-signers of Collateral wallet.

I gave plowsof and luigi as example to keep CCS structure as much AS-IS.


3.
Collateral wallet is 2-3 multi-signature wallet but it doesn't have to be Monero. 

Bitcoin multi-signature is much more tested and very ease to use using Electrum or similar.

https://electrum.readthedocs.io/en/latest/multisig.html

Option two on this topic would be to use Monero multi-signature to keep Collateral.

Positive aspect is that Monero multi-sig wallet need to be just created and used only in case there is problem.



4.

Dispute:

In case Custodian lose funds or create other problems, plowsof and luigi can claim funds from Collateral wallet.

It would need both plowsof and luigi to be compromised to steal Collateral wallet, Custodian can always claim funds from CCS Wallet.

So there is no incentive for Custodian to steal funds and would need both co-signers to be compromised.

Also Custodian will make sure those funds are super safe, since his own funds are involved.



5.

Downside:

In case We use monero multi-sig for Collateral wallet, there will be no market loss since XMR = XMR.

In case We use bitcoin multi-sig for Collateral, there is possible loss considering XMR - BTC market rate.

Since April this year XMR - BTC ratio seems stable around 0.0050 +- 10%

Protection for such losses either fall on Custodian or to the CCS Funds itself such as 10% buffer.

It doesn't have to be a loss, it actually might be a win.

I picked BTC because XMR BTC ratio is often close to each other and they follow it.


6.

Payments: 

This dependent on who is Custodian and who are two co-signers.

Best scenario is where Custodian create secure system using VMs to implement software 2-3 multisig.

Such system should be available behind auth-only onion link with high uptime level.

plowsof should be able to create payment request on software 2-3 multi-sig.

luigi would visit his side of software 2-3 on website and confirm the payment to complete the payment.

Custodian need to make sure his presence is not needed for payment to go around the clock.



Other solution would be that Custodian send payments manually as agreed with plowsof and luigi.



7.

Compensation:

Who in the world would risk his own money for the Community?

Well we can now see we took a lot of things for granted over the years.

This option is open for discussion, should and how Custodian should be paid for this role of keeping funds secure.

There is standard rate banks give on year level for deposits which is around 6%.




This is a draft to much longer idea, Collateral wallet adds liability and responsibility for Custodian to keep community money secure.





# Discussion History
## monerobull | 2023-11-09T07:49:37+00:00
Interesting idea however let's say the collateral wallet is compromised, then the custodian is refunded with the CCS funds, now the  CCS has basically been drained again. 
Even worse scenario: Custodian gets fully compromised, if either of the other collateral wallet signers now get compromised, both wallets get drained. What do you do now?


## MajesticBank | 2023-11-11T12:04:34+00:00
Thanks for taking your time to read the proposal !

`Collateral Wallet is multi-signature wallet, it's safe as much as Threshold, I hope that's clear.`

In a multisig wallet, threshold refers to the minimum number of signatories required to authorize a transaction. When creating a multisig wallet, the threshold is set as a parameter, along with the list of public keys (addresses) of the signatories.

If you consider 2/3 multisig is not safe, then add BinaryFate for example as co-signer and you have 3/4 multisig.

Any kind of assumption that you can compromise 3 people in the community to overtake 100k usd is probably just part of wildest dreams.

Currently people guarding CCS wallet had moral, integrity and non-direct financial obligation to keep community money safe.

This proposal adds direct-financial obligation for Custodian to keep the CCS wallet safe which implies he will maintain highest 

possible level of operational security to keep his (first) and then community  money secure.

`Importance of General Funds 2:`

Each proposal should have end-date written inside of it, after end-date Custodian will wait 30 days if 

conditions for payment are not meet (as decided by CCS coordinator), he should transfer funds to General Fund 2 to remove liability from his wallet

General fund 2 should have some expiry date of 60/90 days after the end-date after which funds are transferred to General Fund 1

So if someone still need funding but was 60/90 days late from end-date written in proposal, he can get it from General Fund, 

but we remove liability from CCS wallet and Custodian as much as possible to avoid issues from the past

# Action History
- Created by: MajesticBank | 2023-11-08T19:03:25+00:00
