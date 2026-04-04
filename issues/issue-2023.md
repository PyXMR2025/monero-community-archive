---
title: 'Support moneroseed: scheme'
source_url: https://github.com/monero-project/monero-gui/issues/2023
author: sanderfoobar
assignees: []
labels: []
created_at: '2019-03-17T20:16:49+00:00'
updated_at: '2019-09-15T16:38:32+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
> I was playing around with a `moneroseed:` scheme to allow someone to start using monero without relying on the seed modes. Basically, Alice would tell Bob "download monero from this repo, run this setup thingie that sets up moneroseed: handling, then click on this link".

The intent is that someone new to the GUI can get a `moneroseed://a.b.c.d:port` from someone, click the link and the GUI starts via this seed. This bypasses the centralization inherent to using seed servers.

Scheme format is `moneroseed://127.0.0.1` but could be a FQDN as well, it depends on what `--seed-node` from monerod takes.

### To-do's

1. Make OS recognize `moneroseed://` scheme (Windows/Linux/Mac)
2. Handle incoming seed string in the GUI, pass it to QML. Save this string in `appWindow`. 
3. Upon spawning `monerod` from within the GUI, use it as the value when passing `--seed-node` arg in `DaemonManager.cpp`.

Relevant moo branch: https://github.com/moneromooo-monero/bitmonero/commits/moneroseed

xdg-open example:

```
[Desktop Entry]
Name=Monero
GenericName=Monero
X-GNOME-FullName=Monero
Comment=Monero
Keywords=Monero;
Exec=/home/user/src/bitmonero/test-monero.sh %U
Terminal=true
Type=Application
Icon=monero
Categories=GNOME;
MimeType=x-scheme-handler/moneroseed;
StartupNotify=true
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-UsesNotifications=true
```

# Discussion History
## moneromooo-monero | 2019-03-17T20:37:07+00:00
> Save this string in appWindow.persistentSettings, as it probably should be persistent.

It should probably not be. It's meant as an entry point into the network, so you can get more peers via P2P comms. Once you've got that, it's probably best to do the "normal" thing.


## sanderfoobar | 2019-03-17T20:43:45+00:00
Edited.

## sanderfoobar | 2019-07-03T17:34:11+00:00
cross-ref https://github.com/monero-project/monero/issues/5426, waiting on that

## kpcyrd | 2019-09-15T16:38:32+00:00
I think this should always cause some kind of confirmation prompt by the user before using the node to fetch more nodes (or processing any other url handler for that matter). Otherwise any website can redirect to a moneroseed: url and push its own peers into the peerlist and/or try to fingerprint the browser host using p2p connections.

# Action History
- Created by: sanderfoobar | 2019-03-17T20:16:49+00:00
