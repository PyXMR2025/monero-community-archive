---
title: 'monero-blockchain-ancestry --refresh fails '
source_url: https://github.com/monero-project/monero/issues/8952
author: benmordecai
assignees:
- '0xFFFC0000'
labels:
- low priority
- reproduction needed
- more info needed
created_at: '2023-07-17T16:28:40+00:00'
updated_at: '2024-06-25T11:43:41+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
```
2023-07-17 16:22:22.299 W Starting...
2023-07-17 16:22:22.299 W Initializing source blockchain (BlockchainDB)
/usr/include/c++/13.1.1/bits/unique_ptr.h:453: typename std::add_lvalue_reference<_Tp>::type std::unique_ptr<_Tp, _Dp>::operator*() const [with _Tp = cryptonote::Blockchain; _Dp = std::default_delete<cryptonote::Blockchain>; typename std::add_lvalue_reference<_Tp>::type = cryptonote::Blockchain&]: Assertion 'get() != pointer()' failed.
Aborted (core dumped)
```

# Discussion History
## selsta | 2023-07-18T11:34:03+00:00
Self compiled? Release binaries?

## benmordecai | 2023-07-18T11:58:26+00:00
Installed from Arch repos

## selsta | 2023-07-18T11:59:30+00:00
Can you try release binaries too?

## benmordecai | 2023-07-18T12:04:51+00:00
Looks like release binaries did not crash at the same point. I assume this means it is a problem with the way that Arch has packaged it from their repos?

## selsta | 2023-07-18T12:07:21+00:00
Could be due to using a newer compiler version, but should still be a bug in our code somewhere.

## benmordecai | 2023-07-18T12:08:41+00:00
Is there anything you need from me to produce diagnostic information?

## benmordecai | 2023-07-18T12:09:07+00:00
And should this be reported to Arch maintainers?

## selsta | 2023-07-20T22:18:43+00:00
Since it seems to be a bug in monero, I'd say no. I doubt they would downgrade compiler for such a niche program like monero-blockchain-ancestry.

## 0xFFFC0000 | 2024-02-13T12:47:38+00:00
I tried with 
```
$ gcc --version
gcc (GCC) 13.2.1 20231205 (Red Hat 13.2.1-6)
```

and was not able to reproduce.  Can you run with `--log-level=4` and put the log output here.

## benmordecai | 2024-06-25T11:43:40+00:00
```
$ monero-blockchain-ancestry --refresh --log-level=4
2024-06-25 11:43:17.931 W Starting...
2024-06-25 11:43:17.931 W Initializing source blockchain (BlockchainDB)
/usr/include/c++/13.2.1/bits/unique_ptr.h:453: typename std::add_lvalue_reference<_Tp>::type std::unique_ptr<_Tp, _Dp>::operator*() const [with _Tp = cryptonote::Blockchain; _Dp = std::default_delete<cryptonote::Blockchain>; typename std::add_lvalue_reference<_Tp>::type = cryptonote::Blockchain&]: Assertion 'get() != pointer()' failed.
Aborted (core dumped)
```

# Action History
- Created by: benmordecai | 2023-07-17T16:28:40+00:00
