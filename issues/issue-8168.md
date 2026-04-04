---
title: Don't require --rpc-login with --rpc-access-control-origins
source_url: https://github.com/monero-project/monero/issues/8168
author: woodser
assignees: []
labels: []
created_at: '2022-02-05T18:06:10+00:00'
updated_at: '2022-04-29T03:09:42+00:00'
type: issue
status: closed
closed_at: '2022-04-29T03:09:42+00:00'
---

# Original Description
This issue requests removing the requirement to use RPC authentication when starting monerod with `--rpc-access-control-origins`.

That way, public nodes may serve browser clients.

# Discussion History
## jeffro256 | 2022-02-19T18:46:19+00:00
This would be great! I've run into this issue myself

## jeffro256 | 2022-02-19T19:55:31+00:00
@woodser check out the above PR. There may be some security implications with allowing --rpc-access-control-origins with public nodes, but I think that would mostly be a concern for the browser applications, not the daemon operators. In that case, the incumbent security concerns of using an untrusted node overshadow what issues --rpc-access-control-origins bring into the equation, 

## woodser | 2022-03-08T13:29:16+00:00
Great. The PR should be opened on release-0.17 to be incorporated into the next release, too.

## jeffro256 | 2022-03-27T18:52:16+00:00
@woodser done: #8227 

# Action History
- Created by: woodser | 2022-02-05T18:06:10+00:00
- Closed at: 2022-04-29T03:09:42+00:00
