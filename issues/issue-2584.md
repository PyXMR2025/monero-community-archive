---
title: While on testnet, randomly generated wallets do not receive transactions
source_url: https://github.com/monero-project/monero/issues/2584
author: emesik
assignees: []
labels: []
created_at: '2017-10-05T22:26:46+00:00'
updated_at: '2019-06-24T14:49:45+00:00'
type: issue
status: closed
closed_at: '2017-10-07T21:54:26+00:00'
---

# Original Description
I've created own testnet. The setup/sandbox is present here: https://github.com/emesik/monero-testnet-sandbox

When I transfer coins between wallets that have been generated from 25-word seed, it works as expected (`walletA` and `walletB` are examples in the sandbox). 

However, if I generate a random wallet and send coins to the address it presents on startup, the new wallet never acknowledges incoming transactions. No matter if they are in mempool or already signed in a block, the new wallet always shows balances as 0/0. `refresh` command doesn't change anything. The wallet also doesn't receive freshly mined coins if I direct a daemon to mine to its' address. `walletC` in the sandbox is an example of it. 

The destination address is correct and coins aren't lost. The only way I found to recover them is:

1. Issue `seed` command in client running `walletC` and copy away the words.
2. Exit client.
3. Remove all wallet files.
4. Run client again with `monero-wallet-cli --testnet --restore-deterministic-wallet` and enter the 25 words.
5. The new wallet suddenly refreshes all transactions and displays correct balance.

The behavior is 100% reproducible. I tried it on several new wallets, rebooted the network from scratch. Always fails. I'm running `monero-0.11.0.0` and current testnet blockchain height is 425.

On real network I'm also using randomly generated wallet and it works perfectly.

# Discussion History
## perl5577 | 2017-10-05T23:34:19+00:00
When you are create wallet, wallet is connected on daemon?

I have already problem wallet create without start daemon . 

## emesik | 2017-10-06T03:09:25+00:00
I don't know. The client doesn't say explicitly when it connects to the node, but I guess it happens after wallet creation.

## moneromooo-monero | 2017-10-06T07:42:24+00:00
Try with https://github.com/monero-project/monero/pull/2542

## emesik | 2017-10-07T02:38:47+00:00
I rebuilt monero from latest master including that merge. Nothing has changed, the bug is still there.

## gsovereignty | 2017-10-07T02:51:18+00:00
If you delete the random wallets and regenerate them from the mnenomic does it work?

If that's the case it's probably getting the start sync height from mainnet instead of testnet, so the wallet is not syncing transactions from before block x.

## moneromooo-monero | 2017-10-07T10:22:07+00:00
Try https://github.com/monero-project/monero/pull/2596

## emesik | 2017-10-07T17:27:15+00:00
It doesn't help either.

Here's an example output of a freshly created wallet. I sent there 2.00 XMR which are visible in `show_transfers` as being in the pool. However, two blocks later the pool gets empty but balance is still 0.

```
Monero 'Helium Hydra' (v0.11.0.0-86e9de58)                 
Logging to monero-wallet-cli.log                           
Generated new wallet: 9uW1Y6N1RvK131tptvyyQyhWhTGakDBktG2LttdfwECTZLDHYnHHS9e9DEg9DhT5s2Qq3FY8UNhJZdNdttVVTigf3sM54zo  
View key: 3a15b644b646bff66b834580330299576a84f5b31963b64c0063b3984b24af03                                             
**********************************************************************                                                 
Your wallet has been generated!                            
To start synchronizing with the daemon, use "refresh" command.                                                         
Use "help" command to see the list of available commands.  
Always use "exit" command when closing monero-wallet-cli to save your                                                  
current session's state. Otherwise, you might need to synchronize                                                      
your wallet again (your wallet keys are NOT at risk in any case).                                                      


PLEASE NOTE: the following 25 words can be used to recover access to your wallet. Please write them down and store them somewhere safe and secure. Please do not store them in your email or on file storage services outside of your immediate control.

lair festival bogeys token umpire welders inkling coffee   
lobster silk gifts certain nocturnal pistons almost exquisite                                                          
gambit nasty setup afraid bunch pool bowling cohesive gifts                                                            
**********************************************************************                                                 
Monero 'Helium Hydra' (v0.11.0.0-86e9de58)                 
Logging to monero-wallet-cli.log                           
Opened wallet: 9uW1Y6N1RvK131tptvyyQyhWhTGakDBktG2LttdfwECTZLDHYnHHS9e9DEg9DhT5s2Qq3FY8UNhJZdNdttVVTigf3sM54zo         
**********************************************************************                                                 
Use "help" command to see the list of available commands.  
**********************************************************************                                                 
Starting refresh...          
Refresh done, blocks received: 0                                                                                       
Balance: 0.000000000000, unlocked balance: 0.000000000000  
Background refresh thread started                          
[wallet 9uW1Y6]: refresh     
Starting refresh...          
Refresh done, blocks received: 0                                                                                       
Balance: 0.000000000000, unlocked balance: 0.000000000000  
[wallet 9uW1Y6]: show_transfers                            
    pool     in      05:17:43 PM       2.000000000000 7dcae948240f99ee7697b813694f76cf409d760e044816d61b43aeff820f5234 0000000000000000 - 
[wallet 9uW1Y6]: refresh                                                                                               
Starting refresh...          
Refresh done, blocks received: 2                                                                                       
Balance: 0.000000000000, unlocked balance: 0.000000000000  
[wallet 9uW1Y6]: show_transfers                            
[wallet 9uW1Y6]:
```

## moneromooo-monero | 2017-10-07T17:59:13+00:00
Hmm, works for me. Can you log the value of m_refresh_from_block_height in wallet2.cpp,line 2207 (just before store_keys) ?

## emesik | 2017-10-07T21:54:26+00:00
Yes, it works! I must have used wrong binary in the last test.

BTW, the value reported in line 2207 is 0

## CoinLogik | 2018-01-29T02:51:39+00:00
@gazhayes 
> If that's the case it's probably getting the start sync height from mainnet instead of testnet, so the wallet is not syncing transactions from before block x.

But shouldn't that be fixed by `refresh`?

## acardi | 2018-02-06T12:49:46+00:00
Following commands solved the problem for me:

set refresh-from-block-height 1
rescan_bc


## nikitasius | 2019-06-24T14:49:45+00:00
> Following commands solved the problem for me:
> 
> set refresh-from-block-height 1
> rescan_bc

the same even those days on latest xmr client.

# Action History
- Created by: emesik | 2017-10-05T22:26:46+00:00
- Closed at: 2017-10-07T21:54:26+00:00
