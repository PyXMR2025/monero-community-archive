---
title: '[Bug] `monero-blockchain-prune` copies the whole DB. Extremely slowly.'
source_url: https://github.com/monero-project/monero/issues/9097
author: Erquint
assignees: []
labels:
- bug
- database
- reproduction needed
created_at: '2023-12-23T14:57:18+00:00'
updated_at: '2025-08-30T18:22:45+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Initially setting up the node in the GUI wallet a long time ago I picked the pruned option.
The CLI option for pruning was not added but I assumed a DB seeded as pruned wouldn't be able to grow to the full ledger size. I was wrong.

Ran the daemon ever since without the pruning CLI option until it gradually reached 172 GB, which seems like the size of the full ledger. Added the CLI option and ran like that recently.

There was some option to check if it's pruned in `monerod` itself, IIRC, which reported it as pruned.

However, pruning with `monerod` does not reduce the file size, as it only marks entries available for overwriting. I wanted to deflate the database by discarding the marked entries from disk. And that's what `monero-blockchain-prune` is supposedly for.

Running `monero-blockchain-prune` prints `Blockchain is already pruned, use --copy-pruned-database to copy it anyway`. So I added that option.

```
PS C:\Program Files\Monero GUI Wallet> .\monero-blockchain-prune.exe --db-sync-mode=fastest --data-dir=F:\blockchain\bitmonero --copy-pruned-database
2023-12-20 18:05:33.256 I Starting...
2023-12-20 18:05:33.256 I Initializing source blockchain (BlockchainDB)
2023-12-20 18:05:33.257 I Loading blockchain from folder "F:\blockchain\bitmonero\lmdb" ...
2023-12-20 18:05:33.315 I source blockchain storage initialized OK
2023-12-20 18:05:33.887 I Loading blockchain from folder "F:\blockchain\bitmonero\lmdb-pruned" ...
2023-12-20 18:05:34.029 I pruned blockchain storage initialized OK
2023-12-20 18:05:34.081 I Pruning...
2023-12-20 18:05:34.082 I Copying blocks
2023-12-20 18:20:18.332 I LMDB Mapsize increased.  Old: 1024MiB, New: 1536MiB
2023-12-20 18:39:41.664 I LMDB Mapsize increased.  Old: 1536MiB, New: 2048MiB
2023-12-20 18:56:47.871 I LMDB Mapsize increased.  Old: 2048MiB, New: 2560MiB
2023-12-20 19:13:10.387 I LMDB Mapsize increased.  Old: 2560MiB, New: 3073MiB
2023-12-20 19:19:13.470 I Copying block_info
2023-12-20 19:29:33.322 I Copying block_heights
2023-12-20 19:31:12.863 I LMDB Mapsize increased.  Old: 3073MiB, New: 3585MiB
2023-12-20 19:38:13.909 I Copying txs_pruned
2023-12-20 19:42:05.554 I LMDB Mapsize increased.  Old: 3585MiB, New: 4098MiB
2023-12-20 19:53:06.670 I LMDB Mapsize increased.  Old: 4098MiB, New: 4610MiB
2023-12-20 20:05:05.176 I LMDB Mapsize increased.  Old: 4610MiB, New: 5123MiB
2023-12-20 20:18:35.796 I LMDB Mapsize increased.  Old: 5123MiB, New: 5636MiB
2023-12-20 20:32:38.086 I LMDB Mapsize increased.  Old: 5636MiB, New: 6148MiB
2023-12-20 20:46:59.214 I LMDB Mapsize increased.  Old: 6148MiB, New: 6660MiB
2023-12-20 21:04:02.733 I LMDB Mapsize increased.  Old: 6660MiB, New: 7172MiB
2023-12-20 21:21:55.012 I LMDB Mapsize increased.  Old: 7172MiB, New: 7684MiB
2023-12-20 21:39:03.485 I LMDB Mapsize increased.  Old: 7684MiB, New: 8197MiB
2023-12-20 21:55:33.367 I LMDB Mapsize increased.  Old: 8197MiB, New: 8709MiB
2023-12-20 22:11:59.276 I LMDB Mapsize increased.  Old: 8709MiB, New: 9221MiB
2023-12-20 22:27:56.201 I LMDB Mapsize increased.  Old: 9221MiB, New: 9734MiB
2023-12-20 22:44:01.175 I LMDB Mapsize increased.  Old: 9734MiB, New: 10246MiB
2023-12-20 22:59:50.662 I LMDB Mapsize increased.  Old: 10246MiB, New: 10759MiB
2023-12-20 23:15:39.095 I LMDB Mapsize increased.  Old: 10759MiB, New: 11271MiB
2023-12-20 23:31:12.265 I LMDB Mapsize increased.  Old: 11271MiB, New: 11783MiB
2023-12-20 23:46:28.582 I LMDB Mapsize increased.  Old: 11783MiB, New: 12295MiB
2023-12-21 00:02:26.300 I LMDB Mapsize increased.  Old: 12295MiB, New: 12808MiB
2023-12-21 00:18:07.745 I LMDB Mapsize increased.  Old: 12808MiB, New: 13320MiB
2023-12-21 00:33:15.715 I LMDB Mapsize increased.  Old: 13320MiB, New: 13832MiB
2023-12-21 00:48:36.166 I LMDB Mapsize increased.  Old: 13832MiB, New: 14344MiB
2023-12-21 01:04:42.586 I LMDB Mapsize increased.  Old: 14344MiB, New: 14856MiB
2023-12-21 01:20:53.668 I LMDB Mapsize increased.  Old: 14856MiB, New: 15369MiB
2023-12-21 01:36:56.742 I LMDB Mapsize increased.  Old: 15369MiB, New: 15881MiB
2023-12-21 01:52:42.995 I LMDB Mapsize increased.  Old: 15881MiB, New: 16393MiB
2023-12-21 02:08:42.747 I LMDB Mapsize increased.  Old: 16393MiB, New: 16905MiB
2023-12-21 02:24:40.641 I LMDB Mapsize increased.  Old: 16905MiB, New: 17417MiB
2023-12-21 02:40:29.754 I LMDB Mapsize increased.  Old: 17417MiB, New: 17929MiB
2023-12-21 02:56:32.155 I LMDB Mapsize increased.  Old: 17929MiB, New: 18441MiB
2023-12-21 03:11:14.078 I LMDB Mapsize increased.  Old: 18441MiB, New: 18953MiB
2023-12-21 03:18:02.363 I LMDB Mapsize increased.  Old: 18953MiB, New: 19466MiB
2023-12-21 03:34:16.075 I LMDB Mapsize increased.  Old: 19466MiB, New: 19978MiB
2023-12-21 03:50:25.705 I LMDB Mapsize increased.  Old: 19978MiB, New: 20490MiB
2023-12-21 04:06:38.374 I LMDB Mapsize increased.  Old: 20490MiB, New: 21002MiB
2023-12-21 04:22:55.678 I LMDB Mapsize increased.  Old: 21002MiB, New: 21514MiB
2023-12-21 04:40:48.210 I LMDB Mapsize increased.  Old: 21514MiB, New: 22027MiB
2023-12-21 04:42:19.347 I Copying txs_prunable_hash
2023-12-21 05:01:08.310 I LMDB Mapsize increased.  Old: 22027MiB, New: 22539MiB
2023-12-21 05:20:41.597 I LMDB Mapsize increased.  Old: 22539MiB, New: 23051MiB
2023-12-21 05:40:51.916 I LMDB Mapsize increased.  Old: 23051MiB, New: 23563MiB
2023-12-21 05:50:42.689 I Copying tx_indices
2023-12-21 06:01:44.849 I LMDB Mapsize increased.  Old: 23563MiB, New: 24075MiB
2023-12-21 06:21:57.749 I LMDB Mapsize increased.  Old: 24075MiB, New: 24587MiB
2023-12-21 06:42:12.985 I LMDB Mapsize increased.  Old: 24587MiB, New: 25099MiB
2023-12-21 07:02:25.190 I LMDB Mapsize increased.  Old: 25099MiB, New: 25611MiB
2023-12-21 07:22:36.673 I LMDB Mapsize increased.  Old: 25611MiB, New: 26123MiB
2023-12-21 07:42:09.976 I LMDB Mapsize increased.  Old: 26123MiB, New: 26635MiB
2023-12-21 08:01:58.976 I LMDB Mapsize increased.  Old: 26635MiB, New: 27147MiB
2023-12-21 08:22:10.481 I LMDB Mapsize increased.  Old: 27147MiB, New: 27659MiB
2023-12-21 08:34:23.332 I Copying tx_outputs
2023-12-21 08:40:41.778 I LMDB Mapsize increased.  Old: 27659MiB, New: 28171MiB
2023-12-21 09:00:48.670 I LMDB Mapsize increased.  Old: 28171MiB, New: 28683MiB
2023-12-21 09:21:05.658 I LMDB Mapsize increased.  Old: 28683MiB, New: 29195MiB
2023-12-21 09:32:55.079 I Copying output_txs
2023-12-21 09:37:12.644 I LMDB Mapsize increased.  Old: 29195MiB, New: 29707MiB
2023-12-21 09:52:38.582 I LMDB Mapsize increased.  Old: 29707MiB, New: 30219MiB
2023-12-21 10:10:35.962 I LMDB Mapsize increased.  Old: 30219MiB, New: 30731MiB
2023-12-21 10:30:59.190 I LMDB Mapsize increased.  Old: 30731MiB, New: 31243MiB
2023-12-21 10:49:52.248 I LMDB Mapsize increased.  Old: 31243MiB, New: 31755MiB
2023-12-21 11:08:26.427 I LMDB Mapsize increased.  Old: 31755MiB, New: 32268MiB
2023-12-21 11:27:30.449 I LMDB Mapsize increased.  Old: 32268MiB, New: 32780MiB
2023-12-21 11:46:29.177 I LMDB Mapsize increased.  Old: 32780MiB, New: 33292MiB
2023-12-21 12:05:53.486 I LMDB Mapsize increased.  Old: 33292MiB, New: 33804MiB
2023-12-21 12:25:21.597 I LMDB Mapsize increased.  Old: 33804MiB, New: 34316MiB
2023-12-21 12:33:18.261 I Copying output_amounts
2023-12-21 12:45:10.456 I LMDB Mapsize increased.  Old: 34316MiB, New: 34828MiB
2023-12-21 13:05:36.502 I LMDB Mapsize increased.  Old: 34828MiB, New: 35340MiB
2023-12-21 13:23:44.624 I LMDB Mapsize increased.  Old: 35340MiB, New: 35852MiB
2023-12-21 13:41:31.410 I LMDB Mapsize increased.  Old: 35852MiB, New: 36364MiB
2023-12-21 13:58:57.329 I LMDB Mapsize increased.  Old: 36364MiB, New: 36876MiB
2023-12-21 14:16:12.644 I LMDB Mapsize increased.  Old: 36876MiB, New: 37388MiB
2023-12-21 14:33:33.424 I LMDB Mapsize increased.  Old: 37388MiB, New: 37900MiB
2023-12-21 14:50:53.402 I LMDB Mapsize increased.  Old: 37900MiB, New: 38412MiB
2023-12-21 15:08:21.884 I LMDB Mapsize increased.  Old: 38412MiB, New: 38924MiB
2023-12-21 15:25:58.135 I LMDB Mapsize increased.  Old: 38924MiB, New: 39436MiB
2023-12-21 15:43:32.744 I LMDB Mapsize increased.  Old: 39436MiB, New: 39948MiB
2023-12-21 16:01:13.736 I LMDB Mapsize increased.  Old: 39948MiB, New: 40461MiB
2023-12-21 16:19:11.262 I LMDB Mapsize increased.  Old: 40461MiB, New: 40973MiB
2023-12-21 16:37:11.792 I LMDB Mapsize increased.  Old: 40973MiB, New: 41485MiB
2023-12-21 16:55:20.038 I LMDB Mapsize increased.  Old: 41485MiB, New: 41997MiB
2023-12-21 17:13:53.476 I LMDB Mapsize increased.  Old: 41997MiB, New: 42509MiB
2023-12-21 17:34:14.318 I LMDB Mapsize increased.  Old: 42509MiB, New: 43021MiB
2023-12-21 17:53:01.956 I LMDB Mapsize increased.  Old: 43021MiB, New: 43533MiB
2023-12-21 18:10:37.544 I LMDB Mapsize increased.  Old: 43533MiB, New: 44045MiB
2023-12-21 18:14:54.418 I Copying spent_keys
2023-12-21 18:31:00.480 I LMDB Mapsize increased.  Old: 44045MiB, New: 44557MiB
2023-12-21 18:52:07.552 I LMDB Mapsize increased.  Old: 44557MiB, New: 45069MiB
2023-12-21 19:13:09.776 I LMDB Mapsize increased.  Old: 45069MiB, New: 45581MiB
2023-12-21 19:34:12.144 I LMDB Mapsize increased.  Old: 45581MiB, New: 46093MiB
2023-12-21 19:55:16.605 I LMDB Mapsize increased.  Old: 46093MiB, New: 46605MiB
2023-12-21 20:16:08.452 I LMDB Mapsize increased.  Old: 46605MiB, New: 47117MiB
2023-12-21 20:37:40.676 I LMDB Mapsize increased.  Old: 47117MiB, New: 47629MiB
2023-12-21 20:59:00.978 I LMDB Mapsize increased.  Old: 47629MiB, New: 48141MiB
2023-12-21 21:20:07.195 I LMDB Mapsize increased.  Old: 48141MiB, New: 48653MiB
2023-12-21 21:40:54.823 I LMDB Mapsize increased.  Old: 48653MiB, New: 49165MiB
2023-12-21 22:01:46.637 I LMDB Mapsize increased.  Old: 49165MiB, New: 49677MiB
2023-12-21 22:11:28.891 I Copying txpool_meta
2023-12-21 22:11:29.001 I Copying txpool_blob
2023-12-21 22:11:29.509 I Copying hf_versions
2023-12-21 22:13:42.962 I Copying properties
2023-12-21 22:13:42.976 I Copying txs_prunable
2023-12-21 22:15:26.431 I LMDB Mapsize increased.  Old: 49677MiB, New: 50190MiB
2023-12-21 22:23:43.046 I LMDB Mapsize increased.  Old: 50190MiB, New: 50703MiB
2023-12-21 22:32:26.300 I LMDB Mapsize increased.  Old: 50703MiB, New: 51215MiB
2023-12-21 22:38:56.832 I LMDB Mapsize increased.  Old: 51215MiB, New: 51728MiB
2023-12-21 22:45:20.718 I LMDB Mapsize increased.  Old: 51728MiB, New: 52243MiB
2023-12-21 22:52:00.001 I LMDB Mapsize increased.  Old: 52243MiB, New: 52761MiB
2023-12-21 22:52:54.281 I LMDB Mapsize increased.  Old: 52761MiB, New: 53279MiB
2023-12-21 22:53:18.647 I LMDB Mapsize increased.  Old: 53279MiB, New: 53793MiB
2023-12-21 22:53:39.152 I LMDB Mapsize increased.  Old: 53793MiB, New: 54308MiB
2023-12-21 22:53:58.006 I LMDB Mapsize increased.  Old: 54308MiB, New: 54833MiB
2023-12-21 22:54:17.635 I LMDB Mapsize increased.  Old: 54833MiB, New: 55350MiB
2023-12-21 22:54:37.686 I LMDB Mapsize increased.  Old: 55350MiB, New: 55871MiB
2023-12-21 22:54:58.713 I LMDB Mapsize increased.  Old: 55871MiB, New: 56390MiB
2023-12-21 22:55:18.354 I LMDB Mapsize increased.  Old: 56390MiB, New: 56905MiB
2023-12-21 22:55:36.927 I LMDB Mapsize increased.  Old: 56905MiB, New: 57422MiB
2023-12-21 22:55:54.496 I LMDB Mapsize increased.  Old: 57422MiB, New: 57934MiB
2023-12-21 22:56:14.389 I LMDB Mapsize increased.  Old: 57934MiB, New: 58452MiB
2023-12-21 22:56:34.222 I LMDB Mapsize increased.  Old: 58452MiB, New: 58969MiB
2023-12-21 22:56:55.162 I LMDB Mapsize increased.  Old: 58969MiB, New: 59491MiB
2023-12-21 22:57:18.105 I LMDB Mapsize increased.  Old: 59491MiB, New: 60018MiB
2023-12-21 22:57:40.352 I LMDB Mapsize increased.  Old: 60018MiB, New: 60576MiB
2023-12-21 22:57:59.666 I LMDB Mapsize increased.  Old: 60576MiB, New: 61105MiB
2023-12-21 22:58:19.258 I LMDB Mapsize increased.  Old: 61105MiB, New: 61621MiB
2023-12-21 22:58:38.401 I LMDB Mapsize increased.  Old: 61621MiB, New: 62142MiB
2023-12-21 22:58:57.515 I LMDB Mapsize increased.  Old: 62142MiB, New: 62662MiB
2023-12-21 22:59:15.947 I LMDB Mapsize increased.  Old: 62662MiB, New: 63184MiB
2023-12-21 22:59:33.688 I LMDB Mapsize increased.  Old: 63184MiB, New: 63697MiB
2023-12-21 22:59:51.741 I LMDB Mapsize increased.  Old: 63697MiB, New: 64224MiB
2023-12-21 23:00:09.906 I LMDB Mapsize increased.  Old: 64224MiB, New: 64741MiB
2023-12-21 23:00:26.879 I LMDB Mapsize increased.  Old: 64741MiB, New: 65266MiB
2023-12-21 23:00:45.683 I LMDB Mapsize increased.  Old: 65266MiB, New: 65815MiB
2023-12-21 23:01:02.484 I LMDB Mapsize increased.  Old: 65815MiB, New: 66337MiB
2023-12-21 23:01:20.056 I LMDB Mapsize increased.  Old: 66337MiB, New: 66865MiB
2023-12-21 23:01:36.735 I LMDB Mapsize increased.  Old: 66865MiB, New: 67411MiB
2023-12-21 23:01:54.510 I LMDB Mapsize increased.  Old: 67411MiB, New: 67924MiB
2023-12-21 23:02:11.575 I LMDB Mapsize increased.  Old: 67924MiB, New: 68443MiB
2023-12-21 23:02:30.317 I LMDB Mapsize increased.  Old: 68443MiB, New: 68958MiB
2023-12-21 23:02:49.160 I LMDB Mapsize increased.  Old: 68958MiB, New: 69481MiB
2023-12-21 23:03:07.154 I LMDB Mapsize increased.  Old: 69481MiB, New: 69996MiB
2023-12-21 23:03:25.547 I LMDB Mapsize increased.  Old: 69996MiB, New: 70519MiB
2023-12-21 23:03:46.229 I LMDB Mapsize increased.  Old: 70519MiB, New: 71040MiB
2023-12-21 23:04:05.505 I LMDB Mapsize increased.  Old: 71040MiB, New: 71562MiB
2023-12-21 23:04:24.359 I LMDB Mapsize increased.  Old: 71562MiB, New: 72077MiB
2023-12-21 23:04:43.426 I LMDB Mapsize increased.  Old: 72077MiB, New: 72593MiB
2023-12-21 23:05:02.250 I LMDB Mapsize increased.  Old: 72593MiB, New: 73112MiB
2023-12-21 23:05:21.204 I LMDB Mapsize increased.  Old: 73112MiB, New: 73639MiB
2023-12-21 23:05:39.436 I LMDB Mapsize increased.  Old: 73639MiB, New: 74155MiB
2023-12-21 23:05:58.609 I LMDB Mapsize increased.  Old: 74155MiB, New: 74673MiB
2023-12-21 23:06:16.790 I LMDB Mapsize increased.  Old: 74673MiB, New: 75187MiB
2023-12-21 23:06:36.054 I LMDB Mapsize increased.  Old: 75187MiB, New: 75706MiB
2023-12-21 23:06:54.804 I LMDB Mapsize increased.  Old: 75706MiB, New: 76229MiB
2023-12-21 23:07:13.624 I LMDB Mapsize increased.  Old: 76229MiB, New: 76751MiB
2023-12-21 23:07:33.410 I LMDB Mapsize increased.  Old: 76751MiB, New: 77280MiB
2023-12-21 23:07:52.753 I LMDB Mapsize increased.  Old: 77280MiB, New: 77803MiB
2023-12-21 23:08:10.685 I LMDB Mapsize increased.  Old: 77803MiB, New: 78324MiB
2023-12-21 23:08:28.792 I LMDB Mapsize increased.  Old: 78324MiB, New: 78838MiB
2023-12-21 23:08:48.041 I LMDB Mapsize increased.  Old: 78838MiB, New: 79359MiB
2023-12-21 23:09:08.615 I LMDB Mapsize increased.  Old: 79359MiB, New: 79880MiB
2023-12-21 23:09:28.030 I LMDB Mapsize increased.  Old: 79880MiB, New: 80397MiB
2023-12-21 23:09:47.243 I LMDB Mapsize increased.  Old: 80397MiB, New: 80927MiB
2023-12-21 23:10:06.465 I LMDB Mapsize increased.  Old: 80927MiB, New: 81444MiB
2023-12-21 23:10:25.815 I LMDB Mapsize increased.  Old: 81444MiB, New: 81961MiB
2023-12-21 23:10:45.408 I LMDB Mapsize increased.  Old: 81961MiB, New: 82483MiB
2023-12-21 23:11:04.375 I LMDB Mapsize increased.  Old: 82483MiB, New: 83001MiB
2023-12-21 23:11:22.821 I LMDB Mapsize increased.  Old: 83001MiB, New: 83526MiB
2023-12-21 23:11:42.397 I LMDB Mapsize increased.  Old: 83526MiB, New: 84046MiB
2023-12-21 23:12:03.039 I LMDB Mapsize increased.  Old: 84046MiB, New: 84569MiB
2023-12-21 23:12:22.022 I LMDB Mapsize increased.  Old: 84569MiB, New: 85090MiB
2023-12-21 23:12:42.948 I LMDB Mapsize increased.  Old: 85090MiB, New: 85606MiB
2023-12-21 23:13:01.590 I LMDB Mapsize increased.  Old: 85606MiB, New: 86119MiB
2023-12-21 23:13:20.941 I LMDB Mapsize increased.  Old: 86119MiB, New: 86638MiB
2023-12-21 23:13:39.474 I LMDB Mapsize increased.  Old: 86638MiB, New: 87161MiB
2023-12-21 23:13:59.286 I LMDB Mapsize increased.  Old: 87161MiB, New: 87683MiB
2023-12-21 23:14:18.982 I LMDB Mapsize increased.  Old: 87683MiB, New: 88209MiB
2023-12-21 23:14:37.976 I LMDB Mapsize increased.  Old: 88209MiB, New: 88731MiB
2023-12-21 23:14:57.802 I LMDB Mapsize increased.  Old: 88731MiB, New: 89246MiB
2023-12-21 23:15:16.912 I LMDB Mapsize increased.  Old: 89246MiB, New: 89770MiB
2023-12-21 23:15:36.689 I LMDB Mapsize increased.  Old: 89770MiB, New: 90290MiB
2023-12-21 23:16:00.701 I LMDB Mapsize increased.  Old: 90290MiB, New: 90816MiB
2023-12-21 23:16:20.527 I LMDB Mapsize increased.  Old: 90816MiB, New: 91338MiB
2023-12-21 23:16:41.805 I LMDB Mapsize increased.  Old: 91338MiB, New: 91855MiB
2023-12-21 23:17:02.076 I LMDB Mapsize increased.  Old: 91855MiB, New: 92373MiB
2023-12-21 23:17:22.377 I LMDB Mapsize increased.  Old: 92373MiB, New: 92895MiB
2023-12-21 23:17:43.358 I LMDB Mapsize increased.  Old: 92895MiB, New: 93411MiB
2023-12-21 23:18:02.966 I LMDB Mapsize increased.  Old: 93411MiB, New: 93929MiB
2023-12-21 23:18:23.233 I LMDB Mapsize increased.  Old: 93929MiB, New: 94445MiB
2023-12-21 23:18:41.833 I LMDB Mapsize increased.  Old: 94445MiB, New: 94960MiB
2023-12-21 23:19:03.137 I LMDB Mapsize increased.  Old: 94960MiB, New: 95484MiB
2023-12-21 23:19:25.277 I LMDB Mapsize increased.  Old: 95484MiB, New: 95997MiB
2023-12-21 23:19:46.347 I LMDB Mapsize increased.  Old: 95997MiB, New: 96512MiB
2023-12-21 23:20:06.951 I LMDB Mapsize increased.  Old: 96512MiB, New: 97027MiB
2023-12-21 23:20:27.595 I LMDB Mapsize increased.  Old: 97027MiB, New: 97541MiB
2023-12-21 23:20:49.640 I LMDB Mapsize increased.  Old: 97541MiB, New: 98058MiB
2023-12-21 23:21:09.469 I LMDB Mapsize increased.  Old: 98058MiB, New: 98575MiB
2023-12-21 23:21:28.428 I LMDB Mapsize increased.  Old: 98575MiB, New: 99089MiB
2023-12-21 23:21:48.559 I LMDB Mapsize increased.  Old: 99089MiB, New: 99604MiB
2023-12-21 23:22:07.885 I LMDB Mapsize increased.  Old: 99604MiB, New: 100122MiB
2023-12-21 23:22:28.375 I LMDB Mapsize increased.  Old: 100122MiB, New: 100648MiB
2023-12-21 23:22:49.222 I LMDB Mapsize increased.  Old: 100648MiB, New: 101166MiB
2023-12-21 23:23:10.526 I LMDB Mapsize increased.  Old: 101166MiB, New: 101687MiB
2023-12-21 23:23:30.907 I LMDB Mapsize increased.  Old: 101687MiB, New: 102202MiB
2023-12-21 23:23:52.777 I LMDB Mapsize increased.  Old: 102202MiB, New: 102728MiB
2023-12-21 23:24:14.552 I LMDB Mapsize increased.  Old: 102728MiB, New: 103246MiB
2023-12-21 23:24:35.120 I LMDB Mapsize increased.  Old: 103246MiB, New: 103769MiB
2023-12-21 23:24:55.191 I LMDB Mapsize increased.  Old: 103769MiB, New: 104285MiB
2023-12-21 23:25:15.524 I LMDB Mapsize increased.  Old: 104285MiB, New: 104809MiB
2023-12-21 23:34:20.898 I LMDB Mapsize increased.  Old: 104809MiB, New: 105331MiB
2023-12-21 23:45:20.104 I LMDB Mapsize increased.  Old: 105331MiB, New: 105845MiB
2023-12-21 23:58:39.662 I LMDB Mapsize increased.  Old: 105845MiB, New: 106358MiB
2023-12-22 00:11:33.557 I LMDB Mapsize increased.  Old: 106358MiB, New: 106871MiB
2023-12-22 00:24:23.187 I LMDB Mapsize increased.  Old: 106871MiB, New: 107385MiB
2023-12-22 00:36:28.964 I LMDB Mapsize increased.  Old: 107385MiB, New: 107900MiB
2023-12-22 00:49:01.446 I LMDB Mapsize increased.  Old: 107900MiB, New: 108414MiB
2023-12-22 01:01:53.324 I LMDB Mapsize increased.  Old: 108414MiB, New: 108926MiB
2023-12-22 01:14:34.966 I LMDB Mapsize increased.  Old: 108926MiB, New: 109441MiB
2023-12-22 01:26:50.912 I LMDB Mapsize increased.  Old: 109441MiB, New: 109956MiB
2023-12-22 01:39:19.718 I LMDB Mapsize increased.  Old: 109956MiB, New: 110471MiB
2023-12-22 01:51:48.180 I LMDB Mapsize increased.  Old: 110471MiB, New: 110983MiB
2023-12-22 02:03:56.485 I LMDB Mapsize increased.  Old: 110983MiB, New: 111499MiB
2023-12-22 02:16:51.692 I LMDB Mapsize increased.  Old: 111499MiB, New: 112011MiB
2023-12-22 02:30:02.063 I LMDB Mapsize increased.  Old: 112011MiB, New: 112524MiB
2023-12-22 02:43:08.685 I LMDB Mapsize increased.  Old: 112524MiB, New: 113037MiB
2023-12-22 02:56:10.212 I LMDB Mapsize increased.  Old: 113037MiB, New: 113551MiB
2023-12-22 03:08:27.517 I LMDB Mapsize increased.  Old: 113551MiB, New: 114065MiB
2023-12-22 03:21:16.605 I LMDB Mapsize increased.  Old: 114065MiB, New: 114579MiB
2023-12-22 03:33:43.255 I LMDB Mapsize increased.  Old: 114579MiB, New: 115093MiB
2023-12-22 03:47:02.159 I LMDB Mapsize increased.  Old: 115093MiB, New: 115605MiB
2023-12-22 03:59:31.730 I LMDB Mapsize increased.  Old: 115605MiB, New: 116118MiB
2023-12-22 04:11:59.513 I LMDB Mapsize increased.  Old: 116118MiB, New: 116631MiB
2023-12-22 04:24:26.397 I LMDB Mapsize increased.  Old: 116631MiB, New: 117144MiB
2023-12-22 04:36:48.047 I LMDB Mapsize increased.  Old: 117144MiB, New: 117657MiB
2023-12-22 04:49:12.118 I LMDB Mapsize increased.  Old: 117657MiB, New: 118171MiB
2023-12-22 05:01:36.408 I LMDB Mapsize increased.  Old: 118171MiB, New: 118687MiB
2023-12-22 05:13:57.394 I LMDB Mapsize increased.  Old: 118687MiB, New: 119201MiB
2023-12-22 05:26:21.825 I LMDB Mapsize increased.  Old: 119201MiB, New: 119716MiB
2023-12-22 05:38:44.583 I LMDB Mapsize increased.  Old: 119716MiB, New: 120228MiB
2023-12-22 05:50:51.464 I LMDB Mapsize increased.  Old: 120228MiB, New: 120741MiB
2023-12-22 06:02:48.984 I LMDB Mapsize increased.  Old: 120741MiB, New: 121254MiB
2023-12-22 06:14:59.445 I LMDB Mapsize increased.  Old: 121254MiB, New: 121767MiB
2023-12-22 06:27:03.189 I LMDB Mapsize increased.  Old: 121767MiB, New: 122282MiB
2023-12-22 06:38:52.583 I LMDB Mapsize increased.  Old: 122282MiB, New: 122794MiB
2023-12-22 06:51:13.623 I LMDB Mapsize increased.  Old: 122794MiB, New: 123310MiB
2023-12-22 07:02:30.964 I LMDB Mapsize increased.  Old: 123310MiB, New: 123822MiB
2023-12-22 07:14:42.849 I LMDB Mapsize increased.  Old: 123822MiB, New: 124336MiB
2023-12-22 07:26:42.290 I LMDB Mapsize increased.  Old: 124336MiB, New: 124850MiB
2023-12-22 07:38:56.964 I LMDB Mapsize increased.  Old: 124850MiB, New: 125363MiB
2023-12-22 07:51:41.135 I LMDB Mapsize increased.  Old: 125363MiB, New: 125875MiB
2023-12-22 08:04:48.985 I LMDB Mapsize increased.  Old: 125875MiB, New: 126388MiB
2023-12-22 08:18:19.129 I LMDB Mapsize increased.  Old: 126388MiB, New: 126902MiB
2023-12-22 08:31:56.626 I LMDB Mapsize increased.  Old: 126902MiB, New: 127415MiB
2023-12-22 08:45:04.373 I LMDB Mapsize increased.  Old: 127415MiB, New: 127927MiB
2023-12-22 08:58:29.322 I LMDB Mapsize increased.  Old: 127927MiB, New: 128441MiB
2023-12-22 09:12:09.221 I LMDB Mapsize increased.  Old: 128441MiB, New: 128953MiB
2023-12-22 09:25:14.354 I LMDB Mapsize increased.  Old: 128953MiB, New: 129466MiB
2023-12-22 09:38:29.362 I LMDB Mapsize increased.  Old: 129466MiB, New: 129980MiB
2023-12-22 09:51:56.804 I LMDB Mapsize increased.  Old: 129980MiB, New: 130493MiB
2023-12-22 10:04:43.633 I LMDB Mapsize increased.  Old: 130493MiB, New: 131006MiB
2023-12-22 10:17:46.578 I LMDB Mapsize increased.  Old: 131006MiB, New: 131520MiB
2023-12-22 10:30:56.177 I LMDB Mapsize increased.  Old: 131520MiB, New: 132032MiB
2023-12-22 10:44:17.589 I LMDB Mapsize increased.  Old: 132032MiB, New: 132544MiB
2023-12-22 10:57:33.159 I LMDB Mapsize increased.  Old: 132544MiB, New: 133057MiB
2023-12-22 11:09:46.237 I LMDB Mapsize increased.  Old: 133057MiB, New: 133571MiB
2023-12-22 11:23:39.457 I LMDB Mapsize increased.  Old: 133571MiB, New: 134085MiB
2023-12-22 11:37:34.618 I LMDB Mapsize increased.  Old: 134085MiB, New: 134597MiB
2023-12-22 11:51:35.203 I LMDB Mapsize increased.  Old: 134597MiB, New: 135110MiB
2023-12-22 12:05:29.194 I LMDB Mapsize increased.  Old: 135110MiB, New: 135623MiB
2023-12-22 12:19:38.956 I LMDB Mapsize increased.  Old: 135623MiB, New: 136136MiB
2023-12-22 12:33:27.091 I LMDB Mapsize increased.  Old: 136136MiB, New: 136649MiB
2023-12-22 12:46:44.304 I LMDB Mapsize increased.  Old: 136649MiB, New: 137162MiB
2023-12-22 12:59:52.500 I LMDB Mapsize increased.  Old: 137162MiB, New: 137674MiB
2023-12-22 13:12:54.020 I LMDB Mapsize increased.  Old: 137674MiB, New: 138186MiB
2023-12-22 13:26:43.133 I LMDB Mapsize increased.  Old: 138186MiB, New: 138699MiB
2023-12-22 13:39:33.423 I LMDB Mapsize increased.  Old: 138699MiB, New: 139214MiB
2023-12-22 13:52:57.108 I LMDB Mapsize increased.  Old: 139214MiB, New: 139727MiB
2023-12-22 14:04:51.695 I LMDB Mapsize increased.  Old: 139727MiB, New: 140245MiB
2023-12-22 14:18:28.577 I LMDB Mapsize increased.  Old: 140245MiB, New: 140757MiB
2023-12-22 14:31:54.699 I LMDB Mapsize increased.  Old: 140757MiB, New: 141271MiB
2023-12-22 14:45:10.299 I LMDB Mapsize increased.  Old: 141271MiB, New: 141784MiB
2023-12-22 14:58:31.002 I LMDB Mapsize increased.  Old: 141784MiB, New: 142297MiB
2023-12-22 15:11:47.977 I LMDB Mapsize increased.  Old: 142297MiB, New: 142811MiB
2023-12-22 15:25:21.769 I LMDB Mapsize increased.  Old: 142811MiB, New: 143324MiB
2023-12-22 15:39:06.604 I LMDB Mapsize increased.  Old: 143324MiB, New: 143837MiB
2023-12-22 15:52:53.616 I LMDB Mapsize increased.  Old: 143837MiB, New: 144351MiB
2023-12-22 16:06:16.018 I LMDB Mapsize increased.  Old: 144351MiB, New: 144863MiB
2023-12-22 16:19:46.399 I LMDB Mapsize increased.  Old: 144863MiB, New: 145377MiB
2023-12-22 16:33:21.350 I LMDB Mapsize increased.  Old: 145377MiB, New: 145891MiB
2023-12-22 16:47:07.360 I LMDB Mapsize increased.  Old: 145891MiB, New: 146403MiB
2023-12-22 17:00:34.819 I LMDB Mapsize increased.  Old: 146403MiB, New: 146916MiB
2023-12-22 17:14:18.850 I LMDB Mapsize increased.  Old: 146916MiB, New: 147429MiB
2023-12-22 17:27:56.750 I LMDB Mapsize increased.  Old: 147429MiB, New: 147943MiB
2023-12-22 17:41:45.372 I LMDB Mapsize increased.  Old: 147943MiB, New: 148456MiB
2023-12-22 17:55:12.076 I LMDB Mapsize increased.  Old: 148456MiB, New: 148969MiB
2023-12-22 18:08:49.258 I LMDB Mapsize increased.  Old: 148969MiB, New: 149481MiB
2023-12-22 18:22:34.994 I LMDB Mapsize increased.  Old: 149481MiB, New: 150003MiB
2023-12-22 18:36:35.453 I LMDB Mapsize increased.  Old: 150003MiB, New: 150517MiB
2023-12-22 18:50:35.388 I LMDB Mapsize increased.  Old: 150517MiB, New: 151030MiB
2023-12-22 19:04:47.179 I LMDB Mapsize increased.  Old: 151030MiB, New: 151543MiB
2023-12-22 19:18:36.428 I LMDB Mapsize increased.  Old: 151543MiB, New: 152055MiB
2023-12-22 19:32:12.027 I LMDB Mapsize increased.  Old: 152055MiB, New: 152568MiB
2023-12-22 19:45:28.429 I LMDB Mapsize increased.  Old: 152568MiB, New: 153082MiB
2023-12-22 19:59:05.007 I LMDB Mapsize increased.  Old: 153082MiB, New: 153595MiB
2023-12-22 20:12:30.771 I LMDB Mapsize increased.  Old: 153595MiB, New: 154107MiB
2023-12-22 20:26:46.876 I LMDB Mapsize increased.  Old: 154107MiB, New: 154621MiB
2023-12-22 20:40:29.441 I LMDB Mapsize increased.  Old: 154621MiB, New: 155133MiB
2023-12-22 20:53:49.252 I LMDB Mapsize increased.  Old: 155133MiB, New: 155645MiB
2023-12-22 21:06:55.936 I LMDB Mapsize increased.  Old: 155645MiB, New: 156159MiB
2023-12-22 21:20:07.165 I LMDB Mapsize increased.  Old: 156159MiB, New: 156671MiB
2023-12-22 21:33:09.140 I LMDB Mapsize increased.  Old: 156671MiB, New: 157185MiB
2023-12-22 21:46:32.477 I LMDB Mapsize increased.  Old: 157185MiB, New: 157699MiB
2023-12-22 21:59:55.946 I LMDB Mapsize increased.  Old: 157699MiB, New: 158211MiB
2023-12-22 22:13:07.074 I LMDB Mapsize increased.  Old: 158211MiB, New: 158724MiB
2023-12-22 22:26:14.997 I LMDB Mapsize increased.  Old: 158724MiB, New: 159236MiB
2023-12-22 22:38:53.479 I LMDB Mapsize increased.  Old: 159236MiB, New: 159750MiB
2023-12-22 22:52:06.900 I LMDB Mapsize increased.  Old: 159750MiB, New: 160263MiB
2023-12-22 23:05:09.427 I LMDB Mapsize increased.  Old: 160263MiB, New: 160776MiB
2023-12-22 23:17:30.355 I LMDB Mapsize increased.  Old: 160776MiB, New: 161289MiB
2023-12-22 23:29:54.583 I LMDB Mapsize increased.  Old: 161289MiB, New: 161802MiB
2023-12-22 23:42:44.547 I LMDB Mapsize increased.  Old: 161802MiB, New: 162315MiB
2023-12-22 23:55:42.216 I LMDB Mapsize increased.  Old: 162315MiB, New: 162827MiB
2023-12-23 00:08:59.015 I LMDB Mapsize increased.  Old: 162827MiB, New: 163339MiB
2023-12-23 00:21:59.126 I LMDB Mapsize increased.  Old: 163339MiB, New: 163853MiB
2023-12-23 00:35:10.867 I LMDB Mapsize increased.  Old: 163853MiB, New: 164365MiB
2023-12-23 00:47:53.023 I LMDB Mapsize increased.  Old: 164365MiB, New: 164877MiB
2023-12-23 01:00:24.573 I LMDB Mapsize increased.  Old: 164877MiB, New: 165391MiB
2023-12-23 01:13:25.057 I LMDB Mapsize increased.  Old: 165391MiB, New: 165908MiB
2023-12-23 01:26:55.730 I LMDB Mapsize increased.  Old: 165908MiB, New: 166420MiB
2023-12-23 01:40:12.246 I LMDB Mapsize increased.  Old: 166420MiB, New: 166933MiB
2023-12-23 01:52:59.023 I LMDB Mapsize increased.  Old: 166933MiB, New: 167445MiB
2023-12-23 02:05:38.437 I LMDB Mapsize increased.  Old: 167445MiB, New: 167958MiB
2023-12-23 02:18:33.315 I LMDB Mapsize increased.  Old: 167958MiB, New: 168472MiB
2023-12-23 02:31:36.445 I LMDB Mapsize increased.  Old: 168472MiB, New: 168984MiB
2023-12-23 02:44:45.309 I LMDB Mapsize increased.  Old: 168984MiB, New: 169497MiB
2023-12-23 02:57:52.084 I LMDB Mapsize increased.  Old: 169497MiB, New: 170011MiB
2023-12-23 03:10:29.449 I LMDB Mapsize increased.  Old: 170011MiB, New: 170525MiB
2023-12-23 03:23:18.080 I LMDB Mapsize increased.  Old: 170525MiB, New: 171039MiB
2023-12-23 03:36:16.195 I LMDB Mapsize increased.  Old: 171039MiB, New: 171553MiB
2023-12-23 03:49:15.554 I LMDB Mapsize increased.  Old: 171553MiB, New: 172067MiB
2023-12-23 04:02:13.546 I LMDB Mapsize increased.  Old: 172067MiB, New: 172580MiB
2023-12-23 04:15:34.150 I LMDB Mapsize increased.  Old: 172580MiB, New: 173093MiB
2023-12-23 04:28:11.819 I LMDB Mapsize increased.  Old: 173093MiB, New: 173605MiB
2023-12-23 04:41:05.896 I LMDB Mapsize increased.  Old: 173605MiB, New: 174118MiB
2023-12-23 04:54:08.288 I LMDB Mapsize increased.  Old: 174118MiB, New: 174632MiB
2023-12-23 05:06:56.366 I LMDB Mapsize increased.  Old: 174632MiB, New: 175145MiB
2023-12-23 05:20:10.786 I LMDB Mapsize increased.  Old: 175145MiB, New: 175658MiB
2023-12-23 05:33:09.924 I LMDB Mapsize increased.  Old: 175658MiB, New: 176170MiB
2023-12-23 05:46:38.981 I LMDB Mapsize increased.  Old: 176170MiB, New: 176685MiB
2023-12-23 06:00:54.636 I LMDB Mapsize increased.  Old: 176685MiB, New: 177198MiB
2023-12-23 06:14:59.326 I LMDB Mapsize increased.  Old: 177198MiB, New: 177710MiB
2023-12-23 06:29:04.377 I LMDB Mapsize increased.  Old: 177710MiB, New: 178223MiB
2023-12-23 06:43:33.227 I LMDB Mapsize increased.  Old: 178223MiB, New: 178736MiB
2023-12-23 06:54:06.344 I Copying txs_prunable_tip
2023-12-23 06:54:27.311 I Swapping databases, pre-pruning blockchain will be left in F:\blockchain\bitmonero\lmdb-old and can be removed if desired
2023-12-23 06:54:27.313 I Blockchain pruned OK
```
![image](https://github.com/monero-project/monero/assets/4364856/41996f32-61b0-4725-8ed4-a88627f5e74c)
I don't believe pruning was supposed to slightly increase the size of the database.
By golly, this is the most inefficient file copier I have ever ran, taking three days to copy a 172 GB file.

P.S.
At the point where it rapidly shot past the expected size, it started using all of the available memory on Windows 10 on the file handle of the initial DB — probably a read cache/buffer.

# Discussion History
## selsta | 2023-12-23T15:05:04+00:00
What type of storage is `F:\`? HDD, SSD, ...?

## Erquint | 2023-12-23T15:21:52+00:00
My fastest old HDD. Here's a [Cross Platform Disk Test](https://github.com/maxim-saplin/CrossPlatformDiskTest) result:
![image](https://github.com/monero-project/monero/assets/4364856/da6d17f2-37ac-42ba-938a-a1ea8af49efb)
This doesn't matter. If it took three days and gave me an actually deflated pruned DB — I wouldn't complain much.

Was it supposed to copy all of the `txs_prunable`? It all looked good until that started.

## selsta | 2023-12-23T15:38:46+00:00
We have a pull request to speed up monero-blockchain-prune: https://github.com/monero-project/monero/pull/8503

Together with an SSD it should take about 1-2h, we just haven't included the code yet in the latest release version, only master branch.

HDDs have slow random read / write speeds so they will always be significantly slower than SSDs in monero.

Regarding your reported issue, the easiest way to solve it would be to re-sync from scratch with setting `--prune-blockchain` from the beginning. This issue should stay open until someone reproduces it.

## selsta | 2023-12-23T15:39:58+00:00
> So I had a node that was, as I recall, initially ran with pruning, then without, then pruned again using the Monero daemon.

Can you explain this in more detail? You can't unprune a daemon so it was always pruned, unless you deleted the blockchain in-between?

## Erquint | 2023-12-23T15:45:01+00:00
No, I didn't delete it. Just ran the daemon without the pruning option after initial DB creation in GUI wallet, where I picked the pruned option, until it gradually reached 172 GB, which seems like the size of the full ledger.
It almost sounds like another issue to be opened for `monerod` separately, but I don't have detailed statistics to illustrate it.
Unless you wanna explain to me how a supposedly pruned DB of either/both `monerod` and `monero-blockchain-prune` is 172 GB.

`monero-blockchain-prune` reported the DB created by `monerod` as pruned.
And there was some option to check if it's pruned in `monerod` itself, IIRC, which also reported it as pruned.

## Erquint | 2023-12-23T16:05:38+00:00
As for the HDD and speed… Look, the point I'm making is…
The pruned entries are already marked for rewriting/discarding.
All that I would expect of a program intended to deflate the DB, to discard those stained entries, is to simply sequentially copy the entries that aren't stained, skipping the stained ones.
How complicated could that really be?
I'd be able to copy this entire disk twice over in a matter of minutes, hours at most with the slow built-in OS copier. Not days. It's insult to injury when it copies the entries it promised to skip and then also takes an eternity to do what I never wanted it to do.

## hyc | 2023-12-23T16:07:48+00:00
> No, I didn't delete it. Just ran the daemon without the pruning option

That doesn't matter. Once you use the option, that's recorded in the DB so it will always be pruning after that point. Only deleting the blockchain DB would reset that option.

## Erquint | 2023-12-23T16:12:23+00:00
You'd think that, but 172 GB…
Refresh the page.
I edited the message you responded to with more detail.
Expected GitHub's dynamic UI to reflect my changes in real time.
Detailed it in the head post too now.

## nahuhh | 2023-12-26T14:41:40+00:00
"A" appears to be OPs case:

A) Internally Pruned
1. sync blockchain normally
= ~170gb node (expected)
2. run with `--prune-blockchain`
= The database is now pruned internally, but is still ~170gb on disk (expected) 
3. Run `monero-blockchain-prune --copy-pruned-database`
= copies the database from 2 (~170gb, expected?)

if OP did 3b (below):
3b. Run `monero-blockchain-prune` w/o the copy flag
= ~~does this shrink the db?~~ Or should this error out and say db is already pruned?
edit: op says this does indeed throw an error
Perhaps op expected this to shrink the db instead of throwing an error


This use case should work:
B) Unpruned BC
1. fully sync blockchain normally
= ~170gb node (expected)
2. Run `monero-blockchain-prune`
= prunes the database from 1 (expected)


## nahuhh | 2023-12-26T14:50:12+00:00
> Unless you wanna explain to me how a supposedly pruned DB of either/both `monerod` and `monero-blockchain-prune` is 172 GB.


pruning doesn't free already allocated space on disk. It frees space within the db and wont allocate more until the "internal" db reaches the size on disk. 

> `monero-blockchain-prune` reported the DB created by `monerod` as pruned.
> And there was some option to check if it's pruned in `monerod` itself, IIRC, which also reported it as pruned.


if you ever ran `--prune-blockchain`, it was pruned (pruned != shrunken) and monerod is reporting correctly. 

This _appears_ to be caused by usage of `--copy-pruned-database`.
~~I'm interested in if it shrinks a pruned but overallocated BC if the copy flag if dropped.~~



## selsta | 2023-12-26T14:58:24+00:00
I think this is an issue with a bugged / corrupted database, @Erquint says they initially started monerod with the `--pruned-blockchain` flag, which means it should have never gotten that big in the first place.

## Erquint | 2023-12-27T06:30:44+00:00
Correction to a thing many of you seem to misinterpret: I didn't start the DB with a pruning **flag**. The official Monero GUI Wallet offered the two choices and I **picked pruned in the GUI** when initializing. I added the flag at some later point. But as we established, if the GUI did its job — the flag should do nothing.

Admittedly, I initialized the DB a very long time ago.

@nahuhh
> Perhaps op expected this to shrink the db instead of throwing an error

It would be nice if it did what's on the tin. Can't argue there.

> Run `monero-blockchain-prune --copy-pruned-database`
  = copies the database from 2 (~170gb, expected?)

If you suppose this behavior expected, care to explain what the purpose is?
To basically replicate the function of `monerod --prune-blockchain`?
If that's the case — why didn't the `monero-blockchain-prune` complain that the DB is already pruned with the `--copy-pruned-database` flag as it did without it? This inconsistency created much confusion, without it even being clear if either both or none modes should raise that complaint.

> pruning doesn't free already allocated space

Well aware. Everything I wrote in this here entire issue is under that very assumption.
I think you missed the `monero-blockchain-prune` part of my question. That's what was supposed to shrink it. Surely, running all of the options on the table must've produced a shrunk DB file — otherwise shrinking wouldn't even be a thing we're able to discuss as an applicable concept.


Alright, so if we go with the assumption that `monero-blockchain-prune --copy-pruned-database` worked as expected, then the issue boils down to `monero-blockchain-prune` (no such flag) not working as expected, printing `Blockchain is already pruned, use --copy-pruned-database to copy it anyway` and halting.

## 123123123123123123123123123123123123one | 2025-08-30T18:21:03+00:00
> > No, I didn't delete it. Just ran the daemon without the pruning option
> 
> That doesn't matter. Once you use the option, that's recorded in the DB so it will always be pruning after that point. Only deleting the blockchain DB would reset that option.

thats stupid, so if i accidentally run monerod with prune blockchain but then immediately exit, the ENTIRE thing gets labeled as pruned?

## selsta | 2025-08-30T18:22:45+00:00
@123123123123123123123123123123123123one if your daemon starts pruning it will start deleting information, removing the flag won't magically get you back that data, you have to resync from scratch

# Action History
- Created by: Erquint | 2023-12-23T14:57:18+00:00
