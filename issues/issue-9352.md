---
title: 'ERROR: chunk size exceeds buffer size while exporting monero database'
source_url: https://github.com/monero-project/monero/issues/9352
author: PunchEnergyFTW
assignees: []
labels:
- bug
created_at: '2024-06-04T00:00:51+00:00'
updated_at: '2024-06-06T09:01:03+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi!

I wanted to create a backup of my monero database and found the tool monero-blockchain-export.exe.
Yesterday, i let the tool run for a few minutes and it all worked very well.

But when i want to restart the backup, i get a "chunk size exceeds buffer size" error.
I have synced the database in between these two export attempts, could this be the problem? If yes, isn't this tool supposed to make incremental backups easier?

My blockchain.raw export file is currently ~9GB and at about block height ~1.300.000
```
C:\Users\xxx\Documents\monero-gui-win-x64-v0.18.3.3\monero-gui-v0.18.3.3\extras>monero-blockchain-export.exe --d
ata-dir U:\MoneroBlockChain --output-file U:\Monero-Blockchain-Export\blockchain.raw
2024-06-03 23:52:08.648 W Starting...
2024-06-03 23:52:08.649 W Export output file: U:\Monero-Blockchain-Export\blockchain.raw
2024-06-03 23:52:08.649 W Initializing source blockchain (BlockchainDB)
2024-06-03 23:52:08.650 W database: LMDB
2024-06-03 23:52:08.651 W Loading blockchain from folder U:\MoneroBlockChain\lmdb ...
2024-06-03 23:52:08.748 W Source blockchain storage initialized OK
2024-06-03 23:52:08.749 W Exporting blockchain raw data...
2024-06-03 23:52:08.750 I Storing blocks raw data...
2024-06-03 23:52:08.750 I source blockchain height: 3106278
2024-06-03 23:52:08.750 I Using block height of source blockchain: 3106278
2024-06-03 23:52:08.758 I bootstrap file recognized
2024-06-03 23:52:08.758 I bootstrap::file_info size: 4
2024-06-03 23:52:08.759 I bootstrap file v1.0
2024-06-03 23:52:08.759 I bootstrap magic size: 4
2024-06-03 23:52:08.759 I bootstrap header size: 1024
2024-06-03 23:52:08.760 I bootstrap::blocks_info size: 6
2024-06-03 23:52:08.760 I bootstrap first block:0
2024-06-03 23:52:08.760 I bootstrap last block:2888442
2024-06-03 23:52:08.761 I Scanning blockchain from bootstrap file...
2024-06-03 23:53:16.722 W WARNING: chunk_size 596646401 > BUFFER_SIZE 2097152  height: 8, offset 453105
2024-06-03 23:53:16.723 E Exception at [Export error], what=Aborting: chunk size exceeds buffer size
```

# Discussion History
## selsta | 2024-06-04T00:02:30+00:00
You can just copy the data.mdb file if you want to make a backup. There is no reason to use monero-blockchain-export.

## PunchEnergyFTW | 2024-06-04T00:03:30+00:00
> You can just copy the data.mdb file if you want to make a backup. There is no reason to use monero-blockchain-export.

Which would make incremental backups to an external source much harder. Again, I thought this tool was a solution to make easy, incremental backups.

## selsta | 2024-06-04T00:08:26+00:00
Can you delete blockchain.raw and try to export it again, does it stop/error at the same height?

## PunchEnergyFTW | 2024-06-04T00:10:05+00:00
> Can you delete blockchain.raw and try to export it again, does it stop at the same height?

I'll have to let it run for a while. It slows down quite a lot even though it's on a local SSD.
Once it's done, i'll let you know. I'll get to it in probably 12-24 hours.

## PunchEnergyFTW | 2024-06-04T21:21:55+00:00
~The new export has been running for a few hours now and is almost finished. I also briefly stopped the export in between and turned on the Monero node to let the blockchain synchronize. After a few minutes of synchronization, I turned off the node again and restarted the export, which then continued without any problems. It really seems as if the first export was corrupted for some reason, even though the export tool did not give me any error message.~

**UPDATE:**

Seems like i replied too early. After now fully synchronizing my Blockchain and trying to update the blockchain_new.raw exported file, i get the same error again.

```powershell
C:\monero-gui-v0.18.3.3\extras>monero-blockchain-export.exe --data-dir U:\MoneroBlockChain --output-file F:\Monero-Blockchain-Export\blockchain_new.raw
2024-06-06 08:38:59.940 W Starting...
2024-06-06 08:38:59.941 W Export output file: F:\Monero-Blockchain-Export\blockchain_new.raw
2024-06-06 08:38:59.943 W Initializing source blockchain (BlockchainDB)
2024-06-06 08:38:59.944 W database: LMDB
2024-06-06 08:38:59.944 W Loading blockchain from folder U:\MoneroBlockChain\lmdb ...
2024-06-06 08:39:00.016 W Source blockchain storage initialized OK
2024-06-06 08:39:00.016 W Exporting blockchain raw data...
2024-06-06 08:39:00.017 I Storing blocks raw data...
2024-06-06 08:39:00.017 I source blockchain height: 3165117
2024-06-06 08:39:00.017 I Using block height of source blockchain: 3165117
2024-06-06 08:39:00.576 I bootstrap file recognized
2024-06-06 08:39:00.576 I bootstrap::file_info size: 4
2024-06-06 08:39:00.577 I bootstrap file v1.0
2024-06-06 08:39:00.577 I bootstrap magic size: 4
2024-06-06 08:39:00.577 I bootstrap header size: 1024
2024-06-06 08:39:00.578 I bootstrap::blocks_info size: 6
2024-06-06 08:39:00.579 I bootstrap first block:0
2024-06-06 08:39:00.579 I bootstrap last block:3106278
2024-06-06 08:39:00.580 I Scanning blockchain from bootstrap file...
2024-06-06 08:53:46.735 W WARNING: chunk_size 1316299468 > BUFFER_SIZE 2097152  height: 0, offset 196735
2024-06-06 08:53:46.738 E Exception at [Export error], what=Aborting: chunk size exceeds buffer size
```

# Action History
- Created by: PunchEnergyFTW | 2024-06-04T00:00:51+00:00
