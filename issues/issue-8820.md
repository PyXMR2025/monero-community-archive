---
title: I can't download monero's mdb_recover tool
source_url: https://github.com/monero-project/monero/issues/8820
author: hugohugo130
assignees: []
labels: []
created_at: '2023-04-08T02:13:02+00:00'
updated_at: '2023-04-08T02:17:34+00:00'
type: issue
status: closed
closed_at: '2023-04-08T02:17:34+00:00'
---

# Original Description
I can't download monero's mdb_recover tool from the official website, both github and monero official website show 404 errors

I'm use windows system
my blockchain file(data.mdb) is broken
I don't want to fix this by resyncing the blockchain
then I asked the artificial intelligence, and the 3 download links he provided were all invalid. Finally, the artificial intelligence told me that I could ask questions on Github.
Hope I provided enough information.
(Translated by Google, I am from Hong Kong)

# Discussion History
## selsta | 2023-04-08T02:17:34+00:00
There's no monero tool named mdb_recover.

You can try to start monerod.exe with `--db-salvage` and if that doesn't solve the corruption issues you have to resync from scratch. 

# Action History
- Created by: hugohugo130 | 2023-04-08T02:13:02+00:00
- Closed at: 2023-04-08T02:17:34+00:00
