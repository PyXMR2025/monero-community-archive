---
title: Monero still makes ~/log directory even if specific .log file specified in
  .conf
source_url: https://github.com/monero-project/monero/issues/1043
author: ghost
assignees: []
labels: []
created_at: '2016-09-03T22:41:43+00:00'
updated_at: '2017-02-24T06:07:38+00:00'
type: issue
status: closed
closed_at: '2017-02-24T06:07:38+00:00'
---

# Original Description
Unless I'm missing something, I've got my `bitmonero.conf` (which should maybe be renamed to `monero.conf`)  looking like so:

```
log-file=./monero.log
log-level=0
p2p-bind-ip=192.168.xxx.xxx
p2p-bind-port=18080
max-concurrency=3
out-peers=64
```

Even specifying a .log file, I keep getting a /log directory containing `dr-monero` and `net` subdirectories each time. Is there a way to stop the system from creating these or trying to log to these? 


# Discussion History
## radfish | 2016-09-03T23:18:39+00:00
I noticed that too. If you really don't want those files created, a workaround is to run the daemon from a working directory where it has no write access:

```
sudo mkdir /var/lib/monero
cd /var/lib/monero
./monerod
```


## ghost | 2016-09-04T01:12:32+00:00
:(


## Gingeropolous | 2016-09-14T10:00:09+00:00
try using the `data-dir` command line flag instead of the logfile flag. This will put both the logfile and the block data in the same, new directory. 


## ghost | 2016-09-30T07:19:46+00:00
I may have traced the reason to the order in which the Daemon processes args at startup. Testing this weekend. 


## ghost | 2017-02-24T06:07:38+00:00
This should now be fixed following the inclusion of easylogger++

Will open a new issue if not

# Action History
- Created by: ghost | 2016-09-03T22:41:43+00:00
- Closed at: 2017-02-24T06:07:38+00:00
