---
title: monero-blockchain-prune prune DB from 80 GB -> to 83 GB - bravo! :)
source_url: https://github.com/monero-project/monero/issues/9500
author: itmagpro
assignees: []
labels:
- invalid
- question
- low priority
- more info needed
created_at: '2024-10-03T07:07:37+00:00'
updated_at: '2024-11-04T16:04:18+00:00'
type: issue
status: closed
closed_at: '2024-11-04T16:04:18+00:00'
---

# Original Description
Ha-ha-ha! ))) monero-blockchain-prune prune DB from 80 GB -> to 83 GB - bravo!

```
$ monero-blockchain-prune --help
Monero 'Fluorine Fermi' (v0.18.3.4-release)
...
$ monero-blockchain-prune --copy-pruned-database --db-sync-mode=fast:8000
2024-09-29 19:36:42.145	I Starting...
2024-09-29 19:36:42.145	I Initializing source blockchain (BlockchainDB)
2024-09-29 19:36:42.150	I Loading blockchain from folder "~/.bitmonero/lmdb" ...
2024-09-29 19:36:42.151	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2024-09-29 19:36:42.682	I source blockchain storage initialized OK
2024-09-29 19:36:42.687	I Loading blockchain from folder "~/.bitmonero/lmdb-pruned" ...
2024-09-29 19:36:42.689	W The blockchain is on a rotating drive: this will be very slow, use an SSD if possible
2024-09-29 19:36:44.803	I pruned blockchain storage initialized OK
2024-09-29 19:36:45.209	I Pruning...
2024-09-29 19:36:45.215	I Copying blocks
2024-09-29 19:54:47.580	I LMDB Mapsize increased.  Old: 1024MiB, New: 1539MiB <<<--- 540M
2024-09-29 20:18:18.859	I LMDB Mapsize increased.  Old: 1539MiB, New: 2059MiB
2024-09-29 20:52:26.540	I LMDB Mapsize increased.  Old: 2059MiB, New: 2575MiB
2024-09-29 21:44:26.315	I LMDB Mapsize increased.  Old: 2575MiB, New: 3091MiB
2024-09-29 22:17:37.114	I LMDB Mapsize increased.  Old: 3091MiB, New: 3623MiB
2024-09-29 22:25:06.761	I Copying block_info
2024-09-29 22:41:40.356	I Copying block_heights
2024-09-29 22:44:49.883	I LMDB Mapsize increased.  Old: 3623MiB, New: 4135MiB
2024-09-29 22:52:48.472	I Copying txs_pruned
2024-09-29 23:04:47.945	I LMDB Mapsize increased.  Old: 4135MiB, New: 4664MiB
2024-09-29 23:24:43.046	I LMDB Mapsize increased.  Old: 4664MiB, New: 5182MiB
2024-09-29 23:45:29.371	I LMDB Mapsize increased.  Old: 5182MiB, New: 5694MiB
2024-09-30 00:20:40.711	I LMDB Mapsize increased.  Old: 5694MiB, New: 6212MiB
2024-09-30 00:41:16.895	I LMDB Mapsize increased.  Old: 6212MiB, New: 6727MiB
2024-09-30 01:02:02.746	I LMDB Mapsize increased.  Old: 6727MiB, New: 7242MiB
2024-09-30 01:24:13.983	I LMDB Mapsize increased.  Old: 7242MiB, New: 7754MiB
2024-09-30 01:44:18.274	I LMDB Mapsize increased.  Old: 7754MiB, New: 8267MiB
2024-09-30 02:04:02.637	I LMDB Mapsize increased.  Old: 8267MiB, New: 8783MiB
2024-09-30 02:25:05.323	I LMDB Mapsize increased.  Old: 8783MiB, New: 9297MiB
2024-09-30 02:43:27.032	I LMDB Mapsize increased.  Old: 9297MiB, New: 9811MiB
2024-09-30 03:01:33.020	I LMDB Mapsize increased.  Old: 9811MiB, New: 10326MiB
2024-09-30 03:19:25.945	I LMDB Mapsize increased.  Old: 10326MiB, New: 10839MiB
2024-09-30 03:41:35.700	I LMDB Mapsize increased.  Old: 10839MiB, New: 11352MiB
2024-09-30 04:02:24.309	I LMDB Mapsize increased.  Old: 11352MiB, New: 11866MiB
2024-09-30 04:20:05.390	I LMDB Mapsize increased.  Old: 11866MiB, New: 12378MiB
2024-09-30 04:54:50.040	I LMDB Mapsize increased.  Old: 12378MiB, New: 12891MiB
2024-09-30 05:34:04.543	I LMDB Mapsize increased.  Old: 12891MiB, New: 13403MiB
2024-09-30 05:52:04.426	I LMDB Mapsize increased.  Old: 13403MiB, New: 13918MiB
2024-09-30 06:15:15.952	I LMDB Mapsize increased.  Old: 13918MiB, New: 14430MiB
2024-09-30 06:38:50.981	I LMDB Mapsize increased.  Old: 14430MiB, New: 14944MiB
2024-09-30 07:02:57.808	I LMDB Mapsize increased.  Old: 14944MiB, New: 15457MiB
2024-09-30 07:31:34.534	I LMDB Mapsize increased.  Old: 15457MiB, New: 15973MiB
2024-09-30 08:02:09.626	I LMDB Mapsize increased.  Old: 15973MiB, New: 16485MiB
2024-09-30 08:23:22.767	I LMDB Mapsize increased.  Old: 16485MiB, New: 17000MiB
2024-09-30 08:43:28.056	I LMDB Mapsize increased.  Old: 17000MiB, New: 17513MiB
2024-09-30 09:02:38.888	I LMDB Mapsize increased.  Old: 17513MiB, New: 18028MiB
2024-09-30 09:23:01.503	I LMDB Mapsize increased.  Old: 18028MiB, New: 18542MiB
2024-09-30 09:44:31.837	I LMDB Mapsize increased.  Old: 18542MiB, New: 19058MiB
2024-09-30 10:00:57.732	I LMDB Mapsize increased.  Old: 19058MiB, New: 19575MiB
2024-09-30 10:14:52.300	I LMDB Mapsize increased.  Old: 19575MiB, New: 20090MiB
2024-09-30 10:34:30.008	I LMDB Mapsize increased.  Old: 20090MiB, New: 20602MiB
2024-09-30 10:54:06.689	I LMDB Mapsize increased.  Old: 20602MiB, New: 21115MiB
2024-09-30 11:14:45.578	I LMDB Mapsize increased.  Old: 21115MiB, New: 21628MiB
2024-09-30 11:33:52.347	I LMDB Mapsize increased.  Old: 21628MiB, New: 22142MiB
2024-09-30 11:52:06.918	I LMDB Mapsize increased.  Old: 22142MiB, New: 22655MiB
2024-09-30 12:10:13.637	I LMDB Mapsize increased.  Old: 22655MiB, New: 23168MiB
2024-09-30 12:26:35.651	I LMDB Mapsize increased.  Old: 23168MiB, New: 23681MiB
2024-09-30 12:42:05.387	I LMDB Mapsize increased.  Old: 23681MiB, New: 24195MiB
2024-09-30 12:58:14.525	I LMDB Mapsize increased.  Old: 24195MiB, New: 24708MiB
2024-09-30 13:14:28.792	I LMDB Mapsize increased.  Old: 24708MiB, New: 25224MiB
2024-09-30 13:33:13.457	I LMDB Mapsize increased.  Old: 25224MiB, New: 25739MiB
2024-09-30 13:50:51.824	I LMDB Mapsize increased.  Old: 25739MiB, New: 26254MiB
2024-09-30 14:08:21.257	I LMDB Mapsize increased.  Old: 26254MiB, New: 26770MiB
2024-09-30 14:26:17.221	I LMDB Mapsize increased.  Old: 26770MiB, New: 27283MiB
2024-09-30 14:30:50.930	I Copying txs_prunable_hash
2024-09-30 14:45:19.588	I LMDB Mapsize increased.  Old: 27283MiB, New: 27795MiB
2024-09-30 15:01:14.397	I LMDB Mapsize increased.  Old: 27795MiB, New: 28307MiB
2024-09-30 15:31:15.868	I LMDB Mapsize increased.  Old: 28307MiB, New: 28820MiB
2024-09-30 15:58:24.052	I LMDB Mapsize increased.  Old: 28820MiB, New: 29332MiB
2024-09-30 16:12:21.144	I Copying tx_indices
2024-09-30 16:20:10.933	I LMDB Mapsize increased.  Old: 29332MiB, New: 29844MiB
2024-09-30 16:38:13.585	I LMDB Mapsize increased.  Old: 29844MiB, New: 30357MiB
2024-09-30 16:56:38.880	I LMDB Mapsize increased.  Old: 30357MiB, New: 30870MiB
2024-09-30 17:15:01.495	I LMDB Mapsize increased.  Old: 30870MiB, New: 31383MiB
2024-09-30 17:33:06.305	I LMDB Mapsize increased.  Old: 31383MiB, New: 31895MiB
2024-09-30 17:51:41.397	I LMDB Mapsize increased.  Old: 31895MiB, New: 32408MiB
2024-09-30 18:10:01.680	I LMDB Mapsize increased.  Old: 32408MiB, New: 32921MiB
2024-09-30 18:28:16.972	I LMDB Mapsize increased.  Old: 32921MiB, New: 33434MiB
2024-09-30 18:46:45.812	I LMDB Mapsize increased.  Old: 33434MiB, New: 33946MiB
2024-09-30 19:05:05.932	I LMDB Mapsize increased.  Old: 33946MiB, New: 34459MiB
2024-09-30 19:22:16.823	I Copying tx_outputs
2024-09-30 19:23:08.353	I LMDB Mapsize increased.  Old: 34459MiB, New: 34972MiB
2024-09-30 19:41:14.365	I LMDB Mapsize increased.  Old: 34972MiB, New: 35484MiB
2024-09-30 20:03:18.925	I LMDB Mapsize increased.  Old: 35484MiB, New: 35996MiB
2024-09-30 20:35:07.485	I LMDB Mapsize increased.  Old: 35996MiB, New: 36508MiB
2024-09-30 20:51:38.155	I Copying output_txs
2024-09-30 20:54:48.267	I LMDB Mapsize increased.  Old: 36508MiB, New: 37020MiB
2024-09-30 21:12:07.420	I LMDB Mapsize increased.  Old: 37020MiB, New: 37532MiB
2024-09-30 21:29:18.266	I LMDB Mapsize increased.  Old: 37532MiB, New: 38044MiB
2024-09-30 21:47:40.671	I LMDB Mapsize increased.  Old: 38044MiB, New: 38556MiB
2024-09-30 22:01:57.292	I LMDB Mapsize increased.  Old: 38556MiB, New: 39068MiB
2024-09-30 22:16:28.039	I LMDB Mapsize increased.  Old: 39068MiB, New: 39581MiB
2024-09-30 22:45:44.285	I LMDB Mapsize increased.  Old: 39581MiB, New: 40093MiB
2024-09-30 23:11:08.540	I LMDB Mapsize increased.  Old: 40093MiB, New: 40605MiB
2024-09-30 23:36:55.051	I LMDB Mapsize increased.  Old: 40605MiB, New: 41117MiB
2024-10-01 00:03:55.808	I LMDB Mapsize increased.  Old: 41117MiB, New: 41629MiB
2024-10-01 00:28:25.102	I LMDB Mapsize increased.  Old: 41629MiB, New: 42141MiB
2024-10-01 00:51:44.446	I LMDB Mapsize increased.  Old: 42141MiB, New: 42653MiB
2024-10-01 01:14:24.312	I LMDB Mapsize increased.  Old: 42653MiB, New: 43165MiB
2024-10-01 01:18:41.058	I Copying output_amounts
2024-10-01 01:33:41.027	I LMDB Mapsize increased.  Old: 43165MiB, New: 43678MiB
2024-10-01 01:51:27.853	I LMDB Mapsize increased.  Old: 43678MiB, New: 44191MiB
2024-10-01 02:06:25.649	I LMDB Mapsize increased.  Old: 44191MiB, New: 44703MiB
2024-10-01 02:21:22.037	I LMDB Mapsize increased.  Old: 44703MiB, New: 45216MiB
2024-10-01 02:34:31.122	I LMDB Mapsize increased.  Old: 45216MiB, New: 45729MiB
2024-10-01 02:48:23.545	I LMDB Mapsize increased.  Old: 45729MiB, New: 46242MiB
2024-10-01 03:01:37.443	I LMDB Mapsize increased.  Old: 46242MiB, New: 46754MiB
2024-10-01 03:17:37.748	I LMDB Mapsize increased.  Old: 46754MiB, New: 47267MiB
2024-10-01 03:43:12.006	I LMDB Mapsize increased.  Old: 47267MiB, New: 47780MiB
2024-10-01 04:04:46.173	I LMDB Mapsize increased.  Old: 47780MiB, New: 48293MiB
2024-10-01 04:32:39.734	I LMDB Mapsize increased.  Old: 48293MiB, New: 48805MiB
2024-10-01 04:59:57.397	I LMDB Mapsize increased.  Old: 48805MiB, New: 49318MiB
2024-10-01 05:23:40.321	I LMDB Mapsize increased.  Old: 49318MiB, New: 49831MiB
2024-10-01 05:47:34.228	I LMDB Mapsize increased.  Old: 49831MiB, New: 50344MiB
2024-10-01 06:11:31.593	I LMDB Mapsize increased.  Old: 50344MiB, New: 50856MiB
2024-10-01 06:34:24.959	I LMDB Mapsize increased.  Old: 50856MiB, New: 51369MiB
2024-10-01 06:55:50.642	I LMDB Mapsize increased.  Old: 51369MiB, New: 51881MiB
2024-10-01 07:15:27.694	I LMDB Mapsize increased.  Old: 51881MiB, New: 52394MiB
2024-10-01 07:35:56.084	I LMDB Mapsize increased.  Old: 52394MiB, New: 52907MiB
2024-10-01 07:54:42.455	I LMDB Mapsize increased.  Old: 52907MiB, New: 53419MiB
2024-10-01 08:13:59.612	I LMDB Mapsize increased.  Old: 53419MiB, New: 53932MiB
2024-10-01 08:35:16.146	I LMDB Mapsize increased.  Old: 53932MiB, New: 54444MiB
2024-10-01 08:56:39.455	I LMDB Mapsize increased.  Old: 54444MiB, New: 54957MiB
2024-10-01 09:15:17.477	I LMDB Mapsize increased.  Old: 54957MiB, New: 55469MiB
2024-10-01 09:24:51.527	I Copying spent_keys
2024-10-01 09:33:09.763	I LMDB Mapsize increased.  Old: 55469MiB, New: 55981MiB
2024-10-01 10:01:40.874	I LMDB Mapsize increased.  Old: 55981MiB, New: 56493MiB
2024-10-01 10:41:40.728	I LMDB Mapsize increased.  Old: 56493MiB, New: 57006MiB
2024-10-01 11:20:00.175	I LMDB Mapsize increased.  Old: 57006MiB, New: 57518MiB
2024-10-01 11:42:10.916	I LMDB Mapsize increased.  Old: 57518MiB, New: 58030MiB
2024-10-01 12:02:57.525	I LMDB Mapsize increased.  Old: 58030MiB, New: 58542MiB
2024-10-01 12:22:55.134	I LMDB Mapsize increased.  Old: 58542MiB, New: 59054MiB
2024-10-01 12:43:31.125	I LMDB Mapsize increased.  Old: 59054MiB, New: 59566MiB
2024-10-01 13:02:32.315	I LMDB Mapsize increased.  Old: 59566MiB, New: 60079MiB
2024-10-01 13:22:53.319	I LMDB Mapsize increased.  Old: 60079MiB, New: 60591MiB
2024-10-01 13:42:51.842	I LMDB Mapsize increased.  Old: 60591MiB, New: 61103MiB
2024-10-01 14:02:42.676	I LMDB Mapsize increased.  Old: 61103MiB, New: 61615MiB
2024-10-01 14:22:09.442	I LMDB Mapsize increased.  Old: 61615MiB, New: 62127MiB
2024-10-01 14:40:53.841	I LMDB Mapsize increased.  Old: 62127MiB, New: 62639MiB
2024-10-01 14:43:03.107	I Copying txpool_meta
2024-10-01 14:43:03.150	I Copying txpool_blob
2024-10-01 14:43:03.150	I Copying hf_versions
2024-10-01 14:45:47.593	I Copying properties
2024-10-01 14:45:47.616	I Copying txs_prunable
2024-10-01 14:51:14.070	I LMDB Mapsize increased.  Old: 62639MiB, New: 63158MiB
2024-10-01 14:59:32.503	I LMDB Mapsize increased.  Old: 63158MiB, New: 63670MiB
2024-10-01 15:09:56.309	I LMDB Mapsize increased.  Old: 63670MiB, New: 64189MiB
2024-10-01 15:15:44.299	I LMDB Mapsize increased.  Old: 64189MiB, New: 64705MiB
2024-10-01 15:23:01.899	I LMDB Mapsize increased.  Old: 64705MiB, New: 65223MiB
2024-10-01 15:27:44.035	I LMDB Mapsize increased.  Old: 65223MiB, New: 65764MiB
2024-10-01 15:28:40.925	I LMDB Mapsize increased.  Old: 65764MiB, New: 66326MiB
2024-10-01 15:29:43.803	I LMDB Mapsize increased.  Old: 66326MiB, New: 66951MiB
2024-10-01 15:30:40.578	I LMDB Mapsize increased.  Old: 66951MiB, New: 67513MiB
2024-10-01 15:31:40.012	I LMDB Mapsize increased.  Old: 67513MiB, New: 68054MiB
2024-10-01 15:32:34.339	I LMDB Mapsize increased.  Old: 68054MiB, New: 68598MiB
2024-10-01 15:35:03.523	I LMDB Mapsize increased.  Old: 68598MiB, New: 69222MiB
2024-10-01 15:39:02.799	I LMDB Mapsize increased.  Old: 69222MiB, New: 69834MiB
2024-10-01 15:42:19.416	I LMDB Mapsize increased.  Old: 69834MiB, New: 70384MiB
2024-10-01 15:44:53.955	I LMDB Mapsize increased.  Old: 70384MiB, New: 70927MiB
2024-10-01 15:47:28.403	I LMDB Mapsize increased.  Old: 70927MiB, New: 71457MiB
2024-10-01 15:48:53.543	I LMDB Mapsize increased.  Old: 71457MiB, New: 71987MiB
2024-10-01 15:58:54.362	I LMDB Mapsize increased.  Old: 71987MiB, New: 72517MiB
2024-10-01 16:03:05.257	I LMDB Mapsize increased.  Old: 72517MiB, New: 73036MiB
2024-10-01 16:05:51.478	I LMDB Mapsize increased.  Old: 73036MiB, New: 73549MiB
2024-10-01 16:10:11.636	I LMDB Mapsize increased.  Old: 73549MiB, New: 74081MiB
2024-10-01 16:14:52.395	I LMDB Mapsize increased.  Old: 74081MiB, New: 74603MiB
2024-10-01 16:21:07.690	I LMDB Mapsize increased.  Old: 74603MiB, New: 75125MiB
2024-10-01 16:27:18.449	I LMDB Mapsize increased.  Old: 75125MiB, New: 75641MiB
2024-10-01 16:36:56.533	I LMDB Mapsize increased.  Old: 75641MiB, New: 76158MiB
2024-10-01 16:50:03.761	I LMDB Mapsize increased.  Old: 76158MiB, New: 76681MiB
2024-10-01 17:04:51.705	I LMDB Mapsize increased.  Old: 76681MiB, New: 77201MiB
2024-10-01 17:19:53.155	I LMDB Mapsize increased.  Old: 77201MiB, New: 77718MiB
2024-10-01 17:34:05.453	I LMDB Mapsize increased.  Old: 77718MiB, New: 78238MiB
2024-10-01 17:48:44.949	I LMDB Mapsize increased.  Old: 78238MiB, New: 78766MiB
2024-10-01 18:02:31.366	I LMDB Mapsize increased.  Old: 78766MiB, New: 79282MiB
2024-10-01 18:17:21.821	I LMDB Mapsize increased.  Old: 79282MiB, New: 79808MiB
2024-10-01 18:31:37.357	I LMDB Mapsize increased.  Old: 79808MiB, New: 80334MiB
2024-10-01 18:45:51.845	I LMDB Mapsize increased.  Old: 80334MiB, New: 80862MiB
2024-10-01 19:00:00.515	I LMDB Mapsize increased.  Old: 80862MiB, New: 81393MiB
2024-10-01 19:13:45.032	I LMDB Mapsize increased.  Old: 81393MiB, New: 81913MiB
2024-10-01 19:26:04.985	I LMDB Mapsize increased.  Old: 81913MiB, New: 82429MiB
2024-10-01 19:38:04.479	I LMDB Mapsize increased.  Old: 82429MiB, New: 82945MiB
2024-10-01 19:51:24.197	I LMDB Mapsize increased.  Old: 82945MiB, New: 83467MiB
2024-10-01 20:04:22.853	I LMDB Mapsize increased.  Old: 83467MiB, New: 83984MiB
2024-10-01 20:17:57.590	I LMDB Mapsize increased.  Old: 83984MiB, New: 84504MiB
2024-10-01 20:32:41.321	I LMDB Mapsize increased.  Old: 84504MiB, New: 85031MiB
2024-10-01 20:43:10.707	I Copying txs_prunable_tip
2024-10-01 20:43:32.544	I Swapping databases, pre-pruning blockchain will be left in ~/.bitmonero/lmdb-old and can be removed if desired
2024-10-01 20:43:32.686	I Blockchain pruned OK
```

2 day wasted. Great pruning! :)

```
$ du -shc ~/.bitmonero/lmdb-old
80G
$ du -shc ~/.bitmonero/lmdb
83G
```

# Discussion History
## nahuhh | 2024-10-03T19:30:01+00:00
~80gb is the pruned db

the full db is ~205gb

## itmagpro | 2024-10-03T20:14:43+00:00
> nahuhh

you genius...

## 0xFFFC0000 | 2024-10-04T18:05:28+00:00
I would appreciate if you clarify what is the exact issue is. 


Otherwise I have to close this issue as unrelated. 

## itmagpro | 2024-10-04T20:45:47+00:00
**You no have brain for understand different between src DB file size 80 GB and result DB file size 83 GB after work your program!?** Then nothing to talk about with you.

## nahuhh | 2024-10-05T06:54:26+00:00
> **You no have brain for understand different between src DB file size 80 GB and result DB file size 83 GB after work your program!?** Then nothing to talk about with you.

Perhaps the tool should have output an error to say "the db youre trying to prune is already pruned. Kthxbye"

the size difference is a nonissue

## itmagpro | 2024-10-05T07:56:58+00:00
> the size (BIG SIZE) difference is a nonissue

ok, - then is a bug.

and you ... stup... idi..t!


## nahuhh | 2024-10-05T14:32:51+00:00
> > the size (BIG SIZE) difference is a nonissue
> 
> ok, - then is a bug.
> 
> and you ... stup... idi..t!
> 

It's not a bug. LMDB is not deterministic. The output size is liable to change between runs. 

## itmagpro | 2024-10-05T15:04:47+00:00
> The output size is liable to change between runs.

Ok, bro! I all understand.., BUT 3 GB - it is **very BIG change** between runs!!! 

Plus 540M "between runs" to result file like 80,5 GB instead 80 - may be.., BUT NOT 3 GB (83 in result)!

Or you don't think so? :)

# Action History
- Created by: itmagpro | 2024-10-03T07:07:37+00:00
- Closed at: 2024-11-04T16:04:18+00:00
