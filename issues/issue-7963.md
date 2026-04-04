---
title: Allow DNS resolution in `--tx-proxy` flag for Docker usage
source_url: https://github.com/monero-project/monero/issues/7963
author: sethforprivacy
assignees: []
labels: []
created_at: '2021-09-21T13:17:23+00:00'
updated_at: '2026-01-27T07:42:19+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
While DNS resolution for the `--tx-proxy` flag is not necessary for normal deployments as Tor is usually run locally and exposes SOCKS5 port on `127.0.0.1:9050`, when running `monerod` and `tor` as Docker containers (as I do in popular guides for both Monero node usage and p2pool usage), you run Tor as a separate container which exposes SOCKS5 only on the internal Docker network, and not even to the host OS.

When doing this, the easiest way to use `--tx-proxy` is to do so by specifying the Tor container name, which is automatically available to all other Docker containers on the same network via DNS as the container name (i.e. `tor`).

For example, I would love to be able to do the following, which would be compatible no matter the Docker network in use, dynamic address, etc.:

`--tx-proxy=tor,tor:9050,disable_noise`

But instead have to find the IP address of the Tor container and then manually specify, i.e.:

`--tx-proxy=tor,172.17.0.5:9050,disable_noise`

# Discussion History
## comminutus | 2022-09-23T18:53:27+00:00
I'm also using monerod and tor in containers.  The monerod daemon runs in a ubuntu container while tor runs on an alpine container, both of them inside the same Docker network.

If I specify `--tx-proxy tor,<tor hostname>:<tor port>,10` (in my case the tor hostname is 'tor', so I use `--tx-proxy tor,tor:9050,10`, the daemon aborts with these messages:
```
E Invalid ipv4:port given for --tx-proxy
E Failed to handle command line
I Deinitializing core...
```

If I specify the IP address given to the tor instance by Docker's networking (`--tx-proxy tor,192.168.176.2:9050,10`) it works fine.  `dig`/`nslookup` on the 'tor' hostname inside the container running monerod works fine.

The trouble with specifying the IP address is orchestration.  I have to explicitly setup a network and a specific IP address known for tor before I launch the docker-compose file.

## selsta | 2022-09-23T20:21:34+00:00
The discussion in https://github.com/monero-project/monero/issues/8562 might be related.

## househead | 2022-09-30T14:00:46+00:00
My way around this was to write an entrypoint.sh script up using bash command substitution (torprivoxy is a container in the same docker network - configured in docker-compose.yml):

```
#!/bin/bash
monerod --non-interactive --config-file=/data/monerod.conf --tx-proxy tor,$(dig +short torprivoxy):9050
```

Which I set in the Dockerfile:

ENTRYPOINT ["/entrypoint.sh"]

Then in docker-compose mount the entrypoint.sh script as a vol:

```
    volumes:
      - ${DATA_DIR:-./data}:/data
      - ./monerod/files/entrypoint.sh:/entrypoint.sh
```

OR (probably better) bake it into the container via Dockerfile and leave out the volume mount:

```
ADD ./files/entrypoint.sh /entrypoint.sh
RUN chmod 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```

My .onion peer seed nodes are in the monerod.conf file.

## hundehausen | 2025-02-16T17:16:55+00:00
This is still relevant also for monero suite, which runs only with docker containers.

## 5andr0 | 2026-01-27T07:42:19+00:00
I would also like to see a PR for this!
Additionally, when Tor is down, sending a transaction incorrectly succeeds without any warning in monero-gui, leaving it stuck in a pending state until it is resubmitted via `relay_tx`

For the time being you guys can use socat to relay `127.0.0.1:9050` to your desired tor server by hostname

```
tor_relay:
  image: alpine/socat:latest
  network_mode: "service:monerod"   # shares localhost with monerod
  command: >
    TCP-LISTEN:9050,bind=127.0.0.1,reuseaddr,fork
    TCP:tor:59050
  restart: unless-stopped
```

Whoever fixes both Problems, add your address in the PR and I will send you a donation.

I would patch it myself, but I have zero time right now.

# Action History
- Created by: sethforprivacy | 2021-09-21T13:17:23+00:00
