---
title: Monerod crashes when synchronizing on Windows.
source_url: https://github.com/monero-project/monero/issues/9569
author: Folindril
assignees: []
labels:
- more info needed
created_at: '2024-11-13T16:20:39+00:00'
updated_at: '2024-12-13T23:03:14+00:00'
type: issue
status: closed
closed_at: '2024-12-13T23:03:14+00:00'
---

# Original Description
When synchronizing the blockchain from 0, most of it is synchronized without problems. Towards the end, monerod starts to crash at random times without any errors. There were cases when the crash occurred in the middle of drawing a log line on the screen. There are also crashes with irreversible damage to the blockchain files. Work in a synchronized state is stable, the bug clearly occurs only when lagging behind the network. This bug occurs either on certain hardware or on a certain OS.This bug is present on all versions 0.18. Did not check earlier versions due to incompatibility of blockchain files.

Version: 0.18.3.4 Windows 64-bit
OS: Windows 11
Processor: Intel Core i5-7600K 3.80GHz
RAM: 16Gb

# Discussion History
## selsta | 2024-11-16T02:01:37+00:00
Do you have any stability issues on your system? Or do you have a different computer where you can test syncing to see if it crashes? There is no known crash bugs in v0.18 that match what you are describing, at least we didn't get other reports about this on Windows.

## Folindril | 2024-11-16T11:15:35+00:00
> Do you have any stability issues on your system? Or do you have a different computer where you can test syncing to see if it crashes? There is no known crash bugs in v0.18 that match what you are describing, at least we didn't get other reports about this on Windows.

No, there are no problems with other applications (mostly games). Monero mining also works stably with a synchronized node.
I have a laptop on Windows 10 in the same network, where synchronization occurs without crashes. No additional parameters in the command line helped me either. Therefore, I decided that this is a bug and it is tied to a certain architecture.

## Folindril | 2024-11-16T12:38:54+00:00
Now I have run new synchronization again with log detalisation level 1 to detect on which block the first crash will occur. It will take a few days because crashes start towards the end.

## selsta | 2024-11-16T23:34:35+00:00
The problem is sometimes the last log message is not related to the crash, a stack trace would ideally be needed but that's a bit more complicated on Windows.

## Folindril | 2024-11-17T15:39:17+00:00
> Now I have run new synchronization again with log detalisation level 1 to detect on which block the first crash will occur. It will take a few days because crashes start towards the end.

Done. Block 1650925 (2018-08-31).
Log:

```
2024-11-17 11:19:56.367 I +++++ BLOCK SUCCESSFULLY ADDED
2024-11-17 11:19:56.368 I id:   <6d920a7d01f688c5f3da5dbb4e7bca6cc67e19b104fc2ef9d56a89b4fad5d9de>
2024-11-17 11:19:56.368 I PoW:  <ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff>
2024-11-17 11:19:56.368 I HEIGHT 1650925, difficulty:   56493714946
2024-11-17 11:19:56.368 I block reward: 3.986338323206(3.969986323206 + 0.016352000000), coinbase_weight: 102, cumulative weight: 53514, 1(0/0)ms
2024-11-17 11:19:56.663 I [91.198.115.225:18380 OUT] 18284 bytes received for category command-1001 initiated by us
2024-11-17 11:19:56.753 I [193.142.4.150:18085 OUT] 2554507 bytes received for category command-2004 initiated by peer
2024-11-17 11:19:56.753 I [193.142.4.150:18085 OUT] Received NOTIFY_RESPONSE_GET_OBJECTS (20 blocks)
2024-11-17 11:19:56.753 I [193.142.4.150:18085 OUT] [0] state: received objects in state synchronizing
2024-11-17 11:19:56.755 I [193.142.4.150:18085 OUT] Failed to lock m_sync_lock, going back to download
2024-11-17 11:19:59.254 I Transaction added to pool: txid <d71ced687cf92480e018b61908911e2383f85b9b39c456678b6fa92457f7b38b> weight: 14927 fee/byte: 159577, count: 1
2024-11-17 11:19:59.255 I [91.198.115.225:18380 OUT] Remote blockchain height: 3283270, id: <985e0b82cdaaa1dd78da8a57a8ad512de6b1407cde839815d4d9f1fa76695d10>
2024-11-17 11:19:59.256 I [91.198.115.225:18380 OUT] [0] state: requesting callback in state synchronizing
2024-11-17 11:19:59.257 I [193.142.4.150:18085 OUT] [0] state: resuming in state synchronizing
2024-11-17 11:19:59.257 I [91.198.115.225:18380 OUT] New connection handshaked, pruning seed 0
```

## selsta | 2024-11-17T15:41:52+00:00
There is nothing interesting in the logs unfortunately, the crash happens after the log message is printed. A stack trace would be required to look into this further.

## EvarDion | 2024-12-12T16:00:54+00:00
I experienced tha same issue and after a few days, I  was able to isolate the root cause of the issue on my Windows 10 system.

**System Spec:**
OS: Windows 10 64-bit
CPU: Ryzen 5950x
Ram: 32GB
Drive: Nvme SSD (Gen 3)
Free Space: 400+GB

**Symptoms:**
Monerod.exe sync appears to work fine untill the blockchain gets to about 70GB in size and then monerod.exe just randomly stops due to some transaction validation errors. If you keep restarting monerod it will work fine for several hours and that stop again. Eventually the monerod crashes become more frequent untill they occur every few seconds and then finallly monerod.exe will fail to start and none of the recovery options can repair the blockchain data.mdb file.

**Root Cause:** 
If the lmdb folder is compressed and the data.mdb file gets too big (70GB+) this will cause the monerod.exe to fail to verify some transactions and eventually crash. Over time, monerod.exe will keep crashing until the data.mdb file reaches an unrecoverable state and monerod.exe will fail to start.

**Note:**
When the lmdb folder is not compressed I can run the entire sync from block 0 on the same hardware without monerod.exe halting a single time.

@Folindril can you check whether your data\lmdb folder is compressed or not?

![Monero bug](https://github.com/user-attachments/assets/2cd40284-71d8-4f8e-b8c7-1011e9603dc8)
_(blue arrows on the folder icon indicate that the folder is compressed and anyting placed in that folder will also be compressed)_

**Recommendation:** 
If this is a known issue, devs should add some code to monerod.exe to prevent it from creating data.mdb in the lmdb folder if it is compressed because it will eventually lead to an unrecoverable error. In the meantime users should make sure their lmdb folder is _not compressed_ on Windows systems becuase it will only end in a completely corrupted blockchain database (data.mdb).

I have included some logs which show the invalid transactions occuring:
[bitmonero.log.zip](https://github.com/user-attachments/files/18114077/bitmonero.log.zip)


## Folindril | 2024-12-12T16:12:10+00:00
> @Folindril can you check whether your data\lmdb folder is compressed or not?

Compressed. Now I'll run it without compression and check.


## Folindril | 2024-12-12T18:02:04+00:00
> @Folindril can you check whether your data\lmdb folder is compressed or not?

I confirm that after removing compression on the folder, monerod works without crashes where it should have quickly stumbled.
@EvarDion, you are my hero!

## EvarDion | 2024-12-12T19:18:55+00:00
@Folindril , im glad we managed to figure it out.. it's a nasty bug.

## selsta | 2024-12-13T23:03:14+00:00
I opened an issue here #9617

# Action History
- Created by: Folindril | 2024-11-13T16:20:39+00:00
- Closed at: 2024-12-13T23:03:14+00:00
