---
title: how do I make a simple payment portal for accepting monero payments on my website,
  without a third party service?
source_url: https://github.com/monero-project/monero/issues/6404
author: mstyp
assignees: []
labels: []
created_at: '2020-03-26T20:12:02+00:00'
updated_at: '2020-04-26T21:01:27+00:00'
type: issue
status: closed
closed_at: '2020-04-26T21:01:27+00:00'
---

# Original Description
I run a brick and mortar shop and I really like the built in merchent view page on the default gui wallet. I would like to add similar functionality to my website, but I have no idea how to do that.

Its just a simple one page website hosted on a debian 10 VPS with apache. No java or css or whatever. Just text product discriptions and links to pay with paypal.

I do have the monero cli wallet installed on the vps but i dont know how to make the website talk to it. Is there something that I can add to my website which generates a new address each time a user clicks a button?

All of the solutions I have seen (including all the ones listed at https://web.getmonero.org/community/merchants/#libraries) require some third party or service that I am not part of (like the wordpress/globee plugins) or their documentation seems to assume people know how to code and are way too complicated for me to follow. 

I tried using the [php libraries](https://github.com/monero-integrations/monerophp) but after the "getting started" section their documentation does not include any steps for how to actually set up a working payment portal. 

ideally the process on my website would be:

1. user inputs their info into form

2. user clicks pay with xmr

3. unique payment code/subadress/whatever is generated

4. user pays

5. after 1 confirmation i get a notification to send out product

I can follow guides and processes but I don't want to have to write my own scripts from scratch or spend hours troubleshooting. I can ssh into my vps, cd around directories and apt install and git clone and copy paste and thats about it.

# Discussion History
## t-900-a | 2020-03-27T16:17:04+00:00
btcpay server supports monero, it's a bit complicated to setup, and I don't believe there is any good documentation out there.
Here's a demo for btcpay server to give you an idea what the site would look like.
https://store.btcpayserver.org/homepage/

You may be able to find someone to set this up for you on telegram: https://t.me/MoneroJobs

Documentation: https://github.com/btcpayserver/btcpayserver-doc/blob/master/Altcoins.md#how-can-i-add-an-altcoin-to-btcpayserver

Unfortunately they BTC pay server is geared towards BTC users, so remember to "Beware of Bitcoin" https://masteringmonero.com/bitcoin.html


# Action History
- Created by: mstyp | 2020-03-26T20:12:02+00:00
- Closed at: 2020-04-26T21:01:27+00:00
