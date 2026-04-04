---
title: Don't use Google DNS
source_url: https://github.com/monero-project/monero/issues/3146
author: leonklingele
assignees: []
labels: []
created_at: '2018-01-17T11:38:59+00:00'
updated_at: '2018-02-18T19:30:24+00:00'
type: issue
status: closed
closed_at: '2018-02-18T19:30:24+00:00'
---

# Original Description
Google DNS (8.8.4.4) is used to e.g. look up the seed nodes.
Why not use a more trustworthy service and stop feeding Google with the number of running nodes and their IP addresses?

Related to https://github.com/monero-project/monero-site/issues/558 which is also using a Google service.

__EDIT__:
Fix referenced issue.

# Discussion History
## moneromooo-monero | 2018-01-17T11:42:48+00:00
Feel free to suggest a better solution.

Or are you saying it does this by default, rather than be the fallback server when you don't specify one ?

## leonklingele | 2018-01-17T11:50:51+00:00
`monerod` could try to use the local resolver first (if available), and use one (multiple?!) from https://wikileaks.org/wiki/Alternative_DNS as a fallback. These might be of interest as well: https://www.reddit.com/r/privacy/comments/43wcg1/non_logging_free_open_dns_without_censorship/
Is kovri also covering DNS given that it supports UDP?

__EDIT__:
Add more DNS server suggestions.

## moneromooo-monero | 2018-01-17T12:00:56+00:00
monerod uses the default resolver if you don't specify DNS_PUBLIC. You're saying you don't have DNS_PUBLIC set, your default resolver is not google's, and monerod uses google to resolve ?

AFAIK DNS will go over kovri too.

## moneromooo-monero | 2018-01-17T12:07:16+00:00
Thanks, that list is useful. 

## leonklingele | 2018-01-17T12:15:36+00:00
Oh, I just noticed I'm defining `export DNS_PUBLIC=tcp` in my startup script. Commenting out that line "fixes" the issue. The Google IP is hardcoded here: https://github.com/monero-project/monero/blob/35d5aa36c9b2f4bba169e5947039bf7871649ee1/src/common/dns_utils.cpp#L45

## moneromooo-monero | 2018-01-17T12:20:12+00:00
You can set DNS_PUBLIC=tcp://x.y.z.a if your local resolver doesn't work well with DNSSEC.

## moneromooo-monero | 2018-02-02T13:08:47+00:00
https://github.com/monero-project/monero/pull/3225

## anonimal | 2018-02-02T15:13:36+00:00
>AFAIK DNS will go over kovri too.

Yes, but only if a DNS server is running a server tunnel and a client tunnel is configured to connect to said server tunnel and the client tunnels DNS requests through said tunnels and only once UDP-related implementations are resolved - but there is no point in using DNS with kovri because the lookup system is [completely different](https://getmonero.org/resources/moneropedia/address-book.html).

When we integrate, we'll most likely distribute a hardcoded b32 ledger of nodes to connect to, so name resolution won't be necessary. On the other hand, namecoin is also taking an interest in kovri so something may come up in the works regarding naming solutions. TBD.

## moneromooo-monero | 2018-02-02T19:47:08+00:00
For updates and checkpoints, since the data is stored in a TXT record in DNS, how would that work then ? You'd change it to a set of known b32 addresses and actually hit the web servers there ?

## anonimal | 2018-02-02T20:04:27+00:00
>For updates and checkpoints, since the data is stored in a TXT record in DNS, how would that work then ?

I could answer this after more time learning monero. Maybe *not* store in a DNS TXT record? I don't know of an alternate solution at the moment.

>You'd change it to a set of known b32 addresses and actually hit the web servers there ?

I'm assuming so. @fluffypony gave an answer to this at some point, I think.


## moneromooo-monero | 2018-02-18T19:22:49+00:00
+resolved

# Action History
- Created by: leonklingele | 2018-01-17T11:38:59+00:00
- Closed at: 2018-02-18T19:30:24+00:00
