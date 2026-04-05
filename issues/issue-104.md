---
title: How to point multiple xmrig miners to the monero daemon instead of a pool?
source_url: https://github.com/xmrig/xmrig/issues/104
author: ghost
assignees: []
labels: []
created_at: '2017-09-08T14:41:20+00:00'
updated_at: '2021-06-05T03:07:57+00:00'
type: issue
status: closed
closed_at: '2017-10-02T11:55:36+00:00'
---

# Original Description
Hello, 

I'd like to solo mine. I know you can do it with the default daemon miner but I have multiple computers and I don't want to maintain a node on each one of them. So I'd like to run the daemon on one of the computers and set up xmrig on the rest of the machines to point to the daemon. Any suggestions on how to do that?

Your help is greatly appreciated. Thanks.

# Discussion History
## xmrig | 2017-09-08T15:27:10+00:00
There not too much options:
* Setup own pool.
* Something like that https://github.com/sammy007/monero-stratum
* Use solo mining on this pool https://xmrpool.net

## kilid | 2018-10-06T21:52:26+00:00
with the new XMR GUI wallet solo mining is added there I think its possible to forward rigs hashing power to that node if they are all connected on same local area network 

## trasherdk | 2018-10-09T11:18:10+00:00
@lexphor I have tested https://github.com/sammy007/monero-stratum, and it works OK.

@kilid XMR GUI Wallet mining works only on a local daemon. Just like mining in the console wallet.
You can connect to a remote wallet, but can't start mining remote.

## kilid | 2018-10-09T11:24:42+00:00
@trasherdk  https://github.com/sammy007/monero-stratum 

nice I would love to try that "be your own pool " did you install it on local server machine next to your rigs or you had to rent a VPS ? 

## trasherdk | 2018-10-14T10:47:58+00:00
@kilid 

I'm mining on a Windows 10 x64, xmr-stak.
And running monero-tratum and monerod on an old laptop, running Slackware 14.2 x64, 2GB RAM.
No problem.

## krisztian-zagonyi | 2021-05-31T16:18:39+00:00
Is there any newer way to do that?
Is that still working? Worth a try? :)
Thank you.

## SChernykh | 2021-05-31T16:27:16+00:00
@krisztian-zagonyi You can point https://github.com/xmrig/xmrig-proxy to your monerod and point all xmrig miners to this proxy.

## krisztian-zagonyi | 2021-05-31T17:30:53+00:00
Thanks for you reply. :)
Proxy config.json:
`{
    "autosave": true,
    "donate-level": 5,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "coin": "monero",
            "url": "127.0.0.1:18081",
            "user": "44G-XXXX",
            "daemon": true
        }
    ]
}`
Xmrig config.json:
`{
    "autosave": true,
    "donate-level": 5,
    "cpu": true,
    "opencl": false,
    "cuda": false,
    "pools": [
        {
            "url": "0.0.0.0:3333"
        }
    ]
}`
I created both jsons with https://xmrig.com/wizard
Currently I see my gui wallet hash is: 183 with 1 thread.
My proxy is connected to the local daemon and I see my worker but with 0.00kH/s.
My xmrig is connected to proxy with 2000h/s.
Is that correct?
Is my xmrig miner mining to my solo mining gui wallet? just because I cannot see the hash on the wallet nor on proxy.
I am sure something not correct. But can you help me?
Thanks for your help. :)

## SChernykh | 2021-05-31T17:35:27+00:00
Wallet only shows its own hashrate. You should check xmrig and proxy hashrates. Proxy shows approximate hashrate based on how many accepted results xmrig submits to it. If the proxy difficulty is too high, it'll show 0 and occasionally something more than 0.

## krisztian-zagonyi | 2021-05-31T19:19:35+00:00
Thank you. So you think my config is good? :)

## SChernykh | 2021-05-31T19:30:19+00:00
`"url": "0.0.0.0:3333"` is not correct, you should use your proxy external IP in xmrig config.

## krisztian-zagonyi | 2021-05-31T20:05:49+00:00
I am using my public IP, and opened the 3333 port on my router, but connect error: "operation canceled" :/

## trasherdk | 2021-06-05T03:07:57+00:00
Another option, to mine with multiple xmrig, against own monerod is [jtgrassie / monero-pool](https://github.com/jtgrassie/monero-pool) 

# Action History
- Created by: ghost | 2017-09-08T14:41:20+00:00
- Closed at: 2017-10-02T11:55:36+00:00
