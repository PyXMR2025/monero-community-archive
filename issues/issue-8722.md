---
title: 'Discussion: deprecation/removal of pay-to-use RPC system from core repo'
source_url: https://github.com/monero-project/monero/issues/8722
author: jeffro256
assignees: []
labels: []
created_at: '2023-01-28T21:25:02+00:00'
updated_at: '2024-07-30T20:57:25+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
## What It Is
The pay-to-use RPC system was added in PR #5357. Node operators can specify an XMR address for public RPC which clients must mine to in order to access their RPC. The idea was that node operators could be compensated some of the cost of operating a node, and that they would compete for the lowest RPC cost by manually adjusting the amount of "credits" received for a hash of certain difficulty. "Credits" are rewarded by clients submitting a valid block (except for network difficulty) which is mined to the node operator receive address, similar to how miner shares are rewarded in a traditional centralized mining pool.

## Is this feature used in the wild?
I created a python network crawler which counts how many public nodes on mainnet have this feature enabled. This script requires that a local unrestricted daemon is running with a well established p2p list.

```python3
import random
import requests

my_daemon_address = 'localhost:18081'
timeout_secs = 10

def invoke_json(addr, uri, json_data):
	resp = requests.post("http://" + addr + '/' + uri, json=json_data, timeout=timeout_secs)
	#assert(resp.status_code == 200)
	resp_json = resp.json()
	if 'json_rpc' not in uri:
		assert(resp_json['status'] == 'OK')
	return resp_json

def invoke_json_rpc(addr, method, params):
	json_data = {'method': method, 'params': params}
	resp_json = invoke_json(addr, 'json_rpc', json_data)
	result = resp_json.get('result')
	error = resp_json.get('error')
	return result, error

def is_peer_info_public_ipv4(peer_info):
	return ':' not in peer_info['host'] and 'rpc_port' in peer_info

def make_ipv4_addr(peer_info):
	return peer_info['host'] + ':' + str(peer_info['rpc_port'])

def filter_nodes(peer_list):
	return [make_ipv4_addr(peer) for peer in peer_list if is_peer_info_public_ipv4(peer)]

# Build valid public IPv4 node list
peers_res = invoke_json(my_daemon_address, 'get_peer_list', {})
white_peer_addrs = filter_nodes(peers_res['white_list'])
gray_peer_addrs = filter_nodes(peers_res['gray_list'])
random.shuffle(white_peer_addrs)
random.shuffle(gray_peer_addrs)
ipv4_public_addrs = white_peer_addrs + gray_peer_addrs # try white nodes before gray nodes
print('Found {} white, {} gray, and {} total IPv4 public nodes.'.format(len(white_peer_addrs), len(gray_peer_addrs), len(ipv4_public_addrs)))

# Connect to each peer and check RPC payment access
total_access_enabled = 0
total_access_not_enabled = 0
total_connection_failure = 0
for peer_addr in ipv4_public_addrs:
	print('Connecting to {}...'.format(peer_addr))
	try:
		rpc_access_info, error_res = invoke_json_rpc(peer_addr, 'rpc_access_info', {})
		# We check if access is enabled mainly by checking for JSONRPC error code CORE_RPC_ERROR_CODE_INVALID_CLIENT (-15)
		access_enabled = (error_res is not None and error_res['code'] == -15) or rpc_access_info['diff'] > 0
		if access_enabled:
			print('Pay-to-use RPC access enabled.')
			total_access_enabled += 1
		else:
			print('Pay-to-use RPC access NOT enabled.')
			total_access_not_enabled += 1
	except KeyboardInterrupt:
		break
	except requests.exceptions.ConnectionError:
		print('Connection failed: timeout')
		total_connection_failure += 1
	except Exception as e:
		print('Connection failed <{}>: {}'.format(type(e), str(e)))
		total_connection_failure += 1
	
	print('{} access enabled, {} access not enabled, {} offline.'.format(total_access_enabled, total_access_not_enabled, total_connection_failure))
```

So you don't have to take my word for it, but I find that only <3% of public nodes have the pay-to-use RPC system enabled. Last time I scanned, 13 had it enabled, and 470 did not have it enabled.

## Reasons to Remove
* Makes wallet development much more complicated, especially for adding new types of connection modes, since tracking credits is very finnicky.
* Most endpoints do not require credits.
* Bootstrap node selector does not sort public nodes by cost, so the "competing for lowest price" aspect is more or less moot.
* Most public nodes don't require RPC payment anyways.
* The main wallet type that uses RPC with public nodes (Monero GUI w/ Bootstrap Mode) will not mine and submit nonces b/c it does not use `wallet2::search_for_rpc_payment`.
* An RPC payment system could be implemented as a seperate reverse proxy server on the server side and a forward proxy on the client side to keep core wallet/daemon code simpler.
* The client payment ID signatures (especially persistent IDs) and payment cookies are detrimental to anonymity by allowing malicious nodes to create strong unique identifiers.
* It's becoming increasingly more apparent that connecting to random public nodes without block verification can be detrimental to privacy and can introduce weaknesses where random public nodes give bad fee information etc. The credit system makes less sense in this adversarial environment because it assumes that node operators will honor credits.
* AFAIK, this is not a feature that is present in other cryptocurrencies because there has not been a demonstrated need for such a system elsewhere.
* As @tobtoht pointed out, including mining software inside the wallet clients may cause UX issues where AV software falsely flags the wallet software as malicious.
* Scripts, RPC libraries, etc must implement RCT cryptography just to use RPC with public nodes that have `--rpc-payment-address` specified.

## What to do 

I have already drafted a PR to remove the payment system if there is support for this. I would like opposing opinions on the matter if one feels strongly about it.

# Discussion History
## plowsof | 2023-01-28T22:11:52+00:00
IRC discussion on this topic for visibility - beginning here https://libera.monerologs.net/monero-dev/20230127#c196498
and https://libera.monerologs.net/monero-dev/20230129#c197576

## moneromooo-monero | 2023-01-30T17:44:05+00:00
> As @tobtoht pointed out, including mining software inside the wallet clients may cause UX issues where AV software falsely flags the wallet software as malicious.

That one is a bad argument. It's kowtowing to people who are pissing on you and don't even care to look whether you're there.

I think it can be removed though. The incentives are wrong for the adversarial case. However, the incentives are right for third party usage, like micropayments for online services, like Primo (https://repo.getmonero.org/selene/primo) does. But it seems that nobody cares, so...


## SamsungGalaxyPlayer | 2023-01-31T16:51:30+00:00
@moneromooo-monero while it is stupid (I 100% agree with you), I can say from personal experience that Cake has been marked as malware and denied access to pretty basic tools simply because the mining code (that we don't use) is bundled in there. This also happens to the official GUI, etc.

We are complain all we want about it, but from a practical perspective, I'd rather it be removed/isolated. We can't force people like antivirus companies to care enough. But we can avoid cases where people who won't mine don't need to run into these annoyances.

Yes, I've complained to several companies about them marking Cake as a virus because we have the official Monero mining code. They simply do NOT care, no matter how much I spell it out for them.

Edit: I support fluffy's comments [here](https://libera.monerologs.net/monero-dev/20230129#c197585): remove from wallet code; I don't particularly care as much about node code.

## iamamyth | 2023-02-03T16:41:32+00:00
I think the wallet + miner being marked by AV software shows the separation of concerns problem: Wallets are for paying already-held currency and receiving currency to facilitate the former. Therefore, mining doesn't match their scope. If a service says, "you need to pay for use", the wallet has a way of doing that: By initiating a transaction. If a service says, "you must pay in mining shares", then the wallet simply shouldn't act as the payment channel; anyone wanting to use such a service in conjunction with the wallet can run a "mining shares" equivalent to the wallet, i.e. run a miner to accumulate a balance of mining shares with the service, and forward service authentication credentials to the wallet.

## fullmetalScience | 2024-05-16T06:55:58+00:00
> like Primo (https://repo.getmonero.org/selene/primo) does. But it seems that nobody cares, so...

It's a great tool that's probably a bit ahead of it's time. Self-hosting audiovisual content is expensive and most content creators would not be able to afford it before they are big. Then, when they are, they are pretty much locked in to their platform of "choice".

While Nostr with sites like flare.pub (where hosting is for the user to select) could help against getting locked in, a tool like Primo could fund the expenses for those who want to go independent. While removing the functionality from core, it's something to keep in mind for future (separate) interfaces to Monero.

## kayabaNerve | 2024-07-11T22:08:57+00:00
I'm late to this discussion but I'm in strong favor of this. If someone wants to pay for RPC calls, they can set up access tokens on their end. If this was successfully used, maybe? Yet the world has gone in favor of either free services (potentially internally subsidized), or corporate-level nodes which have their own infrastructure (not pick a random node and obtain 'credits').

## thisIsNotTheFoxUrLookingFor | 2024-07-27T10:14:12+00:00
ACK to remove this. Also have seen MSFT Defender for Endpoint restricting the GUI wallet because it thinks it is in the "cryptominer" category of applications that it thinks should not exist in the enterprise.

## jeffro256 | 2024-07-30T20:57:24+00:00
@tortxoFFoxtrot Removing support for this feature won't remove mining binary code inside the GUI wallet build, and thus probably won't change antivirus behavior. Solo mining and p2pool mining to one's own wallet is supported in "Advanced Mode". 

# Action History
- Created by: jeffro256 | 2023-01-28T21:25:02+00:00
