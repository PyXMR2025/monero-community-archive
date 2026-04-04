---
title: '[User Interface] Transaction Stuck with BlockHeight 0 and the Amount is Locked
  (in GUI Beta)'
source_url: https://github.com/monero-project/monero-gui/issues/444
author: ghost
assignees: []
labels:
- resolved
created_at: '2017-02-02T14:13:23+00:00'
updated_at: '2017-08-07T18:40:10+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:40:10+00:00'
---

# Original Description
I sent a transaction using the GUI and the amount is deducted from my wallet balance, but the transaction was never placed on the blockchain. The "History" tab shows a BlockHeigh of 0 and it has been stuck in this state for 2 days now. How can I cancel this transaction and return these funds to my balance? The wallet says the transaction id is ce609b67ffb51011bf52f5d97aef698ee532eb2867bbf9c02f40affc7eaf2f25 and this doesn't exist on the blockchain. Thank you!

# Discussion History
## dEBRUYNE-1 | 2017-02-02T18:15:13+00:00
There's two options. The most convenient option is to take the binaries from the buildbot. They are on current master. You can find them here:

https://github.com/monero-project/monero-core/pull/442

First, click on details of your relevant operating system. On the left side of the page you'll see "Steps and Logfiles:". At step 6 you can download the buildbot binaries. 

Subsequently, run the binaries and open the relevant wallet. Go to the `Send` page and use the `Rescan Spent` button. This will make sure that the wallet shows the correct balance again. 

----------------------------

As second option you can remove the cache such that a rescan is triggered. See instructions here:

https://monero.stackexchange.com/questions/3122/how-do-i-delete-the-wallet-cache/3123

## medusadigital | 2017-04-18T09:47:37+00:00
can probably be closed.

## dEBRUYNE-1 | 2017-08-07T17:49:16+00:00
+resolved

# Action History
- Created by: ghost | 2017-02-02T14:13:23+00:00
- Closed at: 2017-08-07T18:40:10+00:00
