---
title: More prominently display wallets that don't send any data by default in the
  download section
source_url: https://github.com/monero-project/monero-site/issues/2011
author: erciccione
assignees: []
labels:
- downloads
- enhancement
created_at: '2022-08-04T08:22:24+00:00'
updated_at: '2024-03-24T08:16:06+00:00'
type: issue
status: closed
closed_at: '2024-03-24T08:16:06+00:00'
---

# Original Description
After the controversy risen in https://github.com/monero-project/monero-site/pull/2007, was pointed out that some wallets listed on getmonero might have a controversial privacy policy and/or ping home (sending sensitive data) without the user's specific consent. This can result in the privacy of the user being compromised.

Users of getmonero should be able to make an informed choice about what wallets listed on getmonero don't communicate externally unless specifically requested by the user.

We should show a badge or a note near the wallets that don't send data by default. We could also do the opposite, noting which wallets do send data.

To my knowledge, currently the wallets listed on getmonero that send data back home by default are:

- ~~Cake wallet~~ (edit: not anymore)
- Edge
- Mymonero

# Discussion History
## ghost | 2022-08-04T08:25:34+00:00
i think a "warning" label for those wallets is more appropriate with an explanation that they leak sensitive data by default

## ChristopherKing42 | 2022-08-09T19:05:30+00:00
To avoid duplicating work, why not just use the list of F-droid antifeatures? https://f-droid.org/docs/Anti-Features/#:~:text=certain%20Anti%2DFeatures.-,List%20of%20Anti%2DFeatures,-F%2DDroid%20currently

The intent of the anti-feature list seems to be the same as what this issue is trying to solve.

## erciccione | 2022-08-12T07:45:53+00:00
@ChristopherKing42 that could be a good idea, but contributors will need to extensively test the wallets listed to make sure all the requisites are fulfilled. Maybe we could compile a list of our own anti-feature and publish it on the website, so that it will be clear for everyone.

In the meantime i opened #2019, that simply adds a disclaimer to the wallets i mentioned.

## HardenedSteel | 2022-08-12T16:10:18+00:00
Feather and Monerujo wallet too pinging external sources to get their fiat prices by default. Currently Feather uses Tor for this but not Monerujo

## SamsungGalaxyPlayer | 2022-08-12T16:27:34+00:00
Please make sure that if included, there's some obvious nuance between looking up "what's the price of XMR/USD" and "here, have my private view key for eternity."

## erciccione | 2022-08-29T09:16:36+00:00
> Feather and Monerujo wallet too pinging external sources to get their fiat prices by default. Currently Feather uses Tor for this but not Monerujo

According to the report in #monero-site, Feather and Monerujo don't ping their servers by default when the app is turned on. There seems to be conflicting information about this, so some clarity is needed.

> Please make sure that if included, there's some obvious nuance between looking up "what's the price of XMR/USD" and "here, have my private view key for eternity."

What i care about is if the apps pings external servers by default at launch or not. It doesn't matter if it's "for the price only", because this is something the final user cannot verify. Instead they have to trust the wallet provider that's indeed the only thing that happens (when you get a price request, you also get their IP + metadata).

Let's also remember that servers can be hacked and IPs collected regardless of the intentions of wallet providers, which could also be forced by government agencies to provide the info they have about specific IPs (which is even easier to achieve if the wallet is managed by a corporation). Even simply knowing that a wallet was open at a certain time could be critical information. Let's not forget the famous "We kill people based on metadata".

So, there are multiple ways for an innocuous call for price fetching to result in a critical problem for Monero users that need to protect their privacy because, for example, they are persecuted because of their religion orsexual orientation or are whistleblowers.

To reiterate: Monero users are in general more careful about their privacy and some of them might actually find themselves in trouble if sensitive info is leaked. The standard should be the official wallets, which when started don't make any external communication that people don't expect or cannot control, like sending IP + metadata by default for price fetching.

Yes, of course the wallets need to connect to either a local or remote node to work, but that's part of how the network works and users with particular privacy requirement are probably aware of the tool they are using and how to use it in a way that doesn't put them in danger. The point is to protect them about behaviours they cannot control.

## HardenedSteel | 2022-09-10T20:58:26+00:00
AFAIK there's no option to disable and its enabled by default, in this case cake and monero.com wallet should ask to users before setting up the app. Most people would want this feature too @SamsungGalaxyPlayer 

## erciccione | 2022-12-21T09:45:35+00:00
AFAIK Cake now offers the possibility to not ping their servers. @SamsungGalaxyPlayer please confirm.

## SamsungGalaxyPlayer | 2022-12-21T15:31:59+00:00
@erciccione yes that is correct. By clicking Advanced Privacy Settings when first setting up Cake Wallet, you can disable the fiat API and specify your own node so that 0 connections are made to our servers.

## nahuhh | 2023-02-22T08:34:36+00:00
I can confirm cake and monero.com can be run without making any external connections. These settings can be configured on first launch and also toggled on an off as a user wishes.

## erciccione | 2023-02-22T12:56:06+00:00
Edited the issue accordingly.

## ghost | 2023-02-22T20:56:19+00:00
*by default* is the issue at hand. looks like cake still does that, and buries an option to disable it, rather than off by default and opting in

# Action History
- Created by: erciccione | 2022-08-04T08:22:24+00:00
- Closed at: 2024-03-24T08:16:06+00:00
