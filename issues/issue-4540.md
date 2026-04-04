---
title: Ledger Stax crash when using Monero wallet
source_url: https://github.com/monero-project/monero-gui/issues/4540
author: vampyren
assignees: []
labels: []
created_at: '2025-12-09T16:46:38+00:00'
updated_at: '2026-03-10T02:24:15+00:00'
type: issue
status: closed
closed_at: '2026-01-30T15:03:24+00:00'
---

# Original Description
Hi, 

As the title mentions i installed Monero wallet on my Ledger Stax and in 2 days it has crashed my stax in a way that it reset everything. Basically ledger reboots and the device has  resett. 
I need to input my 24 work to recover so its not just a wallet crash. And i only used monero wallet for both crashes. I think it was when it was idle and it went to sleep that caused the crash...i dont want to really force it to crash as its pretty scary. 

I'm using all the latest firmware and softare. 

OS version 1.9.0
Ledger Wallet 2.133.0
Monero wallet Ledger Version 2.1.2 • Ledger • 79 KB
Monero wallet Core 0.18.4.4-unknown (Qt 5.15.17)


# Discussion History
## selsta | 2025-12-09T16:49:27+00:00
You have to reach out to Ledger. Such a crash is a bug in their firmware.

Also can you confirm which operating system you are using?

@johnalanwoods did you see this behavior before?

## johnalanwoods | 2025-12-09T16:53:31+00:00
Nah never. Not seeing this. 

## selsta | 2025-12-09T17:43:55+00:00
It might be related to

https://github.com/LedgerHQ/app-monero/issues/167

## vampyren | 2025-12-09T21:22:58+00:00
Thanks for the replies. As for OS i'm using CachyOS only. I used BTC, ETH, AVAX, Sol and many other wallets and seen this type of reset one other time and that was when i was using Near wallet. 
And i'm sure if i go to Ledger they point me right back here. 
Without proof of what exactly goes wrong its like catch 22. 
I would think as a Monero user this will affect us more then it harms Ledger. They won't care. But we do want people to have a great experience using the hw wallet right? 
If you can debug and proof this is on them then it makes for a much stronger case for them to fix otherwise they can simply shrug it off as bad wallet (i think). 

By the way i save the log from ledger live app if that helps in anyway?

[ledgerwallet-logs-2025.12.09-21.12.28-b870b80-sanitized.txt](https://github.com/user-attachments/files/24064173/ledgerwallet-logs-2025.12.09-21.12.28-b870b80-sanitized.txt)


## nahuhh | 2025-12-09T21:44:05+00:00
Well monero's ledger implementation hasnt changed, and the fact that youve seen the same error when using NEAR leads me to believe that its a stax firmware issue

## vampyren | 2025-12-09T21:48:47+00:00
I'm not saying your wrong here, just that without evidence its hard to convince Ledger to do anything about it. I can file a bug there as well and see how that goes. I bet i know their answer or silence :) 
I'm hoping to see the wallet on Trezor 7 soon, maybe its more stable...

## selsta | 2025-12-09T23:17:53+00:00
@vampyren the next release will make sure that monero uses `hidapi 0.15.0`, that might fix the issue you are seeing. The fact that it wiped the device appears to be a serious bug in the firmware and has to be reported to Ledger directly, even if the issue gets fixed from our side.

## vampyren | 2025-12-10T08:26:34+00:00
Thank you @selsta ! 

Went to file a bug on Ledger's side but not sure where to do it....only one i found somewhat relevant is their live wallet but then again it ask for npm package and things i dont know about.  If you know where i should file please do let me know. 
i also email them at [hello@ledger.fr](mailto:hello@ledger.fr)

ps. i think i found someone with similar report here: https://github.com/LedgerHQ/app-monero/issues/104

Cheers!

<img width="855" height="372" alt="Image" src="https://github.com/user-attachments/assets/283971c3-87a1-4bc8-88b3-b4253751bf44" />

## selsta | 2026-01-30T15:03:04+00:00
This should not show up anymore with v0.18.4.5 due to updated hidapi.

Either way, the bug itself has to be fixed on Ledger's side so I'm closing this issue.

## vampyren | 2026-02-02T20:24:57+00:00
Thanks, downloaded today and trying it. ITs a very nasty bug. It dont just crash the app but the whole ledger so i need to initialize the ledger with 24 words so its scary. This should never happen no matter where the bug lies. 
I hope it dont happen. Thanks . 

## vampyren | 2026-03-09T22:05:03+00:00
Sadly i have already have had 3 crashes that forced my ledger to reset! This just happened now....Why does this only happen with monero? Is there something special about what is being executed? This is really serious. App crash is one thing, this crashes the whole thing. Please continue with this investigation. The problem remains. 
![Image](https://github.com/user-attachments/assets/d65e642b-72b9-402c-a5d1-c09673b0d542)

## selsta | 2026-03-10T00:48:18+00:00
Did Ledger reply to your email? This isn't something that can be fixed on our side as it's an issue with their application and firmware.

## vampyren | 2026-03-10T02:24:15+00:00
> Did Ledger reply to your email? This isn't something that can be fixed on our side as it's an issue with their application and firmware.

Sadly no :( 
Hoping once the support for new Trezor is done this works better. Thanks 

# Action History
- Created by: vampyren | 2025-12-09T16:46:38+00:00
- Closed at: 2026-01-30T15:03:24+00:00
