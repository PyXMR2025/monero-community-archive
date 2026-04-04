---
title: DIFFICULTY_TARGET_V1 was not declared in this scope?
source_url: https://github.com/monero-project/monero/issues/2760
author: thawwed
assignees: []
labels:
- invalid
created_at: '2017-11-04T07:37:56+00:00'
updated_at: '2017-11-14T10:12:45+00:00'
type: issue
status: closed
closed_at: '2017-11-05T16:08:25+00:00'
---

# Original Description
I am trying to build from the source and I keep getting this error. Any advice is much appreciated, as I am beating my head on the wall over this one.

```
[ 70%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o
/root/monero/tests/core_tests/block_validation.cpp: In function ‘bool {anonymous}::lift_up_difficulty(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&, std::vector<long unsigned int>&, std::vector<long unsigned int>&, test_generator&, size_t, cryptonote::block, const cryptonote::account_base&)’:
/root/monero/tests/core_tests/block_validation.cpp:48:85: error: ‘DIFFICULTY_TARGET_V1’ was not declared in this scope
       difficulty_type diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                     ^
/root/monero/tests/core_tests/block_validation.cpp: In member function ‘bool gen_block_invalid_nonce::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const’:
/root/monero/tests/core_tests/block_validation.cpp:178:81: error: ‘DIFFICULTY_TARGET_V1’ was not declared in this scope
   difficulty_type diffic = next_difficulty(timestamps, commulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                 ^
In file included from /root/monero/src/cryptonote_basic/cryptonote_basic.h:47:0,
                 from /root/monero/src/cryptonote_basic/account.h:33,
                 from /root/monero/src/cryptonote_basic/account_boost_serialization.h:33,
                 from /root/monero/tests/core_tests/chaingen.h:47,
                 from /root/monero/tests/core_tests/block_validation.cpp:31:
/root/monero/tests/core_tests/block_validation.cpp: In member function ‘bool gen_block_unlock_time_is_timestamp_in_future::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const’:
/root/monero/src/cryptonote_config.h:85:57: error: ‘DIFFICULTY_TARGET_V1’ was not declared in this scope
 #define DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN             DIFFICULTY_TARGET_V1 //just alias; used by tests
                                                         ^
/root/monero/tests/core_tests/block_validation.cpp:267:87: note: in expansion of macro ‘DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN’
   miner_tx.unlock_time = blk_0.timestamp + 3 * CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW * DIFFICULTY_BLOCKS_ES
                                                                                       ^
/root/monero/tests/core_tests/block_validation.cpp: In member function ‘bool gen_block_invalid_binary_format::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const’:
/root/monero/tests/core_tests/block_validation.cpp:575:67: error: ‘DIFFICULTY_TARGET_V1’ was not declared in this scope
     diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                   ^
/root/monero/tests/core_tests/block_validation.cpp:590:65: error: ‘DIFFICULTY_TARGET_V1’ was not declared in this scope
   diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                 ^
tests/core_tests/CMakeFiles/coretests.dir/build.make:86: recipe for target 'tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o' failed
make[3]: *** [tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o] Error 1

```

# Discussion History
## moneromooo-monero | 2017-11-04T09:07:14+00:00
Which commit hash are you building ?

## thawwed | 2017-11-04T14:18:14+00:00
I am assuming the latest one. I used the git clone command.

On Nov 4, 2017 4:07 AM, "moneromooo-monero" <notifications@github.com>
wrote:

> Which commit hash are you building ?
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2760#issuecomment-341882548>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Af0nFQJwy4ngXJdW_nbb-D3CLsC0Janeks5szClHgaJpZM4QR7H1>
> .
>


## moneromooo-monero | 2017-11-04T15:19:59+00:00
git show


## thawwed | 2017-11-04T15:57:14+00:00
I figured it out. I wasn't compiling the correct release. I used the
command "make release" instead of just "make" and it works now. Thank you!

On Nov 4, 2017 10:20 AM, "moneromooo-monero" <notifications@github.com>
wrote:

> git show
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/2760#issuecomment-341904958>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/Af0nFTFOS4C6oMezz1GrXt4K4_O_aqmqks5szIClgaJpZM4QR7H1>
> .
>


## moneromooo-monero | 2017-11-04T16:14:56+00:00
This will just avoid building tests. Please post the output of git show.

## moneromooo-monero | 2017-11-05T14:55:15+00:00
Oh, and also please report your OS, architecture, and compiler please. Because it seems to be particular to one of those since it doesn't happen to me.

## thawwed | 2017-11-05T16:08:23+00:00
I am using Ubuntu 16.04 LTS and I am brand new to Linux, so please excuse me for not knowing what architecture or compiler means. Either way, I have everything working now, but I appreciate your time in trying to help.

## lettersnumbers | 2017-11-06T17:19:28+00:00
Hey, I am having this same issue right now, even when running "sudo make release".

git show - etnadmin@ip-172-31-23-143:~/electroneum$ git show
commit 53f8b3fa5a382fcb29e9fa7e10b4425cf82d7ce5
Author: Richard Ells <richard@ells.co.uk>
Date:   Tue Oct 31 23:10:15 2017 +0000

    Update README.md

diff --git a/README.md b/README.md
index fdf6a6f..a194c05 100644
--- a/README.md
+++ b/README.md
@@ -1,14 +1,14 @@
 # Electroneum

-Copyright (c) 2017, The Electroneum Project
-Copyright (c) 2014-2017, The Monero Project
-Portions Copyright (c) 2012-2013, The Cryptonote developers
+Copyright (c) 2017, The Electroneum Project
+Copyright (c) 2014-2017, The Monero Project
+Portions Copyright (c) 2012-2013, The Cryptonote developers

 ## Development Resources

 - Web: [electroneum.com](https://electroneum.com)
 - Forum: [electroneumtalk.proboards.com](https://electroneumtalk.proboards.com)
-- Mail: [dev@electroneum.com](mailto:dev@electroneum.com)
+- Mail: [support@electroneum.com](mailto:support@electroneum.com)
 - GitHub: [https://github.com/electroneum/electroneum](https://github.com/electroneum/electroneum)

 ## Introduction
etnadmin@ip-172-31-23-143:~/electroneum$ git show verbose
fatal: ambiguous argument 'verbose': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'
etnadmin@ip-172-31-23-143:~/electroneum$ git show --all
commit 53f8b3fa5a382fcb29e9fa7e10b4425cf82d7ce5
Author: Richard Ells <richard@ells.co.uk>
Date:   Tue Oct 31 23:10:15 2017 +0000

    Update README.md

diff --git a/README.md b/README.md
index fdf6a6f..a194c05 100644
--- a/README.md
+++ b/README.md
@@ -1,14 +1,14 @@
 # Electroneum

-Copyright (c) 2017, The Electroneum Project
-Copyright (c) 2014-2017, The Monero Project
-Portions Copyright (c) 2012-2013, The Cryptonote developers
+Copyright (c) 2017, The Electroneum Project
+Copyright (c) 2014-2017, The Monero Project
+Portions Copyright (c) 2012-2013, The Cryptonote developers

 ## Development Resources

 - Web: [electroneum.com](https://electroneum.com)
 - Forum: [electroneumtalk.proboards.com](https://electroneumtalk.proboards.com)
-- Mail: [dev@electroneum.com](mailto:dev@electroneum.com)
+- Mail: [support@electroneum.com](mailto:support@electroneum.com)
 - GitHub: [https://github.com/electroneum/electroneum](https://github.com/electroneum/electroneum)

 ## Introduction

commit c328163ffa28fee3236ddc7a958a50cede727ba6
Merge: 793bc97 cb23be8
Author: Riccardo Spagni <ric@spagni.net>
Date:   Wed Oct 25 15:26:58 2017 +0200

    Merge pull request #2724

    cb23be8f Wallet API: always use approximate calc of blockchain height (Jaquee)

(END)

    Update README.md

diff --git a/README.md b/README.md
index fdf6a6f..a194c05 100644
--- a/README.md
+++ b/README.md
@@ -1,14 +1,14 @@
 # Electroneum

-Copyright (c) 2017, The Electroneum Project
-Copyright (c) 2014-2017, The Monero Project
-Portions Copyright (c) 2012-2013, The Cryptonote developers
+Copyright (c) 2017, The Electroneum Project
+Copyright (c) 2014-2017, The Monero Project
+Portions Copyright (c) 2012-2013, The Cryptonote developers

 ## Development Resources

 - Web: [electroneum.com](https://electroneum.com)
 - Forum: [electroneumtalk.proboards.com](https://electroneumtalk.proboards.com)
-- Mail: [dev@electroneum.com](mailto:dev@electroneum.com)
+- Mail: [support@electroneum.com](mailto:support@electroneum.com)
 - GitHub: [https://github.com/electroneum/electroneum](https://github.com/electroneum/electroneum)

 ## Introduction

commit c328163ffa28fee3236ddc7a958a50cede727ba6
Merge: 793bc97 cb23be8
Author: Riccardo Spagni <ric@spagni.net>
Date:   Wed Oct 25 15:26:58 2017 +0200

    Merge pull request #2724

    cb23be8f Wallet API: always use approximate calc of blockchain height (Jaquee)

(END)


## lettersnumbers | 2017-11-06T20:54:42+00:00
I think I resolved this error by rm -r the electroneum directory and then starting from scratch. Assuming the first failure that I corrected cause an issue, but it's now beyond that percentage.. will update if any further issues building

## hyc | 2017-11-06T21:04:05+00:00
This is the Monero issue tracker, not the Electroneum issue tracker.

## hyc | 2017-11-06T21:04:14+00:00
+invalid

## adelinvrd | 2017-11-14T10:12:45+00:00
I have the same error how can I fix it?

`[ 58%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp: In function 'bool {anonymous}::lift_up_difficulty(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&, std::vector<long unsigned int>&, std::vector<long unsigned int>&, test_generator&, size_t, cryptonote::block, const cryptonote::account_base&)':
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:48:85: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
       difficulty_type diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                     ^
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_invalid_nonce::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:178:81: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
   difficulty_type diffic = next_difficulty(timestamps, commulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                 ^
In file included from /dev/shm/electroneum-master/src/cryptonote_basic/cryptonote_basic.h:47:0,
                 from /dev/shm/electroneum-master/src/cryptonote_basic/account.h:33,
                 from /dev/shm/electroneum-master/src/cryptonote_basic/account_boost_serialization.h:33,
                 from /dev/shm/electroneum-master/tests/core_tests/chaingen.h:47,
                 from /dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:31:
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_unlock_time_is_timestamp_in_future::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/dev/shm/electroneum-master/src/cryptonote_config.h:85:57: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
 #define DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN             DIFFICULTY_TARGET_V1 //just alias; used by tests
                                                         ^
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:267:87: note: in expansion of macro 'DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN'
   miner_tx.unlock_time = blk_0.timestamp + 3 * CRYPTONOTE_MINED_MONEY_UNLOCK_WINDOW * DIFFICULTY_BLOCKS_ESTIMATE_TIMESPAN;
                                                                                       ^
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_invalid_binary_format::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:575:67: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
     diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                   ^
/dev/shm/electroneum-master/tests/core_tests/block_validation.cpp:590:65: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
   diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);`

# Action History
- Created by: thawwed | 2017-11-04T07:37:56+00:00
- Closed at: 2017-11-05T16:08:25+00:00
