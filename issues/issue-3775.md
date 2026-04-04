---
title: macOS Monterey Error Messages
source_url: https://github.com/monero-project/monero-gui/issues/3775
author: mikev1963
assignees: []
labels: []
created_at: '2021-12-04T22:26:59+00:00'
updated_at: '2023-01-17T05:03:28+00:00'
type: issue
status: closed
closed_at: '2023-01-17T05:03:28+00:00'
---

# Original Description
I am receiving the following errors in my $HOME/Library/Logs/monero-wallet-gui.log:

```
2021-12-04 21:00:38.460	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1047	daemonBlockChainHeight: Failed to connect to daemon
2021-12-04 21:00:38.950	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1066	daemonBlockChainTargetHeight: Failed to connect to daemon
2021-12-04 21:00:38.951	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1047	daemonBlockChainHeight: Failed to connect to daemon
2021-12-04 22:08:28.609	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1047	daemonBlockChainHeight: Failed to connect to daemon
2021-12-04 22:08:29.002	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1066	daemonBlockChainTargetHeight: Failed to connect to daemon
2021-12-04 22:08:29.002	  0x700008ce3000	ERROR	WalletAPI	src/wallet/api/wallet.cpp:1047	daemonBlockChainHeight: Failed to connect to daemon
```

# Discussion History
## selsta | 2021-12-07T23:09:04+00:00
Do you run into any issues apart from these error messages?

## mikev1963 | 2021-12-09T19:19:34+00:00
I see this balance from the Monaro site:
![Monero](https://user-images.githubusercontent.com/10714291/145461544-7b9485f6-cb60-4ad4-be9a-56636ecfacdb.jpg)

but when I look at the wallet I have installed it shows zero balance.


## selsta | 2021-12-09T19:20:54+00:00
Did you get a payout from your pool? If yes, what's the transaction id?

## mikev1963 | 2021-12-09T19:21:58+00:00
How do I find out if I got a payout?  Im new to this.

Thanks
Mike

> On Dec 9, 2021, at 2:21 PM, selsta ***@***.***> wrote:
> 
> 
> Did you get a payout from your pool? If yes, what's the transaction id?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub <https://github.com/monero-project/monero-gui/issues/3775#issuecomment-990151049>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/ACRXZM5XYILGOORI5QGW7CLUQD6SBANCNFSM5JMBFEFQ>.
> Triage notifications on the go with GitHub Mobile for iOS <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675> or Android <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>. 
> 



## selsta | 2021-12-09T19:22:31+00:00
Contact your pool support.

# Action History
- Created by: mikev1963 | 2021-12-04T22:26:59+00:00
- Closed at: 2023-01-17T05:03:28+00:00
