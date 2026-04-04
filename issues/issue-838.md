---
title: --p2p-bind-ip not binding outgoing connections to the specified interface when
  having more than one interface.
source_url: https://github.com/monero-project/monero/issues/838
author: osensei
assignees: []
labels:
- bug
created_at: '2016-05-13T08:29:24+00:00'
updated_at: '2019-09-26T21:43:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When having more than one interface with internet access on your system, e.g. eth0 and eth1, and being eth0 the default route, if you bind bitmonerod to eth1, outgoing connections will still be made on eth0.

I would expect the behavior to be that outgoing connections would be bound to eth1.

I believe this also results in bitmonerod announcing eth0 interface to other peers, but not receiving incoming connections because they are only accepted on eth1 (which apparently is not being announced).

In the meantime, as a work-around I used this: http://daniel-lange.com/archives/53-Binding-applications-to-a-specific-IP.html


# Discussion History
## moneromooo-monero | 2016-07-15T19:34:00+00:00
Not tested, as I have only one NIC, but let me know if this works: https://github.com/moneromooo-monero/bitmonero/tree/bind-ip


## osensei | 2016-09-18T07:36:05+00:00
@moneromooo-monero 

I totally missed your comment here, I'll give it a try as soon as I can.


## ghost | 2018-01-07T11:43:13+00:00
@osensei Has your issue been fixed?

## dEBRUYNE-1 | 2018-01-08T12:28:11+00:00
+bug

## coneiric | 2018-07-01T04:19:33+00:00
> Not tested, as I have only one NIC, but let me know if this works: https://github.com/moneromooo-monero/bitmonero/tree/bind-ip

Tested, and it works for binding the p2p IP properly. The code has moved around a bit since the patch, but the fix works.

Here is a patch against the current master with @moneromooo-monero's fix:

```diff
diff --git a/src/p2p/net_node.inl b/src/p2p/net_node.inl
index 85470f79..e318f564 100644
--- a/src/p2p/net_node.inl
+++ b/src/p2p/net_node.inl
@@ -934,7 +934,7 @@ namespace nodetool
     bool res = m_net_server.connect(epee::string_tools::get_ip_string_from_int32(ipv4.ip()),
       epee::string_tools::num_to_string_fast(ipv4.port()),
       m_config.m_net_config.connection_timeout,
-      con);
+      con, m_bind_ip.empty() ? "0.0.0.0" : m_bind_ip);
 
     if(!res)
     {
@@ -1614,7 +1614,7 @@ namespace nodetool
         return false;
       }
       return true;
-    });
+    }, m_bind_ip.empty() ? "0.0.0.0" : m_bind_ip);
     if(!r)
     {
       LOG_WARNING_CC(context, "Failed to call connect_async, network error.");
```

## moneromooo-monero | 2018-07-02T17:07:59+00:00
Thanks, PRed.

## ossii79 | 2019-04-11T06:25:30+00:00
This is still an issue in 0.14, would appriciate a merge in to master for this one.
Running a few servers with full nodes, where I got multiple IPs and want to force traffic in+out trough a specific IP (not the main).
Currently I get a "No incoming connections - check firewalls/routers allow port 18080" when binding p2p to a non-default IP.

## moneromooo-monero | 2019-04-11T22:49:07+00:00
IIRC the patch caused trouble with connecting via Tor, so got reverted.


## trasherdk | 2019-04-12T01:17:54+00:00
So maybe `--p2p-bind-ip-for-real` :)

# Action History
- Created by: osensei | 2016-05-13T08:29:24+00:00
