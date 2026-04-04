---
title: Monero blockchain problem
source_url: https://github.com/monero-project/monero/issues/8935
author: hugohugo130
assignees: []
labels: []
created_at: '2023-07-07T11:30:15+00:00'
updated_at: '2023-07-07T13:38:00+00:00'
type: issue
status: closed
closed_at: '2023-07-07T12:04:28+00:00'
---

# Original Description
I get an error when I try to sync the Monero blockchain

D:\Apps\Monero GUI Wallet>monerod.exe --prune-blockchain --data-dir "G:\monero-blockchain" --db-salvage
2023-07-07 11:26:46.112 My Monero "Fluoro Fermi" (v0.18.2.2-release)
2023-07-07 11:26:46.113 I am initializing the cryptocurrency protocol...
2023-07-07 11:26:46.114 I Cryptonote protocol initialization is normal
2023-07-07 11:26:46.115 I am initializing core...
2023-07-07 11:26:46.116 I am loading blockchain from folder G:\monero-blockchain\lmdb...
2023-07-07 11:26:46.137 W Attempt to get block from height 2879495 failed - block not in database


I used --db-salvage, doesn't work, and I accidentally backed up the wrong data.mdb, do I need to resync the blockchain? or other methods?

(Translated by google)

# Discussion History
## selsta | 2023-07-07T11:32:07+00:00
Yes, you will likely have to resync if you don't have a backup.

Did you plug out the harddrive during sync, have a power outtage or did you force shutdown your computer? All of this can cause corruption.

## hugohugo130 | 2023-07-07T11:34:16+00:00
I didn't unplug the hard drive (because it was a built-in SSD hard drive), didn't open monerod.exe when the power was off, and didn't force shut down the computer

## hugohugo130 | 2023-07-07T11:44:53+00:00
I am downloading the blockchain file (moneroblockchain.raw) and my command to import the blockchain is
monero-blockchain-import --imput-file "W:\rawfile\moneroblockchain.raw" --batch 2 --batch-size 35000 --log-level 4 --dangerous-unverified-import 1 --prune-blockchain - -data-dir "W:\monero-blockchain"

## selsta | 2023-07-07T11:46:25+00:00
I would sync with monerod, downloading  blockchain.raw is usually not faster and is also not recommended.

Edit: Seems you are doing unverified import which is faster but also not recommended for security reasons.

## hugohugo130 | 2023-07-07T11:47:27+00:00
oh ok thx. I'll use monerod.exe to sync my monero blockchain

## selsta | 2023-07-07T13:38:00+00:00
20 days on an SSD?

# Action History
- Created by: hugohugo130 | 2023-07-07T11:30:15+00:00
- Closed at: 2023-07-07T12:04:28+00:00
