---
title: torsocks'd monerod thread consumes 100% cpu when tor stops
source_url: https://github.com/monero-project/monero/issues/6950
author: joediggs111
assignees: []
labels: []
created_at: '2020-10-29T13:41:13+00:00'
updated_at: '2021-12-11T18:28:32+00:00'
type: issue
status: closed
closed_at: '2021-12-11T18:28:32+00:00'
---

# Original Description
I am using torsocks to launch monerod from systemd.  /usr/lib/systemd/system/monero.service includes:

ExecStart=/usr/bin/torsocks /usr/bin/monerod --config-file /etc/monerod.conf

As mentioned here: https://github.com/monero-project/monero/blob/master/utils/systemd/monerod.service

When I stop or restart the tor service (or if it crashes), even if it restarts succesfully, 1 monerod thread continually thereafter consumes 100% of 1 cpu core.  The problem is only seemingly alleviated by restarting monerod.

Unfortunately I can't just use the anonymous-incoming and tx-proxy options as I want to hide ALL my traffic from my ISP.

Thanks for all your hard work, hopefully someone can reproduce this.

# Discussion History
## garlicgambit | 2020-10-30T19:35:24+00:00
This [issue](https://github.com/monero-project/monero/issues/3779) may be related.  
  
Can you provide more information about your setup? What distro, kernel, torsocks and monero version do you use?  
  
Can you reproduce it without launching from systemd?

## joediggs111 | 2020-10-31T17:22:30+00:00
Thank you for the response garlicgambit.

This is Ubuntu 20.04.1 on x86_64.  5.4.0-52-generic kernel.
Torsocks 2.3.0 from the package torsocks available in regular cannonical repo, along with Tor 0.4.4.5 from same.

Monero is the latest, v0.17.1.1 from getmonero.org (compiled release).

When I launch monero manually with torsocks (not from systemd), and then I stop Tor, everything is fine: regular, minimal cpu usage happens and the log repeatedly says:
PERROR torsocks[88492]: socks5 libc connect: Connection refused (in socks5_connect() at socks5.c:202)

So maybe this is a problem with systemd and/or the monerod.service file.

## garlicgambit | 2020-11-05T19:24:49+00:00
We are able to reproduce this issue.

## selsta | 2021-12-11T18:28:32+00:00
Use `--proxy` from v0.17.3.0: https://github.com/monero-project/monero/releases/tag/v0.17.3.0

# Action History
- Created by: joediggs111 | 2020-10-29T13:41:13+00:00
- Closed at: 2021-12-11T18:28:32+00:00
