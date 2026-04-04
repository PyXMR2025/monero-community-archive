---
title: 4 failed test cases
source_url: https://github.com/monero-project/monero/issues/1114
author: anonimal
assignees: []
labels: []
created_at: '2016-09-21T23:51:36+00:00'
updated_at: '2018-01-11T00:50:13+00:00'
type: issue
status: closed
closed_at: '2018-01-11T00:49:24+00:00'
---

# Original Description
- Arch Linux "internal" machine against 53e18cafdfb2bf24e8e0f8dd7355733eb31dc1c4
- Internal machine running [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html)
- `/etc/resolv.conf`

```
nameserver 127.0.0.1
nameserver 192.168.0.1
```
- Internal machine behind a Tor transproxy gateway (`192.168.0.1`)

Summary:

```
[----------] Global test environment tear-down
[==========] 620 tests from 57 test cases ran. (35273 ms total)
[  PASSED  ] 616 tests.
[  FAILED  ] 4 tests, listed below:
[  FAILED  ] DNSResolver.DNSSECSuccess
[  FAILED  ] DNSResolver.GetTXTRecord
[  FAILED  ] AddressFromURL.Success
[  FAILED  ] AddressFromURL.Failure
```

Details:

```
[----------] 1 test from boosted_tcp_server
[ RUN      ] boosted_tcp_server.worker_threads_are_exception_resistant
ERROR   {2} {p1} 2016-09-21 23:32:28.788729 [abstract_tcp_server2.inl+783 ::worker_thread] Exception at server worker thread, unknown execption
ERROR   {3} {p1} 2016-09-21 23:32:28.789217 [abstract_tcp_server2.inl+779 ::worker_thread] Exception at server worker thread, what=test 1
ERROR   {3} {p1} 2016-09-21 23:32:28.794630 [abstract_tcp_server2.inl+783 ::worker_thread] Exception at server worker thread, unknown execption
ERROR   {2} {p1} 2016-09-21 23:32:28.795467 [abstract_tcp_server2.inl+783 ::worker_thread] Exception at server worker thread, unknown execption
[       OK ] boosted_tcp_server.worker_threads_are_exception_resistant (14 ms)
[----------] 1 test from boosted_tcp_server (14 ms total)
```

```
[----------] 6 tests from DNSResolver
[ RUN      ] DNSResolver.IPv4Success
[       OK ] DNSResolver.IPv4Success (2375 ms)
[ RUN      ] DNSResolver.IPv4Failure
[       OK ] DNSResolver.IPv4Failure (4090 ms)
[ RUN      ] DNSResolver.DNSSECSuccess
/home/anonimal/monero/tests/unit_tests/dns_resolver.cpp:84: Failure
Value of: valid
  Actual: false
Expected: true
[  FAILED  ] DNSResolver.DNSSECSuccess (64 ms)
[ RUN      ] DNSResolver.DNSSECFailure
[       OK ] DNSResolver.DNSSECFailure (1591 ms)
[ RUN      ] DNSResolver.IPv6Failure
[       OK ] DNSResolver.IPv6Failure (27 ms)
[ RUN      ] DNSResolver.GetTXTRecord
/home/anonimal/monero/tests/unit_tests/dns_resolver.cpp:145: Failure
Expected: (0) != (records.size()), actual: 0 vs 0
[  FAILED  ] DNSResolver.GetTXTRecord (14 ms)
[----------] 6 tests from DNSResolver (8162 ms total)
```

```
[----------] 2 tests from AddressFromURL
[ RUN      ] AddressFromURL.Success
/home/anonimal/monero/tests/unit_tests/address_from_url.cpp:91: Failure
      Expected: 1
To be equal to: addresses.size()
      Which is: 0
/home/anonimal/monero/tests/unit_tests/address_from_url.cpp:99: Failure
      Expected: 1
To be equal to: addresses.size()
      Which is: 0
[  FAILED  ] AddressFromURL.Success (3 ms)
[ RUN      ] AddressFromURL.Failure
/home/anonimal/monero/tests/unit_tests/address_from_url.cpp:113: Failure
Value of: dnssec_result
  Actual: false
Expected: true
[  FAILED  ] AddressFromURL.Failure (14 ms)
[----------] 2 tests from AddressFromURL (17 ms total)
```

Note: `monerod` syncs successfully, wallet _appears_ functional (I have yet to do any txs on this machine).


# Discussion History
## ghost | 2016-12-05T00:19:43+00:00
@anonimal is this still the case with the latest builds?

## anonimal | 2016-12-15T17:44:39+00:00
Yes. Same conditions, same errors (+1):
```
[  FAILED  ] 5 tests, listed below:
[  FAILED  ] DNSResolver.DNSSECSuccess
[  FAILED  ] DNSResolver.DNSSECFailure
[  FAILED  ] DNSResolver.GetTXTRecord
[  FAILED  ] AddressFromURL.Success
[  FAILED  ] AddressFromURL.Failure

 5 FAILED TESTS
```

## anonimal | 2017-02-18T05:56:31+00:00
DNSSEC related? Similar to https://github.com/monero-project/monero/issues/1661?

## dEBRUYNE-1 | 2018-01-08T13:02:27+00:00
@anonimal Is this still relevant?

## anonimal | 2018-01-11T00:50:13+00:00
Yes but the problem is related to both [DNSSEC + Tor](https://trac.torproject.org/projects/tor/ticket/7829) and my setup (I would need to tweak the dnsmasq config or install/configure unbound to use DNSSEC over Tor).

# Action History
- Created by: anonimal | 2016-09-21T23:51:36+00:00
- Closed at: 2018-01-11T00:49:24+00:00
