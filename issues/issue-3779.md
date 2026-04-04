---
title: Excessive CPU usage of monero daemon with torsocks when Tor is not available
source_url: https://github.com/monero-project/monero/issues/3779
author: garlicgambit
assignees: []
labels: []
created_at: '2018-05-07T21:48:32+00:00'
updated_at: '2018-08-29T10:37:13+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Excessive CPU usage of monero daemon with torsocks when the Tor proxy is not available. Tested on Tails 3.6.2 and OpenBSD amd64 with Monero v0.12.0.0. Tested on Tails with cli binaries from getmonero.org.

When the Tor proxy is not available the monerod process will consume a lot of CPU power. When you enable the Tor proxy it will drop to normal levels, even when the Tor proxy is not connected to the Tor network. CPU usage will jump back up when you stop the Tor proxy again.

The --detach and --non-interactive options are also affected by this issue.

The following data is from an OpenBSD amd64 system with Monero v0.12.0.0 and torsocks 2.2.0. The monerod daemon system is configured with ip address 172.16.1.2 and is able to communicate with 172.16.1.1. There is no Tor, DNS or Monero daemon service running on 172.16.1.1. The daemon is bootstrapping from scratch.

Results:

100% CPU usage on 1 core:
        TORSOCKS_ALLOW_INBOUND=1 /usr/local/bin/torsocks /usr/local/bin/monerod

Less then 1% CPU usage:
        TORSOCKS_ALLOW_INBOUND=1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

100% CPU usage on 1 core:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks /usr/local/bin/monerod

Less then 1% CPU usage:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

80-90% CPU usage on 1 core:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://127.0.0.1 /usr/local/bin/torsocks /usr/local/bin/monerod

Less then 1% CPU usage:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://127.0.0.1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://127.0.0.1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

100% CPU usage on 1 core:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks /usr/local/bin/monerod

Less then 1% CPU usage:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

100% CPU usage on more then 4 cores. 9 tcp connections. Very slow response to the stop signal in detach and non-interactive mode:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod

100% CPU usage on 4 cores. 4 tcp connections. Very slow response to the stop signal in detach and non-interactive mode:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

100% CPU usage on more then 4 cores. 9 tcp connections. Very slow response to the stop signal in detach and non-interactive mode:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod

100% CPU usage on 4 cores. 4 tcp connections. Very slow response to the stop signal in detach and non-interactive mode:
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod --add-exclusive-node=127.0.0.1
        TORSOCKS_ALLOW_INBOUND=1 DNS_PUBLIC=tcp://172.16.1.1 /usr/local/bin/torsocks --address 172.16.1.1 /usr/local/bin/monerod --add-exclusive-node=172.16.1.1

# Discussion History
## moneromooo-monero | 2018-06-09T11:39:34+00:00
https://github.com/monero-project/monero/pull/3970

## rex4539 | 2018-08-26T05:44:10+00:00
I'm able to reproduce it too.

Attaching a memory sample during the bug.

[Sample of monerod.txt](https://github.com/monero-project/monero/files/2321274/Sample.of.monerod.txt)


## moneromooo-monero | 2018-08-26T11:41:04+00:00
What version of torsocks are you using ?
This is very likely to be fixed by 3f39f4f0c1ee39116d720282f912303279b02d93, which is in torsocks 2.2.0, but not 2.1.0.

## rex4539 | 2018-08-26T11:42:11+00:00
I'm on 2.2.0

## moneromooo-monero | 2018-08-26T11:48:37+00:00
Weird, because it's stuck right in a recv loop.
Can you run monerod with --log-level=0,net.p2p:DEBUG so we can see how often monerod tries to connect to a new peer ?

## rex4539 | 2018-08-26T12:12:37+00:00
[bitmonero.log](https://github.com/monero-project/monero/files/2321492/bitmonero.log)
[Sample of monerod.txt](https://github.com/monero-project/monero/files/2321493/Sample.of.monerod.txt)


## moneromooo-monero | 2018-08-26T12:20:11+00:00
So there's 21 connection attempts in 15 minutes. That really still seems to be a problem with torsocks itself.

## moneromooo-monero | 2018-08-26T12:44:59+00:00
Anyway, how do you do *exactly* to get into that state so I can reproduce it ?

## moneromooo-monero | 2018-08-26T12:58:50+00:00
Also, the code in wait_on_fd seems a bit off. Try this (in torsocks):

```
diff --git a/src/common/socks5.c b/src/common/socks5.c
index 9f7853b..6ecb8bf 100644
--- a/src/common/socks5.c
+++ b/src/common/socks5.c
@@ -60,7 +60,12 @@ static ssize_t recv_data_impl(int fd, void *buf, size_t len)
        index = 0;
        do {
                read_len = recv(fd, buf + index, read_left, 0);
-               if (read_len <= 0) {
+               if (read_len == 0) {
+                       /* Orderly shutdown from Tor daemon. Stop. */
+                       ret = -EIO;
+                       goto error;
+               }
+               if (read_len < 0) {
                        ret = -errno;
                        if (errno == EINTR) {
                                /* Try again after interruption. */
@@ -71,10 +76,6 @@ static ssize_t recv_data_impl(int fd, void *buf, size_t len)
                                        goto error;
                                }
                                continue;
-                       } else if (read_len == 0) {
-                               /* Orderly shutdown from Tor daemon. Stop. */
-                               ret = -EIO;
-                               goto error;
                        } else {
                                PERROR("recv socks5 data");
                                goto error;

```

## rex4539 | 2018-08-26T14:54:50+00:00
1. Start the Tor daemon.
2. Start monerod with torsocks `DNS_PUBLIC=tcp TORSOCKS_ALLOW_INBOUND=1 torsocks monerod --p2p-bind-ip 127.0.0.1 --no-igd --hide-my-port --detach`.
3. After a while, kill the Tor daemon and then immediately restart it.

monerod runs to 100% CPU and stays there forever.

## moneromooo-monero | 2018-08-27T16:31:30+00:00
Does https://github.com/moneromooo-monero/bitmonero/tree/bindex help ?

## rex4539 | 2018-08-28T07:28:09+00:00
I'm unable to compile from source.

If you could provide a precompiled binary for macOS I will test right away.

## moneromooo-monero | 2018-08-28T08:14:01+00:00
https://github.com/monero-project/monero/pull/4307 has links to the build bots, there are two Mac ones (10.11 and 10.13). Click on details for the one you want, and there's a link to a tarball at the bottom of the "Steps and log files" section.

## rex4539 | 2018-08-28T11:46:49+00:00
I tested with that build and I can't reproduce there but that build appears unable to connect to the network (seeing multiple errors in the log) so I'm not sure I'm testing correctly.

[bitmonero.log](https://github.com/monero-project/monero/files/2327831/bitmonero.log)


## moneromooo-monero | 2018-08-28T12:32:11+00:00
To double check this isn't something in this particular build, can the binary you were previously using connect at roughly the same time ?

## rex4539 | 2018-08-28T12:34:23+00:00
Well, now the previous one (release build) can't launch due to DB migration...

I need to restore the blockchain from a backup. Will try to find some time to do that...

## moneromooo-monero | 2018-08-28T12:35:22+00:00
Oops. You can still ceck with a temp --data-dir.

## rex4539 | 2018-08-29T05:37:48+00:00
I restored from backup but I get `Uncaught exception! Attempt to get block from height...`

I tried to fix with `--db-salvage` but no luck.

Sigh, monerod is too buggy. I give up for now. Will try to re-sync from scratch next month when I will have some free time hopefully.

## moneromooo-monero | 2018-08-29T10:13:09+00:00
The actual stack trace would be helpful. It'll be in the log.

## moneromooo-monero | 2018-08-29T10:37:12+00:00
Oh, you didn't back that one up while monerod was running, right ? Because if so, it's not monerod that's buggy, it's your backup script :)

# Action History
- Created by: garlicgambit | 2018-05-07T21:48:32+00:00
