---
title: 'Exception: cryptonote::OUTPUT_DNE'
source_url: https://github.com/monero-project/monero/issues/1355
author: glv2
assignees: []
labels: []
created_at: '2016-11-18T10:43:00+00:00'
updated_at: '2017-08-07T18:36:21+00:00'
type: issue
status: closed
closed_at: '2017-08-07T18:36:21+00:00'
---

# Original Description
I compiled the daemon (git head at commit dbf2ab56c54b8be3d0f704f067c9bff79e90ed7e) on my system (GNU/Linux Gentoo x86_64) and I get many *OUTPUT_DNE* exceptions while syncing the blockchain.

Exerpt from the log file (testnet):

```
2016-Nov-18 11:21:58.237766 Attempting to get output pubkey by global index, but key does not exist
2016-Nov-18 11:21:58.237856 Exception: cryptonote::OUTPUT_DNE
2016-Nov-18 11:21:58.237882 Unwinded call stack:
2016-Nov-18 11:21:58.238332      1                  0x7f26fda1ac72 __cxa_throw + 0x117
2016-Nov-18 11:21:58.238811      2                  0x7f26fe5153ec void (anonymous namespace)::throw1<cryptonote::OUTPUT_DNE>(cryptonote::OUTPUT_DNE const&) + 0x119
2016-Nov-18 11:21:58.239283      3                  0x7f26fe524c48 cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&) + 0x3f0
2016-Nov-18 11:21:58.240030      4                  0x7f26ffd01fdc cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&) const + 0x32
2016-Nov-18 11:21:58.240790      5                  0x7f26ffd3aad2 boost::asio::detail::completion_handler<boost::_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::value<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::value<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long) + 0x124
2016-Nov-18 11:21:58.241497      6                  0x7f26ffd2d420 boost::asio::io_service::run() + 0x49e
2016-Nov-18 11:21:58.242192      7                  0x7f26ffd2103f boost::detail::thread_data<boost::_bi::bind_t<unsigned long, boost::_mfi::mf0<unsigned long, boost::asio::io_service>, boost::_bi::list1<boost::_bi::value<boost::asio::io_service*> > > >::run() + 0x33
2016-Nov-18 11:21:58.242534      8                  0x7f26fcec28f6 boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool) + 0x1f6
2016-Nov-18 11:21:58.242789      9                  0x7f26fc38e3b4 __pthread_get_minstack + 0x1364
2016-Nov-18 11:21:58.243058     10                  0x7f26fc0d5aed clone + 0x6d
2016-Nov-18 11:21:58.243157 EXCEPTION: Attempting to get output pubkey by global index, but key does not exist
```

Although there are a lot of these *OUTPUT_DNE* exceptions, the daemon seems to keep working and syncing the blockchain.

Do these exceptions indicate a serious issue, or can they be ignored?


# Discussion History
## moneromooo-monero | 2016-11-18T18:08:30+00:00
I think it's OK, but I don't know that code much at all.


## moneromooo-monero | 2017-08-07T17:22:54+00:00
These are now silenced when they're an expected part of looking up an output to check a transaction's validity.

+resolved

# Action History
- Created by: glv2 | 2016-11-18T10:43:00+00:00
- Closed at: 2017-08-07T18:36:21+00:00
