---
title: Segmentation fault in monerod on OpenBSD
source_url: https://github.com/monero-project/monero/issues/2851
author: ston1th
assignees: []
labels: []
created_at: '2017-11-21T23:22:10+00:00'
updated_at: '2018-02-14T08:11:54+00:00'
type: issue
status: closed
closed_at: '2018-02-14T08:11:54+00:00'
---

# Original Description
Hi there,

today monerod crashed with a segfault, I think while resizing the DB.

Debug log:
```
2017-11-21 22:53:58.051 [P2P1]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2198 Blockchain::have_block
2017-11-21 22:53:58.051 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:1725 BlockchainLMDB::block_exists
2017-11-21 22:53:58.051 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2759 BlockchainLMDB::block_rtxn_start
2017-11-21 22:53:58.051 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:314  mdb_txn_safe: destructor
2017-11-21 22:53:58.051 [P2P1]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:2203 block exists in main chain
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:3861 Blockchain::prepare_handle_incoming_blocks
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2595 BlockchainLMDB::batch_start
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:555  BlockchainLMDB::check_and_resize_for_batch
2017-11-21 22:53:58.052 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:556  [check_and_resize_for_batch] checking DB size
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:587  BlockchainLMDB::get_estimated_batch_size
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2023 BlockchainLMDB::height
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2759 BlockchainLMDB::block_rtxn_start
2017-11-21 22:53:58.052 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:314  mdb_txn_safe: destructor
2017-11-21 22:53:58.052 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:610  [get_estimated_batch_size] m_height: 72684  block_start: 72184  block_stop: 72683
2017-11-21 22:53:58.053 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:648  estimated average block size for batch: 16863
2017-11-21 22:53:58.053 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:563  calculated batch size: 379417504
2017-11-21 22:53:58.053 [P2P1]  DEBUG   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:572  increase size: 536870912
2017-11-21 22:53:58.053 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:504  BlockchainLMDB::need_resize
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:520  DB map size:     1073741824
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:521  Space used:      717357056
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:522  Space remaining: 356384768
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:523  Size threshold:  379417504
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:525  Percent used: 0.6681  Percent threshold: 0.8000
2017-11-21 22:53:58.053 [P2P1]  INFO    blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:531  Threshold met (size-based)
2017-11-21 22:53:58.053 [P2P1]  INFO    global  src/blockchain_db/lmdb/db_lmdb.cpp:580  [batch] DB resize needed
2017-11-21 22:53:58.053 [P2P1]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:436  BlockchainLMDB::do_resize
2017-11-21 22:53:59.040 [P2P9]  TRACE   net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1184    Checking for idle peers...
2017-11-21 22:53:59.041 [P2P9]  INFO    net.cn  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1196    [185.112.158.127:18080 OUT]  kicking passive peer
2017-11-21 22:54:02.550 [P2P6]  TRACE   blockchain      src/cryptonote_core/blockchain.cpp:297  Blockchain::get_current_blockchain_height
2017-11-21 22:54:02.550 [P2P6]  TRACE   blockchain.db.lmdb      src/blockchain_db/lmdb/db_lmdb.cpp:2023 BlockchainLMDB::height
Segmentation fault.
```

GDB:
```
(gdb) bt
#0  _libc_memcpy (dst0=0xdc471541888, src0=Variable "src0" is not available.
) at /usr/src/lib/libc/string/memcpy.c:103
#1  0x00000dc171d79402 in mdb_txn_renew0 (txn=0xdc471541800) at /home/build/monero/external/db_drivers/liblmdb/mdb.c:2949
#2  0x00000dc171d78e55 in mdb_txn_renew (txn=0xdc471541800) at /home/build/monero/external/db_drivers/liblmdb/mdb.c:2989
Die: DW_TAG_<unknown> (abbrev = 175, offset = 14257677)
        has children: FALSE
        attributes:
                DW_AT_type (DW_FORM_ref4) constant ref: 13920693 (adjusted)
Dwarf Error: Cannot find type of die [in module /var/xmr/bin/monerod-debug]
```

# Discussion History
## ston1th | 2017-12-08T17:34:59+00:00
Monerod runs stable now since 5 days.

I think a full /tmp partition caused the segfault.

## bjornaugestad | 2018-02-13T14:30:08+00:00
FYI: this has happened to me three times today, on linux with master rev ed67e5c001d50a, built with gcc 7.3.
(google brought me here...)

## ston1th | 2018-02-13T17:01:12+00:00
So maybe we should prevent writing to `/tmp/bitmonero.daemon.stdout.stderr`, when running as daemon, since the logfile already defaults to `<datadir>/bitmonero.log` and contains the same logs.

## ston1th | 2018-02-13T22:32:17+00:00
@moneromooo-monero On your recommendation, I tried to reproduce this using a full `/tmp` and `/dev/null`.
I started syncing the blockchain from scratch both times.
Either way monerod crashed, so my assumption about the full `/tmp` was wrong.

But I got a stacktrace:

```
#0  0x000002242fe1625e in mdb_txn_renew0 () from /var/xmr/debug/monerod-debug
#1  0x000002242fc92b0a in cryptonote::BlockchainLMDB::block_rtxn_start () from /var/xmr/debug/monerod-debug
#2  0x000002242fc842c4 in cryptonote::BlockchainLMDB::height () from /var/xmr/debug/monerod-debug
#3  0x000002242fce0431 in cryptonote::Blockchain::prevalidate_block_hashes () from /var/xmr/debug/monerod-debug
#4  0x000002242fc0bdfe in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_chain_entry ()
   from /var/xmr/debug/monerod-debug
#5  0x000002242fa66531 in epee::net_utils::buff_to_t_adapter<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_CHAIN_ENTRY::request&, cryptonote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > > () from /var/xmr/debug/monerod-debug
#6  0x000002242fa308b6 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_invoke_map<cryptonote::cryptonote_connection_context> () from /var/xmr/debug/monerod-debug
#7  0x000002242fa2d0e4 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > () from /var/xmr/debug/monerod-debug
#8  0x000002242fa29378 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify ()
   from /var/xmr/debug/monerod-debug
#9  0x000002242fc30e42 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv () from /var/xmr/debug/monerod-debug
#10 0x000002242fc38758 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read () from /var/xmr/debug/monerod-debug
#11 0x000002242fc3b652 in boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> > () from /var/xmr/debug/monerod-debug
#12 0x000002242fc3b538 in boost::asio::io_service::strand::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> > () from /var/xmr/debug/monerod-debug
#13 0x000002242fc3b426 in boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>::operator()<boost::system::error_code, unsigned long> () from /var/xmr/debug/monerod-debug
#14 0x000002242fc3b161 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete () from /var/xmr/debug/monerod-debug
#15 0x000002242fc3af78 in boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > > () from /var/xmr/debug/monerod-debug
#16 0x000002242fc3acbc in boost::asio::detail::asio_handler_invoke<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> () from /var/xmr/debug/monerod-debug
#17 0x000002242fc3ab47 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete ()
   from /var/xmr/debug/monerod-debug
#18 0x000002242fa71afa in boost::asio::detail::task_io_service::do_run_one () from /var/xmr/debug/monerod-debug
#19 0x000002242fa71671 in boost::asio::detail::task_io_service::run () from /var/xmr/debug/monerod-debug
#20 0x000002242fc25501 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread () from /var/xmr/debug/monerod-debug
#21 0x000002242ff00f0b in _ZN5boost12_GLOBAL__N_1L12thread_proxyEPv () from /var/xmr/debug/monerod-debug
#22 0x0000022687420cae in _rthread_start (v=Variable "v" is not available.
) at /usr/src/lib/librthread/rthread.c:96
#23 0x00000226a88939bb in __tfork_thread () at /usr/src/lib/libc/arch/amd64/sys/tfork_thread.S:75
#24 0x0000000000000000 in ?? ()
```

## ston1th | 2018-02-14T08:11:53+00:00
So I completely overlooked issue #3230.
PR #3231 fixed it.

# Action History
- Created by: ston1th | 2017-11-21T23:22:10+00:00
- Closed at: 2018-02-14T08:11:54+00:00
