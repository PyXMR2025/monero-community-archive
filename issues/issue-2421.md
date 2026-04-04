---
title: improved Tor support - use onion remote node if Whonix (Tails, Tor, ...) is
  detected
source_url: https://github.com/monero-project/monero-gui/issues/2421
author: adrelanos
assignees: []
labels: []
created_at: '2019-10-28T13:46:10+00:00'
updated_at: '2019-10-28T14:14:28+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
In https://github.com/monero-project/monero-gui/issues/2420 I've noticed that monero GUI uses a hardcoded list of IP addresses in simple mode as monero remote nodes. No progress on syncing after 15 minutes over Tor. Using `monero-gui-v0.14.1.0` on Qubes-Whonix 15 (Debian `buster` based).

I am the founder of Whonix, which I am maintaining at present for more than 7 years. [Whonix](https://www.whonix.org/) (formerly TorBOX) is a Debian GNU/Linuxbased security-focused Linux distribution. It aims to provide privacy, security and anonymity on the internet. With my Whonix hat on, I would like to request the following feature:

If Whonix is detected [1] (prefer) using a list of built-in monero remote nodes available over `.onion` instead. This is because:

* these will provide better connectivity for Tor users.
* obviously won't block Tor users.
* have no SSL vs non-SSL issues (https://github.com/monero-project/monero-gui/issues/2206#issuecomment-512769208).
* provide an extra layer of end-to-end encryption (Tor to onion, "Tor to Tor") 

Monero could detect it is being run inside Whonix by checking for existence of the marker file `/usr/share/anon-dist/marker`.

----

[1] Or any other "anonymity distribution" ("`anon-dist`").  A label which any Linux distribution that routes its traffic over Tor is welcome to use.

# Discussion History
## adrelanos | 2019-10-28T14:14:28+00:00
> No progress on syncing after 15 minutes over Tor.

Now connected. This enhancement would be worthwhile anyhow.

# Action History
- Created by: adrelanos | 2019-10-28T13:46:10+00:00
