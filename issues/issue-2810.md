---
title: Electroneum BUILD PROBLEM
source_url: https://github.com/monero-project/monero/issues/2810
author: minitzi
assignees: []
labels:
- invalid
created_at: '2017-11-14T11:52:58+00:00'
updated_at: '2017-11-14T14:23:16+00:00'
type: issue
status: closed
closed_at: '2017-11-14T14:23:16+00:00'
---

# Original Description
Hello
Ubuntu 16.04.3 LTS \n \l

I go this error while trying to install Electroneum
[ 58%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/block_validation.cpp.o
/usr/src/gtest/electroneum-master/tests/core_tests/block_validation.cpp: In function 'bool {anonymous}::lift_up_difficulty(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&, std::vector<long unsigned int>&, std::vector<long unsigned int>&, test_generator&, size_t, cryptonote::block, const cryptonote::account_base&)':
/usr/src/gtest/electroneum-master/tests/core_tests/block_validation.cpp:48:85: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
       difficulty_type diffic = next_difficulty(timestamps, cummulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                     ^
/usr/src/gtest/electroneum-master/tests/core_tests/block_validation.cpp: In member function 'bool gen_block_invalid_nonce::generate(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visitor_settings> >&) const':
/usr/src/gtest/electroneum-master/tests/core_tests/block_validation.cpp:178:81: error: 'DIFFICULTY_TARGET_V1' was not declared in this scope
   difficulty_type diffic = next_difficulty(timestamps, commulative_difficulties,DIFFICULTY_TARGET_V1);
                                                                                 ^
In file included from /usr/src/gtest/electroneum-master/src/cryptonote_basic/cryptonote_basic.h:47:0,
                 from /usr/src/gtest/electroneum-master/src/cryptonote_basic/account.h:33,
                 from /usr/src/gtest/electroneum-master/src/cryptonote_basic/account_boost_serialization.h:33,
                 from /usr/src/gtest/electroneum-master/tests/core_tests/chaingen.h:47,
                 from /usr/src/gtest/electroneum-master/tests/core_tests/block_validation.cpp:31:



Can anybody help me please ?
Thanks

# Discussion History
## moneromooo-monero | 2017-11-14T11:55:09+00:00
Wrong project, this is the monero repo.

+invalid

## minitzi | 2017-11-14T11:56:17+00:00
where i can post ? 
do you have any idee when i press on electroleum they bring me here

## moneromooo-monero | 2017-11-14T11:57:19+00:00
Where did you find the link to this repo exactly ?


## minitzi | 2017-11-14T11:57:37+00:00
https://github.com/electroneum/

## moneromooo-monero | 2017-11-14T11:59:19+00:00
Ah, well, that link seems to be where you should file bugs. When I click on electroneum, it doesn't bring me here, but to their own repo. What did you do exactly (ie, which links/button did you click) ?


## minitzi | 2017-11-14T12:01:28+00:00
https://github.com/electroneum/electroneum  / Pull Requesst / New Pull REquest / https://github.com/monero-project/monero/compare/master...electroneum:master / ISSUE / New Issue

## moneromooo-monero | 2017-11-14T12:03:51+00:00
OK, that's a github weirdness then. The electroneum people seem to have disabled their bug report page, probably because they don't care about bug reports.

## minitzi | 2017-11-14T12:04:13+00:00
i understand. :) thanks

## moneromooo-monero | 2017-11-14T12:17:46+00:00
Cool. Or you could use monero, which is pretty much the same, but actually builds ^_^

## serhack | 2017-11-14T12:22:49+00:00
Use Monero instead of electroneum.

## minitzi | 2017-11-14T13:59:40+00:00
im currenty mining electrneum on a public pool and its ok . i wanted to create my own pool :)
monero is not that profitable at the moment.

## moneromooo-monero | 2017-11-14T14:17:03+00:00
Alright, fair enough. Can you close this please, looks like the bot failed to close it when asked.

# Action History
- Created by: minitzi | 2017-11-14T11:52:58+00:00
- Closed at: 2017-11-14T14:23:16+00:00
