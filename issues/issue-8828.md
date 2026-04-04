---
title: cant connect with to wallet with windows monero gui
source_url: https://github.com/monero-project/monero/issues/8828
author: hubgitbb
assignees: []
labels: []
created_at: '2023-04-22T14:12:03+00:00'
updated_at: '2023-04-24T16:18:07+00:00'
type: issue
status: closed
closed_at: '2023-04-24T16:18:07+00:00'
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
- MONERO_GIT_TAG=latest
container_name: p2pool-monero
networks:
- p2pool
ports:
- 18080:18080/tcp
- 18081:18081/tcp
volumes:
- monero:/home/monero/.bitmonero:rw
- /dev/null:/home/monero/.bitmonero/bitmonero.log:rw
- /dev/hugepages:/dev/hugepages:rw
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
## selsta | 2023-04-22T14:38:23+00:00
Ignore the above comment, seems to be a scammer.

## plowsof | 2023-04-22T20:54:23+00:00
ill give him a second reason to think negatively about it: it _is_ a scam, ignore and ban @ahymedDEV from this repo :smile: 

## selsta | 2023-04-22T20:57:34+00:00
@hubgitbb  So you are running this on Windows? Mining inside a docker container on Windows is a bad idea. I'd avoid docker in this case.

Also remove 

```
--fast-block-sync=0
```

from your config, it's a bad setting for the average user.

## hubgitbb | 2023-04-23T08:25:52+00:00
the project https://github.com/SChernykh/p2pool/ is runing on linux/docker. 
the Monero GUI Wallet https://www.getmonero.org/downloads/  is runing on Windows.
i dont want to mine on windows.

## selsta | 2023-04-23T16:55:54+00:00
Try opening `http://your_ip:18081/get_info` in your browser on your Windows machine to see if it returns an info page. If nothing shows up try the same on the machine where you host the docker container.

## plowsof | 2023-04-24T01:27:17+00:00
monero-gui is looking @ localhost:18081 for a daemon. docker containers have their own ip address (not localhost) usually something like 172.0...  see https://stackoverflow.com/questions/17157721/how-to-get-a-docker-containers-ip-address-from-the-host or do some research on giving them a static ip.

but this feels out of scope for monero and i have no idea why you are making life difficult for yourself with docker windows/linux mash up.

## hubgitbb | 2023-04-24T14:31:27+00:00
i dont want to make things difficult. It can also be a webUI for connect to the wallet - if it´s easy. The monero windows gui is also not a "must have". I never thought it would be difficult to do what im trying to do.
So if i do http://your_ip:18081/get_info on my windows maschine i get some  info about the wallet. that means the connection to the container wallet works.

## selsta | 2023-04-24T14:50:05+00:00
> So if i do http://your_ip:18081/get_info

Can you make a screenshot of what you entered on the GUI when adding / editing the remote node?

## hubgitbb | 2023-04-24T15:52:30+00:00
![mwscr1](https://user-images.githubusercontent.com/11647819/234050171-85b98f5b-0e8c-46f9-952e-792c08898b4d.JPG)


## selsta | 2023-04-24T15:56:46+00:00
Try to add the following node:

```
Address: selsta2.featherwallet.net
Port: 18081
Username / Password blank
```

Are you able to connect to that node?

A couple more questions that might help with debugging:

- Which version are you using?
- Do you use a VPN?
- Do you have an anti-virus / firewall installed?

> I never thought it would be difficult to do what im trying to do.

It usually is as simple as adding the IP and port but something non obvious is going on here.

## hubgitbb | 2023-04-24T16:18:07+00:00
im not using VPN and firewall / antivirus are the windows build in stuff.
i have used version monero-gui-v0.17.3.1 and now i tried it with the newer version monero-gui-v0.18.2.2 and now it works
now that it's working I haven't tested the Address selsta2.featherwallet.net anymore.
thanks for your help @selsta and @plowsof 


# Action History
- Created by: hubgitbb | 2023-04-22T14:12:03+00:00
- Closed at: 2023-04-24T16:18:07+00:00
