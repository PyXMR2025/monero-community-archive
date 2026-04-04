---
title: Revise Light Wallet section
source_url: https://github.com/monero-project/monero-site/issues/2162
author: CryptoGrampy
assignees: []
labels:
- 💬 discussion
- downloads
created_at: '2023-05-03T17:54:46+00:00'
updated_at: '2025-08-19T14:32:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I'm creating this issue to get some discussion and input on significant revisions to the light wallet section on the getmonero downloads page.

1. Remove any wallets that don't support self-hosted light wallet servers.  The higher the % of Monero users using hosted light wallet servers, the worse privacy becomes for ALL users of Monero.  Any wallet that doesn't safely support the use of a self-hosted Light Wallet Server (any server that follows the Light Wallet API spec) should not be recommended. 
 
2. Add more clarity to the privacy dangers of using the default 'hosted' light wallet server in these wallets.  It's not just that your privacy can be 'lessened'.  It's that all of your past, current and future incoming transactions tied to that view key will be recorded and saved, even if you decide to stop using the wallet.  Usage of the default behavior of that wallet lowers the privacy of all users of Monero, and additionally, significant information around a spend (not the spend amount itself) is leaked when using Light Wallets with a server out of your control.  

# Discussion History
## SamsungGalaxyPlayer | 2023-05-04T13:39:22+00:00
1 would include the official wallets, Feather, Cake, Monerujo, etc. I don't see a reason to remove wallets that don't have this feature at this time. Perhaps a year after formal official wallet support (?). Unless you mean the removal of light wallets that rely on a set centralized server.

## lalanza808 | 2023-05-04T18:03:17+00:00
+1 - would love to see a stronger push for self-hosted LWS setups.

@SamsungGalaxyPlayer just the light wallets section:
![image](https://user-images.githubusercontent.com/4086248/236289626-2425a6b7-5893-40cb-814c-2eb8f3e97b5f.png)



## erciccione | 2023-05-05T06:59:19+00:00
> Remove any wallets that don't support self-hosted light wallet servers

I disagree with the complete removal, but i agree we should expand the warning or put these wallets after the self-hostable ones.

> Add more clarity to the privacy dangers of using the default 'hosted' light wallet server in these wallets

I agree. Any suggestion about the specific phrasing? I would keep it short, or, if we want it longer, we might exand the "light wallets" Moneropedia entry to include all the information we want. 

## CryptoGrampy | 2023-05-08T21:49:22+00:00
Regarding complete removal:

1. If a light wallet doesn't allow users to input a custom server URL, they are essentially profiting off of the reduction of system privacy in Monero for the reasons stated above.  Why on Earth would we put thousands of XMR per year into the further development of the privacy protocol if we also push users (via suggestion on getmonero.org and the reddit sidebar) into wallets that give users no choice but to give up their transaction data to propriatary black box data collection.   It makes no sense.

2. Considering the substantial amount of server resources required to monitor thousands+ if not hundreds of thousands of wallets in a light wallet server, doesn't it seem a little strange that a wallet company running these servers doesn't make it easy for users to use their own personal server resources to reduce compute cost?  Could it be that the in-app exchange offered by the Light Wallets isn't the only funding mechanism for their companies, and that they may be following the footsteps of countless other companies that sell user data?

3.  If  CakeWallet @SamsungGalaxyPlayer only allowed users to use Cake's Monero node, there would be a mass uprising in the Monero community.  Why does a wallet like Edge get a pass in this regard?  

Regarding phrasing:

Let me mull this one a bit.  I agree that short is always best, but it may be good to reach out to MRL or Monero-Dev to get an full and accurate understanding of the risks associated with these wallets in conjunction with a hosted server; it's a much worse situation than most people understand. 

## SamsungGalaxyPlayer | 2023-05-08T21:51:59+00:00
I'm for removing lightweight wallets that don't allow using a custom server. Maybe I'll change my mind with Seraphis/JAMTIS, but not now. The privacy leak is significant, and should not be recommended.

## plowsof | 2023-07-01T13:08:30+00:00
MajesticBank noted on IRC that the edge app is the only one to have trackers https://reports.exodus-privacy.eu.org/en/reports/co.edgesecure.app/latest/ (if this would play into any decision making) 

## jermanuts | 2024-03-18T14:33:12+00:00
As I said at https://github.com/monero-project/monero-site/pull/2143#issuecomment-2002555434 you are putting a lot of trust in these Web-based wallets to not serve you a backdoored client from the server by dynamically serving JavaScript code to the browser to handle cryptography, creating wallets (stealing seeds) and when using an existing wallet etc.

They are too much of security risk to recommend.

EDIT: https://www.devever.net/~hl/webcrypto

## detherminal | 2024-04-13T22:13:10+00:00
changing the section's name might also be a good choice. feather is neither mobile nor light but it is still there.

## SyntheticBird45 | 2024-04-17T16:31:27+00:00
What about "Roaming" instead of "Lightweight". This is the only use case fwiw

## Dolorozo | 2025-08-06T14:24:20+00:00
I was going to start a new thread, but I think this is the right place to bring it up. I’d like to revisit the idea of listing Coin Wallet.

Previous PRs:
https://github.com/monero-project/monero-site/pull/1725, https://github.com/monero-project/monero-site/pull/2143

I won’t focus on what we feel were somewhat unfair listing criteria. Instead we just want to remind about our solution and have a constructive discussion about the catalog

In short:
- we are the only wallet that supports Monero without any sync (no local or remote node involved) https://www.reddit.com/r/Monero/comments/1llayok/nosync_monero_wallets_are_we_still_alone/
- we don’t share the private view key and we have no way of seeing future user transactions (a good point that was brought up earlier)

We believe we bring real value to Monero users: instant access to XMR, no remote nodes, no scanning delays. We get positive feedback from users every day. for real

We’d love to hear your thoughts! But please don’t repeat what was already said in the previous PR, so we can actually move forward

## nahuhh | 2025-08-06T17:25:55+00:00
> In short:
> - we are the only wallet that supports Monero without any sync (no local or remote node involved) https://www.reddit.com/r/Monero/comments/1llayok/nosync_monero_wallets_are_we_still_alone/

you require users input the txid, don't you? It has to reconcile that info _somewhere_.

> - we don’t share the private view key and we have no way of seeing future user transactions (a good point that was brought up earlier)

you require users input the txid, don't you? this is just as revealing as inputting a view key. 

So how do you track balances w/o knowledge of send/receives?

## Dolorozo | 2025-08-07T13:10:35+00:00
@nahuhh hey
>you require users input the txid, don't you? It has to reconcile that info somewhere.

Yes, the user needs to manually enter the txid. Where do they get it from? From wherever they communicate with the sender (chat, email, etc.) It’s just a hash, not sensitive data

>you require users input the txid, don't you? this is just as revealing as inputting a view key.

Not really. Entering a single txid checks one specific transaction, **locally**.
from https://github.com/CoinSpace/monerolib 
X = Hs(R * pV | i) * G + PS
It runs entirely on the **user’s device**, with their keys. 
https://github.com/CoinSpace/monerolib/blob/master/lib/crypto-util.js#L178

>So how do you track balances w/o knowledge of send/receives?

We don’t. Coin Wallet isn’t meant for users (or businesses) who receive unexpected transactions (like donations).
It’s built for users who know they’re expecting a transaction. Of course, funds are never lost. They belong to the user and can be added at any time, as long as the hash is known.


## Dolorozo | 2025-08-11T11:54:25+00:00
By the way, I found this post https://github.com/monero-project/monero-site/issues/2412
All criteria are met

## Dolorozo | 2025-08-13T13:07:26+00:00
Hi @plowsof, @jermanuts, @erciccione ,
Sorry for pinging, but I think your input is important here. 

We’d love it if you could take a look at our request and share your thoughts. Would it be okay for us to open a **new PR** that reflects everything discussed so far? We have already covered all the pros and cons in the PR and in the comments.

As an extra note, our wallet has been reviewed and listed in several Monero directories (like Observer, Monerica). We know this isn’t a deciding factor, but we hope it shows our commitment. We’ve been supporting Monero for 4 years and have no plans to stop.

## nahuhh | 2025-08-13T15:40:58+00:00
@Dolorozo do u still charge fees

## Dolorozo | 2025-08-18T11:48:27+00:00
We fully meet the criteria described here: https://github.com/monero-project/monero-site/issues/2412.
If this is not the case, please point out the specific items where we do **not** fit. Otherwise, why define criteria and not follow them?

All wallets except GUI and CLI have features that monetize users (buying, selling, swapping, gift card purchases etc.). Since last week buying xmr inside the wallet has become nearly impossible but this option had been available for many years

## nahuhh | 2025-08-18T13:00:38+00:00
> We fully meet the criteria described here: https://github.com/monero-project/monero-site/issues/2412.
> If this is not the case, please point out the specific items where we do **not** fit. Otherwise, why define criteria and not follow them?
> 
> All wallets except GUI and CLI have features that monetize users (buying, selling, swapping, gift card purchases etc.). Since last week buying xmr inside the wallet has become nearly impossible but this option had been available for many years

Note: that is a users proposed criteria. It hasn't been accepted, or even acknowledged.


The main criteria is community acceptance.
We are a decentralized community, managed by the community.

- we have numerous reports of "wheres my money" because of your nob-standard implementation (must scan txs)
- you scrape fees
- iiuc, you recommend changelly

Without ever testing your wallet, I would hard NACK it on any one of those 3 points. 


## Dolorozo | 2025-08-18T18:59:05+00:00
Where do you get these reports, and in what volume?
We have a few hints when the Monero balance is 0, when receiving, and we also have a dedicated Monero [support page](https://support.coin.space/hc/en-us/articles/4403046925204-How-to-accept-Monero-transactions.).
We run our own support, and regarding Monero we get up to 10 tickets per month (on all topics), which is about the same as for other currencies.

As for changelly that’s an unexpected complaint, we haven’t seen it before. Disabling a swap partner would take about half an hour. Reasons?

Are you really saying you haven’t tested our wallet, and judging by your previous questions (especially this one "this is just as revealing as inputting a view key") , you don’t fully understand how and why we built it without using remote nodes? That’s a bit disappointing to us. Why leave such a comment without actually checking?

## plowsof | 2025-08-18T19:21:38+00:00
"without remote nodes" is not correct- users enter a tx id that belongs to them for which info is fetched from 'a remote node'.

Scan tx exists within the Monero GUI wallet and others, you point it at your own local/remote/tor node 

Wallets can add a skip sync if users like this https://bounties.monero.social/posts/79/0-421m-add-a-skip-sync-feature-to-a-monero-wallet

in the end your wallet has a boat load of meta data at low cost of entry



## nahuhh | 2025-08-18T19:32:43+00:00
> Where do you get these reports, and in what volume?

matrix/irc. Greater than 0

> As for changelly that’s an unexpected complaint, we haven’t seen it before. Disabling a swap partner would take about half an hour. Reasons?

They have been a red flagged swapper for years. Surprise kyc, refusing to refund. Im sure you can search the web for reports of changelly's behavior.

> Are you really saying you haven’t tested our wallet, and judging by your previous questions (especially this one "this is just as revealing as inputting a view key") , you don’t fully understand how and why we built it without using remote nodes?

You cant scan in a tx or spend funds without a node


> Why leave such a comment without actually checking?

Last i checked, ya'll charged fees for withdrawal, so why would deposit $ there?



## Dolorozo | 2025-08-19T14:32:03+00:00
Hi again!
we honestly don’t understand why you keep saying this without checking the code. I ask you to spend a bit of time reviewing it or involve someone who **understands**. Judging by the repeated questions you haven’t looked. It's really hard to imagine, but it is possible to scan a tx without node. 

About Matrix reports. Over the last year there was only one mention about us. Yes, that’s more than 0, but not "numerous reports.” Why misinform? What’s the point? We do have support guys, I’ll ask them to respond faster, but we can’t be quicker than toxic comments no matter how hard we try :-)

Changelly - okay, we checked. We never recommend it manually (there’s no such functionality), the swap partner is chosen automatically by best rate. We will discuss this with the team asap.

Either we can open another PR to get proper attention from the developers. Otherwise it feels like off-top and no one will actually look at the code.

# Action History
- Created by: CryptoGrampy | 2023-05-03T17:54:46+00:00
