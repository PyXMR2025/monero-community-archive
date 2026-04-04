---
title: Segmentation Fault During Daemon Sync For monero-wallet-gui.AppImage
source_url: https://github.com/monero-project/monero/issues/6780
author: downystreet
assignees: []
labels: []
created_at: '2020-08-26T21:49:06+00:00'
updated_at: '2021-10-06T03:19:25+00:00'
type: issue
status: closed
closed_at: '2021-10-06T03:19:25+00:00'
---

# Original Description
I experienced a segmentation fault using the new gui AppImage Monero wallet when the daemon was syncing. I have used this wallet before without experiencing a segmentation fault.
Version: monero-gui-v0.16.0.3]
OS: CentOS 8

Readout from the command terminal:

2020-08-26 21:33:11.977	E Public key 5794d7d9560c7135a66f3ca2a7ea870678c2266c1561a16f285862c0a8fdf0fb from received 0.110187000001 output already exists with spent 0.110187000001 in tx <f60cde70e03fdeb6588b08b9bcac48eb3da188f51843d0bb9a4c17f4ad4427b3>, received output ignored
2020-08-26 21:34:09.040	E Public key d1580223db02dc5cb22d4eff4b512cc30f7a7150a0423dd5571aa342bd1c28bd from received 0.111871000001 output already exists with spent 0.111871000001 in tx <96f6bea344a5ab609ffdb2538888ecc364068114c0e29cd715ca3694078f2432>, received output ignored
2020-08-26 21:34:09.139	W Spent money: 0.110187000001, with tx: <8614d8c3fc3503dce31dcf45c4c3f0e490b1de985c27d7677a50c9a48e5639df>
2020-08-26 21:34:09.139	W Spent money: 0.111871000001, with tx: <8614d8c3fc3503dce31dcf45c4c3f0e490b1de985c27d7677a50c9a48e5639df>
./monero-wallet-gui.AppImage: line 1: 752271 Segmentation fault      (core dumped) ./monero-wallet-gui


# Discussion History
## selsta | 2020-08-26T21:51:31+00:00
Does this happen every time you sync? Or one time crash? Also are you using Trezor / Ledger?

## downystreet | 2020-08-26T22:37:42+00:00
It just happened one time. I was able to use the wallet just fine after restarting. I was not using a Trezor/Ledger.

## moneromooo-monero | 2020-08-26T23:09:49+00:00
Do you have a stack trace for that crash ? 

## downystreet | 2020-08-27T00:37:36+00:00
No I don't.

## selsta | 2021-10-06T03:19:25+00:00
Not much we can do without stack trace. Closing as there are a lot of stability improvements since 6780.

# Action History
- Created by: downystreet | 2020-08-26T21:49:06+00:00
- Closed at: 2021-10-06T03:19:25+00:00
