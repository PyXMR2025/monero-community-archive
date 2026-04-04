---
title: warnings about unused variables and unnessecry moves
source_url: https://github.com/monero-project/monero/issues/5714
author: moneroexamples
assignees: []
labels: []
created_at: '2019-07-01T11:19:29+00:00'
updated_at: '2019-07-01T11:39:08+00:00'
type: issue
status: closed
closed_at: '2019-07-01T11:39:08+00:00'
---

# Original Description


```
/home/mwo2/monero/src/wallet/wallet_rpc_server.cpp: In member function ‘bool tools::wallet_rpc_server::on_incoming_transfers(const request&, tools::wallet_rpc::COMMAND_RPC_INCOMING_TRANSFERS::response&, epee::json_rpc::error&, const connection_context*)’:
/home/mwo2/monero/src/wallet/wallet_rpc_server.cpp:1809:10: warning: variable ‘transfers_found’ set but not used [-Wunused-but-set-variable]
 1809 |     bool transfers_found = false;
      |          ^~~~~~~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp: In member function ‘boost::optional<epee::wipeable_string> cryptonote::simple_wallet::new_wallet(const boost::program_options::variables_map&, const secret_key&, bool, bool, const string&)’:
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4328:19: warning: redundant move in return statement [-Wredundant-move]
 4328 |   return std::move(password);
      |          ~~~~~~~~~^~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4328:19: note: remove ‘std::move’ call
/home/mwo2/monero/src/simplewallet/simplewallet.cpp: In member function ‘boost::optional<epee::wipeable_string> cryptonote::simple_wallet::new_wallet(const boost::program_options::variables_map&, const cryptonote::account_public_address&, const boost::optional<epee::mlocked<tools::scrubbed<crypto::ec_scalar> > >&, const secret_key&)’:
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4375:19: warning: redundant move in return statement [-Wredundant-move]
 4375 |   return std::move(password);
      |          ~~~~~~~~~^~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4375:19: note: remove ‘std::move’ call
/home/mwo2/monero/src/simplewallet/simplewallet.cpp: In member function ‘boost::optional<epee::wipeable_string> cryptonote::simple_wallet::new_wallet(const boost::program_options::variables_map&)’:
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4416:19: warning: redundant move in return statement [-Wredundant-move]
 4416 |   return std::move(password);
      |          ~~~~~~~~~^~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4416:19: note: remove ‘std::move’ call
/home/mwo2/monero/src/simplewallet/simplewallet.cpp: In member function ‘boost::optional<epee::wipeable_string> cryptonote::simple_wallet::new_wallet(const boost::program_options::variables_map&, const epee::wipeable_string&, const string&)’:
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4469:19: warning: redundant move in return statement [-Wredundant-move]
 4469 |   return std::move(password);
      |          ~~~~~~~~~^~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4469:19: note: remove ‘std::move’ call
/home/mwo2/monero/src/simplewallet/simplewallet.cpp: In member function ‘boost::optional<epee::wipeable_string> cryptonote::simple_wallet::open_wallet(const boost::program_options::variables_map&)’:
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4572:19: warning: redundant move in return statement [-Wredundant-move]
 4572 |   return std::move(password);
      |          ~~~~~~~~~^~~~~~~~~~
/home/mwo2/monero/src/simplewallet/simplewallet.cpp:4572:19: note: remove ‘std::move’ call
```

and

```
/tmp/monero/src/wallet/wallet2.cpp: In member function ‘void tools::wallet2::get_outs(std::vector<std::vector<std::tuple<long unsigned int, crypto::public_key, rct::key> > >&, const std::vector<long unsigned int>&, size_t)’:
/tmp/monero/src/wallet/wallet2.cpp:7729:12: warning: variable ‘existing_ring_found’ set but not used [-Wunused-but-set-variable]
 7729 |       bool existing_ring_found = false;
      |            ^~~~~~~~~~~~~~~~~~~
```


# Discussion History
## moneromooo-monero | 2019-07-01T11:33:48+00:00
The variable ones are fixed on github, and the move ones are harmless.

## moneroexamples | 2019-07-01T11:39:08+00:00
Thanks for info. Closing then.

# Action History
- Created by: moneroexamples | 2019-07-01T11:19:29+00:00
- Closed at: 2019-07-01T11:39:08+00:00
