---
title: monero-blockchain-blackball uses a lot of memory
source_url: https://github.com/monero-project/monero/issues/3875
author: jamespic
assignees: []
labels: []
created_at: '2018-05-28T10:07:54+00:00'
updated_at: '2018-08-21T18:31:05+00:00'
type: issue
status: closed
closed_at: '2018-08-21T18:31:05+00:00'
---

# Original Description
I'm running official Monero CLI 0.12.0 binaries on an Ubuntu 18.04 machine with 8GB of RAM. I run monero-blockchain-blackball with the command:

```
./monero-blockchain-blackball --blackball-db-dir /var/lib/monero/.shared-ringdb --inputs /var/lib/monero-original/lmdb /var/lib/monero/lmdb
```

Memory usage climbs constantly, easily exceeding the 8GB on the box, and going into swap memory.

I didn't obtain a core dump last time this happened, but happy to re-run it to generate one.

# Discussion History
## moneromooo-monero | 2018-05-28T10:28:17+00:00
You want to use the monero db as first parameter IIRC. Can't recall why now though :/
Maybe closing each db after each run of the "for (size_t n = 0; n < inputs.size(); ++n)" loop would help.
There could be better data structures than maps and sets for this.
There's also an incremental mode PRed to github, though I don't think that's going to do much for memory usage, unless a lot of it is shared mmap memory being mishandled by the OS.

## jamespic | 2018-06-03T18:56:57+00:00
It's not exactly a fix, but is there any value in providing an easy way to import a blackball DB (it's currently in the same file as the ring DB, so copying in a blackball DB would nuke the ring DB)? Generating a blackball DB needs a copy of the forked chain, which most main chain users won't have anyway, so it might be useful to have a way to import a blackball DB produced by a third party.

## moneromooo-monero | 2018-06-03T22:03:46+00:00
This is possible, not by straight copy (it'd nuke the ring table), but using mdb_tools.
However, a better way is to import a text file with the blackballed outputs. monero-wallet-cli can do that (see import_blackballs command). We just need someone trusted to maintain such a file (which consists of running monero-blockchain-blackball regularly, and running mdb_dump on the db to create that import file), and make it available for download. So far nobody volunteered.



## jamespic | 2018-06-03T22:31:54+00:00
Ah, I didn't spot the `import_blackballs` command - that's exactly what I was hoping for. I'm in the process of running `monero-blockchain-blackball` right now, and was planning to make the results available for download, but given the risk of abuse (including an output in the blackball list would be a great way to deanonymise it), I suspect you'd be looking for someone more trusted. 

## moneromooo-monero | 2018-08-15T11:18:39+00:00
https://github.com/monero-project/monero/pull/4260 improves memory usage a lot by using LMDB.

## SamsungGalaxyPlayer | 2018-08-21T18:14:39+00:00
I can confirm that #4260 significantly reduces RAM use. The tool now uses less than 1GB of RAM.

# Action History
- Created by: jamespic | 2018-05-28T10:07:54+00:00
- Closed at: 2018-08-21T18:31:05+00:00
