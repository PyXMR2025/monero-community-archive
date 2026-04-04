---
title: Monero GUI does not update after transaction
source_url: https://github.com/monero-project/monero-gui/issues/4052
author: Lowlay75
assignees: []
labels: []
created_at: '2022-10-21T19:02:20+00:00'
updated_at: '2022-10-22T09:58:41+00:00'
type: issue
status: closed
closed_at: '2022-10-21T22:08:18+00:00'
---

# Original Description
Hello, I think the problem has already been encountered. I made a transaction on local monero and it never reached my wallet. I performed a "Wallet restore height" and I put the current date (20221021).
But now I have 0.000000 XMR instead of 0.500000 before.
I should have several hundred currency. I would really like your help....

# Discussion History
## Lowlay75 | 2022-10-21T19:04:06+00:00
I would like to add that the transaction is effective here is the ID :  6ef284989deb62f9edc3cd2bdc26e0394dd2841fb9fdaebfdf1182005f292302  

## selsta | 2022-10-21T19:05:52+00:00
You have to enter a date in this format: YYYY-MM-DD not YYYYMMDD

And you have to enter a date that was before your first received transaction, not the current date.

## Lowlay75 | 2022-10-21T19:21:36+00:00
Thank you for your help, I did exactly what you told me, it still doesn't work

## selsta | 2022-10-21T19:23:15+00:00
Please go to Settings -> Info and post:

- Version
- Wallet mode
- Wallet restore height

## Lowlay75 | 2022-10-21T19:24:29+00:00
yes, i already do that 

## selsta | 2022-10-21T19:26:43+00:00
You did not. I only see that you posted a transaction id, no version, no wallet mode and no wallet restore height.

## Lowlay75 | 2022-10-21T19:28:57+00:00
oh, my bad I misunderstand. 

Version : 0.17.3.2-release
Wallet mode : Simple mode
Wallet Restore height : 2713588

## selsta | 2022-10-21T19:32:52+00:00
The problem is that you are using v0.17, monero had a network upgrade and you have to use v0.18.

## Lowlay75 | 2022-10-21T19:34:17+00:00
Thanks !
Can you explain me how can i update it ?
I'm on Linux 

## selsta | 2022-10-21T19:35:30+00:00
It depends on how you installed it in the first place. Did you download it from the website or using a package manager?

Does the GUI ask you to update on startup?

## Lowlay75 | 2022-10-21T19:38:23+00:00
The GUI don't ask to me for an update.
I use a virtual machine and GUI was already here and I already suspect the version to be bad, so i download on the website and now i have just a files called monero-wallet-gui but i can't open it 

## selsta | 2022-10-21T19:44:54+00:00
Try to double click on the .appimage file, and if that doesn't work start monero-wallet-gui from the command line.

## Lowlay75 | 2022-10-21T19:57:22+00:00
should i uninstall my actual monero gui ? 

## selsta | 2022-10-21T20:36:23+00:00
Delete the old version and download the new version.

## selsta | 2022-10-21T22:08:18+00:00
Closing this since there is no bug report here. If you continue to have issues you can comment.

## Lowlay75 | 2022-10-22T09:58:41+00:00
I got all my funds back thanks to the update

Thank you for your help !! 

# Action History
- Created by: Lowlay75 | 2022-10-21T19:02:20+00:00
- Closed at: 2022-10-21T22:08:18+00:00
