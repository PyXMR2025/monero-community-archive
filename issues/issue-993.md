---
title: Stack dump on aarch64 (ARMv8) Ubuntu 16.04 if libunwind installed
source_url: https://github.com/monero-project/monero/issues/993
author: ghost
assignees: []
labels:
- invalid
created_at: '2016-08-26T23:29:51+00:00'
updated_at: '2018-01-08T14:16:32+00:00'
type: issue
status: closed
closed_at: '2018-01-08T14:16:32+00:00'
---

# Original Description
Hi all,

So I'm on an Odroid C2, ARMv8 Cortex-A53 system (Amlogic S905) and ARMbian Ubuntu 16.04 server. I've put in a pull request that allows monero to compile on ARMv8 (#966).

During testing I came across the following issue:

Compiled with my PR and -O2 optimisation. Ran just fine.

Decided to install libunwind because I don't like to see messages at the start of compilation :)

Compiled with my PR and -O3 optimisation. Stack dump, bitmonerod crashed.

Compiled with my PR and -Ofast optimisation. Stack dump, bitmonerod crashed.

Compiled with my PR and -O2 optimisation (again). Stack dump, bitmonerod crashed. **Uh oh**

Uninstalled and purged libunwind, recompiled with -O2 optimisation. Up and running again.

Now going to go back and test with -Ofast again...without libunwind.

Stack dump listed below: 

```
2016-Aug-25 20:57:35.014443 Attempting to get output pubkey by global index, but key does not exist
2016-Aug-25 20:57:35.014656 Exception: cryptonote::OUTPUT_DNE
2016-Aug-25 20:57:35.014703 Unwinded call stack:
2016-Aug-25 20:57:35.016343 1 0x65f9a4 __cxa_throw + 0x74
2016-Aug-25 20:57:35.016893 Attempting to get output pubkey by global index, but key does not exist
2016-Aug-25 20:57:35.016976 Exception: cryptonote::OUTPUT_DNE
2016-Aug-25 20:57:35.017016 Unwinded call stack:
2016-Aug-25 20:57:35.017869 2 0x61aa54 void (anonymous namespace)::throw1cryptonote::OUTPUT_DNE(cryptonote::OUTPUT_DNE const&) [clone .constprop.1186] + 0xcc
2016-Aug-25 20:57:35.019217 1 0x65f9a4 __cxa_throw + 0x74
2016-Aug-25 20:57:35.020183 2 0x61aa54 void (anonymous namespace)::throw1cryptonote::OUTPUT_DNE(cryptonote::OUTPUT_DNE const&) [clone .constprop.1186] + 0xcc
2016-Aug-25 20:57:35.021003 3 0x5c9d80 cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector > const&, std::vector >&) + 0x3b8
2016-Aug-25 20:57:35.021154 3 0x5c9d80 cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector > const&, std::vector >&) + 0x3b8
2016-Aug-25 20:57:35.022687 4 0x601ab4 cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector > const&, std::vector >&, std::unordered_map, std::equal_tocrypto::hash, std::allocator > >&) const + 0x2c
2016-Aug-25 20:57:35.022686 4 0x601ab4 cryptonote::Blockchain::output_scan_worker(unsigned long, std::vector > const&, std::vector >&, std::unordered_map, std::equal_tocrypto::hash, std::allocator > >&) const + 0x2c
2016-Aug-25 20:57:35.024186 5 0x601f0c boost::asio::detail::completion_handler > const&, std::vector >&, std::unordered_map, std::equal_tocrypto::hash, std::allocator > >&>, boost::_bi::list5boost::_bi::value<cryptonote::Blockchain*, boost::_bi::value, boost::_bi::value > const> >, boost::_bi::value > > >, boost::_bi::value, std::equal_tocrypto::hash, std::allocator > > > > > > >::do_complete(boost::asio::detail::task_io_service, boost::asio::detail::task_io_service_operation, boost::system::error_code const&, unsigned long) + 0xa4
2016-Aug-25 20:57:35.024184 5 0x601f0c boost::asio::detail::completion_handler > const&, std::vector >&, std::unordered_map, std::equal_tocrypto::hash, std::allocator > >&>, boost::_bi::list5boost::_bi::value<cryptonote::Blockchain*, boost::_bi::value, boost::_bi::value > const> >, boost::_bi::value > > >, boost::_bi::value, std::equal_tocrypto::hash, std::allocator > > > > > > >::do_complete(boost::asio::detail::task_io_service, boost::asio::detail::task_io_service_operation, boost::system::error_code const&, unsigned long) + 0xa4
2016-Aug-25 20:57:35.025458 6 0x6bd5d8 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1045] + 0x2e8
2016-Aug-25 20:57:35.026183 6 0x6bd5d8 boost::asio::detail::task_io_service::run(boost::system::error_code&) [clone .constprop.1045] + 0x2e8
2016-Aug-25 20:57:35.026874 7 0x5399a0 boost::asio::io_service::run() + 0x28
2016-Aug-25 20:57:35.027595 7 0x5399a0 boost::asio::io_service::run() + 0x28
2016-Aug-25 20:57:35.027921 8 0x7f80d01cf8 boost::this_thread::interruption_requested() + 0x128
2016-Aug-25 20:57:35.029096 8 0x7f80d01cf8 boost::this_thread::interruption_requested() + 0x128
2016-Aug-25 20:57:35.029223 9 0x7f81072fb4 start_thread + 0xa4
2016-Aug-25 20:57:35.030480 9 0x7f81072fb4 start_thread + 0xa4
```


# Discussion History
## radfish | 2016-08-26T23:37:22+00:00
I believe OUTPUT_DNE is harmless.

I've been meaning to look into this exception and suggest to demote it to a fail return code, because it appears to be very frequent.

If your bitmonerod crashes with this as the last output, increase the log level (--log_level 2, or above) and/or run within gdb to get a coredump. My bet is that if it does crash, it won't be related to the OUTPUT_DNE exception.

PS. Please consider using the three backticks in a row to delimit log output snippets here.


## radfish | 2016-08-26T23:39:13+00:00
Btw, without libunwind you won't get a stack trace -- that's the only purpose libunwind is used for.


## ghost | 2016-08-26T23:58:10+00:00
Thanks for the quick reply. Have added the three back ticks.

Soooo...why has my node been up and running just fine for a couple of days if compiled without libunwind available...but when it's available it dumps and crashes in under a minute?

I've just pulled in the latest commits and am compiling my branch with the ARMv8 flags (and no libunwind) to get up to date with the wallet changes.

After that I'll try reinstalling libunwind, recompiling at -O2 with my PR, and then running with --log_level 2 to give you some more info here, but that might not be until tomorrow.


## radfish | 2016-08-27T00:11:02+00:00
> Thanks for the quick reply. So then...why has my node been up and running just fine for a couple of days if compiled without libunwind available...but when it's available it dumps and crashes in under a minute.

To debug the crash you need to get the coredump: run your failing build with `gdb  --args bitmonerod ...` and once it crashes `generate-core-file` and also look at `bt`. My point is that you will not see a stack trace in the log/output in a build without libunwind.

The crash might or might not be related to libunwind, I don't know, but what is certain on my node: OUTPUT_DNE exception happened many times while the node kept running just fine.

I _might_ have experienced the same crash on armv7 which I mentioned to @moneromooo-monero. I was not able to get a coredump for it, because it didn't crash inside gdb.


## radfish | 2016-08-27T00:12:14+00:00
Btw, also try the failing build with `--max-concurrency 1`.


## ghost | 2016-08-27T00:21:18+00:00
Do you mean literally `gdb --args bitmonerod ...` or do I replace `--args` with the `--detach` option and/or the `--max-concurrency 1` option?


## radfish | 2016-08-27T00:23:11+00:00
First, before `gdb`, run `bitmonerod` as you usually do, but add `--max-concurrency 1`, and check if your crash is still happening.

Second experiment: run `gdb --args bitmonerod` folowed by whatever args you normally supply to it, excluding `--detach`.


## moneromooo-monero | 2016-08-28T09:54:30+00:00
> I believe OUTPUT_DNE is harmless.

It is. I agre that using a return code would be a good change.


## radfish | 2016-09-04T01:52:02+00:00
@NanoAkron Any more details on this? Does `--max-concurrency 1` help?


## ghost | 2016-09-04T10:30:53+00:00
I promise to try ASAP but I'm crazy busy this weekend.


## ghost | 2016-09-04T14:32:10+00:00
My bitmonero.conf:

```
log-file=./monero.log
log-level=2
p2p-bind-ip=192.168.xxx.xxx 
p2p-bind-port=18080
max-concurrency=3
out-peers=64
```

Log file with level=2 with max-concurrency=3:

```
2016-Sep-04 15:20:18.645827 Attempting to get output pubkey by global index, but key does not exist
2016-Sep-04 15:20:18.646052 Exception: cryptonote::OUTPUT_DNE
2016-Sep-04 15:20:18.646111 Unwinded call stack:
2016-Sep-04 15:20:18.647591      1                  0x60f2fc __cxa_throw + 0x74
2016-Sep-04 15:20:18.648587      2                  0x6651ac void (anonymous namespace)::throw1<cryptonote:
:OUTPUT_DNE>(cryptonote::OUTPUT_DNE const&) [clone .constprop.1235] + 0xdc
2016-Sep-04 15:20:18.649542      3                  0x598af8 cryptonote::BlockchainLMDB::get_output_key(uns
igned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonot
e::output_data_t, std::allocator<cryptonote::output_data_t> >&) + 0x448
2016-Sep-04 15:20:18.650546      4                  0x5e1ce4 cryptonote::Blockchain::output_scan_worker(uns
igned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::outp
ut_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::trans
action, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, 
cryptonote::transaction> > >&) const + 0x2c
2016-Sep-04 15:20:18.651571      5                  0x5e2d34 boost::asio::detail::completion_handler<boost:
:_bi::bind_t<void, boost::_mfi::cmf4<void, cryptonote::Blockchain, unsigned long, std::vector<unsigned long
, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote:
:output_data_t> >&, std::unordered_map<crypto::hash, cryptonote::transaction, std::hash<crypto::hash>, std:
:equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, cryptonote::transaction> > >&>, boost
::_bi::list5<boost::_bi::value<cryptonote::Blockchain*>, boost::_bi::value<unsigned long>, boost::_bi::valu
e<std::reference_wrapper<std::vector<unsigned long, std::allocator<unsigned long> > const> >, boost::_bi::v
alue<std::reference_wrapper<std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t
> > > >, boost::_bi::value<std::reference_wrapper<std::unordered_map<crypto::hash, cryptonote::transaction,
 std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash const, crypton
ote::transaction> > > > > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::ta
sk_io_service_operation*, boost::system::error_code const&, unsigned long) + 0xa4
2016-Sep-04 15:20:18.652671      6                  0x6614b8 boost::asio::detail::task_io_service::run(boos
t::system::error_code&) [clone .constprop.1093] + 0x2e8
2016-Sep-04 15:20:18.653709      7                  0x54d660 boost::asio::io_service::run() + 0x28
2016-Sep-04 15:20:18.654735      8                  0x7f8893fcf8 boost::this_thread::interruption_requested
() + 0x128
2016-Sep-04 15:20:18.655861      9                  0x7f88cb0fb4 start_thread + 0xa4
```

Changed max-concurrency to 1, still crashing but with a slightly different output:

```
 2016-Sep-04 15:22:21.131162 [P2P1]Attempting to get output pubkey by global index, but key does not exist
2016-Sep-04 15:22:21.131642 [P2P1]Exception: cryptonote::OUTPUT_DNE
2016-Sep-04 15:22:21.131792 [P2P1]Unwinded call stack:
2016-Sep-04 15:22:21.133387 [P2P1]     1                  0x60f2fc __cxa_throw + 0x74
2016-Sep-04 15:22:21.134679 [P2P1]     2                  0x6651ac void (anonymous namespace)::throw1<crypt
onote::OUTPUT_DNE>(cryptonote::OUTPUT_DNE const&) [clone .constprop.1235] + 0xdc
2016-Sep-04 15:22:21.135904 [P2P1]     3                  0x598af8 cryptonote::BlockchainLMDB::get_output_k
ey(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cry
ptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&) + 0x448
2016-Sep-04 15:22:21.137183 [P2P1]     4                  0x5e1ce4 cryptonote::Blockchain::output_scan_work
er(unsigned long, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote
::output_data_t, std::allocator<cryptonote::output_data_t> >&, std::unordered_map<crypto::hash, cryptonote:
:transaction, std::hash<crypto::hash>, std::equal_to<crypto::hash>, std::allocator<std::pair<crypto::hash c
onst, cryptonote::transaction> > >&) const + 0x2c
2016-Sep-04 15:22:21.138306 [P2P1]     5                  0x5f46dc cryptonote::Blockchain::prepare_handle_i
ncoming_blocks(std::__cxx11::list<cryptonote::block_complete_entry, std::allocator<cryptonote::block_comple
te_entry> > const&) + 0x160c
2016-Sep-04 15:22:21.139525 [P2P1]     6                  0x5456b0 cryptonote::t_cryptonote_protocol_handle
r<cryptonote::core>::handle_response_get_objects(int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cr
yptonote::cryptonote_connection_context&) + 0x10a8
2016-Sep-04 15:22:21.140697 [P2P1]     7                  0x6353c0 int epee::net_utils::buff_to_t_adapter<c
ryptonote::t_cryptonote_protocol_handler<cryptonote::core>, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::reques
t, cryptonote::cryptonote_connection_context, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_c
ryptonote_protocol_handler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, crypt
onote::cryptonote_connection_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protoc
ol_handler<cryptonote::core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > > >(cryptonote::t_cryptonote_
protocol_handler<cryptonote::core>*, int, std::__cxx11::basic_string<char, std::char_traits<char>, std::all
ocator<char> > const&, boost::_bi::bind_t<int, boost::_mfi::mf3<int, cryptonote::t_cryptonote_protocol_hand
ler<cryptonote::core>, int, cryptonote::NOTIFY_RESPONSE_GET_OBJECTS::request&, cryptonote::cryptonote_conne
ction_context&>, boost::_bi::list4<boost::_bi::value<cryptonote::t_cryptonote_protocol_handler<cryptonote::
core>*>, boost::arg<1>, boost::arg<2>, boost::arg<3> > >, cryptonote::cryptonote_connection_context&) [clon
e .constprop.483] + 0x3e0
2016-Sep-04 15:22:21.141975 [P2P1]     8                  0x637de0 int nodetool::node_server<cryptonote::t_
cryptonote_protocol_handler<cryptonote::core> >::handle_invoke_map<nodetool::p2p_connection_context_t<crypt
onote::cryptonote_connection_context> >(bool, int, std::__cxx11::basic_string<char, std::char_traits<char>,
 std::allocator<char> > const&, std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<cha
r> >&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool&) [clone .const
prop.448] + 0x1060
2016-Sep-04 15:22:21.143182 [P2P1]     9                  0x6af230 nodetool::node_server<cryptonote::t_cryp
tonote_protocol_handler<cryptonote::core> >::notify(int, std::__cxx11::basic_string<char, std::char_traits<
char>, std::allocator<char> > const&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_
context>&) + 0x38
2016-Sep-04 15:22:21.144314 [P2P1]    10                  0x5053dc epee::levin::async_protocol_handler<node
tool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::handle_recv(void const*, unsig
ned long) + 0x544
2016-Sep-04 15:22:21.145484 [P2P1]    11                  0x50fb24 epee::net_utils::connection<epee::levin:
:async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::
handle_read(boost::system::error_code const&, unsigned long) + 0x994
2016-Sep-04 15:22:21.146541 [P2P1]    12                  0x525230
2016-Sep-04 15:22:21.147575 [P2P1]    13                  0x52962c
2016-Sep-04 15:22:21.148633 [P2P1]    14                  0x4a5824 boost::asio::detail::epoll_reactor::desc
riptor_state::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_opera
tion*, boost::system::error_code const&, unsigned long) + 0x1ac
2016-Sep-04 15:22:21.149704 [P2P1]    15                  0x6614b8 boost::asio::detail::task_io_service::ru
n(boost::system::error_code&) [clone .constprop.1093] + 0x2e8
2016-Sep-04 15:22:21.150759 [P2P1]    16                  0x4cd4a0 epee::net_utils::boosted_tcp_server<epee
::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_contex
t> > >::worker_thread() + 0x128
2016-Sep-04 15:22:21.151822 [P2P1]    17                  0x7f85816cf8 boost::this_thread::interruption_req
uested() + 0x128
2016-Sep-04 15:22:21.153100 [P2P1]    18                  0x7f85b87fb4 start_thread + 0xa4
```

GDB output coming next


## ghost | 2016-09-04T14:37:42+00:00
Ran GDB with all the arguments from my bitcoin.conf, with max-concurrency = 1

```
2016-Sep-04 15:37:04.528714 [P2P6]Attempting to get output pubkey by global index, but key does not exist

Thread 19 "monerod" received signal SIGSEGV, Segmentation fault.
[Switching to Thread 0x7c0baff1e0 (LWP 4097)]
0x000000000070e584 in mdb_txn_reset ()
(gdb) bt
#0  0x000000000070e584 in mdb_txn_reset ()
#1  0x00000000006d87cc in cryptonote::mdb_txn_safe::~mdb_txn_safe() [clone .part.503] [clone .lto_priv.3473] ()
#2  0x0000000000598b18 in cryptonote::BlockchainLMDB::get_output_key(unsigned long const&, std::vector<unsigned long, std::allocator<unsigned long> > const&, std::vector<cryptonote::output_data_t, std::allocator<cryptonote::output_data_t> >&) ()
Backtrace stopped: previous frame inner to this frame (corrupt stack?)
```

What should I try next? Going to go back to the binaries compiled without libunwind.


## radfish | 2016-09-04T16:26:02+00:00
Thanks. Btw, is this on latest master? I thought @moneromooo-monero  changed
something for the OUTPUT_DNE exception to not be thrown (or is that
not merged yet?).

Are you getting only one stack trace, or many of those in a row before
the crash?


## ghost | 2016-09-04T17:27:02+00:00
Hi @radfish, yes I'm a little obsessive in compiling from source ;) Have got everything except the 6 current PRs.

And it's only the one trace as shown before it stops writing to the log file and unceremoniously vanishes from `top`

Would like to know why this happens with libunwind, or is it actually happening all the time in the background and just not getting an exception thrown?


## radfish | 2016-09-16T02:31:40+00:00
The exception happens with or without libunwind, and it is caught silently, this is normal. Perhaps, libunwind stack tracing routines are broken on aarch64, corrupting memory, or perhaps something is broken in the hook on-throw in stack_trace.cpp.

To narrow down a little more, you could try commenting out the body of log_stack_trace function in src/common/stack_trace.cpp and building with libunwind installed. If no crash, likely libunwind is broken, otherwise probably the hook itself is problematic.

In any case, since it does seem to be the culprit, we should probably force-disable STACK_TRACE for aarch64 in CMakeLists.txt.


## ghost | 2016-09-16T23:04:18+00:00
That seems a bit of a 'dirty' fix. Probably best to let it keep crashing for people but keep this issue alive so they can see what's going on.

I'll try your suggestion after I get a little more free time (isn't that what we all say...)


## moneromooo-monero | 2016-10-15T19:38:53+00:00
You can simply add this near the start of smplewallet.c's main:

tools::log_stack_trace("");
throw 0;

This will tell you whether the libunwind code is borked on your machine/arch.


## jonathancross | 2017-10-11T13:47:08+00:00
@NanoAkron Does it still make sense to have this open?

## dEBRUYNE-1 | 2018-01-08T13:01:43+00:00
+invalid

# Action History
- Created by: ghost | 2016-08-26T23:29:51+00:00
- Closed at: 2018-01-08T14:16:32+00:00
