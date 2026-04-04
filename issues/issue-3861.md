---
title: 'Offline transaction signing: Unknown method parameter type: size_t'
source_url: https://github.com/monero-project/monero-gui/issues/3861
author: selsta
assignees: []
labels:
- bug
created_at: '2022-03-15T05:40:47+00:00'
updated_at: '2022-03-16T15:26:09+00:00'
type: issue
status: closed
closed_at: '2022-03-16T15:26:09+00:00'
---

# Original Description
I am trying to sign an offline transaction in monero gui wallet version [0.17.3.1](https://0.17.3.1/). Both the cold (on tails) and view only wallet (on windows) have the same version. This is what I do.

1. Export outputs from view only wallet
2. Import outputs to cold wallet
3. Export key images from cold wallet
4. Import key images to view only wallet
5. Create a transaction in view only wallet and save it to a file
6. Use the transaction file to sign it offline on a cold wallet
7. However, at step 6 nothing happens when I click sign and choose the created transaction file. All the previous steps work fine. Does anybody know what could be the problem?

I tried to search here and in monero subreddit but could not find an answer. I am aware that previous gui versions did not really support offline transaction signing (there was no export import outputs function) and that using the cli wallet seems to be a more foolproof solution. However, I am wondering if I can do it with gui wallet only, I guess it should be possible now. Any help is much appreciated.

EDIT

This is the error I get: Model size of -1 is less than 0
qrc:/pages/Transfer.qml:648: Error: Unknown method parameter type: size_t

I have now used the combination of gui for view wallet and cli for cold one and when using the cli I was able to sign and broadcast the transaction. Nevertheless, I am still wondering why it would not work in gui cold wallet.

From: https://old.reddit.com/r/monerosupport/comments/tccpp0/offline_transaction_signing/

# Discussion History
## reemuru | 2022-03-15T09:07:45+00:00
@selsta I put a temp fix on #3862. How to get more than one transaction in the file? Even with multiple recipients the count is one, but `confirmationMessage` shows multiple transactions.

## selsta | 2022-03-16T04:29:33+00:00
I honestly never used offline signing so I'm not really familiar with it. Can you post a screenshot how it would look with #3862?

## reemuru | 2022-03-16T11:26:08+00:00
@selsta  I have used it once before. It looks like old code was using logic to parse and array but there is none, however there is confirmationMessage field on the transaction object. Maybe it was not there before? I don't know how to put multiple separate txs in a file (if that is supported). I'm ok with just fixing confirmation message for now since batching to multiple recipients appears to be working.

![fix3862](https://user-images.githubusercontent.com/13033037/158579302-cc0477c9-7828-4626-98fb-37de3d8fc10b.png)



## selsta | 2022-03-16T15:26:08+00:00
#3862

# Action History
- Created by: selsta | 2022-03-15T05:40:47+00:00
- Closed at: 2022-03-16T15:26:09+00:00
