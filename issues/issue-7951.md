---
title: 'Option --rpc-access-control-origins doesn''t do anything for monerod '
source_url: https://github.com/monero-project/monero/issues/7951
author: jeffro256
assignees: []
labels: []
created_at: '2021-09-17T23:05:37+00:00'
updated_at: '2021-09-18T04:15:11+00:00'
type: issue
status: closed
closed_at: '2021-09-18T04:15:11+00:00'
---

# Original Description
## Expected behavior:
I expected monerod to send a `Access-Control-Allow-Origin: *` header along with its RPC response for `/get_info` when I specified command-line option `--rpc-access-control-origins '*'`. This header is immensely helpful for enabling browser javascript interaction with monero daemons. 

## Actual behavior:
There was no `Access-Control-Allow-Origin` header. 

## MWE:
1. Run `monerod --rpc-access-control-origins '*' --rpc-login u:p`
2. Run `curl -vvv localhost:18081/get_info --digest --user u:p`

Output of step 2:

    *   Trying 127.0.0.1:18081...
    * TCP_NODELAY set
    * Connected to localhost (127.0.0.1) port 18081 (#0)
    * Server auth using Digest with user 'u'
    > GET /get_info HTTP/1.1
    > Host: localhost:18081
    > User-Agent: curl/7.68.0
    > Accept: */*
    > 
    * Mark bundle as not supporting multiuse
    < HTTP/1.1 401 Unauthorized
    < Server: Epee-based
    < Content-Length: 98
    < Content-Type: text/html
    < Last-Modified: Fri, 17 Sep 2021 22:50:13 GMT
    < Accept-Ranges: bytes
    < WWW-authenticate: Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="Pb3LuMW311dnFLeOCTeWxA==",stale=false
    * Ignoring duplicate digest auth header.
    < WWW-authenticate: Digest qop="auth",algorithm=MD5-sess,realm="monero-rpc",nonce="Pb3LuMW311dnFLeOCTeWxA==",stale=false
    < 
    * Ignoring the response-body
    * Connection #0 to host localhost left intact
    * Issue another request to this URL: 'http://localhost:18081/get_info'
    * Found bundle for host localhost: 0x55f7ae8b8b50 [serially]
    * Can not multiplex, even if we wanted to!
    * Re-using existing connection! (#0) with host localhost
    * Connected to localhost (127.0.0.1) port 18081 (#0)
    * Server auth using Digest with user 'u'
    > GET /get_info HTTP/1.1
    > Host: localhost:18081
    > Authorization: Digest username="u", realm="monero-rpc", nonce="Pb3LuMW311dnFLeOCTeWxA==", uri="/get_info", cnonce="YjFlYWRiYWU4YTM3NWVjNThiMmRlYTU5ZjQ4NWY3NTc=", nc=00000001, qop=auth, response="39ac3c7b9a18a8c8ee9b539caa2a8e07", algorithm="MD5"
    > User-Agent: curl/7.68.0
    > Accept: */*
    > 
    * Mark bundle as not supporting multiuse
    < HTTP/1.1 200 Ok
    < Server: Epee-based
    < Content-Length: 1305
    < Content-Type: application/json
    < Last-Modified: Fri, 17 Sep 2021 22:50:23 GMT
    < Accept-Ranges: bytes
    < 
    .... <THE REST OF THE RESPONSE WAS NORMAL>
    * Connection #0 to host localhost left intact

## System information:

    Monero: 0.17.2.3-release
    OS: Ubuntu 20.04.3
    Arch: x64

# Discussion History
## jeffro256 | 2021-09-18T00:44:49+00:00
I think the relevant code is [here](https://github.com/monero-project/monero/blob/a39b1d56c8835798e2f5e3cc43c33b5f2d8e13da/contrib/epee/include/net/http_protocol_handler.inl#L668).
Note: what's even weirder is that it still doesn't send that header even if I request with an `Origin: http://localhost` header. Also tested on Firefox browser, it blocks the request for CORS reasons. 

## jeffro256 | 2021-09-18T04:15:09+00:00
If anyone else has this issue, you have the specify the origin **exactly** in the `--rpc-access-control-origins` flag. i.e. if the origin is `http://localhost:3000`, then these will NOT work: `http://localhost`, `localhost:3000`, or `http://127.0.0.1:3000`. 

# Action History
- Created by: jeffro256 | 2021-09-17T23:05:37+00:00
- Closed at: 2021-09-18T04:15:11+00:00
