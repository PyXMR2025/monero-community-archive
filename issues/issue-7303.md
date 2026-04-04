---
title: '[EMERGENCY - help needed] Stuck at "Some owned outputs have missing key images
  - import_key_images needed" on hot wallet.'
source_url: https://github.com/monero-project/monero/issues/7303
author: xmrdog
assignees: []
labels: []
created_at: '2021-01-10T13:25:14+00:00'
updated_at: '2021-10-06T02:38:33+00:00'
type: issue
status: closed
closed_at: '2021-10-06T02:38:33+00:00'
---

# Original Description
My offline setup is broken. Can someone help me?

* I'm stuck at "Some owned outputs have missing key images - import_key_images needed" on my hot wallet.
* Online wallet is v0.17.1.9
* Offline wallet is v0.17.0.1

These are the steps I followed:

* Removed existing hot wallet (to start from scratch).
* On cold wallet run `save_watch_only` and transferred to hot machine.
* On hot machine, completely refresh the newly created watch-only wallet.
* It shows a clearly incorrect balance (way too high) and says "Some owned outputs have missing key images - import_key_images needed".
* Still on hot wallet, run `export_outputs`, transfer outputs to cold machine.
* On cold machine, run `import_outputs`. It said "0" imported. (Why?)
* On cold machine, run `export_key_images`, and transfer to hot machine.
* On hot machine, run `import_key_images`. It says "Signed key images imported to height 0, 0.000000000000 spent, 0.000000000000 unspent".
* I still have exactly the same output: The incorrect balance and "Some owned outputs have missing key images - import_key_images needed".

What's wrong?

# Discussion History
## selsta | 2021-01-10T13:27:45+00:00
Did you try the all parameter?

export_outputs all filename
export_key_images all filename

## xmrdog | 2021-01-10T13:28:50+00:00
@selsta Thanks for the quick reply. No, I didn't do that. Why would that even be needed? I'll try this now and report back to you, but I'm just curious why this isn't the default?

## xmrdog | 2021-01-10T13:42:08+00:00
@selsta Update: Adding "all" did not help. I still got "0" for the output import, and same output for subsequent key image import.

Are my funds lost? :(

## selsta | 2021-01-10T14:21:28+00:00
I’m not super familiar with cold / hot wallets in monero, someone else has to reply. But I doubt your funds are lost.

## xmrdog | 2021-01-10T15:03:08+00:00
I tried the above steps again, this time truly starting from scratch with only the .keys file (i.e. deleting the corresponding wallet file) on the cold machine.

I still get the same "0" imported on the cold machine and the same "Signed key images imported to height 0, 0.000000000000 spent, 0.000000000000 unspent" on hot machine.

I'm worried.

## selsta | 2021-01-10T15:05:12+00:00
I would also try to use the same version on both cold and hot wallet.

Also, could you theoretically restore from seed?

## xmrdog | 2021-01-10T15:06:56+00:00
Are wallet/file formats not completely the same for v0.17.1.9 and v0.17.0.1 for hot and cold? @moneromooo-monero 

## selsta | 2021-01-10T15:08:13+00:00
Using the same version is just to rule out any issues with using different software.

## xmrdog | 2021-01-10T15:08:15+00:00
To test a same version, I'd rather go back to v0.17.0.1 on hot machine instead (in case v0.17.1.9 introduced some catastrophic security bugs). Can I do downgrade safely in terms of blockchain sync? @moneromooo-monero 

## selsta | 2021-01-10T15:12:15+00:00
v0.17.1.0 had

- Fix a bug in wallet serialization that could lead to inaccurate display balance

in its release notes. Not guaranteed to be related but that's why I would try to use the same version.

## moneromooo-monero | 2021-01-10T15:33:34+00:00
What is the size of the output export file (when you use all) ?

## xmrdog | 2021-01-10T15:38:36+00:00
@moneromooo-monero Output file of `export_outputs all` on hot machine has size 3,773 bytes.

## moneromooo-monero | 2021-01-10T15:44:00+00:00
If I post a patch adding more logs, can you apply it and run with it, then paste the resulting log ? It'll have some private info (like the number of outputs you have, that kind of thing, but no secret keys etc)

## xmrdog | 2021-01-10T15:47:29+00:00
@moneromooo-monero Sure, let's do it. You only want me to run this on the hot wallet anyway, right? How can I PM you?

## xmrdog | 2021-01-10T15:52:44+00:00
I'm on ProtonMail e.g.. BTW, your patch will not reveal any XMR amounts either right?

## moneromooo-monero | 2021-01-10T15:54:04+00:00
Both. It'll log basic data for each of the four steps. You can find me on freenode as moneromooo if you need.

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index 7f8851748..9794ca6b3 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -12651,6 +12651,7 @@ bool wallet2::export_key_images(const std::string &filename, bool all) const
     data += std::string((const char *)&i.first, sizeof(crypto::key_image));
     data += std::string((const char *)&i.second, sizeof(crypto::signature));
   }
+MGINFO("export_key_images: " << all << " " << ski.second.size());
 
   // encrypt data, keep magic plaintext
   PERF_TIMER(export_key_images_encrypt);
@@ -12781,6 +12782,7 @@ uint64_t wallet2::import_key_images(const std::vector<std::pair<crypto::key_imag
   THROW_WALLET_EXCEPTION_IF(signed_key_images.size() > m_transfers.size() - offset, error::wallet_internal_error,
       "The blockchain is out of date compared to the signed key images");
 
+MGINFO("import_key_images: " << signed_key_images.size() << " " << offset);
   if (signed_key_images.empty() && offset == 0)
   {
     spent = 0;
@@ -13184,6 +13186,7 @@ std::pair<size_t, std::vector<tools::wallet2::transfer_details>> wallet2::export
     while (offset < m_transfers.size() && (m_transfers[offset].m_key_image_known && !m_transfers[offset].m_key_image_request))
       ++offset;
 
+MGINFO("export_outputs: " << all << " " << offset << " " << m_transfers.size());
   outs.reserve(m_transfers.size() - offset);
   for (size_t n = offset; n < m_transfers.size(); ++n)
   {
@@ -13223,6 +13226,7 @@ size_t wallet2::import_outputs(const std::pair<size_t, std::vector<tools::wallet
 
   const size_t offset = outputs.first;
   const size_t original_size = m_transfers.size();
+MGINFO("import_outputs: " << offset << " " << original_size << " " << outputs.second.size());
   m_transfers.resize(offset + outputs.second.size());
   for (size_t i = 0; i < offset; ++i)
     m_transfers[i].m_key_image_request = false;
```

patch -p1 < FILENAME

## moneromooo-monero | 2021-01-10T15:55:02+00:00
No, you can see above, just info about number of outputs. After that I'll have more logs probably. This is just to see which step goes wonky.

## moneromooo-monero | 2021-01-10T15:57:01+00:00
Oh, and you need to run with: --log-level 0
There might also be exception logs, I'm interested if any you might have running this.

## moneromooo-monero | 2021-01-10T22:50:07+00:00
Are you sure you built the new patch for the loading/cold wallet ? It should log for both load and save.

## moneromooo-monero | 2021-01-10T23:16:42+00:00
Trying here, I get logs on both sides. Make sure you built both and post on IRC again when you're back.

## xmrdog | 2021-01-11T05:58:52+00:00
@moneromooo-monero I just checked again. I'm certain the patch was applied and the new monero-wallet-cli was transferred over correctly. The only explantation I now have is that those new lines of code are simply not getting executed, for some reason. Would you like to provide a new patch to analyze further?

## xmrdog | 2021-01-11T09:44:11+00:00
@moneromooo-monero From one point of view this kind of makes sense... the import is not yielding any outputs for some reason (0 outputs, as we saw) and therefore nothing interesting gets logged out.

## moneromooo-monero | 2021-01-11T12:29:16+00:00
It does not make sense.

## moneromooo-monero | 2021-01-11T12:46:17+00:00
Try https://paste.debian.net/hidden/2ffecaaa/ instead then

## xmrdog | 2021-01-13T13:06:00+00:00
@moneromooo-monero Thanks again for the help. Do you have an approx ETA on a new public update that fixes the issue?

## moneromooo-monero | 2021-01-15T20:06:00+00:00
No.

## moneromooo-monero | 2021-01-16T17:23:13+00:00
https://github.com/moneromooo-monero/bitmonero/commit/2910c84f4ba7c80f70e20c2746be6bf4189d1df0 should fix this and have backward compatibility with previous wallet caches. Nasty hack though.

## xmrdog | 2021-01-16T22:07:22+00:00
@moneromooo-monero hey, thanks so much for working on this and publishing as a commit! Any chance you can do a pull request into the official repo, on top of the v0.17.1.9 commit? I could, if you want, be one of the reviewers/testers for such a pull request.

## moneromooo-monero | 2021-01-17T13:09:51+00:00
I will. I'd like for a mac user to confirm it doesn't break wallet caches first though.

## moneromooo-monero | 2021-01-17T21:07:29+00:00
https://github.com/moneromooo-monero/bitmonero/commit/b744466e906b6c6233e996de07fa648624918a4c (slightly modified, thanks xmrdog for mac testing) fixes it.

## moneromooo-monero | 2021-01-18T22:25:15+00:00
If you don't mind double checking it works for you, I changed the code after review, https://github.com/monero-project/monero/pull/7321

# Action History
- Created by: xmrdog | 2021-01-10T13:25:14+00:00
- Closed at: 2021-10-06T02:38:33+00:00
