---
title: When Will RPC Pay feature be available for GUI Wallets?
source_url: https://github.com/monero-project/monero/issues/7369
author: downystreet
assignees: []
labels: []
created_at: '2021-02-10T18:13:28+00:00'
updated_at: '2022-02-19T00:35:49+00:00'
type: issue
status: closed
closed_at: '2022-02-19T00:35:49+00:00'
---

# Original Description
I think it's been over a year now since the RPC pay feature was released but I was just wondering when exactly it will be available in the GUI wallets. It would be of great benefit to those who run nodes to be able to get rpc payments from the people using the GUI wallets, as I assume the GUI wallet is used more widely than the CLI wallet. 

# Discussion History
## moneromooo-monero | 2021-02-11T12:33:23+00:00
To be honest, I'm not sure it'll be so great. If was a nice idea in principle, but spies and other lowlives will surely set free RPC, attracting all noobs. So... that system may be of use only for things like pay-for-website-access or the like. Once again, assholes on hte internet ruining things for everyone else.

## Gingeropolous | 2021-02-26T03:53:36+00:00
In addition, there is a potential "attack" with this feature, wherein a malicious node could signal that it requires hashes for service, accept hashes for service, but then never delivers the services (I can't read the code well enough to know if this actually could occur, but architecturally it could). So, effectively, the malicious node can cryptojack users.  (well, until the user connects to a different node). I think this could be mitigated by the wallet recognizing that it is not receiving services for the hashes it is sending. 

@downystreet , I'm not as dire as @moneromooo-monero may be regarding the .... feasibility of a public RPC service network thing, but I do agree that more thought needs to be put into how it can be done in an adversarial environment. 

on the flipside, though, the electrum infrastructure in bitcoinland is pretty much the same - they encourage users to run their own electrum nodes to achieve the safest experience. But who actually does that? 

But on the flip flipside, electrum isn't part of the bitcoin core codebase - its a separate thing. 

## selsta | 2022-02-19T00:35:49+00:00
Please open a feature request to the GUI repo, though I don't think it currently has high priority as there are a lot of free public nodes.

# Action History
- Created by: downystreet | 2021-02-10T18:13:28+00:00
- Closed at: 2022-02-19T00:35:49+00:00
