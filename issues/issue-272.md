---
title: Problem after building monero from source on OSX Mavericks
source_url: https://github.com/monero-project/monero/issues/272
author: almo2001
assignees: []
labels: []
created_at: '2015-04-25T04:05:51+00:00'
updated_at: '2015-11-24T14:53:34+00:00'
type: issue
status: closed
closed_at: '2015-11-24T14:53:34+00:00'
---

# Original Description
I have a 2013 MacPro with Mavericks on it.
I just built monero from source using brew. Seemed to build.

I set up ~/.bitmonero/blockchain.bin.

Then I go to the folder where the binaries are, and do ./bitmonerod

Looks like it's trying to allocate too large a block of memory while setting up the first block.

SilentMac:bin almo$ ./bitmonerod 
2015-Apr-25 00:01:06.940890 Starting...
2015-Apr-25 00:01:06.941116 bitmonero v0.8.8.6-release
2015-Apr-25 00:01:06.941159 Module folder: ./bitmonerod
2015-Apr-25 00:01:06.941326 Initializing P2P server...
2015-Apr-25 00:01:08.519913 Binding on 0.0.0.0:18080
2015-Apr-25 00:01:08.520011 Net service bound to 0.0.0.0:18080
2015-Apr-25 00:01:08.520038 Attempting to add IGD port mapping.
2015-Apr-25 00:01:12.730342 Added IGD port mapping.
2015-Apr-25 00:01:12.730400 P2P server initialized OK
2015-Apr-25 00:01:12.730419 Initializing protocol...
2015-Apr-25 00:01:12.730434 Protocol initialized OK
2015-Apr-25 00:01:12.730450 Initializing core RPC server...
2015-Apr-25 00:01:12.730477 Binding on 127.0.0.1:18081
2015-Apr-25 00:01:12.730552 Core RPC server initialized OK on port: 18081
2015-Apr-25 00:01:12.730574 Initializing core...
2015-Apr-25 00:01:12.730604 Loading blockchain...
bitmonerod(61618,0x7fff79a2b310) malloc: **\* mach_vm_map(size=281474976714752) failed (error code=3)
**\* error: can't allocate region
**\* set a breakpoint in malloc_error_break to debug
2015-Apr-25 00:01:40.580696 ERROR /tmp/bitmonero-Ym84G8/bitmonero-0.8.8.6/src/common/boost_serialization_helper.h:108 Exception at [unserialize_obj_from_file], what=std::bad_alloc
2015-Apr-25 00:01:40.580755 Can't load blockchain storage from file, generating genesis block.
2015-Apr-25 00:01:40.600328 ERROR /tmp/bitmonero-Ym84G8/bitmonero-0.8.8.6/src/cryptonote_core/blockchain_storage.cpp:127 Failed to add genesis block to blockchain
2015-Apr-25 00:01:40.600389 ERROR /tmp/bitmonero-Ym84G8/bitmonero-0.8.8.6/src/cryptonote_core/cryptonote_core.cpp:165 Failed to initialize blockchain storage
2015-Apr-25 00:01:40.600419 ERROR /tmp/bitmonero-Ym84G8/bitmonero-0.8.8.6/src/daemon/daemon.cpp:255 Failed to initialize core
2015-Apr-25 00:01:40.600666 Mining has been stopped, 0 finished


# Discussion History
## fluffypony | 2015-04-25T07:08:18+00:00
Ok so that's not the latest source, that's the 0.8.8.6 tagged release, which under normal circumstances would be the right choice (staging having no guarantee of stability what what), but in this situation I'd suggest trying the latest build.

Did you build it using Sammy's tap or from scratch?


## almo2001 | 2015-04-25T13:09:18+00:00
I believe I used Sammy's tap.


## fluffypony | 2015-11-24T14:53:34+00:00
Fixed


# Action History
- Created by: almo2001 | 2015-04-25T04:05:51+00:00
- Closed at: 2015-11-24T14:53:34+00:00
