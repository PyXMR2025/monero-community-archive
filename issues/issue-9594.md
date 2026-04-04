---
title: RPC connectivity stops for good in high traffic
source_url: https://github.com/monero-project/monero/issues/9594
author: moneromooo-monero
assignees: []
labels:
- important
- discussion
created_at: '2024-11-25T14:24:51+00:00'
updated_at: '2025-01-22T08:55:23+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
I've been debugging it on and off in Townforge for quite a long time, as I thought it was specific to my changes, but I can actually get it to happen in Monero reliably. Townforge has quite heavy TF specific functional tests, which trigger is reliably, and I got Monero to trigger it reliably by simply calling a RPC over and over, with this patch:

```
diff --git a/tests/functional_tests/daemon_info.py b/tests/functional_tests/daemon_info.py
index 9d645330d..94ef57c5f 100755
--- a/tests/functional_tests/daemon_info.py
+++ b/tests/functional_tests/daemon_info.py
@@ -50,7 +50,8 @@ class DaemonGetInfoTest():
         print('Test hard_fork_info')
 
         daemon = Daemon()
-        res = daemon.hard_fork_info()
+        while True:
+            res = daemon.hard_fork_info()
 
         # hard_fork version should be set at height 1
         assert 'earliest_height' in res.keys()
diff --git a/tests/functional_tests/functional_tests_rpc.py b/tests/functional_tests/functional_tests_rpc.py
index e483352a4..449512339 100755
--- a/tests/functional_tests/functional_tests_rpc.py
+++ b/tests/functional_tests/functional_tests_rpc.py
@@ -52,7 +52,7 @@ WALLET_DIRECTORY = builddir + "/functional-tests-directory"
 FUNCTIONAL_TESTS_DIRECTORY = builddir + "/tests/functional_tests"
 DIFFICULTY = 10
 
-monerod_base = [builddir + "/bin/monerod", "--regtest", "--fixed-difficulty", str(DIFFICULTY), "--no-igd", "--p2p-bind-port", "monerod_p2p_port", "--rpc-bind-port", "monerod_rpc_port", "--zmq-rpc-bind-port", "monerod_zmq_port", "--zmq-pub", "monerod_zmq_pub", "--non-interactive", "--disable-dns-checkpoints", "--check-updates", "disabled", "--rpc-ssl", "disabled", "--data-dir", "monerod_data_dir", "--log-level", "1"]
+monerod_base = [builddir + "/bin/monerod", "--regtest", "--fixed-difficulty", str(DIFFICULTY), "--no-igd", "--p2p-bind-port", "monerod_p2p_port", "--rpc-bind-port", "monerod_rpc_port", "--zmq-rpc-bind-port", "monerod_zmq_port", "--zmq-pub", "monerod_zmq_pub", "--non-interactive", "--disable-dns-checkpoints", "--check-updates", "disabled", "--rpc-ssl", "disabled", "--data-dir", "monerod_data_dir", "--log-level", "3"]
 monerod_extra = [
   ["--offline"],
   ["--rpc-payment-address", "44SKxxLQw929wRF6BA9paQ1EWFshNnKhXM3qz6Mo3JGDE2YG3xyzVutMStEicxbQGRfrYvAAYxH6Fe8rnD56EaNwUiqhcwR", "--rpc-payment-difficulty", str(DIFFICULTY), "--rpc-payment-credits", "5000", "--offline"],


```
Note that setting log level to 3 is *needed* here. Running with log level 1 will not trigger it. In Townforge, log level 1 is fine. Log level 2 will trigger fairly quickly. Monero with log level 3 will trigger is pretty much at once.

Once triggered, it never recovers. I tried adding recovery code in Townforge, to no avail (that may be because the underlying issue is not what I vaguely expect it to be).

The symptoms are en exception in handle_accept, where a syscall returns EBADF. The socket is valid at the start of the function, and becomes invalid somewhere along the execution of handle_accept. AFAICT this is not a case of the connection being destroyed by another thread, but I'd be happy to be shown to be wrong there since it's the obvious inference.

I've spent days on this over the months, I hope someone with more networking chops can have a try at it.

Note that there's been reports of RPC connectivity going down over the years, that's probably the same thing.


# Discussion History
## 0xFFFC0000 | 2024-11-25T15:07:34+00:00
I can confirm this happening. and after (briefly) testing it, this is the call stack which consumes most of the computation time: 

![image](https://github.com/user-attachments/assets/2bc8e9d4-359c-4988-a52a-d4096d7bd6a5)

P.S. Take this information with grain of salt. I will profile / debug this tomorrow. 


## moneromooo-monero | 2024-11-25T15:13:00+00:00
To be clear, the issue isn't performance degradation due to heavy logging, it is the server stopping accepting connections after this:

> ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:1528  Exception in boosted_tcp_server<t_protocol_handler>::handle_accept: set_option: Bad file descriptor

Note that if you trace around, the EBADF might come from another function, set_option is just the most likely to get whacked.


## 0xFFFC0000 | 2024-11-25T15:33:16+00:00
In that case, I left it running for about 10 minutes. But I don't have any 

> Exception in boosted_tcp_server<t_protocol_handler>::handle_accept: set_option: Bad file descriptor

in my logs.

Usually how long it takes for the exception to show up?

## moneromooo-monero | 2024-11-25T15:44:08+00:00
In three attempts, about... 5 seconds, 5 seconds, 20 seconds maybe. After waiting for servers to be running. This is on master from a1dc85c5373a30f14aaf7dcfdd95f5a7375d3623.


## moneromooo-monero | 2024-11-25T15:45:04+00:00
Running:

./tests/functional_tests/functional_tests_rpc.py /usr/bin/python tests/functional_tests/ build/Linux/master/release/ daemon_info


## 0xFFFC0000 | 2024-11-25T15:51:52+00:00
I am hitting the infinite while loop correctly. But haven't been able to reproduce the `Bad file descriptor`. After 15 minutes of running.

I will update you if anything comes up, and will do it on bare metal machine too. I am doing it on a VM right now. 

## moneromooo-monero | 2024-11-25T15:56:11+00:00
I'm running on an old Fedora VM. I'll try setting up a more recent one later, it might be a dep issue if you can't get it to happen.

## 0xFFFC0000 | 2024-11-25T15:58:29+00:00
I tried on a vm:

```
 $ >> cat /etc/os-release 
PRETTY_NAME="Ubuntu 24.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="24.04"
VERSION="24.04.1 LTS (Noble Numbat)"
VERSION_CODENAME=noble
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
```

## moneromooo-monero | 2024-11-26T16:08:50+00:00
Also happens pretty much instantly on Fedora 41, GCC 14.2.1.


## moneromooo-monero | 2024-11-27T11:43:50+00:00
Also Debian 12, GCC 12.2.0.

All of this running in Qubes OS, so there might be something weird to do with xen I guess, though it does seem a bit unlikely.

## vtnerd | 2025-01-06T00:06:36+00:00
#9459 might fix this

## tankf33der | 2025-01-07T18:00:27+00:00
i wrote a short code on vlang to bomb (!) rpc: i see like short ddos but without any crash or stops.

## moneromooo-monero | 2025-01-10T17:13:50+00:00
> #9459 might fix this

It does not, though it does seem to be lasting a bit longer before it dies.

## tankf33der | 2025-01-10T17:42:17+00:00
while debugging and repeating huge wallet from #9405 I found i can not send huge `transfer_split` txs WITHOUT `--rpc-payment-allow-free-loopback` on `monerod`.

@moneromooo-monero - you could try to add to `monerod_base` this key and try again.

## moneromooo-monero | 2025-01-11T09:17:10+00:00
This problem occurs without using the RPC payment system.


## tankf33der | 2025-01-14T13:57:35+00:00
I repeated issue in my env: Ubuntu 24.04.1 LTS under Docker. All settings out of box.
I manually compiled recent master of monero in ASAN mode.
daemon_info.py looped and crashed (?) with long trace from ASAN for boost.
I won't show it for now.
my `Exception` line from log:
```
./monerod0/bitmonero.log:2025-01-14 13:09:00.717        [RPC1]  ERROR   net     contrib/epee/include/net/abstract_tcp_server2.inl:1528  Exception in boosted_tcp_server<t_protocol_handler>::handle_accept: local_endpoint: Bad file descriptor [system:9 at /usr/include/boost/asio/detail/reactive_socket_service.hpp:202 in function 'local_endpoint']
```

p.s.
Later, when I wrote this issue, I also experimented with launching, and the launch always fails with an ASAN error on Ctrl-C, but of a different type.


## jeffro256 | 2025-01-22T07:11:49+00:00
@moneromooo-monero Would you be willing to share the last 1000 lines of the monerod0.log file once it triggers please (or the full log)? By the way, I was not able to reproduce the error on bare-metal Linux Mint 21.3 after running it for a couple hours. 

# Action History
- Created by: moneromooo-monero | 2024-11-25T14:24:51+00:00
