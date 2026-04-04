---
title: monerod exits under dinit with "Loading checkpoi"
source_url: https://github.com/monero-project/monero/issues/9964
author: iacore
assignees: []
labels:
- question
created_at: '2025-06-22T19:57:16+00:00'
updated_at: '2025-06-23T19:11:12+00:00'
type: issue
status: closed
closed_at: '2025-06-23T18:07:19+00:00'
---

# Original Description
If I run the command via SSH inside a terminal, it works fine. However, it refuses to be started by dinit.

```shell
user@ef ~/.c/dinit.d> cat monerod
type = process
command = /home/user/monero-linux/monerod --zmq-pub tcp://127.0.0.1:18083 --out-peers 32 --in-peers 64 --add-priority-node=p2pmd.xmrvsbeast.com:18080 --add-priority-node=nodes.hashvault.pro:18080 --disable-dns-checkpoints --enable-dns-blocklist
log-type = buffer
user@ef ~/.c/dinit.d> dinitctl start monerod
Service 'monerod' started.
user@ef ~/.c/dinit.d> dinitctl start monerod
Service (already) started.
user@ef ~/.c/dinit.d> dinitctl list
[[+]     ] boot
[     {-}] monerod (exit status: 0)
user@ef ~/.c/dinit.d> dinitctl status monerod
Service: monerod
    State: STOPPED (terminated)
user@ef ~/.c/dinit.d> dinitctl catlog monerod
(dinit: note: service restarted)
2025-06-22 19:46:19.724	I Monero 'Fluorine Fermi' (v0.18.4.0-release)
2025-06-22 19:46:19.724	I Initializing cryptonote protocol...
2025-06-22 19:46:19.724	I Cryptonote protocol initialized OK
2025-06-22 19:46:19.724	I Initializing core...
2025-06-22 19:46:19.724	I Loading blockchain from folder /home/user/.bitmonero/lmdb ...
2025-06-22 19:46:19.739	I Loading checkpoi
(last line is truncated or incomplete)
```

# Discussion History
## nahuhh | 2025-06-23T01:11:53+00:00
Looks like an issue with your dinit setup

## iacore | 2025-06-23T18:07:19+00:00
You are correct.

## nahuhh | 2025-06-23T18:52:25+00:00
@iacore  have you tried running monerod with `--detach` or `--non-interactive` ?

## iacore | 2025-06-23T19:11:12+00:00
Yes, `--no-interactive` has solved the issue.

there is no stdin

# Action History
- Created by: iacore | 2025-06-22T19:57:16+00:00
- Closed at: 2025-06-23T18:07:19+00:00
