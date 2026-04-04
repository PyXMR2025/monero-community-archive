---
title: 'Funds transfer not successful, Daemon fully synched  '
source_url: https://github.com/monero-project/monero-gui/issues/2938
author: Ommy77
assignees: []
labels: []
created_at: '2020-06-08T11:32:36+00:00'
updated_at: '2020-06-29T22:04:36+00:00'
type: issue
status: closed
closed_at: '2020-06-29T22:04:35+00:00'
---

# Original Description
On 2020/05/04 10:52am CEST I sent 2.19990000 XMR from my Bittrex acc to my Nano S. The money has still not showing in my Gui wallet despite the wallet and Daemon being fully synched. Bittrex is no longer showing the XMR in my acc and says that the withdrawl was successful. Ive tried resynching the wallet a number of times now and I am still not seeing my funds.

Can someone help? 

![IMG_3387](https://user-images.githubusercontent.com/43322701/84025781-70ba6200-a98c-11ea-9f72-35ba6c8e6ccb.jpg)


# Discussion History
## selsta | 2020-06-08T11:33:45+00:00
What wallet mode are you using? You can check in Settings -> Info.

## Ommy77 | 2020-06-08T11:46:26+00:00
<img width="511" alt="Screen Shot 2020-06-08 at 13 42 28" src="https://user-images.githubusercontent.com/43322701/84026920-6ef19e00-a98e-11ea-8e10-31a287d896f0.png">


## selsta | 2020-06-08T11:47:55+00:00
You are using extremely outdated software. Update to v0.16 and try again. You will also have to update your Ledger firmware and monero app.

## Ommy77 | 2020-06-08T11:49:35+00:00
Ok , once I update, should I be able to see the funds?

## selsta | 2020-06-08T11:50:24+00:00
Yes.

## Ommy77 | 2020-06-08T11:51:48+00:00
K, cheers. I'll give that a go. 

## selsta | 2020-06-08T12:13:15+00:00
It might take a while to sync up when you update.

## Ommy77 | 2020-06-08T18:12:37+00:00
Hi,
I downloaded the latest version, and after signing in, I had this circling for 2 hours with no change. Does this sound right to you? I eventually had to stop it, should I have waited longer?
Thx

<img width="835" alt="Screen Shot 2020-06-08 at 14 35 30" src="https://user-images.githubusercontent.com/43322701/84065195-3e2c5b80-a9c4-11ea-83a1-43796c6da9ec.png">



## selsta | 2020-06-08T18:13:32+00:00
Did you export the view key on your Ledger?

## Ommy77 | 2020-06-08T18:14:26+00:00
yes

## selsta | 2020-06-08T18:17:04+00:00
Which monero ledger app version do you have? Also can you try again and make sure to look on the Ledger in case it requires input?

## Ommy77 | 2020-06-08T18:18:49+00:00
ok, Ill try again. Im about an hour away from home so I will update later.
Thx.

## Ommy77 | 2020-06-29T22:00:30+00:00
Hello,
Me again. I think I'm doing something wrong at this point. I updated the firmware on my ledger and I spent the last two days syching everything in the Monero wallet and I still see a zero balance in my Monero wallet. The Monero wallet app I have is 1.6.0.
Is there something else I can try?
Thanks in advance :) 

## Ommy77 | 2020-06-29T22:03:59+00:00
Hello,

Me again again :)

Just logged out of the wallet and back in and my funds are now showing. 

Really appreciate your help. Thanks a million :)

## selsta | 2020-06-29T22:04:35+00:00
@Ommy77 Good to hear. If you are having a problem in the future you can open a new issue or ask on Reddit / Stackexchange.

# Action History
- Created by: Ommy77 | 2020-06-08T11:32:36+00:00
- Closed at: 2020-06-29T22:04:35+00:00
