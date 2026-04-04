---
title: Network lost my monero
source_url: https://github.com/monero-project/monero/issues/2380
author: walec51
assignees: []
labels:
- invalid
created_at: '2017-08-31T07:12:00+00:00'
updated_at: '2017-09-01T08:20:26+00:00'
type: issue
status: closed
closed_at: '2017-08-31T07:42:22+00:00'
---

# Original Description
http://imgur.com/a/9GSYF

transaction confirmed lots of times but there a NO transactions in my wallet history 

# Discussion History
## moneromooo-monero | 2017-08-31T07:36:36+00:00
If you're having a problem with Mymonero, check #mymonero on freenode, or ask on reddit, or there should be a contact email somewhere on the site.

+invalid


## walec51 | 2017-08-31T07:44:09+00:00
I have the exact same problem in my fully synced official desktop wallet !!!
its a network problem!

## stoffu | 2017-08-31T09:08:25+00:00
Don't panic, I'm pretty sure your fund isn't lost. Try opening the wallet file with the CLI.

## walec51 | 2017-08-31T14:27:15+00:00
same thing:

```
[wallet 48Pszc]: balance
Balance: 0.000000000000, unlocked balance: 0.000000000000
[wallet 48Pszc]: show_transfers
[wallet 48Pszc]:
```

reopen this issue

## fluffypony | 2017-08-31T14:52:02+00:00
CLI works fine, your node probably isn't caught up.

![screen shot 2017-08-31 at 4 50 29 pm](https://user-images.githubusercontent.com/1944293/29929752-a06aca46-8e6c-11e7-9804-fef4b4b08474.png)

It didn't show up in MyMonero because you didn't pay the import fee, so it only scanned for transactions from when you first loaded it into MyMonero.

## fluffypony | 2017-08-31T14:55:45+00:00
I triggered a manual import on MyMonero for no charge, and your tx is showing up on the backend now.

## walec51 | 2017-09-01T08:20:26+00:00
Ok, many thanks. Freaked out when I didn't see it in any of the three wallets. However it is still strange that a freshly installed desktop wallet didn't pick up the transactions. 

# Action History
- Created by: walec51 | 2017-08-31T07:12:00+00:00
- Closed at: 2017-08-31T07:42:22+00:00
