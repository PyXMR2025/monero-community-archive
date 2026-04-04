---
title: '[Feature request] Push-on-update in wallet RPC'
source_url: https://github.com/monero-project/monero/issues/4124
author: lessless
assignees: []
labels: []
created_at: '2018-07-10T10:39:16+00:00'
updated_at: '2022-07-20T20:39:03+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:37:43+00:00'
---

# Original Description
Hi,

There is an obvious demand to scan blockchain for transactions for multiple wallets and from time to time it manifests itself as a feature requests to add multiple wallet support to monero-json-rpc.

What is possible to do instead is to implement push-on-update feature in rpc service which will send a balance update to the provided endpoint. It's much easier to implement and strikes right balance between scalability and engineering complexity.

Of course it was expected as a part of 0mq integration which makes sense because it will work perfect over pub/sub http://zguide.zeromq.org/page:all#Chapter-Advanced-Pub-Sub-Patterns but it's fairly broad topic and a simple HTTP  POST with update details in payload will be enough.

/cc @hyc @moneromooo-monero 

# Discussion History
## xiphon | 2018-07-10T13:46:34+00:00
I'm sure it should be done by running multiple Monero Wallet RPC instances, one for each wallet you want to monitor, and then fetch them for balance updates. 

Is not possible to add support for multiple wallets to Monero Wallet RPC without breaking RPC backward compatibility. 

Although could be implemented as a separate tool, but the use case is too narrow in my opinion.

## lessless | 2018-07-10T14:45:28+00:00
@xiphon running a pool of wallets is a current go to solution and it's not a problem. The real bottleneck in that scenario is a polling which is an I/O heavy process and impose a significant limit on how many monero-wallet-rpc processes it's possible to run per machine. 

Instead, if monero-wallet-rpc can notify service about balance update it will be a real game changer. 

## vtnerd | 2018-07-10T20:49:10+00:00
There was/is an outstanding FFS request to implement PUB/SUB from `monerod`, but the person attached with that request is no longer doing work on Monero. It is something that I will get to eventually, should no one else pick up the task, as its useful for several projects. That will probably get implemented before any PUB/SUB in `monero-wallet-rpc`.

There is also an open-source implementation for a view-only wallet server (i.e. non custodial). It will be compatible with MyMonero iOS and desktop applications. Most of the code is public (but you have to hunt for it) - its not listed anywhere yet as I ran into some DB design issues (it uses LMDB), so some re-working has been done. I've been thinking about PUB/SUB for this wallet server too, as it should reduce load on these view-only servers too.

## lessless | 2018-07-11T06:29:02+00:00
Ah, so I had a wrong assumption that 0mq was integrated in the monero-rpc-service. Anyways, simple POST request  will work and it's an easiest option possible. 

## moneromooo-monero | 2018-09-04T23:03:43+00:00
https://github.com/monero-project/monero/pull/4333 (not RPC, but external process spawn, which can be turned into a RPC call back)

## Cactii1 | 2022-07-20T20:32:19+00:00
> #4333 (not RPC, but external process spawn, which can be turned into a RPC call back)

A suitable workaround has been suggested fr this feature request.

Propose to close this, a new issue can be opened in the future if necessary.

## selsta | 2022-07-20T20:37:43+00:00
Please also see https://github.com/monero-project/monero/blob/master/docs/ZMQ.md, if this isn't enough then comment and I can reopen the issue.

# Action History
- Created by: lessless | 2018-07-10T10:39:16+00:00
- Closed at: 2022-07-20T20:37:43+00:00
