---
title: Feature Request for smoother hard forks
source_url: https://github.com/monero-project/monero/issues/3653
author: Gingeropolous
assignees: []
labels: []
created_at: '2018-04-17T11:58:19+00:00'
updated_at: '2018-04-20T03:25:53+00:00'
type: issue
status: closed
closed_at: '2018-04-20T03:25:53+00:00'
---

# Original Description
A newly downloaded daemon should reject peers that still show they are are on a v6 block when the new daemon says the hard fork for v7 already happened. They should only connect to peers showing v7. (or whatever the version numbers are ... you get the idea)

A newly downloaded daemon should clear their p2pstate.bin or however the peerlist is stored. This will prevent peering with non-updated nodes. 

# Discussion History
## moneromooo-monero | 2018-04-17T17:03:06+00:00
Start with --log-level 1, and add this extra log:
```
diff --git a/src/cryptonote_protocol/cryptonote_protocol_handler.inl b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
index a561d56..d421475 100644
--- a/src/cryptonote_protocol/cryptonote_protocol_handler.inl
+++ b/src/cryptonote_protocol/cryptonote_protocol_handler.inl
@@ -269,6 +269,7 @@ namespace cryptonote
     if (hshd.current_height > 0)
     {
       const uint8_t version = m_core.get_ideal_hard_fork_version(hshd.current_height - 1);
+      MGINFO(context << " peer claims version " << (unsigned)hshd.top_version << " for " << (hshd.current_height - 1) << ", we expect " << 
(unsigned)version);
       if (version >= 6 && version != hshd.top_version)
       {
         if (version < hshd.top_version)
```

## moneromooo-monero | 2018-04-17T17:03:44+00:00
Also, clearing p2pstate.bin is dangerous, it makes you dependent on the seed nodes again to find the network anew.

## Gingeropolous | 2018-04-17T18:53:28+00:00
well I'd argue that any hardforking software released by the monero maintainers is making you dependent on the maintainers ... I mean, I get what your saying, but running new software with code that causes a consensus change is a vote of confidence and trust, so the seed nodes should be non-dangerous.

also, i don't get whats going on in the first comment... does this mean that this feature is already present? Or does that patch do what was described? 

## iamsmooth | 2018-04-18T04:15:16+00:00
There is really no need to _ever_ clear p2pstate.bin. Any source of 'potential' peer nodes is okay and should be used (indeed it would be okay in a sense to pick random IPs), but peers that misbehave should be dropped/banned more reliably. It is the latter part that doesn't work now.

## moneromooo-monero | 2018-04-18T09:06:00+00:00
Peers claiming the "wrong" version for their top block are not used. I took your bug report to mean they are being used. If they're not and you just asked because you did not know it was here, then it is here. Maybe buggy though, and in that case the patch above adds logs to see what the peers are claiming.

## iamsmooth | 2018-04-18T15:46:06+00:00
The peers may not be used but they don't appear to be banned (I think). I could be wrong though, I haven't looked at it carefully and just basing this on what I see in logs on my own nodes.

## moneromooo-monero | 2018-04-18T21:42:10+00:00
They're not banned indeed. Banning would get them dropped a bit earlier in the connection process if that's wanted.

## Gingeropolous | 2018-04-20T03:25:53+00:00
a more better suggestion was made in #3661 

# Action History
- Created by: Gingeropolous | 2018-04-17T11:58:19+00:00
- Closed at: 2018-04-20T03:25:53+00:00
