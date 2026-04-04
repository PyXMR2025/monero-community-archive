---
title: Bus error RPi 4, debian buster 64
source_url: https://github.com/monero-project/monero/issues/6853
author: ph4r05
assignees: []
labels: []
created_at: '2020-09-30T15:39:57+00:00'
updated_at: '2022-07-19T20:00:45+00:00'
type: issue
status: closed
closed_at: '2022-07-19T20:00:45+00:00'
---

# Original Description
I am experimenting with Raspberry PI builds of the monero for quite a while. I am experiencing an issue similar to the https://www.reddit.com/r/monerosupport/comments/hbqqd2/debian_buster_rpi_3b_bus_error/

Everything worked fine, fully synced Monero node. Then I installed `raspbian-nspawn-64` [GitHub](https://github.com/sakaki-/raspbian-nspawn-64), [blog](https://dev.to/ijason/cpu-mining-on-a-raspberry-pi-1e1d), rebooted the Rasp.

Now I am getting "Bus error", i.e., SIGBUS is terminating my node. Usual tips on the corrupted DB does not work - DB is fine, I ran it with `--salvage-db`. Also logs confirm the database is fine. 

Node terminates when processing P2P requests (not DB or anything)

```
2020-09-30 12:21:53.596	T Setting 00:05:00 expiry
2020-09-30 12:21:53.597	T Throttle throttle_speed_in: packet of ~7868b  (from 7868 b) Speed AVG=  29[w=1]   29[w=1] /  Limit=16 KiB/sec  [38375 0 0 0 0 0 0 0 0 0 ]
2020-09-30 12:21:53.597	T Throttle <<< global-IN: packet of ~7868b  (from 7868 b) Speed AVG=  29[w=1]   29[w=1] /  Limit=8192 KiB/sec  [38375 0 0 0 0 0 0 0 0 0 ]
2020-09-30 12:21:53.597	T dbg <<< global-IN: speed is A=   38375 vs Max=8.38861e+06  so sleep: D=-0.995238 sec E=   38375 (Enow=   46243) M=8.38861e+06 W=       1 R=8.35023e+06 Wgood      11 History: [38375 0 0 0 0 0 0 0 0 0 ] m_last_sample_time= 6148.66
2020-09-30 12:21:53.597	D [XXX.XXX.XXX.XXX:18080 OUT] LEVIN_PACKET_RECEIVED. [len=38299, flags2, r?=0, cmd = 1001, v=1
```

I was running with `gdb`:
```
#0  0x00919de8 in void std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >::_M_realloc_insert<nodetool::peerlist_entry_base<epee::net_utils::network_address> >(__gnu_cxx::__normal_iterator<nodetool::peerlist_entry_base<epee::net_utils::network_address>*, std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > > >, nodetool::peerlist_entry_base<epee::net_utils::network_address>&&) ()
#1  0x008f4ad0 in bool epee::serialization::unserialize_stl_container_t_obj<std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >, epee::serialization::portable_storage>(std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>, std::allocator<nodetool::peerlist_entry_base<epee::net_utils::network_address> > >&, epee::serialization::portable_storage&, epee::serialization::portable_storage::hsection, char const*) [clone .constprop.6278] ()
#2  0x0097d268 in epee::net_utils::async_invoke_remote_command2<epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t>, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request_t>, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t> const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >(epee::net_utils::connection_context_base const&, int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request_t> const&, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t> const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1} const&, unsigned int)::{lambda(int, epee::span<unsigned char const>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}::operator()(int, unsigned char const, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) const ()
#3  0x009851b8 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::anvoke_handler<epee::net_utils::async_invoke_remote_command2<epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t>, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request_t>, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t> const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >(epee::net_utils::connection_context_base const&, int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::request_t> const&, epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >&, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)::{lambda(int, epee::misc_utils::struct_init<nodetool::COMMAND_HANDSHAKE_T<cryptonote::CORE_SYNC_DATA>::response_t> const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1} const&, unsigned int)::{lambda(int, epee::span<unsigned char const>, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&)#1}>::handle(int, unsigned char const, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&) ()
#4  0x0097c304 in epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsigned int) ()
#5  0x0098a618 in epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::handle_read(boost::system::error_code const&, unsigned int) ()
#6  0x0093f1d4 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int> >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::binder2<boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::system::error_code, unsigned int>&) ()
#7  0x0094089c in boost::asio::detail::completion_handler<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#8  0x00940b48 in void boost::asio::detail::strand_service::dispatch<boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > > >(boost::asio::detail::strand_service::strand_impl*&, boost::asio::detail::rewrapped_handler<boost::asio::detail::binder2<boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running>, boost::system::error_code, unsigned int>, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> > >&) ()
#9  0x00940d24 in boost::asio::detail::reactive_socket_recv_op<boost::asio::mutable_buffers_1, boost::asio::detail::wrapped_handler<boost::asio::io_context::strand, boost::_bi::bind_t<void, boost::_mfi::mf2<void, epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::system::error_code const&, unsigned int>, boost::_bi::list3<boost::_bi::value<boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_con--Type <RET> for more, q to quit, c to continue without paging--
text_t<cryptonote::cryptonote_connection_context> > > > >, boost::arg<1> (*)(), boost::arg<2> (*)()> >, boost::asio::detail::is_continuation_if_running> >::do_complete(void*, boost::asio::detail::scheduler_operation*, boost::system::error_code const&, unsigned int) ()
#10 0x0068bc50 in boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) ()
#11 0x0068bd9c in boost::asio::detail::scheduler::run(boost::system::error_code&) ()
#12 0x009184e8 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() ()
#13 0xf7704cdc in ?? () from /usr/lib/arm-linux-gnueabihf/libboost_thread.so.1.67.0
#14 0xf7498494 in start_thread (arg=0xd09f6ff0) at pthread_create.c:486
#15 0xf741b578 in ?? () at ../sysdeps/unix/sysv/linux/arm/clone.S:73 from /lib/arm-linux-gnueabihf/libc.so.6
Backtrace stopped: previous frame identical to this frame (corrupt stack?)
```

Any ideas what this could be? Meanwhile, I am compiling debug build, trying to get more info. 
Wild guess - unaligned access, kernel is not running in 64bit mode?

Another approach would be to compile 64bit version and test. This is in the TODO list, but compilation takes 6 hours or so :)

# Discussion History
## ph4r05 | 2020-09-30T15:49:23+00:00
Interesting: 32bit build does not work now. I am going for 64bit build.

## ph4r05 | 2020-09-30T16:51:07+00:00
I can confirm that compiling 64bit version and running in 64bit userland works. I did not manage to get it working otherwise. 

Surprisingly, Bitcoind compiled in 32bit userland works without change (compiled and ran before the switch to aarch644 kernel. Monerod compiled in 32bit userland and run in 32bit userland is being killed by the aforementioned SIGBUS. maybe it can be fixed somehow?)

I am providing here compile instructions for googlers:

```bash
sudo apt update
sudo apt full-upgrade
sudo apt-get install -y raspbian-nspawn-64
sudo reboot

# switch to 64bit userland
ds64-shell

# install deps
sudo apt update && sudo apt install build-essential git cmake pkg-config libboost-all-dev libssl-dev libzmq3-dev libunbound-dev libsodium-dev libunwind8-dev liblzma-dev libreadline6-dev libldns-dev libexpat1-dev doxygen graphviz libpgm-dev qttools5-dev-tools libhidapi-dev libusb-1.0-0-dev libprotobuf-dev protobuf-compiler libudev-dev
sudo apt install build-essential cmake libboost-all-dev miniupnpc libunbound-dev graphviz doxygen libunwind8-dev pkg-config libssl-dev libzmq3-dev libsodium-dev libhidapi-dev libnorm-dev libusb-1.0-0-dev libpgm-dev libprotobuf-dev protobuf-compiler libgcrypt20-dev

# build
make -j2 release

# run in 64bit userland, `ds64-run --help` for more options
ds64-run --wait -t build/Linux/release-v0.17/release/bin/monerod --log-file monerod.log --prune-blockchain --bg-mining-enable --pad-transactions --max-concurrency 2 --prep-blocks-threads 2 --log-level 3
```

An alternative way is to switch to the 64bit machine with `ds64-shell` and create systemctl service there...

OR you can re-build 32bit Monero, however, Bus error is still present after rebuild.

```bash
make release-static-linux-armv7
```

## moneromooo-monero | 2020-10-02T13:49:53+00:00
So monero assumes 64 bit alignment somewhere, basically ?

## ph4r05 | 2020-10-02T14:20:16+00:00
I have too little information to say so. This is a bit unusual scenario: monerod compiled in 32bit. Then kernel was updated from 32bit to 64bit aarch64. Now 32bit compiled monerod gets killed by SIGBUS (running in 32bit mode), which usually means unaligned access or invalid address.

According to the stacktrace, this happens during deserialization of the `std::vector<nodetool::peerlist_entry_base<epee::net_utils::network_address>` in p2p incoming handler `epee::levin::async_protocol_handler`. 

Any ideas on how to debug this? 

## ph4r05 | 2020-10-02T14:49:31+00:00
I will try to recompile Monerod with `release-static-linux-armv7` in 32bit mode. If that works I can close the issue.

## ph4r05 | 2020-10-02T16:07:41+00:00
Update: monerod built for 32bit arch does not run under aarch64 kernel in 32bit userland. Bus error. I will do some more experiments.

## moneromooo-monero | 2020-10-02T16:52:06+00:00
> Any ideas on how to debug this?

prints (or MGINFO) everywhere in the serialization code. And -g -O0 might be enough to spot exactly where it breaks in gdb.

## mwthink | 2020-10-30T19:52:51+00:00
Very interested in helping to solve this problem. Trying to run monerod on my Kubernetes cluster made up of Raspberry Pis (mixed 32 and 64bit) and traditional x86_64 nodes. 

It would seem that between the Pi 4 being unable to run the armv8 binary (#2858) and the armv7 binary not running in 64-bit, there is no way to run monerod on a Raspberry Pi in 64-bit mode without compiling it yourself. 

I'm sure there's all sorts of better ways to go about this, but the most straightforward one at this point would just be to build distinct 32 and 64 bit binaries for both versions of ARM. 

## hyc | 2020-10-30T23:19:56+00:00
You'll have to compile your own ARMv8 binary with NO_AES as already noted in #2858, for the 64bit. No idea why the 32bit is broken.

## selsta | 2022-07-19T20:00:45+00:00
Should be solved by #8001

# Action History
- Created by: ph4r05 | 2020-09-30T15:39:57+00:00
- Closed at: 2022-07-19T20:00:45+00:00
