---
title: Creating Unsigned Transaction Through RPC Takes ~15 Min.
source_url: https://github.com/monero-project/monero/issues/5394
author: yawto
assignees: []
labels: []
created_at: '2019-04-03T20:34:51+00:00'
updated_at: '2019-04-05T15:53:49+00:00'
type: issue
status: closed
closed_at: '2019-04-05T15:53:49+00:00'
---

# Original Description
I'm currently using v0.14.0.2 building from Master at commit b6726aaa6ce8c1aa55bd8a38ef2ea93c01ab3304 from April 1.  When making an RPC call using the `transfer` method Monero-Wallet-RPC takes approximately 15 minutes to return an unsigned transaction. Monero-Wallet-RPC proceeds as normal up until this point in the logs:

```
2019-04-03 19:34:56.431 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:240    adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D

2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:linux-armv7:0.14.0.2:f0e3d82354a9a25776bd2081f2bb1c081a8589ffb783e765ec974d211174236a" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:linux-armv8:0.14.0.2:6558f4cff51a1f25c9979a57fc31edd46caaaeda18c81c76e1dc6c94144525c6" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:linux-x64:0.14.0.2:4dd5cd9976eda6b33b16821e79e671527b78a1c9bfb3d973efe84b824642dd21" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:linux-x86:0.14.0.2:be6ad1de8f16bdeeaf5f4f36f93dcaad97eaa8ff02449b7fffed1abe21605e0e" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:mac-x64:0.14.0.2:255ae412daa04a0e0143325a7763e0574a27e7be86f4ef48582efde9fc07241c" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:win-x64:0.14.0.2:ee68ef8d4b3309cca9e68ee272919c222021804e493c2549c910ef370dfe595a" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:win-x86:0.14.0.2:e471015b4851aef259758fc6a98805655c69db53f29b68362f63dccb496f6e55" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero-gui:install-win-x64:0.14.0.0.exe:4c0ceb81361a4b69bff6cd5a47ef94cfd2992796fb25ca3923aed51d6fcd48bd" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero-gui:linux-x64:0.14.0.0:3d03da7d1c6c6b8f0193729ac4e6b31788ee0aea9890e85770e8d62f3ec2558b" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero-gui:linux-x86:0.14.0.0:b711e0b7222c3c701e3b9aa552fcb9d04425dfea2d04671409ea471f2b2c2dc2" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero-gui:mac-x64:0.14.0.0:b5d8150e5dc5edf4463eecd6a05faab1d868d04947181ef14db25f68eb238ea1" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero-gui:win-x64:0.14.0.0:c23c849a2a970370f2bf7e22aae34f633f51d8490b6130337e5fe9369aff77e0" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:source:0.14.0.2:52a6d3f3694e6e94dc7e3e0904e6937a70a2b3b053a0e0795819cc6513aa9301" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:342    Found "monero:freebsd-x64:0.14.0.2:3fc84b1ca32d99d436d304ee1401e911bbc1b0e1fc0314dc3f879df15e8428f3" in TXT record for updates.moneropulse.org
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:292    Failed to verify DNSSEC record from updates.moneropulse.org, falling back to TCP with well known DNSSEC resolvers
2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:240    adding trust anchor: . IN DS 19036 8 2 49AAC11D7B6F6446702E54A1607371607A1A41855200FD2CE1CDDE32F24E8FB5

2019-04-03 19:35:20.784 [RPC0]  INFO    net.dns src/common/dns_utils.cpp:240    adding trust anchor: . IN DS 20326 8 2 E06D44B80B8F1D39A95C0B0D7C65D08458E880409BBC683457104237C7F8EC8D
```
... 15 minute pause ...

```
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:544    DNSSEC not available for hostname: segheights.moneropulse.co, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:549    DNSSEC validation failed for hostname: segheights.moneropulse.co, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:544    DNSSEC not available for hostname: segheights.moneropulse.se, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:549    DNSSEC validation failed for hostname: segheights.moneropulse.se, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:544    DNSSEC not available for hostname: segheights.moneropulse.org, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:549    DNSSEC validation failed for hostname: segheights.moneropulse.org, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:544    DNSSEC not available for hostname: segheights.moneropulse.net, skipping.
2019-04-03 19:50:21.524 [RPC0]  DEBUG   net.dns src/common/dns_utils.cpp:549    DNSSEC validation failed for hostname: segheights.moneropulse.net, skipping.
2019-04-03 19:50:21.524 [RPC0]  WARNING net.dns src/common/dns_utils.cpp:571    WARNING: no two valid DNS TXT records were received
2019-04-03 19:50:21.654 [RPC0]  DEBUG   wallet.wallet2  src/wallet/wallet2.cpp:3201     Daemon is recent enough, requesting rct distribution
... etc., etc.
```

Running `dig -t TXT checkpoints.moneropulse.se` results in:

```
; <<>> DiG 9.10.3-P4-Ubuntu <<>> -t TXT checkpoints.moneropulse.se
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: SERVFAIL, id: 34759
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4000
;; QUESTION SECTION:
;checkpoints.moneropulse.se.    IN      TXT

;; Query time: 5824 msec
;; WHEN: Wed Apr 03 20:14:38 UTC 2019
;; MSG SIZE  rcvd: 55
```

Checking the stack trace for the Monero-Wallet-RPC process running during the wait gives me this:
```
[pid 31198] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) = 24
[pid 31196] close(25 <unfinished ...>
[pid 31198] fcntl(24, F_GETFL <unfinished ...>
[pid 31196] <... close resumed> )       = 0
[pid 31198] <... fcntl resumed> )       = 0x2 (flags O_RDWR)
[pid 31196] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP <unfinished ...>
[pid 31198] fcntl(24, F_SETFL, O_RDWR|O_NONBLOCK <unfinished ...>
[pid 31196] <... socket resumed> )      = 25
[pid 31198] <... fcntl resumed> )       = 0
[pid 31196] fcntl(25, F_GETFL <unfinished ...>
[pid 31198] connect(24, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("194.150.168.168")}, 16 <unfinished ...>
[pid 31196] <... fcntl resumed> )       = 0x2 (flags O_RDWR)
[pid 31196] fcntl(25, F_SETFL, O_RDWR|O_NONBLOCK <unfinished ...>
[pid 31198] <... connect resumed> )     = -1 EINPROGRESS (Operation now in progress)
[pid 31196] <... fcntl resumed> )       = 0
[pid 31198] select(25, [], [24], NULL, {30, 0} <unfinished ...>
[pid 31196] connect(25, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("193.58.251.251")}, 16) = -1 EINPROGRESS (Operation now in progress)
[pid 31196] select(26, [], [25], NULL, {30, 0} <unfinished ...>
[pid 31197] <... select resumed> )      = 0 (Timeout)
[pid 31197] close(27)                   = 0
[pid 31197] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) = 27
[pid 31197] fcntl(27, F_GETFL)          = 0x2 (flags O_RDWR)
[pid 31197] fcntl(27, F_SETFL, O_RDWR|O_NONBLOCK) = 0
[pid 31197] connect(27, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("89.233.43.71")}, 16) = -1 EINPROGRESS (Operation now in progress)
[pid 31197] select(28, [], [27], NULL, {30, 0} <unfinished ...>
[pid 31199] <... select resumed> )      = 0 (Timeout)
[pid 31199] close(26)                   = 0
[pid 31199] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP) = 26
[pid 31199] fcntl(26, F_GETFL)          = 0x2 (flags O_RDWR)
[pid 31199] fcntl(26, F_SETFL, O_RDWR|O_NONBLOCK) = 0
[pid 31199] connect(26, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("193.58.251.251")}, 16) = -1 EINPROGRESS (Operation now in progress)
[pid 31199] select(27, [], [26], NULL, {30, 0} <unfinished ...>
[pid 31198] <... select resumed> )      = 0 (Timeout)
[pid 31196] <... select resumed> )      = 0 (Timeout)
[pid 31198] close(24 <unfinished ...>
[pid 31196] close(25 <unfinished ...>
[pid 31198] <... close resumed> )       = 0
[pid 31196] <... close resumed> )       = 0
[pid 31198] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP <unfinished ...>
[pid 31196] socket(PF_INET, SOCK_STREAM, IPPROTO_TCP <unfinished ...>
[pid 31198] <... socket resumed> )      = 24
[pid 31196] <... socket resumed> )      = 25
[pid 31198] fcntl(24, F_GETFL <unfinished ...>
[pid 31196] fcntl(25, F_GETFL <unfinished ...>
[pid 31198] <... fcntl resumed> )       = 0x2 (flags O_RDWR)
[pid 31196] <... fcntl resumed> )       = 0x2 (flags O_RDWR)
[pid 31198] fcntl(24, F_SETFL, O_RDWR|O_NONBLOCK <unfinished ...>
[pid 31196] fcntl(25, F_SETFL, O_RDWR|O_NONBLOCK <unfinished ...>
[pid 31198] <... fcntl resumed> )       = 0
[pid 31196] <... fcntl resumed> )       = 0
[pid 31198] connect(24, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("109.69.8.51")}, 16 <unfinished ...>
[pid 31196] connect(25, {sa_family=AF_INET, sin_port=htons(53), sin_addr=inet_addr("109.69.8.51")}, 16 <unfinished ...>
[pid 31198] <... connect resumed> )     = -1 EINPROGRESS (Operation now in progress)
[pid 31196] <... connect resumed> )     = -1 EINPROGRESS (Operation now in progress)
[pid 31198] select(25, [], [24], NULL, {30, 0} <unfinished ...>
[pid 31196] select(26, [], [25], NULL, {30, 0} <unfinished ...>
[pid 31197] <... select resumed> )      = 0 (Timeout)
[pid 31197] close(27)                   = 0
... etc., etc.
```

I have added `nameserver 8.8.8.8` to resolv.conf, as well as setting the `DNS_PUBLIC` env var to `tcp` and then `tcp://8.8.8.8`. None of these changes affected the transaction creation speed. Let me know if I can provide any additional detail. Thanks!

# Discussion History
## moneromooo-monero | 2019-04-03T21:02:17+00:00
Do you have any kind of non default DNS setup ?

## moneromooo-monero | 2019-04-03T21:04:47+00:00
For now, you can replace true with false in src/wallet/wallet2.cpp, here:
static const bool use_dns = true;


## moneromooo-monero | 2019-04-03T21:36:03+00:00
https://github.com/monero-project/monero/pull/5396 adds --no-dns to disable this in case your DNS times out.

## yawto | 2019-04-05T15:53:39+00:00
Using #5396 solved my problem. Thanks so much for your help.

# Action History
- Created by: yawto | 2019-04-03T20:34:51+00:00
- Closed at: 2019-04-05T15:53:49+00:00
