---
title: 'ssl: lack of ECDSA cert with USE_EXTRA_EC_CERT'
source_url: https://github.com/monero-project/monero/issues/6206
author: bjacquin
assignees: []
labels: []
created_at: '2019-12-02T00:26:28+00:00'
updated_at: '2020-05-16T17:33:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Hi,

When monero is built with `USE_EXTRA_EC_CERT`, an ECC certificate is generated during startup if none is specified in configuration.

However this certificate is never presented to the client, even when the client is forcing the use of ECC cipher such as `ECDHE-ECDSA-CHACHA20-POLY1305`

```
$ openssl s_client < /dev/null -connect 127.0.0.1:18089 -tls1_2 -cipher ECDHE-ECDSA-CHACHA20-POLY1305
CONNECTED(00000003)
139729583916864:error:14094410:SSL routines:ssl3_read_bytes:sslv3 alert handshake failure:ssl/record/rec_layer_s3.c:1544:SSL alert number 40
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 7 bytes and written 142 bytes
Verification: OK
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID:
    Session-ID-ctx:
    Master-Key:
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1575233552
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
    Extended master secret: no
```

I am currently doing some investigation it, adding an issue so I can refer it in later PR.

# Discussion History
## moneromooo-monero | 2020-05-16T16:12:03+00:00
Did you get anywhere ?

## bjacquin | 2020-05-16T17:33:41+00:00
> Did you get anywhere ?

I've distracted from this lately, I might be able to get back to the investigation next week.

# Action History
- Created by: bjacquin | 2019-12-02T00:26:28+00:00
