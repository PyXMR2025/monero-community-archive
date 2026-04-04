---
title: Tighten up torsocks usage recommendations in README.md
source_url: https://github.com/monero-project/monero/issues/844
author: iamsmooth
assignees: []
labels: []
created_at: '2016-05-17T20:23:03+00:00'
updated_at: '2022-04-08T11:23:39+00:00'
type: issue
status: closed
closed_at: '2022-04-08T11:23:28+00:00'
---

# Original Description
There are conflicting reports whether TORSOCKS_ALLOW_INBOUND=1 is required (may be system-dependent). Based on the documented behavior of that option (allowing external connections) it is certainly not needed and even potentially dangerous since an external connection could bypass Tor.

The readme should be updated to remove the TORSOCKS_ALLOW_INBOUND=1 option from the standard instructions and advise adding it only if needed, or we should figure out where it is actually need and provide system-dependent usage instructions.


# Discussion History
## moneromooo-monero | 2016-06-10T09:41:49+00:00
I just tried again on Fedora 21, x86_64, Tor 0.2.6.10, torsocks 2.1.0.
With TORSOCKS_ALLOW_INBOUND=1, the wallet can connect/refresh.
Without TORSOCKS_ALLOW_INBOUND=1, the wallet cannot and times out.
All the pieces running on the same VM.


## anonimal | 2016-07-12T20:07:13+00:00
I can confirm @moneromooo-monero's results on both Arch and Ubuntu LTS.

torsocks appears to use simple wrappers for [listen](https://gitweb.torproject.org/torsocks.git/tree/src/lib/listen.c) and [accept](https://gitweb.torproject.org/torsocks.git/tree/src/lib/accept.c) and all the `ALLOW_INBOUND`-related code appears to be legitimate; so I don't know why we need to make the exception here with bitmonero (though I haven't spent much time with the code).

Related note: bitmonerod cannot sync when using [proxychains-ng](https://github.com/rofl0r/proxychains-ng) regardless if `--p2p-bind-ip` is bound to localhost or not. I use proxychains-ng all the time, especially for localhost-bound applications (to prevent leaks), so, AFAICT, these issues appear to be specific to bitmonero.


## selsta | 2022-04-08T11:23:28+00:00
`torsocks` isn't recommended anymore, see the `--proxy` or `--tx-proxy` flag.

# Action History
- Created by: iamsmooth | 2016-05-17T20:23:03+00:00
- Closed at: 2022-04-08T11:23:28+00:00
