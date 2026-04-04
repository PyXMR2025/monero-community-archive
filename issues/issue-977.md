---
title: bitmonerod fails to run as systemd service
source_url: https://github.com/monero-project/monero/issues/977
author: pmknutsen
assignees: []
labels: []
created_at: '2016-08-22T19:31:50+00:00'
updated_at: '2016-08-23T07:26:11+00:00'
type: issue
status: closed
closed_at: '2016-08-23T07:26:11+00:00'
---

# Original Description
Here is my .service file:

```
[Unit]
Description=Monero Daemon
After=network.target

[Service]
User=MYUSER
Group=MYGROUP

ExecStart=/opt/bitmonero/bitmonerod --log-file bitmonerod.log

[Install]
WantedBy=multi-user.target
```

and this is the output of `journalctl -f -u bitmonerod.service`:

```
systemd[1]: Started Monero Daemon.
bitmonerod[7131]: Creating the logger system
bitmonerod[7131]: 2016-Aug-22 21:23:05.463278 Initializing cryptonote protocol...
bitmonerod[7131]: 2016-Aug-22 21:23:05.463297 Cryptonote protocol initialized OK
bitmonerod[7131]: 2016-Aug-22 21:23:05.463383 Initializing p2p server...
bitmonerod[7131]: 2016-Aug-22 21:23:05.762653 Set limit-up to 2048 kB/s
bitmonerod[7131]: 2016-Aug-22 21:23:05.762710 Set limit-down to 8192 kB/s
bitmonerod[7131]: 2016-Aug-22 21:23:05.762726 Set limit-up to 2048 kB/s
bitmonerod[7131]: 2016-Aug-22 21:23:05.762745 Set limit-down to 8192 kB/s
bitmonerod[7131]: 2016-Aug-22 21:23:05.763142 Binding on 0.0.0.0:18080
bitmonerod[7131]: 2016-Aug-22 21:23:05.763183 Net service bound to 0.0.0.0:18080
bitmonerod[7131]: 2016-Aug-22 21:23:05.763190 Attempting to add IGD port mapping.
bitmonerod[7131]: 2016-Aug-22 21:23:10.557356 UPnP device was found but not recoginzed as IGD.
bitmonerod[7131]: 2016-Aug-22 21:23:10.557385 P2p server initialized OK
bitmonerod[7131]: 2016-Aug-22 21:23:10.557441 Initializing core rpc server...
bitmonerod[7131]: 2016-Aug-22 21:23:10.557469 Binding on 127.0.0.1:18081
bitmonerod[7131]: 2016-Aug-22 21:23:10.557520 Core rpc server initialized OK on port: 18081
bitmonerod[7131]: 2016-Aug-22 21:23:10.557530 Initializing core...
bitmonerod[7131]: 2016-Aug-22 21:23:10.557619 Loading blockchain from folder /home/MYUSER/.bitmonero/lmdb ...
bitmonerod[7131]: 2016-Aug-22 21:23:10.557631 option: fastest
bitmonerod[7131]: 2016-Aug-22 21:23:10.557635 option: async
bitmonerod[7131]: 2016-Aug-22 21:23:10.557639 option: 1000
bitmonerod[7131]: 2016-Aug-22 21:23:10.582384 Blockchain initialized. last block: 1119313, d0.h0.m21.s28 time ago, current difficulty: 2593344829
bitmonerod[7131]: 2016-Aug-22 21:23:11.130736 Core initialized OK
bitmonerod[7131]: 2016-Aug-22 21:23:11.130761 Starting core rpc server...
bitmonerod[7131]: 2016-Aug-22 21:23:11.130766 Run net_service loop( 2 threads)...
bitmonerod[7131]: 2016-Aug-22 21:23:11.130827 [SRV_MAIN]Core rpc server started ok
bitmonerod[7131]: 2016-Aug-22 21:23:11.130965 [SRV_MAIN]Starting p2p net loop...
bitmonerod[7131]: 2016-Aug-22 21:23:11.130986 [SRV_MAIN]Run net_service loop( 10 threads)...
systemd[1]: bitmonerod.service: Main process exited, code=exited, status=1/FAILURE
systemd[1]: bitmonerod.service: Unit entered failed state.
systemd[1]: bitmonerod.service: Failed with result 'exit-code'.
```

I have tried running in `--detach` mode because of [this](https://github.com/monero-project/bitmonero/issues/853) but with same result.

Running the ExecStart command above directly of course works just fine.


# Discussion History
## radfish | 2016-08-22T21:25:42+00:00
Try this: https://aur.archlinux.org/cgit/aur.git/tree/bitmonerod.service?h=bitmonero-git
(I've been fighting this battle for a while and eventually declared victory)


## pmknutsen | 2016-08-23T07:26:11+00:00
Perfect. The `GuessMainPID=no` tweak fixed it. Thank you!


# Action History
- Created by: pmknutsen | 2016-08-22T19:31:50+00:00
- Closed at: 2016-08-23T07:26:11+00:00
