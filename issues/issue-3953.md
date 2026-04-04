---
title: XMR was lost after trying to send to another wallet
source_url: https://github.com/monero-project/monero-gui/issues/3953
author: xmr2206
assignees: []
labels: []
created_at: '2022-06-26T19:40:02+00:00'
updated_at: '2024-08-29T10:08:16+00:00'
type: issue
status: closed
closed_at: '2023-01-18T15:11:44+00:00'
---

# Original Description
A very strange situation has happened. I tried to send my XMR to my another wallet but got a double spend error. Then immediately tried again and got the same error. I wanted to try for the third time, but the GUI hung on the commission calculation and I moved away from the computer. When I returned the next day, I saw that the XMR had been sent but not received by the recipient. The sender address was not specified in the details of the operation, I do not see to whom the XMR were sent. The sender field is set to **unknown recipient**. And when I asked for confirmation, I got a long string that started with **SpendProofV1**ZNDb...

I tried to check the operation through https://xmrchain.net/myoutputs - but it is clear that the recipient did not receive the money (I used transaction hash and Recipient Address and private viewkey)

Also I will trigger a wallet refresh from scratch but nothing happened.

Can anyone help me?

GUI version: 0.17.3.2-unknown (Qt 5.15.3)
Embedded Monero version: 0.17.3.2-unknown
Wallet restore height: 1446091
Wallet mode: Advanced mode (Remote node)
Graphics mode: OpenGL

# Discussion History
## selsta | 2022-06-26T19:44:55+00:00
Can you post a screenshot from the "Transactions" section in the GUI and also post your transaction id?

Which remote node were you using?

## xmr2206 | 2022-06-27T06:48:32+00:00
> Can you post a screenshot from the "Transactions" section in the GUI and also post your transaction id?
> 
> Which remote node were you using?

![image](https://user-images.githubusercontent.com/108237234/175876671-9d22c7dd-f88c-43a4-b72f-a2abef98ff67.png)

Transaction Id is e474a49ba3836a4fa21501fc9d3460e199c8d54bc5bea266820a489de2a926f7

remote node: node.moneroworld.com:18089


## plowsof | 2022-06-27T21:02:24+00:00
Triggering a wallet refresh will remove the recipient address / replace it with 'Unknown Recipient'. You have confirmed using xmrchain.net that you sent the funds to another address.

## xmr2206 | 2022-06-28T13:55:04+00:00
Are there any ways to find out which wallet the XMR was sent to, if I have all access and keys, as well as logs? I don't understand where the tokens could have been sent if the address has to be exact and not a junk character set that could be causing the error.

In my case, the money is 100% gone from my wallet. I could not specify an address other than my other wallet or the same wallet from which I sent (I copied the address from the address book, where I had both addresses recorded).

Could it be the reason for the disappearance of the money that I indicated the same address from which I sent?

## selsta | 2022-06-28T23:29:59+00:00
Can you use `88.198.199.23:18081` as your remote node (it's hosted by me) and then restore all wallets you have from seed with a restore height than is lower than 2652820? You don't have to restore the wallet where you sent the transaction from.

## xmr2206 | 2022-06-29T07:07:57+00:00
Probably I figured out what happened. My seed phrase was compromised via wallet.mymonero.com where I had the misfortune to go some time ago. The phrase Unknown Recipient also indicates that the transaction was not made from my wallet.

Yesterday I did a test, sent XMR to my wallet and they were also transferred by someone else. Someone monitors my wallet and initiates transactions as soon as XMR arrives there. The first time it took 2 hours. Last test time - around 11 hours.

## selsta | 2022-06-29T10:25:53+00:00
Is this the same seed you used on MyMonero a while ago? Or could your whole computer be compromised?

But yes, what you are saying seems likely. Someone is monitoring and moving out the funds in your wallet :/

## kongkeed | 2024-08-29T10:08:15+00:00
everybody listen to me       when COPY ADDRESS  please do  not copy the whole in one time it happen to another always    i  do HALF COPY and replace in same  place    never wrong address  can use all kind of wallet  address

# Action History
- Created by: xmr2206 | 2022-06-26T19:40:02+00:00
- Closed at: 2023-01-18T15:11:44+00:00
