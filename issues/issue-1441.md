---
title: 'Adding Incognito Wallet to the https://www.getmonero.org/downloads/#mobilelight '
source_url: https://github.com/monero-project/monero-site/issues/1441
author: incognickv
assignees: []
labels:
- 💬 discussion
- downloads
created_at: '2021-01-28T11:23:52+00:00'
updated_at: '2021-02-02T11:45:48+00:00'
type: issue
status: closed
closed_at: '2021-02-02T11:24:33+00:00'
---

# Original Description
Incognito Wallet is an open source mobile wallet app for iOS and Android devices that supports XMR. The wallet designed and developed by the Incognito Dev team. The purpose of this wallet is enabling an option for storing XMR funds privately. Following the requirements for only open sourced wallets to be listed at https://repo.getmonero.org/monero-project/monero-site/-/issues/982 we are asking if the wallet can be listed under the Downloads > Mobile and Light Wallets section of the https://www.getmonero.org/

Source code: https://github.com/incognitochain/incognito-wallet

# Discussion History
## erciccione | 2021-01-28T11:44:38+00:00
> Following the requirements for only open sourced wallets to be listed

Just a small clarification: it's not only open source wallets, but open source *and* trusted wallets.

Personally i don't know much about Incognito, beside the fact that they use some kind of token between trades (i might be incorrect). I'm interested in knowing the opinion of @SamsungGalaxyPlayer, since AFAIK he took a deep look into Incognito not long ago.

## incognickv | 2021-01-28T12:43:04+00:00
thanks for the clarification, so i think I should mention that Incognito is already among exchanges at the Merchants sections, though it's not an endorsement form the community.
It will be nice if we can hear objective assessment form @SamsungGalaxyPlayer. Also, I will try to respond for questions. Opinion of the Monero folks is important  for us, as we value the same principles of privacy first as you. 

## SamsungGalaxyPlayer | 2021-01-28T13:52:42+00:00
The Monero is non-custodial, correct? Only custodied if converted to the wrapped version?

Edit: can users store Monero and use the Monero natively in a non-custodial way? Without touching the wrapped version?

## incognickv | 2021-01-31T21:17:28+00:00
storing in Incognito wallet app is non-custodial by default, as only wallet creator owns his keychains;
the current implementation of the app for XMR by default means minting pXMR on our behalf and lock native coins in a "trusted" way;
how it works and what level of privacy we get from monero community members already jumped to Incognito is shown in numbers of ~$1,735,137.22 for liquidity and ~$7,648,312.97 for trading volume (https://incscan.io/pdex); these numbers say for themselves about trusted opportunity for XMR to go into DeFi using our wallet app;
that's why we request for adding Incognito to the list of mobile wallets and open direct gates to DeFi opportunities for XMR 

## erciccione | 2021-02-01T09:36:47+00:00
From a short research seems like the Incognito team is allergic to giving clear answers, as the comment above shows well. Their business model is shady, their implementation is shady and they are more an exchange not really a wallet. Beside, i don't seem to find a clear answer about Monero or only the wrapped version being used in the wallet.

I don't trust them and i wouldn't feel comfortable in pointing Monero users their way, especially since they are mostly an exchange, not a wallet, and their behaviour doesn't inspire trust.

**NACK** for me.

## incognickv | 2021-02-01T15:05:17+00:00
pardon, but I gave the most direct and clear answer of what we have built and how it works, probably it was not so obviously clear, so let me break things down in details:
we don't have a business model for monetization by any means at the current stage of the development; 
are we more likely a DEX or a wallet? - the answer is we're the wallet having a whole ecosystem for storing, trading, providing liquidity in a private way for XMR exactly and we enabled atomic swap for XMR to BTC (or any other currencies listed) internally in the Incognito wallet - Incognito wallet is kinda a 'private swiss army knife';
don't understand what you mean with 'their implementation is shady';
we don't use term of 'wrapped' as well as 'depositing to incognito address' for any crypto, but instead we shield native asset to a private one,  which is in XMR particular case looks the next: shielding of XMR to >>> pXMR (private XMR), that has access to all features in the wallet >>> then unshielding and user gets back to the native coin; this scenario is similar for all assets and as i mentioned in previous comment was battle tested with hundreds of transactions but thousands of users and millions of TVL on chain;

i'm happy to answer more questions and prove that we follow the same goals of building privacy as monero folks 

## SamsungGalaxyPlayer | 2021-02-01T15:47:19+00:00
Before this discussion is really considered further, I need to have some sort of confirmation someone can use it as an entirely native XMR app. Users deposit real XMR and keep is as real, non-wrapped XMR and send/receive transactions in real XMR, etc.

## incognickv | 2021-02-01T21:20:27+00:00
@SamsungGalaxyPlayer, may i suggest a solution which can definitely set things strait. what if you can try testing the wallet and probably any other feature available yourself. this way you can answer your queries based on real experience. it will be pleasure for me to assist you with any kind of support needed. also, i can fund you with a fraction of xmr (refundable) for the test purpose.
just let me know your thought on the suggestion above.

## SamsungGalaxyPlayer | 2021-02-01T22:42:32+00:00
Based on testing, it looks like users can deposit and withdraw Monero. However, they can only hold wrapped XMR from what I can tell. XMR deposits are converted to wrapped XMR, and wrapped XMR withdrawals are converted to XMR.

This doesn't really meet the description of wallets that are included on the website. Wallets listed here allow users to store, send, and receive funds in native (unwrapped) XMR.

## incognickv | 2021-02-02T09:41:15+00:00
@SamsungGalaxyPlayer, thank you very much for personal testing and providing wise and reasonable feedback on Incognito wallet app. From the perspective you shared above I can conclude that the series of ongoing storing > sending> receiving for native (unwrapped) XMR when it comes to Incognito mode supported in the wallet is broken and it doesn't match to the requirements for mobile wallets listed on get.monero.org. Considering this, **I agree that Incognito app doesn't match the description to be listed on there**. 

I think this the end of the story for listing Incognito wallet among mobile wallets for Monero on the website. Thanks for all your input.

Meanwhile, I see that you was personally trying **shielding/unshielding features for XMR** using Incognito tech. So, @SamsungGalaxyPlayer, Can you share some words about how smooth and friendly these features worked for you, please? Can we chat in dm for this purpose, pls?


## erciccione | 2021-02-02T11:24:33+00:00
> I agree that Incognito app doesn't match the description to be listed on there.

Closing the issue.

> Can you share some words about how smooth and friendly these features worked for you, please?

Not here please. A better platform would be IRC/matrix or whatever.

# Action History
- Created by: incognickv | 2021-01-28T11:23:52+00:00
- Closed at: 2021-02-02T11:24:33+00:00
