---
title: 'Im trying to import the blockchain i downloaded '
source_url: https://github.com/monero-project/monero/issues/3587
author: dmgmaker
assignees: []
labels: []
created_at: '2018-04-09T06:36:28+00:00'
updated_at: '2021-08-13T04:23:26+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:23:26+00:00'
---

# Original Description
Hey guys i downloaded a blockchain from the internet which seems pretty trusted but i cant get to import it. This is what i did and what i got as a result: 
C:\Users\hidden\Desktop\Neuer Ordner (2)\monero-v0.12.0.0>monero-blockchain-import.exe --guard-against-pwnage 1 --input-file ./blockchain.raw
2018-04-09 06:26:03.141 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:688   Starting...
2018-04-09 06:26:03.141 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:723   database: lmdb
2018-04-09 06:26:03.141 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:724   database flags: 0
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:725   verify:  true
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:729   batch:   true  batch size: 5000
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:735   resume:  true
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:736   nettype: mainnet
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:738   bootstrap file path: ./blockchain.raw
2018-04-09 06:26:03.142 8672    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:739   database path:       C:\ProgramData\bitmonero
2018-04-09 06:26:03.145 8672    INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-04-09 06:26:03.979 8672    INFO    global  src/cryptonote_core/cryptonote_core.cpp:525     Loading checkpoints
2018-04-09 06:28:34.244 8672    WARN    net.dns src/common/dns_utils.cpp:508    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-04-09 06:28:34.260 8672    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2780 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-04-09 06:28:34.275 8672    FATAL   bcutil  src/blockchain_utilities/blockchain_import.cpp:251   bootstrap file not found: "./blockchain.raw"

# Discussion History
## moneromooo-monero | 2018-04-09T09:38:48+00:00
Seems self explanatory. It does not find the file. That doesn't seem to be a bug, unless you can confirm the file is really there and readable.

## dmgmaker | 2018-04-09T10:26:38+00:00
I can confirm that the file is there and i downloaded it twice because i thought that the file is maybe corrupt but it seems to be alright so i dont know what i do wrong but im a newbie to the moneri gui wallet

## moneromooo-monero | 2018-04-09T10:30:55+00:00
Since this is Windows, try just blockchain.raw without the ./ as maybe this confuses it.


## dmgmaker | 2018-04-09T10:38:19+00:00
Ok i will try it. Thank you very much for trying to help me :)

## dmgmaker | 2018-04-09T10:55:06+00:00
Ok i tried to do it without the point but i still get the same error message

## moneromooo-monero | 2018-04-09T11:16:53+00:00
Try sha256sum blockchain.raw

If you don't have the sha256sum tool, then anything that reads the file (to check there's no permission issue, etc).

## dmgmaker | 2018-04-09T11:23:19+00:00
i dont really get how it works to use the sha256sum tool.

## moneromooo-monero | 2018-04-09T11:25:25+00:00
Just "sha256sum blockchain.raw", without the quotes.

## dmgmaker | 2018-04-09T11:27:13+00:00
Do they have to be in the same folder or something? My cmd just says that it is written false
i downloaded winmd5checksum and this brought me some numbers. but i dont know what they mean

## dmgmaker | 2018-04-09T11:28:38+00:00
Sha256: 4b9f31686ecaad97cdb175e6574bf307f8d1c410427825f4304c21da8aac1864
Md5: 44ba4505f45e10a603a7b3e757010029

## moneromooo-monero | 2018-04-09T11:29:48+00:00
You told monero-blockchain-import the file is in the same folder, so it is, right ?

## dmgmaker | 2018-04-09T11:32:17+00:00
![monero](https://user-images.githubusercontent.com/38203374/38495579-67333448-3bfa-11e8-8a2e-652389daa31c.jpg)
i think so yes

## moneromooo-monero | 2018-04-09T11:33:39+00:00
It should be called "blockchain.raw". It's called blockchain here, and Windows thinks it's a zip file. Unzip it, and make sure the uncompressed file is called blockchain.raw.

## moneromooo-monero | 2018-04-09T11:35:23+00:00
Also, there's no way it's only 110 MB. It'd be simpler to just run monerod and let it sync normally.

## dmgmaker | 2018-04-09T11:36:27+00:00
![monero 2](https://user-images.githubusercontent.com/38203374/38495696-d65dff60-3bfa-11e8-8e44-599df426f002.jpg)
![monero 3](https://user-images.githubusercontent.com/38203374/38495697-d67a1146-3bfa-11e8-9c57-311b82b6bc1f.jpg)
i think i downloaded the wrong file.. It doesn look like this is right. 
The File was 34,5 Gb when i downloaded it.. 

## moneromooo-monero | 2018-04-09T11:38:05+00:00
34.5 GB sounds plausible.

## dmgmaker | 2018-04-09T11:41:28+00:00
Oh FCK me i was totaly blind, there where 2 files in my download directory one was the zip file but the correct download was still there.

## dmgmaker | 2018-04-09T11:42:45+00:00
![monero](https://user-images.githubusercontent.com/38203374/38495949-df3a0d4e-3bfb-11e8-8c1b-bc4c5ff22435.png)


## dmgmaker | 2018-04-09T11:59:34+00:00
I think it kind of worked: 
C:\Users\timit\Desktop\monero-gui-v0.12.0.0>monero-blockchain-import.exe --guard-against-pwnage 1 --input-file ./blockchain.raw
2018-04-09 11:47:26.690 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:688   Starting...
2018-04-09 11:47:26.691 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:723   database: lmdb
2018-04-09 11:47:26.691 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:724   database flags: 0
2018-04-09 11:47:26.692 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:725   verify:  true
2018-04-09 11:47:26.692 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:729   batch:   true  batch size: 5000
2018-04-09 11:47:26.693 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:735   resume:  true
2018-04-09 11:47:26.693 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:736   nettype: mainnet
2018-04-09 11:47:26.694 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:738   bootstrap file path: ./blockchain.raw
2018-04-09 11:47:26.694 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:739   database path:       C:\ProgramData\bitmonero
2018-04-09 11:47:26.698 6288    INFO    global  src/cryptonote_core/cryptonote_core.cpp:427     Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2018-04-09 11:47:26.810 6288    INFO    global  src/cryptonote_core/cryptonote_core.cpp:525     Loading checkpoints
2018-04-09 11:49:56.986 6288    WARN    net.dns src/common/dns_utils.cpp:508    WARNING: no two valid MoneroPulse DNS checkpoint records were received
2018-04-09 11:49:56.987 6288    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2780 WARNING: batch transaction mode already enabled, but asked to enable batch mode
2018-04-09 11:49:56.989 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:346 bootstrap file recognized
2018-04-09 11:49:56.989 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:356 bootstrap::file_info size: 4
2018-04-09 11:49:56.990 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:367 bootstrap file v0.1
2018-04-09 11:49:56.991 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:368 bootstrap magic size: 4
2018-04-09 11:49:56.991 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:369 bootstrap header size: 1024
2018-04-09 11:49:56.992 6288    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:466 Scanning blockchain from bootstrap file...
block height: 1546094
Done scanning bootstrap file
Full header length: 1028 bytes
Scanned for blocks: 36999965467 bytes
Total:              36999966495 bytes
Number of blocks: 1546095

2018-04-09 11:52:39.065 6288    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:264   bootstrap file last block number: 1546094 (zero-based height)  total blocks: 1546095

The problem is that my monero wallet still want to synchronize and download all the blocks..

## dmgmaker | 2018-04-09T12:10:22+00:00
![unbenannt](https://user-images.githubusercontent.com/38203374/38496972-b77ab3ae-3bff-11e8-8538-b5812de33ebb.jpg)


## moneromooo-monero | 2018-04-09T12:47:19+00:00
Did you wait till the import finished ? It will take a while.

## dmgmaker | 2018-04-09T12:53:19+00:00
i think i did yes. but maybe i didnt. when i try to do it again it says permission not granted
And i get a message from win 10 which tells me it cant run this on my pc. 

## moneromooo-monero | 2018-09-14T11:37:54+00:00
Permission not granted is a windows/filesystem thing, not a monero thing. Make sure you're using the right binaries for your platform too. After you imported a blockchain, the node will still connect to sync the latest blocks, and keep up to date as the blockchain grows. After that, the wallet will scan the local blockchain. This is fine.
Is this all working now ? There appeared to be no bug, just computer issues AFAICT.

## selsta | 2021-08-13T04:23:26+00:00
Closing as there is no bug and the issue author didn't reply anymore.

# Action History
- Created by: dmgmaker | 2018-04-09T06:36:28+00:00
- Closed at: 2021-08-13T04:23:26+00:00
