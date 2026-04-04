---
title: Compile monerod for SunOS (SmartOS) - failures - zeromq related
source_url: https://github.com/monero-project/monero/issues/5802
author: kayront
assignees: []
labels: []
created_at: '2019-08-10T14:31:33+00:00'
updated_at: '2022-02-19T04:52:35+00:00'
type: issue
status: closed
closed_at: '2022-02-19T04:52:35+00:00'
---

# Original Description
To get to this point, in src/rpc/zmq_server.h I had to change #include <zmq.hpp> to #include <zmq.h>, since there is no zmq.hpp installed by:

zeromq-4.3.1         The ZeroMQ messaging library

Which was installed from [pkgsrc](https://pkgsrc.org) - the standard way to install packages on SmartOS.

Compilation fails with:

```
[ 34%] Built target rpc_base
[ 35%] Building CXX object src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o
In file included from /home/admin/src/monero/src/rpc/zmq_server.cpp:29:
/home/admin/src/monero/src/rpc/zmq_server.h:73:5: error: 'zmq' does not name a type
     zmq::context_t context;
     ^~~
/home/admin/src/monero/src/rpc/zmq_server.h:77:21: error: 'zmq' was not declared in this scope
     std::unique_ptr<zmq::socket_t> rep_socket;
                     ^~~
/home/admin/src/monero/src/rpc/zmq_server.h:77:34: error: template argument 1 is invalid
     std::unique_ptr<zmq::socket_t> rep_socket;
                                  ^
/home/admin/src/monero/src/rpc/zmq_server.h:77:34: error: template argument 2 is invalid
/home/admin/src/monero/src/rpc/zmq_server.cpp: In constructor 'cryptonote::rpc::ZmqServer::ZmqServer(cryptonote::rpc::RpcHandler&)':                                                                                                         
/home/admin/src/monero/src/rpc/zmq_server.cpp:41:5: error: class 'cryptonote::rpc::ZmqServer' does not have any field named 'context'                                                                                                        
     context(DEFAULT_NUM_ZMQ_THREADS) // TODO: make this configurable                                                                                                                                                                        
     ^~~~~~~
/home/admin/src/monero/src/rpc/zmq_server.cpp: In member function 'void cryptonote::rpc::ZmqServer::serve()':
/home/admin/src/monero/src/rpc/zmq_server.cpp:56:7: error: 'zmq' has not been declared
       zmq::message_t message;
       ^~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:62:24: error: base operand of '->' is not a pointer
       while (rep_socket->recv(&message))
                        ^~
/home/admin/src/monero/src/rpc/zmq_server.cpp:62:32: error: 'message' was not declared in this scope
       while (rep_socket->recv(&message))
                                ^~~~~~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:62:32: note: suggested alternative: 'rusage'                                                                                                                                                   
       while (rep_socket->recv(&message))
                                ^~~~~~~
                                rusage
/home/admin/src/monero/src/rpc/zmq_server.cpp:70:9: error: 'zmq' has not been declared
         zmq::message_t reply(response.size());
         ^~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:71:25: error: 'reply' was not declared in this scope
         memcpy((void *) reply.data(), response.c_str(), response.size());
                         ^~~~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:73:19: error: base operand of '->' is not a pointer
         rep_socket->send(reply);
                   ^~
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:18: error: ISO C++ forbids declaration of 'zmq' with no type [-fpermissive]
     catch (const zmq::error_t& e)
                  ^~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:21: error: expected ')' before '::' token
     catch (const zmq::error_t& e)
           ~         ^~
                     )
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:21: error: expected '{' before '::' token
     catch (const zmq::error_t& e)
                     ^~
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:23: error: '::error_t' has not been declared
     catch (const zmq::error_t& e)
                       ^~~~~~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:23: note: suggested alternative: 'minor_t'
     catch (const zmq::error_t& e)
                       ^~~~~~~
                       minor_t
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:32: error: 'e' was not declared in this scope
     catch (const zmq::error_t& e)
                                ^
/home/admin/src/monero/src/rpc/zmq_server.cpp:82:32: note: suggested alternative: 'el'
     catch (const zmq::error_t& e)
                                ^
                                el
/home/admin/src/monero/src/rpc/zmq_server.cpp: In member function 'bool cryptonote::rpc::ZmqServer::addTCPSocket(std::__cxx11::string, std::__cxx11::string)':
/home/admin/src/monero/src/rpc/zmq_server.cpp:102:16: error: request for member 'reset' in '((cryptonote::rpc::ZmqServer*)this)->cryptonote::rpc::ZmqServer::rep_socket', which is of non-class type 'int'
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
                ^~~~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:102:26: error: 'zmq' does not name a type
     rep_socket.reset(new zmq::socket_t(context, ZMQ_REP));
                          ^~~
/home/admin/src/monero/src/rpc/zmq_server.cpp:104:15: error: base operand of '->' is not a pointer
     rep_socket->setsockopt(ZMQ_RCVTIMEO, &DEFAULT_RPC_RECV_TIMEOUT_MS, sizeof(DEFAULT_RPC_RECV_TIMEOUT_MS));
               ^~
/home/admin/src/monero/src/rpc/zmq_server.cpp:111:15: error: base operand of '->' is not a pointer
     rep_socket->bind(bind_address.c_str());
               ^~
make[2]: *** [src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/build.make:76: src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/zmq_server.cpp.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:1935: src/rpc/CMakeFiles/obj_daemon_rpc_server.dir/all] Error 2
make: *** [Makefile:141: all] Error 2
```

Please advise.

# Discussion History
## vtnerd | 2019-08-10T15:43:11+00:00
`cppzmq` is needed, which is a single header file `zmq.hpp`. I think this can be re-worked, so that only the zmq baseline install is needed. There isn't much gain to the C++ bindings IMO (only a simple struct + `unique_ptr` thing is really needed - light_wallet_server PR is doing this already).

## thomasvaughan | 2019-08-10T15:46:44+00:00
You want cppzmq, which isn't in the official pkgsrc repositories. If you have your own pkgsrc tree, you could make a local/cppzmq directory therein and populate it with the files from [https://github.com/thomasvaughan/cppzmq_pkgsrc/tree/master/cppzmq](https://github.com/thomasvaughan/cppzmq_pkgsrc/tree/master/cppzmq). It's hastily cobbled together, and not up to date, but it's a trivial package, so adapt the distinfo if you want a newer version.

Edit: There's an open pull request to update Monero's cppzmq dependency to 4.3.2, so the above cppzmq pkgsrc files *do* need updating if you want to use them.

## kayront | 2019-08-10T18:10:18+00:00
I see. Thanks for the feedback guys.

Downloaded zmq.hpp from the interwebz and compilation is proceeding. Will open more tickets as necessary should more trouble come to pass.

**I will keep this one open, because** we face an issue here: how to properly have this compile without downloading a random hpp from the internet.

I see three options:

  - Contact the maintainer of the zeromq package and ask to include zmq.hpp in it.

  - Go with @vtnerd's suggestion. What do you all think? Is it easy to change the code?

  - Create a pkgsrc package like @thomasvaughan has and submit it for official inclusion. It will require babysitting until the end of time, but unless the code is changed to not require cppzmq, it's the only option wholly within our power for when the time comes to create a monero package in pkgsrc (which I plan to do once everything compiles & has been tested)

Curious to 'hear' your opinions on this one.

## thomasvaughan | 2019-08-10T18:52:31+00:00

>when the time comes to create a
>monero package in pkgsrc (which I plan to do once everything compiles &
>has been tested)

A pkgsrc build finds its libs and includes in ${WRKDIR}/.buildlink (either as symlinks or as regular files). It's therefore reasonable to suppose that a Monero pkgsrc build would be able to use cppzmq .hpp files in ${WRKSRC}/.buildlink)include; which would eliminate any requirement for a cppzmq package or changes in the Monero source - i.e. do everything from the pkgsrc Makefile. If the cppzmq dependency is just one or two headers, this makes sense.


## kayront | 2019-08-10T19:04:52+00:00
It's been a long time since I dabbled with creating pkgsrc packages, but it should be possible to download the file as part of the general build setup.

If that is the case, then your suggestion could work. In any cause, I have contacted the zeromq pkgsrc maintainer about adding zmq.hpp.

## moneromooo-monero | 2019-08-19T15:24:35+00:00
If the C++ layer is indeed barely needed, feel free to PR a change to remove it. It could also be added as a submodule if it proves to be needed more than that.

## vtnerd | 2019-08-19T17:38:10+00:00
> If the C++ layer is indeed barely needed, feel free to PR a change to remove it. It could also be added as a submodule if it proves to be needed more than that.

https://github.com/monero-project/monero/pull/5818

## moneromooo-monero | 2019-10-10T12:48:50+00:00
Is this fixed ?

## selsta | 2022-02-19T04:52:35+00:00
cppzmq has been dropped

# Action History
- Created by: kayront | 2019-08-10T14:31:33+00:00
- Closed at: 2022-02-19T04:52:35+00:00
