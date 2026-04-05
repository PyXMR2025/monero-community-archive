---
title: A Faster Encryption Key Hash
source_url: https://github.com/MrCyjaneK/monero_c/issues/86
author: zhaono1
assignees: []
labels: []
created_at: '2024-11-08T01:51:49+00:00'
updated_at: '2024-12-10T02:05:38+00:00'
type: issue
status: closed
closed_at: '2024-12-10T02:05:38+00:00'
---

# Original Description
Hi @MrCyjaneK , I noticed that Monero supports [four types of UR](https://github.com/MrCyjaneK/monero_c/blob/master/patches/monero/0003-airgap.patch) and uses [encrypt_with_view_secret_key](https://github.com/monero-project/monero/blob/b089f9ee69924882c5d14dd1a6991deb05d9d1cd/src/wallet/wallet2.cpp#L14691) and [decrypt_with_view_secret_key](https://github.com/monero-project/monero/blob/b089f9ee69924882c5d14dd1a6991deb05d9d1cd/src/wallet/wallet2.cpp#L14724) to keep things safe when sending data. Sadly, cn_slow_hash is too hard on many devices. Can we switch to cn_fast_hash instead? I'd like to help by adding code and want to talk more about it.

# Discussion History
## MrCyjaneK | 2024-11-08T14:40:21+00:00
Hey! I don't have anything against supporting other formats - however I didn't notice any issue with it currently. By some devices did you mean low end phones or something closer to embedded?

## zhaono1 | 2024-11-08T15:59:04+00:00
I'm talking about some small devices where the slow hash needs a few M of memory, which is often hard to do on these devices since most small hardware doesn't have much memory. I think if the private view key is the same, it doesn't really matter what hash you use. What do you think? Can't wait to hear back from you! @MrCyjaneK 

## MrCyjaneK | 2024-11-12T12:35:51+00:00
Hey! Sorry for delayed reply - I'm up to having that kind of feature, however it should maintain backwards compatibility with other wallets. Do you plan on opening a PR to have this feature in monero_c?

## zhaono1 | 2024-11-12T14:05:24+00:00
Yes, I hope to open a PR to monero_c, either as a patch or another method. If you're okay with that, I'll start asap. By the way, what approach do you think is better? I think adding a new UR type could ensure compatibility with older versions, but it might add extra maintenance work.

## MrCyjaneK | 2024-11-13T00:02:20+00:00
@Charon-Fan I see two options
- Create a new UR format.. I don't think that it is good idea, as it would add much more maintenance burden.
- Brute force scanning to take in two encryption methods (if one fails, try the other one), and to functions that output UR strings we should add a boolean (or int/enum) to switch between the two encryption methods.



## MrCyjaneK | 2024-11-13T00:04:20+00:00
If you need any help, support or assistance I'm up to guide you through the steps of adding a patch, easiest way is to
1. clone the repo, run apply-patches.sh script
2. Make you change and commit it (in monero submodule)
3. `$ git format-patch -1`
4. Move it to patches directory

There is a pending cleanup PR going on currently so a new patch is fine, ideally I would like it to be in the UR patch but.. don't bother with it, I have to cleanup all of the patches anyway.

## zhaono1 | 2024-11-18T11:24:34+00:00
Hey bro @MrCyjaneK , I want to check something with you. I noticed that when unsigned data is sent to an offline device, it seems like the minor subaddress is missing. The current method is to search for it by going through a subaddress map. Am I understanding this right? https://github.com/monero-project/monero/blob/b089f9ee69924882c5d14dd1a6991deb05d9d1cd/src/cryptonote_basic/cryptonote_format_utils.cpp#L314

## MrCyjaneK | 2024-11-18T12:01:36+00:00
```
From f49bc7059762210dc0d00c4ad0ab2461f81c8119 Mon Sep 17 00:00:00 2001
From: ANONERO <anonero@dnmx.org>
Date: Mon, 20 May 2024 16:11:57 +0000
Subject: [PATCH] Offline-signing: show actual address when spending to
 integrated address

fix by tobtoht
---
 src/wallet/api/unsigned_transaction.cpp | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)

diff --git a/src/wallet/api/unsigned_transaction.cpp b/src/wallet/api/unsigned_transaction.cpp
index 6165a2240..2202f06bb 100644
--- a/src/wallet/api/unsigned_transaction.cpp
+++ b/src/wallet/api/unsigned_transaction.cpp
@@ -297,7 +297,7 @@ std::vector<std::string> UnsignedTransactionImpl::recipientAddress() const
           MERROR("empty destinations, skipped");
           continue;
         }
-        result.push_back(cryptonote::get_account_address_as_str(m_wallet.m_wallet->nettype(), utx.dests[0].is_subaddress, utx.dests[0].addr));
+        result.push_back(utx.dests[0].address(m_wallet.m_wallet->nettype(), {}));
     }
     return result;
 }
```

This may be the fix, if I understand the issue correctly @Charon-Fan 

## zhaono1 | 2024-11-18T12:22:44+00:00
~~Sorry, I didn't explain it clearly. The specific situation is that offline signing needs to generate a key image, but the data is missing the minor of the output I need (I only have the [unsigned_tx_set](https://github.com/monero-project/monero/blob/b089f9ee69924882c5d14dd1a6991deb05d9d1cd/src/wallet/wallet2.h#L677)). I want to know if I need to find it myself by going through the list.~~

## zhaono1 | 2024-12-02T16:03:11+00:00
```
/Documents/code/github/cake_wallet/scripts/monero_c/monero/src/device/device_io_dummy.hpp:38:16: error: redefinition of 'hid_conn_params'
        struct hid_conn_params {
               ^
/Documents/code/github/cake_wallet/scripts/monero_c/monero/src/device/device_io_hid.hpp:53:12: note: previous definition is here
    struct hid_conn_params {

```
Hi @MrCyjaneK , when I compile, I run into a redefinition problem. How should I fix it?

## MrCyjaneK | 2024-12-02T16:55:48+00:00
`-DHIDAPI_DUMMY=ON` should fix it

## zhaono1 | 2024-12-02T17:17:51+00:00
https://github.com/cake-tech/cake_wallet/blob/main/howto-build-ios.md Actually, I followed the guide from Cake Wallet, and this issue happened during the `./build_monero_all.sh` step. And yes, I noticed that -DHIDAPI_DUMMY=ON is already included in the configuration, but the problem still happens

## MrCyjaneK | 2024-12-02T19:31:25+00:00
@Charon-Fan are you up for a quick call? This issue is most likely fixed in #76 

## zhaono1 | 2024-12-10T02:05:35+00:00
I’ve already resolved this issue by optimizing device space. Thanks for your help🙌

# Action History
- Created by: zhaono1 | 2024-11-08T01:51:49+00:00
- Closed at: 2024-12-10T02:05:38+00:00
