---
title: out_peers setting not respected in monero.conf
source_url: https://github.com/monero-project/monero/issues/4754
author: jlopp
assignees: []
labels: []
created_at: '2018-10-29T19:19:36+00:00'
updated_at: '2018-10-29T22:02:26+00:00'
type: issue
status: closed
closed_at: '2018-10-29T22:02:26+00:00'
---

# Original Description
I've been experiencing unexpected behavior regarding the out_peers setting.

If I put "out_peers=40" in monero.conf and start monerod, it only creates 8 outgoing peers.
I've also tried "out-peers=40" in monero.conf to the same effect.

However, if monerod is running and I set out_peers dynamically, it immediately creates a lot of outgoing peer connections.

So it's unclear how to achieve the desired number of outgoing connections via the conf file

# Discussion History
## xiphon | 2018-10-29T20:38:04+00:00
> If I put "out_peers=40" in monero.conf and start monerod, it only creates 8 outgoing peers.
> I've also tried "out-peers=40" in monero.conf to the same effect.

monerod won't start if it can't parse config file parameter, it will print a error and exit. `out-peers=40` is correct. 

If it doesn't exit on invalid option in the config (`out_peers=40`), that means it didn't try to parse this config at all. Do you have `--config-file=monero.conf` in the command line?



## iDunk5400 | 2018-10-29T21:39:43+00:00
You either have to supply a config file parameter as stated above when using a non-default config file, or use the default config file `bitmonero.conf` (not created by default).

## jlopp | 2018-10-29T22:02:26+00:00
Drat, that explains everything - confirmed. Have you ever considered generating an empty conf file on first startup so that it's more obvious to newbies what the conf file should be named?

# Action History
- Created by: jlopp | 2018-10-29T19:19:36+00:00
- Closed at: 2018-10-29T22:02:26+00:00
