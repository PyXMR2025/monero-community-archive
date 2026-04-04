---
title: 'daemon RPC: get_info / set_daemon_address not working properly'
source_url: https://github.com/monero-project/monero/issues/7420
author: camthegeek
assignees: []
labels: []
created_at: '2021-03-03T17:53:32+00:00'
updated_at: '2021-03-05T16:13:48+00:00'
type: issue
status: closed
closed_at: '2021-03-05T16:12:48+00:00'
---

# Original Description
When using daemon RPC and setting the bootstrap daemon, it does not seem to be applied to the daemon.

Steps taken: 

Started with running monerod with flags `--rpc-bind-port`.

`curl http://127.0.0.1:44112/set_bootstrap_daemon -d '{"params":{"address": "node2.getmonero.us:18081", "username": "", "password": ""}}' -H 'Content-Type: application/json'`
returns
``{
  "status": "OK"
}``

At this point, I'm left to assume everything is fine. However, there are no indications in daemon that this was actually set other than the OK status given back from daemon RPC.

Run get_info: `curl http://127.0.0.1:44112/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_info"}' -H 'Content-Type: application/json'`
returns [trimmed irrelevant information]
```
{
  "id": "0",
  "jsonrpc": "2.0",
  "result": {
    ...
    "bootstrap_daemon_address": "",
    "busy_syncing": true,
    ...
    "database_size": 25362432,
    ...
    "height": 9101,
    "height_without_bootstrap": 9101,
   ...
    "mainnet": true,
    "nettype": "mainnet",
    ...
    "start_time": 1614792725,
    "status": "OK",
    "synchronized": false,
    ...
    "untrusted": false,
    ...
    "version": "0.17.0.0-b8f3e44a3",
    "was_bootstrap_ever_used": false,
    ...
  }
}
```

According to get_info, set_daemon_address was never set. I did try using different nodes (IP and domain), with port and without port as well as a local network fully synchronized Monero node.

# Discussion History
## moneromooo-monero | 2021-03-05T13:32:32+00:00
<s>Is this a restricted RPC port ?</s> Nevermind, the set_bootstrap_daemon RPC is not available in restricted mode, so it is not.

## moneromooo-monero | 2021-03-05T14:03:28+00:00
Can you run with this patch and set the logs ? The address appears for me.

```
diff --git a/src/rpc/core_rpc_server.cpp b/src/rpc/core_rpc_server.cpp
index e3c03ae3b..1d67e7088 100644
--- a/src/rpc/core_rpc_server.cpp
+++ b/src/rpc/core_rpc_server.cpp
@@ -225,6 +225,7 @@ namespace cryptonote
     constexpr const uint32_t credits_per_hash_threshold = 0;
     constexpr const bool rpc_payment_enabled = credits_per_hash_threshold != 0;
 
+MGINFO("set_bootstrap_daemon:  " << address);
     if (address.empty())
     {
       m_bootstrap_daemon.reset(nullptr);
@@ -430,6 +431,7 @@ namespace cryptonote
     bool r;
     if (use_bootstrap_daemon_if_necessary<COMMAND_RPC_GET_INFO>(invoke_http_mode::JON, "/getinfo", req, res, r))
     {
+MGINFO("trace: getinfo bs");
       {
         boost::shared_lock<boost::shared_mutex> lock(m_bootstrap_daemon_mutex);
         if (m_bootstrap_daemon.get() != nullptr)
@@ -444,6 +446,7 @@ namespace cryptonote
       return r;
     }
 
+MGINFO("trace: getinfo start");
     CHECK_PAYMENT_MIN1(req, res, COST_PER_GET_INFO, false);
 
     const bool restricted = m_restricted && ctx;
@@ -480,6 +483,7 @@ namespace cryptonote
     res.free_space = restricted ? std::numeric_limits<uint64_t>::max() : m_core.get_free_space();
     res.offline = m_core.offline();
     res.height_without_bootstrap = restricted ? 0 : res.height;
+MGINFO("trace: restricted: " << restricted);
     if (restricted)
     {
       res.bootstrap_daemon_address = "";
@@ -487,10 +491,13 @@ namespace cryptonote
     }
     else
     {
+MGINFO("trace: checking bootstrap daemon");
       boost::shared_lock<boost::shared_mutex> lock(m_bootstrap_daemon_mutex);
       if (m_bootstrap_daemon.get() != nullptr)
       {
+MGINFO("trace: not NULL");
         res.bootstrap_daemon_address = m_bootstrap_daemon->address();
+MGINFO("trace: -> " << res.bootstrap_daemon_address);
       }
       res.was_bootstrap_ever_used = m_was_bootstrap_ever_used;
     }
```

## camthegeek | 2021-03-05T16:12:48+00:00
Applied patch and re-ran using commands posted in original post. I could see the logging but it seems address was still not being set. After comparing methods, I realized that I was doing this the wrong way.

As this is using an endpoint that is not /json_rpc, I do not need to include -d params:{} and instead use -d {address:...}.

Closing issue as the issue was in my syntax and there is nothing for anyone else to do. 

edit: correct syntax: `curl http://127.0.0.1:44112/set_bootstrap_daemon -d '{"address": "node2.getmonero.us:18081"}' -H 'Content-Type: application/json'`

# Action History
- Created by: camthegeek | 2021-03-03T17:53:32+00:00
- Closed at: 2021-03-05T16:12:48+00:00
