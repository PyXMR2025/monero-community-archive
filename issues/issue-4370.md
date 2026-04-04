---
title: monero-wallet-cli logical error!
source_url: https://github.com/monero-project/monero/issues/4370
author: ncnylon
assignees: []
labels: []
created_at: '2018-09-13T03:28:45+00:00'
updated_at: '2018-09-22T16:00:54+00:00'
type: issue
status: closed
closed_at: '2018-09-22T16:00:54+00:00'
---

# Original Description
Hi there:

I was authorized by an crypto currency exchange to take a penetration testing for the current version (v0.12.3.0) of Monero wallet, I was following the method which posted by [this,](https://hackerone.com/reports/379049) and I can confirmed that the wallet was operating correctly and there is no any side effects on our customer's services.

After that, I want to transfer ~1.685XMR back to my another account, but the command line tool of Monero wallet cannot process correctly. Here's my steps to get the error message:

\[wallet <wallet_addr>\]: version
Monero 'Lithium Luna' (v0.12.3.0-release)
[wallet <wallet_addr>]: show_transfers
 1657607     in       2018-09-09       0.690000000000 <txid1> 0000000000000000 0 - 
 1657622     in       2018-09-09       1.000223730000 <txid2> 0000000000000000 0 - 
 1657635    out       2018-09-09       1.500000000000 <txid3> <16 chars HEX code> 0.002195060000 <dummy_addr>: 1.500000000000 0 - 
 1657660     in       2018-09-09       1.497255825000 <txid4> 0000000000000000 0 - 
[wallet <wallet_addr>]: transfer_original <dest_addr> 1.685                                                                     
Wallet password: 
Error: internal error: the tx uses funds from multiple accounts
Error: There was an error, which could mean the node may be trying to get you to retry creating a transaction, and zero in on which outputs you own. Or it could be a bona fide error. It may be prudent to disconnect from this node, and not try to send a tranasction immediately. Alternatively, connect to another node so the original node cannot correlate information.
[wallet <wallet_addr>]:

Also, I tried used another mobile app to transfer, no go. Because they are calling the monero-wallet-rpc command.

Until now, I can only receive XMR from others but fail to send. Is that mean my 1.686 XMR was freeze?


# Discussion History
## moneromooo-monero | 2018-09-13T08:27:16+00:00
Don't use transfer_original, it's obsolete and unmaintained, and about to be removed. Can you repro it with transfer ?

## ncnylon | 2018-09-13T08:37:35+00:00
> 
> 
> Don't use transfer_original, it's obsolete and unmaintained, and about to be removed. Can you repro it with transfer ?

If using the transfer command, output was: 

> transaction was not constructed.

Then no any relating logs found in bitmonero.log.

I think the problem is: when the wallet calculate the unlocked balance, there is an error on previous transactions which is notated by <dummy_address>, so it will not be approved by the remote node and cannot be processed further.

## moneromooo-monero | 2018-09-13T08:46:15+00:00
In the wallet:
set_log 2
Then try again
Then post the resulting log to fpaste.org or paste.debian.net or a gist.

## ncnylon | 2018-09-13T14:06:25+00:00
I am using the command:

> sweep_all <dist_addr> <payment_id>

then get the result in [http://paste.debian.net/1042086/](url)

Thanks for your reply.

## moneromooo-monero | 2018-09-13T14:12:48+00:00
That's fixed in #4330.

## moneromooo-monero | 2018-09-22T15:59:13+00:00
+resolved

# Action History
- Created by: ncnylon | 2018-09-13T03:28:45+00:00
- Closed at: 2018-09-22T16:00:54+00:00
