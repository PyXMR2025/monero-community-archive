---
title: DNSResolver.DNSSECFailure test fails on some machines
source_url: https://github.com/monero-project/monero/issues/2172
author: moneromooo-monero
assignees: []
labels:
- tests
created_at: '2017-07-14T08:05:57+00:00'
updated_at: '2018-08-09T06:35:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
That seems to be something dependent on ISP or other network configuration. At least on a Mac build machine.

dnssec-failed.org seems to be a valid domain, with DNSSEC info set up intentionally wrong.

Querying an A record for dnssec-failed.org on some machives gives:
- the expected IPv4 address
- no DNSSEC validation
- no warning that DNSSEC validation failed

So instead of "we got data, but it failed validation", we get "we got data, but it's not proven". It looks to me this is because some DNS server along the way might not support DNSSEC and ignores all it sees about it.

However, asking 8.8.4.4 seems to return no data.

I don't know DNS enough to know what's going on.


# Discussion History
## moneromooo-monero | 2017-07-14T08:27:00+00:00
The internet says that "dig $DOMAIN +dnssec" should include an ad flag if DNSSEC validation got done. I don't get it for either dnssec-failed.org nor getmonero.org on the failing machine. I get it from home for getmonero.org, but not dnssec-failed.org. The getmonero.org result shows the failing machine's DNS machinery is dropping the DNSSEC stuff.

## moneromooo-monero | 2017-07-14T08:45:37+00:00
On the failing machine, if I run "dig @8.8.4.4. getmonero.org +dnssec", I do get the ad flag, whereas I do not get it when omitting @8.8.4.4, so it's the default DNS server that's stripping DNSSEC info.

## moneromooo-monero | 2017-07-14T08:49:17+00:00
And if I run "dig +8.8.4.4 dnssec-failed.org +dnssec", I get some data, which apparently is invalid, as the data ought to be emptied due to the DNSSEC failure. However, since 8.8.4.4 did carry the DNSSEC data for getmonero.org, I'm confused why I'm getting data here.

## fluffypony | 2017-07-14T10:13:21+00:00
So *as I understand it*, which might be entirely incorrect, we're NOT doing DNSSEC checking ourselves. What we're doing is a normal lookup, but passing the "secure" flag. Then, IF the DNS server supports it, it replies with a "yes" or "no" confirming the validity of the DNSSEC data.

***This is entirely the wrong way of doing it***

We should, instead, be checking the DNSSEC records from the actual record up to the root. A DNS server will never (typically) fail to send a particular record type, so getting all the different record types we need for DNSSEC isn't an issue, but relying on the DNS server to do the validation for us is an obvious issue.

If memory serves, we spoke to Unbound about how we do this using libunbound, and I don't know if we ever got a straight answer or if we're meant to just roll our own.

## radfish | 2017-09-26T23:50:01+00:00
Attached console output and pcap from tcpdump while running the unit tests with failing dns server and with successful dns server.

[monero-dns-tcpdump-failing.pcap.log](https://github.com/monero-project/monero/files/1335337/monero-dns-tcpdump-failing.pcap.log)
[monero-dns-tcpdump-public.pcap.log](https://github.com/monero-project/monero/files/1335338/monero-dns-tcpdump-public.pcap.log)
[monero-dns-test.txt](https://github.com/monero-project/monero/files/1335339/monero-dns-test.txt)

tcpdump -nnvvXSs 1514 -r /path/to/pcap



## danrmiller | 2017-12-13T18:09:59+00:00
+tests

## moneromooo-monero | 2018-01-26T19:11:57+00:00
Is this fixed by https://github.com/monero-project/monero/pull/2996 ?

## radfish | 2018-01-27T00:29:21+00:00
Looks like #2996 does not fix it. I'm on 35d5aa36c9b2f4bba169e5947039bf7871649ee1 and I get failure:
   [ RUN      ] DNSResolver.DNSSECSuccess
    /home/redfish/dev/monero-git/src/monero/tests/unit_tests/dns_resolver.cpp:84: Failure
    Value of: valid
      Actual: false
    Expected: true
    [  FAILED  ] DNSResolver.DNSSECSuccess (166 ms)

Same with DNS_PUBLIC=8.8.8.8  and DNS_PUBLIC=0.0.0.0.
But test succeeds with DNS_PUBLIC=tcp

# Action History
- Created by: moneromooo-monero | 2017-07-14T08:05:57+00:00
