---
title: 'cryptonote_protocol_handler.inl: no match for operator...missing_tx_req.missing_tx_indices
  ...'
source_url: https://github.com/monero-project/monero/issues/3182
author: danrmiller
assignees: []
labels: []
created_at: '2018-01-26T03:40:23+00:00'
updated_at: '2018-01-28T18:00:29+00:00'
type: issue
status: closed
closed_at: '2018-01-28T18:00:29+00:00'
---

# Original Description
https://build.getmonero.org/builders/monero-static-ubuntu-i686/builds/3315/steps/compile/logs/stdio

```
In file included from /home/vagrant/slave/monero-static-ubuntu-i686/build/src/rpc/instanciations.cpp:34:0:
/home/vagrant/slave/monero-static-ubuntu-i686/build/src/cryptonote_protocol/cryptonote_protocol_handler.inl: In instantiation of 'int cryptonote::t_cryptonote_protocol_handler<t_core>::handle_notify_new_fluffy_block(int, cryptonote::NOTIFY_NEW_FLUFFY_BLOCK::request&, cryptonote::cryptonote_connection_context&) [with t_core = cryptonote::core]':
/home/vagrant/slave/monero-static-ubuntu-i686/build/src/rpc/instanciations.cpp:37:39:   required from here
/home/vagrant/slave/monero-static-ubuntu-i686/build/src/cryptonote_protocol/cryptonote_protocol_handler.inl:615:43: error: no match for 'operator=' (operand types are 'std::vector<long long unsigned int>' and 'std::remove_reference<std::vector<unsigned int>&>::type {aka std::vector<unsigned int>}')
         missing_tx_req.missing_tx_indices = std::move(need_tx_indices);
                                           ^
```
Also https://build.getmonero.org/builders/monero-static-osx-10.12/builds/3406/steps/compile/logs/stdio etc

# Discussion History
## moneromooo-monero | 2018-01-26T10:14:14+00:00
I *think* https://github.com/monero-project/monero/pull/3186 should fix it.

## danrmiller | 2018-01-26T15:21:01+00:00
Thanks, it does fix it.

## danrmiller | 2018-01-28T18:00:29+00:00
Fixed by #3186 

# Action History
- Created by: danrmiller | 2018-01-26T03:40:23+00:00
- Closed at: 2018-01-28T18:00:29+00:00
