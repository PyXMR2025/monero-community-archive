---
title: funds lost!!!
source_url: https://github.com/monero-project/monero/issues/8440
author: dance88
assignees: []
labels: []
created_at: '2022-07-17T17:06:49+00:00'
updated_at: '2023-06-06T01:35:12+00:00'
type: issue
status: closed
closed_at: '2023-06-06T01:35:12+00:00'
---

# Original Description
I transferred funds from one web wallet[xmrwallet.Com] to another,

but the funds haven't arrived,

But the XMR in my wallet has been deducted,


<img width="693" alt="1" src="https://user-images.githubusercontent.com/109477764/179416719-d77b0e6c-3e71-45d4-a65b-2ca03c640fc0.PNG">


When I checked the transaction id[00a888c91b0f6cceb8e2a7d2fc1a93dd00253d53d6226c74604399b0d51cf0a1] at xmrchain, 



<img width="1714" alt="2" src="https://user-images.githubusercontent.com/109477764/179416731-d0b0b94d-fcc2-48ee-bd55-8ebf6531a8a8.PNG">



After entering the wallet address and private viewkey in the Decode outputs option, the returned result is as follows,

<img width="1533" alt="3" src="https://user-images.githubusercontent.com/109477764/179416737-1a5da0ad-c130-4205-8d02-b7a4e2a68b1b.PNG">


I tried using Multiple remote node to restore the height before the transaction, but it didn't work,

address: 88.198.199.23
port: 18081

address: node.supportxmr.com
port: 18081

address: 78.47.80.55
port: 18081

address: node.community.rino.io
port: 18081







#### How To get my XMR back?

#### Please Help Me.

# Discussion History
## selsta | 2022-07-17T17:25:36+00:00
Your screenshot and your text shows a different transaction id, starting with 00a88, or what is that?

Are you the one who made the transaction on that exact date?

## dance88 | 2022-07-18T00:10:17+00:00
> Your screenshot and your text shows a different transaction id, starting with 00a88, or what is that?
> 
> Are you the one who made the transaction on that exact date?

Sorry, the transaction id in the text is wrong, I have changed it, the correct transaction id is: 00a888c91b0f6cceb8e2a7d2fc1a93dd00253d53d6226c74604399b0d51cf0a1

## SChernykh | 2022-07-18T05:33:37+00:00
xmrwallet[dot]com is a known scam: https://www.reddit.com/r/Monero/comments/jh15e3/psa_xmrwalletcom_is_a_scam_who_steals_your_funds/
You've got scammed.

## dance88 | 2022-07-18T08:16:05+00:00
> xmrwallet[dot]com is a known scam: https://www.reddit.com/r/Monero/comments/jh15e3/psa_xmrwalletcom_is_a_scam_who_steals_your_funds/ You've got scammed.

I've used this web wallet many times, and it worked until now,

and I checked other successful transactions,

After entering the wallet address and private viewkey in the Decode outputs option, The results of Decode outputs look different


<img width="1586" alt="5" src="https://user-images.githubusercontent.com/109477764/179470845-08a01db3-0cc0-4448-8549-a75538c4a782.PNG">



## SChernykh | 2022-07-18T08:44:55+00:00
Which means you actually sent your XMR to a different address. Maybe you have clipboard hijack malware on your PC.

## dance88 | 2022-07-18T10:26:46+00:00
> Which means you actually sent your XMR to a different address. Maybe you have clipboard hijack malware on your PC.

I can be sure that my pc is not infected with a hijack malware

## SChernykh | 2022-07-18T10:54:56+00:00
But your screenshot in the first post shows that XMR were sent to some other address. If viewkey doesn't decode any output, it went somewhere else.

## selsta | 2022-07-18T10:59:09+00:00
You didn't answer my question. Did you send those funds at the timestamp yourself? Or did you log into your wallet and there was an outgoing transaction?

Also on IRC you said you didn't send these funds to yourself so how do you have the view key?

## dance88 | 2022-07-18T12:44:16+00:00
> You didn't answer my question. Did you send those funds at the timestamp yourself? Or did you log into your wallet and there was an outgoing transaction?
> 
> Also on IRC you said you didn't send these funds to yourself so how do you have the view key?

I recharge funds to my own Binance account via xmrwallet,

view key from xmrwallet[.]com----account----View Key (Private).
<img width="744" alt="6" src="https://user-images.githubusercontent.com/109477764/179513778-276f349b-9be4-4841-8a9f-69d1dbcf0573.PNG">



## nmateo | 2022-07-18T12:59:15+00:00
As stated above, multiple people have already reported lost funds using xmrwallet[dot]com, you should use another wallet, like official GUI or cake.

## SChernykh | 2022-07-18T13:00:09+00:00
> I recharge funds to my own Binance account via xmrwallet,

So you sent fund from xmrwallet to Binance? Then you can't use the viewkey from xmrwallet to check Binance's wallet, it doesn't work this way.

## selsta | 2022-07-18T13:00:29+00:00
Yes, the receiver view key is required, not the sender.

## SChernykh | 2022-07-18T13:02:38+00:00
Hmm, there's also "Your Seed" on that screenshot - you can use it to restore your wallet in the official CLI or GUI wallet.

## dance88 | 2022-07-18T13:15:53+00:00
> Yes, the receiver view key is required, not the sender.

I don't quite understand,Shouldn't I enter my address and key in the Decode option?

## selsta | 2022-07-18T13:16:45+00:00
No. The receiver has to enter their address and their view key.

## dance88 | 2022-07-18T13:19:28+00:00
> Hmm, there's also "Your Seed" on that screenshot - you can use it to restore your wallet in the official CLI or GUI wallet.

I restored the mnemonic in the gui wallet,
got the same result.

## dance88 | 2022-07-18T14:04:50+00:00



> No. The receiver has to enter their address and their view key.

How can I check if my transfer was successful? I have no way to get the Binance view key, there is only one xmr recharge 
 address.

## SamsungGalaxyPlayer | 2022-07-21T14:18:44+00:00
This is an issue tracker, not a help desk for third party wallets. Please try asking for help in https://reddit.com/r/MoneroSupport

# Action History
- Created by: dance88 | 2022-07-17T17:06:49+00:00
- Closed at: 2023-06-06T01:35:12+00:00
