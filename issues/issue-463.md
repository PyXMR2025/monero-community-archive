---
title: Categorize/Declutter Moneropedia Articles
source_url: https://github.com/monero-project/monero-site/issues/463
author: QuickBASIC
assignees: []
labels: []
created_at: '2017-10-31T14:05:33+00:00'
updated_at: '2020-04-07T09:34:11+00:00'
type: issue
status: closed
closed_at: '2020-04-07T09:34:11+00:00'
---

# Original Description
Even though Kovri is going to be integrated into Monero in the future, I feel like having a lot of stub articles about Kovri topics in the Moneropedia is detrimental to it's function as instructional for new users. (Currently 34.9% of articles are Kovri-based.)

I'm not as familiar with I2P or Kovri, so I don't feel equipped to make the change myself. I think a lot of this information can be moved copied over to [monero-project/kovri-site](https://github.com/monero-project/kovri-site) eventually, but for now I think we should consolidate it into one article. (Another possibility I've considered is to expand Moneropedia to include categories, and categorize these in a way that it's easier to navigate Monero specific topics seperate from Kovri topics.)

I believe these are all the articles that are currently Kovri related:

[Base32-Address](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/base32-address.md)
[Base64-Address](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/base64-address.md)
[Canonically Unique Host](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/canonically-unique-host.md)
[Clearnet](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/clearnet.md)
[Destination](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/destination.md)
[Eeepsite](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/eepsite.md)
[Floodfill](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/floodfill.md)
[Garlic Encryption](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/garlic-encryption.md)
[Garlic Routing](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/garlic-routing.md)
[i2np](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/i2np.md)
[i2p](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/i2p.md)
[i2pcontrol](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/i2pcontrol.md)
[java-i2p](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/java-i2p.md)
[Jump Service](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/jump-service.md)
[Kovri](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/kovri.md)
[Lease](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/lease.md)
[Network Database](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/network-database.md)
[Router Info](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/router-info.md)
[SSU](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/ssu.md)
[Subscription](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/subscription.md)
[Transports](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/transports.md)
[Tunnel](https://github.com/monero-project/monero-site/blob/master/resources/moneropedia/tunnel.md)

+moneropedia
+enhancement

# Discussion History
## anonimal | 2017-10-31T14:34:09+00:00
Bad idea to merge into a single article. Good idea to have top-level categories.

## QuickBASIC | 2017-10-31T15:02:47+00:00
> Bad idea to merge into a single article. Good idea to have top-level categories.

I kinda agree with you, but with Kovri having it's own site, I think we don't have to have individual articles for things that could be categorized under a particular article. Wikipedia does this somewhat and uses section headers for each bit of information, so it's still possible to link directly to a particular subject in the article. The articles should have magnet links to jump to each section. 

For instance:

Kovri
*Top level information of what Kovri is and does. Explaining the difference between it and I2P. (C++ vs Java, etc).*
_I2P (subsections explaining each of these things specifically how their implemented in Kovri)
__Tunnel
__Transport
__Jump Service
__Subscription
__Garlic Encryption
__Garlic Routing
__EEP Site

## erciccione | 2017-10-31T15:03:21+00:00
I agree that many of those terms may create confusion, but I also agree that merge everything in one article is not optimal and dispersive. What about make a 'Kovripedia' on getkovri where pull this terms? IMO they are enough and they will increase with time, it would be needed in future anyway

Edit: I think labels should go in a comment

+moneropedia
+enhancement

## QuickBASIC | 2017-11-02T17:55:37+00:00
+moneropedia

@danrmiller Any idea why the bot didn't pick up the labels from the OP?

EDIT: Apparently, enhancement is not a label.
+improvement

## el00ruobuob | 2018-05-05T09:48:16+00:00
Could we perhaps add "tags" to moneropedia articles? And improve the index page to filter/sort by tags? Advantage is an article may have multiple tags.
I can see at least this tag list:
- monero
- kovri
- wallet
- daemon

In the future, maybe moneropedia should be a dedicated moneropedia.org? with links from both getmonero & getkovri? Or just a mirror on both sites?

+discussion


## anonimal | 2018-05-07T21:06:05+00:00
I think monerpedia could use more work and be given more exposure once that works done. I'm agreeing with all the issues here.

## erciccione | 2020-04-07T09:34:11+00:00
This issue is old and was discussed and closed on gitlab. Please reopen if you feel it's still relevant.

# Action History
- Created by: QuickBASIC | 2017-10-31T14:05:33+00:00
- Closed at: 2020-04-07T09:34:11+00:00
