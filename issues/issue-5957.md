---
title: chunk size warnings in blockchain export, fatal error in import
source_url: https://github.com/monero-project/monero/issues/5957
author: ndorf
assignees: []
labels: []
created_at: '2019-10-02T20:23:44+00:00'
updated_at: '2019-10-24T15:55:22+00:00'
type: issue
status: closed
closed_at: '2019-10-24T15:55:22+00:00'
---

# Original Description
I'm trying to export the blockchain from one node and import it on another. Both are using the same software version (v0.14.1.2-release) and running on stagenet. The source (exporter) is FreeBSD 11.2 while the destination (importer) is Ubuntu 18.04.

The exporter logs a bunch of warnings about chunk_size, but these appear to be non-fatal and the process completes anyway:
```
2019-10-02 19:54:29.567	W Exporting blockchain raw data...
2019-10-02 19:54:29.567	I Storing blocks raw data...
2019-10-02 19:54:29.568	I source blockchain height: 423174
2019-10-02 19:54:29.568	I Using block height of source blockchain: 423174
2019-10-02 20:04:37.769 W WARNING: chunk_size 1064978 > BUFFER_SIZE 1000000
2019-10-02 20:04:37.860	W WARNING: chunk_size 1104766 > BUFFER_SIZE 1000000
2019-10-02 20:04:37.907	W WARNING: chunk_size 1120106 > BUFFER_SIZE 1000000
2019-10-02 20:04:38.001	W WARNING: chunk_size 1131990 > BUFFER_SIZE 1000000
2019-10-02 20:04:38.058	W WARNING: chunk_size 1147996 > BUFFER_SIZE 1000000
2019-10-02 20:04:40.614	W WARNING: chunk_size 1177307 > BUFFER_SIZE 1000000
2019-10-02 20:04:40.756	W WARNING: chunk_size 1205335 > BUFFER_SIZE 1000000
2019-10-02 20:04:40.851	W WARNING: chunk_size 1204968 > BUFFER_SIZE 1000000
2019-10-02 20:04:41.053	W WARNING: chunk_size 1205241 > BUFFER_SIZE 1000000
2019-10-02 20:04:41.177	W WARNING: chunk_size 1204891 > BUFFER_SIZE 1000000
2019-10-02 20:04:41.314	W WARNING: chunk_size 1206780 > BUFFER_SIZE 1000000
2019-10-02 20:04:42.533	W WARNING: chunk_size 1200679 > BUFFER_SIZE 1000000
2019-10-02 20:04:42.728	W WARNING: chunk_size 1160495 > BUFFER_SIZE 1000000
2019-10-02 20:04:43.048	W WARNING: chunk_size 1192786 > BUFFER_SIZE 1000000
block 423174/423174                 
2019-10-02 20:07:15.064	I Number of blocks exported: 423175
2019-10-02 20:07:15.075	I Largest chunk: 1206780 bytes
2019-10-02 20:07:15.084	W Blockchain raw data exported OK
```

The importer logs one similar warning, and immediately aborts:

```
2019-10-02 20:16:22.986	I Loading checkpoints
2019-10-02 20:16:30.599	I bootstrap file recognized
2019-10-02 20:16:30.599	I bootstrap::file_info size: 4
2019-10-02 20:16:30.600	I bootstrap file v1.0
2019-10-02 20:16:30.600	I bootstrap magic size: 4
2019-10-02 20:16:30.600	I bootstrap header size: 1024
2019-10-02 20:16:30.600	I Scanning blockchain from bootstrap file...
2019-10-02 20:16:32.863 W WARNING: chunk_size 1064978 > BUFFER_SIZE 1000000  height: 1, offset 898531
2019-10-02 20:16:32.880	E Exception at [Import error], what=Aborting: chunk size exceeds buffer size
```

What could be the problem? The node exported-from appears to be fine and happily serving wallets, so I don't think the blockchain is corrupt.

# Discussion History
## moneromooo-monero | 2019-10-02T21:00:08+00:00
You probably have to use a smaller number of blocks per chunk.

## moneromooo-monero | 2019-10-02T21:06:39+00:00
Looks like it's just always 1 block per chunk, so the problem is elsehwere.

## ndorf | 2019-10-02T21:17:03+00:00
Although the warning message says height=1, it doesn't actually appear until it gets to approximately block 360000 (of the initial scanning stage, not the actual import).

Same thing on the export side, no warnings until it gets to that height.



## ndorf | 2019-10-02T21:18:05+00:00
Just for fun, I tried `--batch-size=2000000`, `--batch-size=10` and `--batch=0` and the result is the same for all 3.

## moneromooo-monero | 2019-10-02T23:01:55+00:00
Actually, there really are such large blocks on stagenet. The size limits just need bumping.

## ndorf | 2019-10-02T23:36:57+00:00
Ah, ok, thanks. I'll give that a shot and PR if it works.

## ndorf | 2019-10-04T19:24:40+00:00
Weird, it worked with `--dangerous-unverified-import=1` but not without it (verification fails). Still looking into it.

# Action History
- Created by: ndorf | 2019-10-02T20:23:44+00:00
- Closed at: 2019-10-24T15:55:22+00:00
