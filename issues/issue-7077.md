---
title: Weird DNS requests from monerod to moneroPulse
source_url: https://github.com/monero-project/monero/issues/7077
author: hundehausen
assignees: []
labels: []
created_at: '2020-12-04T23:58:35+00:00'
updated_at: '2020-12-10T21:37:19+00:00'
type: issue
status: closed
closed_at: '2020-12-10T21:37:19+00:00'
---

# Original Description
#### Issue description

As I saw in my pihole logs, monerod is making dns requests to [moneroPulse](https://monerodocs.org/infrastructure/monero-pulse/) which is normal, but some DNS queries look weird, because the only contain a dot or the tld. My upstream DNS server has no answer obviously. 
I am not sure if this is intended to act like this or if this has something to do with DNSSEC which I do not have enabled.

#### Steps to reproduce the issue

1.  Log all types of DNS queries (A, AAAA, TXT, DS, DNSKEY)
2.  Start monerod

#### What's the expected result?

- normal A and AAAA queries

#### What's the actual result?

- TXT, DS, DNSKEY queries with just a dot or the tld

#### Additional details / screenshot

<img width="878" alt="monerod_dns" src="https://user-images.githubusercontent.com/25672277/101226449-d31ec180-3694-11eb-956f-df4994926961.png">


# Discussion History
## moneromooo-monero | 2020-12-05T02:01:32+00:00
I don't know about DNSSEC, but this is probably the root.

## moneromooo-monero | 2020-12-10T17:50:10+00:00
From the, er, horse's mouth:

```
<@fluffypony> yes it's the root
<@fluffypony> https://dnssec-analyzer.verisignlabs.com/checkpoints.moneropulse.net
```

## hundehausen | 2020-12-10T21:20:43+00:00
All right thanks. The issue can be closed. 

# Action History
- Created by: hundehausen | 2020-12-04T23:58:35+00:00
- Closed at: 2020-12-10T21:37:19+00:00
