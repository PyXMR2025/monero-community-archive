---
title: 'tx not posible '
source_url: https://github.com/monero-project/monero/issues/4133
author: yura-sutnuk
assignees: []
labels:
- invalid
created_at: '2018-07-13T20:40:32+00:00'
updated_at: '2018-07-14T15:40:54+00:00'
type: issue
status: closed
closed_at: '2018-07-14T15:40:54+00:00'
---

# Original Description
I'm testing the transaction, I successfully sent 4-5 transactions, but then there was an error
```
 {
  "error": {
     "code": -16
     "message": "tx not possible"
  }
  "id": "0"
  "jsonrpc": "2.0"
}.
```
my request looks like this
```

{"jsonrpc":"2.0",
        "id":"0",
        "method":"transfer",
        "params":{
            "destinations":[
                {"amount": 0.000000000100,
                "address":"9zVq8LppqpzfGoKnJJ5RLHgvMViP2g1hCPCAzqv2ppNv598tNFthYjnf3oDnHkwDaqXUQGSo6tXVCDeBRD9kpsamPgiVBnZ"}
               ],
                  
            }}
```

 money on the wallet enough. why it arose and how to fix it?

# Discussion History
## moneromooo-monero | 2018-07-13T23:34:07+00:00
Are you sure you have enough unlocked monero for this and th fee ?

## yura-sutnuk | 2018-07-14T05:08:42+00:00
yes, this is testnet so i have 100 monero on wallet, also when i have not enough unlocked balance the error say "not enough unlocked money"

## yura-sutnuk | 2018-07-14T05:14:25+00:00
also when I send 100 piconero, sends all 100 monero, but 99 are back, and now they are on the blocked balance, I have to wait for them to be on the unlocked balance again. it turns out I can make only 1-2 transactions and then wait again when the balance unlocks?

## yura-sutnuk | 2018-07-14T06:30:09+00:00
it looks like a problem realy is in the shortage of funds for paying fee due to the fact that although I have 100 monero but almost all of them are sent regardless of the amount of the transaction but the excess is then returned to the closed balance
```
Height 1143644, txid <26bb0871459af596d86793e32ec797fefb871ffa7127d85fe0ee2b6675c55dfc>, 99.995675199789, idx 0/0
Height 1143644, txid <26bb0871459af596d86793e32ec797fefb871ffa7127d85fe0ee2b6675c55dfc>, spent 99.996540069789, idx 0/0
Height 1143644, txid <26bb0871459af596d86793e32ec797fefb871ffa7127d85fe0ee2b6675c55dfc>, spent 0.000000000010, idx 0/0
```


## moneromooo-monero | 2018-07-14T09:06:41+00:00
in the wallet: set_log 2
Try your tx again
If it fails with the same error, paste the resulting log here, or fpaste.org, or paste.debian.net or pastebin.mozilla.org

## yura-sutnuk | 2018-07-14T12:47:43+00:00
Yes, it happens again. from wallet cli:
```
Height 1143871, txid <697e1628c66f22fcd9429cee4193e5cb832aa704e7347f201fceab8bf855fed1>, 99.994810719789, idx 0/0
Height 1143871, txid <697e1628c66f22fcd9429cee4193e5cb832aa704e7347f201fceab8bf855fed1>, spent 99.995675199789, idx 0/0
Height 1143871, txid <697e1628c66f22fcd9429cee4193e5cb832aa704e7347f201fceab8bf855fed1>, spent 0.000000000010, idx 0/0
Height 1143871, txid <e65e3e8c99cf7f80344eb4a6e4e30551ee48d2c61a32c4d018b186ec05349a05>, 0.092080199778, idx 0/0
Height 1143871, txid <e65e3e8c99cf7f80344eb4a6e4e30551ee48d2c61a32c4d018b186ec05349a05>, spent 0.000000000010, idx 0/0
Height 1143871, txid <e65e3e8c99cf7f80344eb4a6e4e30551ee48d2c61a32c4d018b186ec05349a05>, spent 0.092944679778, idx 0/0
Height 1143871, txid <b87bd490e50a7769999965602b696d7c512dba8078f481459c792079e5fe4014>, 0.993090199868, idx 0/0
Height 1143871, txid <b87bd490e50a7769999965602b696d7c512dba8078f481459c792079e5fe4014>, spent 0.000000000010, idx 0/0
Height 1143871, txid <b87bd490e50a7769999965602b696d7c512dba8078f481459c792079e5fe4014>, spent 0.993954679868, idx 0/0
Height 1143871, txid <62c5358ea306615f0f0717491cd283cf21ee1c8b447ee124ac8977b3e0681941>, 9.983483539669, idx 0/0
Height 1143871, txid <62c5358ea306615f0f0717491cd283cf21ee1c8b447ee124ac8977b3e0681941>, spent 0.000000000010, idx 0/0
Height 1143871, txid <62c5358ea306615f0f0717491cd283cf21ee1c8b447ee124ac8977b3e0681941>, spent 9.984348019669, idx 0/0
Height 1143871, txid <b5124062e305188e8ba8545e6b924eac821bfd5c3424b61ecdc454271f83f83f>, 0.993080199778, idx 0/0
Height 1143871, txid <b5124062e305188e8ba8545e6b924eac821bfd5c3424b61ecdc454271f83f83f>, spent 0.000000000010, idx 0/0
Height 1143871, txid <b5124062e305188e8ba8545e6b924eac821bfd5c3424b61ecdc454271f83f83f>, spent 0.993944679778, idx 0/0
[wallet 9toANQ]: balance
Currently selected account: [0] Primary account
Tag: (No tag assigned)
Balance: 112.056546061372, unlocked balance: 0.000001202490
```
from wallet rpc:
```
2018-07-14 12:46:42.098 [RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:5327     Requested ring size 1 too low for hard fork 7, using 7
2018-07-14 12:46:42.516 [RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:7560     1. THROW EXCEPTION: error::tx_not_possible
2018-07-14 12:46:42.521 [RPC0]  WARN    net.http        src/wallet/wallet_errors.h:794  /DISTRIBUTION-BUILD/src/wallet/wallet2.cpp:7560:N5tools5error15tx_not_possibleE: tx not possible, available = 0.000001202490, tx_amount = 0.000000000010, fee = 0.000864480000
```


## yura-sutnuk | 2018-07-14T12:51:08+00:00
i am trying send only 10 piconero why sending 99.9 monero? they of course returned but balance become locked and i cannot send it again and now i have this error "tx not possible"

## moneromooo-monero | 2018-07-14T13:22:07+00:00
0.000001202490 is not enough for the fee.

Outputs are chosen randomly among unrelated outs, unless one or two are large enough, in which case those are used. You can send to several recipients in one tx if you want.


## yura-sutnuk | 2018-07-14T15:19:38+00:00
I can not affect how much monero goes and if I need to do several separate transactions I have to wait until the balance is unlocked, right?. if so then I think you can close the topic

## moneromooo-monero | 2018-07-14T15:35:42+00:00
Mostly right. You can make sure merge-destinations is 0 in settings (type "set"), and send yourself small outputs if you want. Otherwise, you can't.

+invalid


# Action History
- Created by: yura-sutnuk | 2018-07-13T20:40:32+00:00
- Closed at: 2018-07-14T15:40:54+00:00
