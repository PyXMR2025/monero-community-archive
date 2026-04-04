---
title: Ledger Nano-X - data lost after update
source_url: https://github.com/monero-project/monero-gui/issues/3671
author: Stenzl
assignees: []
labels: []
created_at: '2021-08-20T11:52:28+00:00'
updated_at: '2021-08-26T12:11:34+00:00'
type: issue
status: closed
closed_at: '2021-08-26T12:11:34+00:00'
---

# Original Description
My Nano-X lost his Monero account data during update.

How to set up the account again with:

- 24 Electrum words passphrase (from Nano-X)

- Monero account number

- all key except ptivate send key (lost on Ledger Nano-X due to update)

Thanks for reply!

# Discussion History
## selsta | 2021-08-20T16:32:05+00:00
Do you still have your Ledger seed? If yes, set up your Ledger with the seed and download the monero app using Ledger Live.

## Stenzl | 2021-08-21T06:26:49+00:00
Thank You!

 

I already did that, but received a different Monero account number on the Ledger.

 

How to bring the original account number to the Ledger?

 

Best regards

 

Bernhard

 

Von: selsta ***@***.***> 
Gesendet: Freitag, 20. August 2021 18:32
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Do you still have your Ledger seed? If yes, set up your Ledger with the seed and download the monero app using Ledger Live.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-902814466> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2J2I4DL4SXBFJSNFPDT5Z7RDANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2NB65TUE25ZZSED63DT5Z7RDA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGXH5WAQ.gif> 



## selsta | 2021-08-23T14:03:56+00:00
Did you select account #0 and mainnet on your Ledger monero app settings? Did you use a passphrase?

## Stenzl | 2021-08-23T15:16:17+00:00
Yes, these are standard.

 

Additionally it says ´Electrum seed NOTSET´.

 

Is it principally possible to feed the original Monero account number to the Ledger?

 

Von: selsta ***@***.***> 
Gesendet: Montag, 23. August 2021 16:04
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Did you select account #0 and mainnet on your Ledger settings?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-903802764> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2NR6YT3TGG76QUX2XTT6JINPANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2PAKDH2NGRR7PVGG5TT6JINPA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGXPO7DA.gif> 



## Stenzl | 2021-08-24T14:56:57+00:00
Hi, checked again.

 

The Monero-address on Leger is CORRECT, it is the old wallet address.

 

Tried to restore wallet, but received a failure message from GUI.

 

Where ist he problem?

 

Thanks for Your help.

 

Stenzl

 

Von: ***@***.*** ***@***.***> 
Gesendet: Montag, 23. August 2021 17:16
An: 'monero-project/monero-gui' ***@***.***>
Betreff: AW: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Yes, these are standard.

 

Additionally it says ´Electrum seed NOTSET´.

 

Is it principally possible to feed the original Monero account number to the Ledger?

 

Von: selsta ***@***.*** ***@***.***> > 
Gesendet: Montag, 23. August 2021 16:04
An: monero-project/monero-gui ***@***.*** ***@***.***> >
Cc: Stenzl ***@***.*** ***@***.***> >; Author ***@***.*** ***@***.***> >
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Did you select account #0 and mainnet on your Ledger settings?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-903802764> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2NR6YT3TGG76QUX2XTT6JINPANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2PAKDH2NGRR7PVGG5TT6JINPA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGXPO7DA.gif> 



## selsta | 2021-08-24T14:57:46+00:00
You need to post the exact error / failure message.

## Stenzl | 2021-08-24T15:20:40+00:00
Changed input language from German to English:

 

<create a new wallet from hardware>

 

<restore a wallet from device>

 

<Ledger Nano S/X>

 

<2021-03-09> (full node is synchronized)

 

path to old Ledger keys opened

 

Ledger: account 0, main network, ELECTRUM SEED NOTSET

 

Export view key <accept>

 

<Password set>

 

<create wallet>

 

ERROR. Failed to store the wallet

 

?

 

Von: selsta ***@***.***> 
Gesendet: Dienstag, 24. August 2021 16:58
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

You need to post the exact error / failure message.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-904717723> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2PUOTEXEGJIDO7IKSTT6OXPJANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2IIH5KGMPCHOAAADM3T6OXPJA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGXWOLGY.gif> 



## selsta | 2021-08-24T15:21:47+00:00
Which OS are you using? It has problems storing the wallet on your computer, could be an permission issue.

## Stenzl | 2021-08-25T05:56:23+00:00
It is Windows 10.

 

Maybe the key-file to open the account in GUI has to be renewed?

 

Von: selsta ***@***.***> 
Gesendet: Dienstag, 24. August 2021 17:22
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Which OS are you using? It has problems storing the wallet on your computer, could be an permission issue.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-904738544> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2MDRU4224AGZXIAHWDT6O2JLANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2KTKHWGMJQ5CFOU3DLT6O2JLA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGXWTN4A.gif> 



## selsta | 2021-08-25T13:32:54+00:00
Do you have a different computer to test this?

## Stenzl | 2021-08-25T14:34:50+00:00
No – not with full node.

 

Von: selsta ***@***.***> 
Gesendet: Mittwoch, 25. August 2021 15:33
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Do you have a different computer to test this?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-905505421> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2IZFGRUIL6O7QVEECDT6TWJDANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2NB2Q5FUB6QJJTHJPDT6TWJDA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGX4OVDI.gif> 



## selsta | 2021-08-25T14:48:37+00:00
Full or remote node doesn't matter currently. I just want to see if you can create the wallet on a different computer.

Currently it fails because something is blocking the GUI from creating a wallet (anti virus maybe).

Did you use the installer or the .zip when installing the GUI? I would try the installer from here, it can fix permission issues: https://www.getmonero.org/downloads/

## Stenzl | 2021-08-25T15:20:28+00:00
Now I resetted the Ledger again – 24 words phrase – again the wrong account number. The error message of GUI states, that Ledger has the wrong account number. So GUI verifies correctly.

 

Is there any other way to access my Monero account, despite the damned Ledger?

 

To remember: the private spend key was lost on Ledger due to update…

 

Von: selsta ***@***.***> 
Gesendet: Mittwoch, 25. August 2021 16:49
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

Full or remote node doesn't matter currently. I just want to see if you can create the wallet on a different computer.

Currently it fails because something is blocking the GUI from creating a wallet (anti virus maybe).

Did you use the installer or the .zip when installing the GUI? I would try the installer from here, it can fix permission issues: https://www.getmonero.org/downloads/

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-905569732> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2IMKPCYVF4HQIO6UPLT6T7FDANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2J4VZBCSYB2VSZA553T6T7FDA5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGX46LRA.gif> 



## selsta | 2021-08-25T15:23:15+00:00
> The Monero-address on Leger is CORRECT, it is the old wallet address.

Here you said the monero address on Ledger is correct. Is this still the case or not anymore?

## Stenzl | 2021-08-25T15:37:42+00:00
It is NOT CORRECT. And that is the reason why GUI denies access.

 

Von: selsta ***@***.***> 
Gesendet: Mittwoch, 25. August 2021 17:23
An: monero-project/monero-gui ***@***.***>
Cc: Stenzl ***@***.***>; Author ***@***.***>
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

The Monero-address on Leger is CORRECT, it is the old wallet address.

Here you said the monero address on Ledger is correct. Is this still the case or not anymore?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-905605684> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2I5IK7BCCPD74VUYQLT6UDG3ANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2PTZLUDSB44EMYML53T6UDG3A5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGX5HENA.gif> 



## Stenzl | 2021-08-26T08:38:54+00:00
I found the problem. The correct account was stored on Ledger as account #1, account #0 is different. So GUI denied.

 

With account #1 I could restore my Monero.

 

Thank You for Your assistance and Your patience with my limited understanding oft he interrelations!

 

Von: ***@***.*** ***@***.***> 
Gesendet: Mittwoch, 25. August 2021 17:38
An: 'monero-project/monero-gui' ***@***.***>; 'monero-project/monero-gui' ***@***.***>
Cc: 'Author' ***@***.***>
Betreff: AW: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

It is NOT CORRECT. And that is the reason why GUI denies access.

 

Von: selsta ***@***.*** ***@***.***> > 
Gesendet: Mittwoch, 25. August 2021 17:23
An: monero-project/monero-gui ***@***.*** ***@***.***> >
Cc: Stenzl ***@***.*** ***@***.***> >; Author ***@***.*** ***@***.***> >
Betreff: Re: [monero-project/monero-gui] Ledger Nano-X - data lost after update (#3671)

 

The Monero-address on Leger is CORRECT, it is the old wallet address.

Here you said the monero address on Ledger is correct. Is this still the case or not anymore?

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3671#issuecomment-905605684> , or unsubscribe <https://github.com/notifications/unsubscribe-auth/AVI6V2I5IK7BCCPD74VUYQLT6UDG3ANCNFSM5CQFLT4Q> .
Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>  or Android <https://play.google.com/store/apps/details?id=com.github.android&utm_campaign=notification-email> .  <https://github.com/notifications/beacon/AVI6V2PTZLUDSB44EMYML53T6UDG3A5CNFSM5CQFLT42YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOGX5HENA.gif> 



## selsta | 2021-08-26T12:11:34+00:00
Glad you figured this out :)

# Action History
- Created by: Stenzl | 2021-08-20T11:52:28+00:00
- Closed at: 2021-08-26T12:11:34+00:00
