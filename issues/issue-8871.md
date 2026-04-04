---
title: monero-wallet-rpc digest authentication doesn't work
source_url: https://github.com/monero-project/monero/issues/8871
author: trueToastedCode
assignees: []
labels: []
created_at: '2023-05-22T12:32:12+00:00'
updated_at: '2023-05-22T14:01:02+00:00'
type: issue
status: closed
closed_at: '2023-05-22T14:00:36+00:00'
---

# Original Description
it works with curl...
`curl -X POST http://localhost:38088/json_rpc -H 'Content-Type: application/json' -u monero:<password> --digest -v`
```
< HTTP/1.1 200 Ok
< Server: Epee-based
< Content-Length: 111
< Content-Type: application/json
< Last-Modified: Mon, 22 May 2023 12:08:53 GMT
< Accept-Ranges: bytes
< 
{
  "error": {
    "code": -32600,
    "message": "Invalid Request"
  },
  "id": 0,
  "jsonrpc": "2.0"
* Connection #0 to host 192.168.0.31 left intact
}
```
but the same thing with javascript fails... although the Authorization header is correct
```
import fetch from 'node-fetch'
import DigestClient from 'digest-fetch'

const host = 'localhost'
const port = '38088'
const username = 'monero'
const password = '<password>'

const url = `http://${host}:${port}/json_rpc`
const client = new DigestClient(username, password, { algorithm: 'MD5' })
const response = await fetch(url, { 'method': 'post', 'headers': { 'Content-Type': 'application/json' } })
client.lastAuth = response.headers.raw()['www-authenticate'][0]
// Digest qop="auth",algorithm=MD5,realm="monero-rpc",nonce="HvSmkDOsva9+baX7mqizfA==",stale=false
client.parseAuth(client.lastAuth)
const auth = client.addAuth('/json_rpc', { method: 'POST' }).headers.Authorization
// Digest username="monero",realm="monero-rpc",nonce="HvSmkDOsva9+baX7mqizfA==",uri="/json_rpc",qop=auth,algorithm=MD5,response="84f3675b78e05811ee3c0655b8a140d7",nc=00000001,cnonce="afbb9b954b68f37036a5911caa859577"
const response2 = await fetch(url, { 'method': 'post', 'headers': { 'Authorization': auth } })
// status 401
```

It's NOT an invalid Authorization header that's causing the issue.

Thx.

# Discussion History
## trueToastedCode | 2023-05-22T14:00:35+00:00
Ok, the solution is to use a http agent with connection keep-alive.
```
import http from 'node:http'
import fetch from 'node-fetch'
import DigestClient from 'digest-fetch'

const host = 'localhost'
const port = '38088'
const username = 'monero'
const password = '<password>'

const httpAgent = new http.Agent({ keepAlive: true })

const url = `http://${host}:${port}/json_rpc`
const client = new DigestClient(username, password, { algorithm: 'MD5' })
const response = await fetch(url, { 'method': 'post', 'headers': { 'Content-Type': 'application/json' }, agent: (_) => httpAgent })
client.lastAuth = response.headers.raw()['www-authenticate'][0]
client.parseAuth(client.lastAuth)
const auth = client.addAuth('/json_rpc', { method: 'POST' }).headers.Authorization
const response2 = await fetch(url, { 'method': 'post', 'headers': { 'Authorization': auth }, agent: (_) => httpAgent })
// 200
```


# Action History
- Created by: trueToastedCode | 2023-05-22T12:32:12+00:00
- Closed at: 2023-05-22T14:00:36+00:00
