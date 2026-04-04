---
title: Cannot a view-only wallet be created?
source_url: https://github.com/monero-project/monero-gui/issues/4049
author: ukaznil
assignees: []
labels: []
created_at: '2022-10-19T02:27:55+00:00'
updated_at: '2022-10-19T05:41:40+00:00'
type: issue
status: closed
closed_at: '2022-10-19T05:41:40+00:00'
---

# Original Description
This official article ( https://www.getmonero.org/resources/user-guides/view_only.html ) says that a view-only wallet can be created thru the GUI app. However, with the current v0.18.1.2, I cannot see the option of "Create a view-only wallet" in the setting. Is this feature currently deactivated?

My env is as follows:
GUI version: 0.18.1.2-release (Qt 5.15.6) built from the code
OS: mac

# Discussion History
## ukaznil | 2022-10-19T02:49:39+00:00
Here is my current setting window where I cannot find the "Create a view-only wallet" option that must be here according to the article.

<img width="647" alt="image" src="https://user-images.githubusercontent.com/10129946/196585468-6e92455d-efd6-4d9d-846e-22c12a39c6c8.png">


## selsta | 2022-10-19T02:51:10+00:00
Can you go to Settings -> Info and post which wallet mode you have selected?

## ukaznil | 2022-10-19T02:55:46+00:00
> Can you go to Settings -> Info and post which wallet mode you have selected?

@selsta Thanks for your reply.
I'm using Simple mode now. But, even when I tried Advanced mode before, there wasn't this option for a view-only wallet.
<img width="330" alt="image" src="https://user-images.githubusercontent.com/10129946/196586504-bd3179b9-50e0-4a5c-8c57-54ba8555dca1.png">


## selsta | 2022-10-19T03:06:16+00:00
Simple mode is just for basic sending and receiving, make sure to select Advanced mode as a first step.

## ukaznil | 2022-10-19T03:17:13+00:00
Okay. I switched to Advanced mode. But, even with Advanced mode, I cannot see the option here.
I'm not sure whether some caches of Simple mode may be causing something bad. If so, where is the cache saved in mac?

<img width="451" alt="image" src="https://user-images.githubusercontent.com/10129946/196589040-99639b02-a37f-4d42-b7ca-89c311176bb8.png">
<img width="954" alt="image" src="https://user-images.githubusercontent.com/10129946/196588940-718623c7-881a-48c4-ae5a-1d30da06e002.png">


## selsta | 2022-10-19T03:18:54+00:00
Do you use a Ledger wallet?

## ukaznil | 2022-10-19T03:21:18+00:00
Yes, I'm using Ledger Nano S Plus. Isn't the hardware wallet supported for this feature?
I thought you can create view-only wallet also for hardware wallet as the article says "You can also create a view-only wallet of a hardware wallet, however this kind of view-only wallet doesn't support offline transaction signing and importing of key images."

## selsta | 2022-10-19T03:27:52+00:00
The code specifically doesn't allow creating a view only wallet with a Ledger: https://github.com/monero-project/monero-gui/pull/3160

It might be possible with Trezor, I'm not sure. The documentation has to be updated to make that more clear.

## ukaznil | 2022-10-19T03:31:39+00:00
Oh sorry I haven't seen this merge. I totally got it. Thanks for your prompt replies and support!

## ukaznil | 2022-10-19T05:41:40+00:00
As my concern has been resolved, I close this issue. Thanks.

# Action History
- Created by: ukaznil | 2022-10-19T02:27:55+00:00
- Closed at: 2022-10-19T05:41:40+00:00
