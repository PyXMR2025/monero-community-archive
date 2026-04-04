---
title: Transaction made with pre-fork xmr-cli on post-fork network
source_url: https://github.com/monero-project/monero/issues/5312
author: vprcs
assignees: []
labels: []
created_at: '2019-03-18T15:24:18+00:00'
updated_at: '2019-03-26T13:41:48+00:00'
type: issue
status: closed
closed_at: '2019-03-26T13:41:48+00:00'
---

# Original Description
Hi, 

last week I totally forgot about Monero network upgrade and I have sent a transaction with xmr-cli v0.13.0.4 couple of days *after* the network switched. I can see the balance of the account being the same, however when i want to repeat the transaction or do anything with the account i get a "double spend error". Is there a way to recover the funds ? 

thanks !

# Discussion History
## moneromooo-monero | 2019-03-18T15:43:55+00:00
The tx might be in your daemon. flush_txpool, refresh, refresh, try again.

## vprcs | 2019-03-18T15:49:43+00:00
Thanks for the quick reply. Should i do it with the new v0.14.0.2 client or with the old one ? Are you implying that the trasaction should go through even with the old client on a new network ? 

## moneromooo-monero | 2019-03-18T15:52:03+00:00
New one. If you sent with an old wallet and daemon, what probably happened is that your daemon accepted it but other daemons which were up to date did not, so your daemon is waiting for someone to mine it, which will not happen (except on the obsolete chain). After you update, you need to tell your daemon to remove that tx. It might do that automatically, not sure. But if not, flush_txpool, and double refresh in the wallet. If your tx was not mined on the blockchain, you will be able to send your monero normally.

## dEBRUYNE-1 | 2019-03-18T18:09:54+00:00
You should be able to resolve your issue with this guide:

https://monero.stackexchange.com/questions/7993/i-forgot-to-upgrade-from-cli-or-gui-v0-13-to-cli-or-gui-v0-14-and-created-pe

## vprcs | 2019-03-18T18:11:58+00:00
@moneromooo-monero thanks for advice. i will add that this only works when you operate on the same wallet files as when you created the tx. i had a earlier backup of the wallet (pre bad tx), to which i reverted and flush_pool wasnt working with it, i had to do it with the post-bad tx wallet. terminology lol. thanks anyway, here have some love <3 :100: 

## vprcs | 2019-03-18T18:12:53+00:00
@dEBRUYNE-1 yes, found it only after opening this issue. sorry :)

## moneromooo-monero | 2019-03-18T20:48:14+00:00
flush_txpool, not flush_pool, and it's a daemon command, not wallet. The two refresh calls after that are wallet commands. It should have worked, if the above is kept in mind.

## dEBRUYNE-1 | 2019-03-19T06:47:21+00:00
@vprcs - No problem. To be clear, your issue is resolved now? 

## dEBRUYNE-1 | 2019-03-26T13:32:33+00:00
I am going to close this, as the author has not responded for over a week. 

+resolved

# Action History
- Created by: vprcs | 2019-03-18T15:24:18+00:00
- Closed at: 2019-03-26T13:41:48+00:00
