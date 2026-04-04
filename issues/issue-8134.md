---
title: Issue Fixed
source_url: https://github.com/monero-project/monero/issues/8134
author: ghost
assignees: []
labels: []
created_at: '2022-01-07T18:25:38+00:00'
updated_at: '2022-01-09T07:31:23+00:00'
type: issue
status: closed
closed_at: '2022-01-09T07:20:06+00:00'
---

# Original Description


I have posted image proof I did not check transaction fee before sending however I have sent countless transactions with very low transaction fees instead of this one…


Can you lmk how this happened and or why? I’ve accepted I have lost the xmr but yeah… I’m willing to share the logs with the devs to see why this would happen prevent it from happening etc 

# Discussion History
## selsta | 2022-01-07T18:26:33+00:00
I need to know the IP of the remote node (I asked on Reddit about it)

## ghost | 2022-01-07T18:35:22+00:00
[1/7/22 6:33 PM] 2022-01-07 18:33:48.935 I Monero 'Oxygen Orion' (v0.17.2.0-release)
Height: 2532154/2532154 (100.0%) on mainnet, bootstrapping from 23.88.121.112:18089, local height: 620051 (24.5%), not mining, net hash 3.11 GH/s, v14, 0(out)+0(in) connections




that is what you requested I did not know your a dev t hanks for the help

## selsta | 2022-01-07T18:36:25+00:00
that's a completely different IP now :/ do you have the previous one?

## ghost | 2022-01-07T18:37:46+00:00
unfortunately just what i had posted on reddit, I am using monero on whonix so theirs that

## selsta | 2022-01-07T18:41:35+00:00
Ok, next time you see an extremely high fee, please go directly to Settings -> Log and post the output of `status` so that we can find out which node is responsible for this.

Currently you are the only transaction on the blockchain with a high fee so it isn't widespread yet.

## ghost | 2022-01-07T18:44:50+00:00
Hey thanks for the help I appreciate it. I don’t lie this is very disheartening for me and has pushed me away from monero and crypto altogether…

i appreciate the help nonetheless and support and that the devs are willing to help with this… that makes me happy and softens the blow a bit I certainly will…

i can show you transactions from like yesterday and days ago where transaction fees are low so I know this isn’t user error..

but thanks for the help :) 

## selsta | 2022-01-07T18:49:49+00:00
The fee / block was mined by MineXMR, I will contact them, maybe they can refund it :)

## ghost | 2022-01-07T18:53:02+00:00
Sure I would appreciate that greatly most definitely.. if they do I will be incredibly happy I will be like whoa like crazy the support up till now is amazing…

idk you you don’t know me, your a developer doijg this for free it’s clear what has happened isn’t user error but something else..

to want to go above and beyond and want to help me and even go as far as request a refund for me is amazing your a nice person..

Im just a random disabled combat veteran posting on the internet you bring a little
Faith to me thanks I’ll be check this email and thread for results..

your a great Dev selsta 

## selsta | 2022-01-07T19:01:40+00:00
It will probably take a bit until I can contact @xnbya (MineXMR admin). Can you post your XMR address here in the meantime?

## ghost | 2022-01-07T19:04:26+00:00
That is my xmr address I receive xmr for as well as the one I made with the transaction no worries, ill be keeping an eye on my email its cool i appreciate it regardless selsta. I'll keep the thread open until you come to a resolution refund or no refund :) 




## selsta | 2022-01-07T19:12:56+00:00
Though I don't know how quickly the pool distributes the block rewards. If they do it quickly then maybe they can't refund it anymore. Sorry, I didn't want to get your hopes up. Let's wait for @xnbya reply.

## xnbya | 2022-01-07T19:18:33+00:00
The block reward has already been distributed to miners, the pool won't be able to refund it I'm afraid.

## ghost | 2022-01-07T19:24:52+00:00
hey guys thats ok thanks for your help its much appreciated :) Again I have no idea why this happened.. I have a couple of transactions with incredibly low fees...

But I have never had this issue with bitcoin sneding transactions and certainly this one transaction with a 3.93xmr transaction fee has seriously made me weary of doing any cyrpto transactions..

Again I guess the name of the game is if your not present in the moment or paying attention then do not mess with cyrpto..

I dont ever mess with the settings.. but yes this has been a disheartening situation my friends.. I plan to not deal with cyrpto for a decent time atm..

3.93 xmr transaction fee for .34 transaction seems way to high and hopefully this is something that does not happen ever to anyone else.. it was 800 dollars approximately transaction fee for a 70 dollar transaction..

hopefully this doesnt happen to anyone else ever but I have just learned to always look at the transaction fee before sending..

thanks again for your help regardless its greatly appreciated.. ;) 

## selsta | 2022-01-07T19:32:37+00:00
I'm still trying to figure out why this happened and how we can avoid it in the future.

Couple ideas:

- Warn the user if the fee seems too high.
- Let GUI simple mode only connect to "trusted" remote node.

## ghost | 2022-01-07T20:52:09+00:00
Hey im very curious to the resolution of what will happen from here..

Like when you find out why how can you fix it etc?

Will you have a warning with monero about connecting to certain nodes?

Warning the user about transaction ids etc is great as well as connected to trusted nodes..

I wish I was paying attention more but I have so many transactions that have a low transaction fee..

What possibility how much control does an operator of a nefarious node have? Is it possible the transaction fee would have shown up as low and not the actual number? Like and got that way? 

## selsta | 2022-01-07T20:56:47+00:00
> Is it possible the transaction fee would have shown up as low and not the actual number

No, this is not possible. It would be visible on the confirmation screen. The fee gets calculated client side with data from the server.

## escapethe3RA | 2022-01-07T22:35:42+00:00
Posted a report on Monero Observer: https://www.monero.observer/pacificnwvet-pays-3.93-xmr-fee-0.34-xmr-transaction/

Hopefully you can recover at least some of the funds. @PacificNWVet

## Hueristic | 2022-01-08T00:38:03+00:00
No one using wallet in simple mode will have a use case to have a higher fee than transaction so a simple check should be installed (maybe just keep area greyed if out of bounds with popup stating why) for any wallet not in advanced mode.

## ghost | 2022-01-08T03:36:51+00:00
Hey someone from this dev team or someone from the xmrmine rig sent me the exact amount I lost in transaction fees.. I am truly blessed you guys are amazing.... Im not an emotional person.. but basically it had to be someone from here.. I already have a hard time from the holidays because of my mental health issues/pain issues from the military, but you guys have made my day and very happy..

What was going to be a bad day, and bad week for me, took a very nice turn.. you guys are awesome.. and my faith in the crypto community, particularly the xmr/monero community is amazing.. you guys went above and beyond to help me out i love you guys dearly for doing this for me.. I couldn't be happier that you guys helped me out.

I am incredibly blessed to have had you guys help me..

I will 100 percent be looking at transaction fees before sending and if it happens again I will certainly cancel the transaction and click on status for the log..

Thanks guys you guys are awesome :) 

## shopglobal | 2022-01-08T03:39:10+00:00
Happy new year!

On Fri, Jan 7, 2022, 10:37 PM PacificNWVet ***@***.***> wrote:

> Hey someone from this dev team or someone from the xmrmine rig sent me the
> exact amount I lost in transaction fees.. I am truly blessed you guys are
> amazing.... Im not an emotional person.. but basically it had to be someone
> from here.. I already have a hard time from the holidays because of my
> mental health issues/pain issues from the military, but you guys have made
> my day and very happy..
>
> What was going to be a bad day, and bad week for me, took a very nice
> turn.. you guys are awesome.. and my faith in the crypto community,
> particularly the xmr/monero community is amazing.. you guys went above and
> beyond to help me out i love you guys dearly for doing this for me.. I
> couldn't be happier that you guys helped me out.
>
> I am incredibly blessed to have had you guys help me..
>
> I will 100 percent be looking at transaction fees before sending and if it
> happens again I will certainly cancel the transaction and click on status
> for the log..
>
> Thanks guys you guys are awesome :)
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/8134#issuecomment-1007878121>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ADBQBZ7E37ZND5FRTSXIJFTUU6WOVANCNFSM5LPLUL5A>
> .
> Triage notifications on the go with GitHub Mobile for iOS
> <https://apps.apple.com/app/apple-store/id1477376905?ct=notification-email&mt=8&pt=524675>
> or Android
> <https://play.google.com/store/apps/details?id=com.github.android&referrer=utm_campaign%3Dnotification-email%26utm_medium%3Demail%26utm_source%3Dgithub>.
>
> You are receiving this because you are subscribed to this thread.Message
> ID: ***@***.***>
>


## ghost | 2022-01-09T07:20:06+00:00
thanks for the help guys and hope this gets fixed ;) thanks

# Action History
- Created by: ghost | 2022-01-07T18:25:38+00:00
- Closed at: 2022-01-09T07:20:06+00:00
