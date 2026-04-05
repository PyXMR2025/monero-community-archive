---
title: Don't use keepalive option with minergate and nicehash.com
source_url: https://github.com/xmrig/xmrig/issues/97
author: dexametazon
assignees:
- xmrig
labels:
- bug
created_at: '2017-09-07T09:21:21+00:00'
updated_at: '2017-11-02T23:32:15+00:00'
type: issue
status: closed
closed_at: '2017-10-06T16:11:31+00:00'
---

# Original Description
hi 
mining is working but dont connect to the pool 
i try in two different server but have problem to connection 
![1](https://user-images.githubusercontent.com/23564495/30155901-5c2d164c-93d3-11e7-8e05-c9e61de43eb2.JPG)


# Discussion History
## xmrig | 2017-09-07T13:25:38+00:00
Don't use keepalive option with minergate, 
Remove `-k` or `--keepalive` from command line options or set `"keepalive": false,` in config file.

- [x] Ignore keepalive option for minergate.com and nicehash.com

## dexametazon | 2017-09-08T10:04:05+00:00
remove --keepalive from command line in config file but still have issue 
![capture](https://user-images.githubusercontent.com/23564495/30206862-b64856f8-94a2-11e7-81c6-1dde862eb126.JPG)


## xmrig | 2017-09-08T13:57:57+00:00
Looks like minergate now use aggressive timeouts and close connection after 2 minutes after last accepted share. Nothing can do on miner side, it only minergate issue also this pool untrusted by community.
Only if you see green **accepted** messages you shares calculated by pool.

## dorimanx | 2017-09-13T05:32:18+00:00
Question, xmrig proxy using nicehash structure to work, do i need to disable keep alive on miners directed to your proxy? Nicehash is ON on miners and no visible issues.

## xmrig | 2017-09-13T16:10:53+00:00
Proxy supports keepalive, but the nicehash.com not. Nicehash is must be ON if you use the proxy.
keepalive not standard extension, but widely supported, prevent to prevent slow workers timeouts. As I know only minergate.com, nicehash.com and some old pool software like cryptonote-universal-pool not support it.

## xmrig | 2017-10-06T16:11:31+00:00
Fixed

## fogoat | 2017-11-01T14:52:06+00:00
@xmrig - I thought cryptonote-universal-pool added support for KeepAlive last year?
 https://github.com/zone117x/node-cryptonote-pool/pull/100

Hard to know what is official repo though...

## xmrig | 2017-11-01T15:25:47+00:00
[cryptonote-universal-pool](https://github.com/fancoder/cryptonote-universal-pool) != node-cryptonote-pool. universal fork does't support keepalve, it trivial change but not present in code.

cryptonote-universal-pool looks abandoned.
Thank you.

## fogoat | 2017-11-02T23:32:15+00:00
So, fancoder is the original cryptonote-universal-pool?

I found another repo that seems to have keep-alive implemented?

https://github.com/clintar/cryptonote-universal-pool/blob/master/lib/pool.js#L1245-L1249

https://github.com/clintar/cryptonote-universal-pool/blob/master/lib/pool.js#L276-L299

I'm not a programmer, so I don't really know for sure.

# Action History
- Created by: dexametazon | 2017-09-07T09:21:21+00:00
- Closed at: 2017-10-06T16:11:31+00:00
