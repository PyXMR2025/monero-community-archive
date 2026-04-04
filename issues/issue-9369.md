---
title: Error when running wallet in Gramine (Intel SGX)
source_url: https://github.com/monero-project/monero/issues/9369
author: yagop
assignees: []
labels:
- low priority
- more info needed
created_at: '2024-06-16T15:09:21+00:00'
updated_at: '2024-12-14T00:10:04+00:00'
type: issue
status: closed
closed_at: '2024-12-14T00:10:03+00:00'
---

# Original Description
I'm trying to run `monero-wallet-rpc` in [Gramine](https://gramineproject.io/) as for security purposes.

The http request are not working (it receives and close them), and errors got shadowed so not sure what's going on. Neither writing logs to log file seems working.

```
$ gramine-sgx /etc/gramine/monero-wallet --wallet-dir=/home/monero/wallet/ --rpc-bind-port=18083 --rpc-bind-ip=127.0.0.1 --disable-rpc-login --rpc-ssl disabled --offline --non-interactive --log-level=4 --log-file=/home/monero/monero-wallet.log --stagenet
...
2024-06-16 14:48:42.701	D handle_accept
2024-06-16 14:48:42.702	D New server for RPC connections, SSL disabled
2024-06-16 14:48:42.702	D Spawned connection #1 to 0.0.0.0 currently we have sockets count:2
(libos_epoll.c:406:do_epoll_mod) [P1:T2:monero-wallet-rpc] debug: epoll: modified 6 (0xffff268678) on epoll handle 0xffff268440
2024-06-16 14:48:42.702	D Destructing connection #0 to 127.0.0.1
```

Any idea how to proceed?

Full log: https://pst.innomi.net/paste/ubs4wyx4rxvc9pnfjb7kqk5v
Gramine template: https://pst.innomi.net/paste/6exw6jsndsh9jk6btjuxz9ya

# Discussion History
## 0xFFFC0000 | 2024-06-17T20:40:47+00:00
Very interesting question. I will try Grammine myself. 


But honestly I don't think this will be related to Monero code base. The error happens on much lower level (epoll syscall). There is all sort of restriction in SGX runtime. 

## selsta | 2024-12-14T00:10:04+00:00
Closing this as running with Intel SGX is not something we support and the error message does appear to be lower level than monero itself.

# Action History
- Created by: yagop | 2024-06-16T15:09:21+00:00
- Closed at: 2024-12-14T00:10:03+00:00
