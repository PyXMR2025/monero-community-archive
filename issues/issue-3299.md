---
title: Snap monerod startup silently failing
source_url: https://github.com/monero-project/monero/issues/3299
author: zone117x
assignees: []
labels: []
created_at: '2018-02-20T17:46:29+00:00'
updated_at: '2021-08-13T04:26:32+00:00'
type: issue
status: closed
closed_at: '2021-08-13T04:26:32+00:00'
---

# Original Description
Seeing this behavior on several lower end systems using the snap package on Ubuntu 16.04.

On a $10/month tier azure server it fails to start almost every time. The last log entry is usually one of the following: "forking to background" or "initializing p2p".

Using the Snap stop/start or restart commands has never got it up and running past that stage, only occasionally works after just restarting the server. Seems like some timing issue?

Will update if I get better logs. Maybe some info in systemd?

Potentially related issue https://github.com/monero-project/monero/pull/3270

This has been reproducible on every Ubuntu system I've tried.

# Discussion History
## moneromooo-monero | 2018-02-20T23:33:35+00:00
Does it leave a core (you might have to run ulimit -c unlimited or echo core | sudo tee /proc/sys/kernel/core_pattern first) ? Does dmesg show an OOM kill ?

## anonimal | 2018-02-21T01:03:12+00:00
`snapcraft.yml` currently runs `monerod-wrapper --detach --data-dir ${SNAP_COMMON} --config-file ${SNAP_USER_DATA}/etc/monerod.conf`. @zone117x have you tried running without `--detach`?

Pinging @elopio.

## come-maiz | 2018-02-21T16:20:31+00:00
@zone117x, do you get anything related to the daemon in /var/log/syslog?
I have installed it in two different Ubuntu machines and the daemon seems to auto start alright:

```
$ ps aux | grep monero
root     28747 12.2  1.5 2637368 128336 ?      Sl   10:17   0:04 /snap/monero/3/bin/monerod --detach --data-dir /var/snap/monero/common --config-file /root/snap/monero/3/etc/monerod.conf
```

Also, the output of `sudo snap logs monero.monerod` would be useful.

## thebeardbe | 2018-02-25T10:04:56+00:00
I'm also trying to run it through the snap. I'm running the snap on solus os. 

monerod never runs and the monerod.wrapper link is not installed. 
When I run monerod manually it gives me the following error:

`./monerod: error while loading shared libraries: libminiupnpc.so.10: cannot open shared object file: No such file or directory
`
I'm running : 

`sudo ./monerod --data-dir /snap/monero/common/ --config-file /snap/monero/3/etc/monerod.conf`

Any suggestions?


## come-maiz | 2018-02-26T15:03:29+00:00
That is weird @Bunker. Can you please run:

```
$ find /snap/monero -name libminiupnpc.so.10
```

I get this:
```
/snap/monero/3/usr/lib/x86_64-linux-gnu/libminiupnpc.so.10
```

## zone117x | 2018-02-28T22:24:28+00:00
From `cat /var/log/syslog | grep monerod`:
```
Feb 28 22:18:56 MoneroVM systemd[1]: Started Service for snap application monero.monerod.
Feb 28 22:19:46 MoneroVM systemd[1]: Starting Service for snap application monero.monerod...
Feb 28 22:19:54 MoneroVM monero.monerod[1257]: 2018-02-28 22:19:54.517#011    7ff59224b740#011INFO #011global#011src/daemon/main.cpp:279#011Monero 'Helium Hydra' (v0.11.1.0-release)
Feb 28 22:19:54 MoneroVM monero.monerod[1257]: Forking to background...
Feb 28 22:19:54 MoneroVM systemd[1]: Started Service for snap application monero.monerod.
Feb 28 22:19:56 MoneroVM kernel: [   36.250772] audit: type=1400 audit(1519856396.644:35): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="snap.monero.monerod" pid=1840 comm="apparmor_parser"
```

From `sudo snap logs monero.monerod`:
```
2018-02-28T22:19:46Z systemd[1]: Starting Service for snap application monero.monerod...
2018-02-28T22:19:54Z monero.monerod[1257]: 2018-02-28 22:19:54.517	    7ff59224b740	INFO 	global	src/daemon/main.cpp:279	Monero 'Helium Hydra' (v0.11.1.0-release)
2018-02-28T22:19:54Z monero.monerod[1257]: Forking to background...
2018-02-28T22:19:54Z systemd[1]: Started Service for snap application monero.monerod.
```
From `dmesg | grep monero`:
```
[   36.240986] audit: type=1400 audit(1519856396.634:33): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="snap.monero.monero-wallet-cli" pid=1836 comm="apparmor_parser"
[   36.246077] audit: type=1400 audit(1519856396.639:34): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="snap.monero.monero-wallet-rpc" pid=1838 comm="apparmor_parser"
[   36.250772] audit: type=1400 audit(1519856396.644:35): apparmor="STATUS" operation="profile_replace" info="same as current profile, skipping" profile="unconfined" name="snap.monero.monerod" pid=1840 comm="apparmor_parser"
```

The monerod process only shows up in `ps aux | grep monero` on the rare occasion that the snap happens to work. Otherwise nothing. 

I also run into the same problem as @Bunker when trying to run monerod manually. The libs like libminiupnpc.so.10 are in the right place.

## selsta | 2021-08-13T04:26:32+00:00
Snap package is no longer supported and has been removed.

# Action History
- Created by: zone117x | 2018-02-20T17:46:29+00:00
- Closed at: 2021-08-13T04:26:32+00:00
