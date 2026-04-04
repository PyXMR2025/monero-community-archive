---
title: Failed send XMR, Monero GUi WALLET / Ledger Nano X
source_url: https://github.com/monero-project/monero/issues/8629
author: Ho-Ss
assignees: []
labels: []
created_at: '2022-11-02T13:33:03+00:00'
updated_at: '2026-01-23T11:32:10+00:00'
type: issue
status: closed
closed_at: '2022-11-02T14:37:05+00:00'
---

# Original Description
Hello, 
I want to send my XMR that I had deposited some time ago on my Monero Gui Wallet, linked to my ledger nano X.

I can connect to the wallet, see my balance etc.
When I initiate a transaction, it is sent, with confirmation on my ledger key etc.

But after a few minutes the transaction is marked as "failed" in my GUI Wallet transaction history.

My application is up to date.
The ledger is up to date.
Monero application on ledger is up to date.
Wallet & daemon synchronized.

I already tried to reboot the wallet, the key, the computer.
Also tried on another computer it doesn't work.

I really don't know what else to try.

Could someone please help me? Thanks

# Discussion History
## selsta | 2022-11-02T13:37:48+00:00
Please go to Settings -> Info and post:

- Version
- Wallet mode

## Ho-Ss | 2022-11-02T13:41:56+00:00
GUI version: 0.18.1.2-unknown (Qt 5.15.6)

Wallet mode: Simple mode (bootstrap)


## selsta | 2022-11-02T13:45:33+00:00
Can you go to Settings -> Log, enter "status" into the textbox and post the output?

## Ho-Ss | 2022-11-02T13:47:35+00:00
>>> status
[02/11/2022 14:46] 2022-11-02 13:46:52.836 I Monero 'Fluorine Fermi' (v0.18.1.2-release) 
Height: 2747034/2747034 (100.0%) on mainnet, bootstrapping from 99.85.127.38:18089, local height: 1698132 (61.8%), not mining, net hash 3.12 GH/s, v16, 0(out)+0(in) connections

## selsta | 2022-11-02T13:51:09+00:00
My suggestion would be to set a custom remote node: https://github.com/monero-project/monero-gui/issues/3989#issuecomment-1214412781

If it still fails to transact afterwards it could be that the wallet cache is buggy and a full wallet rescan is required.

## Ho-Ss | 2022-11-02T13:53:26+00:00
I'll try this and let you know.
Thank you.


## Ho-Ss | 2022-11-02T14:37:05+00:00
It works.
Thank you very much @selsta.

## SabriMercimek | 2026-01-23T10:09:52+00:00
Hello @selsta, I have the same issue. I have send a few days before XMR to another wallet succesfully. I have not linked my Monero GUI wallet to my ledger.  I do not understand why all my transactions are failing. It worked a few days ago. If I now try to send XMR to the same wallet address it is failing all the time. 

<img width="743" height="158" alt="Image" src="https://github.com/user-attachments/assets/379f3d73-975f-41b9-8b5b-221b069d2ba6" />


This is from log:

>>> status
[23/01/2026 11:09] 2026-01-23 10:09:21.298 I Monero 'Fluorine Fermi' (v0.18.4.5-release) 
Height: 3594030/3594030 (100.0%) on mainnet, bootstrapping from 116.251.217.58:18089, local height: 1 (0.0%), not mining, net hash 6.69 GH/s, v16, 0(out)+0(in) connections

would you know perhaps what is going on?

Dear regards,

Sabri 



## plowsof | 2026-01-23T11:32:10+00:00
@SabriMercimek be aware that you have shared an image containing the recipient address. you appear to be in simple and/or bootstrap mode. using node `116.251.217.58:18089` - which has failed to broadcast your transaction to the network. to manually select the remote node you connect to, close the wallet `[<-` top left and change the wallet mode to `advanced` then open the wallet from file as usual. go to settings > node > and add a remote node, for example `node3.monerodevs.org` port `18089` (click on the node after adding it so it connects) - now you will likely need to resync your wallet , to do this, go to settings > info > click `change` next to restore height and then `ok` .. `ok` (without changing any numbers and reading the information screen). after sync is complete, you should be able to send as normal. further assistance please join `#monero-support` on IRC or via Matrix using https://beta.monerodevs.org/community/hangouts/ 

# Action History
- Created by: Ho-Ss | 2022-11-02T13:33:03+00:00
- Closed at: 2022-11-02T14:37:05+00:00
