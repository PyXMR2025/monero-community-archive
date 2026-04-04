---
title: 's390x: notice regarding incompatbile lmdb format'
source_url: https://github.com/monero-project/monero/issues/9484
author: bolives-hax
assignees: []
labels:
- question
- low priority
- database
created_at: '2024-09-15T13:37:12+00:00'
updated_at: '2024-09-24T00:53:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hey I build monerod and monero-wallet-cli for s390x and ran it on one of my hosts (testnet fauccet worked) but while I now know that copying over the lmdb file from a little endian host such as my x86 host to my big endian s390x host  isn't possible due to the endianess mismatch. It would be great to maybe make monerod be aware of the differences between the 2 formats and report it before exiting with an error as other people may not come across this issue or draw the conlcusion themself as to why that happened. 

Other than that im happy to report monero-wallet-cli + monerod (--testnet) seem to work fine on s390x against all initial expectations and i was able to send funds in a circle on testnet from and to my x86 host and back to s390x

# Discussion History
## moneromooo-monero | 2024-09-19T14:52:34+00:00
It would help if you could make available an empty database in big endian format (ie, start monerod with --offline --data-dir /tmp/monerobe, which would create an empty db with just the genesis block). Then any detection code can be checked with it.

## jeffro256 | 2024-09-22T05:27:39+00:00
IIRC, LMDB is also ABI dependent. For example, the struct `mdb_block_info` is read/written directly as it's in-memory format. This in-memory format is ABI-dependent because of padding, although most compilers for 64-bit targets, even across OSes, are going to follow the same packing scheme (put the minimum number of bytes after a member field such that the next member field's offset is a multiple of it's alignment). 

## hyc | 2024-09-22T19:10:30+00:00
> most compilers for 64-bit targets, even across OSes, are going to follow the same packing scheme (put the minimum number of bytes after a member field such that the next member field's offset is a multiple of it's alignment).

That should be true of all compilers. But yes, it's imperative that developers working on this code keep data size and alignment in mind when modifying structure definitions.

And the data types should be explicitly sized such that they're the same on 32 bit targets as well. AFAIK this has all been ensured up till now. And of course, 32 bit is going extinct anyway so that's not such a huge concern any more.


## bolives-hax | 2024-09-24T00:49:37+00:00
> It would help if you could make available an empty database in big endian format (ie, start monerod with --offline --data-dir /tmp/monerobe, which would create an empty db with just the genesis block). Then any detection code can be checked with it.

I have created a git repository containing the lmdb database file as well as the bitmonro log file. 

https://github.com/bolives-hax/monrod-bigendian-demo-lmdb

The monerod I compiled was invoked via

```bash

/nix/store/p5q0klnh2bynm9mwdkcw6z1c3hm81kk9-monero-cli-0.18.3.3/bin/monerod  --offline --data-dir /tmp/monerobe

```

in my case with which should be just the way you requested it to be 

# Action History
- Created by: bolives-hax | 2024-09-15T13:37:12+00:00
