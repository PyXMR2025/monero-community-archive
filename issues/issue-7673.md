---
title: View-only wallet doesn't show outgoing sweep transfers
source_url: https://github.com/monero-project/monero/issues/7673
author: ndorf
assignees: []
labels: []
created_at: '2021-04-19T18:27:29+00:00'
updated_at: '2021-04-22T20:18:33+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Given an offline (cold) wallet and an associated view-only (hot) wallet, with all outputs and key_images exported & imported, the `show_transfers` command correctly shows outgoing transactions that were made using the `transfer` command, but not those that were made using the `sweep_single` command.

The swept output still shows up as spent in `incoming_transfers`, and the output of `balance` is still correct (doesn't include the amount of the spent/swept output). 

# Discussion History
## ndorf | 2021-04-19T19:57:10+00:00
Correction: they do show up as expected in `show_transfers`, after the relevant `submit_transfer` was performed in the same wallet. They go missing if/when when the wallet is regenerated from the view key, or the `rescan_bc` command is used.

Here is a stagenet wallet that demonstrates the issue:

Address: 54e7mbbPdb5SbxSkDpzS163msDHKbTtqsB6krkWTUBui3ZV78VocotrCnATu2AJpiaFxdWNJ7M1rBF6H4WCWEK2cP97otsN
View key: c7b0484dd03dbf5ebcbc4af835d5ade6353a0f648ed90597604e04adfba7da0f
Restore height: 817248

The `show_transfers` output is correct in the original, view-only wallet which created and submitted the two outgoing transactions:

```
  817248     in unlocked       2021-04-19 18:43:32       0.990000000000 d4acb7d9d5f32bd3d8a0f1d6afac55f4e14fd132bfb67ec3a428bbbc3593a0e5 0000000000000000 0.000000000000 54e7mb:0.990000000000 0 - 
  817250     in unlocked       2021-04-19 18:45:33       0.810000000000 634ec03d9841813403d46fe8a85a29bcf037aa8e893851b5ad7b0d08a0572d04 0000000000000000 0.000000000000 54e7mb:0.810000000000 0 - 
  817252     in unlocked       2021-04-19 18:56:08       0.630000000000 f01ef29a50c793e1646903acf3539b7cd799a4de27cc3cc68a74e4020e937e75 0000000000000000 0.000000000000 72nyqL:0.630000000000 1 - 
  817260    out        -       2021-04-19 19:12:03       0.989926310000 a657ed4cb6022ba5d3996d50a62138ac07ffe6bc9b3d2a15b5b9cd152a770c6d fa6e57d45eb95096 0.000073690000 76BAgUuAfJX75Hzen3RRzP1e2EXm2sz9YhaNBGiEZiD59iwACJVg16PhUD2DmNtefbQjxoXY5vGK2VpSy2R5pWpoKf9e4q4:0.989926310000 0 - 
  817261    out        -       2021-04-19 19:19:03       0.450000000000 0ba4202455b72e2dacca24e2d738627f289b93dffba07d72591ff187e2a950be ce4c7fc509ad9377 0.000073790000 76BAgUuAfJX75Hzen3RRzP1e2EXm2sz9YhaNBGiEZiD59iwACJVg16PhUD2DmNtefbQjxoXY5vGK2VpSy2R5pWpoKf9e4q4:0.450000000000 0 - 

```

The first tx, at height 817260, was made with the `sweep_all` command and has a dummy change output. The second tx, at height 817261, was made with the `transfer` command and has a normal change output.

After this, I ran the `export_outputs all` command in this wallet, followed by `import_outputs` and `export_key_images all` in the cold wallet. The exported key images are attached: 
[issue7673.key_images.gz](https://github.com/monero-project/monero/files/6338640/issue7673.key_images.gz)

Now, a new wallet generated from the above address and viewkey, and with these key images imported, only shows the second outgoing transaction in `show_transfers` (the one made with `transfer`); the first one is missing (the one made with `sweep_all`):
```

  817248     in unlocked       2021-04-19 18:43:32       0.990000000000 d4acb7d9d5f32bd3d8a0f1d6afac55f4e14fd132bfb67ec3a428bbbc3593a0e5 0000000000000000 0.000000000000 54e7mb:0.990000000000 0 - 
  817250     in unlocked       2021-04-19 18:45:33       0.810000000000 634ec03d9841813403d46fe8a85a29bcf037aa8e893851b5ad7b0d08a0572d04 0000000000000000 0.000000000000 54e7mb:0.810000000000 0 - 
  817252     in unlocked       2021-04-19 18:56:08       0.630000000000 f01ef29a50c793e1646903acf3539b7cd799a4de27cc3cc68a74e4020e937e75 0000000000000000 0.000000000000 72nyqL:0.630000000000 1 - 
  817261    out        -       2021-04-19 19:19:03       0.450000000000 0ba4202455b72e2dacca24e2d738627f289b93dffba07d72591ff187e2a950be 0000000000000000 0.000073790000 - 0 - 
```

The same thing happens if `rescan_bc` is used in the original, previously correct wallet.


## ndorf | 2021-04-19T20:23:05+00:00
Binary wallet files attached:

1) [issue7673_good.tar.gz](https://github.com/monero-project/monero/files/6338833/issue7673_good.tar.gz), the original which shows both outgoing transfers correctly

2) [issue7673_bad_regenerated.tar.gz](https://github.com/monero-project/monero/files/6338835/issue7673_bad_regenerated.tar.gz), regenerated from view key, missing the transfer with a dummy change output

3) [issue7673_bad_rescanned.tar.gz](https://github.com/monero-project/monero/files/6338841/issue7673_bad_rescanned.tar.gz), after `rescan_bc` run on the first, good wallet; also missing the dummy-change transfer




## ndorf | 2021-04-19T22:16:33+00:00
So, I guess these transactions can't be found during scanning, because the dummy change output isn't addressed to us, and the key images aren't available yet (and can't be computed on the view-only wallet).

It seems this could only be truly fixed if we could look up not only spent=true/false for key images, but the corresponding txid as well?

Alternatively, if `rescan_bc` could be coaxed into not discarding the already-imported images, and refer to them during scanning instead, that might be a decent workaround.

## ndorf | 2021-04-19T22:51:57+00:00
I just realized there was a `rescan_bc keep_ki` option. But, it doesn't seem to do anything, just returns immediately.

## ndorf | 2021-04-20T03:42:27+00:00
So, that command doesn't do anything because [this exception](https://github.com/monero-project/monero/blob/f6e63ef260e795aacd408c28008398785b84103a/src/wallet/wallet2.cpp#L14111) is thrown (and silently caught somewhere outside the command handler).

Suppressing that exception [here](https://github.com/monero-project/monero/blob/f6e63ef260e795aacd408c28008398785b84103a/src/simplewallet/simplewallet.cpp#L5803) allows the command to proceed, and it actually finds all transactions including the missing one!

It fails later, due to the same exception, this time from [here](https://github.com/monero-project/monero/blob/f6e63ef260e795aacd408c28008398785b84103a/src/simplewallet/simplewallet.cpp#L5824). However at this point, everything has been found. Key images have to be reimported, but after that the full history shows up correctly.

## ndorf | 2021-04-22T20:18:19+00:00
With #7680, the `rescan_bc keep_ki` command fixes this situation, but still has to be run manually.

Perhaps `import_key_images` should check that all images match a known transfer, and warn/suggest the user run `rescan_bc keep_ki` if not?

# Action History
- Created by: ndorf | 2021-04-19T18:27:29+00:00
