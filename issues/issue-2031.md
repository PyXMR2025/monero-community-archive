---
title: 'monero : Error on importing blockchain.raw file, Screenshot provided in end
  of message.'
source_url: https://github.com/monero-project/monero/issues/2031
author: albertahirwar
assignees: []
labels: []
created_at: '2017-05-16T17:03:28+00:00'
updated_at: '2020-02-16T23:11:49+00:00'
type: issue
status: closed
closed_at: '2017-09-20T21:18:25+00:00'
---

# Original Description
==========================================
Error on importing blockchain.raw file, Screenshot provided in end of message.
Says : "**Aborting: chunk size exceeds buffer size**"
==========================================
monero-blockchain-import.exe --batch-size 2000000 --database lmdb#fastest --verify off --input-file blockchain.raw
2017-05-16 22:12:42.567 4024    INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,s
tacktrace:INFO
2017-05-16 22:12:42.567 4024    INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net:FATAL,net.p2p:FATAL,global:INFO,verify:FATAL,s
tacktrace:INFO,bcutil:INFO
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:729   Starting...
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:774   database: lmdb
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:775   database flags: 10289152
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:776   verify:  false
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:780   batch:   true  batch size: 2000000
2017-05-16 22:12:42.567 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:786   resume:  true
2017-05-16 22:12:42.582 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:787   testnet: false
2017-05-16 22:12:42.582 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:789   bootstrap file path: blockchain.raw
2017-05-16 22:12:42.582 4024    INFO    bcutil  src/blockchain_utilities/blockchain_import.cpp:790   database path:       C:\ProgramData\bitmonero
2017-05-16 22:12:42.582 4024    WARN    default src/blockchain_utilities/fake_core.h:81 Loading blockchain from folder C:\ProgramData\bitmonero\lmdb ...
2017-05-16 22:12:42.738 4024    ERROR   blockchain      src/cryptonote_core/blockchain.cpp:4024 Block hash data does not match expected hash
2017-05-16 22:12:42.738 4024    WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2423 WARNING: batch transaction mode already enabled, but ask
ed to enable batch mode
2017-05-16 22:12:42.738 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:347 bootstrap file recognized
2017-05-16 22:12:42.754 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:357 bootstrap::file_info size: 4
2017-05-16 22:12:42.754 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:368 bootstrap file v0.1
2017-05-16 22:12:42.754 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:369 bootstrap magic size: 4
2017-05-16 22:12:42.754 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:370 bootstrap header size: 1024
2017-05-16 22:12:42.770 4024    INFO    bcutil  src/blockchain_utilities/bootstrap_file.cpp:400 Scanning blockchain from bootstrap file...
2017-05-16 22:20:59.663 4024    WARN    bcutil  src/blockchain_utilities/bootstrap_file.cpp:436 **WARNING: chunk_size 2629486972 > BUFFER_SIZE 1000000  height: 1296544**
terminate called after throwing an instance of 'std::runtime_error'
  what():  Aborting: chunk size exceeds buffer size

This application has requested the Runtime to terminate it in an unusual way.
Please contact the application's support team for more information.
=================================================
screenshot
=================================================
![untitled](https://cloud.githubusercontent.com/assets/25181843/26118243/c83ad758-3a86-11e7-9fee-12908812254b.jpg)


# Discussion History
## moneromooo-monero | 2017-05-17T19:49:38+00:00
Does it also happen without the --batch-size 2000000 ?

## npodonnell | 2017-05-17T20:06:21+00:00
I also had this problem, on Linux

## KushGoyal | 2017-05-18T10:22:52+00:00
I am getting the same error when using command:

`./monero-blockchain-import --verify 0 --input-file ./blockchain.raw`

import log: https://pastebin.com/a6SH34tY

Previously I was syncing up using monerod but got segmentation fault error.


## albertahirwar | 2017-05-19T05:43:28+00:00
YES

On Thu, May 18, 2017 at 1:19 AM, moneromooo-monero <notifications@github.com
> wrote:

> Does it also happen without the --batch-size 2000000 ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2031#issuecomment-302212521>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AYA-k2bsCNwNIRD5fFsecwwLGT9Ncf8Lks5r609XgaJpZM4NczI8>
> .
>


## moneromooo-monero | 2017-05-19T18:28:19+00:00
Can you please run the following:
monero-blockchain-import.exe --batch-size 2000000 --database lmdb#fastest --verify off --input-file blockchain.raw --log-level 1,bcutil:DEBUG
and post the output ? Thanks.

## albertahirwar | 2017-05-21T05:38:53+00:00
ok, will send it a.s.a.p. ...

On Fri, May 19, 2017 at 11:58 PM, moneromooo-monero <
notifications@github.com> wrote:

> Can you please run the following:
> monero-blockchain-import.exe --batch-size 2000000 --database lmdb#fastest
> --verify off --input-file blockchain.raw --log-level 1,bcutil:DEBUG
> and post the output ? Thanks.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2031#issuecomment-302777452>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AYA-kypAoo4ALHJAxx3f9zvg2Pz-JNHfks5r7d9GgaJpZM4NczI8>
> .
>


## KushGoyal | 2017-05-22T06:48:40+00:00
@moneromooo-monero I ran the command you gave on ubuntu. The whole output is too large. I am posting the last few lines and the error.

```c++
2017-05-22 12:06:03.226     7f8d21672ec0    DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:430 chunk_size: 40057
2017-05-22 12:06:03.226     7f8d21672ec0    DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:461 Number bytes scanned: 8229814395
2017-05-22 12:06:03.227     7f8d21672ec0    DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:430 chunk_size: 1731799020
2017-05-22 12:06:03.227     7f8d21672ec0    WARN    bcutil  src/blockchain_utilities/bootstrap_file.cpp:436 WARNING: chunk_size 1731799020 > BUFFER_SIZE 1000000  height: 1292838
2017-05-22 12:06:03.394     7f8d21672ec0    ERROR   bcutil  src/blockchain_utilities/blockchain_import.cpp:861  Exception at [Import error], what=Aborting: chunk size exceeds buffer size
```

## moneromooo-monero | 2017-05-22T07:34:59+00:00
Can you put the full output though on fpaste.org please ? I want to calculate accumulated sizes from the log.
Also please give the size in bytes of the file you're trying to import.


## KushGoyal | 2017-05-22T08:23:34+00:00
the size of the file I am importing is 9749168097 bytes.

The command produced 4 files: 
* 3 are each 104mb with names like `?-2017-05-22-08-13-28`
* the 4th file is `monero-blockchain-import.log` which is 14mb

I also saved the output of the command in a text file. This file is 354mb. Which one do you need?



## moneromooo-monero | 2017-05-24T21:19:25+00:00
Hrm. I did not expect such a large amount of logs. Try running with --log-level 0,bcutil:DEBUG instead, that should cut on logs a lot and still give me what I want.

## KushGoyal | 2017-05-25T06:31:14+00:00
I ran the command with `--log-level 0,bcutil:DEBUG` but got the same huge outputs. I am attaching monero import log file which is 13mb.

[monero-blockchain-import.txt](https://github.com/monero-project/monero/files/1028159/monero-blockchain-import.txt)


## moneromooo-monero | 2017-05-27T10:56:06+00:00
Start is missing, but nevermind. I think that file is corrupt.

## KushGoyal | 2017-05-27T11:27:46+00:00
@moneromooo-monero 

I downloaded this file from here: https://downloads.getmonero.org/blockchain.raw

Before downloading this file I first synced the whole blockchain using ./monerod but I got segmentation fault/ bus error.

So what do you suggest I do next? Should I try to sync up the db again? Or try to download the raw file?

## moneromooo-monero | 2017-05-27T13:30:20+00:00
You could try downloading it again. I think it's automatically updated on a timer, so you might have got it while it was written to.
As for segmention fault or bus error, give a stack trace (gdb monerod core). Replace monerod with the path to it if neeed, and core might be named core.PID.


## moneromooo-monero | 2017-09-02T12:40:41+00:00
Not sure what to do with this one. I think I might close it, since it looks like it's a corrupted file, and such errors are now exiting nicely instead of via terminate.

## hyc | 2017-09-20T19:40:44+00:00
Yeah, sounds like should be closed.

## moneromooo-monero | 2017-09-20T21:02:35+00:00
I'll set as resolved since we now error out nicely.

+resolved

## JPaulMora | 2018-01-08T06:39:33+00:00
Hey I just got this error, I'm using `Monero 'Helium Hydra' (v0.11.1.0-release)` compiled by myself on Ubuntu Desktop 16.04
 

````
block height: 1392230    2018-01-08 07:00:33.996            7fbd22651740        DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:430 chunk_size: 99470
2018-01-08 07:00:33.996     7fbd22651740        DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:461 Number bytes scanned: 19841163138
2018-01-08 07:00:33.997     7fbd22651740        DEBUG   bcutil  src/blockchain_utilities/bootstrap_file.cpp:430 chunk_size: 4010446727
2018-01-08 07:00:33.997     7fbd22651740        WARN    bcutil  src/blockchain_utilities/bootstrap_file.cpp:436 WARNING: chunk_size 4010446727 > BUFFER_SIZE 1000000  height: 1392231
2018-01-08 07:00:34.088     7fbd22651740        ERROR   bcutil  src/blockchain_utilities/blockchain_import.cpp:747      Exception at [Import error], what=Aborting: chunk size exceeds buffer size
monerodaemon@USKCCRYPTO:/mnt/External/bitmonero$ /usr/local/src/monero/build/release/bin/monero-blockchain-import --data-dir /mnt/External/bitmonero --input-file Bchain.raw --database lmdb#fastest --verify off --log-level 1,bcutil:DEBUG
````

## ivanmohnatov | 2018-02-16T09:22:21+00:00
Hello everybody
on ubuntu 16.04 here such error when importing a blockchain
WARN 	blockchain.db.lmdb	src/blockchain_db/lmdb/db_lmdb.cpp:2674	WARNING: batch transaction mode already enabled, but asked to enable batch mode
After blocks are checked and after
ERROR	bcutil	src/blockchain_utilities/blockchain_import.cpp:747	Exception at [Import error], what=Aborting
![_054](https://user-images.githubusercontent.com/36532494/36300857-dfe58a9a-1313-11e8-8e5b-eb3b1dc4ecc5.png)
The question is what am I doing wrong?


## malachid | 2018-04-11T06:26:29+00:00
I'm seeing this on Ubuntu 18.04 as well with v0.12.0.0

## yekimtrof | 2018-04-13T01:20:22+00:00
Someone please tell.me how this can be solved

## malachid | 2018-04-13T04:01:17+00:00
Over the last 6 days I have tried multiple things (and hundreds of gigs of failed syncs).  I never got the import to work - it always failed and refused to salvage near the end.  The one thing that finally worked (today) on Linux was a full fresh sync using: `./monerod --db-sync-mode 'safe:async:10' --db-salvage`.  Every time it gave a failure, I restarted the computer and re-ran that command to get it to continue.  When that 10 was 1000 or 100, it would failed the same way the import did.  on v10 I never had these kinds of problems, but v12 seems to have a very hard time recovering.

## MrChriZ | 2020-02-14T15:16:57+00:00
Just ran into this problem

## ndorf | 2020-02-14T16:28:10+00:00
@MrChriZ can you paste the exact command you're using and the error message?

## MrChriZ | 2020-02-14T16:57:28+00:00
@ndorf 
The same as KushGoyal
./monero-blockchain-import --verify 0 --input-file ./blockchain.raw

## MrChriZ | 2020-02-14T18:24:12+00:00
Sorry slightly different actually:
./monero-blockchain-import --dangerous-unverified-import 0 --input-file ./blockchain.raw 
I'm on build 0.15.0.2

## ndorf | 2020-02-16T17:53:46+00:00
@MrChriZ and the error message?

edit: Specifically, if you're getting one like "WARNING: chunk_size X > BUFFER_SIZE Y height: Z," I'd like to know what the X Y and Z values are.

## MrChriZ | 2020-02-16T18:42:28+00:00
Apologies here's the full command and output:
```
 ./monero-blockchain-import --dangerous-unverified-import 0 --input-file ./blockchain.raw 

2020-02-16 18:40:12.893 I Starting...
2020-02-16 18:40:12.893 I database: LMDB
2020-02-16 18:40:12.893 I verify:  true
2020-02-16 18:40:12.893 I batch:   true  batch size: 5000
2020-02-16 18:40:12.893 I resume:  true
2020-02-16 18:40:12.893 I nettype: mainnet
2020-02-16 18:40:12.893 I bootstrap file path: ./blockchain.raw
2020-02-16 18:40:12.893 I database path:       /home/chris/.bitmonero
2020-02-16 18:40:12.895 I Loading blockchain from folder /home/chris/.bitmonero/lmdb ...
2020-02-16 18:40:12.940 I Loading checkpoints
2020-02-16 18:40:26.252 I bootstrap file recognized
2020-02-16 18:40:26.252 I bootstrap::file_info size: 4
2020-02-16 18:40:26.252 I bootstrap file v0.1
2020-02-16 18:40:26.252 I bootstrap magic size: 4
2020-02-16 18:40:26.252 I bootstrap header size: 1024
2020-02-16 18:40:26.252 I Scanning blockchain from bootstrap file...
2020-02-16 18:41:56.462 W WARNING: chunk_size 3494290415 > BUFFER_SIZE 2097152  height: 3, offset 758540
2020-02-16 18:41:56.488 E Exception at [Import error], what=Aborting: chunk size exceeds buffer size
```

## ndorf | 2020-02-16T19:04:42+00:00
Yowza, 3.5GB chunk size certainly seems unreasonable. I'll try to reproduce this locally.

## ndorf | 2020-02-16T22:09:12+00:00
It seems this does not happen with a freshly exported blockchain (from mainnet at height 2035082). The biggest chunk was 474343 bytes, and it imported without error.

Did you export this file yourself? If so, which options to `monero-blockchain-export` did you use?



## MrChriZ | 2020-02-16T22:14:17+00:00
Hmm no that was downloaded from 
https://downloads.getmonero.org/blockchain.raw

Weird...



## MrChriZ | 2020-02-16T22:46:05+00:00
OK so I think I understand how my problem came to be.
So I followed instructions here:
https://monero.stackexchange.com/questions/2761/what-is-the-fastest-way-to-synchronize-the-daemon
To get the raw file.   However the steps described are flawed.
The answer states that if the download fails with wget to simply restart it again...
On a high speed connection from the UK I the raw file only comes down at 120kbs or so.

I see above that the server side raw file is updated on a timer and in [another place it](https://www.reddit.com/r/Monero/comments/6tiq7v/question_why_doesnt_getmonero_provide_checksums/) updates every eight hours. So I guess if you restart the download after the server file has been updated that's probably going to corrupt the RAW file that's been downloaded...possibly it's going to be corrupted without even restarting the download.

## ndorf | 2020-02-16T23:11:48+00:00
I agree, those steps are flawed.

Aside from the specific issue of attempting to resume a download when the source file has changed, the fact is that the fastest way to sync the blockchain is usually to just let it sync over the P2P network. This is actually mentioned [on the official download page](https://www.getmonero.org/downloads/#blockchain) (of course, I'm not blaming you for not seeing this when following a direct link, just supporting my statement).

Hopefully, it should at least work if the download is not interrupted and then resumed. But even that would still take 5 days at 120kbps. Syncing from scratch over P2P should be a lot faster than that (you usually have at least 8 peers, and many of them can do a lot better than 120kb).


# Action History
- Created by: albertahirwar | 2017-05-16T17:03:28+00:00
- Closed at: 2017-09-20T21:18:25+00:00
