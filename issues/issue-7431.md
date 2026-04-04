---
title: Weird errors creating wallet via RPC
source_url: https://github.com/monero-project/monero/issues/7431
author: mrx23dot
assignees: []
labels: []
created_at: '2021-03-05T15:04:54+00:00'
updated_at: '2023-08-09T00:19:52+00:00'
type: issue
status: closed
closed_at: '2023-08-09T00:19:52+00:00'
---

# Original Description
1,
monero-wallet-rpc --wallet-dir . --rpc-bind-port 28089 --rpc-bind-ip 127.0.0.1 --disable-rpc-login

Monero 'Oxygen Orion' (v0.17.1.9-release)
Win10 x64

2,
Issue RPC call
```
cmd1 = {
 "method": "create_wallet",
 "params": {
    "filename":"wallet",
    "password":"54b6565r7hhDSTH!",
    "language":"English"
  }
}
```

3,
warnings in console:
```
2021-03-05 14:49:49.970 W Espa+¦ol word 'asa' is shorter than its prefix length, 4
2021-03-05 14:49:49.971 W Espa+¦ol word 'ave' is shorter than its prefix length, 4
2021-03-05 14:49:49.972 W Espa+¦ol word 'boa' is shorter than its prefix length, 4
2021-03-05 14:49:49.972 W Espa+¦ol word 'cal' is shorter than its prefix length, 4
2021-03-05 14:49:49.973 W Espa+¦ol word 'dar' is shorter than its prefix length, 4
2021-03-05 14:49:49.974 W Espa+¦ol word 'don' is shorter than its prefix length, 4
2021-03-05 14:49:49.974 W Espa+¦ol word 'dos' is shorter than its prefix length, 4
```

Wallet file created **20secs** (!) after POST. Files:
  wallet.keys
  wallet

4,
```
cmd2 = {
 "method": "open_wallet",
 "params": {
    "filename":"wallet",
    "password":"54b6565r7hhDSTH!",
  }
}
```

5,
```
2021-03-05 14:50:07.766 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon   <-- **I never wanted to connect!**
2021-03-05 14:50:07.767 E Exception at while refreshing, what=no connection to daemon
2021-03-05 14:50:29.778 E !r. THROW EXCEPTION: tools::error::no_connection_to_daemon
2021-03-05 14:50:29.779 E Exception at while refreshing, what=no connection to daemon
2021-03-05 14:50:58.823 E Failed to open ./wallet.keys: system:32
2021-03-05 14:50:58.825 E !is_keys_file_locked(). THROW EXCEPTION: error::wallet_internal_error    <-- **why??**
```

full log:
[monero-wallet-rpc.log](https://github.com/monero-project/monero/files/6091329/monero-wallet-rpc.log)


# Discussion History
## moneromooo-monero | 2021-03-05T16:26:22+00:00
Did you close the wallet between creating and opening it ?


## mrx23dot | 2021-03-05T16:53:46+00:00
Nope, all I did is listed.
RPC seems super unreliable, despite running everything locally.
Why would executing a wallet creation take 20seconds? 1-2s maybe.
I'm not even connected to remote node, not running mining.
That's a lot of burden to put on an higher level application.

I wanted auto generate wallets via RPC, but it has to be done manually as I see.

Wallet is not open after creation.

## moneromooo-monero | 2021-03-05T17:35:20+00:00
You can run "sudo perf top -a" to see what your system is doing during that time. I just tried here, about 1.6 seconds.

## moneromooo-monero | 2021-03-05T23:44:03+00:00
Maybe it's just timing out on the daemon. When creating a wallet, it asks the daemon for the current height for example.

## mrx23dot | 2021-03-08T16:54:16+00:00
--offline solved it.

But after connected to remote node the RPC was unresponsive until it fully synced.
My RPC POST call timed out after 2minutes. Is that expected? 

> 2021-03-08 16:49:05.339 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:05.359 T READ ENDS: Success. bytes_tr: 10087
> 2021-03-08 16:49:05.766 D Pulled blocks: blocks_start_height 2292820, count 580, height 2293400, node height 2312630
> 2021-03-08 16:49:05.916 D Pulling blocks: start_height 0
> 2021-03-08 16:49:05.916 D Block is already in blockchain: 069e601117f8d13671e785663aabf7d9bd77f1921ead4adaa07e8c1e742b4b72
> 2021-03-08 16:49:33.091 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.123 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.174 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.189 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.189 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.362 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.405 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.483 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.504 T READ ENDS: Success. bytes_tr: 16384
> 2021-03-08 16:49:33.611 T READ ENDS: Success. bytes_tr: 16384
> ...



## moneromooo-monero | 2021-03-08T18:02:27+00:00
Yes.

## mrx23dot | 2021-03-08T18:38:38+00:00
That makes development any application that uses monero kinda awkward.
I saw RPC already uses 8 threads, can't we add one more that only handles RPC connection?

How does the Monero GUI connect to the backend, because it's able to query the progress of syncing.

## vtnerd | 2021-03-12T14:40:53+00:00
This is likely due to a lock in `core` being held for a while. [Poorman's profiler](https://poormansprofiler.org/) will help determine where its being stuck.

As per the GUI, its probably making a different API call that doesn't block.

## mrx23dot | 2021-03-12T15:53:04+00:00
That GDB inspection wouldn't work on my windows.
It won't even allow to connect to RPC server. So GUI must be using something else.

Can you connect to your RPC while it's syncing? Maybe it's only windows.

## selsta | 2021-10-06T02:36:38+00:00
#7760 should help with RPC becoming unresponsive but it's not clear if that's the issue you are seeing.

> Can you connect to your RPC while it's syncing?

Yes that should work fine.

## selsta | 2023-08-09T00:19:51+00:00
New versions of monero have a `--no-initial-sync` flag which should solve your issue.

https://github.com/monero-project/monero/pull/8355

# Action History
- Created by: mrx23dot | 2021-03-05T15:04:54+00:00
- Closed at: 2023-08-09T00:19:52+00:00
