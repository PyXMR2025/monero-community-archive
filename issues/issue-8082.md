---
title: 'Enhancement: viewkey-based background refresh for libwallet'
source_url: https://github.com/monero-project/monero/issues/8082
author: hyc
assignees: []
labels: []
created_at: '2021-11-26T08:54:57+00:00'
updated_at: '2025-06-06T17:40:35+00:00'
type: issue
status: closed
closed_at: '2025-06-06T17:40:35+00:00'
---

# Original Description
Just recapping the idea in this bounty https://bounties.monero.social/posts/10/implement-background-wallet-sync-via-view-keys-on-monerujo (also discussed in https://github.com/m2049r/xmrwallet/issues/785)

The idea I'm proposing is to add a background-sync-cache that is separate from the main wallet cache, encrypted with its own secret key, and used to perform refreshes with the wallet viewkey while the main wallet is idle/off. The point is to allow the wallet to stay sync'd with the blockchain without leaving the private spendkey exposed or leaving the main wallet cache in decrypted state.

When the user returns to active use of the wallet and enters their passphrase to unlock/decrypt the main wallet cache, it can then suck in whatever transaction info was recorded in the background-sync-cache, thus avoiding having to wait for a refresh in realtime.

I haven't looked in detail at the wallet cache format recently but I suggest the background-sync-cache file should be written incrementally in append-only fashion, with each transaction record encrypted independently, and in a length-prefixed binary format. This way the refresher doesn't need to constantly re-read and re-encrypt the existing data before writing new records to the file.

The basic functionality to enable periodic background refreshing should be built into libwallet, with hooks to allow the frontend to turn it on and off (e.g. for a smartphone connecting/disconnecting wifi, etc.), set poll interval, etc.

# Discussion History
## busyboredom | 2021-11-26T18:10:27+00:00
Would it be possible to also remain continuously connected to the selected remote node in the background? I've found that even when fully synchronized, wallets can often take upwards of 20 seconds to connect (even when using a private node hosted on the local network). This can be a pain when you're just trying to pay your buddy back for beer and you're both just standing there awkwardly holding your phones, waiting. 

edit: continuously connected as opposed to periodically refreshing, because simply periodically connecting for a quick 1 minute sync every 15 minutes means that when a user finally opens the app, there'd still be a 14/15 chance of the user needing to wait for the connection. 

## selsta | 2021-11-26T18:15:12+00:00
@busyboredom on what kind of hardware is your node hosted? 20 seconds sounds long for local network

## busyboredom | 2021-11-26T18:17:53+00:00
@selsta it's hosted on an ubuntu machine with an SSD, 12GB RAM and a 3GHz quad-core from 2015.

## selsta | 2021-11-26T18:28:39+00:00
@busyboredom Can you start your daemon with `--rpc-ssl disabled` and check if you still have to wait 20 seconds? Connecting takes no longer than 1-2 seconds here on my local and remote node.

## busyboredom | 2021-11-26T18:46:12+00:00
No problem, I gave that a shot just now. After starting my node with that argument, I connected 4 times from cake wallet using the "reconnect" button and got these times:

1. 5 seconds
2. 17 seconds
3. 13 seconds
4. 38 seconds

Also maybe valuable datapoint is that when I simply call rpc endpoints with curl from my desktop, I see a response pretty much immediately, so I'm inclined to think the slowness is in the wallet rather than the node. 

## SamsungGalaxyPlayer | 2021-11-26T19:52:29+00:00
While I like the idea of optionally revealing the view key to a local process on the machine which can scan in the background while the spend key remains locked, we can even get better than this.

The ideal for almost all wallets is to be able to send the view key to a chosen remote node, which can then act as a lightweight server and scan all blocks on the server side. Then, the wallet can request for a status update every time it connects to the remote node. This is preferred in most cases because:

* It avoids the need to have a background process running locally (which is effectively impossible on iOS)
* It saves bandwidth since blocks can be scanned directly at the source (the full node)
* It works even if a phone or computer is off; the server is far more likely to be running 24/7

The main disadvantage is that local notices will be more difficult to display if funds are received if the wallet isn't connected to the remote node. Still, a persistent connection to the remote node listening for relevant transactions is more efficient than keeping an open connection to scan all blocks locally.

Ideally, both options should be made available. But in terms of prioritization, we really should allow remote nodes to function as lightweight servers imo.

## hyc | 2021-11-26T22:28:14+00:00
> While I like the idea of optionally revealing the view key to a local process on the machine which can scan in the background while the spend key remains locked, we can even get better than this.

I think you need to also consider the very serious cons to your suggestion:

- It changes the security and threat model for the nodes. Instead of storing no sensitive data, they become ripe targets for attacks
- It doesn't scale; adding workload to nodes will eventually overload them. Keeping workload distributed to individual wallets is far more scalable.


## SamsungGalaxyPlayer | 2021-11-26T22:38:30+00:00
All of these situations place more stress on nodes. Background connections to remote nodes aren't great either :/

Again, these aren't mutually exclusive features. I want Monero to support both!

If people don't run their own nodes, then the solution described here is better from their UX perspective. It also puts a lot more stress on the nodes though if they request an effectively permanent connection to send all block data continuously instead of only when open. They each have their own different tradeoffs. As someone who runs my own node, I would much rather store my private view key there and push all the hard work to that server.

## hyc | 2021-11-26T22:57:39+00:00
Continually sending blocks is no different from what p2p already does. But the change in sensitivity of data residing on the node is a major difference. IMO it's a huge mistake.

## SamsungGalaxyPlayer | 2021-11-26T22:59:15+00:00
Eh, don't use the feature then :p

## hyc | 2021-11-26T23:00:42+00:00
Cavalierly dismissing security concerns isn't really a good way to proceed here.

## Gingeropolous | 2021-11-27T02:20:48+00:00
random idea, but would it be useful to retrieve and store in this secondary cache a bunch of fake outputs, so even if the cache is compromised, the attacker has to deal that? The users wallet will have to re-check the cache, but its not like its going through the blockchain. 

## tevador | 2021-11-28T15:31:48+00:00
> but would it be useful to retrieve and store in this secondary cache a bunch of fake outputs, so even if the cache is compromised, the attacker has to deal that?

If I understand correctly, the cache contains the private view key, so this wouldn't work.

However, there is a proposal in the [Seraphis addressing schemes](https://github.com/monero-project/research-lab/issues/92) to have a separate keypair for view tags. If this private key is shared with the node, it can only detect a subset of all outputs that contains all of the real outputs owned by the wallet. The amount of leaked information is low because the node still cannot recognize which outputs are real, but the number of outputs the wallet has to check is significantly reduced.

Additionally, this view tag private key has the interesting property that *any* random private key will match some subset of outputs, which makes it possible to use decoy keys.



## r4v3r23 | 2022-01-01T17:48:55+00:00
is this necessary with the upcoming view-tag PR? 

also wallet scan times aren't really an issue, unless you haven't used your wallet in a few months.

## j-berman | 2022-01-08T09:19:19+00:00
@r4v3r23 yes I think this is still necessary. The view tag PR is an improvement, but even a 30-40% improvement (e.g. 30 seconds -> 20 seconds) still leaves room for a better UX, especially on mobile. When a user needs to rescan because they redownload an app e.g., it's still going to be annoying to keep the wallet hot

One implementation detail worth highlighting/discussing: assume a user needs to rescan for their tx's (or spends from a different device), the background cache wouldn't be able to pick up that the user spent outputs (need the spend key for this). 

If a user is using a 3rd party node, and the user returns and queries that 3rd party node with the user's key images (some of which are not yet included in the chain), the 3rd party node can likely use that information to determine outputs that belong to the user*. To avoid this, the cache could store key images (+ tx id + other desired metadata) from *all* tx's that include your received outputs as decoys (one of those tx's would be yours if you've spent, the rest would be other people's tx's). The client can prune the key images that aren't the user's when the user revisits the wallet and loads the spend key. I figure the hook allows a mobile app to turn the background cache off if the device is low on space, or keep the cache capped at some reasonable amount if needed

EDIT: also worth mentioning @tevador 's bloom filter idea over [here](https://gist.github.com/tevador/50160d160d24cfc6c52ae02eb3d17024#gistcomment-4019738) to *potentially* not need to download all key images. But I figure that is more suited for light wallets if it's considered acceptable, since it leaks *some* information, whereas the approach described above does not.

EDIT2: edited to make clear the implementation detail scenario only applies to people using 3rd party nodes. It wouldn't be necessary for people who run their own node, since you're safe just querying for key images from your own node.

*: assume a 3rd party node sees a key image at time t0 that is not yet included in the chain. Assume the key image is then included at time t1. The 3rd party can deduce this tx was constructed by the user, and likely contains a change output back to the user (and deduce any outputs created after t0 are not being spent in the ring). Assume the user then queries for key images again later on, then this change output is included in a tx containing a key image requested by the same user. The 3rd party can then make a strong link back to the prior tx, and deduce the change output was likely spent by the user in that subsequent tx.

## j-berman | 2022-03-04T08:58:01+00:00
@hyc, your thoughts on this update would be much appreciated :)

I've got a preliminary not-too-complex implementation of the background sync working, just re-using the wallet cache and like 95% of the existing scanning code. It syncs without requiring the spend key, storing all received outs *and* tx's that use the user's outs as ring members as it scans the chain. Upon disabling the background sync, the wallet sucks in all that data and sets up wallet cache as normal, prunes the unneeded data once the setup is complete (removes those extra tx's from the cache that use the user's outputs in rings), then just continues scanning normally from the height the background sync left off. It's a pretty nice UX, I must say.

I'm thinking that it *seems* like the background sync cache doesn't absolutely need to live separately from the wallet cache. This is mostly because while syncing, the syncer should also check for spends of *prior* outputs that the wallet cache knew about (and it needs those key images in decrypted state too). So really it seems ok to keep the wallet cache in decrypted state while background syncing, because it should know key images of all unspent outputs in the cache anyway (although granted, seems there is still more potentially sensitive data than just non-spent outputs in the wallet cache file. I'm definitely open to re-considering this).

With this current implementation, it also has the benefit of not needing to close/re-open the wallet cache file when switching between background sync mode and not. But the number of "plausible" spend tx's where outputs are included as ring members may get pretty large for wallets with lots of outputs, especially with larger rings (I can prune all data from tx's needed to get the feature working, but point remains). I imagine exchanges will not really like this feature.

I'm thinking either I should work on the wallet cache migration to LMDB in tandem (as discussed in [#monero-research-lab](https://libera.monerologs.net/monero-research-lab/20220228#c74028-c74032)), or keep building off wallet cache for this feature, because I don't see a huge need to keep the files separate as discussed above. I'm trying to be extra careful to write re-usable code for a migration :) I learn toward re-using wallet cache for now, and work on the LMDB migration after.

## hyc | 2022-03-04T14:23:15+00:00
> It syncs without requiring the spend key, storing all received outs and tx's that use the user's outs as ring members as it scans the chain. 

As you say, exchanges and such would hate this. But it might be OK as a togglable feature. Either via an explicit wallet setting, or implicitly based on the `--trusted-daemon` flag since you obviously don't need it if you actually trust the daemon.

Working with the existing cache has the virtue of being a drop-in feature enhancement. It may mean rewriting extra code if/when anyone get around to doing the LMDB migration but that'll be a future worry.

## j-berman | 2022-03-04T23:46:37+00:00
> But it might be OK as a togglable feature. Either via an explicit wallet setting

This is how it's implemented on my end now :)

> or implicitly based on the --trusted-daemon flag since you obviously don't need it if you actually trust the daemon

I think this would be a nice optimization (assuming you meant *not* needing to save plausible spends, and just fetch key image spent status/associated tx's from the trusted daemon when you have the key images). Figure makes sense to implement both to make the feature available to all, and allow correct behavior switching between syncing from trusted and untrusted daemons. Although if the feature in general was only implemented for trusted daemons, a separate background sync cache would be a lot more worthwhile I think

> It may mean rewriting extra code if/when anyone get around to doing the LMDB migration but that'll be a future worry.

The extra data structure I'm looking at adding is a single key value store. I think it will be a straightforward migration to an LMDB table considering, relative to the rest of the wallet cache. But granted non-0 work still

## hyc | 2025-06-06T17:40:35+00:00
Closed by #8619 

# Action History
- Created by: hyc | 2021-11-26T08:54:57+00:00
- Closed at: 2025-06-06T17:40:35+00:00
