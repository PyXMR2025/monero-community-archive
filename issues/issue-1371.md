---
title: Withdrew Monero XMR from Binance Exchange to my local Monero GUI wallet using
  wrong Payment ID
source_url: https://github.com/monero-project/monero-gui/issues/1371
author: fintechlim
assignees: []
labels:
- resolved
created_at: '2018-05-04T21:19:53+00:00'
updated_at: '2018-07-04T09:09:32+00:00'
type: issue
status: closed
closed_at: '2018-07-04T09:09:32+00:00'
---

# Original Description
I used the Payment ID from Monero Wallet GUI that was generated from the wallet. Plugged that into the Binance Withdraw of XMR using the correct address. The transaction completed but no coins showed up in wallet. After emails with Binance they said I used the wrong payment ID but had the correct address and they gave me the correct Payment ID but the transaction already completed.

I can view the transaction and decoded it using the my private view key on MoneroExplorer and can see the transaction and correct amount of funds and showed "ouput match = true" please see attachment but 
[MoneroFoundLostTransaction.docx](https://github.com/monero-project/monero-gui/files/1975925/MoneroFoundLostTransaction.docx)
[MoneroFoundLostTransaction.docx](https://github.com/monero-project/monero-gui/files/1975929/MoneroFoundLostTransaction.docx)

But never showed up Monero GUI Wallet. I was told this would fix it but it didn't.

I have tried:
1) Created new wallet using same seed as old wallet using localhost sync
2) Created new wallet using same seed as old wallet using remote node.moneroworld.com  sync 
Nothing is working.

TX ID:   b2b2df0f1ae824a4d5eec82e212b7d5eb23a673eed2bb833afe38578546b5add
Wallet Payment Key Used (bad):   20197c09a0b58da9
My Public Send Address (good):  41ngmusSp7mbhWbdwWUEsj6bVSaaJQsh94LJdwVKUBRKD34ZYntaSDTAefzDAJo3jkPbk3b5r8QxLN2FVpRyRLsUDZ2Ycmr
Block Height: 1565673

Binance said I should have used this Payment ID: dee6dfa4a67f1b8e5b34f4b420506da32d2d1d4da0be47b4805fa5618c174f05

Amount: Completed        XMR    5.52529256         2018-05-03 13:48:52

Please Help!

# Discussion History
## dEBRUYNE-1 | 2018-05-05T10:04:31+00:00
Could you post the full `Show status` output (on the `Settings` page of the GUI)? Also, what is the `Wallet creation height` (on the `Settings` page under `Debug info`)? 

## fintechlim | 2018-05-05T14:02:12+00:00
I reran the remote node sync and the funds appeared thank you for your support! All good! One question though, can I switch back to local mode because remote is slow but I don't want to chance losing the funds again, thanks again! Sincerely, Graham P. RiveraFinTech Limited 8(a)/SWaM/DBME13711 Solstice CloseMidlothian, VA 23113Tel: (804) 536-3200Fax: (804) 464-2439http://www.fintechlimited.com CONFIDENTIALITY NOTICE  The information in this email and any attachments may contain legally privileged, proprietary and confidential information that is intended for a particular recipient. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, retention or use of the contents of this e-mail information is prohibited. When addressed to FinTech Limited's clients or vendors, any information contained in this e-mail is subject to the terms and conditions in the governing contracts that are currently in place. If you have received this e-mail in error, please immediately notify us by telephone or by return e-mail, and delete the e-mail.


      From: dEBRUYNE-1 <notifications@github.com>
 To: monero-project/monero-gui <monero-gui@noreply.github.com> 
Cc: fintechlim <graham@fintechlimited.com>; Author <author@noreply.github.com>
 Sent: Saturday, May 5, 2018 6:04 AM
 Subject: Re: [monero-project/monero-gui] Withdrew Monero XMR from Binance Exchange to my local Monero GUI wallet using wrong Payment ID (#1371)
   
Could you post the full Show status output (on the Settings page of the GUI)? Also, what is the Wallet creation height (on the Settings page under Debug info)?—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub, or mute the thread.  

   

## dEBRUYNE-1 | 2018-05-05T14:28:59+00:00
@fintechlim - I first need to verify your full `Show status` output before I can safely let you switch back to the local node. 

## fintechlim | 2018-05-05T15:07:35+00:00
Here you go. I tried to send 0.5 XMR out to Kraken when I was in remote sync mode hung for a while then failed??? Kraken doesnt require a payment ID. Trying local mode now. Sincerely, Graham P. RiveraFinTech Limited 8(a)/SWaM/DBME13711 Solstice CloseMidlothian, VA 23113Tel: (804) 536-3200Fax: (804) 464-2439http://www.fintechlimited.com CONFIDENTIALITY NOTICE  The information in this email and any attachments may contain legally privileged, proprietary and confidential information that is intended for a particular recipient. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, retention or use of the contents of this e-mail information is prohibited. When addressed to FinTech Limited's clients or vendors, any information contained in this e-mail is subject to the terms and conditions in the governing contracts that are currently in place. If you have received this e-mail in error, please immediately notify us by telephone or by return e-mail, and delete the e-mail.


      From: dEBRUYNE-1 <notifications@github.com>
 To: monero-project/monero-gui <monero-gui@noreply.github.com> 
Cc: fintechlim <graham@fintechlimited.com>; Mention <mention@noreply.github.com>
 Sent: Saturday, May 5, 2018 10:29 AM
 Subject: Re: [monero-project/monero-gui] Withdrew Monero XMR from Binance Exchange to my local Monero GUI wallet using wrong Payment ID (#1371)
   
@fintechlim - I first need to verify your full Show status output.—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.  

   

## fintechlim | 2018-05-05T15:08:33+00:00
Cant do local mode funds disappeared???? Changing back to remote mode. Sincerely, Graham P. RiveraFinTech Limited 8(a)/SWaM/DBME13711 Solstice CloseMidlothian, VA 23113Tel: (804) 536-3200Fax: (804) 464-2439http://www.fintechlimited.com CONFIDENTIALITY NOTICE  The information in this email and any attachments may contain legally privileged, proprietary and confidential information that is intended for a particular recipient. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, retention or use of the contents of this e-mail information is prohibited. When addressed to FinTech Limited's clients or vendors, any information contained in this e-mail is subject to the terms and conditions in the governing contracts that are currently in place. If you have received this e-mail in error, please immediately notify us by telephone or by return e-mail, and delete the e-mail.


      From: dEBRUYNE-1 <notifications@github.com>
 To: monero-project/monero-gui <monero-gui@noreply.github.com> 
Cc: fintechlim <graham@fintechlimited.com>; Mention <mention@noreply.github.com>
 Sent: Saturday, May 5, 2018 10:29 AM
 Subject: Re: [monero-project/monero-gui] Withdrew Monero XMR from Binance Exchange to my local Monero GUI wallet using wrong Payment ID (#1371)
   
@fintechlim - I first need to verify your full Show status output.—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.  

   

## dEBRUYNE-1 | 2018-05-06T15:26:26+00:00
>when I was in remote sync mode hung for a while then failed???

Have you tried using a different remote node?

>Cant do local mode funds disappeared????

Please ignore that for a bit and post the full `Show status` output whilst being in local mode. 

## fintechlim | 2018-05-06T15:54:13+00:00
Remote mode finally worked just slower, local mode does not. You can close the ticket and thanks for your help! Sincerely, Graham P. RiveraFinTech Limited 8(a)/SWaM/DBME13711 Solstice CloseMidlothian, VA 23113Tel: (804) 536-3200Fax: (804) 464-2439http://www.fintechlimited.com CONFIDENTIALITY NOTICE  The information in this email and any attachments may contain legally privileged, proprietary and confidential information that is intended for a particular recipient. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, retention or use of the contents of this e-mail information is prohibited. When addressed to FinTech Limited's clients or vendors, any information contained in this e-mail is subject to the terms and conditions in the governing contracts that are currently in place. If you have received this e-mail in error, please immediately notify us by telephone or by return e-mail, and delete the e-mail.


      From: dEBRUYNE-1 <notifications@github.com>
 To: monero-project/monero-gui <monero-gui@noreply.github.com> 
Cc: fintechlim <graham@fintechlimited.com>; Mention <mention@noreply.github.com>
 Sent: Sunday, May 6, 2018 11:26 AM
 Subject: Re: [monero-project/monero-gui] Withdrew Monero XMR from Binance Exchange to my local Monero GUI wallet using wrong Payment ID (#1371)
   

when I was in remote sync mode hung for a while then failed???
Have you tried using a different remote node?
Cant do local mode funds disappeared????
Please ignore that for a bit and post the full Show status output whilst being in local mode.—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub, or mute the thread.  

   

## dEBRUYNE-1 | 2018-07-04T08:43:20+00:00
+resolved

# Action History
- Created by: fintechlim | 2018-05-04T21:19:53+00:00
- Closed at: 2018-07-04T09:09:32+00:00
