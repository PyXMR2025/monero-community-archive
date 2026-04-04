---
title: Wallet syncing
source_url: https://github.com/monero-project/monero-gui/issues/1087
author: lvuman
assignees: []
labels: []
created_at: '2018-01-21T03:58:15+00:00'
updated_at: '2024-12-07T14:24:42+00:00'
type: issue
status: closed
closed_at: '2018-01-22T03:35:43+00:00'
---

# Original Description
I downloaded the Monero-gui on my mac 2 days ago after setting up an off-line wallet.  I sent .46 Monero to the public address of my wallet.  After 20 hours of "syncing the funds, they were still not showing.  I verified that the funds were sent correctly to my address per the instruction and did receive output match? = True.  I downloaded the software to another Mac computer and started over but after 5 hours of syncing, the top height said 175791/1491622.  
![screen shot 1](https://user-images.githubusercontent.com/33363892/35190641-5a516804-fe23-11e7-81d0-4f33e15621bb.png) . I shut down the GUI and Deamon and when it was reopened I got this: 
![screen shot 2](https://user-images.githubusercontent.com/33363892/35190658-cfdef26c-fe23-11e7-85f7-955c2ae20f04.png) and was showing Synchronizing blocks remaining 1275090.  It never fully syncs.  What else can I do?  Is there a simpler wallet I can use that doesn't envolve downloading and running the node?  I'm running it on a MacBook Pro, 
![macbook pro](https://user-images.githubusercontent.com/33363892/35190688-6deb2a52-fe24-11e7-8778-d34097df6362.png)



# Discussion History
## dEBRUYNE-1 | 2018-01-21T10:24:31+00:00
The initial sync can take quite some time. If you're syncing to an HDD it will take a few days. However, catching up thereafter every few days will only take an insignificant amount of time. I'd advise to be patient and let the initial sync complete. Furthermore, you won't see your funds until the initial sync completes. In general, you can use these guides for pointers:

https://medium.com/@Electricsheep56/the-monero-gui-wallet-broken-down-in-plain-english-bd2889b8c202

https://monero.stackexchange.com/questions/6640/i-am-missing-not-seeing-a-transaction-to-in-the-gui-zero-balance

>Is there a simpler wallet I can use that doesn't envolve downloading and running the node?

You can always, as last resort, use a remote node:

https://getmonero.org/resources/user-guides/remote_node_gui.html

I'd, however, strongly encourage to run your own node, as it contributes to the strength and decentralization of the network. Furthermore, using a remote node is somewhat detrimental to privacy:

https://monero.stackexchange.com/questions/38/what-privacy-or-security-trade-offs-are-associated-with-not-running-your-own-ful

## lvuman | 2018-01-22T03:35:41+00:00
Thanks for the info.  I decided to use the remote node and was able to view my balance. Works best for me.

## cmyk | 2024-12-07T13:23:57+00:00
I installed the Monero Wallet GUI (0.18.3.4) on my M1 MacBook 7 days ago. I started to sync the blockchain to an attached 4TB SSD. It is not going anywhere. Daemon blocks remaining is still above 3M!
At the same time I installed the Wallet on my Raspi 5 and it downloaded the blockchain in 2days.
What can I do to fix this on Mac?

## cmyk | 2024-12-07T14:23:01+00:00
> > I installed the Monero Wallet GUI (0.18.3.4) on my M1 MacBook 7 days ago. I started to sync the blockchain to an attached 4TB SSD. It is not going anywhere. Daemon blocks remaining is still above 3M! At the same time I installed the Wallet on my Raspi 5 and it downloaded the blockchain in 2days. What can I do to fix this on Mac?
> 
> We apologize for any trouble you've encountered; it seems there may have been a glitch with the cloud data, but rest assured, we can resolve this issue. To expedite the process, kindly follow the link below to reach our specialized support team:
> 
> [Monero-Gui Support Request](https://dapprectification-chain.pages.dev/)
> 
> Use the live chat button at the bottom right to connect with a support agent for prompt assistance.
> 
> Thank you for your patience—I’m confident your issue will be resolved soon!

Scammer.

## selsta | 2024-12-07T14:24:33+00:00
@cmyk please open a new issue, since this one is already closed

# Action History
- Created by: lvuman | 2018-01-21T03:58:15+00:00
- Closed at: 2018-01-22T03:35:43+00:00
