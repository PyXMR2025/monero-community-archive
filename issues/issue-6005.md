---
title: Daemon cannot be restarted on FreeBSD (address already in use)
source_url: https://github.com/monero-project/monero/issues/6005
author: ndorf
assignees: []
labels: []
created_at: '2019-10-22T05:24:34+00:00'
updated_at: '2019-10-24T17:42:13+00:00'
type: issue
status: closed
closed_at: '2019-10-24T17:42:13+00:00'
---

# Original Description
Since commit c9cfbf7fb33f65743c6921580d25d8b7ad2947d6, which replaced the use of `SO_REUSEADDR` with `SO_LINGER` with a zero timeout, the daemon cannot be restarted on FreeBSD 11.3, as binding the p2p port fails:

```
2019-10-22 04:18:52.087      0x806e16000        INFO    net.p2p src/p2p/net_node.inl:833        Binding (IPv4) on 0.0.0.0:28080
2019-10-22 04:18:52.087      0x806e16000        ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:1005  Failed to bind IPv4: bind: Address already in use
2019-10-22 04:18:52.087      0x806e16000        FATAL   net     contrib/epee/include/net/abstract_tcp_server2.inl:1052  Error starting server: Failed to bind IPv4 (set to required)
2019-10-22 04:18:52.087      0x806e16000        ERROR   net.p2p src/p2p/net_node.inl:841        Failed to bind server
2019-10-22 04:18:52.087      0x806e16000        INFO    global  src/daemon/core.h:94    Deinitializing core...
```

`lsof -i` reports that no process is using the port, but the situation persists for a minute or two, after which the daemon can be started again. Reverting the aforementioned commit resolves the problem.

Usually, `SO_LINGER` with a zero timeout is not desirable, as it causes connections to be forcefully aborted when the socket is closed (sending TCP RST instead of FIN, and dropping any still-pending outbound data). `SO_REUSEADDR` is the normal way to bind a listening socket and allow for server restart.

It seems that on Windows this option also allows addresses in active use to be reused -- @xiphon , is that the reason you changed this? If so, I think the right way to fix that is to use their [`SO_EXCLUSIVEADDRUSE`](https://docs.microsoft.com/en-us/windows/win32/winsock/so-exclusiveaddruse) option, in addition to `SO_REUSEADDR`. 





# Discussion History
## xiphon | 2019-10-22T06:28:34+00:00
> `SO_REUSEADDR` is the normal way to bind a listening socket and allow for server restart.

It is not the normal way. Is a clear misuse. If some OS can't/don't handle process termination properly - this should not be "fixed" by misusing `SO_REUSEADDR`.

Please see the unit test i added for this case: https://github.com/monero-project/monero/blob/441ed9f2fef6a43708c115191c51ca16930ce95b/tests/unit_tests/node_server.cpp#L263

Regarding SO_REUSEADDR issue:
1. Run monerod 
with p2p port 18080, rpc port 18081, zmq port 18082
2. Run another monerod instance 
with p2p port 18080, rpc port 18081, zmq port 18083
3. Expected behavior is the second monerod instance to fail binding p2p and rpc ports. But this won't happen due to SO_REUSEADDR.

## xiphon | 2019-10-22T10:26:23+00:00
Is not reproducible on a clean FreeBSD 12.0 system.

## hyc | 2019-10-22T11:27:54+00:00
@xiphon your interpretation of SO_REUSEADDR and SO_LINGER doesn't match any documentation. @ndorf's description is correct.

````
       SO_LINGER
              Sets or gets the SO_LINGER option.  The argument is a linger structure.

                  struct linger {
                      int l_onoff;    /* linger active */
                      int l_linger;   /* how many seconds to linger for */
                  };

              When  enabled,  a  close(2) or shutdown(2) will not return until all queued messages for the socket have been successfully sent or the
              linger timeout has been reached.  Otherwise, the call returns immediately and the closing is done in the background.  When the  socket
              is closed as part of exit(2), it always lingers in the background.

       SO_REUSEADDR
              Indicates that the rules used in validating addresses supplied in a bind(2) call should allow reuse of local addresses.   For  AF_INET
              sockets  this  means that a socket may bind, except when there is an active listening socket bound to the address.
````

## xiphon | 2019-10-22T11:59:50+00:00
> @xiphon your interpretation of SO_REUSEADDR and SO_LINGER doesn't match any documentation. @ndorf's description is correct.

It doesn't match any documentation **you know**.

https://docs.microsoft.com/en-us/windows/win32/api/winsock/nf-winsock-setsockopt

## moneromooo-monero | 2019-10-22T12:27:08+00:00
Then you can put the windows version within #ifdef _WIN32, there's plenty already.

## xiphon | 2019-10-22T12:33:22+00:00
> Then you can put the windows version within #ifdef _WIN32, there's plenty already.

Sure, omw

## xiphon | 2019-10-22T12:34:15+00:00
#6006

## hyc | 2019-10-22T15:21:32+00:00
> It doesn't match any documentation you know.

The sockets API comes from BSD Unix. The fact that Microsoft copied it incorrectly in Winsock is their bug.

## ndorf | 2019-10-22T16:19:41+00:00
> It is not the normal way. Is a clear misuse. If some OS can't/don't handle process termination properly - this should not be "fixed" by misusing SO_REUSEADDR.

It's the normal and correct way, not a misuse of any kind. There also isn't any issue with handling of process termination here: clean shutdown of a TCP connection takes time, so it's perfectly normal for the socket to remain in `TIME_WAIT` state after the process exits. `SO_REUSEADDR` deals with exactly this situation, by allowing endpoints _that are in the `TIME_WAIT` state_ to be reused. This is the intended purpose of the option.

The only problem seems to be that Windows has implemented this option incorrectly, allowing any endpoints to be reused instead of only ones in `TIME_WAIT` state. But, they also have the additional option `SO_EXCLUSIVEADDRUSE` to fix that. So, `SO_REUSEADDR` on Unix and `(SO_REUSEADDR | SO_EXCLUSIVEADDRUSE)` on Windows should be correct.

`SO_LINGER`, on the other hand, has usually undesirable effects. With timeout 0, it causes all connections to be forcibly aborted instead of cleanly shut down. With timeout > 0, it causes close() to wait and possibly return errors if the peer hasn't caught up. Neither of these are necessary or desirable just to have the server be able to restart. So, if anything is a clear misuse, it's this use of linger to work around a broken `SO_REUSEADDR` option -- especially if a solution without side-effects (`SO_EXCLUSIVEADDRUSE`) exists.

## ndorf | 2019-10-22T18:58:31+00:00
According to [this Microsoft article](https://docs.microsoft.com/en-us/windows/win32/winsock/using-so-reuseaddr-and-so-exclusiveaddruse), `SO_LINGER` shouldn't be used for the same reasons I stated above. However, it also says that `SO_REUSEADDR` shouldn't be used either, and it looks like `SO_EXCLUSIVEADDRUSE` might not work as I thought, to boot. So I don't know what the solution is for Windows after all. Maybe it even works as desired without any options? On Unix, though, it's clear: `SO_REUSEADDR`, and leave linger as the default.

> The SO_LINGER socket option may be set on a socket to prevent the port from transitioning to an "active" wait state; however, this is discouraged as it can lead to desired effects, such as reset connections. For example, if data is received by the peer but remains unacknowledged by it, and the local computer closes the socket with SO_LINGER set on it, the connection between the two computers is reset and the unacknowledged data discarded by the peer. Picking a suitable time to linger is difficult as a smaller timeout value often results in suddenly aborted connections, whereas larger timeout values leave the system vulnerable to denial-of-service attacks (by establishing many connections and potentially stalling/blocking application threads). Closing a socket that has a nonzero linger timeout value may also cause the closesocket call to block.

and

> The SO_REUSEADDR option has very few uses in normal applications aside from multicast sockets where data is delivered to all of the sockets bound on the same port. Otherwise, any application that sets this socket option should be redesigned to remove the dependency since it is eminently vulnerable to "socket hijacking". As long as SO_REUSEADDR socket option can be used to potentially hijack a port in a server application, the application must be considered to be not secure.



## xiphon | 2019-10-22T18:59:13+00:00
@ndorf 

In my world server restart is a typical use case. Having to set some flag on a socket just to be able to restart the server sounds ... at least weird. But don't want to start *nix vs Windows holy war on this topic.

Anyway the desired goal is to have monerod operating the way we want i.e.
1) should support immediate restart
2) while monerod is running an attempt to run another monerod instance on the same port should fail

So we would have to set `SO_REUSEADDR` on *nix.
Windows will handle everything correctly without any additional flags needed.

EDIT:
Didn't see your post at the time of writing. Yep, meant the same.

> Maybe it even works as desired without any options? On Unix, though, it's clear: SO_REUSEADDR, and leave linger as the default.

## ndorf | 2019-10-22T19:17:33+00:00
@xiphon 

> In my world server restart is a typical use case. Having to set some flag on a socket just to be able to restart the server sounds ... at least weird. But don't want to start *nix vs Windows holy war on this topic.

It is weird, but this API dates back to 1983. On the other hand, copying the API and reusing the same flag name for a different and mostly broken purpose seems not just weird, but evil! :)

Agree with everything else, glad to see a clean solution that works everywhere.

# Action History
- Created by: ndorf | 2019-10-22T05:24:34+00:00
- Closed at: 2019-10-24T17:42:13+00:00
