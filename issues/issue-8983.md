---
title: How should I use wallet-rpc development to implement payment and collection?
source_url: https://github.com/monero-project/monero/issues/8983
author: augushong
assignees: []
labels: []
created_at: '2023-09-07T06:16:18+00:00'
updated_at: '2023-09-07T09:27:40+00:00'
type: issue
status: closed
closed_at: '2023-09-07T09:27:40+00:00'
---

# Original Description
How should I use wallet-rpc development to implement payment and collection?
My needs are as follows. I have an application with multiple users who recharge through xrm. What are the specific development ideas?

The first one: My initial idea was very simple. Provide a public wallet address. The recharge amount for different orders is different. If it is an order with the same price, it will fluctuate randomly on a certain precision. The price paid may be 10.0001, 10.0002, etc., to distinguish the amount of different users within the same validity period. In this way, I only need to monitor the payment records.

Second: But the above solution is not good enough. I thought make_uri could pass in the payment_id parameter, so that I only need to check the money received by payment_id within the validity period. But it seems that the new version does not allow this parameter to be passed in.

Third option: There is another solution, which is to generate a wallet address every time I collect money, which is only used for this payment, but I am worried that a lot of useless junk addresses will be generated.

The fourth method: Or I generate a wallet address for each user, statistically check the changes in the money received at each address, and determine how much money has been recharged.

I want to know what is the correct development idea? The information I found on the Internet is basically the second solution, and they are all articles written two or three years ago.

The fourth option is quite acceptable to me, so what is the process of calling rpc?
Check whether there is any change through get_height at regular intervals, check whether there is income through get_transfers, and determine the recharging user through the address of the income. Is that so?

If it is the first type, it seems simpler. I only need to determine the amount and the payment order amount within the validity period.

I want to know what the most efficient solution should be and how to call rpc reasonably.

# Discussion History
## augushong | 2023-09-07T06:18:15+00:00
In fact, my scenario is not just recharging, but more like purchasing goods and packages.

# Action History
- Created by: augushong | 2023-09-07T06:16:18+00:00
- Closed at: 2023-09-07T09:27:40+00:00
