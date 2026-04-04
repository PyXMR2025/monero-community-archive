---
title: Typo error in src/wallet/wallet2.cpp
source_url: https://github.com/monero-project/monero/issues/2057
author: BurtonChia
assignees: []
labels: []
created_at: '2017-05-31T08:49:28+00:00'
updated_at: '2017-07-06T09:40:53+00:00'
type: issue
status: closed
closed_at: '2017-07-06T09:40:53+00:00'
---

# Original Description
Hi, I was compiling the code and encountered this error:

/usr/local/src/monero/src/wallet/wallet2.cpp: In member function 'void tools::wallet2::transfer_selected_rct(std::vector<cryptonote::tx_destination_entry>, std::__cxx11::list<long unsigned int>, size_t, std::vec
tor<std::vector<std::tuple<long unsigned int, crypto::public_key, rct::key> > >&, uint64_t, uint64_t, const std::vector<unsigned char>&, cryptonote::transaction&, tools::wallet2::pending_tx&)':
/usr/local/src/monero/src/wallet/wallet2.cpp:3933:75: error: 'get_upper_tranaction_size_limit' was not declared in this scope
   uint64_t upper_transaction_size_limit = get_upper_tranaction_size_limit();
                                                                           ^

Editing the wallet2.cpp to rename get_upper_tranaction_size_limit() to get_upper_tran**s**action_size_limit() fixed the issue.

# Discussion History
## moneromooo-monero | 2017-05-31T22:01:27+00:00
Thanks for the report, fixed in https://github.com/monero-project/monero/pull/2058

# Action History
- Created by: BurtonChia | 2017-05-31T08:49:28+00:00
- Closed at: 2017-07-06T09:40:53+00:00
