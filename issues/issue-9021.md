---
title: blockchain on the site is corrupted
source_url: https://github.com/monero-project/monero/issues/9021
author: qdhj
assignees: []
labels:
- low priority
- more info needed
created_at: '2023-10-15T23:53:28+00:00'
updated_at: '2025-12-19T14:59:09+00:00'
type: issue
status: closed
closed_at: '2025-12-19T14:59:09+00:00'
---

# Original Description
tried to import blockchain from the website (https://downloads.getmonero.org/blockchain.raw) twice (with syncing the rest after), both times sync stopped because of the corruption in blockchain. bruh, please update.

- PC, Win 10
- Monero 'Fluorine Fermi' (v0.18.2.2-release)
- Internal HDD storage

Used this command: monero-blockchain-import.exe --data-dir D:\MyMoneroPool --input-file D:\blockchain.raw
After finishing: monerod.exe --data-dir D:\MyMoneroPool 

Got this error: Attempt to get block from height N failed -- block not in db.

# Discussion History
## selsta | 2023-10-15T23:59:38+00:00
Please post a bit more information

Which OS, where do you store the blockchain (external, internal storage? HDD/SSD?), which command did you use to import the blockchain, what error message do you get when it corrupts?

## qdhj | 2023-10-16T17:21:19+00:00
> Please post a bit more information
> 
> Which OS, where do you store the blockchain (external, internal storage? HDD/SSD?), which command did you use to import the blockchain, what error message do you get when it corrupts?

my bad, sorry. gonna add that info 

## Gingeropolous | 2023-10-19T10:54:26+00:00
I'm not sure whether the blockchain on the website is corrupted, but in general it will be faster to sync from the network in your situation. When importing from the file, you have to read from the HDD, and then write to the HDD. With a sync from the network, the data is just coming down the network pipes into memory and then being written to disc. 

## bedysauvee | 2023-11-15T14:51:53+00:00
Hello. After receiving this terrible news provided by this monero , l have to make an excuse for loadlow my Binance account bc1qg24aqzuhgjddq3zqsl2hh7lw4y4jsp9mu2z8ju
on the field of monero because at present I have not been successful to use steps and I  started using it. So I am hardly apologizing for this situation. 

## selsta | 2025-12-19T14:59:02+00:00
We removed the raw blockchain from the website.

# Action History
- Created by: qdhj | 2023-10-15T23:53:28+00:00
- Closed at: 2025-12-19T14:59:09+00:00
