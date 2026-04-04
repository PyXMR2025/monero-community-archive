---
title: WHERE SENSE in rpc-login for both core and restricted RPC?!
source_url: https://github.com/monero-project/monero/issues/9489
author: itmagpro
assignees: []
labels:
- question
- low priority
- more info needed
created_at: '2024-09-23T00:10:43+00:00'
updated_at: '2024-11-04T16:05:18+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Example config:

```
# Binding on 0.0.0.0 (IPv4):18081
# CORE RPC server initialized OK on port: 18081
# Initializing restricted RPC server...
rpc-bind-ip=0.0.0.0
rpc-bind-port=18081
confirm-external-bind=1
restricted-rpc=0
no-igd=1
rpc-login=login:password

# Binding on xxx.xxx.xxx.xxx(IPv4):18091
# RESTRICTED RPC server initialized OK on port: 18091
# Starting core RPC server...
rpc-restricted-bind-ip=xxx.xxx.xxx.xxx
rpc-restricted-bind-port=18091
```

Then, **if we try login to CORE RPC or RESTRICTED RPC without --rpc-login=login:password flag, in both case we get this**:

```
Error: wallet failed to connect to daemon: xxx.xxx.xxx.xxx:18091. Daemon either is not started or wrong port was passed. Please make sure daemon is running or change the daemon address using the 'set_daemon' command.
Background refresh thread started
[wallet xxxxxx (no daemon)]:
```

For CORE RPC ok, rpc-login set.., **but for why he need to me on rpc-restricted-bind-ip?**

**What if I not want set password for rpc-restricted-bind?**

**In this case I see solution to make additional option like** rpc-restricted-bind-login

ALSO...

```
[wallet xxxxxx (no daemon)]: help all
Commands:
...
```

Give us set_daemon option:

`set_daemon <host>[:<port>] [trusted|untrusted|this-is-probably-a-spy-node]`

But.., **HOW WEE CAN connect** with login password with this set_daemon option!?

```
[wallet xxxxxx (no daemon)]: set_daemon xxx.xxx.xxx.xxx:18091 trusted
Warning: connecting to a non-local daemon without SSL, passive adversaries will be able to spy on you.
```

**WHERE** set_proxy (direct access deny to remote IP from my network), set_allow_any_ssl or **some thing else for connect to password protected node from wallet without exit?**

```
[wallet xxxxxx (no daemon)]: version
Monero 'Fluorine Fermi' (v0.18.3.4-release)
```

...a raw fake...

# Discussion History
## nahuhh | 2024-11-04T16:05:16+00:00
So this is a feature request for --restricted-rpc-login ?

# Action History
- Created by: itmagpro | 2024-09-23T00:10:43+00:00
