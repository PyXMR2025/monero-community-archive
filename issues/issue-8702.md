---
title: 'Exception: boost::wrapexcept<boost::bad_weak_ptr> during synchronization'
source_url: https://github.com/monero-project/monero/issues/8702
author: ovhpse
assignees: []
labels: []
created_at: '2023-01-07T10:41:20+00:00'
updated_at: '2024-07-30T20:14:49+00:00'
type: issue
status: closed
closed_at: '2023-01-21T09:49:01+00:00'
---

# Original Description
Hello,

Following #8690,

When I build Monero myself, there is exceptions that are preventing a successful synchronization. Meanwhile if I install the Monero release on the same server (release-v0.18, the same as the branch I build), the synchronization go forward without issue. Therefore this cannot be a system related issue.




```
Exception: boost::wrapexcept<boost::bad_weak_ptr>
Unwound call stack:
     1                  0x557a0a101559 __wrap___cxa_throw + 0xbf

     2                  0x557a09b38458 void boost::throw_exception<boost::bad_weak_ptr>(boost::bad_weak_ptr const&) + 0x57

     3                  0x557a09b26536 boost::detail::shared_count::shared_count(boost::detail::weak_count const&) + 0x84

     4                  0x557a09f71809 boost::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::shared_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >(boost::weak_ptr<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > > const&) + 0x2f

     5                  0x557a09f67251 boost::enable_shared_from_this<epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::shared_from_this() + 0x27

     6                  0x557a09fbff0b epee::net_utils::connection<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::add_ref() + 0x39

     7                  0x557a09f28b76 epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::start_outer_call() + 0xfe

     8                  0x557a09f1d386 bool epee::levin::async_protocol_handler_config<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> >::foreach_connection<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_addr_connected(epee::net_utils::network_address const&)::{lambda(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&)#1}>(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_addr_connected(epee::net_utils::network_address const&)::{lambda(nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> const&)#1} const&) + 0x10e

     9                  0x557a09ee3eb5 nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::is_addr_connected(epee::net_utils::network_address const&) + 0xc3

     a                  0x557a09f19afd bool nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connect_to_peerlist<std::__cxx11::list<epee::net_utils::network_address, std::allocator<epee::net_utils::network_address> > >(std::__cxx11::list<epee::net_utils::network_address, std::allocator<epee::net_utils::network_address> > const&) + 0xad

     b                  0x557a09edf63c nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::connections_maker() + 0x19a

     c                  0x557a09f55511 boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >::operator()(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*) const + 0x69

     d                  0x557a09f4373e bool boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> >::operator()<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >&, boost::_bi::list0&, long) + 0x52

     e                  0x557a09f313ce boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > >::operator()() + 0x48

     f                  0x557a09f1945a bool epee::math_helper::once_a_time<epee::math_helper::get_constant_interval<1000000ul>, true>::do_call<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >(boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > >) + 0x44

    10                  0x557a09ede7aa nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::idle_worker() + 0x142

    11                  0x557a09f55511 boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >::operator()(nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*) const + 0x69

    12                  0x557a09f4373e bool boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> >::operator()<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >&, boost::_bi::list0&, long) + 0x52

    13                  0x557a09f313ce boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > >::operator()() + 0x48

    14                  0x557a09f3e70c epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >::call_handler() + 0x20

    15                  0x557a09f29075 bool epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::global_timer_handler<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > >(boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > >) + 0x43

    16                  0x557a09f9007c boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >::operator()(epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > >) const + 0x9a

    17                  0x557a09f8c999 bool boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > >::operator()<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::rrlist1<boost::system::error_code const&> >(boost::_bi::type<bool>, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >&, boost::_bi::rrlist1<boost::system::error_code const&>&, long) + 0x91

    18                  0x557a09f89667 bool boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >::operator()<boost::system::error_code const&>(boost::system::error_code const&) + 0x53

    19                  0x557a09f86063 boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>::operator()() + 0x27

    1a                  0x557a09f815e3 void boost::asio::asio_handler_invoke<boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code> >(boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>&, ...) + 0x74

    1b                  0x557a09f7cc64 void boost_asio_handler_invoke_helpers::invoke<boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>, boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > > >(boost::asio::detail::binder1<boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >, boost::system::error_code>&, boost::_bi::bind_t<bool, boost::_mfi::mf1<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >, boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > >, boost::_bi::list2<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*>, boost::_bi::value<boost::shared_ptr<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::idle_callback_conext<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> > >, boost::_bi::list1<boost::_bi::value<nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >*> > > > > > > >&) + 0x37

    1c                  0x557a09f78906

    1d                  0x557a09f737cc

    1e                  0x557a09b28f56 boost::asio::detail::scheduler_operation::complete(void*, boost::system::error_code const&, unsigned long) + 0x3a

    1f                  0x557a09b2d069 boost::asio::detail::scheduler::do_run_one(boost::asio::detail::conditionally_enabled_mutex::scoped_lock&, boost::asio::detail::scheduler_thread_info&, boost::system::error_code const&) + 0x1c3

    20                  0x557a09b2c5d1 boost::asio::detail::scheduler::run(boost::system::error_code&) + 0x147

    21                  0x557a09b2d619 boost::asio::io_context::run() + 0x4d

    22                  0x557a09f29af9 epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::worker_thread() + 0x12f

    23                  0x557a09fc19e1 boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >::operator()(epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*) const + 0x69

    24                  0x557a09fc13ee bool boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*> >::operator()<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, boost::_bi::list0>(boost::_bi::type<bool>, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >&, boost::_bi::list0&, long) + 0x52

    25                  0x557a09fc067e boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*> > >::operator()() + 0x48

    26                  0x557a09fbec6e boost::detail::thread_data<boost::_bi::bind_t<bool, boost::_mfi::mf0<bool, epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > > >, boost::_bi::list1<boost::_bi::value<epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >*> > > >::run() + 0x22

    27                  0x557a0a432dcb thread_proxy + 0x7b

    28                  0x7f6f298ae14d start_thread + 0x2cd

    29                  0x7f6f2992ebb4 __clone + 0x44
```

# Discussion History
## selsta | 2023-01-08T00:31:22+00:00
>Meanwhile if I install the Monero release on the same server

do you mean the binary from getmonero.org?

## ovhpse | 2023-01-08T09:04:07+00:00
Yes, to be precise I installed:
https://downloads.getmonero.org/cli/monero-linux-x64-v0.18.1.2.tar.bz2

While not a C++ dev myself, looking at the code it seem the exception shall be catch:

```
  template<typename T>
  bool connection<T>::add_ref()
  {
    try {
      auto self = connection<T>::shared_from_this();
      std::lock_guard<std::mutex> guard(m_state.lock);
      this->self = std::move(self);
      ++m_state.protocol.reference_counter;
      return true;
    }
    catch (boost::bad_weak_ptr &exception) {
      return false;
    }
  }
```

https://github.com/monero-project/monero/blob/master/contrib/epee/include/net/abstract_tcp_server2.inl

Also I have this kind of messages in dmesg:

```segfault at 0 ip 00007fb2aa8b45ea sp 00007f8b7c4fabc8 error 4 in libc.so.6[7fb2aa769000+156000]```

## afungible | 2023-01-08T19:29:39+00:00
@selsta 
Apparently, I get a similar exception when starting monero daemon. I wonder if it is related to above or something to do with my database. If it is an actual issue, then I can raise it separately if needed.

`[P2P0]	INFO	stacktrace	src/common/stack_trace.cpp:133	Exception: boost::wrapexcept<boost::bad_weak_ptr>`

The stack trace shows me "addresses", but not the actual function names I'd have expected. I tried to demangle the addresses using, 
`echo "0x562cf638d57a" | addr2line -e monerod --pretty-print`
but ended up getting gibberish.

Attached is the log with log_level=1.
[error_while_starting_monerod.txt](https://github.com/monero-project/monero/files/10369302/error_while_starting_monerod.txt)

Any help is appreciated.

Note: v0.18.1.2, compiled from source.

## afungible | 2023-01-08T19:36:17+00:00
Ok, I just verified. When I used the latest monerod bin directly from getmonero, I don't see this exception. But when I compiled it myself on Ubuntu 18, then I can see exception similar to what OP has raised (but without stack_trace function names, in my case) - so, I am unable to say with certainty if this issue is same as what OP has reported.

## ovhpse | 2023-01-14T10:44:25+00:00
@afungible 

Happy to see that you can reproduce. Me too I has no stack trace at the beginning, but I found a workaround described in #8690 

## ovhpse | 2023-01-15T10:06:06+00:00
Adding one check in `add_ref()` solve the issue for the moment:

https://github.com/monero-project/monero/blob/50aa0e8b7f11680be3954c176f2daa9ccf77b7dd/contrib/epee/include/net/abstract_tcp_server2.inl#L1100

```
  template<typename T>
  bool connection<T>::add_ref()
  {
    try {
      if (connection<T>::weak_from_this().expired())
        return false;
      auto self = connection<T>::shared_from_this();
      std::lock_guard<std::mutex> guard(m_state.lock);
      this->self = std::move(self);
      ++m_state.protocol.reference_counter;
      return true;
    }
    catch (boost::bad_weak_ptr &exception) {
      return false;
    }
  }
```

Not being well versed in C++ concurrency myself I don't know if it's a good solution.

## vtnerd | 2023-01-16T00:03:56+00:00
@ovhpse The change should be a red-herring. `::shared_from_this()` should throw if `expired() == true`.

## ovhpse | 2023-01-21T09:49:01+00:00
Hello,

For all the hobbyists out there who wanted to build Monero by themselves and got this issue, the origin of the problem come from this block of code:

https://github.com/monero-project/monero/blob/50aa0e8b7f11680be3954c176f2daa9ccf77b7dd/CMakeLists.txt#L528-L553

Depending on the platform you build on, for example if you build on Linux x86_64 with GCC, the build process will substitute `__cxa_throw` with a custom implementation that print stack traces even for exceptions which are handled properly by catch blocks as part of the intended control flow of the code.

You can add `-D STACK_TRACE=OFF` to your build to prevent this.

## thisIsNotTheFoxUrLookingFor | 2024-07-30T20:14:48+00:00
Good to know thanks, I am compiling on Ubuntu and getting smashed with these. I will rebuild with -D STACK_TRACE=OFF because I think all the constant stack traces are crippling my machine haha

# Action History
- Created by: ovhpse | 2023-01-07T10:41:20+00:00
- Closed at: 2023-01-21T09:49:01+00:00
