---
title: GUI shows <br> when multiple transfers are made in the To field.
source_url: https://github.com/monero-project/monero-gui/issues/4431
author: Tzadiko
assignees: []
labels: []
created_at: '2025-04-04T15:55:49+00:00'
updated_at: '2025-07-04T17:02:39+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
![Image](https://github.com/user-attachments/assets/15a9670f-a5ba-43a5-a945-a2a32715814e)

I notice when I send to multiple addresses in 1 transaction, there is <br> in the To field.
I want to submit a PR to get rid of this
Perhaps, instead add a [# Addresses] which says how many transfers were made to the Title To. For example To [# Addresses].

Don't want to spend time on this if people hate this idea. What do people think?

# Discussion History
## selsta | 2025-04-04T16:52:14+00:00
I would be open to a PR that fixes this, as long as the change isn't too big. So basically it says "To... 3 Addresses" and when you click on it it displays all the addresses?

## Tzadiko | 2025-04-04T17:40:41+00:00
> I would be open to a PR that fixes this, as long as the change isn't too big. So basically it says "To... 3 Addresses" and when you click on it it displays all the addresses?

When it's collapsed:

![Image](https://github.com/user-attachments/assets/132402d1-7823-400e-bdc5-cd32654abac9)

When expanded:

![Image](https://github.com/user-attachments/assets/c146c4a0-22da-4bd6-8de8-fe6167248170)

Question for you on duplicate handling. Assuming Address 1 and Address 2 are the same, should they be listed once or twice? Furthermore, if there are 10 addresses, and they are all the same, should the user be shown To 10 Recipients, or should it just show the single recipient address?

![Image](https://github.com/user-attachments/assets/0299e6dd-66b8-43f7-93b6-371985e40e62)

Also, should Address 1 and Address 2 (assuming they're different), just be listed, or should Recipients be a collapsable box?


## hiddener | 2025-07-04T14:58:24+00:00
@Tzadiko I think same address should be listed as a single recipient (all destinations + amounts would be in Details). Recipients in a collapsible box or scrollbox (in case there are many (20+) addresses) would be best

## Tzadiko | 2025-07-04T16:06:01+00:00
@hiddener What do you mean? You're saying if all recipients are the same person (share the same address), then To shows the address instead of (2 Recipients) as shown in my example? If you can expand on what you mean, that would be great.

## hiddener | 2025-07-04T16:49:09+00:00
I mean 10 destinations with the same address is 1 address in To (but will be harder to identify it as a batch transfer). 10 destinations with the same address + 2 different addresses is 3 addresses (as you showed above with the recipients)

# Action History
- Created by: Tzadiko | 2025-04-04T15:55:49+00:00
