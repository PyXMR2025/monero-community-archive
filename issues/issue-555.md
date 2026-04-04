---
title: generate new wallet problem
source_url: https://github.com/monero-project/monero/issues/555
author: shamahan
assignees: []
labels: []
created_at: '2015-12-23T10:21:31+00:00'
updated_at: '2015-12-24T14:47:04+00:00'
type: issue
status: closed
closed_at: '2015-12-24T14:47:04+00:00'
---

# Original Description
Hi

2015-Dec-22 05:12:37.034313 ERROR /root/bitmonero-src/src/wallet/wallet2.cpp:1297 e. THROW EXCEPTION: error::file_save_error
2015-Dec-22 05:12:37.034360 /root/bitmonero-src/src/wallet/wallet2.cpp:1297:N5tools5error15file_error_baseILi3EEE: failed to save file "56792186c8f62eea348b4567
": No such file or directory
2015-Dec-22 05:12:37.034498 Error: failed to generate new wallet: failed to save file "56792186c8f62eea348b4567": No such file or directory
2015-Dec-22 05:12:37.034554 ERROR /root/bitmonero-src/src/simplewallet/simplewallet.cpp:882 account creation failed
2015-Dec-22 05:12:37.034568 ERROR /root/bitmonero-src/src/simplewallet/simplewallet.cpp:2581 Failed to initialize wallet

FIX:

<pre>
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index d105291..8c41e1e 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -1293,9 +1293,11 @@ void wallet2::store()
   r = epee::file_io_utils::save_string_to_file(new_file, buf);
   THROW_WALLET_EXCEPTION_IF(!r, error::file_save_error, new_file);
   boost::filesystem::remove(old_file); // probably does not exist
-  std::error_code e = tools::replace_file(m_wallet_file, old_file);
-  THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
-  e = tools::replace_file(new_file, m_wallet_file);
+  if (boost::filesystem::exists(m_wallet_file)) {
+    std::error_code e = tools::replace_file(m_wallet_file, old_file);
+    THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
+  }
+  std::error_code e = tools::replace_file(new_file, m_wallet_file);
   THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
   boost::filesystem::remove(old_file);
 }
</pre>

I'm not sure it's a beautiful solution.


# Discussion History
## fluffypony | 2015-12-23T10:23:11+00:00
Markdown format of your diff:

```
diff --git a/src/wallet/wallet2.cpp b/src/wallet/wallet2.cpp
index d105291..8c41e1e 100644
--- a/src/wallet/wallet2.cpp
+++ b/src/wallet/wallet2.cpp
@@ -1293,9 +1293,11 @@ void wallet2::store()
   r = epee::file_io_utils::save_string_to_file(new_file, buf);
   THROW_WALLET_EXCEPTION_IF(!r, error::file_save_error, new_file);
   boost::filesystem::remove(old_file); // probably does not exist
-  std::error_code e = tools::replace_file(m_wallet_file, old_file);
-  THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
-  e = tools::replace_file(new_file, m_wallet_file);
+  if (boost::filesystem::exists(m_wallet_file)) {
+    std::error_code e = tools::replace_file(m_wallet_file, old_file);
+    THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
+  }
+  std::error_code e = tools::replace_file(new_file, m_wallet_file);
   THROW_WALLET_EXCEPTION_IF(e, error::file_save_error, m_wallet_file, e);
   boost::filesystem::remove(old_file);
 }
```


## PsychicCat | 2015-12-23T19:20:51+00:00
I had this issue as well on OSX. The above fix worked for me.


## fluffypony | 2015-12-23T19:26:23+00:00
@shamahan don't you want to submit it as a Pull Request rather so that the change is attributed to you?


## shamahan | 2015-12-24T14:21:48+00:00
@fluffypony i create pull request #558


## fluffypony | 2015-12-24T14:47:04+00:00
Merged


# Action History
- Created by: shamahan | 2015-12-23T10:21:31+00:00
- Closed at: 2015-12-24T14:47:04+00:00
