---
title: 'Privacy: DNS leak when running with torsocks'
source_url: https://github.com/monero-project/monero/issues/6218
author: leonklingele
assignees: []
labels: []
created_at: '2019-12-05T11:44:27+00:00'
updated_at: '2020-02-09T22:17:09+00:00'
type: issue
status: closed
closed_at: '2020-02-09T22:17:09+00:00'
---

# Original Description
It seems `monerod` tries to connect to the [default DNS servers](https://github.com/monero-project/monero/blob/633f14b9766f0aa9786147c0c151322380bb5c18/src/common/dns_utils.cpp#L45-L52) directly (i.e. circumventing the Tor SOCKS proxy) when running it with `torsocks`:

```sh
# Running with torsocks
export DNS_PUBLIC=tcp
torsocks "$MONEROD" \
    --p2p-bind-ip 127.0.0.1 \
    --rpc-bind-ip 127.0.0.1 \
    --no-igd \
    --hide-my-port \
    --db-sync-mode safe \
    --check-updates disabled \
    --disable-dns-checkpoints

# Now observe DNS traffic
```

Related: https://github.com/monero-project/monero/issues/3128

# Discussion History
## moneromooo-monero | 2019-12-05T11:59:33+00:00
monerod tries to do *everything* directly. That's the point of torsocks, it intercepts normal TCP calls to route them through Tor. Are you saying the DNS ones are missed when using TCP mode ?
The second example does not have torsocks btw, forgot ?

## leonklingele | 2019-12-05T12:07:45+00:00
> it intercepts normal TCP calls to route them through Tor.

It doesn't for those TCP DNS requests, i.e. circumventing the Tor proxy, that was my point :) 

> The second example does not have torsocks btw, forgot ?

I've removed the second example (using `--tx-proxy`) as I was misunderstanding its use case.

## moneromooo-monero | 2019-12-05T12:56:41+00:00
torsocks docs hint it could be the call is a direct syscall, which it cannot intercept.
In any case, the DNS queries are for the update mechanism and the checkpoints, they're not really needed so you can use "--disable-dns-checkpoints" and "--check-updates disabled", which should stop any DNS request (can you confirm ?). I'll add this to the README too for now.

## moneromooo-monero | 2019-12-05T13:00:09+00:00
Wait, you have these. It shouldn't do any extra DNS requests in the first place...

## moneromooo-monero | 2019-12-05T13:08:46+00:00
I'm not super familiar with this, but dumping traffic on port 53, I don't see anything when running with torsocks (and I did not use "--disable-dns-checkpoints" nor "--check-updates disabled"). I didn't set DNS_PUBLIC either, just: torsocks ./build/release/bin/monerod --no-igd --p2p-bind-ip 127.0.0.1 --rpc-bind-ip 127.0.0.1 --hide-my-port
To scan for DNS traffic, I used: tcpdump 'tcp port 53'
What do you use, and is this missing some traffic ?
I do see DNS traffic when I run it without torsocks.

## leonklingele | 2019-12-05T13:55:33+00:00
I was using tcpdump too. `monerod` is trying to resolve the [seed nodes](https://github.com/monero-project/monero/blob/411f1b0ee30f1d424621eb856841dc82d2f161c2/src/p2p/net_node.h#L282-L288).

> is this missing some traffic ?

What do you mean by that?

BTW, I'm on Mac OS, Monero 6def88ad405b39f632a91afa3aacbb92ecc63c1f and Torsocks 2.3.0

## moneromooo-monero | 2019-12-05T14:04:32+00:00
I meant, is my usage doing to capture only part of it. Like, can DNS traffic sometimes go not through 53, etc. That is, do you see anything in my command which would miss some traffic you're seeing.

torsocks 2.3.0 here, on master plus various changes but none relating to DNS.

But I've just realized that I'm on Qubes, which has a funky DNS forwarder, so quite possibly port 53 is not getting the traffic it would ohterwise have...


## leonklingele | 2019-12-05T17:38:22+00:00
Your command looks just fine, I'm using it exactly the same way.

> I'm on Qubes

That indeed might be the "problem" here ;)

## ghost | 2019-12-05T20:14:54+00:00
~~torsocks will likely redirect dns queries to the tor dns, rather then the normal ones defined in `resolved.conf`, for resolving `.onion` addresses at least.~~ This is probably not how torsocks works, too much alcohol, please ignore.

## ghost | 2019-12-05T20:18:17+00:00
~~Also it's probably not a leak, since the tor dns still needs to consult local dns. It's probably just normal upstream forwarding, since these are not `.onion` addresses.~~ Actually, ignore this.

## hyperreality | 2019-12-09T16:51:00+00:00
I can't reproduce this on Debian 10, DNS requests are forwarded through torsocks the correct way. @leonklingele can you give more details about your setup? 

As a side note, it's weird how when you directly query seeds.moneroseeds.* URLs, you get a SERVFAIL, but querying the domain directly (without the subdomain) gives you the list of nodes.

## leonklingele | 2020-02-08T10:27:25+00:00
Sorry for the delay.

So far I've only tried to reproduce this on OS X (haven't updated the OS in a quite while). I'm launching monerod using a script (see https://github.com/monero-project/monero/issues/6218#issue-533300053) which has been working fine before, i.e. without leaking DNS queries.

The leaking DNS queries are issued right after logging `Using public DNS server(s): [..]` if that's of any use (I use Little Snitch, a firewall for OS X, which halts the queries as long as they weren't confirmed using a visual GUI prompt).

What has been tested so far:

- Switched back to an older version of torsocks which I was using when DNS leaks were not occurring (to no avail)
- Tried to compile older versions of monerod, but lack some outdated compile-time dependencies (mainly `boost`) which have been upgraded since. I will try to install the older ones again asap

I also found an old version (`monerod-v0.11.1.0-master-35d5aa36` compiled on `12 Jan  2018`) which works fine and doesn't leak anything, so it's either a new bug inside monerod or in one of its updated dependencies.

## moneromooo-monero | 2020-02-08T13:12:47+00:00
If you use torsocks, it can't be a monerod bug since the point of torsocks is to intercept *non tor* requests, so monerod is meant to connect normally without tor.


## leonklingele | 2020-02-09T20:56:44+00:00
> it can't be a monerod bug

Yes it can. It is possible to somehow bypass the Tor SOCKS proxy when using `torsocks`, I've seen that happening before.

__EDIT__:

See https://trac.torproject.org/projects/tor/wiki/doc/torsocks

```
DNS: DNS requests safe for Tor?
           N - The application is known to leak DNS requests when used with torsocks.
           Y - Testing has shown that application does not leak DNS requests.
```

## leonklingele | 2020-02-09T22:01:27+00:00
Interesting, removing local `libunbound v1.9.6` headers (which makes monero compile with https://github.com/monero-project/unbound/tree/0f6c0579d66b65f86066e30e7876105ba2775ef4) has resolved the issue.
The DNS leak was introduced to `libunbound` between `v1.9.4` and `v1.9.5`. Starting a bisect now.

## leonklingele | 2020-02-09T22:17:09+00:00
Actually, the issue was introduced between the `v1.9.4` and `v1.9.5` release of Homebrew's `unbound`. It is caused by compiling it with `--enable-tfo-client`, an option to enable TCP Fast Open. Will file an issue on the torsocks tracker.

Sorry for the abuse.

# Action History
- Created by: leonklingele | 2019-12-05T11:44:27+00:00
- Closed at: 2020-02-09T22:17:09+00:00
