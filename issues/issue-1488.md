---
title: no backwards compatibility with newest boost changes
source_url: https://github.com/monero-project/monero/issues/1488
author: medusadigital
assignees: []
labels: []
created_at: '2016-12-22T11:21:06+00:00'
updated_at: '2017-02-11T21:35:15+00:00'
type: issue
status: closed
closed_at: '2017-02-11T21:35:15+00:00'
---

# Original Description
Ok lets start completely from scratch:

1. delete p2pstate.bin and poolstate.bin
2. run master daemon with new boost changes
3. exit daemon
4. start 10.1 daemon

notice the errors on startup: 

Creating the logger system
2016-Dec-22 12:03:36.769198 Initializing cryptonote protocol...
2016-Dec-22 12:03:36.769198 Cryptonote protocol initialized OK
2016-Dec-22 12:03:36.769198 Initializing p2p server...
2016-Dec-22 12:03:37.081198 Set limit-up to 2048 kB/s
2016-Dec-22 12:03:37.081198 Set limit-down to 8192 kB/s
2016-Dec-22 12:03:37.081198 Set limit-up to 2048 kB/s
2016-Dec-22 12:03:37.096798 Set limit-down to 8192 kB/s
**2016-Dec-22 12:03:37.096798 ERROR C:/msys64/DISTRIBUTION-BUILD/src/p2p/net_node.inl:145 Failed to load p2p config file, falling back to default config**
2016-Dec-22 12:03:37.096798 Binding on 0.0.0.0:18080
2016-Dec-22 12:03:37.096798 Net service bound to 0.0.0.0:18080
2016-Dec-22 12:03:37.096798 Attempting to add IGD port mapping.
2016-Dec-22 12:03:38.313600 Added IGD port mapping.
2016-Dec-22 12:03:38.313600 P2p server initialized OK
2016-Dec-22 12:03:38.313600 Initializing core rpc server...
2016-Dec-22 12:03:38.313600 Binding on 127.0.0.1:18081
2016-Dec-22 12:03:38.313600 Core rpc server initialized OK on port: 18081
2016-Dec-22 12:03:38.313600 Initializing core...
**2016-Dec-22 12:03:38.313600 ERROR C:/msys64/DISTRIBUTION-BUILD/src/common/boost_serialization_helper.h:108 Exception at [unserialize_obj_from_file], what=std::bad_alloc
2016-Dec-22 12:03:38.313600 ERROR C:/msys64/DISTRIBUTION-BUILD/src/cryptonote_core/tx_pool.cpp:695 Failed to load memory pool from file D:\chains\monero/poolstate.bin**
2016-Dec-22 12:03:38.329200 Loading blockchain from folder D:\chains\monero\lmdb ...
2016-Dec-22 12:03:38.329200 option: fast
2016-Dec-22 12:03:38.329200 option: async
2016-Dec-22 12:03:38.329200 option: 1000
2016-Dec-22 12:03:38.407200 Blockchain initialized. last block: 1206896, d0.h0.m4.s12 time ago, current difficulty: 4591403468
2016-Dec-22 12:03:39.624003 WARNING: no two valid MoneroPulse DNS checkpoint records were received
2016-Dec-22 12:03:39.624003 Core initialized OK




5. Exit 10.1 daemon now, this will result in an Appcrash. 

Files p2pstate.bin.unportable and poolstate.bin.unportable got created.
also new p2pstate.bin and poolstate.bin got created. 













# Discussion History
## ghost | 2016-12-22T15:11:44+00:00
Sorry, have to ask - which version of boost do you have?

## medusadigital | 2016-12-23T15:33:58+00:00
i am talking about the 2 versions that get used in official 10.1 bins and the version used in the monero gui beta. 

but we should probably close this until further notice, since i can not reproduce it myself (and the error messages have to be there AFAIK)

## moneroexamples | 2016-12-24T00:08:43+00:00
Boost serialization comtability is a problem. The issue causes other problems as well: https://github.com/monero-project/monero/issues/1456

But there is already a PR aiming at solving this: https://github.com/monero-project/monero/pull/1435

## ghost | 2016-12-24T23:49:00+00:00
#1462 was merged in favour of #1435

@medusadigital Are you using a build including this boost change?

## medusadigital | 2016-12-31T12:37:57+00:00
Yes, i am using the official GUI Beta build (which includes #1462 in libwallet afaik). 

im really not sure if there is an issue at all ? 

to me it seems to incompatibility was known in advance and accepted due to the greater gain of portability ? 

the only issue was the timing, since it got merged between the daemon 10.1 and the GUI release.

or is my assumption wrong here?

## kenshi84 | 2016-12-31T14:54:34+00:00
As the author of #1462, I feel sorry if it's causing any troubles or confusions to some people. Let me clarify the behavior of the program: with the new master version which is included in the GUI, the program saves serialized data using a portable format. If it fails to de-serialize an input file using the portable format, it then tries to read the file using the old unportable format. In this case, the program copies the file into *.unportable as a backup, and the original file name will be overwritten using the portable format. So in your case,

> 1. delete p2pstate.bin and poolstate.bin
> 2. run master daemon with new boost changes
> 3. exit daemon
> 4. start 10.1 daemon

At step 3, the master daemon saves p2pstate.bin and poolstate.bin using the portable format. At step 4, the 10.1 daemon tries to read them which will be unsuccessful, hence it falls back to creating new files using the unportable format. So I'm quite certain that this procedure shouldn't result in p2pstate.bin.unportable and poolstat.bin.unportable being created.


## medusadigital | 2017-02-11T21:35:15+00:00
closing this

# Action History
- Created by: medusadigital | 2016-12-22T11:21:06+00:00
- Closed at: 2017-02-11T21:35:15+00:00
