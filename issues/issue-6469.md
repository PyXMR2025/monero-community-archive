---
title: Useless "unknown command" errors in daemon
source_url: https://github.com/monero-project/monero/issues/6469
author: tmoravec
assignees: []
labels: []
created_at: '2020-04-21T10:41:10+00:00'
updated_at: '2022-02-19T04:35:15+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:35:15+00:00'
---

# Original Description
When given a wrong argument, some daemon commands fail with "unknown command" error, instead of a meaningful error message. 

Examples of useless error messages:

```
hard_fork_info abc
unknown command: hard_fork_info abc
Monero 'Carbon Chamaeleon' (v0.15.0.0-57854a3e2)
Commands:
  ...

in_peers abcd
unknown command: in_peers abcd
Monero 'Carbon Chamaeleon' (v0.15.0.0-57854a3e2)
Commands:
  ...
```

Example of a better error message:

```
relay_tx abc
failed to parse tx id
```

I offer to improve this if there are no objections.

# Discussion History
## sumogr | 2020-04-28T18:36:20+00:00
hard_fork_info doesnt require a flag so it correctly prints 
`unknown command: hard_fork_info rubbish`

`in_peers rubbish` prints
`unknown command: in_peers rubbish` cause it expects a number otherwise it is an unknown letter string hence an unknown command

`relay_tx rubbish` prints
`E invalid hash format: rubbish`

IMO error messages are just fine. Have you spotted any other that might need changing?

## moneromooo-monero | 2020-05-16T01:24:17+00:00
FWIW I'd OK such a patch. The issue is conflating of return false to not found in the caller IIRC,

## tmoravec | 2020-05-23T11:21:56+00:00
> hard_fork_info doesnt require a flag so it correctly prints
> `unknown command: hard_fork_info rubbish`

The problem is that "unknown command" is not the correct message. `hard_fork_info` _is_ a known command, it just received an unknown or wrong argument. So it should say something along the lines of `Unexpected argument rubbish.` Like for example `relay_tx` does when given a wrong argument. "Unknown command" is a misleading message as it suggests that `hard_fork_info` is an unknown command.
 
> Have you spotted any other that might need changing?

Yeah, let me gather them in the patch so we can talk about individual items. 

## tmoravec | 2020-09-18T12:10:01+00:00
Here's the PR: https://github.com/monero-project/monero/pull/6826

## selsta | 2022-02-19T04:35:15+00:00
Resolved in #6826

# Action History
- Created by: tmoravec | 2020-04-21T10:41:10+00:00
- Closed at: 2022-02-19T04:35:15+00:00
