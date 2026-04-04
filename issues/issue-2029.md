---
title: Output selection, and output creation issues
source_url: https://github.com/monero-project/monero/issues/2029
author: RandomRun
assignees: []
labels: []
created_at: '2017-05-15T04:37:02+00:00'
updated_at: '2017-08-07T15:46:12+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
**Output selection:**

I just noticed that in the new wallet 'Wolfram Warptangent' (v0.10.3.1-release), the output selection for a given transaction doesn't seem to be randomized anymore. I tried using @kenshi84's `print-ring-members = 1` which has been very useful in the past, but now it is almost useless, since the outputs are not changing anymore. I find that very frustrating, and it seems like too big a restriction to impose on users. I mean, I get that the new way must have some positive points, but ultimately IMHO the user should have the final say over what outputs go into his/her transaction. 

I don't know the merits of the new system, but I believe that we should randomize everything we can, since predictable patterns tend to work against anonymity. However, if you guys feel that the current way is superior, **can we at least have the option under** `set` **to use the previous randomized output selection algorithm** (perhaps leaving the current non-random method as default)?

**Output creation:**

Here is another behavior that I can't make sense of, and I witnessed this both on testnet, and mainnet: when sending money to myself (different wallets, though), at times the transaction creates *two* outputs for the *same* address. This is creating potential linkability for no apparent good reason, since in the future when the user wants to spend the money, two outputs might be spent from the same transaction, or at least that will be a problem for the wallet to solve... Now, I see from the help session that:

>merge-destinations <1|0> - whether to merge multiple payments to the same destination address

and that indeed seems to fix it. But then **shouldn't the default be switched `merge-destinations = 1`** to help preserve unlinkability? I mean, it even seems from my tests that not merging copies some of the input's amounts, which seems to me like a big and unnecessary leak of information. (Is there a use case where that would ever be desirable?)

Please let me know if I am missing the point on the issues raised above.



# Discussion History
## dEBRUYNE-1 | 2017-05-15T13:20:34+00:00
>at times the transaction creates two outputs for the same address.

As far as I know this is fixed in #1961. 

## moneromooo-monero | 2017-05-15T15:09:43+00:00
Output selection should still be random *within the set of outputs which aren't related*. That might be buggy though.

merge-destinations is meant to merge separate transfers (ie, when you send twice to the same recipient in the same command). The fact that it created more than one output per recipient for a single transfer was a bug, now fixed.


## moneromooo-monero | 2017-05-15T15:11:23+00:00
Also, there's a first try attempt at getting two unrelated outputs, before the general algorithm. In many cases, those will be selected all the time. If there's a better way to select, it'd certainly be accepted, though there's often pros and cons in any method.


# Action History
- Created by: RandomRun | 2017-05-15T04:37:02+00:00
