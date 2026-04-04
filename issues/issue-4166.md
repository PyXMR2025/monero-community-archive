---
title: Monero GUI Wallet - Unable to switch between wallets - A bug or by design?
source_url: https://github.com/monero-project/monero-gui/issues/4166
author: ch9PcB
assignees: []
labels: []
created_at: '2023-05-03T04:58:17+00:00'
updated_at: '2023-05-03T09:02:42+00:00'
type: issue
status: closed
closed_at: '2023-05-03T09:02:42+00:00'
---

# Original Description
Below are the software that I use on my device (Intel 12th generation CPU, 24GB of RAM, 1TB of PCIe NVMe SSD):

```
Debian 11.7.0, 64bit (backported kernel version 6.1.15-1~bpo11+1)
Monero GUI Wallet, 0.18.2.2 - Fluorine Fermi

```
I managed to create a second and third wallet on the same device. Both three wallets -including the first- share the same wallet path. Let's call it `/media/richard/Kolomb/Monero`

Below is the description of the problem that I am facing:

1. Upon launching Monero GUI Wallet, there is a message stating `Please enter password for:` <name of third wallet>. `Please enter password for:` always asks for the latest/most recently created wallet.

2. There is no menu whatsoever to let me choose which wallet I wish to log into. In my case, I have three wallets: the first, second and third.

Is the above scenario a bug or by design?

# Discussion History
## selsta | 2023-05-03T08:13:20+00:00
> There is no menu whatsoever to let me choose which wallet I wish to log into. In my case, I have three wallets: the first, second and third.

After opening the GUI you can click on "Cancel" during password entry and you will go back to the main menu. Afterwards you can click on "Open wallet from file". This should show a list of wallets. If you keep them in the default location you can simply select them from the list, if you selected a custom wallet location you have to click on "Browse filesystem" and select the wallet file you want to open.



## ch9PcB | 2023-05-03T09:01:09+00:00
@selsta 

> If you keep them in the default location you can simply select them from the list, 

Just to clarify: the default location of the wallet is /home/<the name of the user of Debian OS>/Monero/wallets, is that correct?



## selsta | 2023-05-03T09:01:57+00:00
Yes. But even if you don't save them in the default location you can click on "Browse filesystem" and select whatever wallet you want to open.

## ch9PcB | 2023-05-03T09:02:39+00:00
@selsta

Thanks for your clarification.

I will close the issue now.

# Action History
- Created by: ch9PcB | 2023-05-03T04:58:17+00:00
- Closed at: 2023-05-03T09:02:42+00:00
