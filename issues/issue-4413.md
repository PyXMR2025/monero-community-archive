---
title: Support USR1 signal for log rotation
source_url: https://github.com/monero-project/monero/issues/4413
author: ghost
assignees: []
labels: []
created_at: '2018-09-22T04:46:14+00:00'
updated_at: '2026-02-18T21:51:10+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
When monerod and monero-wallet-rpc receives SIGUSR1 signal, they quit just like when they get SIGINT.

Most applications re-open their log files when they get SIGUSR1, and it makes log rotation easier.

I think it will be nice if monerod and the rest support them too.

# Discussion History
## moneromooo-monero | 2018-09-22T08:12:07+00:00
SIGUSR1 is usually a "re-read config" call.

## ghost | 2018-09-22T08:45:12+00:00
No. SIGHUP typically reloads config (and re-opens log for some apps). For example, systemd sends `/bin/kill -HUP $MAINPID` when `ExecReload` is not defined. 

SIGUSR1 is used by some programs (e.g. fluentd, auditd, squid, tomcat, dovecot, openvpn and many other...)  to reopen logs.

## moneromooo-monero | 2018-09-22T09:15:09+00:00
lol, I did confuse things indeed :D Sorry.

## trasherdk | 2018-09-24T10:13:22+00:00
Regarding log rotation. Is it possible to do a `copy-truncate` instead of `close-open`?
This will allow `tail -f logfile.log | dosomething.sh` to function across rotations.

## moneromooo-monero | 2018-09-24T10:28:28+00:00
Seems useful to add.

## moneromooo-monero | 2018-10-02T18:42:44+00:00
+hacktoberfest

## trasherdk | 2019-02-22T09:15:54+00:00
Did the log file `copy-truncate` get implemented ?

And what about graceful shutdown ?

I'm currently using `kill -HUP $(cat ${PID})` or `kill -HUP $(pidof monerod)` which is not exactly graceful.

## moneromooo-monero | 2019-02-22T10:33:38+00:00
No, and yes, respectively.

## trasherdk | 2019-02-22T15:44:49+00:00
I must have missed the commit/patch. Or is it in `monero-v0.14.0.x` ?

## moneromooo-monero | 2019-02-22T16:10:10+00:00
A patch for... a graceful shutdown ? What kind of ungraceful shutdown are you having ?

## trasherdk | 2019-02-22T17:43:06+00:00
When running monerod interactively, I'd do a `save` followed by `exit` to shut down.
The log show the different stages of shutting down.

When running detached, I have to signal the daemon to shut down, and doing a `kill -HUP $(cat ${PID})` it's like a crash. And the log just ends.

I'm running up to 3 monerod, bound to different ip addresses, on a local test server, plus 2 on remote servers.



## moneromooo-monero | 2019-02-22T18:17:42+00:00
I'm confused. SIGHUP for log rotation is not implemented yet. And yet you are saying you're sending SIGHUP. Is it a simple case of "don't do that then" ? :) Am I missing something ?


## moneromooo-monero | 2019-02-23T00:01:27+00:00
If it's that you don't know how to quit, you can use "monerod exit". Signal 15 should also work.

## trasherdk | 2019-02-23T02:06:55+00:00
`SIGHUP` is used by many programs, as a "soft" way to tell it to end. Just like `SIGQUIT`, `SIGKILL` and `SIGTERM`. I've never used `SIGHUP` for logrotation.

When doing a `$ ./monero-v0.13.0.4/monerod exit` I get:

    2019-02-22 17:31:51,465 INFO  [default] Page size: 4096
    Error: Couldn't connect to daemon: 127.0.0.1:18081

And that's expected, as this instance is on `192.168.1.71:18081`


## trasherdk | 2019-02-23T02:59:00+00:00
Ok. `SIGTERM` is the graceful shutdown signal. `$ kill -s TERM $(cat ${PID})`

And come to think of it.
`$ curl -X POST http://192.168.1.71:18081/stop_daemon -H 'Content-Type: application/json'`
is just as good.

Thanks for your patience :)

## moneromooo-monero | 2019-02-23T11:04:23+00:00
You'll have to add --p2p-bind-ip too for "monerod exit" to work. And --testnet/--stagenet if applicable I think.

# Action History
- Created by: ghost | 2018-09-22T04:46:14+00:00
