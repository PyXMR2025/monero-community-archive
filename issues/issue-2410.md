---
title: Extend warning when using a view key that the balance might not be correct
source_url: https://github.com/monero-project/monero-gui/issues/2410
author: peli-pro
assignees: []
labels: []
created_at: '2019-10-08T09:16:53+00:00'
updated_at: '2019-10-27T19:04:38+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
If you are using a view key outgoing transactions are not reflected in the balance. This is counterintuitive for the not-so-experienced user and different from what people are used to from other cryptocurrencies. It leads to quite some questions in forums on why monero shows a wrong balance. But we have no warnings in place in the gui. This will lead to confusion for many users and it has been raised here too: https://github.com/monero-project/monero-gui/issues/1260. It can be corrected by importing keyimages.
We already have a warning in place in the gui when using a view wallet in file pages/Transfer.qml in line 751:
```
if(appWindow.viewOnly){
            root.sendButtonWarning = qsTr("Wallet is view-only and sends are not possible.") + translationManager.emptyString;
            return false;
        }
```
We might just extend this warning a bit to make clear that the balance might not be correct. Maybe something like:
```
Wallet is view-only and sends are not possible. 
Balance reflects only incoming but not outgoing transactions. 
The balance shown might be wrong.
```
or
```
Wallet is view-only and sends are not possible. 
Balance reflects only incoming but not outgoing transactions. 
The balance shown might be wrong unless you have imported key images.
```


# Discussion History
## peli-pro | 2019-10-08T16:40:18+00:00
![m](https://user-images.githubusercontent.com/55572025/66415110-0e732100-e9fb-11e9-8ca1-04a3af960af0.png)


## rating89us | 2019-10-08T19:14:29+00:00
I prefer 2nd option + adding a "Read more..." link to a getmonero.org guide explaining further this issue and how to import key images

## SamsungGalaxyPlayer | 2019-10-08T20:18:02+00:00
I would rather not include a link unless absolutely necessary. I propose the following:

```
Wallet is view-only and sends are not possible. 
Unless key images are imported, the balance reflects only incoming but not outgoing transactions.
```

We can perhaps add some help text on key images. But this is already an advanced feature.

## peli-pro | 2019-10-09T11:16:15+00:00
I think we do not need a link. If the user is aware that the balance might be incorrect and that the solution has something to do with key images - that should be enough as a warning. 
Maybe we could add that the balance reflects incoming and change transactions.
```
Wallet is view-only and sends are not possible. 
Unless key images are imported, the balance reflects only incoming and change but not outgoing transactions.
```


## SamsungGalaxyPlayer | 2019-10-11T02:09:25+00:00
@peli-pro "incoming" includes change, so it may be redundant.

## peli-pro | 2019-10-11T05:48:29+00:00
@SamsungGalaxyPlayer  It is redundant. My thought was: for not-so-experienced people it is not immediately clear that if you spend money you have an incoming transaction as change. To simplify things many wallets in other cryptocurrencies hide this fact (a ledger or trezor make you check the bitcoin address you are sending to but tell you nothing about change). So imaging you start with 10 XMR incoming and later you spend 1 XMR (0.99 XMR+0.01 Fee) your Balance will show 19 XMR in a view only wallet. Pro users immediately know that the 9 XMR are the change but newbies might be confused about recieving 9 XMR (especially if the numbers do not add up nicely).
So I thought about adding the hint with the "change". But pro users might think it is imprecise.


## rating89us | 2019-10-24T17:11:29+00:00
Is it possible to import key images into GUI wallet?

## peli-pro | 2019-10-27T19:04:38+00:00
To my knowledge you can not import them in the gui, but you can import them with the cli and then they are reflected in the gui.
The main idea is to give a user a hint that the balance might be wrong and how might resolve it.

# Action History
- Created by: peli-pro | 2019-10-08T09:16:53+00:00
