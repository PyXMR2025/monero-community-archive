---
title: Strange crash this morning
source_url: https://github.com/monero-project/monero/issues/7253
author: agentpatience
assignees: []
labels: []
created_at: '2021-01-01T13:13:08+00:00'
updated_at: '2022-07-20T20:06:54+00:00'
type: issue
status: closed
closed_at: '2022-07-20T20:06:44+00:00'
---

# Original Description
See photo different crash error than yesterday.
![AE839FDD-77D7-4B8C-8F4B-B2165ECB91C1](https://user-images.githubusercontent.com/36264810/103439232-268b1d80-4c09-11eb-9a99-ebea9c0144c9.jpeg)


# Discussion History
## moneromooo-monero | 2021-01-01T13:23:07+00:00
gdb /path/to/monerod core\*
bt full

## selsta | 2021-01-01T13:46:15+00:00
Try `gdb /path/to/monerod core*`

It seems like you entered `gdb /path/to/monerod*`

## agentpatience | 2021-01-01T13:51:16+00:00
![E17AA9E0-B7E3-40CD-AE5B-5A7D56B43709](https://user-images.githubusercontent.com/36264810/103439849-7e785300-4c0e-11eb-9bec-03d87c24c77d.jpeg)


## agentpatience | 2021-01-01T13:52:51+00:00
Something still not right, typing “bt full” in gdb says no stack.

## moneromooo-monero | 2021-01-01T14:37:44+00:00
It's not finding the core file. Possibly it's kept somewhere else by something like systemd or so.
If you're running that, try:

coredumpctl debug monerod

## agentpatience | 2021-01-01T14:49:43+00:00
 coredumpctl debug monerod
No match found.   


## moneromooo-monero | 2021-01-04T12:45:04+00:00
coredumpctl list
coredumpctl debug XXX

And replace XXX with the full name of the binary the list command will print.

## agentpatience | 2021-01-04T16:29:06+00:00
I since restarted and have not seen that again yet tho it is still crashing with “Killed”. I think that’s a separate issue. I ran the commands you asked for but it comes back as “no core dumps found”. This is Ubuntu 20.10 desktop minimal install - maybe have to turn anything on?

## arizvisa | 2021-01-06T14:36:52+00:00
@agentpatience, look for any "*.core" files in the directory you ran the monerod binary (or even "*core*" might match it). make sure you back it up too.

nonetheless, if you run `sysctl kernel.core_pattern`, it'll list what your distro is doing with core files (i.e. dropping it in a file, or passing it to some program). If it's being passed to `systemd-coredump`, then you can use `coredumpctl` as @moneromooo-monero mentioned. If you use `coredumpctl info /path/to/monerod`, it'll print out information about the corefile which should include the backtrace.

If it's being kill'd and you couldn't figure out the signal number, `dmesg` or `journalctl -ke` might dump out whether your kernel's oom killer signalled `monerod`.

## arizvisa | 2021-01-06T15:20:48+00:00
Heh. Friend just informed me that ubuntu is using "apport" (https://wiki.ubuntu.com/Apport), and will occasionally set the `ulimit -c` to 0. If that's the case, we should probably document somewhere to ensure `ulimit -c unlimited` is set.

Nonetheless, "corrupted size vs. prev_size" implies memory corruption. So if this issue is reproduceable, this could be serious...

## moneromooo-monero | 2021-01-06T17:53:57+00:00
It is in the README.

## voidzero | 2021-01-08T09:55:54+00:00
maybe log a warning when ulimit -c is 0 so the user can be made aware.

## moneromooo-monero | 2021-01-09T01:37:44+00:00
People freak out for random things, like the initial message that tells you the log settings. Telling them "core files can't get generated because your limit is 0" will freak some other set of people out, I'm sure of that.

## arizvisa | 2021-01-09T02:43:13+00:00
also, regardless of the core limit being 0, the pid's corefile will still get piped to things like apport or systemd-coredump. so those tools will still be able to snag the backtrace and core from the signal'd process, it's just the kernel won't write its standard corefile to disk by default.

## Artefact2 | 2021-08-13T18:32:49+00:00
I have run into this bug a couple of times while syncing my node. Seems to appear randomly, maybe more frequently during heavy i/o load. Restarting the node will continue the sync OK. Monero 'Oxygen Orion' (v0.17.2.0-release) running on Linux 5.13.7-arch1-1 x86_64.

~~~
Aug 13 14:31:11 Silmeria monerod[37552]: 2021-08-13 12:31:11.178        I Synced 2368970/2426188 (97%, 57218 left)
Aug 13 14:31:15 Silmeria monerod[37552]: 2021-08-13 12:31:15.921        E Failed to parse transaction from blob
Aug 13 14:31:15 Silmeria monerod[37552]: 2021-08-13 12:31:15.922        E Failed to parse transaction from blob
Aug 13 14:31:16 Silmeria monerod[37552]: corrupted size vs. prev_size
Aug 13 14:31:22 Silmeria systemd[1]: monerod.service: Main process exited, code=killed, status=6/ABRT
Aug 13 14:31:22 Silmeria systemd[1]: monerod.service: Failed with result 'signal'.
~~~

Below is the output of `thread apply all bt`.
[gdb.txt.gz](https://github.com/monero-project/monero/files/6984573/gdb.txt.gz)

Edit: it crashed again with a different message, but it looks to be the same issue (or closely related).

~~~
Aug 13 20:37:14 Silmeria monerod[43465]: 2021-08-13 18:37:14.440        I Synced 2404285/2426372 (99%, 22087 left)
Aug 13 20:37:18 Silmeria monerod[43465]: 2021-08-13 18:37:18.588        E Failed to parse transaction from blob
Aug 13 20:37:18 Silmeria monerod[43465]: double free or corruption (!prev)
Aug 13 20:37:31 Silmeria systemd[1]: monerod.service: Main process exited, code=killed, status=6/ABRT
Aug 13 20:37:31 Silmeria systemd[1]: monerod.service: Failed with result 'signal'.
~~~

[gdb.txt.gz](https://github.com/monero-project/monero/files/6984595/gdb.txt.gz)

Edit: again a different message.

~~~
Aug 13 22:37:45 Silmeria monerod[78581]: 2021-08-13 20:37:45.845        I Synced 2414247/2426442 (99%, 12195 left)
Aug 13 22:37:54 Silmeria monerod[78581]: 2021-08-13 20:37:54.359        E Failed to parse transaction from blob
Aug 13 22:37:54 Silmeria monerod[78581]: free(): invalid pointer
Aug 13 22:38:12 Silmeria systemd[1]: monerod.service: Main process exited, code=killed, status=6/ABRT
Aug 13 22:38:12 Silmeria systemd[1]: monerod.service: Failed with result 'signal'.
~~~
[gdb.txt.gz](https://github.com/monero-project/monero/files/6985078/gdb.txt.gz)

My node will no longer sync as my database appears to be corrupted (despite using `--db-sync-mode safe`).

~~~
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I **********************************************************************
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I The daemon will start synchronizing with the network. This may take a long time to complete.
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I You can set the level of process detailization through "set_log <level|categories>" command,
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING).
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I Use the "help" command to see the list of available commands.
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I Use "help <command>" to see a command's documentation.
Aug 13 22:46:11 Silmeria monerod[90726]: 2021-08-13 20:46:11.780        I **********************************************************************
Aug 13 22:46:22 Silmeria monerod[90726]: 2021-08-13 20:46:22.691        I [195.154.29.215:54604 INC] Sync data returned a new top block candidate: 2414255 -> 2426445 [Your node is 12190 blocks (16.9 days) behind]
Aug 13 22:46:22 Silmeria monerod[90726]: 2021-08-13 20:46:22.691        I SYNCHRONIZATION started
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.361        W Error attempting to retrieve an output pubkey from the dbMDB_BAD_TXN: Transaction must abort, has a child, or is invalid
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.370        E Error adding transaction to txpool: Error adding txpool tx metadata to db transaction: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.370        W Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.374        E Exception at [core::handle_incoming_txs()], what=Failed to query m_blocks: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.376        W Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
Aug 13 22:46:52 Silmeria monerod[90726]: 2021-08-13 20:46:52.380        E Exception in cleanup_handle_incoming_blocks: Failed to commit a transaction to the db: MDB_BAD_TXN: Transaction must abort, has a child, or is invalid
~~~

## arizvisa | 2021-08-13T18:40:28+00:00
Double reference being added to a vector it seems...
```
Thread 1 (Thread 0x7f76066fa640 (LWP 37603)):
#0  0x00007f934c117d22 in raise () from /usr/lib/libc.so.6
#1  0x00007f934c101862 in abort () from /usr/lib/libc.so.6
#2  0x00007f934c159d28 in __libc_message () from /usr/lib/libc.so.6
#3  0x00007f934c16192a in malloc_printerr () from /usr/lib/libc.so.6
#4  0x00007f934c162826 in unlink_chunk.constprop () from /usr/lib/libc.so.6
#5  0x00007f934c16307b in _int_free () from /usr/lib/libc.so.6
#6  0x00007f934c1669e8 in free () from /usr/lib/libc.so.6
#7  0x000055ef2bf6bf43 in std::vector<cryptonote::block_complete_entry, std::allocator<cryptonote::block_complete_entry> >::~vector() ()
#8  0x000055ef2c17d9cb in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::try_add_next_blocks(cryptonote::cryptonote_connection_context&) ()
#9  0x000055ef2c184184 in cryptonote::t_cryptonote_protocol_handler<cryptonote::core>::handle_response_get_objects(int, epee::misc_utils::struct_init<cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request_t>&, cryptonote::cryptonote_connection_context&) ()
#10 0x000055ef2be330cb in int nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >(bool, int, epee::span<unsigned char const>, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) ()
#11 0x000055ef2be35953 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::notify(int, epee::span<unsigned char const>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#12 0x000055ef2c12a870 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned long) ()
#13 0x000055ef2c151a42 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long) ()
#14 0x000055ef2c11e25b in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned long>&) ()
#15 0x000055ef2c121166 in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >, boost::asio::io_context::basic_executor_type<std::allocator<void>, 0u> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) ()
#16 0x000055ef2bd9a68f in boost::asio::detail::strand_service::do_dispatch(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::scheduler_operation*) ()
#17 0x000055ef2c1208aa in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#18 0x000055ef2c120c57 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::asio::any_io_executor>::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned long) ()
#19 0x000055ef2c0a7a06 in ?? ()
#20 0x000055ef2c0e9826 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#21 0x00007f934c68fc07 in ?? () from /usr/lib/libboost_thread.so.1.76.0
#22 0x00007f934c2b0259 in start_thread () from /usr/lib/libpthread.so.0
#23 0x00007f934c1d95e3 in clone () from /usr/lib/libc.so.6
```

## selsta | 2021-11-13T00:57:35+00:00
@Artefact2 can you test to sync with `--rpc-ssl disabled` ?

## selsta | 2022-07-20T20:06:44+00:00
Please try v0.18.0.0 and open a new issue if this is still reproducible.

# Action History
- Created by: agentpatience | 2021-01-01T13:13:08+00:00
- Closed at: 2022-07-20T20:06:44+00:00
