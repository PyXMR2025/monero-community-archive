---
title: 'Exception: cryptonote::TX_DNE with every refresh'
source_url: https://github.com/monero-project/monero/issues/1130
author: anonimal
assignees: []
labels: []
created_at: '2016-09-25T01:31:20+00:00'
updated_at: '2017-08-09T00:27:43+00:00'
type: issue
status: closed
closed_at: '2017-08-09T00:27:42+00:00'
---

# Original Description
Log excerpt [attached](https://github.com/monero-project/monero/files/491453/monero_TX_DNE.txt).

Built against release `0.10.0` using [release AUR package](https://aur.archlinux.org/packages/monero/).

Doesn't appear to effect functionality (at least not immediately).


# Discussion History
## moneromooo-monero | 2016-09-27T22:17:35+00:00
The stack trace is not very useful. For instance, there is no call to get_tx in expand_transaction_2, etc. I suspect optimizations confused the source lookup. A debug version might help in that regard.


## anonimal | 2016-09-28T02:57:08+00:00
I'll have to build a debug version on another machine and also see if its reproducible, then I'll attach any new results.


## anonimal | 2016-09-28T15:50:00+00:00
When I `-DCMAKE_BUILD_TYPE=Debug` against a cloned tagged release, I cannot reproduce this issue.  When using the same `.bitmonero` data directory but `-DCMAKE_BUILD_TYPE=Release` in the AUR package, I **can** reproduce this issue.

Note: I can _only_ build `Release` with the AUR package because, when building with `Debug`, `monerod` will fail to start:

`/usr/bin/monerod: error while loading shared libraries: librpc.so: cannot open shared object file: No such file or directory`

Fortunately, cloning and building `Release` _or_ `Debug` **cannot** reproduce any of these issues.

 @radfish any ideas why the AUR package is problematic? Could `monerod` somehow not like split packages for `libmonero-wallet` and `monero`? Could GUI deps have any impact? Note: removing linkage with `ld.gold` has _no_ effect on the issue (at least on x86_64).


## moneromooo-monero | 2016-09-30T20:11:05+00:00
Maybe any custom CFLAGS either get the compiler to emit bad code, or expose some undefined behavior. 


## radfish | 2016-10-04T05:35:40+00:00
On Wed, Sep 28, 2016 at 08:50:04AM -0700, 0x914409F1 wrote:

> Note: I can _only_ build `Release` with the AUR package because, when building with `Debug`, `monerod` will fail to start:
> 
> `/usr/bin/monerod: error while loading shared libraries: librpc.so: cannot open shared object file: No such file or directory`

What's librpc.so? is that a new internal lib?

Could you please try with `-DCMAKE_BUILD_TYPE=Debug -DBUILD_SHARED_LIBS=OFF`? (make sure to rm build dir completely before retrying).


## moneromooo-monero | 2017-08-08T11:22:40+00:00
I think that can be closed. Can you check whether this still happens with 0.10.3.1 ? There were some expected TX_DNE (verifying an invalid tx) which were "hidden" (logged as normal errors, not exceptions) while back.

## anonimal | 2017-08-09T00:27:42+00:00
I can't reproduce.

# Action History
- Created by: anonimal | 2016-09-25T01:31:20+00:00
- Closed at: 2017-08-09T00:27:42+00:00
