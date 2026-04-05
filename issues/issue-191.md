---
title: monerod relays pool txs to syncing peers
source_url: https://github.com/seraphis-migration/monero/issues/191
author: j-berman
assignees: []
labels:
- upstream
created_at: '2025-10-22T22:14:17+00:00'
updated_at: '2025-12-12T02:33:15+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Looking at my logs, looks like peers are relaying pool txs to my node while I'm syncing, and then my node just ignores them [here](https://github.com/seraphis-migration/monero/blob/29f12ff356d427028ab8edce5043fa4d7c27820b/src/cryptonote_protocol/cryptonote_protocol_handler.inl#L927-L931). I would think peers shouldn't be trying to relay me pool txs while I'm syncing.

# Discussion History
## j-berman | 2025-12-02T22:49:57+00:00
It's also possible for a node to attempt to relay a tx with `reference_block` that is too high, causing the connection to get dropped:

- Node A receives block n+1 while node B's tip is still block n.
- Node A receives a tx with `reference_block=block n+1`, then relays it to node B before node B has finished processing block n+1.
  - This is especially possible when node B is missing some fluffy txs from block n+1, and needs to make a round trip request back to Node A for those missing fluffy txs.
  - Node A might attempt to relay txs with `reference_block=block n+1` to node B before that round trip completes, causing node B to drop the connection.

Checking peers' sync height before relaying would prevent this.

E.g. see the following logs:

```
2025-12-02 22:29:24.795	E tx <hash> included reference block that was too high
2025-12-02 22:29:24.795	E failed to get tree root
2025-12-02 22:29:24.795	I tx used wrong inputs, rejected
2025-12-02 22:29:24.795	I [<IP addr> OUT] Tx verification failed, dropping connection
2025-12-02 22:29:24.795	D [<IP addr> OUT] dropping connection id <uuid> (pruning seed 0), score 0, flush_all_spans 0
```

## j-berman | 2025-12-09T16:33:20+00:00
Logs from @redsh4de in the stressnet channel showing the above `failed to get tree root` & `tx included reference block that was too high`:

<details>
<summary>Show logs</summary>

```
2025-12-09 11:34:55.809 I SYNCHRONIZATION started
2025-12-09 11:35:56.267 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2892796
2025-12-09 11:35:56.268 I id:   <e154aae617841f72a6a33726e3fc7f6250b06d4dccbb8cd0fbc6d0f702c32bd5>
2025-12-09 11:35:56.268 I PoW:  <24874e7a38c7a263fe0cc27cf32d47d89a2709d9d68bb0459638e27c95540000>
2025-12-09 11:35:56.268 I difficulty:   33924
2025-12-09 11:39:42.318 I ###### REORGANIZE on height: 2892796 of 2892796 with cum_difficulty 1146834719106
2025-12-09 11:39:42.318 I  alternative blockchain size: 2 with cum_difficulty 1146834753031
2025-12-09 11:39:43.417 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2892796
2025-12-09 11:39:43.417 I id:   <197bcc7ea35407e11fe84c3d9fa0fd729e1d002e3b4cfe6dd723126381ca6eae>
2025-12-09 11:39:43.417 I PoW:  <85b331141810dda99533679ff310fe7257c6b6459b778a7ad9082a8e7b030100>
2025-12-09 11:39:43.417 I difficulty:   33924
2025-12-09 11:39:43.438 I REORGANIZE SUCCESS! on height: 2892796, new blockchain size: 2892798
2025-12-09 11:39:44.224 I Synced 2892798/2892799 (99%, 1 left, 50% of total synced, estimated 4.8 minutes left)
2025-12-09 11:39:53.875 I [194.58.47.153:28080 OUT] Sync data returned a new top block candidate: 2892798 -> 2892801 [Your node is 3 blocks (6.0 minutes) behind]
2025-12-09 11:39:53.875 I SYNCHRONIZATION started
2025-12-09 11:39:55.280 I [148.63.215.132:28080 OUT] Sync data returned a new top block candidate: 2892798 -> 2892802 [Your node is 4 blocks (8.0 minutes) behind]
2025-12-09 11:39:55.280 I SYNCHRONIZATION started
2025-12-09 11:40:05.885 I Synced 2892799/2892802 (99%, 3 left)
2025-12-09 11:40:17.922 I Synced 2892800/2892802 (99%, 2 left)
2025-12-09 11:40:22.505 I Synced 2892801/2892802 (99%, 1 left)
2025-12-09 11:40:23.613 I Synced 2892802/2892802
2025-12-09 11:40:27.346 I [116.203.98.127:28080 OUT] Sync data returned a new top block candidate: 2892802 -> 2892803 [Your node is 1 blocks (2.0 minutes) behind]
2025-12-09 11:40:27.346 I SYNCHRONIZATION started
2025-12-09 11:40:56.784 I Synced 2892803/2892803
2025-12-09 11:42:43.836 I [208.123.187.151:28080 OUT] Sync data returned a new top block candidate: 2892803 -> 2892804 [Your node is 1 blocks (2.0 minutes) behind]
2025-12-09 11:42:43.836 I SYNCHRONIZATION started
2025-12-09 11:43:06.025 W No incoming connections - check firewalls/routers allow port 28080
2025-12-09 11:43:22.746 I Synced 2892804/2892804
2025-12-09 11:49:58.221 I [83.81.210.152:28080 OUT] Sync data returned a new top block candidate: 2892804 -> 2892806 [Your node is 2 blocks (4.0 minutes) behind]
2025-12-09 11:49:58.222 I SYNCHRONIZATION started
2025-12-09 11:50:19.407 I Synced 2892805/2892806 (99%, 1 left)
2025-12-09 11:50:27.408 E tx <3a7ab11bb48a83a3beacec916c433590ba3ac68fbc1687872e2efd3edc817d65> included reference block that was too high
2025-12-09 11:50:27.408 E failed to get tree root
2025-12-09 11:50:29.020 I [172.103.161.225:28080 OUT] Sync data returned a new top block candidate: 2892805 -> 2892807 [Your node is 2 blocks (4.0 minutes) behind]
2025-12-09 11:50:29.021 I SYNCHRONIZATION started
2025-12-09 11:50:29.542 I Synced 2892806/2892807 (99%, 1 left)
2025-12-09 11:50:32.442 I Synced 2892807/2892807
2025-12-09 11:54:14.838 I [71.31.219.134:28080 OUT] Sync data returned a new top block candidate: 2892807 -> 2892810 [Your node is 3 blocks (6.0 minutes) behind]
2025-12-09 11:54:14.838 I SYNCHRONIZATION started
2025-12-09 11:54:31.334 I Synced 2892808/2892810 (99%, 2 left)
2025-12-09 11:54:53.136 E tx <48688f4ed53584db21a44f81c5a77c4801321588b52e1d44d7336b82c4a84c8c> included reference block that was too high
2025-12-09 11:54:53.136 E failed to get tree root
2025-12-09 11:54:55.254 I Synced 2892809/2892810 (99%, 1 left)
2025-12-09 11:54:55.263 E tx <82beb426a152ea563e55c9327ca1bc412c0ad80fc6408c67d4b5ef4076f2b3a4> included reference block that was too high
2025-12-09 11:54:55.263 E failed to get tree root
2025-12-09 11:54:56.586 I Synced 2892810/2892810
2025-12-09 11:55:53.935 I [116.203.98.127:28080 OUT] Sync data returned a new top block candidate: 2892810 -> 2892811 [Your node is 1 blocks (2.0 minutes) behind]
2025-12-09 11:55:53.936 I SYNCHRONIZATION started
2025-12-09 11:56:42.915 I Synced 2892811/2892811
2025-12-09 12:01:02.828 I [116.203.98.127:28080 OUT] Sync data returned a new top block candidate: 2892811 -> 2892812 [Your node is 1 blocks (2.0 minutes) behind]
2025-12-09 12:01:02.829 I SYNCHRONIZATION started
2025-12-09 12:02:59.420 I ----- BLOCK ADDED AS ALTERNATIVE ON HEIGHT 2892810
2025-12-09 12:02:59.420 I id:   <5db20420d2f9530bdd3b33e8021fbdbd06cde1925ecdac439c45ffe13161f651>
2025-12-09 12:02:59.420 I PoW:  <f7ef6b7895f06e2d67bc37d8b274f9999507a8742b0c6579726ff36950ed0000>
2025-12-09 12:02:59.420 I difficulty:   33588
2025-12-09 12:02:59.813 E tx <c0c06ad18472316918f80e23dffb4cbf702c0622cad9a73fa545144907c5bb0a> included reference block that was too high
2025-12-09 12:02:59.814 E failed to get tree root
2025-12-09 12:03:00.233 E tx <1c09b7726aaac020bd1c44d742d8b463e0d8090da6274d80a81baa6f4f0d845b> included reference block that was too high
2025-12-09 12:03:00.234 E failed to get tree root
2025-12-09 12:03:24.842 E tx <aa3f6cca9a1af71e8ba4b5a78e2b7d8348010e85646dabecbf41c39febcb4f18> included reference block that was too high
2025-12-09 12:03:24.842 E failed to get tree root
2025-12-09 12:03:31.579 E tx <c5c7634086504e33648c967af0f0f29576470770bafc0f1a83d8fda75b4695f9> included reference block that was too high
2025-12-09 12:03:31.579 E failed to get tree root
2025-12-09 12:05:09.868 I ###### REORGANIZE on height: 2892810 of 2892810 with cum_difficulty 1146835193049
2025-12-09 12:05:09.868 I  alternative blockchain size: 2 with cum_difficulty 1146835226641
```

</details>

This is a high priority fix for FCMP++, since the issue seems to be causing the node to fall behind and stay behind for a period of time (edit: and it's a more likely issue to surface with FCMP++, because rings don't reference the latest tip).

## jeffro256 | 2025-12-09T21:25:06+00:00
Could an alternative solution just to make transactions with a too-high reference block a no-drop offense instead of the relayer waiting for a response from the peer?

## j-berman | 2025-12-10T00:29:26+00:00
Compared to #204, I think this case makes more sense to keep as a drop offense, and to just not do it in the first place.

1. Nodes keep track of their peers' heights, so it wouldn't need to be a 2 round thing (although yes, you'd still need to be informed by your peer that the peer has synced).

2. If we were to stop relaying txs in this case, then the edge case where an honest node might get dropped should be so narrow, that a drop seems acceptable (we could even increment a drop score counter).

This is unlike #204 because nodes aren't keeping track of which peers have which key images in their chain, and the case where an honest node might relay key images already spent in the chain seems more likely.

Also! I just checked the code and there already is some logic to do this in the tx relay flow. It doesn't seem to be working as expected though and so could use some further investigation. See `get_out_connections` in `levin_notify.cpp`

It would seem a nice quick win to get this working as expected and save bandwidth versus making it a no drop offense. Although I'm not deeply opposed to making it a no drop offense. I can see an argument for doing that as well.

## Boog900 | 2025-12-12T02:02:25+00:00
AFAICT the `is_synchronized` condition can be true if the node stopped syncing then started syncing again, I think this is what is happening in @redsh4de's logs. Cuprate does it slightly differently by ignoring the txs if we are more than 2 blocks behind the peer.

IMO I think we should ideally do both, make this a no-drop offence and only relay to peers who are close to our height, although AFAIK we don't currently have a method to inform peers that you are synced. I would be worried about nodes failing to track their peer's height correctly and then not sending txs to them. Because tracking the peer's height is inherently just tracking a minimum bound* on their height, ignore incoming txs because the peer is too far ahead is different than not sending txs because the peer is too far behind.  

So I am not really sure if the bandwidth savings are worth it, especially when tx relay will just be hashes, with the check for if the root is in the chain being cheap too. 

> Also! I just checked the code and there already is some logic to do this in the tx relay flow. It doesn't seem to be working as expected though and so could use some further investigation. See get_out_connections in levin_notify.cpp

This is just used for stemming txs, if you are only sending the tx to one peer, you want that peer to be synced so it actually gets the tx. For fluffing this isn't used.


*If the peer switches to an alt-chain their height could drop, however then they are on a different chain anyway so ignoring their tx-pool txs is still valid. 

## j-berman | 2025-12-12T02:33:15+00:00
I'm fine with making it no-drop for the same reasons. I'll make a PR for that soon.

> IMO I think we should ideally do both
> I would be worried about nodes failing to track their peer's height correctly and then not sending txs to them

Fair concern. I'm good with both as well -- it does seem it'll take some heightened care to make sure the height tracking is done correctly/effectively

# Action History
- Created by: j-berman | 2025-10-22T22:14:17+00:00
