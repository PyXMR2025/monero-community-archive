---
title: CLI Wallet parsing incorrect balance
source_url: https://github.com/monero-project/monero/issues/4018
author: el00ruobuob
assignees: []
labels: []
created_at: '2018-06-18T07:28:00+00:00'
updated_at: '2018-07-31T11:50:32+00:00'
type: issue
status: closed
closed_at: '2018-07-31T11:50:31+00:00'
---

# Original Description
Hi folks,

I have a strange behavior on monero-wallet-cli (discovered with monerujo [here](https://github.com/m2049r/xmrwallet/issues/227)).

First, my design:
- I have a full node called "front wallet" on which i have an audit wallet (GUI)
- I have an semi-air-gapped vm "back wallet" connected to "front wallet" only with a dedicated interco on which i have my expense wallet (GUI too)
- I use monerujo on my smartphone to check my balance with an audit wallet, which i connect to my full node.
- I only had a few mining incomes, and no expenses.

The issue:
- I wanted to contribute in FFS.
- I created a transaction on front wallet, pass the tx file to back wallet, sign it, and give it to back to my front wallet, success transaction gone
- At this time, i saw (by the difference between balance and unlock balance) the change my transaction had generated, but in the gui history, no problem. I see the expense corresponding to my FFS donation.
- Later i opened monerujo and let him refresh, but here i could see a different transactation.
  - Transaction expected: - Transaction - Fees - Change + Change
  - Transaction seen: + Transaction + Fees + Change
- I tried to create a new audit wallet, let it sync, same behavior
- As suggested by @m2049r i tried restoring the audit wallet with monero-wallet-cli: same behavior
- I tried to open my expense wallet with cli: as it has been parsed correctly by the GUI, i have the right balance. 

Now i'm restoring the expense wallet from seeds on my "back wallet" machine to see how it behaves.

What log could i send?

# Discussion History
## moneromooo-monero | 2018-06-18T08:35:05+00:00
This is a bit confusing.
If the audit wallet a view only wallet ? It seems implied. I also guess the expense wallet is a wallet with the spend key. What is an interco ? Is the incorrect value showing on a view only walet, or on a full wallet ? Is this fixed by https://github.com/monero-project/monero/pull/3985 ? Are you using subaddresses in this wallet ?


## el00ruobuob | 2018-06-18T15:42:35+00:00
Sorry for the confusion.

- Audit wallet (or Front Wallet) is a view only wallet ;
- Expense wallet (or Back Wallet) is the same wallet with spend key.
- The "interco" is just a private netowrk between my two VMs i use to give my "back wallet" access to my node, or to transfer a tx file between front and back wallet (it is not really important in this issue) so that "back wallet" is not directly routable from the Internet World
- The incorrect value is on view only wallet in CLI only (spend cli wallet still syncing, so i can tell) . View only wallet in GUI is showing the good balance, as well as spend GUI wallet.
- I have not tested #3985 but can give it a try soon.
- I do have two subadresses generated on this gui wallet (not used or involved in the transaction), but i even did not generate them in the cli wallet.

## moneromooo-monero | 2018-06-18T20:11:05+00:00
Did you export/import key images ?

## el00ruobuob | 2018-06-18T21:14:10+00:00
No. I only created, signed, and import a tx file.

Btw, my "spend" cli wallet has sync and it is showing the appropriate balance.
Last logs in it shows the transactions (i don't mind publishing it, as my donation was itself public on the forum):
```
Height 1594880, txid <5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589>, 2.209497808428, idx 0/0
Height 1594880, txid <5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589>, spent 0.411971888428, idx 0/0
Height 1594880, txid <5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589>, spent 2.000000000000, idx 0/0
```

On the view-only wallet, the last two are not counted in the balance.

## el00ruobuob | 2018-06-18T21:19:35+00:00
show_transfers from spend_wallet:
```
 1594880    out       2018-06-14       0.200000000000 5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589 1828f3582065d29550ebab4b20841f7fe0206dfccf74479e5ce5978f5354e614 0.002474080000  0 -
```

Show_transfers from read-only wallet:
```
 1594880     in       2018-06-14       2.209497808428 5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589 1828f3582065d29550ebab4b20841f7fe0206dfccf74479e5ce5978f5354e614 0 -
```

## el00ruobuob | 2018-06-18T21:22:49+00:00
show_transfer <txid> on spend wallet:
```
[wallet 47xu3g]: show_transfer 5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589
Outgoing transaction found
txid: <5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589>
Height: 1594880
Timestamp: 2018-06-14
Amount: 0.200000000000
Payment ID: 1828f3582065d29550ebab4b20841f7fe0206dfccf74479e5ce5978f5354e614
Change: 2.209497808428
Fee: 0.002474080000
Destinations:
Note:
```
on view-only wallet:
```
[wallet 47xu3g]: show_transfer 5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589
Incoming transaction found
txid: <5c695ab11d4e034fdd978faa91dec83207f10e318de8471df115e1972dc65589>
Height: 1594880
Timestamp: 2018-06-14
Amount: 2.209497808428
Payment ID: 1828f3582065d29550ebab4b20841f7fe0206dfccf74479e5ce5978f5354e614
3071 confirmations
Address index: 0
Note:
```

## iDunk5400 | 2018-06-19T18:08:41+00:00
You can learn [here](https://monero.stackexchange.com/questions/2868/is-there-any-way-to-construct-a-transaction-manually/2916) how to use the view-only wallet.

## moneromooo-monero | 2018-06-19T21:27:23+00:00
Re-reading the first post, do you have *two* view only wallets ? I had missed that at first, but it kinda seems like it.

## el00ruobuob | 2018-06-20T05:09:16+00:00
I only have one single wallet (One address). Restored as view-only or with spend key depending on the situation.

## moneromooo-monero | 2018-06-20T07:33:43+00:00
If restored, that counts as two :)
If a wallet doesn't know about one of its output's key images, then it can't see when it's spent.

## el00ruobuob | 2018-06-20T11:08:06+00:00
Ok. So by design a view-only wallet will incorrectly parse the spend amount If it has not seen the output key image? Isn't it a problem if we wanted to use view-only for audit purposes?

## moneromooo-monero | 2018-06-20T11:58:08+00:00
It parses fine AFAICT. I does not know which key images are yours unless you import key images, which you said you did not do. If that's still buggy after you do it, it may need fixing.

## el00ruobuob | 2018-07-31T11:50:31+00:00
Close because OP wasn't fully understanding the wallet mechanism at the time of opening.

# Action History
- Created by: el00ruobuob | 2018-06-18T07:28:00+00:00
- Closed at: 2018-07-31T11:50:31+00:00
