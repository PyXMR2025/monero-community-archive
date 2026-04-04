---
title: chaingen_main.cpp fails to build on Ubuntu 14.04
source_url: https://github.com/monero-project/monero/issues/739
author: iamsmooth
assignees: []
labels: []
created_at: '2016-03-21T09:45:07+00:00'
updated_at: '2016-05-10T12:35:05+00:00'
type: issue
status: closed
closed_at: '2016-05-10T12:35:05+00:00'
---

# Original Description
Pretty sure this worked until recently

In file included from /home/ubuntu/github/bitmonero/tests/core_tests/chaingen_main.cpp:31:0:
/home/ubuntu/github/bitmonero/tests/core_tests/chaingen.h: In instantiation of ‘bool do_replay_events(std::vector<boost::variant<cryptonote::block, cryptonote::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_objectcryptonote::transaction, event_visitor_settings> >&) [with t_test_class = gen_simple_chain_001]’:
/home/ubuntu/github/bitmonero/tests/core_tests/chaingen_main.cpp:97:5:   required from here
/home/ubuntu/github/bitmonero/tests/core_tests/chaingen.h:474:8: error: invalid initializer for array member ‘const std::pair<unsigned char, long unsigned int> get_test_options<gen_simple_chain_001>::hard_forks [1]’
 struct get_test_options {
        ^

many more lines of error output follow


# Discussion History
## iamsmooth | 2016-03-21T10:03:26+00:00
Changing line 475 to this fixes it: 

  const std::pair<uint8_t, uint64_t> hard_forks[1] = {std::make_pair((uint8_t)1, (uint64_t)0)};


## iamsmooth | 2016-03-22T07:20:11+00:00
correction, still broken


## laanwj | 2016-03-23T16:46:35+00:00
Same problem here w/ master eb1b87d2393f34caa9698bec23a4b78fa57da752

```
[ 80%] Building CXX object tests/core_tests/CMakeFiles/coretests.dir/chaingen_main.cpp.o
In file included from /home/ubuntu/bitmonero/tests/core_tests/chaingen_main.cpp:31:0:
/home/ubuntu/bitmonero/tests/core_tests/chaingen.h: In instantiation of ‘bool do_replay_events(std::vector<boost::variant<cryptonote::block, cryptonote
::transaction, cryptonote::account_base, callback_entry, serialized_object<cryptonote::block>, serialized_object<cryptonote::transaction>, event_visito
r_settings> >&) [with t_test_class = gen_simple_chain_001]’:
/home/ubuntu/bitmonero/tests/core_tests/chaingen_main.cpp:97:5:   required from here
/home/ubuntu/bitmonero/tests/core_tests/chaingen.h:474:8: error: invalid initializer for array member ‘const std::pair<unsigned char, long unsigned int
> get_test_options<gen_simple_chain_001>::hard_forks [1]’
 struct get_test_options {
        ^
/home/ubuntu/bitmonero/tests/core_tests/chaingen.h:500:34: note: synthesized method ‘constexpr get_test_options<gen_simple_chain_001>::get_test_options
()’ first required here 
   get_test_options<t_test_class> gto;
```


## iamsmooth | 2016-03-24T02:03:29+00:00
This substitute compiles. Not tested

```
struct get_test_options {
  const std::pair<uint8_t, uint64_t> hard_forks[1];
  const cryptonote::test_options test_options = {
    hard_forks
  };
  get_test_options():hard_forks{std::make_pair((uint8_t)1, (uint64_t)0)}{}
};
```


## moneromooo-monero | 2016-03-27T09:47:33+00:00
Passes tests.


## p4fg | 2016-03-30T17:55:49+00:00
Any news on when this might be fixed in master?


## moneromooo-monero | 2016-04-02T21:02:11+00:00
https://github.com/monero-project/bitmonero/pull/788


## fluffypony | 2016-05-10T12:35:05+00:00
Fixed


# Action History
- Created by: iamsmooth | 2016-03-21T09:45:07+00:00
- Closed at: 2016-05-10T12:35:05+00:00
