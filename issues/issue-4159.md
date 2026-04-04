---
title: cant connect to wallet  with windows monero gui
source_url: https://github.com/monero-project/monero-gui/issues/4159
author: hubgitbb
assignees: []
labels: []
created_at: '2023-04-22T14:40:27+00:00'
updated_at: '2023-06-20T20:40:48+00:00'
type: issue
status: closed
closed_at: '2023-06-20T20:40:48+00:00'
---

# Original Description
Hi,
i have build a p2pool with Docker Compose https://github.com/SChernykh/p2pool/tree/master/docker-compose.
Now im trying to connect with the windows monero-gui-v0.18.2.2 to the p2pool-monero container, which i think is also the monero wallet, but the monero gui doesent connect.
I also have added the port 18081 in the docker file witch looks like this

monero:
image: monero:latest
build:
context: monero
args:
    MONERO_GIT_TAG=latest
    container_name: p2pool-monero
    networks:
    p2pool
    ports:
    18080:18080/tcp
    18081:18081/tcp
    volumes:
    monero:/home/monero/.bitmonero:rw
    /dev/null:/home/monero/.bitmonero/bitmonero.log:rw
    /dev/hugepages:/dev/hugepages:rw
    restart: unless-stopped
    command: >-
    --zmq-pub tcp://0.0.0.0:18083
    --disable-dns-checkpoints
    --enable-dns-blocklist
    --out-peers 32
    --in-peers 16
    --add-priority-node=nodes.hashvault.pro:18080
    --add-priority-node=node.supportxmr.com:18080
    --non-interactive
    --p2p-bind-ip=0.0.0.0
    --p2p-bind-port=18080
    --rpc-bind-ip=0.0.0.0
    --rpc-bind-port=18081
    --restricted-rpc
    --confirm-external-bind
    --log-level=0
    --prune-blockchain
    --fast-block-sync=0

container is started and synced.
what can i check to get the gui connected?

# Discussion History
## 2hot2exist | 2023-06-20T13:40:13+00:00
There's a couple things you can try to do:

- check ufw if the port is whitelisted (if you have one)
- check the logs with `docker logs p2pool-monero`
- test the connectivity with curl on your windows host:
`curl http://<DockerHostIP>:18081/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}' -H 'Content-Type: application/json'`

This should give you an idea of what's wrong.


## selsta | 2023-06-20T20:40:48+00:00
Resolved in https://github.com/monero-project/monero/issues/8828

# Action History
- Created by: hubgitbb | 2023-04-22T14:40:27+00:00
- Closed at: 2023-06-20T20:40:48+00:00
