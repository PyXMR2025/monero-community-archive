---
title: 'Exception: cryptonote::BLOCK_DNE'
source_url: https://github.com/monero-project/monero/issues/1360
author: ghost
assignees: []
labels:
- invalid
created_at: '2016-11-19T19:19:54+00:00'
updated_at: '2017-09-02T13:00:21+00:00'
type: issue
status: closed
closed_at: '2017-09-02T13:00:21+00:00'
---

# Original Description
Hi


My monerod service logs:

```
2016-Nov-19 14:41:05.614873 Monero 'Wolfram Warptangent' (v0.10.0.0-dbf2ab5)
2016-Nov-19 14:41:05.621149 Monero 'Wolfram Warptangent' (v0.10.0.0-dbf2ab5) Daemonised
2016-Nov-19 14:41:05.621260 Initializing cryptonote protocol...
2016-Nov-19 14:41:05.621275 Cryptonote protocol initialized OK
2016-Nov-19 14:41:05.621570 Initializing p2p server...
2016-Nov-19 14:41:08.783004 Set limit-up to 2048 kB/s
2016-Nov-19 14:41:08.783071 Set limit-down to 8192 kB/s
2016-Nov-19 14:41:08.783098 Set limit-up to 2048 kB/s
2016-Nov-19 14:41:08.783138 Set limit-down to 8192 kB/s
2016-Nov-19 14:41:08.786115 Binding on 0.0.0.0:18080
2016-Nov-19 14:41:08.786237 Net service bound to 0.0.0.0:18080
2016-Nov-19 14:41:08.786248 Attempting to add IGD port mapping.
2016-Nov-19 14:41:10.874412 Added IGD port mapping.
2016-Nov-19 14:41:10.874462 P2p server initialized OK
2016-Nov-19 14:41:10.874540 Initializing core rpc server...
2016-Nov-19 14:41:10.874586 Binding on 127.0.0.1:18081
2016-Nov-19 14:41:10.874673 Core rpc server initialized OK on port: 18081
2016-Nov-19 14:41:10.874700 Initializing core...
2016-Nov-19 14:41:10.874896 Loading blockchain from folder /var/lib/monero/lmdb ...
2016-Nov-19 14:41:10.874921 option: fast
2016-Nov-19 14:41:10.874931 option: async
2016-Nov-19 14:41:10.874940 option: 1000
2016-Nov-19 14:41:10.960789 Attempt to get block from height 732124 failed -- block not in db
2016-Nov-19 14:41:10.960859 Exception: cryptonote::BLOCK_DNE
2016-Nov-19 14:41:10.960870 Unwinded call stack:
2016-Nov-19 14:41:10.961148      1                  0x67cf40 __cxa_throw + 0x80
2016-Nov-19 14:41:10.961293      2                  0x777c7e cryptonote::HardFork::HardFork(cryptonote::BlockchainDB&, unsigned char, unsigned long, long, long, unsigned long, unsigned char) + 0xc08e
2016-Nov-19 14:41:10.961426      3                  0x70c0f8 cryptonote::BlockchainLMDB::get_block_from_height(unsigned long const&) const + 0x378
2016-Nov-19 14:41:10.961556      4                  0x766731 cryptonote::HardFork::rescan_from_block_height(unsigned long) + 0x1e1
2016-Nov-19 14:41:10.961680      5                  0x7677d5 cryptonote::HardFork::init() + 0x325
2016-Nov-19 14:41:10.961810      6                  0x5f4737 cryptonote::Blockchain::init(cryptonote::BlockchainDB*, bool, cryptonote::test_options const*) + 0x1b7
2016-Nov-19 14:41:10.961951      7                  0x6754f9 cryptonote::core::init(boost::program_options::variables_map const&, cryptonote::test_options const*) + 0x13e9
2016-Nov-19 14:41:10.962081      8                  0x4fb1fc daemonize::t_daemon::run(bool) + 0x1fc
2016-Nov-19 14:41:10.962212      9                  0x49b261 main + 0x2911
2016-Nov-19 14:41:10.962530     10                  0x7f6eb77f7291 __libc_start_main + 0xf1
2016-Nov-19 14:41:10.962672     11                  0x4a9f3a _start + 0x2a
2016-Nov-19 14:41:10.962898     12                  0x0

```


My OS: is ArchLinux
Installation mode: AUR package 
Link package AUR: https://aur.archlinux.org/packages/bitmonero-git

# Discussion History
## moneromooo-monero | 2016-11-19T21:54:13+00:00
That sounds like a corrupted blockchain.


## ghost | 2016-11-20T20:31:15+00:00
So it seems


## ghost | 2016-11-21T01:32:07+00:00
@hyc any easy tests or further info @oPensyLar could provide to find out why this became corrupted?

## hyc | 2016-11-21T14:32:39+00:00
Nothing straightforward - there is an mdb_stat command in the LMDB source that can print statistics about the DB but we don't build or provide it in the monero build. So he'd have to get the monero v0.10.0 source code from github and compile mdb_stat himself. (That's easy enough though, just type "make" in the LMDB source directory.) Then provide the output of `mdb_stat -ea <path to blockchain dir>`

## ghost | 2016-11-21T15:10:29+00:00
@hyc  Hello, mdb_stat output:


```
Environment Info
  Map address: (nil)
  Map size: 9663676416
  Page size: 4096
  Max pages: 2359296
  Number of pages used: 1393762
  Last transaction ID: 732359
  Max readers: 126
  Number of readers used: 0
Status of Main DB
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 11
Status of block_heights
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 732304
Status of block_info
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 732304
Status of blocks
  Tree depth: 4
  Branch pages: 269
  Leaf pages: 60060
  Overflow pages: 5
  Entries: 732304
Status of hf_versions
  Tree depth: 3
  Branch pages: 17
  Leaf pages: 3590
  Overflow pages: 0
  Entries: 732304
Status of output_amounts
  Tree depth: 4
  Branch pages: 473
  Leaf pages: 70403
  Overflow pages: 0
  Entries: 14557791
Status of output_txs
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 14557791
Status of properties
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1
Status of spent_keys
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 11886584
Status of tx_indices
  Tree depth: 1
  Branch pages: 0
  Leaf pages: 1
  Overflow pages: 0
  Entries: 1202281
Status of tx_outputs
  Tree depth: 3
  Branch pages: 153
  Leaf pages: 34263
  Overflow pages: 2381
  Entries: 1202281
Status of txs
  Tree depth: 4
  Branch pages: 498
  Leaf pages: 111612
  Overflow pages: 550292
  Entries: 1202281

```

## hyc | 2016-11-21T15:30:56+00:00
Thanks for that. The blocks, block_heights, and block_info table all seem to agree with each other. You could try using mdb_dump to see if blocks and block_info contain the same keys: `mdb_dump -s blocks <path to DB>`  and `mdb_dump -s block_info <path to DB>`

Don't paste the output here, it'll be too big. The output is a pair of lines, the first line is the key and the second line is the data, all in hex. The idea is to find the record for key 732124, hex 0B2BDC.

## ghost | 2016-11-21T22:58:31+00:00
mdb_dump after 5 minutes..

0101caceedad05f954316ce6b98f605b088a3403c13c146ea71f62e66295277667e390c75ed2073beaffff01ca982901ff8e982904fe80f2871202cc60781443ca0a2ea7d887d27f2a00d29c9618342ba3fb761f2ecc9db29c56088088aca3cf0202e81bb20eb666c14171832fb4409d36274b1d9e0bbae6a9c0504451c760b1a7d680a0b787e90502cd1a6043fd3e5372743bb18343470b7fe7d2285054cef73f20763b288814c40c80a0b6cef78502026d6bbc958e1dcbc42b0f29f77f0973df3b58c8fbb6337ea07caa0fb9c7da0c9b57018bdcdd1da929124450dc022fef288c868f2960602161026769d494de7f33dbd002114dadc201000000000000000000000000000321005252b6d5509fe12471f8bd4b8687313732124a726c90274c296f13192864b13a01e982428c45db8ddc3dbe236a948691b3f2ac37905e124f89e8a54df2153e3e08
 

0100df9bffae05acf64734d7c771a4a41db53f889b680fbdf90243777e2712a85ab669a4c675853c0b000001dbcb2b01ff9fcb2b0489e5c8931602d6107628fcea5fbd962385373212464f24d8a1ed3f0ebb30ee739774fed6871f8090dfc04a020376b90789dfd0aa28bf567f8b259c6f0148c265856aae8b68f8b0fd55cf8da580d0b8e1981a02c01681cc7d46787621fc526a53300e8b4b6bcf8b8531e20e3876ff26b9cfee708080a2a9eae8010245662eb5e04fbedd81b790db5f1ec0dba8fa858adc3d3e63b799fe25fc5f58b62b019885520a0c157280c845f907679ce840534a8f8090c252c97db6c2837441b2a202080000000618b43cc200

mdb.c:5697: Assertion 'IS_LEAF(mp)' failed in mdb_cursor_next()


Corrupt database?

## hyc | 2016-11-22T02:12:19+00:00
Indeed, seems corrupt. There is something else we can try, if you're comfortable with binary/hex editing files. (In the future there will be an LMDB option to do this without requiring such munging.) LMDB always maintains two versions of the DB and ping-pongs between them. When opening a DB it always uses the most recent version. However it's possible that the previous version is intact when the latest version is corrupted. You can trick the current code into using the previous version by editing the data.mdb file and changing a transaction ID in the file. The transaction ID is a 64bit (8 byte) integer stored at offset 0x0090 and 0x1090 in the data.mdb file. When LMDB opens a DB file it reads both IDs and whichever is greater is the most recent. To force it to use the other version instead, find whichever is currently the greatest and subtract 2 from it. Store that value with your editor, and then see if mdb_dump works. If it does, then you should be able to resume using the DB. If this is all over your head then never mind; mucking around with binary editing isn't really a safe thing for novices.

## moneromooo-monero | 2017-09-02T12:55:18+00:00
That option is now in the upcoming release, --db-salvage.

Anyway, this is a corrupt file, not a bug, so closing as invalid.

+invalid

# Action History
- Created by: ghost | 2016-11-19T19:19:54+00:00
- Closed at: 2017-09-02T13:00:21+00:00
