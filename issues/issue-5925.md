---
title: --proxy doesn't seem to work
source_url: https://github.com/monero-project/monero/issues/5925
author: ghost
assignees: []
labels: []
created_at: '2019-09-24T03:46:16+00:00'
updated_at: '2020-02-13T11:41:32+00:00'
type: issue
status: closed
closed_at: '2019-10-28T17:09:47+00:00'
---

# Original Description
I'm running 0.14.1.0 like this: `monerod --non-interactive --no-igd --hide-my-port --proxy tor,127.0.0.1:9050,100`

If I do a `lsof -p` on the pid, it has direct connections to nodes and no connection to 127.0.0.1:9050. Didn't see any relevant messages in the logs.

Not sure yet if this is fixed in 0.14.1.2.

Can someone else confirm this behavior? Seems like a pretty major issue given the privacy expectations.

# Discussion History
## vtnerd | 2019-09-24T06:26:34+00:00
It is working as written, although that behavior may not be expected/obvious. The best source to read is the [anonymity networks markdown](https://github.com/monero-project/monero/blob/master/ANONYMITY_NETWORKS.md).

`monerod` is written to work in "dual" mode currently when i2p/tor are configured. P2p control traffic and transaction broadcasting is done over i2p/tor, while everything else is done over the public networks. There are concerns of eclipse attacks and blocking nodes over i2p/tor.

Currently you have to manually specify an i2p/tor node. We are working on seeding nodes - not sure if this will be GUI only or CLI too. Instructions are in that markdown.

## moneromooo-monero | 2019-09-24T13:54:10+00:00
Maybe you should rename --proxy to --txproxy ?

## ghost | 2019-09-24T15:55:19+00:00
Ah, gotcha. I was expecting all outbound traffic would go through the proxy.

Thanks for confirming. Definitely could be better documented in the --help.

## moneromooo-monero | 2019-10-28T16:53:06+00:00
It's now renamed.

+resolved

## ghost | 2019-10-29T16:57:43+00:00
Thank you!

## ghost | 2020-02-09T03:14:09+00:00
I actually think this is broken. My sent transactions seem to never get out of pending if I use --tx-proxy tor,127.0.0.1:9050,100 in 0.15.1. Either that or it's very brittle.

## vtnerd | 2020-02-09T03:21:24+00:00
What is the state of the Tor? Is it initialized? Are there errors printed in the log?

## vtnerd | 2020-02-09T03:25:20+00:00
Nevermind, I know the issue.

There aren't any default seeds, and you most likely haven't explicitly listed a hidden service on the command line. Its a known "issue" as we haven't completely enabled i2p/tor "out-of-the-box". I/we were hoping to come up with a way to spread hidden services over the public network so that new seed nodes would not have to be specified. There are some privacy concerns, and I haven't come up with a good mitigation.

The GUI was considering adding some default nodes in so that it "just-worked" .. @selsta  ?

## ghost | 2020-02-09T04:30:28+00:00
Ah, gotcha. Thank you.

## selsta | 2020-02-13T11:41:31+00:00
> The GUI was considering adding some default nodes in so that it "just-worked" .. @selsta ?

I did not look into I2P / Tor. Maybe @jtgrassie @xmrdsc ?

# Action History
- Created by: ghost | 2019-09-24T03:46:16+00:00
- Closed at: 2019-10-28T17:09:47+00:00
