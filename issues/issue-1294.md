---
title: 'CLI wallet: Sending fund to your own integrated_address results in tx with
  no payment ID'
source_url: https://github.com/monero-project/monero/issues/1294
author: kenshi84
assignees: []
labels: []
created_at: '2016-11-03T05:15:23+00:00'
updated_at: '2016-11-05T09:39:57+00:00'
type: issue
status: closed
closed_at: '2016-11-05T09:39:57+00:00'
---

# Original Description
```
[wallet 4AkvYS]: integrated_address
Random payment ID: <61983fbfdf887d8e>
Matching integrated address: 4LTbZFbaFhHVpN5xasoymZGP5mSDzaEAjMeTnBj97gde7mzot4Qd8E9L33ZzRAW2TcAv3gtvfXCQz8Tu4qr6TnMLhsodpguD2zpH7VDxxE
[wallet 4AkvYS]: transfer 4LTbZFbaFhHVpN5xasoymZGP5mSDzaEAjMeTnBj97gde7mzot4Qd8E9L33ZzRAW2TcAv3gtvfXCQz8Tu4qr6TnMLhsodpguD2zpH7VDxxE 0.1
The transaction fee is 0.010000000000, of which 0.008000000000 is dust from change.
Is this okay?  (Y/Yes/N/No)y
Money successfully sent, transaction <c1c055be0e946ee25a7c67190fc38f3ca2558cb82889b5b9cf4e0399739c88f7>
Height 1171301, transaction <c1c055be0e946ee25a7c67190fc38f3ca2558cb82889b5b9cf4e0399739c88f7>, received 0.090000000000
Height 1171301, transaction <c1c055be0e946ee25a7c67190fc38f3ca2558cb82889b5b9cf4e0399739c88f7>, received 0.100000000000
Height 1171301, transaction <c1c055be0e946ee25a7c67190fc38f3ca2558cb82889b5b9cf4e0399739c88f7>, received 0.600000000000
Height 1171301, transaction <c1c055be0e946ee25a7c67190fc38f3ca2558cb82889b5b9cf4e0399739c88f7>, spent 0.800000000000
[wallet 4AkvYS]: payments 61983fbfdf887d8e
                                                             payment                                                         transaction      height               amount     unlock time
No payments with id <61983fbfdf887d8e000000000000000000000000000000000000000000000000>
```
I know this operation (sending fund to yourself with payment ID) doesn't make any sense, but still shouldn't this be seen as a bug?

# Discussion History
## moneromooo-monero | 2016-11-03T19:24:22+00:00
Look in show_transfers. The payment was most likely sent with the payment id, the payments command is just buggy.


## moneromooo-monero | 2016-11-03T19:36:57+00:00
Ah, you're correct indeed. There's nothing received apart from change, so it is considered a payment of zero to an non existent party.
show_transfers shows the payment id on an outgoing tx.
So, all fine I think. You're welcome to discuss a change of behavior in #monero-dev, as both ways kinda make sense I think.


## kenshi84 | 2016-11-04T05:33:18+00:00
I also think it's all fine. Thanks for clarification!


# Action History
- Created by: kenshi84 | 2016-11-03T05:15:23+00:00
- Closed at: 2016-11-05T09:39:57+00:00
