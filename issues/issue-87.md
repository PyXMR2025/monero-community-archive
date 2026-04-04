---
title: History does not show payment ID
source_url: https://github.com/monero-project/monero-gui/issues/87
author: M5M400
assignees: []
labels: []
created_at: '2016-10-25T11:53:39+00:00'
updated_at: '2016-12-20T14:36:09+00:00'
type: issue
status: closed
closed_at: '2016-12-20T14:36:09+00:00'
---

# Original Description
![screenshot from 2016-10-25 13-29-10](https://cloud.githubusercontent.com/assets/22886679/19684959/62cff8d8-9aba-11e6-9873-04c6bec27faf.png)


# Discussion History
## dEBRUYNE-1 | 2016-10-25T13:41:18+00:00
This is a bit odd. I have been testing this with @medusadigital and back then it worked perfectly. 

Could you try to use an integrated address and see what happens?

Also, which commit did you compile on? 


## medusadigital | 2016-10-26T22:28:10+00:00
Yes, we tested that, but it just happend also to me too, so i guess something with recent commits has to be causing it? or we have overseen something and it only shows with incoming/outgoing trx ? 

anyway, seems only to affect no integrated addresses @M5M400  ? or was it an integrated address? i cant tell since the screenshot is from mymonero


## M5M400 | 2016-10-27T09:48:53+00:00
@dEBRUYNE-1 I was on 05046a5. Now on 08c7ff2, as aparently b74cae4 upwards are broken (src/libwalletqt/WalletManager.cpp:164:35: error: ‘paymentIdFromAddress’ is not a member of ‘Bitmonero::Wallet’). Same behavior.

@medusadigital integrated addresses work as expected. Only transactions using normal addresses affected.


## moneromooo-monero | 2016-10-27T11:13:44+00:00
Are you sure you have a recent enough monero tree ?

$ git grep paymentIdFromAddress
src/wallet/api/wallet.cpp:std::string Wallet::paymentIdFromAddress(const std::string &str, bool testnet)
src/wallet/wallet2_api.h:    static std::string paymentIdFromAddress(const std::string &str, bool testnet);


## Jaqueeee | 2016-10-27T12:29:55+00:00
@M5M400 are you on os x?
Noticed the build instructions isn't up to date. So you would have to delete the monero folder before running build.sh to ensure you get the current wallet api. Will update those instructions soon. 


## M5M400 | 2016-10-27T13:19:09+00:00
@Jaqueeee thanks for the tip, running ubuntu but sure as hell neglected to rebuild the wallet api :( ...

@moneromooo-monero built everything from scratch. Now running on d22e02a.

Sadly, still no payment ID (the 0.1 XMR transaction is the new one - will create another issue for the date sorting not working)

![screenshot from 2016-10-27 15-17-51](https://cloud.githubusercontent.com/assets/22886679/19768621/973f99b2-9c58-11e6-8ef4-0c0ca54385f6.png)


## moneromooo-monero | 2016-10-27T19:29:20+00:00
The GUI won't show my past txes in the first place, so I'm unable to determine whether my recent patches broke this. Revert them if you want to check.


## medusadigital | 2016-11-05T09:21:47+00:00
- Paymend id's regarding new Transactions should be fixed by this: https://github.com/monero-project/monero/pull/1282
- Historical transactions (rebuilding wallet cache) should be fixed by https://github.com/monero-project/monero/pull/1295. 


## medusadigital | 2016-11-06T09:50:04+00:00
@M5M400 have time for a retest? seems good to me but i cant test all combinations


## M5M400 | 2016-11-07T12:26:30+00:00
@medusadigital what am I doing wrong? pulled current master (c9bb2f5); reran get_libwallet_api.sh; make clean; qmake; make; restore wallet from seed (new folderstructure anyway); wallet sync from block 0 -> still not showing historical or new payment IDs from standard address TXs


## dEBRUYNE-1 | 2016-11-07T16:38:25+00:00
@M5M400 Do you have a Monero folder present in the same build environment? 


## M5M400 | 2016-11-09T10:51:28+00:00
@dEBRUYNE-1 @medusadigital I'll be damned. I only ever tested incoming transactions with my mymonero wallet. Now I tested with the CLI wallet and everything works fine. Both classic addresses + payment ID as well as integrated addresses...

![screenshot from 2016-11-09 11-47-58](https://cloud.githubusercontent.com/assets/22886679/20135954/bb7f7b70-a672-11e6-86cc-4e5ecfbbf583.png)

So from where I'm sitting, it seems that there is a bug in mymonero, not in monero-core. can anyone confirm?


## M5M400 | 2016-11-15T13:30:39+00:00
is there a reason why this isn't closed already?


## Jaqueeee | 2016-11-16T18:40:24+00:00
@M5M400 Only you can close this afaik. And repo maintainer (i.e @fluffypony) ofc. 


## Jaqueeee | 2016-12-19T19:30:39+00:00
please close

# Action History
- Created by: M5M400 | 2016-10-25T11:53:39+00:00
- Closed at: 2016-12-20T14:36:09+00:00
