---
title: armv7 binaries for v0.18.1.1 are missing, 404
source_url: https://github.com/monero-project/monero/issues/8581
author: sethforprivacy
assignees: []
labels: []
created_at: '2022-09-21T17:42:27+00:00'
updated_at: '2022-09-23T14:18:23+00:00'
type: issue
status: closed
closed_at: '2022-09-23T14:14:20+00:00'
---

# Original Description
When attempting to pull the latest binaries for armv7 from https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.1.1.tar.bz2, I get a 404 from all networks I have tested.

All other builds seem present and correct, but this one binary is down for some reason.

# Discussion History
## sethforprivacy | 2022-09-21T17:45:41+00:00
Full curl -vv text in case it's useful:

```bash
tiny in tiny in ~ on  master [!?] ❯ curl -vv https://downloads.getmonero.org/cli/monero-linux-armv7-v0.18.1.1.tar.bz2
*   Trying 157.185.158.194:443...
* Connected to downloads.getmonero.org (157.185.158.194) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.0 (OUT), TLS header, Certificate Status (22):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS header, Certificate Status (22):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Certificate Status (22):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-CHACHA20-POLY1305
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: CN=*.getmonero.org
*  start date: Dec 18 00:00:00 2021 GMT
*  expire date: Dec 18 23:59:59 2022 GMT
*  subjectAltName: host "downloads.getmonero.org" matched cert's "*.getmonero.org"
*  issuer: C=GB; ST=Greater Manchester; L=Salford; O=Sectigo Limited; CN=Sectigo RSA Domain Validation Secure Server CA
*  SSL certificate verify ok.
* TLSv1.2 (OUT), TLS header, Supplemental data (23):
> GET /cli/monero-linux-armv7-v0.18.1.1.tar.bz2 HTTP/1.1
> Host: downloads.getmonero.org
> User-Agent: curl/7.81.0
> Accept: */*
>
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Mark bundle as not supporting multiuse
< HTTP/1.1 404 Not Found
< Date: Wed, 21 Sep 2022 17:44:41 GMT
< Content-Type: text/html
< Transfer-Encoding: chunked
< Connection: keep-alive
< Cache-Control: max-age=14400
< CF-Cache-Status: EXPIRED
< Strict-Transport-Security: max-age=15552000; includeSubDomains; preload
< X-Content-Type-Options: nosniff
< Server: PWS/8.3.1.0.8
< CF-RAY: 74e49c3899bcc46d-EWR
< alt-svc: h3=":443"; ma=86400, h3-29=":443"; ma=86400
< Via: 1.1  PS-JFK-01sXg187:12 (W)[372 404 2], 1.1  am77:2 (W)[444 404 2], 1.1  PSmgmamMIA2nu140:3 (W)[448 404 2]
< X-Px: ms PSmgmamMIA2nu140none,ms am77none,ms PS-JFK-01sXg187none(origin)
< X-Ws-Request-Id: 632b4d88_PSmgmamMIA2it139_63164-62438
<
<html>
<head><title>404 Not Found</title></head>
<body>
<center><h1>404 Not Found</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
* TLSv1.2 (IN), TLS header, Supplemental data (23):
* Connection #0 to host downloads.getmonero.org left intact
```

## binaryFate | 2022-09-23T14:03:39+00:00
Thanks for reporting.
There is a typo in the filename, both for the actual file uploaded to the server and in hashes.txt. Hence, the CI checks didn't see anything wrong.
I'm fixing it now.

## sethforprivacy | 2022-09-23T14:18:22+00:00
Thanks for resolving, binary!

# Action History
- Created by: sethforprivacy | 2022-09-21T17:42:27+00:00
- Closed at: 2022-09-23T14:14:20+00:00
