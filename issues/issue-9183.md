---
title: Segfault on any operation on the blockchain
source_url: https://github.com/monero-project/monero/issues/9183
author: ours-code
assignees: []
labels:
- more info needed
created_at: '2024-02-19T19:13:40+00:00'
updated_at: '2024-02-19T20:41:14+00:00'
type: issue
status: closed
closed_at: '2024-02-19T20:41:14+00:00'
---

# Original Description
Hello,

I am running a local node and a few hours ago any operation on the database results in a Segfault: 
![image](https://github.com/monero-project/monero/assets/3473632/6955a794-3797-42b5-9ae0-5b3de8c1ed55)

The main issue since that it looks for a block not in DB:
![image](https://github.com/monero-project/monero/assets/3473632/c7f1e2a4-0578-458c-84c1-841fe5cc2ce1)

I had no success when trying to salvage the database through the daemon:
![image](https://github.com/monero-project/monero/assets/3473632/32fd8910-d403-4129-8539-96661c8dcbaa)

seeing that issue with the block *3082415* I tried to export the blockchain up to the blocks before it, but without success:
![image](https://github.com/monero-project/monero/assets/3473632/b1f95e56-6a7d-4c44-ab95-ad98db698fc3)

I see in the logs that the database is close to a threshold "Percent used: 89.8345  Percent threshold: 90.0000" Should I change a parameter of the database ?
Do you see a way to fix this ? Or where should I look to debug this further ?

_Environment information_:
Running on Debian 12
Using version 0.18.3.1 for monero and GUI 


Many thanks,

# Discussion History
## ours-code | 2024-02-19T19:16:21+00:00
I forgot to add, it is very likely the cause of this was an unexpected power off while the blockchain was synchronizing.

## selsta | 2024-02-19T20:31:42+00:00
Sounds like a corrupted database due to power outage. You have to either delete data.mdb and sync from scratch or restore from backup if you have one.

## ours-code | 2024-02-19T20:40:45+00:00
@selsta Thank you for your prompt response ! Unfortunate news since I have no backups ... lesson learnt.
Thanks again.

# Action History
- Created by: ours-code | 2024-02-19T19:13:40+00:00
- Closed at: 2024-02-19T20:41:14+00:00
