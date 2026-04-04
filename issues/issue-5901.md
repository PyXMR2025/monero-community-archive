---
title: monero-blockchain-import process get killed and doesn't finish bootstraping
source_url: https://github.com/monero-project/monero/issues/5901
author: skinderis
assignees: []
labels:
- invalid
created_at: '2019-09-10T08:20:14+00:00'
updated_at: '2019-09-10T13:01:50+00:00'
type: issue
status: closed
closed_at: '2019-09-10T13:01:50+00:00'
---

# Original Description
I try to bootstrap monero blockchain, but every time I get my process kill for some reason. CPU and RAM usage doesn't hit 100 %. And logs doesn't show any error, just after a while I see this process status:
`[9]   Killed                  ./monero-blockchain-import --input-file blockchain.raw --data-dir /mnt/storage/monero/monero-boot --dangerous-unverified-import 1
`
Characteristics:
```
OS Ubuntu 18.04
3 CPU, 1 GB RAM
```

`./monero-blockchain-import --input-file blockchain.raw --data-dir /mnt/storage/monero/monero-boot --dangerous-unverified-import 1`

Logs:

```
2019-09-10 07:51:25.886	I Starting...
2019-09-10 07:51:25.886	I database: lmdb
2019-09-10 07:51:25.886	I database flags: 0
2019-09-10 07:51:25.886	I verify:  false
2019-09-10 07:51:25.886	I batch:   true  batch size: 20000
2019-09-10 07:51:25.886	I resume:  true
2019-09-10 07:51:25.886	I nettype: mainnet
2019-09-10 07:51:25.886	I bootstrap file path: blockchain.raw
2019-09-10 07:51:25.886	I database path:       /mnt/storage/monero/monero-boot
2019-09-10 07:51:25.886	W 
Import is set to proceed WITHOUT VERIFICATION.
This is a DANGEROUS operation: if the file was tampered with in transit, or obtained from a malicious source,
you could end up with a compromised database. It is recommended to NOT use dangerous-unverified-import.
*****************************************************************************************
You have 90 seconds to press ^C or terminate this program before unverified import starts
*****************************************************************************************
2019-09-10 07:52:55.892	I Loading blockchain from folder /mnt/storage/monero/monero-boot/lmdb ...
2019-09-10 07:52:55.895	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2019-09-10 07:52:58.295	I Loading checkpoints
2019-09-10 07:53:04.052	I bootstrap file recognized
2019-09-10 07:53:04.052	I bootstrap::file_info size: 4
2019-09-10 07:53:04.052	I bootstrap file v0.1
2019-09-10 07:53:04.052	I bootstrap magic size: 4
2019-09-10 07:53:04.052	I bootstrap header size: 1024
2019-09-10 07:53:04.052	I Scanning blockchain from bootstrap file...
block height: 1919225               
Done scanning bootstrap file
Full header length: 1028 bytes
Scanned for blocks: 58044196759 bytes
Total:              58044197787 bytes
Number of blocks: 1919226

2019-09-10 08:01:08.478	I bootstrap file last block number: 1919225 (zero-based height)  total blocks: 1919226

Preparing to read blocks...

2019-09-10 08:01:08.483	I bootstrap file recognized
2019-09-10 08:01:08.484	I bootstrap::file_info size: 4
2019-09-10 08:01:08.484	I bootstrap file v0.1
2019-09-10 08:01:08.484	I bootstrap magic size: 4
2019-09-10 08:01:08.484	I bootstrap header size: 1024
2019-09-10 08:01:08.484	I start block: 1020001  stop block: 1919225
2019-09-10 08:01:08.484	I Reading blockchain from bootstrap file...
```

# Discussion History
## moneromooo-monero | 2019-09-10T10:40:20+00:00
Anything in dmesg ?

## skinderis | 2019-09-10T11:10:53+00:00
@moneromooo-monero thanks for advice, seems that 1GB RAM is not enough. Will try to run on 2GB 2CPU machine.
```
[Tue Sep 10 11:06:31 2019] Out of memory: Kill process 11278 (monero-blockcha) score 676 or sacrifice child
[Tue Sep 10 11:06:31 2019] Killed process 11278 (monero-blockcha) total-vm:5155712kB, anon-rss:700140kB, file-rss:28kB, shmem-rss:0kB
[Tue Sep 10 11:06:31 2019] oom_reaper: reaped process 11278 (monero-blockcha), now anon-rss:4kB, file-rss:0kB, shmem-rss:0kB
```


## moneromooo-monero | 2019-09-10T12:57:04+00:00
+invalid

# Action History
- Created by: skinderis | 2019-09-10T08:20:14+00:00
- Closed at: 2019-09-10T13:01:50+00:00
