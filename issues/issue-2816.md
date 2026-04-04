---
title: Support for importing and exporting outputs
source_url: https://github.com/monero-project/monero-gui/issues/2816
author: jluttine
assignees: []
labels:
- feature
created_at: '2020-03-30T18:39:29+00:00'
updated_at: '2021-10-08T05:17:30+00:00'
type: issue
status: closed
closed_at: '2021-09-05T16:54:29+00:00'
---

# Original Description
In a setup with an offline private-key wallet and an online view-only wallet, one needs to import key images from the offline wallet to the view-only wallet in order to see the true balance that takes into account spending. But the offline wallet needs to know the outputs for it to be able to create the key images. So, one needs to be able to export the outputs from the view-only wallet and import them to the offline wallet. However, GUI doesn't support these two operations. CLI supports `export_outputs` and `import_outputs`. It would be nice to have these features available in the GUI too.

The source of my information was this dicussion:

https://www.reddit.com/r/Monero/comments/fra1k5/questions_on_key_images/flusnou/

Which gave the following instructions:

- Import address, private view key into watch only wallet. Scan for incoming transactions.

- Export the list of outputs from the watching wallet to the offline wallet.

- Import the outputs into the offline wallet, generate key images, export key images to watching wallet.

- Watching wallet is now ready to create unsigned transactions for the offline wallet to sign.

# Discussion History
## jluttine | 2020-03-30T18:49:01+00:00
A side note: Why is "Import key images" disabled in my view-only wallet?

![image](https://user-images.githubusercontent.com/2195834/77949748-2784cc80-72d0-11ea-8fa4-ce74923e145b.png)

It even states above that I should import key images, so why is it disabled?

## selsta | 2020-03-30T19:45:52+00:00
@jluttine You have to set the daemon as a trusted daemon or use a local node to import key images. We should add a warning message there.

## toxinburn | 2021-10-08T05:17:30+00:00
Hi I am trying to figure out how on earth to get my funds out from view only I admit i messed up by making a view only wallet but i have like 360 dollars just stuck in there i can see the funds but under send their is the same message from years ago, it says I can make a file and sign it to transfer the funds can anyone walk me thru steps to either change the wallet back to spendable or how to actually export them from the view only wallet to another one?

# Action History
- Created by: jluttine | 2020-03-30T18:39:29+00:00
- Closed at: 2021-09-05T16:54:29+00:00
