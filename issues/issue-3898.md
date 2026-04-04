---
title: 'High Fee Mitigation: Trusted Nodes for Simple Mode'
source_url: https://github.com/monero-project/monero-gui/issues/3898
author: reemuru
assignees: []
labels: []
created_at: '2022-04-27T17:21:48+00:00'
updated_at: '2022-05-02T14:46:26+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
> Update remote node scanner from simple mode and use hardcoded trusted community nodes.

@selsta 

Reference:

#3897 

# Discussion History
## jeffro256 | 2022-04-28T18:57:39+00:00
If a PR is to be created from this, make sure to also use hardcoded SSL certificates for said nodes

## jeffro256 | 2022-04-30T17:39:03+00:00
I think we should keep the public node list, but each entry must be verified by a chain of SSL certificates which is signed by one of a small set of hard coded root certificates, much like an HTTPS-like certificate authority. 

## selsta | 2022-05-01T05:13:00+00:00
But there is no "public node list". Currently the daemon is used for a p2p node scanner, but I want to remove that because it removes the dependency on the daemon. I'll look into SSL certs.

## jeffro256 | 2022-05-01T23:31:47+00:00
We could create an RPC command that retrieves a daemon's p2p public node list. So on start, the wallet runs the command `get_public_nodes` (or similar) on a *trusted* node, caches the list, randomly picks one from the list, connects to it, checks that it has a verified SSL certificate, and only then starts syncing and asking it for fee estimations. This would allow for a safer environment for users while still remaining scalable and decentralized (not all traffic routed through a small set of nodes). 

Furthermore, the node information (IP + SSL cert) could be saved for each transaction in the wallet file. In the case that a node gave a wallet a ridiculous fee / bad decoys / etc, one could pull up the SSL signed message and "blame" that cert. They could copy/paste that information to the devs and further steps could be taken to revoke that certificate. 

Edit: I know about `get_connections` but by `get_public_nodes` I mean a list where the node would only relay connections with RPC port open and a valid SSL certificate. 

## selsta | 2022-05-02T09:04:49+00:00
There are two things to consider:

- Passive spy nodes (setup by blockchain analysis companies)
- Actively malicious nodes

I would like to avoid both. Yes, it's possible for trusted community nodes to spy too, but the chance is way lower than when selecting a random node in the network.

I'll check into SSL certs, but currently I only plan to use a trusted node list. 

## jeffro256 | 2022-05-02T14:46:25+00:00
> Yes, it's possible for trusted community nodes to spy too, but the chance is way lower than when selecting a random node in the network.

Yeah I'm saying that it shouldn't broadcast random nodes in the network, only those who are signed by a small group of hardcoded community certs

> I'll check into SSL certs, but currently I only plan to use a trusted node list.

This will still maintain the "trusted" aspect of your idea, but now the trusted nodes don't have to be tied down to the same IP address, they can add server nodes and delegate load to them. Also, if someone from the trusted group loses their public IP (changing hosting sites for example) then they can easily move their server without everyone having to recompile their code / download new binaries. 

# Action History
- Created by: reemuru | 2022-04-27T17:21:48+00:00
