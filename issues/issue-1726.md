---
title: Monerod log file has all sorta of errors [LEVIN_ERROR_CONNECTION_DESTROYED]
source_url: https://github.com/monero-project/monero/issues/1726
author: KhojaHoldingCorp
assignees: []
labels:
- invalid
created_at: '2017-02-13T19:58:27+00:00'
updated_at: '2017-09-21T09:36:25+00:00'
type: issue
status: closed
closed_at: '2017-09-21T09:36:25+00:00'
---

# Original Description
I get lots of errors like this:

2017-02-13 11:53:14.817 [P2P6]  ERROR   net.p2p src/p2p/net_node.inl:1455       [72.53.129.124:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)

and one error like this

2017-02-13 11:03:13.440 [P2P4]  ERROR   net.p2p src/p2p/net_node.inl:767        [91.134.234.203:18080 OUT] COMMAND_HANDSHAKE Failed


# Discussion History
## moneromooo-monero | 2017-02-13T19:59:34+00:00
Are you having problems getting peers ? Some amount of those is expected.

## KhojaHoldingCorp | 2017-02-13T20:04:13+00:00
they have appeared since the recompile with the bleeding edge source..

There is about 200 lines of those error since the recompile a few hours ago..

Gonna switch to the pre compiled binaries and see if they go away

## KhojaHoldingCorp | 2017-02-13T20:09:37+00:00
I gave it one more try with the Bleeding Edge!
 
sudo /opt/monero/bin/monerod --config-file /etc/monero/monerod.conf

2017-02-13 12:05:42.382     7fa21a044740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 12:05:42.382     7fa21a044740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:WARNING,global:INFO,stacktrace:INFO

2017-02-13 12:05:42.382     7fa21a044740        INFO    global  src/daemon/main.cpp:280 Monero 'Wolfram Warptangent' (v0.10.1.0-3f171b9)

2017-02-13 12:05:42.383     7fa21a044740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...

2017-02-13 12:05:42.383     7fa21a044740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK

2017-02-13 12:05:42.383     7fa21a044740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...

2017-02-13 12:05:48.662     7fa21a044740        WARN    net.p2p src/p2p/net_node.inl:582        UPnP device was found but not recognized as IGD.

2017-02-13 12:05:48.662     7fa21a044740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK

2017-02-13 12:05:48.662     7fa21a044740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...

2017-02-13 12:05:48.662     7fa21a044740        ERROR   default src/rpc/rpc_args.cpp:76 --rpc-bind-ip permits inbound unencrypted external connections. Consider SSH tunnel or SSL proxy instead. Override with --confirm-external-bind

2017-02-13 12:05:48.663     7fa21a044740        INFO    global  src/daemon/p2p.h:90     Deinitializing p2p...

2017-02-13 12:05:48.664     7fa21a044740        INFO    global  src/daemon/core.h:90    Deinitializing core...

2017-02-13 12:05:48.666     7fa21a044740        ERROR   daemon  src/daemon/core.h:95    Failed to deinitialize core...

2017-02-13 12:05:48.666     7fa21a044740        INFO    global  src/daemon/protocol.h:77        Stopping cryptonote protocol...

2017-02-13 12:05:48.666     7fa21a044740        INFO    global  src/daemon/protocol.h:81        Cryptonote protocol stopped successfully
Daemon stopped successfully

2017-02-13 12:05:48.666     7fa21a044740        ERROR   daemon  src/daemon/main.cpp:288 Exception in main! Failed to initialize core rpc server.

And now with --confirm-external-bind

monero@monerod:/var/log/monero$ sudo /opt/monero/bin/monerod --config-file /etc/monero/monerod.conf --confirm-external-bind

2017-02-13 12:07:50.345     7fda85374740        INFO    global  contrib/epee/src/mlog.cpp:145   New log categories: *:WARNING,net*:FATAL,global:INFO,verify:FATAL,stacktrace:INFO

2017-02-13 12:07:50.345     7fda85374740        INFO    global  contrib/epee/src/mlog.cpp:153   New log categories: *:WARNING,global:INFO,stacktrace:INFO

2017-02-13 12:07:50.345     7fda85374740        INFO    global  src/daemon/main.cpp:280 Monero 'Wolfram Warptangent' (v0.10.1.0-3f171b9)

2017-02-13 12:07:50.346     7fda85374740        INFO    global  src/daemon/protocol.h:55        Initializing cryptonote protocol...

2017-02-13 12:07:50.346     7fda85374740        INFO    global  src/daemon/protocol.h:60        Cryptonote protocol initialized OK

2017-02-13 12:07:50.346     7fda85374740        INFO    global  src/daemon/p2p.h:63     Initializing p2p server...

2017-02-13 12:07:55.930     7fda85374740        WARN    net.p2p src/p2p/net_node.inl:582        UPnP device was found but not recognized as IGD.

2017-02-13 12:07:55.930     7fda85374740        INFO    global  src/daemon/p2p.h:68     P2p server initialized OK

2017-02-13 12:07:55.930     7fda85374740        INFO    global  src/daemon/rpc.h:58     Initializing core rpc server...

2017-02-13 12:07:55.931     7fda85374740        WARN    net.http        contrib/epee/include/net/http_server_impl_base.h:70     Binding on 0.0.0.0:18081

2017-02-13 12:07:55.931     7fda85374740        INFO    global  src/daemon/rpc.h:63     Core rpc server initialized OK on port: 18081

2017-02-13 12:07:55.931     7fda85374740        INFO    global  src/daemon/core.h:74    Initializing core...

2017-02-13 12:07:55.961     7fda85374740        INFO    global  src/cryptonote_core/cryptonote_core.cpp:327     Loading blockchain from folder /var/monero/lmdb ...

2017-02-13 12:07:59.013     7fda85374740        INFO    global  src/daemon/core.h:79    Core initialized OK

2017-02-13 12:07:59.013     7fda85374740        INFO    global  src/daemon/rpc.h:68     Starting core rpc server...

2017-02-13 12:07:59.014 [SRV_MAIN]      INFO    global  src/daemon/rpc.h:73     Core rpc server started ok

2017-02-13 12:07:59.014 [SRV_MAIN]      INFO    global  src/daemon/p2p.h:78     Starting p2p net loop...

2017-02-13 12:08:00.014 [P2P1]  INFO    global  src/cryptonote_core/cryptonote_core.cpp:1037

**********************************************************************
The daemon will start synchronizing with the network. It may take up to several hours.

You can set the level of process detailization* through "set_log <level|categories>" command*,
where <level> is between 0 (no details) and 4 (very verbose), or custom category based levels (eg, *:WARNING)

Use the "help" command to see the list of available commands.
**********************************************************************


2017-02-13 12:08:02.870 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:288     [69.43.206.102:18080 OUT] Sync data returned a new top block candidate: 1245392 -> 1245399 [Your node is 7 blocks (0 days) behind]
SYNCHRONIZATION started

2017-02-13 12:08:03.153 [P2P5]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:288     [173.214.173.29:18080 OUT] Sync data returned a new top block candidate: 1245392 -> 1245399 [Your node is 7 blocks (0 days) behind]
SYNCHRONIZATION started

2017-02-13 12:08:03.615 [P2P2]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:288     [27.93.149.184:18080 OUT] Sync data returned a new top block candidate: 1245392 -> 1245399 [Your node is 7 blocks (0 days) behind]
SYNCHRONIZATION started

2017-02-13 12:08:07.796 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:983     [69.43.206.102:18080 OUT]  Synced 1245399/1245399

2017-02-13 12:08:07.796 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1077    SYNCHRONIZED OK

2017-02-13 12:08:07.796 [P2P1]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:1093

**********************************************************************
You are now synchronized with the network. You may now start monero-wallet-cli.

Use the "help" command to see the list of available commands.
**********************************************************************

2017-02-13 12:08:07.799 [P2P2]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:352   Exception at [connection<t_protocol_handler>::handle_read], what=batch transaction not in progress

2017-02-13 12:08:10.389 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1455       [45.56.66.130:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-3, LEVIN_ERROR_CONNECTION_DESTROYED)

2017-02-13 12:08:13.385 [P2P0]  ERROR   net.p2p src/p2p/net_node.inl:1455       [93.179.68.136:18080 OUT] COMMAND_REQUEST_SUPPORT_FLAGS invoke failed. (-4, LEVIN_ERROR_CONNECTION_TIMEDOUT)


## anonimal | 2017-02-13T20:19:54+00:00
>sudo /opt/monero/bin/monerod --config-file /etc/monero/monerod.conf

Maybe unrelated, but it's not a good idea to run as root.

## KhojaHoldingCorp | 2017-02-13T20:22:25+00:00
usually its run from a systemd service file and i get very few errors. Since the recompile with the "bleeding Edge Source" I have gotten many errors. 

I will try again without root

## KhojaHoldingCorp | 2017-02-13T20:26:40+00:00
got the same error without root.

As soon as I go back to release all the problems go away!


## moneromooo-monero | 2017-02-13T20:27:26+00:00
Most likely not. Try running the release with a bit more logs :)

## KhojaHoldingCorp | 2017-02-13T21:17:57+00:00
I have added log level 2 to the systemd file..

I get lots of log output so it feels silly pasting it here ..

It seems fine with the pre compiled release binaries

here is a grep of the errors in the log:

`2017-02-13 12:08:07.798 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:158      [9] /opt/monero/bin/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned long)+0x1ae [0x4fd24e]

2017-02-13 12:08:07.798 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:158      [11] /opt/monero/bin/monerod:boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned long>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x118 [0x55eb98]

2017-02-13 12:08:07.798 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:158      [12] /opt/monero/bin/monerod:boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_service::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned long>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x4b4 [0x517384]

2017-02-13 12:08:07.798 [P2P2]  INFO    stacktrace      src/common/stack_trace.cpp:158      [13] /opt/monero/bin/monerod:boost::asio::detail::epoll_reactor::descriptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x1e9 [0x4c0ac9]`

( all the errors are from over 1 hour ago )



## ghost | 2017-02-13T21:59:57+00:00
@KhojaHoldingCorp would you mind formatting your pasted code with the 'insert code' apostrophes so that github formats it correctly - makes it easier to read.

Thanks!

## ghost | 2017-02-13T22:00:36+00:00
And can you please paste the contents of your configuration file?

## KhojaHoldingCorp | 2017-02-13T22:06:28+00:00
`monero@monerod:/etc/monero$ cat /etc/monero/monerod.conf

data-dir=/var/monero

log-file=/var/log/monero/monero-daemon.log

log-level=2

rpc-bind-ip=0.0.0.0`

( I've added extra lines for readability )

Keep in mind all the errors have disappeared since going back to the pre compiled binaries. 

The reason for using the "Bleeding Edge" Source was to try and fix this https://github.com/monero-project/monero/issues/1722

## moneromooo-monero | 2017-08-07T23:23:40+00:00
The last comment has a stack trace which has the first part clipped, but in any case none of that appears obviously buggy. You didn't say whether you had trouble finding peers as asked in the first comment, so I assume that is working. So unless there's some evidence of something going wrong (and these network errors alone aren't), I'll call it good.

## moneromooo-monero | 2017-08-10T10:59:09+00:00
Oh, re-reading the log, I see an error:

2017-02-13 12:08:07.799 [P2P2] ERROR net contrib/epee/include/net/abstract_tcp_server2.inl:352 Exception at [connection<t_protocol_handler>::handle_read], what=batch transaction not in progress

It'd be interesting to see the stack trace for this (in bitmonerod.log)

## moneromooo-monero | 2017-09-21T09:21:49+00:00
No evidence anything is going wrong, the net errors are expected unless they happen for every single peer, and the batch transactions one might or might be OK, don't know without the full trace.

+invalid

# Action History
- Created by: KhojaHoldingCorp | 2017-02-13T19:58:27+00:00
- Closed at: 2017-09-21T09:36:25+00:00
