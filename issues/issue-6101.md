---
title: 'Will dev team consider Σ-protocols ? '
source_url: https://github.com/monero-project/monero/issues/6101
author: shine0108
assignees: []
labels: []
created_at: '2019-11-05T10:08:17+00:00'
updated_at: '2019-11-08T06:43:21+00:00'
type: issue
status: closed
closed_at: '2019-11-08T06:43:21+00:00'
---

# Original Description
It seams that Σ-protocols is better than Ring-Sign, will the dev team of monero condider Σ-protocols ?

# Discussion History
## moneromooo-monero | 2019-11-05T11:44:01+00:00
This is not really the place. You'll want to ask on Freenode in #monero-research-lab, or in https://github.com/monero-project/research-lab if you prefer github. I'll still keep this open for now in case a mathematician with an informed opinion on this pops in.


## SarangNoether | 2019-11-05T14:14:10+00:00
What sigma protocol(s) in particular?

## shine0108 | 2019-11-05T16:14:52+00:00
Here is the paper (https://eprint.iacr.org/2014/764.pdf) which the sigma protocol based on.
Using the sigma protocol mentioned in the paper, we can improve anonymity set size to N with only aboult 4 logN proof size.
So, I think sigma protocol can work better than ring sign for hiding the relationship between sender and receiver, since the computational complexity and anonymity set size are a linear relationship if we use Ring-Sign, but they are logarithmic relation while sigma protocol is used.
And Zcoin have already used the sigma protocol. 
https://github.com/zcoinofficial/zcoin

## SarangNoether | 2019-11-05T16:19:17+00:00
That particular sigma protocol deals with single lists of commitments, for which an application to Zerocoin was proposed. Work is currently underway to extend this particular construction (and a generalization by Bootle et al.) to handle the case of both amount commitments and signing keys simultaneously. Other sublinear transaction protocols have also been proposed.

## SarangNoether | 2019-11-05T16:19:58+00:00
Also note that the verifier complexity in this construction is still linear in the size of the anonymity set (with a slight reduction possible using multiexponentiation techniques).

## shine0108 | 2019-11-08T06:43:21+00:00
Thank you very much. I think it can be closed, since no any others continue to discuss this issue.

# Action History
- Created by: shine0108 | 2019-11-05T10:08:17+00:00
- Closed at: 2019-11-08T06:43:21+00:00
