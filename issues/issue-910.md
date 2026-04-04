---
title: It's time to talk about the removal of Kovri from the website
source_url: https://github.com/monero-project/monero-site/issues/910
author: erciccione
assignees: []
labels:
- 💬 discussion
created_at: '2020-04-12T09:18:15+00:00'
updated_at: '2020-08-27T07:27:58+00:00'
type: issue
status: closed
closed_at: '2020-08-27T07:27:58+00:00'
---

# Original Description
*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/990*

---
As we know, Kovri is not developed anymore, but we mention it everywhere on the website. I think it's time to make some cleanup and remove Kovri from most places, like the contacts, roadmpa, etc.

What's the feeling about this? hould we replace the mentions to Kovri with I2P0?

# Discussion History
## erciccione | 2020-05-14T11:09:43+00:00
Thinking of going ahead with this, but i would like community input on a related issue: Should we remove kovri-specific entries from [the Moneropedia](https://web.getmonero.org/resources/moneropedia/)? At the moment we have several, but i don't see the point in keeping them.

Most of these entries are not even specific to Kovri, but more related to I2P in general:

- Base32
- Base64
- Eepsite
- Floodfill
- Garlic Routing
- Garlic-Encryption
- I2N
- I2P
- I2PControl
- In-net
- Java I2P
- Jump Service
- Kovri (maybe this one could be kept, with a note)
- Lease
- Message
- NTCP
- Network Database
- Reseed
- Router-Info
- SSU
- Subscription
- Transports
- Tunnel

While compiling this list i realized that our Moneropedia it's more an I2Pedia. The majority of the entries is related to Kovri/I2P, which doesn't make sense in my opinion.

I would remove all these entries.

## SamsungGalaxyPlayer | 2020-05-14T13:43:36+00:00
Agreed, these seem to clutter the Moneropedia and are not terms that people will likely look up. If some service is integrated properly, then users should ideally never come across these terms.

I agree about keeping Kovri for historical purposes. If anything, we can say "Kovri was a proposed but never-implemented Java i2p router" or similar.

## erciccione | 2020-05-22T09:03:15+00:00
I PRd the change to the 'kovri' Moneropedia entry: #993

## erciccione | 2020-08-10T08:21:38+00:00
I believe that #1120 and #1125 remove the last Kovri-related content (Except for the 'Kovri' Moneropedia entry). IMO this issue can be closed after those 2 PRs are merged.

## erciccione | 2020-08-27T07:27:58+00:00
This is resolved.

# Action History
- Created by: erciccione | 2020-04-12T09:18:15+00:00
- Closed at: 2020-08-27T07:27:58+00:00
