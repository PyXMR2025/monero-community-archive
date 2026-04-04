---
title: bitmonerod stops itself if run without --detach as non-forking systemd service
source_url: https://github.com/monero-project/monero/issues/853
author: radfish
assignees: []
labels: []
created_at: '2016-05-28T18:55:53+00:00'
updated_at: '2018-06-23T23:17:18+00:00'
type: issue
status: closed
closed_at: '2016-05-31T01:16:54+00:00'
---

# Original Description
systemd service file bitmonerod.service:

```
[Unit]
Description=Monero crypto-currency node
After=network.target

[Service]
User=bitmonerod
Group=bitmonerod

# This does not work
ExecStart=/usr/bin/bitmonerod --config-file /etc/bitmonero.conf --data-dir /var/lib/bitmonerod

# This works
#Type=forking
#ExecStart=/usr/bin/bitmonerod --config-file /etc/bitmonero.conf --data-dir /var/lib/bitmonerod --detach

[Install]
WantedBy=multi-user.target
```

From `journalctl -u bitmonerod`:

```
bitmonerod[31030]: 2016-May-28 14:48:25.573784 Core initialized OK
bitmonerod[31030]: 2016-May-28 14:48:25.573948 Starting core rpc server...
bitmonerod[31030]: 2016-May-28 14:48:25.574037 Run net_service loop( 2 threads)...
bitmonerod[31030]: 2016-May-28 14:48:25.574766 [SRV_MAIN]Core rpc server started ok
bitmonerod[31030]: 2016-May-28 14:48:25.576443 [SRV_MAIN]Starting p2p net loop...
bitmonerod[31030]: 2016-May-28 14:48:25.576851 [SRV_MAIN]Run net_service loop( 10 threads)...
bitmonerod[31030]: 2016-May-28 14:48:25.580650 [node] Stop signal sent
```

Nobody sent a SIGINT or SIGTERM to it.

My wild guess: is SIGTERM+SIGINT the only signals that bitmonerod handles? Perhaps systemd is sending some singal like SIGHUP, but bitmonerod doesn't distinguish by signal number?


# Discussion History
## Gingeropolous | 2016-05-31T00:24:52+00:00
So, it works with the --detach? I'm confused. Is the log you showed from 

`ExecStart=/usr/bin/bitmonerod --config-file /etc/bitmonero.conf --data-dir /var/lib/bitmonerod`

Or is it from the one with detach?


## radfish | 2016-05-31T01:16:54+00:00
Solved: bitmonerod stops itself when run by systemd but without `--detach` because it attempts to and fails to open stdin. Nothing wrong here.

(There is some problem with sytemd Type=forking, where bitmonerod dies shortly after launch. This never happens for `sytemctl start` which is run right after `systemctl daemon-reload`, but always happens when trying to start the service after having stopped it. This is likely to be systemd issue because I've seen it on at least one other application. I think this is because PIDFile is not used. So, bitmonerod needs to generate a pid file so that we can use it in systemd service.)

UPDATE on the above issue: 

```
# This is necessary because bitmonerod does not yet support
# writing a PID file, which means systemd tries to guess the PID
# by default, but it guesses wrong (sometimes, depending on
# random timing of events), because the daemon forks twice.
# The ultimate fix is for the daemon to write a PID file, and
# a workaround is to disable the guessing feature in systemd.
GuessMainPID=no
```


## gaffelosked | 2016-10-14T17:12:10+00:00
Having the same issue on ubuntu 16.04 using upstart...


## radfish | 2016-11-18T23:41:10+00:00
@gaffelosked don't run without `--detach`. There shouldn't be a reason to. I only tried because `forking` didn't work with systemd, but that should be irrelevant for upstart.


## jbg | 2017-02-10T15:05:26+00:00
Unfortunately, running without `--detach` seems to be the only way to get log output to go to the journal, since there's no command-line option (that I can see) to send logging to anything other than a file.

A workaround is to add the following to the systemd unit file:

```
StandardInput=tty-fail
TTYPath=/dev/pts/ptmx
TTYReset=yes
TTYVHangup=yes
TTYVTDisallocate=yes
```

This should allocate a pseudo-terminal and attach it to stdin, while still sending stdout and stderr to the journal.

Why does bitmonerod try to read from stdin when `--detach` is not specified?

## FunkyM | 2018-02-05T13:41:42+00:00
@radfish There is a reason. The systemd docs state that daemons should run in the foreground to be managed by systemd and not need to fork. Thus monerod should work with `Type=simple` in the foreground, too.
@jbg The problem here is not `--detach` but the stdin is opened due to interactive mode being default.

So to sum up this for whoever runs into this again, use `Type=simple` in the systemd unit file and make sure to pass the `--non-interactive` command line option in `ExecStart=` if you want `monerod` in foreground mode.

Another important note, a PID file is only created by monerod if `--detach` was provided.

## radfish | 2018-02-05T16:26:36+00:00
Systemd manages forking daemons fine, too, with Type=forking. Did you read something that says 'simple' is preferred over forking?

Yes, the issue was that monerod tried to open stdin and failed. I'm not sure whether --non-interactive existed at the time, but thanks for pointing at it here.

Fwiw, I prefer monero log in a separate file because monerod can get somewhat verbose. But, syslog should be supported, too, for sure.

## rearden-steel | 2018-06-23T23:17:18+00:00
Spent some hours guessing why the monerod works with docker, but does not work with docker-compose and found that it is connected with this stdin issue.
You MUST add logging about the fail, because there is no ERROR level messages, the daemon simply terminates without any reasons.

# Action History
- Created by: radfish | 2016-05-28T18:55:53+00:00
- Closed at: 2016-05-31T01:16:54+00:00
