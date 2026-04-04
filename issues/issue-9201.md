---
title: Problems sending Monero
source_url: https://github.com/monero-project/monero/issues/9201
author: tacobella1
assignees: []
labels:
- question
- low priority
created_at: '2024-02-24T15:43:05+00:00'
updated_at: '2024-04-10T01:22:52+00:00'
type: issue
status: closed
closed_at: '2024-04-10T01:22:52+00:00'
---

# Original Description
I have a Monero GUI wallet that connects to my Nano X. I am unable to send funds out of my account, I get an error message. I watched a YT video which says to go to Settings - Log 4 and that this resolves the issue. I tried this solution but it still doesn't work! Any ideas as I am a bit stuck? Thanks

# Discussion History
## selsta | 2024-02-24T15:45:15+00:00
What error message do you get? Please share the exact wording. Also can you try sending monero if it's a smaller amount?

> I watched a YT video which says to go to Settings - Log 4 and that this resolves the issue

I don't think the log level is related at all, you can set it back to log level 0 or 1.

## tacobella1 | 2024-02-25T16:38:32+00:00
> What error message do you get? Please share the exact wording. Also can you try sending monero if it's a smaller amount?
> 
> > I watched a YT video which says to go to Settings - Log 4 and that this resolves the issue
> 
> I don't think the log level is related at all, you can set it back to log level 0 or 1.

Thanks for getting back to me.  The error message says. 'Can't create transaction unexpected error: Unable to send hidapi command. Error 64: The device is not connected.  

I have tried sending just a small bit of XMR but I'm still getting the error message. Does Ledger still support XMR. I have an xmr app on my nano x but when I look for the app on the ledger platform to see if it can be updated, it doesn't appear. All of my firmware and updates etc have been completed.

## selsta | 2024-02-26T01:37:28+00:00
> Does Ledger still support XMR. 

Yes, Ledger still supports XMR.

> hanks for getting back to me. The error message says. 'Can't create transaction unexpected error: Unable to send hidapi command. Error 64: The device is not connected.

How did you connect the Ledger? If via USB, can you try a different port? Also did you make user everything else Ledger related is closed, do not use monero and Ledger Live simultaniously.

## tacobella1 | 2024-02-28T20:38:52+00:00
I connected it by USB, I have tried both ports. Ledger is closed when i am trying. My Ledger is working with other apps

## selsta | 2024-02-28T21:04:06+00:00
What operating system are you using? Did you make sure that the Ledger stays unlocked and the Ledger monero app open and plugged in?

Do you have access to a different computer where you can try to create a transaction?

## tacobella1 | 2024-02-28T21:36:17+00:00
I will try to set up a new account on a different computer tomorrow. Do you think it's more likely to be the computer than the ledger?

## selsta | 2024-02-28T21:38:16+00:00
You don't have to create a new account, you can just copy the ledger wallet file to the new computer and then open it with monero-gui.

> Do you think it's more likely to be the computer than the ledger?

I don't know, but it seems the Ledger loses connection to the computer during the transaction creation. Could be the computer, could be a bad cable, could be anti-virus interferring, etc.

## tacobella1 | 2024-02-29T19:46:38+00:00
I got it working by deleting the Monero program and reinstalling it from scratch. Thank you for your help, much appreciated.

# Action History
- Created by: tacobella1 | 2024-02-24T15:43:05+00:00
- Closed at: 2024-04-10T01:22:52+00:00
