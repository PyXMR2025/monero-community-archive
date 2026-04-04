---
title: Prompt for password when sending transaction, not opening application
source_url: https://github.com/monero-project/monero/issues/1745
author: woodser
assignees: []
labels: []
created_at: '2017-02-18T17:47:11+00:00'
updated_at: '2017-08-08T11:30:16+00:00'
type: issue
status: closed
closed_at: '2017-08-08T11:30:16+00:00'
---

# Original Description
This is consistent with other applications like Bitcoin Unlimited / Core, Ethereum Wallet, CoPay, Jaxx, etc.

It's an easier experience for the user and emphasizes the finality of sending funds.

If privacy is a concern, this behavior may be optional to the user.

Would this be technically possible?

# Discussion History
## moneromooo-monero | 2017-02-18T18:36:23+00:00
Technically, yes. but it seems a bit pointless since you'll need the password to do anything interesting.
What would be the point anyway, since you'd have to input the password later ?

## woodser | 2017-02-18T23:30:00+00:00
@moneromooo-monero This would be one less step to launch the application, view available balance, copy the receive address, or view transaction history.  This is how most wallets work.  It's convenient but still secure.

## hyc | 2017-02-19T00:59:33+00:00
The receive address is already available in a separate plaintext file. Most people consider viewing available balance and transaction history to be privileged information that needs to be protected.

## moneromooo-monero | 2017-02-19T09:27:29+00:00
I'd consider the address to also be privileged. Maybe I need to kill of fthat foo.address.txt generation...


## moneromooo-monero | 2017-02-19T18:49:34+00:00
Anyway, this could be possible by encrypting the private spend key with a separate password, and keeping the wallet otherwise passwordless. But I don't think we want to do that. Another wallet maker may well choose to do so though.

## binaryFate | 2017-04-03T12:27:20+00:00
> "This is consistent with other applications like Bitcoin Unlimited / Core, Ethereum Wallet, CoPay, Jaxx, etc."   
> "This is how most wallets work"   
   
Seems that @woodser does not grasp how addresses, balances and view keys works in Monero, and that you guys are answering at a lower-level, while not explaining the big picture.   
   
The big picture is that with Monero you can't even see a balance, without a viewkey that is private. It doesn't work like Bitcoin that everybody can look up the balance of an address. So without asking the user for a password, the GUI could not do anything, not even show you anything.

## moneromooo-monero | 2017-08-08T11:24:57+00:00
All the "view" information is encrypted, so this will not be done.
Another wallet is free to not encrypt that information and behave as requested, though I wouldn't recommend that.

+resolved


# Action History
- Created by: woodser | 2017-02-18T17:47:11+00:00
- Closed at: 2017-08-08T11:30:16+00:00
