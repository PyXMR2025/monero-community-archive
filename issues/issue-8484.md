---
title: Segfault and corrupt wallet files caused by exporting and importing outputs
  with monero-wallet-rpc
source_url: https://github.com/monero-project/monero/issues/8484
author: woodser
assignees: []
labels: []
created_at: '2022-08-05T14:11:38+00:00'
updated_at: '2023-07-26T22:42:34+00:00'
type: issue
status: closed
closed_at: '2023-07-26T22:42:34+00:00'
---

# Original Description
I'm able to segfault monero-wallet-rpc and corrupt the wallet files by calling export_outputs then import_outputs with the result. The calls succeed, indicating 0 outputs were imported. But then these errors start appearing when the next transaction is sent. My tests send funds back to the original wallet so it might be something specific to that. Otherwise, my build and tests are working on v0.18.0.0.

```
2022-08-04 23:38:41.438	W Spent money: 0.000000000000, with tx: <48219a8a2c1534c13b2d79448e79598192829327686f45fdd2fcc04649976c64>
2022-08-04 23:38:41.438	E Invalid index
2022-08-04 23:38:41.438	E Error parsing blocks: Invalid index
2022-08-04 23:38:46.206	E Public key 2788e1c6b262a767ee5bcaeea8da6a560c8e68c8d5f8c46aaf97f8b54e9fd5a2 from received 0.000000600000 output already exists with unspent 0.000000600000 in tx <48219a8a2c1534c13b2d79448e79598192829327686f45fdd2fcc04649976c64>, received output ignored
2022-08-04 23:38:46.208	E Public key c185f909de3c0ef5db4255ed423060c00ccc09ad379f08bc669dfdd820ee0fdd from received 0.000000600000 output already exists with unspent 0.000000600000 in tx <48219a8a2c1534c13b2d79448e79598192829327686f45fdd2fcc04649976c64>, received output ignored
```

I confirmed the issue is introduced with #8179 and resolved by reverting this PR.

# Discussion History
## moneromooo-monero | 2022-08-06T15:54:04+00:00
I could make two txes in a row with cold signing, exporting/importing outputs/key images both times. Can you describe your steps in more detail ?

In any case, reading the code, I see something is missing, below. My test wasn't run with that patch. Untested yet.

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 195763949..d87aa0e33 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -13241,7 +13241,7 @@ size_t wallet2::import_outputs(const std::pair<uint64_t, std::vector<tools::wall
     exported_transfer_details etd = outputs.second[i];
     transfer_details &td = m_transfers[i + offset];
 
-    // setup td with "cheao" loaded data
+    // setup td with "cheap" loaded data
     td.m_block_height = 0;
     td.m_txid = crypto::null_hash;
     td.m_global_output_index = etd.m_global_output_index;
@@ -13254,6 +13254,8 @@ size_t wallet2::import_outputs(const std::pair<uint64_t, std::vector<tools::wall
     td.m_key_image_known = etd.m_flags.m_key_image_known;
     td.m_key_image_request = etd.m_flags.m_key_image_request;
     td.m_key_image_partial = false;
+    td.m_subaddr_index.major = etd.m_subaddr_index_major;
+    td.m_subaddr_index.minor = etd.m_subaddr_index_minor;
 
     // skip those we've already imported, or which have different data
     if (i + offset < original_size)
diff --git a/src/wallet/wallet2.h b/src/wallet/wallet2.h
index 16e898ad8..6598dea10 100644
--- a/src/wallet/wallet2.h
+++ b/src/wallet/wallet2.h
@@ -401,9 +401,11 @@ private:
       } m_flags;
       uint64_t m_amount;
       std::vector<crypto::public_key> m_additional_tx_keys;
+      uint32_t m_subaddr_index_major;
+      uint32_t m_subaddr_index_minor;
 
       BEGIN_SERIALIZE_OBJECT()
-        VERSION_FIELD(0)
+        VERSION_FIELD(1)
         FIELD(m_pubkey)
         VARINT_FIELD(m_internal_output_index)
         VARINT_FIELD(m_global_output_index)
@@ -411,6 +413,8 @@ private:
         FIELD(m_flags.flags)
         VARINT_FIELD(m_amount)
         FIELD(m_additional_tx_keys)
+        VARINT_FIELD(m_subaddr_index_major)
+        VARINT_FIELD(m_subaddr_index_minor)
       END_SERIALIZE()
     };
 
```

## j-berman | 2022-08-06T17:36:22+00:00
I think he's re-importing into the same wallet that exports (not doing the cold signing flow). One thing I've noticed so far doing this that's off (that I'm still looking into a good solution for) is that [the `mask` can get overwritten with the identity element](https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/wallet/wallet2.cpp#L13251) upon import, which can trip up this line during tx construction:

https://github.com/monero-project/monero/blob/b6a029f222abada36c7bc6c65899a4ac969d7dee/src/wallet/wallet2.cpp#L8568 

## woodser | 2022-08-06T20:13:48+00:00
Yeah it's exporting and importing back to the same wallet.

Pretty sure a tx is broadcast which sends funds back to the same account, then wallet rpc `export_outputs` and `import_outputs` are called, then another tx is broadcast sending funds back to the same account, all with the same wallet.

## moneromooo-monero | 2022-08-07T14:56:21+00:00
The cold wallet doesn't call the daemon, so I don't think the mask is needed by it.
Maybe the best is to error out when importing outputs in a hot wallet. And presumably importing key images in a cold wallet.


## moneromooo-monero | 2022-08-07T15:29:04+00:00
The three patches at https://github.com/moneromooo-monero/bitmonero/tree/io allow me to export outputs, import them in the same wallet, and make a tx/sweep_all to itself. If you still get it to break, please be more precise about the conditions.

## woodser | 2022-08-08T20:53:20+00:00
It seems to be working. I can't recreate the issues after applying the patches. Thanks.

## moneromooo-monero | 2022-08-08T21:22:04+00:00
Thanks. I'll wait to see what j-berman says about mask and PR if it still seems good.

## j-berman | 2022-08-09T07:02:49+00:00
>  Maybe the best is to error out when importing outputs in a hot wallet. And presumably importing key images in a cold wallet.

I agree this seems like the best solution to me too. Left some comments on the commits

## moneromooo-monero | 2022-08-09T19:45:26+00:00
I cannot find those. Mind posting a link ?

## selsta | 2022-08-09T19:48:26+00:00
https://github.com/moneromooo-monero/bitmonero/commits/io

Click on the patches and the comments should show up.

## moneromooo-monero | 2022-08-12T11:57:11+00:00
Thanks. I thought I'd done that and saw just wooder's comment, guess I did it wrong.

## woodser | 2022-08-13T02:09:25+00:00
Just updating that this issue is still present in v0.18.1.0, and if I apply the patches on top of v0.18.1.0, things are stable, except it occasionally hangs on import_outputs (when used correctly with view-only and offline wallets) for some unknown reason, but I didn't investigate where exactly it's hanging.

## j-berman | 2022-08-16T03:44:33+00:00
@woodser can you see if you can repro the hanging with #8510 :)

## woodser | 2022-08-25T17:20:29+00:00
The hanging is resolved with #8513.

## selsta | 2023-07-26T22:42:34+00:00
Issue appears to be resolved.

# Action History
- Created by: woodser | 2022-08-05T14:11:38+00:00
- Closed at: 2023-07-26T22:42:34+00:00
