---
title: Unsafe clearing of secrets
source_url: https://github.com/monero-project/monero/issues/6129
author: bertptrs
assignees: []
labels: []
created_at: '2019-11-13T16:40:21+00:00'
updated_at: '2020-07-08T23:02:07+00:00'
type: issue
status: closed
closed_at: '2020-07-08T23:02:07+00:00'
---

# Original Description
In a few locations across the codebase, `memset` is used to clear secrets from memory before discarding the memory. However, most compilers will see this as a dead-store and remove the `memset` call. It is therefore better to use `memset_s` (from C11) or similar to actually clear those secrets. The actual locations are:

- ~autotrust.c~ part of a submodule, let's ignore it for now
- ~getentropy_linux.c~ part of a submodule, let's ignore it for now
- md5_l.h
- blake256.c (several times)

I'm working on a patch that fixes those issues, but reading your contributing guidelines, I thought I should open an issue first. Is that correct?

# Discussion History
## moneromooo-monero | 2019-11-13T18:44:08+00:00
md5_l.h is not used. blake is only used for PoW, so nothing secret. Normally you'd use memwipe, but this is in epee, which crypto does not depend on.

## moneromooo-monero | 2019-11-13T18:45:04+00:00
And generally, there is not need for an issue unless you want to ask something, gauge opinions, etc. If you're sure about what to do in a patch, a patch only is fine.

## moneromooo-monero | 2019-11-13T18:46:20+00:00
Cryptonight (the PoW hash which uses blake) is also used as a KDF, where the blake clearing could potentially matter.

## moneromooo-monero | 2019-11-14T12:20:12+00:00
Actually crypto already depends on epee. Patch looks good, thanks.

## moneromooo-monero | 2019-11-23T15:03:05+00:00
OMG. md5 is actually used now. For HTTP auth :S

## moneromooo-monero | 2020-05-16T18:48:26+00:00
https://github.com/monero-project/monero/pull/6540

## moneromooo-monero | 2020-07-08T23:02:07+00:00
Merged

# Action History
- Created by: bertptrs | 2019-11-13T16:40:21+00:00
- Closed at: 2020-07-08T23:02:07+00:00
