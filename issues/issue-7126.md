---
title: Add wallet name/path to the inactivity lock message.
source_url: https://github.com/monero-project/monero/issues/7126
author: normoes
assignees: []
labels: []
created_at: '2020-12-11T10:26:04+00:00'
updated_at: '2022-07-18T20:10:07+00:00'
type: issue
status: closed
closed_at: '2022-07-18T20:10:07+00:00'
---

# Original Description
I very much like and appreciate the locking of the wallet.

Since I tend to work with several wallets in all the Monero networks it is quite confusing to see the same lock message everywhere.

It would be nice to have the wallet name (file name) or complete file path in the lock message (maybe even along with the network mode):
It could look like this:
```
 ____________________________________________   
/ I locked the '<my_wallet_file_name_here>' Monero 'mainnet' wallet to protect you \
| while you were away                        |
\ see "help set" to configure/disable        /
 --------------------------------------------
```
instead of just:
```
 ____________________________________________   
/ I locked your Monero wallet to protect you \
| while you were away                        |
\ see "help set" to configure/disable        /
 --------------------------------------------
```

# Discussion History
## normoes | 2020-12-14T17:49:20+00:00
Is `m_wallet_file` in https://github.com/monero-project/monero/blob/master/src/simplewallet/simplewallet.cpp the right variable to use?

How can I easily  get the network mode? I bet there is a variable as well.

## moneromooo-monero | 2020-12-14T18:03:29+00:00
Yes. See wallet_info, do the same. Put the (user selected) name in the text below, not the cow speech.

## normoes | 2020-12-14T21:04:24+00:00
Understood. Thanks.

## normoes | 2020-12-15T09:46:44+00:00
So, the result looks like this.
* Nothing changed in the cow speech.
* See the linked PR https://github.com/monero-project/monero/pull/7153.
```
 ____________________________________________   
/ I locked your Monero wallet to protect you \
| while you were away                        |
\ see "help set" to configure/disable        /
 --------------------------------------------
        \   (__)
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||


Locked due to inactivity. The wallet password is required to unlock the console.
Filename: <my_wallet_file_name_here>
Network type: Stagenet
Wallet password: 
```

## bill-mcgonigle | 2020-12-30T02:01:15+00:00
Can we make this 'set'-able and a non-default behavior?  I have use cases where I would 'set' it, but if we assume that locking exists for the scenario where somebody walks away from their screen and we're protecting that user from would-be troublemakers, having the wallet name on the lock screen may be too big of an information disclosure in some situations.

## moneromooo-monero | 2020-12-30T15:03:56+00:00
That's a fair point.

## normoes | 2022-03-10T11:26:14+00:00
@moneromooo-monero 
The suggestion above is implemented:
```
set show-wallet-name-when-locked 1|0
```

Could you please check?

## selsta | 2022-07-18T20:10:07+00:00
This seems resolved.

# Action History
- Created by: normoes | 2020-12-11T10:26:04+00:00
- Closed at: 2022-07-18T20:10:07+00:00
