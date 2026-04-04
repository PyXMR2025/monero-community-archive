---
title: windows gui 14.0.0 no balances
source_url: https://github.com/monero-project/monero-gui/issues/2195
author: finehobby
assignees: []
labels:
- resolved
created_at: '2019-06-04T14:50:40+00:00'
updated_at: '2019-07-04T06:36:41+00:00'
type: issue
status: closed
closed_at: '2019-07-04T06:36:41+00:00'
---

# Original Description
After installing version 14.0.0 under windows I created a new wallet using with ledger nano. (previously 13.0.4 used without problems). You can't set the restore hight and no balances are displayed after the synchronization? I tried both: simple mode and bootstrap.
I ask for help

# Discussion History
## dEBRUYNE-1 | 2019-06-04T20:23:54+00:00
Try this guide:

https://monero.stackexchange.com/questions/10598/how-do-i-restore-recreate-my-ledger-monero-wallet

## finehobby | 2019-06-05T09:20:39+00:00
thank you for the link, but this is my problem, in the guid i read:
_Note: Use this work around if you cannot access the Restore height box:
There is a fix for the time being: You can access the restore height window by selecting the wallet location and pressing tab once._
what does it mean : "wallet location"? i dont find this place, where i can press the tab to put in the restore heigth?


## dEBRUYNE-1 | 2019-06-06T07:10:17+00:00
It is the wallet location box, see box (2) of this screenshot:

https://github.com/monero-ecosystem/monero-GUI-guide/raw/master/media/create_hardware_wallet.png

## finehobby | 2019-06-06T11:22:26+00:00
yes this was the solution, it worked and i see balances, thank you for help.
Another question: everytime when I open the .exe i must do this procedure with create a new wallet from hardware? The old Version 13.0.4 started with asking pasword and then found the wallet. Now begins with language and Mode selection?

## dEBRUYNE-1 | 2019-06-06T15:27:24+00:00
@finehobby - No, it should open your Ledger Monero wallet automatically. Did you make sure to exit the wallet properly? That is:

>It's imperative that the closing process of your Ledger Monero wallet is done in this specific consecutive order:

>[1] Exit the GUI by clicking on the x (right top).

>[2] Exit the Ledger Monero app.

>[3] Unplug the Ledger device.

## finehobby | 2019-06-06T20:05:12+00:00
Hello, but I really finished the wallet. That can't be it. It's curious, because with version 13.0.4 it works fine and after the start you are asked for the password and the balance is there. But with version 14.0.0 I have to recreate the wallet every time. Had also deleted everything from the PC in the meantime. But what is strange, when creating a new wallet, the old wallet name is always given. I don't know where it is stored on the PC?

Translated with www.DeepL.com/Translator

## dEBRUYNE-1 | 2019-06-07T07:00:22+00:00
>I don't know where it is stored on the PC?

On Windows the files should be stored in `Documents\Monero`, can you check if the wallet files of the *new* Ledger Monero wallet are actually stored there? 

## dEBRUYNE-1 | 2019-07-04T06:31:08+00:00
I am going to close this, as the author has not responded for ~4 weeks.

## dEBRUYNE-1 | 2019-07-04T06:31:12+00:00
+resolved

# Action History
- Created by: finehobby | 2019-06-04T14:50:40+00:00
- Closed at: 2019-07-04T06:36:41+00:00
