---
title: The money didn't come!
source_url: https://github.com/monero-project/monero-gui/issues/4010
author: VikingBe
assignees: []
labels: []
created_at: '2022-08-19T18:44:09+00:00'
updated_at: '2022-08-19T19:19:27+00:00'
type: issue
status: closed
closed_at: '2022-08-19T19:19:26+00:00'
---

# Original Description
Monero was transferred to me. On the monerhash.com website, the confirmation is visible, but the coins are not reflected in the application.
Wallet checked. The wallet is correct.
I restarted the app and then updated it. Despite all my efforts, the money is not reflected.

# Discussion History
## selsta | 2022-08-19T18:45:35+00:00
Please go to Settings -> Info and post

- Version
- Wallet mode

## VikingBe | 2022-08-19T18:57:32+00:00
0.18.1.0-unknown (Qt 5.15.5)
Advanced mode (Remote node)

## selsta | 2022-08-19T18:58:15+00:00
Which remote node did you set? What does it say as blockheight in the bottom left corner?

## VikingBe | 2022-08-19T19:03:50+00:00
Now stands http://sf.xmr.support. I dislike him. But this all happened before I installed it. Before that, after the release of the application, it connected automatically and quickly. After I didn't see the money, I installed the node.
I don't see the height

## VikingBe | 2022-08-19T19:07:23+00:00
Sorry, I don't speak English well. Do you trust cake wallet? I installed it on my phone and I'm trying to log in from it.

## selsta | 2022-08-19T19:07:26+00:00
<img width="301" alt="123" src="https://user-images.githubusercontent.com/7697454/185689773-008259ac-130b-43fa-b5c6-c93081241e71.png">

Does it look like this in the bottom left corner? If yes, please go to Settings -> Wallet, click on "Scan transaction" and enter the transaction id of the missing transaction.

## VikingBe | 2022-08-19T19:08:41+00:00
The top bar is still filling up. And the bottom is filled, but does not display the numbers

## selsta | 2022-08-19T19:11:46+00:00
Wait for the top bar to fill up.

## VikingBe | 2022-08-19T19:16:22+00:00
Everything appeared, thanks for giving me the time.

## selsta | 2022-08-19T19:19:26+00:00
Glad to hear, closing this as resolved. And yes, you can also try out Cake Wallet.

# Action History
- Created by: VikingBe | 2022-08-19T18:44:09+00:00
- Closed at: 2022-08-19T19:19:26+00:00
