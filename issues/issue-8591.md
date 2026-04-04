---
title: Specifying a hostname instead of an IP address for --tx-proxy causes daemon
  to abort
source_url: https://github.com/monero-project/monero/issues/8591
author: comminutus
assignees: []
labels: []
created_at: '2022-09-23T18:41:26+00:00'
updated_at: '2022-09-23T18:54:00+00:00'
type: issue
status: closed
closed_at: '2022-09-23T18:54:00+00:00'
---

# Original Description
I am using docker-compose to setup a node with tor.  The monerod daemon runs in a ubuntu container while tor runs on an alpine container, both of them inside the same Docker network.

If I specify `--tx-proxy tor,<tor hostname>:<tor port>,10` (in my case the tor hostname is 'tor', so I use `--tx-proxy tor,tor:9050,10`, the daemon aborts with these messages:
```
E Invalid ipv4:port given for --tx-proxy
E Failed to handle command line
I Deinitializing core...
```

If I specify the IP address given to the tor instance by Docker's networking (`--tx-proxy tor,192.168.176.2:9050,10`) it works fine.  `dig`/`nslookup` on the 'tor' hostname inside the container running monerod works fine.

The trouble with specifying the IP address is orchestration.  I have to explicitly setup a network and a specific IP address known for tor before I launch the docker-compose file.

# Discussion History
## selsta | 2022-09-23T18:44:05+00:00
Duplicate of https://github.com/monero-project/monero/issues/7963, maybe you can add your comment to it?

## comminutus | 2022-09-23T18:50:48+00:00
Thanks @selsta , for some reason when I searched for issues I didn't see this one.

# Action History
- Created by: comminutus | 2022-09-23T18:41:26+00:00
- Closed at: 2022-09-23T18:54:00+00:00
