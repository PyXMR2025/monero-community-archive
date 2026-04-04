---
title: 'Monerod: sync on SMB share MDB_NOTFOUND'
source_url: https://github.com/monero-project/monero/issues/5260
author: Unclezz
assignees: []
labels: []
created_at: '2019-03-08T20:57:30+00:00'
updated_at: '2022-02-22T21:38:33+00:00'
type: issue
status: closed
closed_at: '2022-02-22T21:38:33+00:00'
---

# Original Description
Hi,
I tried to setup a new Monero node with latest cli code 0.14.0.2 on a GNU/Linux Debian testing and running data on a Samba share (SMBv2). 

Command I used to start the node is:

`DNS_PUBLIC=tcp://8.8.8.8 ./monerod --restricted-rpc  --limit-rate-up 128 --data-dir /mnt/SMB_SHARE`

Unfortunately the daemon does not start to sync and I immediately noticed this error: 

```
2019-03-08 17:12:49.169     7f21f5e08bc0        INFO    global  src/cryptonote_core/cryptonote_core.cpp:469     Loading blockchain from folder /mnt/SMB_SHARE/lmdb ...
2019-03-08 17:12:49.331     7f21f5e08bc0        WARN    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:76   Error attempting to retrieve a hard
 fork version at height 0 from the db: MDB_NOTFOUND: No matching key/data pair found
2019-03-08 17:12:49.362     7f21f5e08bc0        INFO    stacktrace      src/common/stack_trace.cpp:133  Exception: cryptonote::DB_ERROR
```

In logs (attached here) there are some more details.

[monerod_log2.txt](https://github.com/monero-project/monero/files/2947400/monerod_log2.txt)

I tried to then configure same node using NFS share instead of SMB and it worked like a charm. 

Is there any well known limitation using Samba to store the data of the blockchain? 

Thanks!

# Discussion History
## hyc | 2019-03-08T21:12:31+00:00
In general, LMDB is unsafe on remote filesystems and such use is officially unsupported.

## Unclezz | 2019-03-09T00:27:38+00:00
I see, thanks @hyc 

## leonklingele | 2019-05-31T22:29:31+00:00
@hyc is there a way to use the same database from two nodes? Maybe if one has read permissions only? I'd like to set up a few nodes with limited storage available and thought a shared database would help.

@moneromooo-monero FYI, it's unsafe.

## hyc | 2019-05-31T23:23:50+00:00
Why do you need to run two nodes on two separate machines using the same storage? There's no performance gain from doing that so what benefit is there?

## leonklingele | 2019-05-31T23:49:01+00:00
Limited storage. The servers only have very limited free space available and I don't want to waste 80GB for each additional node only to replicate the database on a shared volume.

> no performance gain

Those nodes are there to support the network with their high performance network connection.

## hyc | 2019-06-01T00:33:03+00:00
Still makes no sense. Run a single node on a single network connection. Adding more nodes on the same network just redundantly eats bandwidth.

## leonklingele | 2019-06-01T05:26:17+00:00
I don't understand.. each of those servers has an independent 1Gbit/s connection. How should adding more servers not help support the network? I don't want to _download_ the blockchain as quickly as possible, I want to _distribute_ it to others _as fast as possible_.
1 server = Relaying blocks with 1 Gbit/s
2 servers = Relaying blocks with 2 Gbit/s
etc.


## hyc | 2019-06-02T17:54:22+00:00
You have two servers talking to the same storage. Run the node on the storage server and plug both networks into it then.

The fact remains that LMDB is entirely built around memory-mapped data, and to my knowledge there are *zero* remote filesystems that support mmap coherence across multiple machines. If you find one that actually claims to do that, we can look at how broken it may or may not be.

## moneromooo-monero | 2019-06-03T11:17:57+00:00
To make things clear, mmap will succeed, but not have the same guarantees it'd have on a local fs ?

## hyc | 2019-06-03T13:30:13+00:00
Pretty sure it has no guarantees at all. In particular, there's no guarantee that two processes running on different machines mmap'ing the same file on a server will ever see the same set of writes, in any particular order. Also note that LMDB uses shared-memory mutexes for concurrency control, and these mutexes live inside an mmap'd region too, and those mutexes have absolutely zero ability to work across multiple machines. The entire question is ludicrous. So, as already stated "THIS IS NOT SUPPORTED."

## moneromooo-monero | 2019-06-03T22:59:38+00:00
Sure. I was just thinking could we just call a test mmap at start and error out if it fails. But that doesn't seem to be the case that it'd fail outright.

# Action History
- Created by: Unclezz | 2019-03-08T20:57:30+00:00
- Closed at: 2022-02-22T21:38:33+00:00
