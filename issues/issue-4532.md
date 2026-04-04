---
title: Ledger Flex Support
source_url: https://github.com/monero-project/monero-gui/issues/4532
author: HerMak56
assignees: []
labels: []
created_at: '2025-11-19T13:23:49+00:00'
updated_at: '2025-11-23T13:15:27+00:00'
type: issue
status: closed
closed_at: '2025-11-23T13:15:27+00:00'
---

# Original Description
Hello, I ve read that Ledger Flex now support monero. [https://www.getmonero.org/2025/10/08/monero-GUI-0.18.4.3-released.html](url)

I download GUI, CLI versions of monero app on Linux, Mac OS, Windows and I have same promlem - **Error: failed to generate new wallet: No device found**
Here my verison GUI: 
<img width="411" height="117" alt="Image" src="https://github.com/user-attachments/assets/4578bec6-5165-4057-8e79-c38179630247" />
Here error: 

<img width="923" height="627" alt="Image" src="https://github.com/user-attachments/assets/92b9feb0-5d69-4e24-be62-059aa4cccbc3" />

I launch monero app on ledger but nothing. Also I checked a several cabels - nothing. Ledger Live see my flex. I think this is a problem of software 

# Discussion History
## HerMak56 | 2025-11-19T13:24:43+00:00
On CLI verison I have this log: 
```
2025-11-19 13:01:04.608	E No device found
```

## HerMak56 | 2025-11-19T14:23:59+00:00
Also I forgot mentonied that I have Ledger OS 1.5.0

## nahuhh | 2025-11-19T14:30:42+00:00
Can you try the suggestion here: https://github.com/monero-project/monero-gui/issues/4438#issuecomment-2839593422

## HerMak56 | 2025-11-19T15:02:30+00:00
> Can you try the suggestion here: [#4438 (comment)](https://github.com/monero-project/monero-gui/issues/4438#issuecomment-2839593422)

Yes, before launch monero-gui I connect ledegr and then open a monero app on ledger 

## HerMak56 | 2025-11-19T15:20:38+00:00
Also I found same problem [https://github.com/LedgerHQ/app-monero/issues/163](url)

## kylecresta | 2025-11-19T15:51:20+00:00
I am having the same issue with the Monero GUI wallet not detecting my Ledger Flex since updating to 1.5.0

I cannot open my existing Monero waller, or create a new one.

I have Ledger Nano X that is not up to date and it is still working in the Monero GUI app without issue.

## HerMak56 | 2025-11-19T16:03:09+00:00
> I am having the same issue with the Monero GUI wallet not detecting my Ledger Flex since updating to 1.5.0
> 
> I cannot open my existing Monero waller, or create a new one.
> 
> I have Ledger Nano X that is not up to date and it is still working in the Monero GUI app without issue.

Look like a bug.....

## nahuhh | 2025-11-19T16:42:44+00:00
For some reason, its reported as working with feather wallet.

Lets see what ledger has to say. Thanks for opening issue there

https://github.com/LedgerHQ/app-monero/issues/163

## HerMak56 | 2025-11-20T09:43:30+00:00
Moreover I tried other client:

<img width="496" height="594" alt="Image" src="https://github.com/user-attachments/assets/b2115967-7724-4779-9f55-8896d249b5e9" />

Same problem

## HerMak56 | 2025-11-20T13:08:50+00:00
I write to Ledger Support and open a ticket: 

> Hi there,
>  
> Thanks for providing this information!
>  
> Rest assured our team is aware of this, we are investigating whether it is related to our recent OS update. We have also confirmed that the Flex is the only device that seems to be experiencing issues connecting. The Stax and all our earlier devices are working with Moreno perfectly as intended.
> 
> Although I am not able to give a direct timeframe, we should hopefully be able to find out more on this issue soon.



Seems like a bug, let's wait a response of Support...

## johnalanwoods | 2025-11-20T13:18:47+00:00
Right, they must have changed the USB identity or something like that in the recent update.

So it's a breaking change and up to the Monero wallet itself to fix.

Which is why it works over BT.


This has changed since they added the Gen5: https://github.com/LedgerHQ/ledger-live/blob/bd1b09970f2f5a27eb08352a67a73dfa2fce29f6/libs/ledgerjs/packages/devices/src/index.ts#L111


But I don't see anything that should affect the Flex:

Diff with develop: 

<img width="897" height="507" alt="Image" src="https://github.com/user-attachments/assets/812f5979-b1f5-4d31-84d6-91d72218413d" />

## HerMak56 | 2025-11-20T16:12:58+00:00
Also, I would like to metion, that using [other app](https://cakewallet.com) helps to create wallet on the phone. So sems that problem with monero GUI....

## HerMak56 | 2025-11-23T11:11:54+00:00
I new version of monero-app was realised and updated to 2.1.1. So I teested and it works fine with current version of monero gui @johnalanwoods @nahuhh 

## johnalanwoods | 2025-11-23T11:28:03+00:00
Nice!

## johnalanwoods | 2025-11-23T13:12:52+00:00
Confirmed issue resolved - @selsta, good to close this one friend.

# Action History
- Created by: HerMak56 | 2025-11-19T13:23:49+00:00
- Closed at: 2025-11-23T13:15:27+00:00
