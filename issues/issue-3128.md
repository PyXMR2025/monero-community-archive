---
title: monerod does DNS lookups and attempts to connect to other nodes, even if specifying
  an exclusive node
source_url: https://github.com/monero-project/monero/issues/3128
author: leonklingele
assignees: []
labels: []
created_at: '2018-01-15T17:40:43+00:00'
updated_at: '2018-01-30T09:56:32+00:00'
type: issue
status: closed
closed_at: '2018-01-30T09:56:32+00:00'
---

# Original Description
I tried launching `monerod` on `node A` with these args:

```sh
"$MONEROD" \
    --add-exclusive-node 127.0.0.1:18090 --allow-local-ip \
    --p2p-bind-ip 127.0.0.1 \
    --rpc-bind-ip 127.0.0.1 \
    --no-igd \
    --hide-my-port \
    --db-sync-mode safe
```

Port 18090 is forwarded from my other `node B` via SSH.

Still, `monerod` on `node A` does DNS lookups on the [seed nodes](https://github.com/monero-project/monero/blob/c611cca4624e3556a5e68b745acbcfbfab71618a/src/p2p/net_node.h#L127-L130) using Google DNS (8.8.4.4) and tries to connect to the various nodes returned.
This is a privacy issue and should not happen when `--add-exclusive-node` is used.

__EDIT__:
Fix Google DNS IP, `monerod` is not using 8.8.8.8.

# Discussion History
## moneromooo-monero | 2018-01-15T18:30:53+00:00
Which commit hash are you running ?

As for DNS lookups, ifyou don't want them, use DNS_PUBLIC=somethinginvalid or tcp://127.0.0.1


## leonklingele | 2018-01-15T19:15:44+00:00
> Which commit hash are you running ?

Latest stable release (793bc973746a10883adb2f89827e223f562b9651)

> As for DNS lookups, ifyou don't want them

Why do I need to opt-out for privacy? DNS lookups are not required when `--add-exclusive-node ` is used (if the node is specified by IP)

## leonklingele | 2018-01-15T19:27:55+00:00
> tcp://127.0.0.1

That wouldn't help if I had a local DNS resolver running, right?

## moneromooo-monero | 2018-01-15T22:47:52+00:00
Then it's fixed by 054054c92f5d6fe6c598a31c64c215485a7f4995.

Why do you think --add-exclusive-node is a DNS option ? It is not.

Using 127.0.0.1 would not work if you have a DNS resolver listening.

## leonklingele | 2018-01-15T23:05:36+00:00
> Why do you think --add-exclusive-node is a DNS option ? It is not.

Why would the daemon need to connect to a DNS server if it only needs to connect to a single IP which was specified via a command line arg?

## moneromooo-monero | 2018-01-16T10:24:52+00:00
To get updates and checkpoints.

## leonklingele | 2018-01-16T10:33:47+00:00
Where does it check for updates / try to retrieve checkpoints from? I assume it uses other nodes. Why is the exclusive node I'm providing not sufficient enough to do that?

## leonklingele | 2018-01-16T10:39:31+00:00
OK, doesn't look like it. I will try to start `monerod` with `--check-updates disabled`. Is there a way to disable checking for checkpoints via DNS?

## moneromooo-monero | 2018-01-16T13:08:04+00:00
It appears not. --offline disables those, but a "just for DNS" switch would seem useful.

## moneromooo-monero | 2018-01-17T10:27:47+00:00
https://github.com/monero-project/monero/pull/3143

## leonklingele | 2018-01-17T10:37:07+00:00
I'm now starting `monerod` with the above flags including `--check-updates disabled --disable-dns-checkpoints`, however it still looks up `seeds.moneroseeds.*`

## moneromooo-monero | 2018-01-17T11:14:29+00:00
Try --seed-node SAMEIP:SAMEPORT

## moneromooo-monero | 2018-01-17T11:16:13+00:00
Or:

```
diff --git a/src/p2p/net_node.inl b/src/p2p/net_node.inl
index 269a9ba..1423518 100644
--- a/src/p2p/net_node.inl
+++ b/src/p2p/net_node.inl
@@ -1107,7 +1107,7 @@ namespace nodetool
   template<class t_payload_net_handler>
   bool node_server<t_payload_net_handler>::connect_to_seed()
   {
-      if (m_seed_nodes.empty() || m_offline)
+      if (m_seed_nodes.empty() || m_offline || !m_exclusive_peers.empty())
         return true;
 
       size_t try_count = 0;
```



## leonklingele | 2018-01-17T11:32:28+00:00
> Try --seed-node SAMEIP:SAMEPORT

Didn't help, even with the patch applied it still does DNS lookups.

## moneromooo-monero | 2018-01-17T11:36:25+00:00
Can you tell what it is trying to resolve ?

## leonklingele | 2018-01-17T11:47:23+00:00
- seeds.moneroseeds.ae.org: type A, class IN
- seeds.moneroseeds.li: type A, class IN
- seeds.moneroseeds.se: type A, class IN
- seeds.moneroseeds.ch: type A, class IN

## moneromooo-monero | 2018-01-17T11:58:50+00:00
Ah, I see it. Fixing...

## moneromooo-monero | 2018-01-17T12:02:54+00:00
https://github.com/monero-project/monero/pull/3145

## leonklingele | 2018-01-17T12:11:11+00:00
Didn't help :( Just to be sure: I've applied #3143 and #3145 and am passing these args:

```sh
"$MONEROD" \
    --add-exclusive-node 127.0.0.1:18090 --allow-local-ip \
    --p2p-bind-ip 127.0.0.1 \
    --rpc-bind-ip 127.0.0.1 \
    --no-igd \
    --hide-my-port \
    --db-sync-mode safe \
    --check-updates disabled \
    --disable-dns-checkpoints
```

## leonklingele | 2018-01-17T12:15:50+00:00
Seems to be fixed, see https://github.com/monero-project/monero/issues/3146#issuecomment-358286989

## moneromooo-monero | 2018-01-17T12:25:21+00:00
I updated 3145, it was checking exclusive nodes before parsing the command line.

## moneromooo-monero | 2018-01-30T09:46:20+00:00
+resolved

# Action History
- Created by: leonklingele | 2018-01-15T17:40:43+00:00
- Closed at: 2018-01-30T09:56:32+00:00
