---
title: 'Privacy: Transaction uniformity and receiving address type -- practical statistical
  de-anonymization'
source_url: https://github.com/monero-project/monero/issues/9351
author: AlwaysCompile
assignees: []
labels:
- low priority
- discussion
created_at: '2024-06-03T19:28:59+00:00'
updated_at: '2024-06-05T11:54:43+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I do not have a lot of technical expertise other than that as a QA, so I at least have some attention to detail. I notice that Monero is highly dependent on transaction uniformity. It follows the principle _the nail that stands out gets hammered_, so in other words you do NOT want to stand out (or else you lose privacy).

Knowing this I used a block explorer to analyze transaction non-uniformi and I notice that **Monero transactions are not very uniform!** I do not know the technical reason for this only say that from an observation point of view anyone can see when looking at a block explorer.

**Problem / Observation**
This non-uninformity can be especially seen as the number of outputs increases. 1/2, 2/2 transactions are _reasonably uniform_, but beyond that no. For example, look at these two 1/16 transactions:

1. https://moneroexplorer.org/tx/ed792c0b42b6506aacac47f86899186ecd4482f2838935ac32ee3d82e4d67f40
2. https://moneroexplorer.org/tx/5becd73df6b33ab2544f576d7bc5b5500a283f0c87a59eb164ddb9eb6919dc8e

From observation the _fee per byte_ and _extra_ is what makes these two transactions so non-uninform despite being in the same block.

Fee per byte maybe can be ignored there is perhaps some randomness to it. However, **why is the extra field _sixteen times_ larger in one transaction?**

I cannot read the code to find out, but I did some testing in feather wallet. Here are the results of the test combinations:

1. **large extra**: many outputs, all to diff subaddresses
2. **small extra**: many outputs, all to diff / same non-subaddress
3. **small extra**: many outputs, all to same non-subaddress


Please correct if I am wrong, but based on these tests it appears extra field length is mostly depending on the number of subaddresses used in a transaction. > 1 unique subaddresses will proportionally increase the extra length. 

**Conclusion:** Extra info / size reveals metadata about the receiving address. Primarily, whether they  are  receiving to a subaddress or a non-subaddress. The is problematic because any non-uninformity creates more data to create statistical probabilities of non-spent / spent outputs to de-anonymize users.

**Note** this entire issue depends on this assumption, so if I am wrong in this observation, then maybe the rest of the issue makes no sense.

**Probabilistic de-anonymization**

For example, Feather wallet users spends a transaction from the TX with _small extra_. We know that is _highly improbable_ to be their true output. How so? Feather wallet does not show primary addresses to receive from (like most sane wallets). So, we know two things about a Feather wallet user:

1. They will be receiving to the a subaddress
2. Any decoy output that has a high-statistical chance of using non-subaddresses is likely not theirs

The small extra output likely has no outputs going to a subaddress. So, any of it's decoys used are highly likely not true inputs to any transaction created by Feather wallet. Thus the anonymity set of feather wallet user was reduced.

One might say, well how do we know they are a Feather wallet user?

The reality is many users use subaddresses exclusively. Most wallets only show subaddresses (like Feather) and other wallets generally encourage a new address per receive, which means subaddresses are the most likely.

However, beyond that, fingerprinting a feather wallet user is likely not difficult. For example, Feather wallet will relay a transaction to every online node it has knowledge of. Whereas, other wallets only relay to one node. There are likely other fingerprinting methods that could be used. But, like I said, most real users are forced into subaddresses regardless, so basically decoy outputs that are highly unlikely to be sent to subaddresses are likely not theirs.

**Solution**

The solution is to improve transaction uninformity. In this case, **one solution would be to deprecate the sending to non-subaddresses, so every receiving address MUST be a subaddresses**. This follows the direction many wallets already use (such as feather wallet) that will only provide subaddresses for the user to be received to.

In addition, it will help solve the previous bug I identified in #9350 . I can speculate the reason this bug exists is to try to create more transaction uniniformity for the 2-output TX case by ensuring in normal use 2 subaddresses never appear in a 2 output transaction. However, improving transaction uninformity in this issue will remove the motive that caused the 9350 bug.

As a non-technical user maybe there is a better way to improve uniformity without deprecating non-subaddresses. My understanding is the uninformity bug is created because subaddress usage > 1 means a pubkey or something must be added to the TX extra field in order for the subaddress to function. This does not exist with non-subaddresses and therefore no extra data is added.

As an alternative to deprecating non-subaddresses maybe it would be possible to create some type of dummy data? in that way it is not possible to use heuristics to determine the quantity of non-subaddresses versus subaddress receivers per-transaction. I will leave that to more intelligent technical minded people.

 

# Discussion History
## Rucknium | 2024-06-04T20:26:41+00:00
This change is under development. Seraphis, a new proposed format for Monero transactions, would eliminate the distinction between subaddresses and main addresses: https://github.com/UkoeHB/Seraphis/blob/master/implementing_seraphis/Impl-Seraphis-0-0-3.pdf

There is an even newer proposal to implement Curve Trees in Monero, but I don't know if it would immediately eliminate the subaddress/main address distinction: https://www.getmonero.org/2024/04/27/fcmps.html

For more info on transaction non-uniformity, you can see my work here:
https://github.com/Rucknium/presentations/blob/main/Rucknium-Monerotopia-2023-Slides.pdf
https://github.com/Rucknium/misc-research/blob/main/Monero-Fungibility-Defect-Classifier/pdf/classify-real-spend-with-fungibility-defects.pdf
https://github.com/Rucknium/misc-research/tree/main/Monero-Nonstandard-Fees
https://reddit.com/r/Monero/comments/176e1zr/privacy_advisory_exodus_desktop_users_update_to/
https://reddit.com/r/Monero/comments/12kv5m0/empirical_privacy_impact_of_mordinals_monero_nfts/

There is a new paper at this conference, but the PDF has not been released yet: Monero Traceability Heuristics: Wallet Application Bugs and the Mordinal-P2Pool Perspective. Nada Hammad (TRM Labs, USA); Friedhelm Victor (TRM Labs, USA) https://icbc2024.ieee-icbc.org/program/program 




# Action History
- Created by: AlwaysCompile | 2024-06-03T19:28:59+00:00
