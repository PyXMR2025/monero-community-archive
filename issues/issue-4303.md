---
title: Transaction supposedly failed but still went through
source_url: https://github.com/monero-project/monero-gui/issues/4303
author: moritztim
assignees: []
labels: []
created_at: '2024-04-07T10:40:03+00:00'
updated_at: '2024-04-08T17:21:59+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I sent some monero to an address from my address book using the GUI. It said something to the effect of transaction failed however when I checked the history it did go through, to an "Unknown Recipient". My wallet is now missing that amount of monero and the recipient has not recieved any money. 
I know this is probably not enough info, feel free to ask for more

# Discussion History
## moritztim | 2024-04-07T11:18:49+00:00
The recipient got it. They had to scan the transaction tho

## selsta | 2024-04-07T14:28:30+00:00
Can you share from Settings -> Info

- Version
- Wallet mode
- Wallet restore height

## moritztim | 2024-04-08T12:07:35+00:00
```
GUI version: 0.18.3.2-release (Qt 5.15.13)
Embedded Monero version: 0.18.3.2-release
Wallet path: /home/moti/Monero/wallets/moti/moti
Wallet restore height: 3100672
Wallet log path: /home/moti/.bitmonero/monero-wallet-gui.log
Wallet mode: Advanced mode (Remote node)
Graphics mode: OpenGL
```
I may have been running my own node while making the transaction, I'm not sure.

## selsta | 2024-04-08T12:09:57+00:00
You seem the have selected a remote node here. Did you make the transition from your local node?

Also currently, does it still say failed or does it say confirmed? Did it only temporarily said failed?

## moritztim | 2024-04-08T12:18:14+00:00
@selsta:
> You seem the have selected a remote node here. Did you make the transition from your local node?

Unfortunately I don't remember if at that point I was running a local node or not.
> Also currently, does it still say failed or does it say confirmed? Did it only temporarily said failed?

It never said failed in the transaction list. But after making the transaction the popup said that it failed.

## moritztim | 2024-04-08T12:26:22+00:00
![image](https://github.com/monero-project/monero-gui/assets/90388353/bd453634-da5c-4ea2-b1e3-34967d41c619)


## selsta | 2024-04-08T17:21:58+00:00
I'm not sure what happened, but the correct status of a transaction can always been seen in the Transactions tab.

# Action History
- Created by: moritztim | 2024-04-07T10:40:03+00:00
