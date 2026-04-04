---
title: 'monerod crashes during resync: Exception in threadpool'
source_url: https://github.com/monero-project/monero/issues/6957
author: nullcopy
assignees: []
labels: []
created_at: '2020-11-01T17:28:58+00:00'
updated_at: '2020-11-04T04:00:03+00:00'
type: issue
status: closed
closed_at: '2020-11-04T04:00:03+00:00'
---

# Original Description
When running `monerod` on latest 0.17.1.1, the node repeatedly crashes during resync with the following output:
```
2020-10-31 15:18:25.197 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     [70.180.135.90:18080 OUT] Sync data returned a new top block candidate: 2210000 -> 2220390 [Your node is 10390 blocks (14.4 days) behind] 
2020-10-31 15:18:25.197 [P2P3]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     SYNCHRONIZATION started
2020-10-31 15:18:30.508 [P2P0]  ERROR   default src/common/threadpool.cpp:170   Exception in threadpool job: mprotect failed
```

I am running monerod v0.17.1.1 on Ubuntu 20.04.

# Discussion History
## moneromooo-monero | 2020-11-02T00:21:47+00:00
Are you using systemd ?

## nullcopy | 2020-11-02T03:25:41+00:00
> Are you using systemd ?

Yes. Below is my `monerod.service`
```
# It is not recommended to modify this file in-place, because it will
# be overwritten during package upgrades. If you want to add further
# options or overwrite existing ones then use
# $ systemctl edit bitcoind.service
# See "man systemd.service" for details.

# Note that almost all daemon options could be specified in
# /etc/bitcoin/bitcoin.conf, but keep in mind those explicitly
# specified as arguments in ExecStart= will override those in the
# config file.

[Unit]
Description=Monero daemon
After=network.target

[Service]
ExecStart=/usr/local/bin/monerod --detach \
                            --pidfile=/run/monerod/monerod.pid \
                            --data-dir=/mnt/raid6/monero
ExecStop=/usr/local/bin/monerod exit

# Make sure the config directory is readable by the service user
PermissionsStartOnly=true
ExecStartPre=/bin/chgrp monero /etc/monero

# Environment Variables
#######################
Environment="MONERO_RANDOMX_UMASK=16"

# Process management
####################

Type=forking
PIDFile=/run/monerod/monerod.pid
Restart=on-failure
TimeoutStopSec=600

# Directory creation and permissions
####################################

# Run as monero:monero
User=monero
Group=monero

# /run/monerod
RuntimeDirectory=monerod
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Deny access to /home, /root and /run/user
#ProtectHome=true

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

This service is mostly copied from Bitcoin core's `bitcoind.service` example (following their system "hardening" techniques). I have also added the `MONERO_RANDOMX_UMASK=16` environment variable, per one of your comments on https://github.com/monero-project/monero/issues/6744#issuecomment-672815697. Even after enabling this, I still observe the mprotect failure.

## moneromooo-monero | 2020-11-02T16:51:42+00:00
99% sure MemoryDenyWriteExecute is the culprit.
randomx should not do that though, it's supposed to alternate, not do both at once.

## moneromooo-monero | 2020-11-02T16:57:20+00:00
Unset MONERO_RANDOMX_UMASK, this unsets the secure mode (W^X) for faster hashing (fewer mprotect changes).

## nullcopy | 2020-11-02T23:04:39+00:00
Confirmed `MemoryDenyWriteExecute` was the issue. I didn't expect that to cause problems, but apparently I was wrong. Thanks for your help!

## nullcopy | 2020-11-02T23:05:43+00:00
Not sure if this is indicative of a bug in RandomX, but for my purposes I will just proceed without `MemoryDenyWriteExecute`.

## tevador | 2020-11-02T23:28:38+00:00
@phreaknik This behavior is not a bug. If you want to keep `MemoryDenyWriteExecute=true` then simply remove `MONERO_RANDOMX_UMASK=16` from the environment variables. Those settings are incompatible.

## nullcopy | 2020-11-02T23:48:55+00:00
I tried without `MONERO_RANDOMX_UMASK=16` and saw the same mprotect failure. I only added that environment variable as a test to try and fix the failure, but accidentally included it in my original issue.

## nullcopy | 2020-11-03T03:52:31+00:00
@tevador to be thorough, I trimmed a lot of the fat out of my service, including removing the  `MONERO_RANDOMX_UMASK` variable. Now the only "extra" option is the `MmoryDenyWriteExecute=true`.
```
[Unit]
Description=Monero daemon
After=network.target

[Service]
ExecStart=/usr/local/bin/monerod --detach \
                            --pidfile=/run/monerod/monerod.pid \
                            --data-dir=/mnt/raid6/monero
ExecStop=/usr/local/bin/monerod exit

# Make sure the config directory is readable by the service user
ExecStartPre=/bin/chgrp monero /etc/monero

# Process management
####################
Type=forking
PIDFile=/run/monerod/monerod.pid
Restart=on-failure
TimeoutStopSec=600

# Directory creation and permissions
####################################
# Run as monero:monero
User=monero
Group=monero

# /run/monerod
RuntimeDirectory=monerod
RuntimeDirectoryMode=0710

# Hardening measures
####################
# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```
And below is the log upon restarting the service:
```
2020-11-03 03:47:22.014 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     [213.32.121.162:13928 OUT] Sync data returned a new top block candidate: 2215620 -> 2222198 [Your node is 6578 blocks (9.1 days) behind] 
2020-11-03 03:47:22.014 [P2P9]  INFO    global  src/cryptonote_protocol/cryptonote_protocol_handler.inl:368     SYNCHRONIZATION started
2020-11-03 03:47:30.566     7f743ebfb700        ERROR   default src/common/threadpool.cpp:170   Exception in threadpool job: mprotect failed
```

As you can see, I still get an `mprotect failed` error with just the `MemoryDenyWriteExecute=true` option. I believe this is a bug.

## tevador | 2020-11-03T06:59:49+00:00
According to the [systemd man pages](https://man7.org/linux/man-pages/man5/systemd.exec.5.html), this is not a bug but the intended behavior of the `MemoryDenyWriteExecute` option:

> MemoryDenyWriteExecute=
>	   Takes a boolean argument. If set, attempts to create memory
>	   mappings that are writable and executable at the same time, or to
>	   change existing memory mappings to become executable, or mapping
>	   shared memory segments as executable are prohibited.
>	   Specifically, a system call filter is added that rejects mmap(2)
>	   system calls with both PROT_EXEC and PROT_WRITE set, mprotect(2)
>	   or pkey_mprotect(2) system calls with PROT_EXEC set and shmat(2)
>	   system calls with SHM_EXEC set. Note that **this option is
>	   incompatible with programs and libraries that generate program
>	   code dynamically at runtime, including JIT execution engines**,
>	   executable stacks, and code "trampoline" feature of various C
>	   compilers.

Emphasis mine. The issue is that it not only enforces W^X, but also prevents existing mappings from being made executable. No JIT compiled code can work under these circumstances. If you insist about having it on, you need to use `MONERO_RANDOMX_UMASK=8`, which disables JIT altogether (at the cost of a much slower synchronization).


## nullcopy | 2020-11-04T04:00:03+00:00
@tevador Ah, I see now. Thanks for the thorough response!

# Action History
- Created by: nullcopy | 2020-11-01T17:28:58+00:00
- Closed at: 2020-11-04T04:00:03+00:00
