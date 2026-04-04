---
title: Cant create wallet on Ledger S with Monero GUI
source_url: https://github.com/monero-project/monero-gui/issues/3725
author: FreeRide23
assignees: []
labels: []
created_at: '2021-11-03T16:55:44+00:00'
updated_at: '2022-04-27T04:50:24+00:00'
type: issue
status: closed
closed_at: '2022-04-27T04:50:24+00:00'
---

# Original Description
Hi there, did not find any working solution, so i create this.

Ledger Nano S Firmware 2.0.0
Monero App for Ledger 1.7.7
Monero GUI Wallet 0.17.2.3-113efbf (Qt 5.15.2)

Error:
Tryed to create a wallet on the Ledger with the Monero GUI, advanced mode -> "create a wallet from hardware" -> named the wallet, wallet location selected, hard ware Model selected "Ledger Nano S" -> create a new wallet from device -> "create wallet" -> error "Error writing wallet from hardware device. Check application logs" -> also a second error on bottom "failed to generate new wallet: no device found"

I tryed to search the error log in the install folder "C:\Program Files\Monero GUI Wallet\" but there is no "log"... anywhere.... wtf!?

Any ideas?

And yes: i have started the monero app on the ledger, i have restartet, i have tryed an other USB, i have closed the ledger live.... no change......

# Discussion History
## FreeRide23 | 2021-11-03T17:00:10+00:00
i will try it again on my linux laptop..... il write again when its done

## selsta | 2021-11-03T17:50:31+00:00
Did it work in the past on your Windows machine?

## FreeRide23 | 2021-11-03T18:50:21+00:00
> 
> 
> Did it work in the past on your Windows machine?

This is the first time i try it, so... no.... i dont know....

## FreeRide23 | 2021-11-04T14:19:22+00:00
Works with fresh installation of win 10....

## mphelp | 2022-01-19T16:00:29+00:00
@FreeRide23 I ran into this too when the Monero app wasn't open on my Nano S. I only had the Nano S main menu up. Making sure the Monero app was open fixed it for me. See #3057.

Does that mean you solved it and this issue can be closed? 

# Action History
- Created by: FreeRide23 | 2021-11-03T16:55:44+00:00
- Closed at: 2022-04-27T04:50:24+00:00
