---
title: boost update 1.86 breaks the build (...again)
source_url: https://github.com/monero-project/monero/issues/9485
author: tkwilliams
assignees: []
labels:
- duplicate
created_at: '2024-09-15T14:37:52+00:00'
updated_at: '2024-09-15T21:21:16+00:00'
type: issue
status: closed
closed_at: '2024-09-15T16:24:17+00:00'
---

# Original Description
Looks like boost added some data types in 1.86 which conflict with those defined in monero - example below.

Sadly, the distros (OpenSUSE in my case) have started pushing out boost-1.86 to their repos and this is of course breaking the package builds.

```
[   21s] cd /home/abuild/rpmbuild/BUILD/monero-0.18.3.4/build/src/cryptonote_protocol && /usr/bin/ccache /usr/bin/c++ -DAUTO_INITIALIZE_EASYLOGGINGPP -DBLOCKCHAIN_DB=DB_LMDB -DBOOST_ASIO_ENABLE_SEQUENTIAL_STRAND_ALLOCATION -DDEFAULT_DB_TYPE=\"lmdb\" -DHAVE_EXPLICIT_BZERO -DHAVE_READLINE -DHAVE_STRPTIME -DMINIUPNP_STATICLIB -DPER_BLOCK_CHECKPOINT -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/external/rapidjson/include -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/external/easylogging++ -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/src -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/contrib/epee/include -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/external -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/external/supercop/include -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/build/generated_include -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/build/translations -I/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/external/db_drivers/liblmdb -O2 -Wall -U_FORTIFY_SOURCE -D_FORTIFY_SOURCE=3 -fstack-protector-strong -funwind-tables -fasynchronous-unwind-tables -fstack-clash-protection -Werror=return-type -flto=auto -g -pthread -maes  -fno-strict-aliasing -D_GNU_SOURCE   -Wall -Wextra -Wpointer-arith -Wundef -Wvla -Wwrite-strings -Wno-error=extra -Wno-error=deprecated-declarations -Wno-unused-parameter -Wno-error=unused-variable -Wno-error=undef -Wno-error=uninitialized -Wlogical-op -Wno-error=maybe-uninitialized -Wno-error=cpp -Wno-reorder -Wno-missing-field-initializers -fPIC  -Wformat -Wformat-security -fstack-protector -fstack-protector-strong -fcf-protection=full -fstack-clash-protection -Werror=switch -Werror=return-type -fno-strict-aliasing -ftemplate-depth=900 -O2 -g -DNDEBUG -std=c++14 -MD -MT src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o -MF CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o.d -o CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o -c /home/abuild/rpmbuild/BUILD/monero-0.18.3.4/src/cryptonote_protocol/block_queue.cpp
[   21s] /home/abuild/rpmbuild/BUILD/monero-0.18.3.4/src/cryptonote_protocol/block_queue.cpp:45:21: error: redefinition of ‘struct std::hash<boost::uuids::uuid>’
[   21s]    45 |   template<> struct hash<boost::uuids::uuid> {
[   21s]       |                     ^~~~~~~~~~~~~~~~~~~~~~~~
[   21s] In file included from /usr/include/boost/uuid/nil_generator.hpp:8,
[   21s]                  from /home/abuild/rpmbuild/BUILD/monero-0.18.3.4/src/cryptonote_protocol/block_queue.cpp:33:
[   21s] /usr/include/boost/uuid/uuid.hpp:353:19: note: previous definition of ‘struct std::hash<boost::uuids::uuid>’
[   21s]   353 | template<> struct hash<boost::uuids::uuid>
[   21s]       |                   ^~~~~~~~~~~~~~~~~~~~~~~~
[   21s] make[2]: *** [src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/build.make:79: src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/block_queue.cpp.o] Error 1
[   21s] make[2]: Leaving directory '/home/abuild/rpmbuild/BUILD/monero-0.18.3.4/build'
[   21s] make[1]: *** [CMakeFiles/Makefile2:3260: src/cryptonote_protocol/CMakeFiles/obj_cryptonote_protocol.dir/all] Error 2
[   21s] make[1]: *** Waiting for unfinished jobs....
```

This built flawlessly against boost-1.85 of course, but backwards compat has always been a low priority for the boost devs :-/

Thanks!

# Discussion History
## 0xFFFC0000 | 2024-09-15T16:24:08+00:00
Thank you for reporting this. 

https://github.com/monero-project/monero/pull/9450

Duplicate. Closing it.

## tkwilliams | 2024-09-15T16:42:43+00:00
Not a duplicate actually.  boost-1.85 broke SOME stuff, but boost-1.86 broke some entirely NEW STUFF.  I don't see any mention in the #9450 thread addressing the new breakage , so I opened this as a new bug.

## selsta | 2024-09-15T16:45:16+00:00
#9450 fixes build with boost 1.86

## tkwilliams | 2024-09-15T16:45:54+00:00
Oook, sorry if so.  Lemme give it another try :)

## selsta | 2024-09-15T16:46:46+00:00
the PR title should ideally be updated to make it more clear

## tkwilliams | 2024-09-15T17:49:21+00:00
Builds great when I apply it to master.  Sadly, master and v0.18.3.4 have diverged pretty significantly (e.g. I can't just rebase v0.18.3.4 against master, then apply this, which would be needed to justify building a package).  The packaging standards are averse to building straight from master - they prefer the pretense of "RELEASE + some git tag", which is of course NO MORE "stable" than just building from master to begin with, but what can you do :)

No worries, you folks will cut a new release soon enough and we can go from there.

Thanks for all the hard work!

## 0xFFFC0000 | 2024-09-15T17:51:15+00:00
@tkwilliams thanks for updating / reporting this issue. 

Keeping this issue closed. 

## selsta | 2024-09-15T20:34:25+00:00
@tkwilliams there is also a release branch version of this PR open #9462 that should apply without issues

## tkwilliams | 2024-09-15T21:21:15+00:00
NICE!  Fetching now :)

Thanks @selsta

On Sun, Sep 15, 2024 at 4:34 PM selsta ***@***.***> wrote:

> @tkwilliams <https://github.com/tkwilliams> there is also a release
> branch version of this PR open #9462
> <https://github.com/monero-project/monero/pull/9462> that should apply
> without issues
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/9485#issuecomment-2351783283>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ABPNS55CKF3EXD7OYDTGG5DZWXVORAVCNFSM6AAAAABOH4BNFKVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDGNJRG44DGMRYGM>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


# Action History
- Created by: tkwilliams | 2024-09-15T14:37:52+00:00
- Closed at: 2024-09-15T16:24:17+00:00
