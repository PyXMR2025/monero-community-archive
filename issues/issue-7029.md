---
title: Daemon RPC target_height always 0 when fully synced
source_url: https://github.com/monero-project/monero/issues/7029
author: michnovka
assignees: []
labels: []
created_at: '2020-11-19T11:01:56+00:00'
updated_at: '2020-12-04T21:21:43+00:00'
type: issue
status: closed
closed_at: '2020-12-04T21:21:42+00:00'
---

# Original Description
In version 0.17.1.3 target_height in sync_info RPC call is always 0 when node is synced. According to the documentation:

> target_height - unsigned int; The height of the next block in the chain.

Before it used to say (from my notes)

> target_height - unsigned int; target height the node is syncing from (optional, absent if node is fully synced)

Not sure when the change occurred, but it is a **breaking** change. It should either be explicitly put to documentation that its 0 when fully synced, or if this is a bug, should be fixed.

### Steps to reproduce:

1. sync node 0.17.1.3 fully

2. perform 
`curl http://127.0.0.1:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"sync_info"}' -H 'Content-Type: application/json'`

3. see     `"target_height": 0,`


# Discussion History
## Kukks | 2020-11-19T11:08:24+00:00
This issue broke the BTCPay integration, and from what I can tell it is from around the latest hard fork version that there were reports of this issue.
I'll patch this issue for the next BTCPay release by checking the `synced = height > 0 && (target_height == height || target_height == 0)`

## xiphon | 2020-11-19T11:11:04+00:00
There is no way to know if the node is synced via RPC at the moment. Looking into it.

## Kukks | 2020-11-19T11:29:42+00:00
The docs at https://www.getmonero.org/resources/developer-guides/daemon-rpc.html#sync_info still states
```
target_height - unsigned int; target height the node is syncing from (optional, absent if node is fully synced)
```

## hyc | 2020-11-19T15:35:22+00:00
Just update the doc to say "absent or zero if node is fully synced" - problem solved.

## michnovka | 2020-11-21T00:42:53+00:00
@hyc I dont think that breaking protocol changes should be announced in a way that after the change starts affecting real-case usage, you update docs to reflect new behavior. This should be included in changelog properly and definitely should not appear between some minor revision updates

## hyc | 2020-11-21T02:43:52+00:00
Agreed, that's not how things ought to be done. But it's been done. Could also simply revert the change.

## hyc | 2020-11-23T15:26:59+00:00
Having looked more deeply into this, the issue is invalid.
> In version 0.17.1.3 target_height in sync_info RPC call is always 0 when node is synced. According to the documentation:

>>    target_height - unsigned int; The height of the next block in the chain.

Incorrect, the line you quoted above is from the get_info RPC documentation.

>Before it used to say (from my notes)

>>    target_height - unsigned int; target height the node is syncing from (optional, absent if node is fully synced)

This line is still present in the current sync_info documentation. It has not changed since it's initial commit on https://repo.getmonero.org/monero-project/monero-site/-/commit/746a5ffb414ed198bccec523afb5b6abaf711adf in 2018.

There is no recent regression here.

The doc for sync_info is incorrect though, the target_height value has never been optional. It will always be present in the response, and will be zero when synced.


## erciccione | 2020-11-25T14:03:46+00:00
Documentation updated with #1328.

# Action History
- Created by: michnovka | 2020-11-19T11:01:56+00:00
- Closed at: 2020-12-04T21:21:42+00:00
