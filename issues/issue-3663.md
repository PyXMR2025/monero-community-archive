---
title: HELP！failed to get outputs to mix
source_url: https://github.com/monero-project/monero-gui/issues/3663
author: simaxuan
assignees: []
labels: []
created_at: '2021-08-10T08:53:36+00:00'
updated_at: '2021-08-13T07:18:13+00:00'
type: issue
status: closed
closed_at: '2021-08-13T07:18:13+00:00'
---

# Original Description
failed to get outputs to mix：failed to get random outs
![QQ截图20210810162358](https://user-images.githubusercontent.com/80314347/128837979-05dadbdf-6f1c-4082-8138-bea6e4b1b2d0.png)


# Discussion History
## selsta | 2021-08-10T21:00:58+00:00
Please post more information. Go to Settings -> Info and post:

version
wallet mode

## simaxuan | 2021-08-11T02:02:47+00:00
![微信图片_20210811100220](https://user-images.githubusercontent.com/80314347/128958348-d51f0a68-7f5b-4922-8844-3b7b44c4d791.png)


## selsta | 2021-08-11T02:55:57+00:00
First, go to the main menu by clicking on the exit symbol in the top left corner.

Then click on "Change wallet mode" and select "Advanced mode". Afterwards open your wallet again, go to Settings -> Node, select "Remote node" and enter the following node:

address: `88.198.199.23`
port: `18081`

Then try to send again.

----------

Other remote node in case the above has issues:

address: `88.198.199.23`
port: `18081`

address: `node.supportxmr.com`
port: `18081`

address: `78.47.80.55`
port: `18081`

address: `node.melo.tools`
port: `18081`

## simaxuan | 2021-08-11T09:10:24+00:00
I tried the remote node above and still displayed the same error message：failed to get outputs to mix：failed to get random outs

## rating89us | 2021-08-11T12:51:21+00:00
You probably have a lot of outputs with small amounts in your wallet (generated from multiple transactions with small amounts), and these outputs can't be used in the transaction you are creating because their amounts are not enough.

I see two possible solutions:

1) Try sending a transaction with a smaller amount

2) If you need to send a larger amount, you will need to have larger output(s). Click the "Send all" button (see below) and send a transaction to yourself (an address of your own wallet). After receiving this transaction, your wallet will have a single large output, which you will be able to spend normally.

![image](https://user-images.githubusercontent.com/45968869/129029803-7779cdce-d486-41be-86f1-84395e08b0bd.png)

## simaxuan | 2021-08-13T07:08:53+00:00

Thank you. The problem has been solved.

# Action History
- Created by: simaxuan | 2021-08-10T08:53:36+00:00
- Closed at: 2021-08-13T07:18:13+00:00
