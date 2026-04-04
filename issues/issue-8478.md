---
title: failed to get output distribution
source_url: https://github.com/monero-project/monero/issues/8478
author: bogdangainusa
assignees: []
labels: []
created_at: '2022-08-02T14:33:34+00:00'
updated_at: '2025-12-28T23:23:33+00:00'
type: issue
status: closed
closed_at: '2025-12-28T23:23:33+00:00'
---

# Original Description
Monero-rpc version:  Monero Fluorine Fermi (v0.18.0.0-release)


I am using method transfer to send out some funds, however it seems this cannot be processed and I am receiving this error. 
Also i posted logs from rpc-daemon. 

> {
  "error": {
    "code": -4,
    "message": "failed to get output distribution"
  },
  "id": "0",
  "jsonrpc": "2.0"

> Aug 02 16:29:54 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:54.022        E reorg_depth > m_max_reorg_depth. THROW EXCEPTION: error::reorg_depth_error
Aug 02 16:29:54 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:54.023        E Error parsing blocks: reorg exceeds maximum allowed depth, use 'set max-reorg-depth N' to allow it, reorg depth: 45478
Aug 02 16:29:54 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:54.023        E pull_blocks failed, try_count=3
Aug 02 16:29:54 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:54.026        E Exception at while refreshing, what=proxy exception in refresh thread
Aug 02 16:29:57 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:57.986        W Requested ring size 1 too low, using 16
Aug 02 16:29:58 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:58.055        W amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 821358 2085599 2400787 3257817 3430451 3442115 3454195 3466340 3472283 3473324 3473878 3476919 3477810 3478906 3479149 3479517
Aug 02 16:29:58 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:58.057        W amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 821358 2085599 2400787 3257817 3430451 3442115 3454195 3466340 3472283 3473324 3473878 3476919 3477810 3478906 3479149 3479517
Aug 02 16:29:58 vanilla monero-wallet-rpc[5935]: 2022-08-02 14:29:58.093        E rct_offsets.back() <= max_rct_index. THROW EXCEPTION: error::get_output_distribution

# Discussion History
## selsta | 2022-08-02T16:01:53+00:00
Mainnet / Stagenet / Testnet? Is your wallet fully synced? Are you running your own node?

## bogdangainusa | 2022-08-02T16:03:05+00:00
@selsta  Testnet and wallet is fully synced. 

## selsta | 2022-08-02T16:03:46+00:00
Are you running your own node?

## selsta | 2022-08-02T16:16:17+00:00
If you are running your own node, could it be that you updated to v0.18 too late? Testnet forked over a month ago. You will likely have to open the wallet with monero-wallet-cli and enter `set max-reorg-depth 2038385` or you have to resync your wallet from scratch.

## bogdangainusa | 2022-08-03T08:08:24+00:00
@selsta  Yes we did upgrade too late for version v.0.18. 
However last night we resynced our wallet from scratch, now it's up to latest block from network but error is the same. 
Please see photo attached 

![image](https://user-images.githubusercontent.com/13803843/182557799-f98beba8-64f6-47ad-8716-f69668abf5fa.png)


## selsta | 2022-08-03T14:18:00+00:00
Are you running your own node?

## bogdangainusa | 2022-08-03T14:21:34+00:00
@selsta  We are running our own central node on one server with & monero-wallet-rpc on other servers which are connected to our node.
From our main central node we are running like this 
`/home/cryptodaemon/bin/monerod --testnet --config-file /monerod.conf --detach`

And on our wallet servers:
`home/cryptodaemon/bin/monero-wallet-rpc --config-file /monero-rpc.conf --testnet`

Issue appeared after we switch to latest version. 


## selsta | 2022-08-03T14:25:00+00:00
What happens if you try to send a smaller amount?

## bogdangainusa | 2022-08-03T14:28:02+00:00
@selsta  Tried with different values, small & big and same result.

![image](https://user-images.githubusercontent.com/13803843/182633656-9f8cd963-8d7c-4a0c-9b99-94e95f02507c.png)


## bogdangainusa | 2022-08-03T14:32:55+00:00
@selsta  It seems 4 years ago same issue happened after fork.
https://github.com/monero-project/monero/issues/3581

## selsta | 2022-08-03T14:35:22+00:00
For testing purposes, does using monero-wallet-cli work when doing the same transaction (amount / receiver)?

## moneromooo-monero | 2022-08-03T14:54:32+00:00
If I post a patch to add logs to see what the code is doing, can you apply it and run with it, then post the logs ?

## bogdangainusa | 2022-08-03T14:55:25+00:00
@moneromooo-monero  Yes we can do it


## moneromooo-monero | 2022-08-03T15:25:10+00:00
Then please try this, apply with "patch -p1", it'll log at the default log level 0.

```
diff --git a/src/blockchain_db/lmdb/db_lmdb.cpp b/src/blockchain_db/lmdb/db_lmdb.cpp
index e2ac9df0b..0ba8e98e1 100644
--- a/src/blockchain_db/lmdb/db_lmdb.cpp
+++ b/src/blockchain_db/lmdb/db_lmdb.cpp
@@ -4317,7 +4317,10 @@ bool BlockchainLMDB::get_output_distribution(uint64_t amount, uint64_t from_heig
   distribution.clear();
   const uint64_t db_height = height();
   if (from_height >= db_height)
+{
+MGINFO("LMDB: failing, " << from_height << " " << db_height);
     return false;
+}
   distribution.resize(db_height - from_height, 0);
 
   MDB_val_set(k, amount);
diff --git a/src/cryptonote_core/blockchain.cpp b/src/cryptonote_core/blockchain.cpp
index 5b7b4353d..c3f2b0436 100644
--- a/src/cryptonote_core/blockchain.cpp
+++ b/src/cryptonote_core/blockchain.cpp
@@ -2357,8 +2357,12 @@ bool Blockchain::get_output_distribution(uint64_t amount, uint64_t from_height,
     start_height = 0;
   base = 0;
 
+MGINFO("BC: type " << (int)m_nettype << ", " << start_height << " " << from_height << " " << to_height);
   if (to_height > 0 && to_height < from_height)
+  {
+MGINFO("bad range");
     return false;
+  }
 
   if (from_height > start_height)
     start_height = from_height;
@@ -2366,9 +2370,15 @@ bool Blockchain::get_output_distribution(uint64_t amount, uint64_t from_height,
   distribution.clear();
   uint64_t db_height = m_db->height();
   if (db_height == 0)
+  {
+MGINFO("bad db");
     return false;
+  }
   if (start_height >= db_height || to_height >= db_height)
+  {
+MGINFO("beyond db: " << db_height);
     return false;
+  }
   if (amount == 0)
   {
     std::vector<uint64_t> heights;
@@ -2386,6 +2396,7 @@ bool Blockchain::get_output_distribution(uint64_t amount, uint64_t from_height,
   }
   else
   {
+MGINFO("calling LMDB");
     return m_db->get_output_distribution(amount, start_height, to_height, distribution, base);
   }
 }
diff --git a/src/rpc/core_rpc_server.cpp b/src/rpc/core_rpc_server.cpp
index 0fe28465f..2fa8781bd 100644
--- a/src/rpc/core_rpc_server.cpp
+++ b/src/rpc/core_rpc_server.cpp
@@ -3267,9 +3267,11 @@ namespace cryptonote
       const uint64_t req_to_height = req.to_height ? req.to_height : (m_core.get_current_blockchain_height() - 1);
       for (uint64_t amount: req.amounts)
       {
+MGINFO("Calling RpcHandler::get_output_distribution: " << amount << ", " << req.from_height << ", " << req.to_height << ", " << req.cumulative << ", " << req.binary << ", " << req.compress);
         auto data = rpc::RpcHandler::get_output_distribution([this](uint64_t amount, uint64_t from, uint64_t to, uint64_t &start_height, std::vector<uint64_t> &distribution, uint64_t &base) { return m_core.get_output_distribution(amount, from, to, start_height, distribution, base); }, amount, req.from_height, req_to_height, [this](uint64_t height) { return m_core.get_blockchain_storage().get_db().get_block_hash_from_height(height); }, req.cumulative, m_core.get_current_blockchain_height());
         if (!data)
         {
+MGINFO("No return");
           error_resp.code = CORE_RPC_ERROR_CODE_INTERNAL_ERROR;
           error_resp.message = "Failed to get output distribution";
           return false;
@@ -3280,6 +3282,7 @@ namespace cryptonote
     }
     catch (const std::exception &e)
     {
+MGINFO("Error: " << e.what());
       error_resp.code = CORE_RPC_ERROR_CODE_INTERNAL_ERROR;
       error_resp.message = "Failed to get output distribution";
       return false;
@@ -3322,9 +3325,11 @@ namespace cryptonote
       const uint64_t req_to_height = req.to_height ? req.to_height : (m_core.get_current_blockchain_height() - 1);
       for (uint64_t amount: req.amounts)
       {
+MGINFO("Calling RpcHandler::get_output_distribution: " << amount << ", " << req.from_height << ", " << req.to_height << ", " << req.cumulative << ", " << req.binary << ", " << req.compress);
         auto data = rpc::RpcHandler::get_output_distribution([this](uint64_t amount, uint64_t from, uint64_t to, uint64_t &start_height, std::vector<uint64_t> &distribution, uint64_t &base) { return m_core.get_output_distribution(amount, from, to, start_height, distribution, base); }, amount, req.from_height, req_to_height, [this](uint64_t height) { return m_core.get_blockchain_storage().get_db().get_block_hash_from_height(height); }, req.cumulative, m_core.get_current_blockchain_height());
         if (!data)
         {
+MGINFO("No return");
           res.status = "Failed to get output distribution";
           return true;
         }
@@ -3334,6 +3339,7 @@ namespace cryptonote
     }
     catch (const std::exception &e)
     {
+MGINFO("Error: " << e.what());
       res.status = "Failed to get output distribution";
       return true;
     }
diff --git a/src/rpc/rpc_handler.cpp b/src/rpc/rpc_handler.cpp
index d528ffef3..9d23c8eeb 100644
--- a/src/rpc/rpc_handler.cpp
+++ b/src/rpc/rpc_handler.cpp
@@ -40,11 +40,15 @@ namespace rpc
       } d;
       const boost::unique_lock<boost::mutex> lock(d.mutex);
 
+MGINFO("RpcHandler::get_output_distribution: " << amount << " " << from_height << " " << to_height << " " << cumulative << " " << blockchain_height);
       crypto::hash top_hash = crypto::null_hash;
       if (d.cached_to < blockchain_height)
         top_hash = get_hash(d.cached_to);
       if (d.cached && amount == 0 && d.cached_from == from_height && d.cached_to == to_height && d.cached_top_hash == top_hash)
+      {
+MGINFO("  processing cached distribution");
         return process_distribution(cumulative, d.cached_start_height, d.cached_distribution, d.cached_base);
+      }
 
       std::vector<std::uint64_t> distribution;
       std::uint64_t start_height, base;
@@ -74,7 +78,10 @@ namespace rpc
       {
         std::vector<std::uint64_t> new_distribution;
         if (!f(amount, d.cached_to + 1, to_height, start_height, new_distribution, base))
+        {
+MGINFO("f failed");
           return boost::none;
+        }
         distribution = d.cached_distribution;
         distribution.reserve(distribution.size() + new_distribution.size());
         for (const auto &e: new_distribution)
@@ -85,7 +92,10 @@ namespace rpc
       else
       {
         if (!f(amount, from_height, to_height, start_height, distribution, base))
+        {
+MGINFO("f failed");
           return boost::none;
+        }
       }
 
       if (to_height > 0 && to_height >= from_height)
@@ -107,6 +117,7 @@ namespace rpc
         d.cached = true;
       }
 
+MGINFO("processing new distribution");
       return process_distribution(cumulative, start_height, std::move(distribution), base);
   }
 } // rpc
```

## bogdangainusa | 2022-08-03T15:50:54+00:00
@moneromooo-monero  Sorry but for me it's not clear how to do that, can you detail a bit please? 

## selsta | 2022-08-03T15:52:44+00:00
Save the patch in a file called patch.txt, then do `git apply patch.txt` and then build monero and use this binary.

## bogdangainusa | 2022-08-03T15:55:20+00:00
@selsta  Thanks, this patch should be applied to monerod not to monero-wallet-rpc right? 

## selsta | 2022-08-03T15:58:41+00:00
You apply that to the monero repository and then you build monero and use the resulting `monerod`.

## bogdangainusa | 2022-08-03T22:41:54+00:00
@selsta  


```
Aug 04 00:40:38 vanilla monero-wallet-rpc[13706]: 2022-08-03 22:40:38.562        W Requested ring size 1 too low, using 16
Aug 04 00:40:38 vanilla monero-wallet-rpc[13706]: 2022-08-03 22:40:38.620        W amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 821358 2479345 3296597 3313152 3327734 3347693 3415186 3424669 3425525 3427574 3429332 3429540 3430285 3430477 3430747 3430830
Aug 04 00:40:38 vanilla monero-wallet-rpc[13706]: 2022-08-03 22:40:38.623        W amount=1.000000000000, real_output=0, real_output_in_tx_index=0, indexes: 821358 2479345 3296597 3313152 3327734 3347693 3415186 3424669 3425525 3427574 3429332 3429540 3430285 3430477 3430747 3430830
Aug 04 00:40:38 vanilla monero-wallet-rpc[13706]: 2022-08-03 22:40:38.657        E rct_offsets.back() <= max_rct_index. THROW EXCEPTION: error::get_output_distribution    
```



![image](https://user-images.githubusercontent.com/13803843/182724769-7989a2d0-e95c-4c42-81ff-37c570b1bc80.png)


## moneromooo-monero | 2022-08-04T06:10:08+00:00
That one means that the wallet received a distribution which does not go as far as at what the wallet owns. Are you really sure you rescanned the wallet ?

## bogdangainusa | 2022-08-18T12:42:20+00:00
@moneromooo-monero  Issue is still here. 
We have also updated to latest monero version but same output, resynced 2 times but didn't helped.


## selsta | 2022-08-18T17:28:17+00:00
Can you explain what you did exactly to "resync"?

## bogdangainusa | 2022-08-18T17:48:02+00:00
@selsta  Stopped monero daemon, deleted blockchain folder and start daemon again. 

I checked block height from time to time and it was updating till latest block available on network from this explorer.

https://community.rino.io/explorer/testnet/

```curl http://localhost:28089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"get_height"}' -H 'Content-Type: application/json' --digest``` 

## selsta | 2022-08-18T17:48:56+00:00
You have to rescan the wallet, not resync the daemon. There are different ways to do this, but the easiest would be restore from seed with restore height 1.

## bogdangainusa | 2022-08-19T12:17:14+00:00
@selsta  Thanks for your answer. 

Can you please be more specific how I can do that? I searched but didn't find any documentation or way how to do It. 

## bogdangainusa | 2022-08-28T18:28:48+00:00
@selsta  @moneromooo-monero  Any help with above question please? 

## selsta | 2022-08-28T20:34:31+00:00
You can use https://www.getmonero.org/resources/developer-guides/wallet-rpc.html#rescan_blockchain for example, or restore the wallet from seed.

## bogdangainusa | 2022-08-29T10:04:09+00:00
@selsta   Accordingly to monero documentation this command should work, however it's returning Method not found 

> curl http://127.0.0.1:28089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"rescan_blockchain"}' -H 'Content-Type: application/json' --digest -u monerorpc:password
> {
>   "error": {
>     "code": -32601,
>     "message": "Method not found"
>   },
>   "id": "0",
>   "jsonrpc": "2.0"
> 

Some others are working some not working

> curl http://127.0.0.1:28089/json_rpc -d '{"jsonrpc":"2.0","id":"0","method":"getblockcount"}' -H 'Content-Type: application/json' --digest -u monerorpc:password
> {
>   "id": "0",
>   "jsonrpc": "2.0",
>   "result": {
>     "count": 72295,
>     "status": "OK",
>     "untrusted": false
>   }


## selsta | 2022-08-30T00:32:44+00:00
I don't use wallet RPC myself. `rescan_blockchain` definitely exists as a command but I'm not sure what the correct way to call it is.

I would suggest to either use monero-wallet-cli to recreate the wallet from seed with restore height 1, or open the wallet in monero-wallet-cli and enter `rescan_bc hard` as a command.

The problem you have is purely testnet related because you used the wrong version over 1 month after the testnet hardforked.

## selsta | 2022-08-30T00:33:39+00:00
Use this command to restore from seed: `./monero-wallet-cli --testnet --restore-deterministic-wallet`

Afterwards use that wallet again for RPC.

## bogdangainusa | 2022-08-30T13:57:12+00:00
@selsta  

> root@monerod-test:~# monero-wallet-cli --testnet  --restore-deterministic-wallet
This is the command line monero wallet. It needs to connect to a monero
daemon to work correctly.
WARNING: Do not reuse your Monero keys on another fork, UNLESS this fork has key reuse mitigations built in. Doing so will harm your privacy.

> Monero 'Fluorine Fermi' (v0.18.1.0-release)
> Logging to monero-wallet-cli.log
> Specify a new wallet file name for your restored wallet (e.g., MyWallet).
> Wallet file name (or Ctrl-C to quit): cx-wallet
> Error: Attempting to generate or restore wallet, but specified file(s) exist.  Exiting to not risk overwriting.

## selsta | 2022-08-30T16:04:12+00:00
Use a different wallet name.

## jettero777 | 2022-10-08T13:55:16+00:00
I'm also sometimes getting error in RPC client:
```
2022-10-08 13:46:54.647 D Trying to create a tx now, with 1 destinations and 1 outputs
2022-10-08 13:46:54.647 D Using v5 rules
2022-10-08 13:46:54.647 D Using v8 rules
2022-10-08 13:46:54.647 D transfer_selected_rct: starting with fee 0.000029840000
2022-10-08 13:46:54.647 D selected transfers: 16
2022-10-08 13:46:54.647 D transfer: adding 0.000000000001, for a total of 0.000029840001
2022-10-08 13:46:54.648 D wanted 0.000029840001, found 0.003776860000, fee 0.000029840000
2022-10-08 13:46:54.648 D fake_outputs_count: 15
2022-10-08 13:46:54.648 D Requesting rct distribution
2022-10-08 13:50:24.649 D Problems at read: Operation canceled
2022-10-08 13:50:24.649 E Unexpected recv fail
2022-10-08 13:50:24.649 I Failed to invoke http request to  /get_output_distribution.bin
2022-10-08 13:50:24.649 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2022-10-08 13:50:24.649 W /root/monero/src/wallet/wallet2.cpp:14410:N5tools5error23no_connection_to_daemonE: no connection to daemon, request = /get_output_distribution.bin
2022-10-08 13:50:24.708 E !get_rct_distribution(rct_start_height, rct_offsets). THROW EXCEPTION: error::get_output_distribution
2022-10-08 13:50:24.708 W /root/monero/src/wallet/wallet2.cpp:8209:N5tools5error23get_output_distributionE: failed to get output distribution, request = Could not obtain output distribution.

```
after sweep_all command, using v0.18.1.2 and RPC and local node

wallet rescan or recreating wallet from scratch doesn't help, at the same time CLI is working normal

## selsta | 2022-10-08T14:50:42+00:00
@jettero777 That seems unrelated to the issue you are replying to.

Which OS are you using? Did you custom compile the RPC binaries?

Edit: Seems it takes 4 minutes during the "Requesting rct distribution" step and then times out. Do you use the same local node for both?

## jettero777 | 2022-10-08T15:14:18+00:00
@selsta 
I'm using AlmaLinux 8.6. I tried binaries (v0.18.1.0 and v0.18.1.2) and tried compiled from source (v0.18.1.2). The error is the same.
Yep, I'm using same local node for CLI and RPC.
The error happens not everytime, usually it works fine but on some random sweep_all tx it happens and is not working further with sending that tx no matter what, including restart, wallet recreation, etc. Only in CLI it works.
When it is working txs being send in few seconds, it is never gets a minute or more.

## selsta | 2022-10-15T21:07:08+00:00
@jettero777 As a work around you should be able to disable RPC SSL with `--rpc-ssl disabled` as a monerod flag.

## SamsungGalaxyPlayer | 2022-12-04T17:01:43+00:00
Adding here for visibility. This is the second report we have received on this error.

https://twitter.com/InnocuousFinch/status/1599442308235395072

## mmikeww | 2023-01-07T05:40:54+00:00
![image](https://user-images.githubusercontent.com/1900684/211133100-30786244-ad40-449b-b4c9-c4ec98ad8518.png)

this happened to me the other day, with Monero GUI 1.8.0 full node wallet on Windows.. creating transaction lags for a few mins, and then the "failed to get output distribution" error is shown. i tried closing and reopening/restarting node, and that worked to fix it. txn created and sent almost instantly.

then i got it again today, and closing/reopening did not work.

then i upgraded to GUI wallet v 18.1.2 , still getting the same problem. cant send my coins.

edit/
keep retrying many times, one time it lagged for a few mins as usual during create txn, and then it finally worked

## selsta | 2023-01-08T02:54:49+00:00
@mmikeww so you are running a local node? What kind of hardware do you have?

## mmikeww | 2023-01-08T02:58:02+00:00
Full node on my laptop. Amd Ryzen 7000, 32gb ram, chain stored on my
external NAS on regular HDDs

On Sat, Jan 7, 2023, 9:55 PM selsta ***@***.***> wrote:

> @mmikeww <https://github.com/mmikeww> so you are running a local node?
> What kind of hardware do you have?
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/8478#issuecomment-1374693711>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAOQBDDJWDHUO56VMXVJCRLWRIUALANCNFSM55LMWPYA>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


## selsta | 2023-01-08T02:58:48+00:00
monerod does not support network storage, that's likely the issue.

## mmikeww | 2023-01-08T03:00:25+00:00
How do you figure? It's works

On Sat, Jan 7, 2023, 9:58 PM selsta ***@***.***> wrote:

> monerod does not support network storage, that's likely the issue.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/monero-project/monero/issues/8478#issuecomment-1374694177>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAOQBDB5I4EGARC42GT5LYTWRIUPFANCNFSM55LMWPYA>
> .
> You are receiving this because you were mentioned.Message ID:
> ***@***.***>
>


## selsta | 2023-01-08T03:03:18+00:00
Please see: https://monero.stackexchange.com/a/13527

It's slow and there are reliability issues like you are reporting here.

## mmikeww | 2023-01-08T11:48:51+00:00
I will say that it is extremely slow, but I thought that was because of HDD instead of SSD. I will look into pruning and moving the chain to the local SSD on the laptop

# Action History
- Created by: bogdangainusa | 2022-08-02T14:33:34+00:00
- Closed at: 2025-12-28T23:23:33+00:00
