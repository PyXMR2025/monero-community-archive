---
title: 'error: variable ‘walvars’ set but not used on Arch linux'
source_url: https://github.com/monero-project/monero/issues/4340
author: moneroexamples
assignees: []
labels: []
created_at: '2018-09-04T23:58:33+00:00'
updated_at: '2018-09-11T20:24:54+00:00'
type: issue
status: closed
closed_at: '2018-09-11T20:24:54+00:00'
---

# Original Description
```
gcc (GCC) 8.2.1 20180831
```

```
/home/mwo/monero/src/wallet/wallet_rpc_server.cpp:158:21: error: variable ‘walvars’ set but not used [-Werror=unused-but-set-variable]
     tools::wallet2 *walvars;
```



# Discussion History
## moneroexamples | 2018-09-05T00:06:57+00:00
possible fix:

```diff
diff --git a/src/wallet/wallet_rpc_server.cpp b/src/wallet/wallet_rpc_server.cpp
index 67f26c7a..79f00e12 100644
--- a/src/wallet/wallet_rpc_server.cpp
+++ b/src/wallet/wallet_rpc_server.cpp
@@ -155,16 +155,9 @@ namespace tools
       return false;
 
     m_vm = vm;
-    tools::wallet2 *walvars;
+
     std::unique_ptr<tools::wallet2> tmpwal;
 
-    if (m_wallet)
-      walvars = m_wallet;
-    else
-    {
-      tmpwal = tools::wallet2::make_dummy(*m_vm, true, password_prompter);
-      walvars = tmpwal.get();
-    }
     boost::optional<epee::net_utils::http::login> http_login{};
     std::string bind_port = command_line::get_arg(*m_vm, arg_rpc_bind_port);
     const bool disable_auth = command_line::get_arg(*m_vm, arg_disable_rpc_login);
```

## ViperRu | 2018-09-09T09:07:13+00:00
The Ubuntu 14.04 LTS has the same problem.

## moneromooo-monero | 2018-09-09T12:38:17+00:00
Since no PR so far, I added it as https://github.com/monero-project/monero/pull/4352 (and removed tmpwal while at it).

## moneroexamples | 2018-09-09T23:41:20+00:00
Thanks. I will close the issue once the PR gets merged. 

## moneromooo-monero | 2018-09-11T20:16:28+00:00
+resolved

# Action History
- Created by: moneroexamples | 2018-09-04T23:58:33+00:00
- Closed at: 2018-09-11T20:24:54+00:00
