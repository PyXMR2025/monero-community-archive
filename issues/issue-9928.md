---
title: monerod should not ban local IP address
source_url: https://github.com/monero-project/monero/issues/9928
author: '0xFFFC0000'
assignees: []
labels: []
created_at: '2025-05-18T08:02:09+00:00'
updated_at: '2025-05-18T08:15:47+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
monerod should not block/ban local IP addresses [1]. This regularly happens if there is a intensive use of RPC, e.g. in local test scenarios. This fixes it. 

````
diff --git a/src/p2p/net_node.inl b/src/p2p/net_node.inl
index 8da16ec72..948f8739c 100644
--- a/src/p2p/net_node.inl
+++ b/src/p2p/net_node.inl
@@ -175,6 +175,12 @@ namespace nodetool
   template<class t_payload_net_handler>
   bool node_server<t_payload_net_handler>::is_remote_host_allowed(const epee::net_utils::network_address &address, time_t *t)
   {
+    if (address.is_local())
+    {
+      MWARNING("Address is local " << address.host_str() << ", local IPs are allowed.");
+      return true;
+    }
+
     CRITICAL_REGION_LOCAL(m_blocked_hosts_lock);
 
     const time_t now = time(nullptr);

````


1. https://github.com/monero-project/monero/blob/125622d5bdc42cf552be5c25009bd9ab52c0a7ca/src/p2p/net_node.inl#L176

# Discussion History
## nahuhh | 2025-05-18T08:09:25+00:00
Onion/i2p etc tunnels are treated as local

edit: nvm that would still be kind of silly to ban local ip, as it would ban all onion/i2p traffic unilaterally 

## 0xFFFC0000 | 2025-05-18T08:15:45+00:00
> Onion/i2p etc tunnels are treated as local
> 
> edit: nvm that would still be kind of silly to ban local ip, as it would ban all onion/i2p traffic unilaterally

What you first said is important IMHO. 

with that 3 lines I am basically preventing any ban. So if onion/i2p IPs are treated as local. Then we are basically not going to ban any onioin/i2p IP. Which is not what we want. 



# Action History
- Created by: 0xFFFC0000 | 2025-05-18T08:02:09+00:00
