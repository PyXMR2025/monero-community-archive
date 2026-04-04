---
title: Recommendation for monero-gui-wallet-guide.pdf (or gui tool for ip binding
  in Monero wallet)
source_url: https://github.com/monero-project/monero-gui/issues/4017
author: Poecilia
assignees: []
labels: []
created_at: '2022-08-28T20:07:19+00:00'
updated_at: '2022-08-29T16:55:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I see the guide github is now archived, but wanted to recommend adding a paragraph on page 26 to explain that if you want to remotely connect to a node in your own home, you will need to run the monerod command "--rpc-bind-ip ...  --confirm-external-bind" on the device that has the node downloaded, as otherwise you will not be able to connect to your own device.

Even better would be a graphical representation of ip binding within the wallet gui. I image a lot of people will want to connect the wallet on different devices to one node in their own homes, and the guide in its current form doesn't explain how to do that for beginners.

# Discussion History
## erciccione | 2022-08-29T08:13:15+00:00
The repository can be unarchived if somebody is willing to maintain it and actively work on it

## Poecilia | 2022-08-29T16:08:10+00:00
> The repository can be unarchived if somebody is willing to maintain it and actively work on it

I work with (English) language and am used to proofreading, so I'd be more than happy to help out with that. I can also help ensure the manual is (beginner) user-friendly. I am not a programmer or a developer, however, so would not feel confident adding the actual technical content.

Edit: to clarify, I'd be happy to do the actual writing, but would need to work with someone who knows how everything works, technically speaking. 

# Action History
- Created by: Poecilia | 2022-08-28T20:07:19+00:00
