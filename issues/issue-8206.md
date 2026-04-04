---
title: unit_tests node_server.bind_same_p2p_port FAILED
source_url: https://github.com/monero-project/monero/issues/8206
author: BebeSparkelSparkel
assignees: []
labels: []
created_at: '2022-03-04T20:31:13+00:00'
updated_at: '2022-03-08T04:04:28+00:00'
type: issue
status: closed
closed_at: '2022-03-08T04:04:28+00:00'
---

# Original Description
OS: OpenBSD 7.0
commit d562deaaa950979b7a31a441a8f02a00013e26d6 (HEAD -> master, origin/master, origin/HEAD)

To reporduce `make release-test`

[LastTest.log](https://github.com/monero-project/monero/files/8188609/LastTest.log)


# Discussion History
## AK041120 | 2022-03-07T00:38:53+00:00
> OS: OpenBSD 7.0 commit [d562dea](https://github.com/monero-project/monero/commit/d562deaaa950979b7a31a441a8f02a00013e26d6) (HEAD -> master, origin/master, origin/HEAD)
> 
> To reporduce `make release-test`
> 
> [LastTest.log](https://github.com/monero-project/monero/files/8188609/LastTest.log)



## selsta | 2022-03-08T04:03:32+00:00
This test currently only works on Linux by default. The following comment is for macOS but should also apply to OpenBSD.

```
For Mac OSX, set the following alias, before running the test, or else it will fail:
sudo ifconfig lo0 alias 127.0.0.2
```

I'll close this as being known "issue", as there is a comment about it in the codebase.

# Action History
- Created by: BebeSparkelSparkel | 2022-03-04T20:31:13+00:00
- Closed at: 2022-03-08T04:04:28+00:00
