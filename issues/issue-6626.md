---
title: 'command ''rpc_payments'' produces ''Error: Unsuccessful -- json_rpc_request:'''
source_url: https://github.com/monero-project/monero/issues/6626
author: shermand100
assignees: []
labels: []
created_at: '2020-06-04T06:26:35+00:00'
updated_at: '2021-11-20T03:58:25+00:00'
type: issue
status: closed
closed_at: '2020-10-20T14:23:02+00:00'
---

# Original Description
Monero v0.16.0

I cannot find a condition where the 'rpc_payments' command works.

####Starting the node with

`./monerod --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --rpc-restricted-bind-port=18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=43HoAhqx9q3MR1crAjpQtYVhvzQhZgqPwSWVQMmPvYmr18qVUEjCHcsEasuCxS486rWSSg1gbGqanet67NWRsh1bQL9KkB9 --rpc-payment-credits=5 --rpc-payment-difficulty=100 --log-level=3`

Allows free usage for local `status`, `version`, `print_cn` commands which output as expected. however `rpc_payments` fails with `Error: Unsuccessful -- json_rpc_request:` when requested in the same condition as the successful outputs.

The node can see the rpc request and gives a very limited log entry of:

```
2020-06-04 05:59:44.266 I HTTP [192.168.1.132] POST /json_rpc
2020-06-04 05:59:44.266 I [192.168.1.132:46638 INC] Calling RPC method rpc_access_data
```


####Further experimenting:

Starting the node with a more basic:

`./monerod --rpc-bind-ip=0.0.0.0 --rpc-bind-port=18083 --confirm-external-bind --rpc-ssl disabled` 

Gives the same result. Successful output of all status commands except `rpc_payments` so I can't pin it onto a particular start flag.

####Other attempts at finding clues:

gdb output from requesting terminal

(gdb) run --rpc-bind-ip=192.168.1.132 --rpc-bind-port=18083 --rpc-ssl disabled rpc_payments
Starting program: /home/pinodexmr/monero/build/release/bin/monerod --rpc-bind-ip=192.168.1.132 --rpc-bind-port=18083 --rpc-ssl disabled rpc_payments
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/aarch64-linux-gnu/libthread_db.so.1".
2020-06-04 06:19:34.753 I Monero 'Nitrogen Nebula' (v0.16.0.0-release)
[New Thread 0xfffff4bd9d50 (LWP 4889)]
Error: Unsuccessful -- json_rpc_request:
[Thread 0xfffff4bd9d50 (LWP 4889) exited]
[Inferior 1 (process 4886) exited normally]
(gdb) bt full
No stack.
(gdb)

gdb output from running node after sending rpc_payments request several times. Stopped with CTRL+C interrupt.

(gdb) bt full
#0  0x0000fffff7310800 in pthread_cond_wait@@GLIBC_2.17 () from /lib/aarch64-linux-gnu/libpthread.so.0
No symbol table info available.
#1  0x0000aaaaaad98ce8 in boost::condition_variable::wait(boost::unique_lock<boost::mutex>&) ()
No symbol table info available.
#2  0x0000fffff78f611c in boost::thread::join_noexcept() () from /usr/lib/aarch64-linux-gnu/libboost_thread.so.1.67.0
No symbol table info available.
#3  0x0000aaaaab0428d4 in epee::net_utils::boosted_tcp_server<epee::levin::async_protocol_handler<nodetool::p2p_connection_context_t<cryptonote::cryptonote_connection_context> > >::run_server(unsigned long, bool, boost::thread_attributes const&) ()
No symbol table info available.
#4  0x0000aaaaab044174 in nodetool::node_server<cryptonote::t_cryptonote_protocol_handler<cryptonote::core> >::run() ()
No symbol table info available.
#5  0x0000aaaaaadb34e4 in daemonize::t_p2p::run() ()
No symbol table info available.
#6  0x0000aaaaaada09a4 in daemonize::t_daemon::run(bool) ()
No symbol table info available.
#7  0x0000aaaaaadefa4c in daemonize::t_executor::run_interactive(boost::program_options::variables_map const&) ()
No symbol table info available.
#8  0x0000aaaaaadf7608 in bool daemonizer::daemonize<daemonize::t_executor>(int, char const**, daemonize::t_executor&&, boost::program_options::variables_map const&) ()
No symbol table info available.
#9  0x0000aaaaaad6994c in main ()
No symbol table info available.
(gdb)


But I'm don't think any of that helps.

####Duplication of error

Another user seems to have this problem

https://www.reddit.com/r/monerosupport/comments/gvucdk/how_to_start_daemon_with_rpc_pay_and_local_free/

Although he/she may be using my same or similar start command so user error is still a possibility!

Any help appreciated, or I can try to produce a more helpful log if you direct me how.

# Discussion History
## moneromooo-monero | 2020-06-04T12:00:16+00:00
The request goes to the default server, the unrestricted one, which does not have payments enabled. It's kind of a longstanding problem that we have two RPC servers when using --restricted-rpc-port.

## pvols1979 | 2020-06-04T14:10:23+00:00
Is there a command-line option to specify a port so that we specifically request from the restricted RPC port?  Something like './monerod -port 18089 rpc_payments'  

## pvols1979 | 2020-06-04T14:14:31+00:00
When I first started running my node after the RPC-Pay feature was added, I ran in interactive mode without detaching.  This worked excellently.  I would use Screen and swap over to the active session whenever I wanted to run commands against the daemon.  However, rpc_payments was always such a huge return as far as output lines that I could not see every line.  I thought it would be nice to output the return of the list to less or more, but I was unable because I was at the server command line and not the bash prompt.  So, this new feature allowing me to run a restricted and non-restricted port is perfect, I just need this command to work as well as the commands listed above.

## moneromooo-monero | 2020-06-04T14:38:39+00:00
Not yet. Worth adding.

## moneromooo-monero | 2020-06-04T17:35:17+00:00
Oh, and that won't help for this case, since the unrestricted server will have pretty much no activity on it, so its RPC data will be mostly empty, wihch is not what you wanted (you wanted the data from the restricted server).

## pvols1979 | 2020-06-04T18:17:45+00:00
Yes. That is correct. I want the data from the restricted server.

On Thu, Jun 4, 2020 at 12:35 PM moneromooo-monero <notifications@github.com>
wrote:

> Oh, and that won't help for this case, since the unrestricted server will
> have pretty much no activity on it, so its RPC data will be mostly empty,
> wihch is not what you wanted (you wanted the data from the restricted
> server).
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/6626#issuecomment-639000204>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AG2BFC4NITBUAVS2UY5DOT3RU7LOHANCNFSM4NSKCLHA>
> .
>


## shermand100 | 2020-10-20T14:23:02+00:00
The RPC allow free loopback introduced in late has v0.16.x.x fixed this issue.

Example working RPC Pay run command for other that stumble across this (Allows local free status, but external RPC Pay):

./monerod --rpc-bind-ip=$DEVICE_IP --rpc-bind-port=$LOCAL_PORT_BEHIND_FIREWALL --rpc-restricted-bind-port=$RPCPAY_PORT_ACCESSIBLE_THROUGH_FIREWALL --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --rpc-payment-address=$PAYMENT_ADDRESS --rpc-payment-credits=$CREDITS --rpc-payment-difficulty=$DIFFICULTY --detach



## pvols1979 | 2021-11-20T03:58:25+00:00
@shermand100 I am still getting the same error:

./monerod rpc_payments
2021-11-20 03:48:04.617 I Monero 'Oxygen Orion' (v0.17.2.3-release)
Error: Unsuccessful -- json_rpc_request:

I am running with the following options:

./monerod --detach --data-dir /home/test/.bitmonero --log-file /home/test/.bitmonero/node.log --rpc-bind-ip 0.0.0.0 --rpc-bind-port 18081 --rpc-restricted-bind-port 18089 --confirm-external-bind --rpc-payment-allow-free-loopback --rpc-ssl disabled --public-node --rpc-payment-address XXX --rpc-payment-credits 250 --rpc-payment-difficulty 1000 

# Action History
- Created by: shermand100 | 2020-06-04T06:26:35+00:00
- Closed at: 2020-10-20T14:23:02+00:00
