---
title: 'Feature: disable AAAA (IPv6) DNS lookups'
source_url: https://github.com/xmrig/xmrig/issues/3201
author: koitsu
assignees: []
labels:
- enhancement
created_at: '2023-01-26T08:32:33+00:00'
updated_at: '2023-01-29T12:02:10+00:00'
type: issue
status: closed
closed_at: '2023-01-28T21:53:28+00:00'
---

# Original Description
**Feature request**

Some of us run IPv4-only networks, including running DNS servers that are IPv4-only (both in transport and in the queries they issue and return (if recursive)).  While we use nameservers that filter AAAA record **responses**, our nameservers still have to handle/answer queries for them; we'd rather clients not submit them at all.

Currently xmrig issues both A and AAAA, and honours whichever is returned first -- unless `--dns-ipv6` is used, or `"dns": { "ipv6": true }` (the latter [is still undocumented](https://github.com/xmrig/xmrig/issues/2883#issuecomment-1019081540), BTW).  It currently does not offer a way to disable AAAA lookups altogether.  What I'm looking for is a configuration directive that stops AAAA lookups entirely from a configuration perspective.  Example below (where the default value would be `true`, obviously):
```
"dns": { 
    "query-aaaa": false
}
```

Please note: I **am not** talking about disabling IPv6 transport (ex. `684d:1111:222:3333:4444:5555:6:77` issuing a DNS query to nameserver `2345:0425:2CA1:0:0:0567:5673:23b5`), I am talking about DNS queries/payload/layer 7.

If this is not possible with the resolver library that xmrig uses, that's fine (close ticket as wontfix), but I wanted to ask about the possibility first.

# Discussion History
## koitsu | 2023-01-26T08:45:39+00:00
Follow-up to my own request:

This likely varies heavily per OS, as OS X vs. Windows vs. Linux (and which libc variant) all behave differently.  Talking about Linux below:

https://docs.libuv.org/en/v1.x/dns.html#api states that `getaddrinfo(3)` libc call is used.  For GNU libc at present, there's no way to disable AAAA lookups.  There has been discussion about this in glibc here: https://bugzilla.redhat.com/show_bug.cgi?id=1027452 (comment 61 is the most useful), but it doesn't appear implemented yet.  Not to mention this `no-aaaa` resolver option wouldn't be something you'd set in xmrig anyway, it would be system-wide via `/etc/resolv.conf`.

Not sure if Windows or OS X offer another way to do this.  I know FreeBSD 13.1 does not.

If you have any other ideas, I'm all ears.  Otherwise it looks like xmrig can't support this (libuv uses getaddrinfo, so not xmrig's fault).

## xmrig | 2023-01-28T15:26:01+00:00
It is possible to disable `A` or `AAAA` lookup, but only via code by replace `AF_UNSPEC` to `AF_INET` (for IPv4 only) or `AF_INET6` (for IPv6 only), overall it's a good idea to make it configurable.

Also xmrig by default only uses `A` records for better compatibility, not whichever is returned first. Only one case to use `AAAA` without `"ipv6": true` is if no `A` records at all.
Thank you.


## xmrig | 2023-01-28T15:26:41+00:00
https://github.com/xmrig/xmrig/blob/master/src/base/net/dns/DnsUvBackend.cpp#L53

## koitsu | 2023-01-28T21:48:01+00:00
> It is possible to disable `A` or `AAAA` lookup, but only via code by replace `AF_UNSPEC` to `AF_INET` (for IPv4 only) or `AF_INET6` (for IPv6 only), overall it's a good idea to make it configurable.

Are you **absolutely 100% sure?**  I am very, very doubtful of that.

AF__INET and AF_INET6 in that context refer to **transport protocol**, not DNS query type/payload.  You linked to https://github.com/xmrig/xmrig/blob/master/src/base/net/dns/DnsUvBackend.cpp#L53 which refers to hints.ai_family.  `hints` refers to an `addrinfo` struct per https://docs.libuv.org/en/v1.x/dns.html#api , and is passed to `getaddrinfo(3)`.  Per `getaddrinfo` man page:

```
     hints is an optional pointer to a struct addrinfo, as defined by ⟨netdb.h⟩:

     struct addrinfo {
             int ai_flags;           /* input flags */
             int ai_family;          /* address family for socket */
             int ai_socktype;        /* socket type */
             int ai_protocol;        /* protocol for socket */
             socklen_t ai_addrlen;   /* length of socket-address */
             struct sockaddr *ai_addr; /* socket-address for socket */
             char *ai_canonname;     /* canonical name for service location */
             struct addrinfo *ai_next; /* pointer to next in list */
     };
```

So this refers to transport protocol / socket type, not DNS query lookup.  Understanding the difference is important.  An IPv4-only system can issue DNS queries for AAAA records (and get AAAA responses) just fine -- it is that behaviour I want to see limited.

If you were to use AF_INET6 on a system which lacks IPv6 transport capability (ex. Linux with kernel flag `ipv6.disable=1` set), you will cause massive breakage: either EPFNOSUPPORT or EAFNOSUPPORT will be returned (I'm not sure which, and not sure what libuv turns these into, if anything).  Edit: it would be EAFNOSUPPORT (`Address family not supported by protocol family`).

**In summary**, I do not think it's possible to achieve what I want in this ticket, because libuv relies on the libc/system resolver.  In the case of Linux and GNU libc, there is no way to control the behaviour (to stop issuing AAAA queries entirely).

So we can resolve this ticket, sadly.

> Also xmrig by default only uses `A` records for better compatibility, not whichever is returned first. Only one case to use `AAAA` without `"ipv6": true` is if no `A` records at all. Thank you.

Understood.

## xmrig | 2023-01-29T04:25:46+00:00
> Are you absolutely 100% sure? I am very, very doubtful of that.

At least on Windows it works, only `A` or `AAAA` returned, not checked on other systems.
Thank you.

## koitsu | 2023-01-29T05:25:16+00:00
> > Are you absolutely 100% sure? I am very, very doubtful of that.
> 
> At least on Windows it works, only `A` or `AAAA` returned, not checked on other systems. Thank you.

Have you tried it on Windows systems which have "Internet Protocol Version 6 (TCP/IPv6)" completely disabled in the Local Area Connection Properties configuration for your NIC?

On Windows, this brings into question what/how libuv behaves.  The libuv API documentation only mentions Linux/UNIX, so I'm not sure how they have implemented this.  Windows and *IX certainly differ in how they behave :)

## SChernykh | 2023-01-29T08:21:30+00:00
@koitsu If you change `AF_UNSPEC` to `AF_INET`, getaddrinfo (which libuv uses) will not even make a DNS request for AAAA records which is how https://github.com/SChernykh/p2pool/issues/229#issuecomment-1406212299 was fixed - and this was on Alpine Linux, not on Windows.

## koitsu | 2023-01-29T11:47:27+00:00
That ticket doesn't do a very good job convincing me.  There are many details omitted.  There are 4 conditions:

* DNS A record lookup using IPv4 (AF_INET) transport to a nameserver
* DNS AAAA record lookup using IPv4 (AF_INET) transport to a nameserver
* DNS A record lookup using IPv6 (AF_INET6) transport to a nameserver
* DNS AAAA record lookup using IPv6  (AF_INET6) transport to a nameserver

Examples of those using `dig` -- which DOES NOT use system resolver functions, I'm only using it as an example of what I'm talking about:

* DNS A record lookup using AF_INET: `dig -4 @8.8.8.8 a www.google.com`
* DNS AAAA record lookup using AF_INET: `dig -4 @8.8.8.8 aaaa www.google.com`
* DNS A record lookup using AF_INET6: `dig -6 @2001:4860:4860::8888 a www.google.com`
* DNS AAAA record lookup using AF_INET6: `dig -6 @2001:4860:4860::8888 aaaa www.google.com`

It may be possible to do `dig -6 @8.8.8.8 {whatever}` as well, depending on the underlying IP stack and 4in6 capability (or the underlying network functions converting an IPv4 address into its IPv6 equivalent (8.8.8.8 == ::ffff:808:808), or possibly through [4in6](https://en.wikipedia.org/wiki/4in6) (IPv4 compatibility within an IPv6-only network).  The inverse of 4in6 is [6to4](https://en.wikipedia.org/wiki/6to4), which allows IPv6 protocol to be encapsulated within IPv4.  Furthermore, AI_V4MAPPED (in flags) changes resolver behaviour as well (where in some implementations, if no AAAA record returns a result, then the resolver falls back to automatically querying for an A record, and if any of those are found, they are returned as IPv4-converted-to-IPv6-addressing-space, since this is specific to AF_INET6).

All of this nonsense is exactly why I do not use IPv6 anywhere.  IPv6-only = fine, IPv4-only = fine, mixed = a hellish nightmare.

The big overlooked fact: **Alpine Linux uses musl libc, not GNU libc.**

* https://alpinelinux.org/posts/Alpine-Linux-has-switched-to-musl-libc.html
* https://wiki.alpinelinux.org/wiki/Running_glibc_programs

How musl chose to implement getaddrinfo(3) is unknown to me, but I do know it DOES NOT behave like GNU libc.  Source:

* https://git.musl-libc.org/cgit/musl/tree/src/network/getaddrinfo.c
* https://git.musl-libc.org/cgit/musl/tree/src/network/lookup_name.c -- see `__lookup_name` and `name_from_dns_search`

Your commit https://github.com/SChernykh/p2pool/commit/c7ba11c607c922d2bd346dff178b9f55fd4e8617 simply falls back to doing IPv4 transport when getaddrinfo() returns a non-zero exit code.  This isn't using libuv either, this is using libc resolver code.

It would be very very interesting to find out what gets reported via that LOGWARN().  I suspect you will find that the errors vary greatly based upon IPv6 transport availability and not so much about DNS payload.

Rather than keep making this ticket longer and longer, I think ultimately what needs to happen for a proper analysis is to launch some systems which have IPv4-only connectivity (IPv6 disabled in kernel), both (IPv4 and IPv6), and IPv6-only connectivity.  And then begin doing actual analysis through `getent` (userland utility with arguments `ahosts`, `ahosts4`, and `ahosts6`) combined with `ltrace` (for libraries), and `tcpdump` (for transport analysis and DNS payload -- let's ignore DNS over TLS etc for now and just assume UDP/TCP port 53) to see what is actually going out the wire + what the underlying userland application gets back from resolver functions.  `strace` would only come in handy if we cared to see how underlying socket calls were behaving.  This would need to be done on an Ubuntu or Debian system (GNU libc), an Alpine system (musl libc), and FreeBSD (BSD libc).  I don't know how Microsoft CRT behaves.  I actually run Linux and FreeBSD and Windows across several bare-metal servers, so I suppose I'd make a good guinea pig for this.  And AFAIK there isn't anyone left using uClibc outside of old routers which aren't mining anyway.  I'm a bit surprised nobody's made a chart of this by now, because there isn't any consistency in it.  It's the thing of nightmares for userland programmers like yourself.

I will see if I can spend some time testing it all and verifying behaviours sometime.  I do not think you need to do this.  I won't be responding past this point unless I have some hard/raw data and a table of behaviours to provide.

## SChernykh | 2023-01-29T12:02:10+00:00
@koitsu libuv uses getaddrinfo internally, you can check the code - it's open source. As for that p2pool fix - hashvault.pro DNS server returns NXDOMAIN for AAAA requests, and LOGWARN shows "try again" or "bad address" error. Falling back to AF_INET makes it skip AAAA request, and it works fine.

# Action History
- Created by: koitsu | 2023-01-26T08:32:33+00:00
- Closed at: 2023-01-28T21:53:28+00:00
