---
title: How to prevent the ability to determine what IP address belongs to what wallet
  address when mining
source_url: https://github.com/xmrig/xmrig/issues/2502
author: Joe23232
assignees: []
labels: []
created_at: '2021-07-30T14:34:30+00:00'
updated_at: '2021-08-01T01:50:52+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Using `xmrig` when mining (for example I am using [QRL](https://wallet.theqrl.org/) and I am using [qrl mining ocean](https://qrl.miningocean.org/) for my mining pool), if not using `--tls` flag, I understand that people are able to determine my IP address belongs to which wallet address.

If a conneciton supports SSL and I decided to use `--tls` flag, would it prevent people from being able to determine my IP address and which wallet address does it belong to?

# Discussion History
## Spudz76 | 2021-07-31T21:33:42+00:00
If you also use the `tls-fingerprint` option it will make sure there is no middleman/proxy going on.  Connect once with TLS and the connection message outputs the fingerprint string.  As long as you're absolutely sure it's the same fingerprint as people on open/free networks also receive (verify with a few people to be sure), then it's legit.

You would have to reset this fingerprint if the pool certificate expires and is renewed/regenerated, it would then have a new (but still official) fingerprint.  And miners would quit connecting until you update, just like they would refuse to connect via any inspection gateway situation where it's recrypted.

Then all they know is you're connecting to a pool and talking to it, but not anything you say (wallet ids or exactly what you're doing).  This could be enough to at least pin mining activity on you even if they can't know your wallet, and then if they 100% know you're mining and you won't give them your wallet-id they could just lean on you legally until you do.

To hide everything including where-to you're connecting, try TOR or some VPN (that you also trust of course).  And run SSL on top of that as well.

## Joe23232 | 2021-08-01T01:50:52+00:00
@Spudz76 Thanks mate for clarifying this with me :)

# Action History
- Created by: Joe23232 | 2021-07-30T14:34:30+00:00
