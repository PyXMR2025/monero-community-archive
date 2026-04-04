---
title: Unable to exit daemon when running with torsocks
source_url: https://github.com/monero-project/monero/issues/5098
author: Jasonhcwong
assignees: []
labels: []
created_at: '2019-01-27T10:49:29+00:00'
updated_at: '2019-01-28T20:33:36+00:00'
type: issue
status: closed
closed_at: '2019-01-28T20:33:36+00:00'
---

# Original Description
When running with torsocks,  monerod starts syncing and responds to commands like "status".
But when I tried to quit the daemon with command "exit".  
The daemon keeps running.   Console stopped printing "sync messages" like "Synced 1672843/1758084 (95% 85241 blocks remaining)"   
I sent SIGTERM after some minutes.  
The daemon still running until being killed by SIGKILL. 

````
status
2019-01-27 10:26:00.301	[P2P2]	INFO 	global	src/cryptonote_protocol/cryptonote_protocol_handler.inl:1179	[138.197.182.105:18080 OUT]  Synced 1672843/1758084 (95% 85241 blocks remaining)
Height: 1672823/1758084 (95.2%) on mainnet, not mining, net hash 615.02 MH/s, v7, up to date, 5(out)+0(in) connections, uptime 0d 0h 16m 43s
exit
Stop signal sent

````  


I also tried to run the daemon in non-interactive mode under systemd, it is not responding to SIGTERM also.  
 
gdb bt after sending SIGTERM and waiting for some minutes
````
(gdb) bt
#0  0x0000007f7d87222c in pthread_cond_wait@@GLIBC_2.17 ()
   from /lib/aarch64-linux-gnu/libpthread.so.0
#1  0x0000005592441520 in boost::thread::join_noexcept() ()
#2  0x0000005591fab91c in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
#3  0x0000005591facd14 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
#4  0x0000005591de7408 in daemonize::t_p2p::run() ()
#5  0x0000005591ddc0f8 in daemonize::t_daemon::run(bool) ()
#6  0x0000005591e635d4 in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
#7  0x0000005591e6a9bc in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
#8  0x0000005591db15b4 in main ()
````

# Discussion History
## moneromooo-monero | 2019-01-27T15:41:31+00:00
One of the threads is likely timing out in a connect call. torsocks is a bit of a jerk with those...

## Jasonhcwong | 2019-01-27T23:11:58+00:00
I am worried about the forceful SIGKILL may cause database corruption....  
a graceful shutdown is more preferable.

## moneromooo-monero | 2019-01-28T11:10:51+00:00
It will not, LMDB is designed to withstand those.

# Action History
- Created by: Jasonhcwong | 2019-01-27T10:49:29+00:00
- Closed at: 2019-01-28T20:33:36+00:00
