---
title: Daemon recurring error message
source_url: https://github.com/monero-project/monero/issues/9314
author: zampano3
assignees: []
labels:
- daemon
created_at: '2024-05-01T04:59:33+00:00'
updated_at: '2025-12-29T01:23:43+00:00'
type: issue
status: closed
closed_at: '2025-12-29T01:23:43+00:00'
---

# Original Description
This error continues to appear when monerod is running:
```
2024-04-30 12:49:42.949	E Unable to send transaction(s) via Dandelion++ stem
2024-05-01 01:22:35.811	E Unable to send transaction(s) via Dandelion++ stem
2024-05-01 01:24:37.642	E Unable to send transaction(s) via Dandelion++ stem
```
I run a node with port 18080 open. Does anyone know what this means, or how it can be resolved?

# Discussion History
## selsta | 2024-05-01T12:46:27+00:00
If it only shows up once in a while you can ignore it. I sometimes see it on my nodes too. The transaction will still end up getting propagated in the Dandelion++ fluff phase.

@vtnerd can you explain in detail what could cause this?

## vtnerd | 2024-05-01T16:14:15+00:00
This should only happen when you don't have any outbound connections. If you have outbound connections, then there is a bug somewhere in the D++ logic.

## zampano3 | 2024-05-01T18:28:47+00:00
> This should only happen when you don't have any outbound connections. If you have outbound connections, then there is a bug somewhere in the D++ logic.

I can confirm I do have outbound connections

## zampano3 | 2024-05-01T18:30:05+00:00
Sorry, I didn't mean to close this

## vtnerd | 2024-05-02T23:45:37+00:00
Did you check for outbound connections when the errors appeared or later? We still don't have confirmation of a bug unfortunately.

## zampano3 | 2024-05-03T00:24:12+00:00
> Did you check for outbound connections when the errors appeared or later? We still don't have confirmation of a bug unfortunately.

I check the status frequently, and I recieved confirmation of inbound and outbound connections before and after the errors appeared. It hasn't appeared again since filing this issue.

## selsta | 2024-05-03T02:38:01+00:00
@vtnerd what happens when the randomly selected peer in the stem phase disconnects? could this cause the message?

## vtnerd | 2024-05-03T16:32:06+00:00
The Dandelion++ code should select a replacement peer, if available.

## toncho6501 | 2024-05-25T13:58:25+00:00
fake   monero

## thisIsNotTheFoxUrLookingFor | 2024-08-14T10:52:57+00:00
> fake monero

What is real monero then?

## selsta | 2025-12-29T01:23:38+00:00
Closing as it's not clear if there is a bug here and OP did not run into this again.

# Action History
- Created by: zampano3 | 2024-05-01T04:59:33+00:00
- Closed at: 2025-12-29T01:23:43+00:00
