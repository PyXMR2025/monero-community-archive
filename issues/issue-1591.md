---
title: 'Algorithm Request: Cryptonight Dynamic'
source_url: https://github.com/xmrig/xmrig/issues/1591
author: cogitocat
assignees: []
labels:
- wontfix
created_at: '2020-03-10T14:00:27+00:00'
updated_at: '2020-08-29T04:50:31+00:00'
type: issue
status: closed
closed_at: '2020-08-29T04:50:31+00:00'
---

# Original Description
Hello,

I'd like to request that crytonight dynamic be added.  This is particularly used by blur (https://blur.cash) and has good development happening.

https://github.com/blur-network/blur


# Discussion History
## fart-master | 2020-03-14T03:18:21+00:00
https://github.com/fart-master/blur-miner

Already exists. Nvidia only. AMD needs some love, but I don't have the hardware

## who-biz | 2020-03-20T21:46:49+00:00
Official support by XMRig would be great.  Happy to help out with the code, if desired.

## who-biz | 2020-03-20T21:54:34+00:00
I already spoke with bendr0id over at XMRigCC about official support for CN-Dynamic as well. 

You’ll find pretty well annotated code here, on the algorithm: https://github.com/blur-network/blur/blob/master/src/cryptonote_basic/cryptonote_format_utils.cpp#L945

Scratchpad is 1MB, and iterations within CNv2 are varied according to the above calculations in `get_block_longhash`. All values for those calculations can be grabbed directly from the block header. 

Don’t mind fart-master. He likes to follow our team around... But feel free to use his work as a reference implementation, too. However, note that his modifications, specifically within `rapidjson`, don’t appear to play nicely with our `epee` library.

All of our miners run at least one full node. So pool/stratum support would not be necessary.

## fart-master | 2020-03-20T22:49:59+00:00
So why not just submit a PR if you are happy to help with code? The code already exists and is not lengthy, just put it into a PR instead of asking people to do it for you. Stratum support is not something you have to "add" if you support this algorithm it is supported via stratum whether you want that or not. Did you read the code I gave you 3 months ago?

## fart-master | 2020-03-20T22:50:30+00:00
BTW, I made no modifications to rapidjson. Dimwit

## who-biz | 2020-03-20T22:54:37+00:00
I may end up PRing it. But I’m not familiar with XMRig code. I’ll let other weigh in before doing so.

Perhaps you should PR your changes, if you’re here to help. No need for the animosity. 

But, should serve as evidence of why we are requesting official XMRig support, instead of going with a persistently malicious author’s implementation. 

## fart-master | 2020-03-20T22:57:48+00:00
Malicious? You're a moron. It isn't malicious to point that out. Is it malicious to say the sky is blue? But I don't need to PR changes. I have a miner that works for myself. You're the one who doesn't understand the code and is trying to get someone else to do the work for you

## who-biz | 2020-03-20T23:02:57+00:00
🙄 Begs the question of why you’re here in the first place.

## fart-master | 2020-03-20T23:05:55+00:00
Just to point out the code already exists and you don't need to be wasting more people's time by asking someone else to do it for you

## who-biz | 2020-03-20T23:09:31+00:00
I’ve been working on integrating DPoW for 11 months now. You’re aware of this. 

Since we are entering the final stage of that rewrite, I’m short on time. The work will be easier for someone familiar with XMRig. However, as I’ve said, I’m happy to help, if necessary.

## fart-master | 2020-03-20T23:31:01+00:00
You mean that dpow that was meant to be finished in June last year? Seems like an excuse. You can't find a few hours in 11 months? I wasn't familiar with xmrig either till I downloaded it an looked at it for half an hour. Real programmers don't use "I'm unfamiliar with the code" as an excuse. You are clearly just not a real programmer. And that is fine, but don't pretend otherwise.

## who-biz | 2020-03-20T23:35:25+00:00
Entitled to your opinion. 

But since others said “it couldn’t be done”... I’d say a year of time is pretty good for a near-full rewrite.

Nice try, though. Have a good night.

If someone from XMRig could let me know if the modifications are too much for your group to manage... I’ll devote the time, when I have some to spare.

## fart-master | 2020-03-21T00:15:15+00:00
Sources? You keep saying people said it couldn't be done. I am yet to see anyone who said that. I have however seen many people who think it's a stupid idea

## cogitocat | 2020-03-21T00:28:36+00:00
Fart is a shameless paid shrill.  I'm more than one occurrence he has said that he is getting paid to naysay. He likes to interject his negativity to distract progress on this project.

## fart-master | 2020-03-21T03:00:21+00:00
So funny. You think you're important enough that people are paying others to say bad things about you. What progress am I hindering? You are 9 months past deadlines you imposed. Seems you're doing just fine at not delivering results all by yourself

## cogitocat | 2020-03-21T03:08:40+00:00
There is no think.  You've flat out said it.  Let's stay on track and
respect the XMrig project, and this request.

On Fri, Mar 20, 2020, 5:00 PM fart-master <notifications@github.com> wrote:

> So funny. You think you're important enough that people are paying others
> to say bad things about you. What progress am I hindering? You are 9 months
> past deadlines you imposed. Seems you're doing just fine at not delivering
> results all by yourself
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1591#issuecomment-601983895>, or
> unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AN7NEASVQS6THYCFGG5STBLRIQUU7ANCNFSM4LE7RK7A>
> .
>


## fart-master | 2020-03-21T05:43:20+00:00
Lulz. Such silly people. So who is paying me? The deep state scared your little shitcoin is going to overthrow the almighty dollar? Maybe it's the Monero fans scared your coin with no trading volume is going to become the foremost cryptonote coin? Who exactly do you believe is financing a fud campaign against you?

Want xmrig support? Just do it yourself. Use the miner that exists or submit a PR. asking someone else to do your dev work is weak.

## Spudz76 | 2020-03-21T21:08:15+00:00
Unless it's already popular and has a certain level of network hashrate (not sure of current limits) nobody is going to add it, unless it's you with a PR and even then it probably won't be accepted unless again, network hashrate is there already.

Oh and then if the coin is hated for any reason it doesn't ever get in (such as defyx/Scala) and then you have to keep your own patchset to apply to every `dev` release like I have been for a while (based on MoneroOcean patchset).

## who-biz | 2020-03-21T21:22:05+00:00
@Spudz76 any idea what a threshold is for network hashrate?

“Hated” sounds a bit arbitrary.

## Spudz76 | 2020-03-21T21:32:53+00:00
Network hashrate total, like from the coins main explorer, or a pool.  I have no idea what the current limit is I knew it when CN-R was a thing before RX.  Essentially if it's not already popular and has a bunch of activity and also probably can be traded somewhere to a more mainstream coin, it doesn't get added.  They have to be past the infant-mortality point, most new coins disappear.

> “Hated” sounds a bit arbitrary.

It is completely arbitrary.  Such as if the coin creator is a toxic jackass, etc.  Or just don't like the coin.  I don't even know why defyx won't be accepted other than it won't.

## who-biz | 2020-03-21T21:35:11+00:00
I understand what network hashrate means. I was asking about what you refer to as “limits,” it seems. 

Alright. Thanks for the info

# Action History
- Created by: cogitocat | 2020-03-10T14:00:27+00:00
- Closed at: 2020-08-29T04:50:31+00:00
