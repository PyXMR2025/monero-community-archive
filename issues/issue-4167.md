---
title: 'Monero wallet RPC: output already exists with unspent X, received output ignored'
source_url: https://github.com/monero-project/monero/issues/4167
author: got3nks
assignees: []
labels: []
created_at: '2018-07-22T19:10:49+00:00'
updated_at: '2019-08-21T11:22:13+00:00'
type: issue
status: closed
closed_at: '2018-08-15T11:33:01+00:00'
---

# Original Description
Our hot wallet is receiving transactions like these:

```
[RPC0]  WARN    wallet.wallet2  src/wallet/wallet2.cpp:1272     Received money: yy.yy, with tx: <xxxxxxx>
[RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1282     Public key zzzzzz from received 0.000000000000 output already exists with unspent yy.yy, received output ignored
[RPC0]  ERROR   wallet.wallet2  src/wallet/wallet2.cpp:1282     Public key zzzzzz from received 0.000000000000 output already exists with unspent yy.yy, received output ignored
```

The transaction hashes shown as confirmed in the Monero blockchain (as in mined in blocks) but amounts are not reflected in our wallet balance. **This is causing transactions to be processed by our system while no XMR is received!**

# Discussion History
## stoffu | 2018-07-23T07:35:29+00:00
This issue is fixed in both the master and the release branches.

## got3nks | 2018-07-23T09:12:17+00:00
Does it mean the XMR was actually received or not by our wallet?

## moneromooo-monero | 2018-07-23T10:08:29+00:00
AFAIK this happens when someone reuses a one time key. This is real monero, but it is unspendable, so the wallt marks it as such. It's the sender burning monero. Or there is a bug somewhere.
Can you give an example pair of txids this happens for ?

## moneromooo-monero | 2018-07-23T10:13:15+00:00
Actually, stoffu's right, it can be triggered by a bug that was fixed a couple weeks ago. Use the current 0.12.3.0 version, which is fixed. Otherwise you can get scammed.

## gituser | 2018-07-23T13:59:01+00:00
guys, you could announce such security issue on reddit and everywhere else..

millions of dollars could be lost due such a bug, seriously.. :(

also, why don't you mark `v0.12.3.0` as the latest release ?

## got3nks | 2018-07-23T15:50:26+00:00
Indeed we processed many transactions with such bug. Are the XMR lost forever?

Why it wasn’t announced on Reddit or other social media a critical update is available? Those transactions look 100% legit when looking them up with the standard RPC calls.

## moneromooo-monero | 2018-07-23T15:55:25+00:00
The blockchain is not affected, it's just a reporting bug.
I've no idea about reddit and other random sites. It should have been posted on the announce mailing list, but that didn't get done, which is wrong, but hey, first time. Hopefully this will get fixed next time.
Also, I originally fixed this without a release following because I didn't realize at the time that it was affecting RPC, I thought it was display only, so that compounded the after effects.
Also, 0.12.3.0 is the latest release on getmonero.org. If you're talking about other sites, then ask them.


## got3nks | 2018-07-23T17:24:28+00:00
Just upgraded to 0.12.3.0, it doesn't look fixed. While querying **get_bulk_payments** for incoming payments those txs are still shown as valid transactions.

```
array (
  'address' => '********************************************************************',
  'amount' => ************,
  'block_height' => ********,
  'payment_id' => '*********',
  'subaddr_index' => 
  array (
    'major' => 0,
    'minor' => 0,
  ),
  'tx_hash' => '**********************************',
  'unlock_time' => 0,
)
```

## moneromooo-monero | 2018-07-23T18:37:19+00:00
That's because it does not rescan the whole blockchain every tim you call get_bulk_payments. Remove the cache file, and let it rescan.
Note: This will lose other metadata such as which addresses you sent to, and the tx keys.

## got3nks | 2018-07-23T18:58:44+00:00
Which files exactly?

## moneromooo-monero | 2018-07-23T19:05:34+00:00
If your keys file is called FOO.keys, it's the FOO file.

## got3nks | 2018-07-23T19:07:52+00:00
root@server:~# ls /home/monero/ | grep Wallet

```
Wallet <-- this one
Wallet.address.txt
Wallet.keys
Wallet.unportable
```

Figured out which one it is and updated the message

`Jul 23 19:19:59 monero-wallet-rpc[21056]: 2018-07-23 19:19:59.857            7fc5e0b3f740        WARN         wallet.wallet2        src/wallet/wallet2.cpp:3789        file not found: /home/monero/Wallet, starting with empty blockchain`

## gituser | 2018-07-23T19:34:39+00:00
@moneromooo-monero 
>The blockchain is not affected, it's just a reporting bug.

Sure, but many automated exchanges lost money because of this. We lost about 100 XMR.

>I've no idea about reddit and other random sites. It should have been posted on the announce mailing list, but that didn't get done, which is wrong, but hey, first time. Hopefully this will get fixed next time.

OK, mailing list would be good too, though I'm quite sure reddit is also a good place to post the link to the announcement.

>Also, I originally fixed this without a release following because I didn't realize at the time that it was >affecting RPC, I thought it was display only, so that compounded the after effects.

Yes, and thank you for that!

>Also, 0.12.3.0 is the latest release on getmonero.org. If you're talking about other sites, then ask them.

Not on github! Latest version there still is 0.12.2.0! And I have a script which specifically checks your github to check for the latest version and this time it didn't work because the latest version didn't change..

I think you need to make latest 0.12.3.0 and make a bold RED announcement regarding the change and also warn many other sites which might rely on wallet-rpc data..

## gituser | 2018-07-23T19:39:14+00:00
>That's because it does not rescan the whole blockchain every tim you call get_bulk_payments. Remove the cache file, and let it rescan. Note: This will lose other metadata such as which addresses you sent to, and the tx keys.

I did rescan our wallet to make sure that new wallet will display correctly last few transactions and on block `1514998` monerod crashed.

There you go the crashlog - https://paste.fedoraproject.org/paste/48AGfZ-iw9N-BGlPJU1Imw/raw (probably I should file a separate issue).
EDIT: it seems it crashed yet again! I've started now with re-synced wallet will see how it goes..

@got3nks does v0.12.3.0 crashes main monerod daemon for you with your old wallet?

## got3nks | 2018-07-23T20:02:18+00:00
> Sure, but many automated exchanges lost money because of this. We lost about 100 XMR.

True, and no warning has been issued yet on social media / getmonero.org website. 
Maybe some services are still using the affected Monero node version and vulnerable to this attack.

EDIT: Removed the cache and finished re-sync just now. All transactions still appear on **get_bulk_payments**.

`@got3nks does v0.12.3.0 crashes main monerod daemon for you with your old wallet?`
No it didn't crash here.

## moneromooo-monero | 2018-07-23T20:28:52+00:00
> Not on github! Latest version there still is 0.12.2.0! And I have a script which specifically checks your github to check for the latest version and this time it didn't work because the latest version didn't change..

Hmm. I see 0.12.3.0 last, though 0.12.2.0 seems highlighted somehow. I've no idea how that works, I'll ping fluffypony about it.

> I did rescan our wallet to make sure that new wallet will display correctly last few transactions and on block 1514998 monerod crashed.

Known bug, it crashes for some people, and harmless for others. It is fixed by https://github.com/monero-project/monero/pull/4130

> EDIT: Removed the cache and finished re-sync just now. All transactions still appear on get_bulk_payments.

Yes, they should, but they also should have the correct amount now.


## moneromooo-monero | 2018-07-23T20:59:13+00:00
OK, that's bad.
Give a sample txid with the problem.


## moneromooo-monero | 2018-07-23T21:00:15+00:00
And get on Freenode IRC in #monero if you can, faster to chat.

## got3nks | 2018-07-23T21:02:48+00:00
Sorry, I double checked and it's indeed showing a different amount, exactly half of what was reported before. This is correct?

## moneromooo-monero | 2018-07-23T22:37:41+00:00
It depends. It should show the correct amount. The "received money" lines was always right, if you want to compare.

## gituser | 2018-07-24T07:38:33+00:00
v0.12.3.0 is still crashing for us..

monerod log ends with:
```
018-07-23 20:27:09.145	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:124	Exception: std::bad_alloc
2018-07-23 20:27:09.145	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:125	Unwound call stack:
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [1] /home/monero/monerod:__wrap___cxa_throw+0x94 [0x557437f3d8a4]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [2] /home/monero/monerod+0x9704a9 [0x5574382f14a9]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [3] /home/monero/monerod:std::string::_Rep::_S_create(unsigned long, unsigned long, std::allocator<char> const&)+0x59 [0x557438337879]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [4] /home/monero/monerod:std::string::_Rep::_M_clone(std::allocator<char> const&, unsigned long)+0x1b [0x5574383384eb]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [5] /home/monero/monerod:std::basic_string<char, std::char_traits<char>, std::allocator<char> >::basic_string(std::string const&)+0x3c [0x557438338c7c]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [6] /home/monero/monerod:std::_Rb_tree_iterator<std::pair<std::string const, unsigned int> > std::_Rb_tree<std::string, std::pair<std::string const, unsigned int>, std::_Select1st<std::pair<std::string const, unsigned int> >, std::less<std::string>, std::allocator<std::pair<std::string const, unsigned int> > >::_M_emplace_hint_unique<std::piecewise_construct_t const&, std::tuple<std::string const&>, std::tuple<> >(std::_Rb_tree_const_iterator<std::pair<std::string const, unsigned int> >, std::piecewise_construct_t const&, std::tuple<std::string const&>&&, std::tuple<>&&)+0x43 [0x557437c93e13]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [7] /home/monero/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::host_count(std::string const&, int)+0x3bc [0x557437e31c1c]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [8] /home/monero/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::shutdown()+0x177 [0x557437e322f7]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [9] /home/monero/monerod:epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::close()+0xf3 [0x557437e32443]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [10] /home/monero/monerod:epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::close(boost::uuids::uuid)+0x3d2 [0x557437e0c332]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [11] /home/monero/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::do_handshake_with_peer(unsigned long&, nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context>&, bool)+0x266 [0x557437e54676]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [12] /home/monero/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::try_to_connect_and_handshake_with_new_peer(epee::net_utils::network_address const&, bool, unsigned long, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::PeerType, unsigned long)+0x704 [0x557437e650f4]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [13] /home/monero/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_seed()+0x12d [0x557437e6798d]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [14] /home/monero/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker()+0x415 [0x557437e68235]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [15] /home/monero/monerod:nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker()+0x80 [0x557437e02250]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [16] /home/monero/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base>)+0x33 [0x557437e1afe3]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [17] /home/monero/monerod:boost::asio::detail::wait_handler<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext_base> > > > >::do_complete(boost::asio::detail::task_io_service*, boost::asio::detail::task_io_service_operation*, boost::system::error_code const&, unsigned long)+0x13c [0x557437e030ac]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [18] /home/monero/monerod:boost::asio::detail::task_io_service::do_run_one(boost::asio::detail::scoped_lock<boost::asio::detail::posix_mutex>&, boost::asio::detail::task_io_service_thread_info&, boost::system::error_code const&)+0x313 [0x557437c624a3]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [19] /home/monero/monerod:epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread()+0x251 [0x557437e18301]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [20] /home/monero/monerod+0x9472fa [0x5574382c82fa]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [21] /lib/x86_64-linux-gnu/libpthread.so.0+0x8064 [0x7fd68a024064]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	    [22] /lib/x86_64-linux-gnu/libc.so.6:clone+0x6d [0x7fd689a5862d]
2018-07-23 20:27:09.149	[P2P6]	INFO 	stacktrace	src/common/stack_trace.cpp:163	
```
```
[3972060.785545] monerod[11377]: segfault at 18 ip 00007fd6899e8ab5 sp 00007fd67dbf7f90 error 4 in libc-2.19.so[7fd689970000+1a1000]
```
We run monerod with: `/home/monero/monerod --block-sync-size 5 --out-peers 200 --data-dir /home/monero/.monero --log-file /home/monero/.monero/monero_product.log --log-level 0 --rpc-bind-ip 127.0.0.1 --rpc-bind-port 18081 --no-igd --hide-my-port --detach`

Though we're building our own from the source, trying now to update the boost to v1.67 and see how it will go with the latest boost, though before there was never a problem with boost v1.62.

## moneromooo-monero | 2018-07-24T09:31:43+00:00
Cherry pick 4130, it fixes this.

## gituser | 2018-07-24T19:32:29+00:00
@moneromooo-monero yes, thank you! seems this fixed it. 

Also, built with boost v1.67, stable so far.

Would be nice if you could reflect this in the README.md of the main repository as well (it still states that you should build v0.12.2.0).

## moneromooo-monero | 2018-08-15T11:09:51+00:00
+resolved

## StefanIsidorovic | 2019-08-21T11:22:13+00:00
> Actually, stoffu's right, it can be triggered by a bug that was fixed a couple weeks ago. Use the current 0.12.3.0 version, which is fixed. Otherwise you can get scammed.

Do you remember which fix exactly?

# Action History
- Created by: got3nks | 2018-07-22T19:10:49+00:00
- Closed at: 2018-08-15T11:33:01+00:00
