---
title: 'Bug: start_height not being respected both in "refresh" RPC call and Wallet.cpp
  API.'
source_url: https://github.com/monero-project/monero/issues/9362
author: AlwaysCompile
assignees: []
labels:
- bug
- more info needed
created_at: '2024-06-11T18:57:21+00:00'
updated_at: '2025-06-29T14:06:11+00:00'
type: issue
status: open
closed_at: null
---

# Original Description
After analyzing #9358  my friend told me there is a bug in Monero software. The software does not respect "start_height" during refreshes. Instead, it will always override the passed height.

You can see this in refresh() in Wallet2.cpp:

`// always reset start_height to 0 to force short_chain_ history to be used on
  // subsequent pulls in this refresh.
  start_height = 0;`

Except it is not "subsequent pulls", but ALL pulls including pulls with explicitly passed start heights. Looking at issue #9358 you see the reproduction steps for this using the wallet RPC. Explicitly passed heights seem to be completely ignored despite the docs saying they will be respected.

For example, the "refresh" RPC call specifically states this:

> start_height - unsigned int; (Optional) **The block height from which to start refreshing**. Passing no value or a value less than the last block scanned by the wallet refreshes from the last block scanned.

However, in practice, it does not work this way in any sense neither from the passed value or the last value scanned. No matter what value is passed it will always refresh based on the blockchain size and the granularity value described in #9361.

I think this is a bug because it is contrary to the documentation and clearly the explicitly passed start_height is not being respected as it should be. 


# Discussion History
## shoriwe | 2025-06-28T17:13:13+00:00
I can confirm this behavior, my only workaround is:

1. First modify the wallet with CLI and set `refresh-from-block-height` manually to 0.

```
set refresh-from-block-height 0
```

2. Subsequent RPC calls to Refresh should work as expected from there

## shoriwe | 2025-06-28T17:25:56+00:00
> I'm not a maintainer just pointing based on my small knowledge of the code:

- Here is the definition of that RPC: 
https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/wallet/wallet_rpc_server.h#L135

- Which callback is defined here:
https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/wallet/wallet_rpc_server.h#L231

- Its implementation can be found at:
https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/wallet/wallet_rpc_server.cpp#L3383

- Apparently there is no hard-coded value:
https://github.com/monero-project/monero/blob/c572e1ad00802fc83b756460838d01436a512750/src/wallet/wallet_rpc_server.cpp#L3394C17-L3394C24

So my assumption is, the request (`const wallet_rpc::COMMAND_RPC_REFRESH::request& req`) is being defaulted to some value or the final function call (see above URL) is changing the value during its call.

## nahuhh | 2025-06-28T17:51:00+00:00
@shoriwe  what version are you using? I believe this should be fixed

## shoriwe | 2025-06-28T17:57:02+00:00
Hi @nahuhh:

```
> monero-wallet-rpc --version
Monero 'Fluorine Fermi' (v0.18.4.0-release)
```

## plowsof | 2025-06-28T18:02:24+00:00
are we trying to resync from 0? or open an old wallet and skip to the future? * what is `auto_refresh` set to during these? true/false?

if resync from 0, it seems the definition of `rescan_blockchain` could be misinterpreted.  "from scratch" appears to be the wallets restore height. [1](https://docs.getmonero.org/rpc-library/wallet-rpc/#rescan_blockchain)

## shoriwe | 2025-06-28T18:07:31+00:00
Yeah, my current workflow is as follows:

1. Create a wallet with the CLI. For some reason. Don't know why, `refresh-from-block-height` starts with a higher value than the currently synced daemon. (Daemon is always 100% sinced)
2. I then call the `refresh` RPC with the start height equal to 0 (this doesn't work) and when set equal to 1 it also doesn't work.
3. My only fix to this is, return to the CLI and modify `refresh-from-block-height` to `0`'

Maybe the Documentation should be updated to point that a value equal to zero is the same to using the defined `refresh-from-block-height`. And `1` really means start from the begining -> first block 

## plowsof | 2025-06-28T18:14:52+00:00
> 1. Create a wallet with the CLI. For some reason. Don't know why, `refresh-from-block-height` starts with a higher value than the currently synced daemon. (Daemon is always 100% sinced)

hm, on testnet, if i create a wallet without being connected to a ~~remote node~~ daemon* - the height estimate seems off (greater than reality) and i have to manually fix that later. if the estimate is off for mainnet, this should be fixed imo

>Passing no value or a value less than the last block scanned by the wallet refreshes from the last block scanned.

the rpc refresh call : as described will, if passed a height smaller than the last block scanned will simply ignore it.

atm the quick method i use is to use cli as you also do to set the refresh-from-block-height 0. exiting the cli, and deleting the wallet cache file (you have a `wallet_name` and `wallet_name.keys`, `wallet_name` can be deleted , and then i open `wallet_name.keys` and it syncs from 0. pls make backups of course 

## shoriwe | 2025-06-28T18:24:08+00:00
In that case, can we force the wallet creation to force `refresh-from-block-height` value to `0` in case there is no daemon connected? I mean, add this behavior to both the CLI and GUI wallet creation

Or at least document this somewhere so unexperienced users can know how to debug out of sync wallets?

## nahuhh | 2025-06-28T19:08:14+00:00

> 1. Create a wallet with the CLI. For some reason. Don't know why, `refresh-from-block-height` starts with a higher value than the currently synced daemon. (Daemon is always 100% sinced)

block heights are estimated when there is no daemon connected

> 2. I then call the `refresh` RPC with the start height equal to 0 (this doesn't work) and when set equal to 1 it also doesn't work.

you cant set the start height lower than the current block height. Setting the start height is for skipping forward

> 3. My only fix to this is, return to the CLI and modify `refresh-from-block-height` to `0`'

this changes the restore height. I assume you rescan the blockchain after this?

> Maybe the Documentation should be updated to point that a value equal to zero is the same to using the defined `refresh-from-block-height`. And `1` really means start from the begining -> first block

Aiui, a value equal to 0 is the genesis block. Running rescan blockchain with a 0 value means sync from genesis. 1 is sync from block 1.

> force refresh-from-block-height value to 0 in case there is no daemon connected?

there this would set a wallets restore height to genesis, which is probably not ideal.

i imagine a better workaround would be to set it a few thousand blocks before the estimate

## shoriwe | 2025-06-29T13:25:23+00:00
> block heights are estimated when there is no daemon connected

That is correct, the problem with this approach is the estimation doesn't seems to be even near the actual blockchain height.

> you cant set the start height lower than the current block height. Setting the start height is for skipping forward

Cool, could we put this exact description at the [WalletRPC docs](https://docs.getmonero.org/rpc-library/wallet-rpc/?h=refresh#refresh)? Current documentation doesn't seem to represent the actual behavior.

> this changes the restore height. I assume you rescan the blockchain after this?

That is correct, I made that modification from the CLI because I didn't found a way to do it from the RPC. Then as you already mentioned, the `refresh` successfully synced my wallet with the blockchain.

> Aiui, a value equal to 0 is the genesis block. Running rescan blockchain with a 0 value means sync from genesis. 1 is sync from block 1.

Thanks for clarifying. Again, as mentioned earlier could we include this in the Docs?

> there this would set a wallets restore height to genesis, which is probably not ideal.

You are correct, that is not convenient specially for those with slower computers.

> i imagine a better workaround would be to set it a few thousand blocks before the estimate

I Agree, the only thing that comes to my mind is an hypothetical case in which the Blockchains Hash rate spikes and there ended more blocks mined for the current time the wallet is created.

Lets experiment with some thousands blocks behind the estimate first. Anyway, if we are still pointing after the real height we can open a issue again.

## nahuhh | 2025-06-29T13:51:37+00:00
> > block heights are estimated when there is no daemon connected
> 
> That is correct, the problem with this approach is the estimation doesn't seems to be even near the actual blockchain height.

what block height are you seeing on creation, and what is the actual block height?

> > you cant set the start height lower than the current block height. Setting the start height is for skipping forward
> 
> Cool, could we put this exact description at the [WalletRPC docs](https://docs.getmonero.org/rpc-library/wallet-rpc/?h=refresh#refresh)? Current documentation doesn't seem to represent the actual behavior.

it is already there
```
Passing no value or a value less than the last block scanned by the wallet refreshes from the last block scanned.
```

i can perhaps modify the description to indicate that its used to skip forward

> > Aiui, a value equal to 0 is the genesis block. Running rescan blockchain with a 0 value means sync from genesis. 1 is sync from block 1.
> 
> Thanks for clarifying. Again, as mentioned earlier could we include this in the Docs?

i think this should be obvious (?). The block heights are the actual block heights. (Genesis is block 0, the first block mined is block 1, tenth is block 10 etc)



## shoriwe | 2025-06-29T14:06:11+00:00
Thanks for clarifying @nahuhh. Official documentation says the following:

```
start_height - unsigned int; (Optional) The block height from which to start refreshing. Passing no value or a value less than the last block scanned by the wallet refreshes from the last block scanned.
```

Based on this I understand the following. In the scenario of having an incorrect estimated `refresh-from-block-height` which usually happens when there is no connected Daemon:
- If passed `0` to `refresh` it tries to scan with the incorrect `refresh-from-block-height`
- If passed `1` to `refresh` even when this block is the first block, since last scanned block was the equal or greater than `refresh-from-block-height` there are no blocks scanned.
- The only case `refresh` could successfully scan the blockchain will be, wait for the blockchain actually reach `refresh-from-block-height` (in my test cases the wrong estimate of `refresh-from-block-height` is always upper to the current height block)

Using a `estimate - thousands` will in deed prevent this behavior. So, based on what you said:

> i can perhaps modify the description to indicate that its used to skip forward

And

> i think this should be obvious (?). The block heights are the actual block heights. (Genesis is block 0, the first block mined is block 1, tenth is block 10 etc)

Apart from the current incorrect estimate of which you already proposed a possible solution (`estimate - thousands`) I think that apart from the Code fix. Docs need to be in sync with the idea, since `refresh` function has this unclear behavior of skipping blocks that it thinks it already scanned. 

# Action History
- Created by: AlwaysCompile | 2024-06-11T18:57:21+00:00
