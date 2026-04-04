---
title: Wallet is slow with 200k subaccounts
source_url: https://github.com/monero-project/monero/issues/9405
author: SChernykh
assignees: []
labels:
- wallet
created_at: '2024-07-25T21:02:44+00:00'
updated_at: '2025-12-20T08:40:46+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
Reported by Antidarknet:

> the official wallets are extremely unstable at 200,000 subaccounts if each has had at least one transaction in and one out. Try generating more subaccounts after 200k it takes many times longer to generate rather than when first initializing a wallet. The more accounts you add the slower it gets. Should probably fix that too. Don't take our word for it but test it yourselves.


# Discussion History
## preland | 2024-07-25T21:06:39+00:00
To be 100% clear: do we have any proof from Antidarknet that this is true?

I’m assuming that the issue is valid, but just making sure

## selsta | 2024-07-25T21:07:41+00:00
200k subaccounts is likely going to require a large amount of RAM so that should be taken into account when testing.

If I remember correctly by default it creates 200 subaddresses per account, 200k accounts will lead to 40M subaddresses.

## SChernykh | 2024-07-25T21:07:58+00:00
@preland  It is possible, based on wallet2 code track record. We just don't know what exactly can cause it.

## plowsof | 2024-07-25T21:39:01+00:00
related? https://github.com/monero-project/monero/issues/8740 , even better: https://github.com/monero-project/monero/issues/8926

## moneromooo-monero | 2024-08-17T14:58:35+00:00
Also https://github.com/monero-project/monero/pull/5370, though that was more about addressing memory usage.

## Gingeropolous | 2024-08-24T13:12:46+00:00
just a reminder there's a server with 256GB of memory ppl can use to test this on the monero research cluster.  contact me for access if you don't have it already

## tankf33der | 2025-01-05T13:09:24+00:00
If someone provides approximate steps on how to replicate this, I can handle all the remaining tedious work.

## preland | 2025-01-05T14:17:34+00:00
Has anyone tried the naive approach of simply spamming the rpc with create_account commands? While the original issue explicitly mentions 200k, that may just be them (antidarknet) outing their own setup rather than the actual point where the issue begins to occur (or be relevant)

## tankf33der | 2025-01-05T14:38:27+00:00
> Has anyone tried the naive approach of simply spamming the rpc with create_account commands?

doing. my server is 64GB RAM, if start swap i will ping @Gingeropolous for access to his one. 


## preland | 2025-01-05T15:17:50+00:00
How quickly is it completing each command? Not related to issue (probably), just curious 

## tankf33der | 2025-01-05T15:42:20+00:00
> How quickly is it completing each command? Not related to issue (probably), just curious

i am on 6k right now. BTW, master branch.
completing immediately.

## tankf33der | 2025-01-06T08:30:18+00:00
recent master. wallet generated - 251k accounts. no slowdown in all range. save to disk every 1k.

monero-wallet-cli takes 3.6GB RAM, load time of wallet 11secs on my dedicated server from hetzner.
you can download them - https://pulsar.pb1n.de/monero/
password: filename, two chars.

let me know if you want more.

## preland | 2025-01-06T14:20:19+00:00
The next step would be to receive and then send 1 transaction for every account

## tankf33der | 2025-01-06T14:58:43+00:00
New Info: 

as i wrote above - load 11sec. this is on RELEASE binary.

DEBUG monero-wallet-cli binary loads the same in 1m31sec.


## SChernykh | 2025-01-06T15:02:58+00:00
> The next step would be to receive and then send 1 transaction for every account

This should be done on a private testnet, preferably. This is 400k transactions we're talking about.

## tankf33der | 2025-01-07T17:56:03+00:00
While mining money on testnet for tests i am implementing picolisp library for monero, will start coding soon. 

Very flexible, i will be able to do via json_rpc whatever i want.  

## tankf33der | 2025-01-10T12:53:49+00:00
Monero library is ready and already sent 5k transactions (chunk is 128 subaccounts) via `transfer_split`. 

To get `out` transactions for every subaccount will be straightforward and take some time.


## tankf33der | 2025-01-11T17:51:59+00:00
> > The next step would be to receive and then send 1 transaction for every account
> 
> This should be done on a private testnet, preferably. This is 400k transactions we're talking about.

software is ready and how to get access of private testnet ?

## SChernykh | 2025-01-11T17:55:12+00:00
By private testnet I meant a testnet that you run yourself - by using `--add-exclusive-node IP:port` to only connect to your own nodes.

## SChernykh | 2025-01-11T18:04:37+00:00
And once you start using `--add-exclusive-node`, you never remove it on those nodes (otherwise they will connect to the regular testnet again and there might be a conflict). You will also need to start mining on one of the nodes to get some blocks going.

## tankf33der | 2025-01-13T19:22:30+00:00
> By private testnet I meant a testnet that you run yourself - by using `--add-exclusive-node IP:port` to only connect to your own nodes.

I have got private testnet, modifed monerod to get 1M+ coins fast after mining.

Now i have 2GB file with 200k subaccounts. 50% have in-out txs, and 50% have only in tx.
Not bad for first attempt.

1. `monero-wallet-cli`: `account new` - command as fast as first creation, no issue. `show_transfers` output ~5 secs.
2. `monero-wallet-rpc`: OMG, commands replies so slow. I thought I had patience, but I can't wait for the `get_accounts` output. This needs to be checked later by somebody with `curl`.
3. `monero-wallet-gui`: _UNKNOWN_.

I can upload the wallet file publicly if anyone is interested.

## FabriLluvia | 2025-12-20T02:58:48+00:00
I'll do some testing

## plowsof | 2025-12-20T08:40:46+00:00
https://github.com/Rucknium/xmrspammer/tree/main also confirms this

# Action History
- Created by: SChernykh | 2024-07-25T21:02:44+00:00
