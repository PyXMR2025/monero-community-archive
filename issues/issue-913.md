---
title: Moneropedia entry 'Scalability' needs to be updated
source_url: https://github.com/monero-project/monero-site/issues/913
author: erciccione
assignees:
- erciccione
labels:
- community
- 📖 moneropedia
created_at: '2020-04-12T09:21:52+00:00'
updated_at: '2020-05-28T17:48:36+00:00'
type: issue
status: closed
closed_at: '2020-05-28T17:48:36+00:00'
---

# Original Description
*This issue was created on gitlab and then migrated here. Only the original post was migrated, not the comments. Please take a look at the discussions on the original Gitlab issue before commenting here: https://repo.getmonero.org/monero-project/monero-site/-/issues/1054*

---
The content is outdated.

https://web.getmonero.org/resources/moneropedia/scalability.html

# Discussion History
## erciccione | 2020-05-25T10:19:28+00:00
@SarangNoether Would somebody from the research lab willing to update this entry? Maybe @articmine?

It's not necessary to build a dev environment for the website. It would be fine to simply provide the updated text, then i'd take care of adding it to the repo.

## SarangNoether | 2020-05-25T14:43:22+00:00
I'm not sure how "into the weeds" this article should go into the details of how block size interacts with the block reward. Besides, this is likely not what people think of when they hear the word "scalability" anyway.

## erciccione | 2020-05-26T09:30:22+00:00
I think we should keep it as simple as possible. I'm ok with changing the content btw.

## SarangNoether | 2020-05-26T14:26:57+00:00
Here are a couple of incomplete musings about scaling that try to keep things simple and accurate.

Digital assets like Monero scale in different ways.

The size of Monero blocks (which contain transactions) is flexible and can accommodate many transactions as demand changes. Formulas determine how the reward miners receive interacts with the number of transactions they choose to include in blocks. The blockchain can therefore scale to meet changes in transaction volume.

Scaling may also refer to the ability to conduct certain types of intermediate transactions safely without interacting with a blockchain. Monero does not currently support native off-chain solutions like atomic swaps, since its privacy features do not permit the use of required functionality like non-interactive refund transactions or complex scripting. However, academic and industry research is ongoing and promising in this area.

## erciccione | 2020-05-27T08:17:33+00:00
@SarangNoether personally i would be fine with what you wrote. We could add some references to other resources (on getmonero or external). Can be further improved later if we want. The important now is to remove the obsolete info.

# Action History
- Created by: erciccione | 2020-04-12T09:21:52+00:00
- Closed at: 2020-05-28T17:48:36+00:00
