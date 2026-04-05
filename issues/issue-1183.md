---
title: src/unix/stream.c:1560
source_url: https://github.com/xmrig/xmrig/issues/1183
author: lexansoft
assignees: []
labels:
- bug
created_at: '2019-09-20T15:12:38+00:00'
updated_at: '2019-09-28T17:52:46+00:00'
type: issue
status: closed
closed_at: '2019-09-28T17:52:45+00:00'
---

# Original Description
Sep 20 15:10:35 pe-1 xmrig[89982]: xmrig: src/unix/stream.c:1560: uv_read_start: Assertion `stream->type == UV_TCP || stream->type == UV_NAMED_PIPE || stream->type == UV_TTY' failed.
Sep 20 15:10:35 pe-1 systemd[1]: xmrig.service: Main process exited, code=dumped, status=6/ABRT
Sep 20 15:10:35 pe-1 systemd[1]: xmrig.service: Failed with result 'core-dump'.

# Discussion History
## xmrig | 2019-09-20T15:43:09+00:00
Please provide full details, how I can reproduce the issue.
Thank you.

## lexansoft | 2019-09-20T18:04:18+00:00
When I try to start xmrig as a service on ubuntu.

The service file:

```
[Unit]
Description=XMRIG Miner

Wants=network.target
After=syslog.target network-online.target

[Service]
User=alexn
Type=simple
ExecStart=/home/alexn/xmrig/build/xmrig -c /home/alexn/xmrig-config.json
Restart=on-failure
RestartSec=10
KillMode=process

[Install]
WantedBy=multi-user.target
```                 

## xmrig | 2019-09-20T18:58:03+00:00
I confirm the bug, for workaround you can change 2 lines:

```
Type=forking
ExecStart=/home/alexn/xmrig/build/xmrig -c /home/alexn/xmrig-config.json -B
```

## xmrig | 2019-09-20T20:29:27+00:00
Fixed in dev and evo branches, option `StandardOutput=null` useful to prevent spamming to syslog, dedicated `syslog` option do job better (if need).

Also I found another bug in forking mode miner crashed on exit, I will check it tomorrow.
Thank you.

## lexansoft | 2019-09-20T23:15:45+00:00
Great. Thank you.

Alexandre Naverniouk


On Fri, Sep 20, 2019 at 1:29 PM xmrig <notifications@github.com> wrote:

> Fixed in dev and evo branches, option StandardOutput=null useful to
> prevent spamming to syslog, dedicated syslog option do job better (if
> need).
>
> Also I found another bug in forking mode miner crashed on exit, I will
> check it tomorrow.
> Thank you.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/xmrig/xmrig/issues/1183?email_source=notifications&email_token=AAQHPJAHCYEQMPOPYHP5AWDQKUXDLA5CNFSM4IYYH3P2YY3PNVWWK3TUL52HS4DFVREXG43VMVBW63LNMVXHJKTDN5WW2ZLOORPWSZGOD7HZO3Y#issuecomment-533698415>,
> or mute the thread
> <https://github.com/notifications/unsubscribe-auth/AAQHPJE6QUF762CJTWEKC5LQKUXDLANCNFSM4IYYH3PQ>
> .
>


## xmrig | 2019-09-28T17:52:45+00:00
Fixed in v3.2.0 and v4.2.0.

# Action History
- Created by: lexansoft | 2019-09-20T15:12:38+00:00
- Closed at: 2019-09-28T17:52:45+00:00
