---
title: Monero payments
source_url: https://github.com/monero-project/monero-site/issues/852
author: Herroo
assignees: []
labels: []
created_at: '2018-08-19T20:29:16+00:00'
updated_at: '2020-04-07T09:44:19+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:44:18+00:00'
---

# Original Description
What can we do to help simple retailers and others to implement Monero payments on their websites? Would it make sense to add a section of "how to get paid in Monero" on the official website and have super simple video guides for how to get it implemented on e.g. your wordpress site? 

Maybe here: https://getmonero.org/get-started/accepting/

How can I/we non-techies help out? Is there someone pedagogic from the core team or a regular contributor to the project who is interested in doing something like this as an FFS? I for one would be interested in funding something like this as it would increase the overall demand for Monero.

Just by looking at the 24h volumes of the top 15 market cap coins it is apparent that Monero is well behind the others, which is worryingSource: https://imgur.com/a/XpahLW1

# Discussion History
## el00ruobuob | 2018-08-20T05:45:16+00:00
I believe we should create a user guide for this (or several) "how to integrate globee to wordpress" for instance. But I'm not sure an FFS might be needed on this. We could write it with the help of payment gateways whom interest is to be used, so they should collaborate easily. Any thoughts from globee perspective @fluffypony ?

## ordtrogen | 2018-08-20T21:15:20+00:00
I seem to recall there was a lot of work done on Wordpress <--> Monero maybe a year ago? 
Maybe it was @serhack who was doing it, or maybe he remembers.

Unless I misunderstand the topic on this thread, what you're asking for could already be available. 

Are these the droids you're looking for?

https://github.com/monero-integrations


## serhack | 2018-08-21T05:44:36+00:00
Hi @Herroo, welcome to Github and Monero community!

I am the lead developer of [Monero Integrations project](https://github.com/monero-integrations). This project aims to give to merchants the most private payment gateway compatible with CMS (Content Managment System). At the moment we have Woocommerce, OpenCart, Prestashop, WHMCS payment gateways.

One year ago I opened a FFS to started work about this. At the moment I am a little busy with another project, [Mastering Monero](https://masteringmonero.com). But when I will release that resource, I'll work fully on Monero Integrations. 

Probably I and @cryptochangements will ask for FFS since we have a couple of ideas to develop, expecially marketing. Why marketing? Well, it seems a lot of people could not looking for our project. I don't know really the reason for that. We'll do some maintenance for all plugins :- ) 

Let me know about any idea! 

## el00ruobuob | 2018-08-21T06:00:23+00:00
So I suggest we simply add a user guide which point to the different repositories with a few wording around, as well as a link to it in "accepting"

## serhack | 2018-08-21T06:56:27+00:00
> So I suggest we simply add a user guide which point to the different repositories with a few wording around, as well as a link to it in "accepting"

Well, I was thinking to write a resource for developers so they could write own private payment gateway too!

## Herroo | 2018-08-21T06:59:54+00:00
All of this sounds very promising, especially @serhack 's dedication for the question in the Integrations Project. Special thanks for that!

I am for any suggestion which make the information available, in a VERY pedagogic format and is simple to find for those seeking information about Monero. In an ideal world I believe that the official Monero website should be the single source of information you would need, to get up and running - and there would be video guides so that we can start attract non-techie people. Whether it is if you would want to learn about the project, start spend, collect, get payments in, mine or exchange Monero. I do however understand that it might be a utopia.

I do like the point made by @el00ruobuob that we do not need to write/make everything ourselves but there might be other parties interested in getting that information on "our" website - for example Globee, monerujo or XMR-stak. We would then just need to invite them to it and to post their material on a logic place once it is up to standards.

## serhack | 2018-08-21T07:42:17+00:00
I agree with @Herroo . At the moment, the getmonero.org website is bare. Definitely, we need more content! 😄 

## el00ruobuob | 2018-08-23T13:38:15+00:00
Damned, i think i responsed to it, but with my country-side internet, it has been lost.
So i suggest to:
- add each existing guides from the repo to a new "merchants" section within user-guide page;
- thanks and cheers @serhack for this dev-guide idee, which will be great to integrate.

If we have consensus on this, i can start with user-guides right away.

## net-stark | 2018-08-26T06:51:38+00:00
Is this where we submit info on merchants accepting monero?

Or is there any form somewhere? TIA..

## rehrar | 2018-08-27T08:57:22+00:00
The Accepting page needs to be completely rewritten to talk about how people (businesses and users) can start accepting Monero. It should highlight things like Monero Integrations and Globee.

## el00ruobuob | 2018-08-27T11:21:27+00:00
@senangonline no. You have to open a new issue to submit your request

## el00ruobuob | 2018-08-27T11:22:56+00:00
@rehrar does it make sense to integrated all the Monero Integrations guides in a new section under user-guides ? Or do we want to only point to the repository ?
I think getmonero.org should be the major (if not single) source of content.

## el00ruobuob | 2018-08-31T05:46:49+00:00
Let's do a poll:

Do we add all the monero-integrations how-to to a new user-guide section?

* **Yes, we need more content**: 3
* Only a link to github: 0
* No, don't even pronounce its name: 0

## Herroo | 2018-08-31T07:15:25+00:00
Great idea to have a vote. My vote falls on:
**Yes, we need more content**

## minerjed | 2018-09-01T14:08:45+00:00
The reason a lot of small merchants do not accept Monero is because of the price functions.  They sell a product and then have to purchase more of that product in their fiat currency.  So you not only need to provide an easy way to accept Monero, the merchant needs an easy way to quickly convert the currency  so they can purchase more product to sell.

## el00ruobuob | 2018-09-01T14:14:14+00:00
@directdepot this is exactly what Globee and other payment gateway are for. Globee allow you to accept XMR and hold it as fiat. That's why we need @fluffypony support to help user to integrate them from our website itself, or at least explain the concept.  

>
    SETTLEMENT OF
    YOUR CHOICE
    
    You can decide in what ratio you'd like to be settled. You may choose between 100% settlement in your national currency via Fiat, Bitcoin or Monero, or any ratio between the three.

 

## cryptochangements34 | 2018-09-01T17:13:07+00:00
I am 100% in favor of explaining how to easily accept Monero. However, if it is going to highlight certain services then I vote for Monero-Integrations as opposed to Globee because Monero-Integrations only supports Monero and is 100% free (both libre and gratis) while Globee is a for-profit company

## serhack | 2018-09-01T19:23:56+00:00
I think few people got the real features of Monero Integrations. The payment gateways developed by Monero Integrations Team are PRIVATE and DECENTRALIZED.

## erciccione | 2020-04-07T09:44:18+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's worth it.

# Action History
- Created by: Herroo | 2018-08-19T20:29:16+00:00
- Closed at: 2020-04-07T09:44:18+00:00
