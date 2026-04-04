---
title: 'Vulnerability Report (3) : Insecure Transportation Security Protocol Supported
  (TLS 1.0)'
source_url: https://github.com/monero-project/meta/issues/336
author: raza5402
assignees: []
labels: []
created_at: '2019-04-27T11:26:03+00:00'
updated_at: '2024-12-21T04:02:22+00:00'
type: issue
status: closed
closed_at: '2019-04-27T15:20:30+00:00'
---

# Original Description
Hi team,

I have found this vulnerability in your website : https://ww.getmonero.org

Summary:

ww.getmonero.org
![monero tls](https://user-images.githubusercontent.com/49895674/56849056-8e218f00-68a4-11e9-9799-b74d5ce2c9e3.png)
 still support TLS 1.0 protocol which has several flaws.

Vulnerability Type:

With a SSL security scanner i was able to identify that an insecure
transportation security protocol (TLS 1.0) is still supported by your
web server.

Vulnerability Description: 

TLS 1.0 has several flaws. An attacker can cause connection failures
and they can trigger the use of TLS 1.0 to exploit vulnerabilities
like BEAST (Browser Exploit Against SSL/TLS).

Websites using TLS 1.0 will be considered non-compliant by PCI after
30 June 2018.

How to FIX :

For Apache, adjust the SSLProtocol directive provided by the mod_ssl
module. This directive can be set either at the server level or in a
virtual host configuration.

SSLProtocol +TLSv1.1 +TLSv1.2

For Nginx, locate any use of the directive ssl_protocols in the
nginx.conf file and remove TLSv1.

ssl_protocols TLSv1.1 TLSv1.2;

For Microsoft IIS, you should make some changes on the system registry.
1) Click on Start and then Run, type regedt32 or regedit, and then click OK.
2) In Registry Editor, locate the following registry key or create if
it does not exist:

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS
1.0\
3) Locate a key named Server or create if it doesn't exist.
4) Under the Server key, locate a DWORD value named Enabled or create
if it doesn't exist and set its value to "0".

Supporting Material/References:

How to disable TLS v1.0
OWASP - Insecure Configuration Management
OWASP - Insufficient Transport Layer Protection
How to disable PCT 1.0, SSL 2.0, SSL 3.0, or TLS 1.0 in Internet
Information Services
IIS Crypto is a free tool that gives administrators the ability to
enable or disable protocols, ciphers, hashes and key exchange
algorithms on Windows Server 2003, 2008 and 2012
Date Change for Migrating from SSL and Early TLS
Browser Exploit Against SSL/TLS Attack (BEAST)


Impact:

Attackers can perform man-in-the-middle attacks and observe the
encryption traffic between your website and its visitors.

POC Link: https://www.ssllabs.com/ssltest/analyze.html?d=ww.getmonero.org&s=104.24.27.115&latest

I Hope that you will fix this issue as soon as possible. Looking forward to hear from you. Thank you

Sincerely,
Ali Raza

# Discussion History
## fluffypony | 2019-04-27T15:20:30+00:00
No.

## raza5402 | 2019-04-27T15:21:42+00:00
Please let me know what do you mean by no? please provide appropriate answer

## raza5402 | 2019-04-27T15:22:50+00:00
I have provided all the proofs and links, you may check from that provided link and can satisfy your self, my findings are right

## fluffypony | 2019-04-27T15:23:31+00:00
If you had any security knowledge at all you would realise that our TLS is terminated by CloudFlare, not by us.

## fdzdev | 2024-12-21T04:02:20+00:00
dang why so mean? @fluffypony lame, huge L

# Action History
- Created by: raza5402 | 2019-04-27T11:26:03+00:00
- Closed at: 2019-04-27T15:20:30+00:00
